##### Report GitHub Issue

Content selection saved. Describe the issue below:

# A Formal Comparison Between Chain of Thought and Latent Thought

###### Abstract

Chain of thought (CoT) elicits reasoning in large language models by explicitly generating intermediate tokens. In contrast, latent thought reasoning operates directly in the continuous latent space, enabling computation beyond discrete linguistic representations. While both approaches exploit iterative computation, their comparative capabilities remain underexplored. In this work, we present a formal analysis showing that latent thought admits more efficient parallel computation than inherently sequential CoT. In contrast, CoT enables approximate counting and sampling through stochastic decoding. These separations suggest the tasks for which depth-driven recursion is more suitable, thereby offering practical guidance for choosing between reasoning paradigms. Code is available at https://github.com/kevin671/cot-vs-loop .

###### Keywords:

## 1 Introduction

Transformer-based large language models (LLMs) ( Vaswani et al., 2017 ) have shown strong performance across diverse tasks and have recently been extended to complex reasoning. Rather than directly predicting final answers, generating intermediate reasoning steps, known as chain of thought (CoT) ( Wei et al., 2022 ) , enhances reasoning abilities. This naturally raises the question: why is CoT effective for complex tasks? Recent studies have approached this question by framing reasoning as a computational problem and analyzing its complexity ( Feng et al., 2023 ; Merrill and Sabharwal, 2024 ; Li et al., 2024 ; Nowak et al., 2024 ) , showing that CoT improves performance by increasing the model’s effective depth through iterative computation, thereby enabling the solution of problems that would otherwise be infeasible.

As an alternative to CoT, recent work has explored latent thought, which reasons directly in the hidden state space rather than in the discrete token space. This paradigm includes chain of continuous thought (Coconut) ( Hao et al., 2025 ) , which replaces next tokens with hidden state, and looped Transformer (looped TF) , in which output hidden states are iteratively fed back as inputs ( Dehghani et al., 2019 ) . Such iterative architectures have been shown to enhance expressivity: Coconut enables the simultaneous exploration of multiple traces ( Zhu et al., 2025a ; Gozeten et al., 2025 ) , while looped TF satisfies universality ( Giannou et al., 2023 ; Xu and Sato, 2025 ) and demonstrates competitive empirical performance ( Csordás et al., 2024 ; Bae et al., 2025 ; Zhu et al., 2025b ) .

These reasoning paradigms share the core idea of iteratively applying Transformers to enhance expressive power, which naturally leads to a fundamental question: What is the separation between chain of thought and latent thought? Recent studies characterize how expressivity scales with the number of iterations. Specifically, it has been shown that looped TF subsumes deterministic CoT ( Saunshi et al., 2025 ) , and exhibits a strict separation with only a logarithmic number of iterations ( Merrill and Sabharwal, 2025a ) . Nevertheless, fundamental questions remain open: Does the separation extend beyond the logarithmic regime? Is latent thought always more expressive than CoT?

### 1.1 Our Contributions

In this work, we address both questions by clarifying the respective strengths and limitations of the two reasoning paradigms through a formal complexity-theoretic analysis of their expressive power. Specifically, we show that latent thought gains efficiency from its parallelizability, yielding separations beyond the polylogarithmic regime. In contrast, CoT benefits from stochasticity, which enables approximate counting. An overview is given in Fig. 1 .

##### Latent thought enables parallel reasoning.

By formalizing decision problems as the evaluation of directed acyclic graphs (DAGs), we reveal the parallel computational capability of latent thought utilizing continuous hidden states. This analysis can be formalized by relating the class of decision problems realizable by the model to Boolean circuits. In particular, Boolean circuits composed of logic gates such as AND, OR, NOT, and Majority, with polylogarithmic depth log k ⁡ n \log^{k}n for k ∈ ℕ k\in\mathbb{N} and input size n n , define the class 𝖳𝖢 k \mathsf{TC}^{k} , a canonical model of parallel computation. Circuit complexity plays a central role in analyzing the computational power of Transformer models: fixed-depth Transformers without CoT are known to be upper-bounded by 𝖳𝖢 0 \mathsf{TC}^{0} ( Merrill and Sabharwal, 2023 ) , and subsequent studies analyze how the expressivity of CoT scales their computational power in terms of Boolean circuit complexity ( Li et al., 2024 ) . We show that latent thought with log k ⁡ n \log^{k}n iterations exactly captures the power of 𝖳𝖢 k \mathsf{TC}^{k} (Thm. 3.12 ); in contrast, CoT with log k ⁡ n \log^{k}n steps cannot realize the full power of 𝖳𝖢 k \mathsf{TC}^{k} (Thm. 3.13 ) due to its inherent sequentiality. This yields a strict separation in favor of latent thought in polylogarithmic regime (Thm. 3.15 ), showing its efficiency in terms of the required number of iterations.

##### CoT enables approximate counting.

A counting problem is a fundamental task in mathematics and computer science that determines the number of solutions satisfying a given set of constraints, including satisfying assignments of Boolean formulas, graph colorings, and partition functions ( Arora and Barak, 2009 ) . While exact counting for the complexity class # ​ 𝖯 \#\mathsf{P} is generally computationally intractable, approximation provides a feasible alternative. We show that CoT supports fully polynomial-time randomized approximation schemes ( 𝖥𝖯𝖱𝖠𝖲 \mathsf{FPRAS} ), yielding reliable estimates even in cases where exact counting via deterministic latent thought reasoning is intractable ( Lemma 4.3 ). Furthermore, leveraging classical results connecting approximate counting and sampling ( Jerrum et al., 1986 ) , we extend this separation to distribution modeling: there exist target distributions that CoT can approximately represent and sample from, but that remain inaccessible to latent thought ( Theorem 4.4 ). To the best of our knowledge, this constitutes the first formal separation in favor of CoT.

## 2 Background

### 2.1 Models of Computation

We define a class of reasoning paradigms in which a Transformer block ( Vaswani et al., 2017 ) is applied iteratively. Informally, CoT generates intermediate reasoning steps explicitly as tokens in an autoregressive manner. Formal definitions and illustrations are given in Appendix A .

###### Definition 2.1 (CoT, following Merrill and Sabharwal (2024) ) .

Let 𝒱 {\mathcal{V}} be a vocabulary, and let TF dec : 𝒱 ∗ → 𝒱 \mathrm{TF}_{\mathrm{dec}}:{\mathcal{V}}^{*}\to{\mathcal{V}} denote an decoder-only Transformer. Given an input sequence x = ( x 1 , … , x n ) ∈ 𝒱 n x=(x_{1},\dots,x_{n})\in{\mathcal{V}}^{n} , the outputs of CoT are defined by f cot 0 ​ ( x ) ≔ x , f cot k + 1 ​ ( x ) ≔ f cot k ​ ( x ) ⋅ TF dec ​ ( f cot k ​ ( x ) ) , f_{\mathrm{cot}}^{0}(x)\coloneq x,\quad f_{\mathrm{cot}}^{k+1}(x)\coloneq f_{\mathrm{cot}}^{k}(x)\cdot\mathrm{TF}_{\mathrm{dec}}(f_{\mathrm{cot}}^{k}(x)), where ⋅ \cdot denotes concatenation. We define the output to be the last tokens of f cot T ⁡ ( n ) ​ ( x ) ∈ 𝒱 n + T ⁡ ( n ) f_{\mathrm{cot}}^{T(n)}(x)\in{\mathcal{V}}^{\,n+T(n)} .

Coconut feeds the final hidden state as the embedding of the next token. Although the original Coconut model ( Hao et al., 2025 ) can generate both language tokens and hidden states, we focus exclusively on hidden state reasoning steps, in order to compare its representational power with that of CoT. Here, 𝔽 \mathbb{F} denotes the set of finite-precision floating-point numbers, and d ∈ ℕ d\in\mathbb{N} denotes the embedding dimension.

###### Definition 2.2 (Coconut) .

Let 𝒱 {\mathcal{V}} be a vocabulary and let TF dec Coconut : 𝒱 ∗ × ( 𝔽 d ) ∗ → 𝔽 d \mathrm{TF}^{\mathrm{Coconut}}_{\mathrm{dec}}:{\mathcal{V}}^{*}\times(\mathbb{F}^{d})^{*}\to\mathbb{F}^{d} be a decoder-only Transformer that maps a fixed token prefix together with a hidden state to the next hidden state. Given an input sequence x = ( x 1 , … , x n ) ∈ 𝒱 n x=(x_{1},\dots,x_{n})\in{\mathcal{V}}^{n} , we define the hidden states recursively by h 0 ≔ ( e ⁡ ( x i ) ) i = 1 n , h k + 1 ≔ TF dec Coconut ​ ( x , h k ) , h^{0}\coloneq\bigl(e(x_{i})\bigr)_{i=1}^{n},\quad h^{k+1}\coloneq\mathrm{TF}^{\mathrm{Coconut}}_{\mathrm{dec}}(x,h^{k}), where e : 𝒱 → 𝔽 d e:{\mathcal{V}}\to\mathbb{F}^{d} denotes an embedding. The output after T ⁡ ( n ) T(n) steps is obtained by decoding a suffix of the hidden state sequence ending at h T ⁡ ( n ) h^{T(n)} .

Looped TFs, by contrast, feed the entire model output back into the input without generating explicit tokens, recomputing all hidden states of the sequence at every iteration.

###### Definition 2.3 (Looped TF) .

Let TF : 𝔽 d × ∗ → 𝔽 d × ∗ \mathrm{TF}:\mathbb{F}^{d\times*}\to\mathbb{F}^{d\times*} denote a Transformer block. Given an input sequence x = ( x 1 , … , x n ) ∈ 𝒱 n x=(x_{1},\dots,x_{n})\in{\mathcal{V}}^{n} , the outputs are defined recursively by f loop 0 ​ ( x ) ≔ ( e ⁡ ( x i ) ) i = 1 n , f loop k + 1 ​ ( x ) ≔ TF ⁡ ( f loop k ​ ( x ) ) , f_{\mathrm{loop}}^{0}(x)\coloneq\bigl(e(x_{i})\bigr)_{i=1}^{n},\quad f_{\mathrm{loop}}^{k+1}(x)\coloneq\mathrm{TF}(f_{\mathrm{loop}}^{k}(x)), where e : 𝒱 → 𝔽 d e:{\mathcal{V}}\to\mathbb{F}^{d} denotes an embedding. The output after T ⁡ ( n ) T(n) loop iterations is the decoded last tokens of f loop T ⁡ ( n ) ​ ( x ) f_{\mathrm{loop}}^{T(n)}(x) .

Here, we assume that the input for looped TF may include sufficient padding so that its length is always at least as large as the output length, as in ( Merrill and Sabharwal, 2025b ) . The definitions of the models describe their core architectures; the specific details may vary depending on the tasks to which they are applied.

### 2.2 Related Work

To understand the expressive power of Transformers, previous work studies which classes of problems can be solved and with what computational efficiency. These questions can be naturally analyzed within the framework of computational complexity theory. Such studies on CoT and latent thought are summarized below and in Table 1 .

##### Computational power of chain of thought.

The expressivity of Transformers is limited by bounded depth ( Merrill and Sabharwal, 2023 ) , whereas CoT enhances their expressiveness by effectively increasing the number of sequential computational steps, enabling the solution of problems that would otherwise be intractable for fixed-depth architectures ( Feng et al., 2023 ) . Recent work has investigated how the expressivity of CoT scales with the number of reasoning steps, formalizing CoT for decision problems and computational complexity classes ( Merrill and Sabharwal, 2024 ; Li et al., 2024 ) . Beyond decision problems, CoT has been further formalized in a probabilistic setting for representing probability distributions over strings ( Nowak et al., 2024 ) .

##### Computational power of latent thought.

Latent thought is an alternative paradigm for increasing the number of computational steps without being constrained to the language space, with the potential to enhance model expressivity. In particular, Coconut has been shown to enable the simultaneous exploration of multiple candidate reasoning traces ( Zhu et al., 2025a ; Gozeten et al., 2025 ) . Looped TFs can simulate iterative algorithms ( Yang et al., 2024 ; de Luca and Fountoulakis, 2024 ) and, more generally, realize polynomial-time computations ( Giannou et al., 2023 ) . Recent results further demonstrate advantages over chain of thought reasoning: looped TFs can subsume the class of deterministic computations realizable by CoT using the same number of iterations ( Saunshi et al., 2025 ) , and exhibit a strict separation within the same logarithmic iterations ( Merrill and Sabharwal, 2025a ) . Concurrent work ( Zhu et al., 2025a ; Merrill and Sabharwal, 2025b ) has also identified connections between parallel reasoning and Coconut and diffusion models.

## 3 Latent Thought Enables Parallel Reasoning

We formalize the reasoning problem as a graph evaluation problem. Section 3.2 illustrates how each model approaches the same problem differently, providing intuitive insight into their contrasting capabilities. Building on these observations, Section 3.3 characterizes their expressive power and establishes a formal separation between them.

### 3.1 Problem Setting

Reasoning problems that can be solved by straight-line programs admit representations as directed acyclic graphs (DAGs) ( Aho and Ullman, 1972 ) , as illustrated in Fig. 2 (a).

###### Definition 3.1 (Computation graph) .

Let Σ \Sigma be a finite alphabet, and let ℱ \mathcal{F} denote a finite set of functions f : Σ ∗ → Σ f:\Sigma^{*}\to\Sigma . A computation graph is a directed acyclic graph G n = ( V n , E n ) G_{n}=(V_{n},E_{n}) that defines a function F G n : Σ n → Σ m ⁡ ( n ) F_{G_{n}}:\Sigma^{n}\to\Sigma^{m(n)} , where m ⁡ ( n ) m(n) denotes the output length. Here V n V_{n} denotes the set of nodes, consisting of (i) n n input nodes with in-degree 0 0 , (ii) function nodes labeled by f ∈ ℱ f\in\mathcal{F} , which take as arguments the predecessor nodes specified by their incoming edges in E n E_{n} , and (iii) m ⁡ ( n ) m(n) output nodes with out-degree 0 0 . The overall function is obtained by evaluating the graph in topological order. The size of the graph is | V n | |V_{n}| , denoted by size ⁡ ( G n ) \mathrm{size}(G_{n}) , and its depth is the length of the longest path from an input to an output node, denoted by depth ⁡ ( G n ) \mathrm{depth}(G_{n}) .

##### Assumptions on models.

Our goal is to evaluate the computational efficiency of each model via an asymptotic analysis of how the required number of reasoning steps or loops scales with the input size n n . Beyond time complexity , we also allow the space complexity of the model to scale with the input size n n . In particular, the embedding dimension in Transformer blocks can be viewed as analogous to the number of processors in classical parallel computation models. Accordingly, we adopt a non-uniform computational model, in which a different model is allowed for each input size. This non-uniform setting is standard in the study of circuit complexity and parallel computation ( Cook, 1985 ) , and is consistent with prior analyses of Transformers and CoT ( Sanford et al., 2024b ; Li et al., 2024 ) .

##### On the fairness of comparing steps and loops.

We analyze expressivity in terms of the number of reasoning steps. Although this may appear unfair in terms of raw computation, it is justified when comparing latency. Specifically, CoT benefits from KV caching, which makes each step computationally inexpensive; however, accessing cached states is typically memory-bound, leaving compute resources underutilized. In contrast, looped TFs recompute over the full sequence at each iteration, incurring higher arithmetic cost but achieving higher arithmetic intensity and better utilization of modern parallel hardware. As a result, the latency of looped TFs is comparable to that of CoT.

### 3.2 CoT Suffices with Size-scaled Steps and Latent Thought Suffices with Depth-scaled Iterations

We show how each model can evaluate DAGs, which provides a lower bound on their expressivity and offers intuition for the distinctions between the models, in terms of sequentiality and parallelizability. Before presenting our main result, we first state the underlying assumptions.

###### Definition 3.2 ( Merrill and Sabharwal, 2023 ) .

The model is log-precision , where each scalar is stored with O ⁡ ( log ⁡ n ) O(\log n) bits and every arithmetic operation is rounded to that precision.

###### Assumption 3.3 (Poly-size graph) .

size ⁡ ( G n ) ∈ 𝗉𝗈𝗅𝗒 ⁡ ( n ) \mathrm{size}(G_{n})\in\mathsf{poly}(n) .

###### Assumption 3.4 (Poly-efficient approximation, cf. ( Feng et al., 2023 ) ) .

Each node function of G n G_{n} can be approximated by a log-precision feedforward network whose parameter size is polynomial in the input length and the inverse of the approximation error. We denote by ff ​ _ ​ param ​ ( G n ) \mathrm{ff\_param}(G_{n}) an upper bound such that every f ∈ ℱ f\in\mathcal{F} admits such a network with at most ff ​ _ ​ param ​ ( G n ) \mathrm{ff\_param}(G_{n}) parameters.

Under these assumptions, we show that CoT can simulate computation by sequentially decoding nodes, where intermediate tokens serve as a scratchpad allowing the evaluation of each node once all its predecessors have been computed.

###### Theorem 3.5 (CoT for DAGs) .

Let { G n } n ∈ ℕ \{G_{n}\}_{n\in\mathbb{N}} be a family of computation graphs that satisfy Assumptions 3.3 and 3.4 . Then, for each n ∈ ℕ n\in\mathbb{N} , there exists a log-precision CoT with parameter size bounded by O ⁡ ( ff ​ _ ​ param ​ ( G n ) ) O(\mathrm{ff\_param}(G_{n})) , such that for every input x ∈ Σ n x\in\Sigma^{n} , the model outputs F G n ​ ( x ) F_{G_{n}}(x) with steps proportional to the “size” of the graph, i.e., O ⁡ ( size ⁡ ( G n ) ) O(\mathrm{size}(G_{n})) .

###### Proof sketch.

At each step, the attention layer retrieves the outputs of predecessor nodes from previously generated tokens, and a feed-forward layer then computes the node function, whose output is generated as the next token. ∎

In contrast, latent thought can operate in parallel, layer by layer, where all nodes at the same depth are computed simultaneously, provided that the model has sufficient size.

###### Theorem 3.6 (Latent thought for DAGs) .

Let { G n } n ∈ ℕ \{G_{n}\}_{n\in\mathbb{N}} be a family of computation graphs that satisfy Assumptions 3.3 and 3.4 . Then, for each n ∈ ℕ n\in\mathbb{N} , there exists a log-precision Coconut and looped TF with parameter size O ⁡ ( ff ​ _ ​ param ​ ( G n ) ⋅ size ⁡ ( G n ) ) O(\mathrm{ff\_param}(G_{n})\cdot\mathrm{size}(G_{n})) , such that for every input x ∈ Σ n x\in\Sigma^{n} , it computes F G n ​ ( x ) F_{G_{n}}(x) with iterations proportional to the “depth” of the graph G n G_{n} , i.e., O ⁡ ( depth ⁡ ( G n ) ) O(\mathrm{depth}(G_{n})) .

###### Proof sketch.

The role assignment of each layer is based on ( Li et al., 2024 ) , as shown in Figure 9 . An attention layer aggregates its inputs into a single hidden state. Unlike discrete tokens, continuous latent states allow the simultaneous encoding of the outputs of multiple nodes, enabling the feed-forward layer to compute node functions in parallel. ∎

##### Remark.

Illustrations are provided in Fig. 2 , with formal proofs deferred to Appendix B . These results reveal distinct characteristics: CoT can utilize intermediate steps as scratchpad memory and perform computations sequentially, whereas latent thought can leverage structural parallelism to achieve greater efficiency with sufficient resources.

### 3.3 Separation in Polylogarithmic Iterations

In this section, we shift to formal decision problems to precisely characterize the computational power of each reasoning paradigm, clarify what cannot be achieved, and use these limitations to derive rigorous separations. We begin by defining their complexity classes, as in ( Li et al., 2024 ) .

###### Definition 3.7 (Complexity Classes 𝖢𝗈𝖳 \mathsf{CoT} , 𝖢𝖳 \mathsf{CT} and 𝖫𝗈𝗈𝗉 \mathsf{Loop} ) .

Let 𝖢𝗈𝖳 ⁡ [ T ⁡ ( n ) , d ⁡ ( n ) , s ⁡ ( n ) ] \mathsf{CoT}[T(n),d(n),s(n)] , 𝖢𝖳 ⁡ [ T ⁡ ( n ) , d ⁡ ( n ) , s ⁡ ( n ) ] \mathsf{CT}[T(n),d(n),s(n)] , and 𝖫𝗈𝗈𝗉 ⁡ [ T ⁡ ( n ) , d ⁡ ( n ) , s ⁡ ( n ) ] \mathsf{Loop}[T(n),d(n),s(n)] denote the sets of languages ℒ : { 0 , 1 } ∗ → { 0 , 1 } {\mathcal{L}}:\{0,1\}^{*}\to\{0,1\} for which there exists a deterministic CoT, Coconut, and looped TF, respectively, denoted by M n M_{n} for each input size n n , with embedding size O ⁡ ( d ⁡ ( n ) ) O(d(n)) and O ⁡ ( s ⁡ ( n ) ) O(s(n)) bits of precision, such that for all x ∈ { 0 , 1 } n x\in\{0,1\}^{n} , the final output token after O ⁡ ( T ⁡ ( n ) ) O(T(n)) iterations equals ℒ ⁡ ( x ) {\mathcal{L}}(x) .

Boolean circuits serve as a standard formal model of computation, where processes are defined by the evaluation of DAGs with well-established complexity measures.

###### Definition 3.8 (Informal) .

A Boolean circuit is a DAG over the alphabet Σ = { 0 , 1 } \Sigma=\{0,1\} , where each internal node (gate) computes a Boolean function such as AND, OR, or NOT. 𝖲𝖨𝖹𝖤 ⁡ [ s ⁡ ( n ) ] \mathsf{SIZE}[s(n)] and 𝖣𝖤𝖯𝖳𝖧 ⁡ [ d ⁡ ( n ) ] \mathsf{DEPTH}[d(n)] denote the class of languages decidable by a non-uniform circuit family { C n } \{C_{n}\} with size O ⁡ ( s ⁡ ( n ) ) O(s(n)) and depth O ⁡ ( d ⁡ ( n ) ) O(d(n)) , respectively.

First, we formalize the results of the previous section to show that latent thought iterations can represent circuit depth, whereas CoT corresponds to circuit size.

###### Theorem 3.9 ( Li et al., 2024 ) .

∀ T ⁡ ( n ) ∈ poly ⁡ ( n ) , \forall T(n)\in\mathrm{poly}(n), 𝖲𝖨𝖹𝖤 ⁡ [ T ⁡ ( n ) ] ⊆ 𝖢𝗈𝖳 ⁡ [ T ⁡ ( n ) , log ⁡ n , 1 ] . \mathsf{SIZE}[T(n)]\subseteq\mathsf{CoT}[T(n),\log{n},1].

###### Theorem 3.10 .

For any function T ⁡ ( n ) ∈ poly ⁡ ( n ) T(n)\in\mathrm{poly}(n) and any non-uniform circuit family { C n } \{C_{n}\} , it holds that 𝖣𝖤𝖯𝖳𝖧 ⁡ [ T ⁡ ( n ) ] \displaystyle\mathsf{DEPTH}[T(n)] ⊆ 𝖫𝗈𝗈𝗉 ⁡ [ T ⁡ ( n ) , size ⁡ ( C n ) , 1 ] , \displaystyle\subseteq\mathsf{Loop}[T(n),\mathrm{size}(C_{n}),1], 𝖣𝖤𝖯𝖳𝖧 ⁡ [ T ⁡ ( n ) ] \displaystyle\mathsf{DEPTH}[T(n)] ⊆ 𝖢𝖳 ⁡ [ T ⁡ ( n ) , size ⁡ ( C n ) , 1 ] . \displaystyle\subseteq\mathsf{CT}[T(n),\mathrm{size}(C_{n}),1].

Boolean circuits serve as a formal model of parallel computations that run in polylogarithmic time using a polynomial number of processors ( Stockmeyer and Vishkin, 1984 ) .

###### Definition 3.11 .

For each k ∈ ℕ k\in\mathbb{N} , the classes 𝖭𝖢 k \mathsf{NC}^{k} , 𝖠𝖢 k \mathsf{AC}^{k} , and 𝖳𝖢 k \mathsf{TC}^{k} consist of languages decidable by non-uniform circuit families of size 𝗉𝗈𝗅𝗒 ⁡ ( n ) \mathsf{poly}(n) and depth O ⁡ ( log k ⁡ n ) O(\log^{k}n) , using bounded-fanin Boolean gates, unbounded-fanin 𝖠𝖭𝖣 \mathsf{AND} / 𝖮𝖱 \mathsf{OR} gates, and threshold gates, respectively.

We then characterize the exact computational power of latent thought in the parallel computation regime.

###### Theorem 3.12 .

For each k ∈ ℕ , k\in\mathbb{N}, it holds that 𝖫𝗈𝗈𝗉 [ log k n , 𝗉𝗈𝗅𝗒 ( n ) , 1 (resp. log n ) ] \displaystyle\mathsf{Loop}[\log^{k}n,\,\mathsf{poly}(n),\,1\ \textup{(resp.\ }\log n)] = 𝖢𝖳 [ log k n , 𝗉𝗈𝗅𝗒 ( n ) , 1 (resp. log n ) ] \displaystyle=\mathsf{CT}[\log^{k}n,\,\mathsf{poly}(n),\,1\ \textup{(resp.\ }\log n)] = 𝖠𝖢 k ​ ( resp. ​ 𝖳𝖢 k ) . \displaystyle=\mathsf{AC}^{k}\ (\textup{resp.\ }\mathsf{TC}^{k}).

###### Proof sketch.

The inclusion from circuits to latent thought follows from Theorem 3.10 . For the converse inclusion, we build on the arguments of prior work ( Merrill and Sabharwal, 2023 ; Li et al., 2024 ) , which show that a fixed-depth Transformer block under finite precision is contained in 𝖠𝖢 0 \mathsf{AC}^{0} (or 𝖳𝖢 0 \mathsf{TC}^{0} under logarithmic precision). We extend their analysis to the looped setting, which can be unrolled into a 𝖳𝖢 k \mathsf{TC}^{k} circuit by composing a 𝖳𝖢 0 \mathsf{TC}^{0} block for log k ⁡ n \log^{k}n iterations. ∎

Moreover, we establish an upper bound on the power of CoT in the parallel computation regime. This limitation arises from the inherently sequential nature of CoT.

###### Lemma 3.13 .

For each k ∈ ℕ , k\in\mathbb{N}, it holds that 𝖢𝗈𝖳 ⁡ [ log k ⁡ n , 𝗉𝗈𝗅𝗒 ⁡ ( n ) , log ⁡ n ] ⊆ 𝖳𝖢 k − 1 . \mathsf{CoT}[\log^{k}{n},\mathsf{poly}(n),\log{n}]\subseteq\mathsf{TC}^{k-1}.

###### Proof.

The total log k ⁡ n \log^{k}n steps can be divided into log k − 1 ⁡ n \log^{k-1}n blocks, each consisting of log ⁡ n \log n steps. Since 𝖢𝗈𝖳 ⁡ [ log ⁡ n , 𝗉𝗈𝗅𝗒 ⁡ ( n ) , log ⁡ n ] ⊆ 𝖳𝖢 0 \mathsf{CoT}[\log n,\mathsf{poly}(n),\log n]\subseteq\mathsf{TC}^{0} ( Li et al., 2024 ) , each block with the previous block’s outputs fed as inputs to the next block can be simulated in 𝖳𝖢 0 \mathsf{TC}^{0} ; iterating this over log k − 1 ⁡ n \log^{k-1}n layers yields a circuit in 𝖳𝖢 k − 1 \mathsf{TC}^{k-1} . ∎

These results lead to a separation in expressive power under standard complexity assumptions, as illustrated in Figure 3 .

###### Theorem 3.14 .

For each k ∈ ℕ k\in\mathbb{N} , if 𝖳𝖢 k − 1 ⊊ 𝖭𝖢 k \mathsf{TC}^{k-1}\subsetneq\mathsf{NC}^{k} , then 𝖢𝗈𝖳 ⁡ [ log k ⁡ n , 𝗉𝗈𝗅𝗒 ⁡ ( n ) , log ⁡ n ] \displaystyle\mathsf{CoT}[\log^{k}n,\mathsf{poly}(n),\log{n}] ⊊ 𝖫𝗈𝗈𝗉 ⁡ [ log k ⁡ n , 𝗉𝗈𝗅𝗒 ⁡ ( n ) , 1 ] , \displaystyle\subsetneq\mathsf{Loop}[\log^{k}n,\mathsf{poly}(n),1], 𝖢𝗈𝖳 ⁡ [ log k ⁡ n , 𝗉𝗈𝗅𝗒 ⁡ ( n ) , log ⁡ n ] \displaystyle\mathsf{CoT}[\log^{k}n,\mathsf{poly}(n),\log{n}] ⊊ 𝖢𝖳 ⁡ [ log k ⁡ n , 𝗉𝗈𝗅𝗒 ⁡ ( n ) , 1 ] . \displaystyle\subsetneq\mathsf{CT}[\log^{k}n,\mathsf{poly}(n),1].

###### Theorem 3.15 .

For each k ∈ ℕ k\in\mathbb{N} , if 𝖳𝖢 k − 1 ⊊ 𝖳𝖢 k \mathsf{TC}^{k-1}\subsetneq\mathsf{TC}^{k} , then 𝖢𝗈𝖳 ⁡ [ log k ⁡ n , 𝗉𝗈𝗅𝗒 ⁡ ( n ) , log ⁡ n ] \displaystyle\mathsf{CoT}[\log^{k}n,\mathsf{poly}(n),\log n] ⊊ 𝖫𝗈𝗈𝗉 ⁡ [ log k ⁡ n , 𝗉𝗈𝗅𝗒 ⁡ ( n ) , log ⁡ n ] , \displaystyle\subsetneq\mathsf{Loop}[\log^{k}n,\mathsf{poly}(n),\log n], 𝖢𝗈𝖳 ⁡ [ log k ⁡ n , 𝗉𝗈𝗅𝗒 ⁡ ( n ) , log ⁡ n ] \displaystyle\mathsf{CoT}[\log^{k}n,\mathsf{poly}(n),\log n] ⊊ 𝖢𝖳 ⁡ [ log k ⁡ n , 𝗉𝗈𝗅𝗒 ⁡ ( n ) , log ⁡ n ] . \displaystyle\subsetneq\mathsf{CT}[\log^{k}n,\mathsf{poly}(n),\log n].

##### Remark.

The claims follow directly from Theorem 3.12 and Lemma 3.13 . The established separations of the complexity classes, as summarized in Fig. 3 , show that latent thought reasoning enables efficient parallel solutions more effectively than CoT, which is inherently sequential.

## 4 CoT Enables Approximate Counting

In the previous section, we showed that for decision problems, latent thought can yield more efficient solutions than CoT. This naturally raises the question of whether latent thought is universally more powerful than CoT. While prior work has shown that CoT can be simulated by looped Transformer models for deterministic decision problems under deterministic decoding ( Saunshi et al., 2025 ) , we found that this result does not directly extend to probabilistic settings with stochastic decoding. Accordingly, we shift our focus from efficiency in terms of the number of reasoning steps to expressive capability under polynomially many iterations.

### 4.1 Preliminaries

##### Approximate counting.

Formally, let Σ \Sigma be a finite alphabet and let R ⊆ Σ ∗ × Σ ∗ R\subseteq\Sigma^{*}\times\Sigma^{*} be a relation. For an input x ∈ Σ ∗ x\in\Sigma^{*} , define R ⁡ ( x ) := { y ∈ Σ ∗ ∣ ( x , y ) ∈ R } , R(x):=\{\,y\in\Sigma^{*}\mid(x,y)\in R\,\}, and the counting problem is to determine | R ⁡ ( x ) | |R(x)| . A wide class of natural relations admits a recursive structure, which allows solutions to be constructed from smaller subproblems.

###### Definition 4.1 (Informal: Self-reducibility ( Schnorr, 1976 ) ) .

A relation R R is self-reducible if there exists a polynomial-time procedure that, given any input x x and prefix y 1 : k y_{1:k} (with respect to a fixed output order), produces a sub-instance ψ ( x , y 1 : k ) \psi(x,y_{1:k}) such that every solution z z of ψ ( x , y 1 : k ) \psi(x,y_{1:k}) extends y 1 : k y_{1:k} to a solution of R ⁡ ( x ) R(x) (and conversely), i.e., R ( ψ ( x , y 1 : k ) ) = { z ∣ concat ( y 1 : k , z ) ∈ R ( x ) } . R\bigl(\psi(x,y_{1:k})\bigr)=\{z\mid\ \mathrm{concat}(y_{1:k},z)\in R(x)\,\}.

While exact counting is intractable, there exist efficient randomized approximation algorithms ( Karp and Luby, 1983 ) .

###### Definition 4.2 (FPRAS) .

An algorithm is called a fully polynomial-time randomized approximation scheme (FPRAS) for a function f f if, for any ε > 0 \varepsilon>0 and δ > 0 \delta>0 , it outputs an estimate f ^ ​ ( x ) \hat{f}(x) such that Pr [ ( 1 − ε ) f ( x ) ≤ f ^ ( x ) ≤ ( 1 + ε ) f ( x ) ] ≥ 1 − δ , \Pr\!\left[(1-\varepsilon)f(x)\leq\hat{f}(x)\leq(1+\varepsilon)f(x)\right]\geq 1-\delta, and runs in time polynomial in | x | |x| , 1 / ε 1/\varepsilon , and log ⁡ ( 1 / δ ) \log(1/\delta) .

The class of counting problems that admit an FPRAS is denoted by 𝖥𝖯𝖱𝖠𝖲 \mathsf{FPRAS} . Although randomized algorithms provide only probabilistic guarantees, they are often both more efficient and simpler than their deterministic counterparts, denoted by 𝖥𝖯𝖳𝖠𝖲 \mathsf{FPTAS} ( Definition C.11 ). For example, counting the number of satisfying assignments of a DNF formula admits an FPRAS based on Monte Carlo methods ( Karp et al., 1989 ) , whereas no FPTAS is known for this problem. Moreover, probabilistic analysis enables us to capture algorithmic behavior on typical instances arising in real-world applications ( Mitzenmacher and Upfal, 2017 ) .

##### Probabilistic models of computation.

In contrast to the deterministic models considered in the previous section, we now study probabilistic models that define a conditional distribution over output strings y = ( y 1 , … , y m ) ∈ Σ ∗ y=(y_{1},\ldots,y_{m})\in\Sigma^{*} . We consider autoregressive next-token prediction of the form p ⁡ ( y ∣ x ) = ∏ i = 1 m p ⁡ ( y i ∣ x , y < i ) , p(y\mid x)=\prod_{i=1}^{m}p(y_{i}\mid x,y_{<i}), where the model is allowed to perform additional reasoning steps before producing each output token y i y_{i} . This formulation was first used to formalize CoT for language modeling by Nowak et al. (2024) . We also allow stochastic decoding for latent reasoning at the token level: reasoning iterations are performed entirely in hidden space and no linguistic tokens are sampled except for the output token y i y_{i} , as illustrated in Fig. 4 . This definition is consistent with practical implementations ( Csordás et al., 2024 ; Bae et al., 2025 ) . Within this framework, we define complexity classes of probabilistic models, denoted by 𝗉𝖢𝗈𝖳 \mathsf{pCoT} , 𝗉𝖢𝖳 \mathsf{pCT} , and 𝗉𝖫𝗈𝗈𝗉 \mathsf{pLoop} , respectively. Formal definitions are in Section C.1 .

### 4.2 Separation in Approximate Counting

We first analyze the expressivity of the token-level conditional prediction at each step, p ⁡ ( y i ∣ x , y < i ) p(y_{i}\mid x,y_{<i}) , and show that CoT is strictly more expressive than latent thought in this setting. The key distinction is whether intermediate computation permits sampling. CoT explicitly samples intermediate reasoning tokens, inducing stochastic computation and enabling the emulation of randomized algorithms. In contrast, latent thought performs only deterministic transformations in latent space, resulting in deterministic computation.

###### Lemma 4.3 (Informal) .

Assume that 𝖥𝖯𝖳𝖠𝖲 ⊊ 𝖥𝖯𝖱𝖠𝖲 \mathsf{FPTAS}\subsetneq\mathsf{FPRAS} for self-reducible relations. There exists a self-reducible relation R R and an associated function f : Σ ∗ × Σ ∗ → ℕ f:\Sigma^{*}\times\Sigma^{*}\to\mathbb{N} defined by f ⁡ ( x , y < i ) ≔ | { z ∈ Σ ∗ : ( x , y < i ​ z ) ∈ R } | f(x,y_{<i})\coloneqq|\{\,z\in\Sigma^{*}:(x,y_{<i}z)\in R\,\}| such that CoT with polynomially many steps admits an FPRAS for f f . Whereas, no latent thought with polynomially many iterations admits the same approximation guarantee.

###### Proof sketch.

For self-reducible relations, approximating the counting function f f on subproblems is polynomial-time inter-reducible with approximating | R ⁡ ( x ) | |R(x)| ( Jerrum et al., 1986 ) . If latent thought with polynomially many iterations admitted an FPTAS for f f , then it would induce a deterministic FPTAS for | R ⁡ ( x ) | |R(x)| , contradicting the assumption.∎

### 4.3 Separation in Approximate Sampling

We then move from token-level conditional distributions p ⁡ ( y i ∣ x , y < i ) p(y_{i}\mid x,y_{<i}) to the full sequence-level distribution p ⁡ ( y ∣ x ) p(y\mid x) . Beyond approximate counting, we establish a separation for approximate sampling problems. Specifically, we construct target distributions for which the complexity of each conditional can be reduced to approximate counting.

###### Theorem 4.4 .

Assume that 𝖥𝖯𝖳𝖠𝖲 ⊊ 𝖥𝖯𝖱𝖠𝖲 \mathsf{FPTAS}\subsetneq\mathsf{FPRAS} for self-reducible relations. There exists a distribution p ⁡ ( y ∣ x ) p(y\mid x) over y ∈ Σ ∗ y\in\Sigma^{*} and x ∈ Σ n x\in\Sigma^{n} such that a CoT with a polynomial number of steps, whose induced output conditionals are denoted by q ⁡ ( y i ∣ x , y < i ) q(y_{i}\mid x,y_{<i}) , admits an FPRAS for approximating the conditional probabilities p ⁡ ( y i ∣ x , y < i ) p(y_{i}\mid x,y_{<i}) for all x ∈ Σ n x\in\Sigma^{n} , indices i ≥ 1 i\geq 1 , and prefixes y < i ≔ ( y 1 , … , y i − 1 ) y_{<i}\coloneq(y_{1},\ldots,y_{i-1}) . In contrast, no latent thought with polynomially many iterations admits the same approximation guarantee.

###### Proof sketch.

Define the target distribution p p to be the uniform distribution supported on the solution set R ⁡ ( x ) R(x) . We rely on the classical result that approximate sampling from the uniform distribution over solutions, captured by the class 𝖥𝖯𝖠𝖴𝖲 \mathsf{FPAUS} , is polynomial-time inter-reducible with approximate counting for self-reducible relations ( Jerrum et al., 1986 ) . Let U ( ⋅ ∣ x ) U(\cdot\mid x) denote the uniform distribution over solutions of a self-reducible relation R ⁡ ( x ) R(x) . This distribution admits an autoregressive factorization U ⁡ ( y ∣ x ) = ∏ i = 1 m p ⁡ ( y i ∣ x , y < i ) , U(y\mid x)\;=\;\prod_{i=1}^{m}p(y_{i}\mid x,y_{<i}), where each conditional probability is given by p ( y i ∣ x , y < i ) = | { z ∈ Σ ∗ : ( x , y 1 : i + 1 z ) ∈ R } | | { z ∈ Σ ∗ : ( x , y 1 : i z ) ∈ R } | . p(y_{i}\mid x,y_{<i})=\frac{\bigl|\{\,z\in\Sigma^{*}:(x,y_{1:i+1}z)\in R\,\}\bigr|}{\bigl|\{\,z\in\Sigma^{*}:(x,y_{1:i}z)\in R\,\}\bigr|}. We show that each conditional probability, expressed as a ratio of subproblem counts, reduces to approximate counting. Then, applying Lemma 4.3 to these conditionals yields the desired separation for approximate sampling. ∎

Consequently, we obtain the following separations in favor of CoT, as also shown in Fig. 5 .

###### Theorem 4.5 .

Assuming 𝖥𝖯𝖳𝖠𝖲 ⊊ 𝖥𝖯𝖱𝖠𝖲 \mathsf{FPTAS}\subsetneq\mathsf{FPRAS} for self-reducible relations, it holds that ∀ ℳ ∈ { 𝗉𝖢𝖳 , 𝗉𝖫𝗈𝗈𝗉 } , ℳ ⁡ [ 𝗉𝗈𝗅𝗒 ⁡ ( n ) ] ⊊ 𝗉𝖢𝗈𝖳 ⁡ [ 𝗉𝗈𝗅𝗒 ⁡ ( n ) ] . \forall\,\mathcal{M}\in\{\mathsf{pCT},\mathsf{pLoop}\},\quad\mathcal{M}[\mathsf{poly}(n)]\subsetneq\mathsf{pCoT}[\mathsf{poly}(n)].

## 5 Experiments

In this section, we provide empirical validation of our theoretical results on tasks with well-characterized complexity. Specifically, we study parallelizable tasks to empirically validate the efficiency of latent thought predicted in Section 3 , and approximate counting and sampling tasks to demonstrate the effectiveness of CoT as shown in Section 4 .

### 5.1 Experimental Setting

##### Fundamental algorithmic reasoning tasks.

We use four problems. (1) Word problems for finite non-solvable groups: given a sequence of generators, the task is to evaluate their composition, which is 𝖭𝖢 1 \mathsf{NC}^{1} -complete ( Barrington, 1986 ) , also studied for Looped TF ( Merrill and Sabharwal, 2025a ) . (2) s s – t t connectivity (STCON): given a directed graph G = ( V , E ) G=(V,E) and two vertices s , t ∈ V s,t\in V , the task is to decide whether t t is reachable from s s , which belongs to 𝖳𝖢 1 \mathsf{TC}^{1} ( Gibbons and Rytter, 1989 ) . (3) Arithmetic expression evaluation: given a formula consisting of + , × , − , / +,\times,-,/ operations on integers, the task is to evaluate it. This problem is 𝖳𝖢 0 \mathsf{TC}^{0} -reducible to Boolean formula evaluation ( Feng et al., 2023 ) , which is 𝖭𝖢 1 \mathsf{NC}^{1} -complete ( Buss, 1987 ) . (4) Edit distance: given two strings x x and y y , the task is to compute the minimum cost to transform x x into y y . By reducing the dynamic programming formulation to shortest paths, this problem is in 𝖳𝖢 1 \mathsf{TC}^{1} ( Apostolico et al., 1990 ) .

##### Approximate counting tasks.

We consider DNF counting and uniform sampling of graph colorings, both of which admit fully polynomial randomized approximation schemes for counting and sampling (FPRAS and FPAUS). Specifically, DNF counting admits an FPRAS via Monte Carlo sampling ( Karp et al., 1989 ) , while approximate counting and sampling of graph colorings admit an FPAUS based on rapidly mixing Markov chain Monte Carlo under suitable degree and color constraints ( Jerrum, 1995 ) .

##### Training strategy.

Since our primary objective is to study expressive power, we allow flexibility in optimization and training strategies. For CoT models, training is performed with supervision from explicit sequential algorithms. For fewer CoT steps, we compare two strategies: uniformly selecting steps from the indices of the complete trajectory ( Bavandpour et al., 2025 ) , and stepwise internalization (distillation) methods ( Deng et al., 2024 ) . For latent thought, we observe that looped TF is easier to train than Coconut, and therefore adopt looped TF as our instantiation of latent thought, with curriculum learning applied to certain tasks.

### 5.2 Results

Table 2 reports results on parallelizable tasks, comparing latent thought and CoT under varying numbers of iterations. Latent thought solves the problems with fewer iterations than CoT requires to reach comparable performance. These empirical results are consistent with our theoretical analysis: latent thought supports efficient parallel reasoning, in contrast to the inherently sequential nature of CoT.

We also evaluate the relationship between performance, input size, and the number of iterations, as in prior studies ( Sanford et al., 2024b ; Merrill and Sabharwal, 2025a ) . Figure 6 presents our results for looped TFs, illustrating that as the input size n n increases, the number of loops required to maintain high accuracy grows only logarithmically, supporting our theoretical claim in the (poly-)logarithmic regime.

Figure 7 shows the results on the approximate counting or sampling tasks. For approximate counting, CoT performs Monte Carlo estimation: the effective number of samples is given by the product of the number of reasoning steps per trial and the number of independent trials. The probability mass plot illustrates how the empirical distribution over valid colorings compares to the target uniform distribution. We observe that CoT produces a distribution that is closer to uniform, whereas the looped model concentrates probability mass on a smaller subset of solutions. This indicates that CoT achieves more uniform coverage of the valid colorings.

## 6 Conclusion

We formally analyze the computational capabilities of chain-of-thought and latent thought reasoning, providing a rigorous comparison that reveals their respective strengths and limitations. Specifically, we show that latent thought enables efficient parallel computation, whereas CoT enables randomized approximate counting.Our results provide practical guidance for selecting between reasoning paradigms: latent reasoning is more suitable for problems that can be solved efficiently, whereas CoT is more effective for more complex problems. For future work, an important direction is to investigate whether techniques such as distillation can reduce the number of iterations without compromising computational power. Another promising avenue is to extend our analysis to diffusion language models, which possess both parallelizability and stochasticity. Moreover, extending the analysis to realistic downstream tasks remains an important direction.

## Impact Statement

This paper presents work whose goal is to advance the field of Machine Learning. There are many potential societal consequences of our work, none which we feel must be specifically highlighted here.

## References

Aho and Ullman (1972) A. V. Aho and J. D. Ullman Optimization of straight line programs . SIAM Journal on Computing 1 ( 1 ), pp. 1–19 . Cited by: §3.1 .

Apostolico et al. (1990) A. Apostolico, M. J. Atallah, L. L. Larmore, and S. McFaddin Efficient parallel algorithms for string editing and related problems . SIAM Journal on Computing . Cited by: §5.1 .

Arora and Barak (2009) S. Arora and B. Barak Computational complexity: a modern approach . Cambridge University Press . Cited by: §1.1 .

Bae et al. (2025) S. Bae, Y. Kim, R. Bayat, S. Kim, J. Ha, T. Schuster, A. Fisch, H. Harutyunyan, Z. Ji, A. Courville, et al. Mixture-of-recursions: learning dynamic recursive depths for adaptive token-level computation . arXiv preprint arXiv:2507.10524 . Cited by: §1 , §4.1 .

Barrington (1986) D. A. Barrington Bounded-width polynomial-size branching programs recognize exactly those languages in nc . In ACM symposium on Theory of computing , Cited by: §5.1 .

Bavandpour et al. (2025) A. A. Bavandpour, X. Huang, M. Rofin, and M. Hahn Lower bounds for chain-of-thought reasoning in hard-attention transformers . In Forty-second International Conference on Machine Learning , External Links: Link Cited by: §D.1.2 , §D.1.2 , §5.1 .

Buss (1987) S. R. Buss The boolean formula value problem is in ALOGTIME . In Proceedings of the nineteenth annual ACM symposium on Theory of computing , pp. 123–131 . Cited by: §5.1 .

Cook (1985) S. A. Cook A taxonomy of problems with fast parallel algorithms . Information and control 64 ( 1-3 ), pp. 2–22 . Cited by: §3.1 .

Csordás et al. (2024) R. Csordás, K. Irie, J. Schmidhuber, C. Potts, and C. D. Manning MoEUT: mixture-of-experts universal transformers . In The Thirty-eighth Annual Conference on Neural Information Processing Systems , External Links: Link Cited by: §1 , §4.1 .

de Luca and Fountoulakis (2024) A. B. de Luca and K. Fountoulakis Simulation of graph algorithms with looped transformers . In Forty-first International Conference on Machine Learning , External Links: Link Cited by: §2.2 .

Dehghani et al. (2019) M. Dehghani, S. Gouws, O. Vinyals, J. Uszkoreit, and L. Kaiser Universal transformers . In International Conference on Learning Representations , External Links: Link Cited by: §1 .

Deng et al. (2024) Y. Deng, Y. Choi, and S. Shieber From explicit cot to implicit cot: learning to internalize cot step by step . arXiv preprint arXiv:2405.14838 . Cited by: §D.1.2 , §5.1 .

Erdos and Renyi (1959) P. Erdos and A. Renyi On random graphs i . Publ. math. debrecen 6 ( 290-297 ), pp. 18 . Cited by: §D.1.1 .

Feng et al. (2023) G. Feng, B. Zhang, Y. Gu, H. Ye, D. He, and L. Wang Towards revealing the mystery behind chain of thought: a theoretical perspective . Advances in Neural Information Processing Systems 36 , pp. 70757–70798 . Cited by: §B.2 , §D.1.1 , §D.1.1 , §D.1.2 , §1 , §2.2 , Assumption 3.4 , §5.1 .

Giannou et al. (2023) A. Giannou, S. Rajput, J. Sohn, K. Lee, J. D. Lee, and D. Papailiopoulos Looped transformers as programmable computers . In International Conference on Machine Learning , pp. 11398–11442 . Cited by: §1 , §2.2 .

Gibbons and Rytter (1989) A. Gibbons and W. Rytter Efficient parallel algorithms . Cambridge University Press . Cited by: §5.1 .

Gozeten et al. (2025) H. A. Gozeten, M. E. Ildiz, X. Zhang, H. Harutyunyan, A. S. Rawat, and S. Oymak Continuous chain of thought enables parallel exploration and reasoning . arXiv preprint arXiv:2505.23648 . Cited by: §1 , §2.2 , Table 1 .

Hao et al. (2025) S. Hao, S. Sukhbaatar, D. Su, X. Li, Z. Hu, J. E. Weston, and Y. Tian Training large language models to reason in a continuous latent space . In Second Conference on Language Modeling , External Links: Link Cited by: §1 , §2.1 .

Jerrum et al. (1986) M. R. Jerrum, L. G. Valiant, and V. V. Vazirani Random generation of combinatorial structures from a uniform distribution . Theoretical computer science 43 , pp. 169–188 . Cited by: Proposition C.13 , Proposition C.16 , Theorem C.19 , §1.1 , §4.2 , §4.3 .

Jerrum (1995) M. Jerrum A very simple algorithm for estimating the number of k-colorings of a low-degree graph . Random Structures & Algorithms 7 ( 2 ), pp. 157–165 . Cited by: §D.2.2 , §5.1 .

Karp et al. (1989) R. M. Karp, M. Luby, and N. Madras Monte-carlo approximation algorithms for enumeration problems . Journal of algorithms 10 ( 3 ), pp. 429–448 . Cited by: §4.1 , §5.1 .

Karp and Luby (1983) R. M. Karp and M. Luby Monte-carlo algorithms for enumeration and reliability problems . In 24th Annual Symposium on Foundations of Computer Science , pp. 56–64 . Cited by: §D.2.1 , §4.1 .

Li et al. (2024) Z. Li, H. Liu, D. Zhou, and T. Ma Chain of thought empowers transformers to solve inherently serial problems . In The Twelfth International Conference on Learning Representations , External Links: Link Cited by: §B.1 , §B.3.1 , §B.7 , Definition B.1 , Lemma B.10 , Definition B.2 , Definition B.3 , Lemma B.5 , Theorem B.9 , §1.1 , §1 , §2.2 , Table 1 , §3.1 , §3.2 , §3.3 , §3.3 , §3.3 , Theorem 3.9 .

Liang et al. (2024) Y. Liang, Z. Sha, Z. Shi, Z. Song, and Y. Zhou Looped relu mlps may be all you need as practical programmable computers . arXiv preprint arXiv:2410.09375 . Cited by: §B.5 .

Merrill et al. (2022) W. Merrill, A. Sabharwal, and N. A. Smith Saturated transformers are constant-depth threshold circuits . Transactions of the Association for Computational Linguistics . Cited by: item 3 , §C.1 .

Merrill and Sabharwal (2023) W. Merrill and A. Sabharwal The parallelism tradeoff: limitations of log-precision transformers . Transactions of the Association for Computational Linguistics 11 , pp. 531–545 . Cited by: §1.1 , §2.2 , §3.3 , Definition 3.2 .

Merrill and Sabharwal (2024) W. Merrill and A. Sabharwal The expressive power of transformers with chain of thought . In The Twelfth International Conference on Learning Representations , External Links: Link Cited by: §C.1 , §1 , §2.2 , Definition 2.1 .

Merrill and Sabharwal (2025a) W. Merrill and A. Sabharwal A little depth goes a long way: the expressive power of log-depth transformers . arXiv preprint arXiv:2503.03961 . Cited by: §A.2 , §1 , §2.2 , §5.1 , §5.2 .

Merrill and Sabharwal (2025b) W. Merrill and A. Sabharwal Exact expressive power of transformers with padding . arXiv preprint arXiv:2505.18948 . Cited by: §D.1.1 , §2.1 , §2.2 , Table 1 .

Mitzenmacher and Upfal (2017) M. Mitzenmacher and E. Upfal Probability and computing: randomization and probabilistic techniques in algorithms and data analysis . Cambridge university press . Cited by: §4.1 .

Nowak et al. (2024) F. Nowak, A. Svete, A. Butoi, and R. Cotterell On the representational capacity of neural language models with chain-of-thought reasoning . In Association for Computational Linguistics , External Links: Link Cited by: §C.1 , Lemma C.6 , §1 , §2.2 , Table 1 , §4.1 .

Sanford et al. (2024a) C. Sanford, B. Fatemi, E. Hall, A. Tsitsulin, M. Kazemi, J. Halcrow, B. Perozzi, and V. Mirrokni Understanding transformer reasoning capabilities via graph algorithms . In The Thirty-eighth Annual Conference on Neural Information Processing Systems , External Links: Link Cited by: §D.1.1 .

Sanford et al. (2024b) C. Sanford, D. Hsu, and M. Telgarsky Transformers, parallel computation, and logarithmic depth . In Forty-first International Conference on Machine Learning , External Links: Link Cited by: §B.5 , §3.1 , §5.2 .

Saunshi et al. (2025) N. Saunshi, N. Dikkala, Z. Li, S. Kumar, and S. J. Reddi Reasoning with latent thoughts: on the power of looped transformers . In The Thirteenth International Conference on Learning Representations , External Links: Link Cited by: §1 , §2.2 , Table 1 , §4 .

Schnorr (1976) C. Schnorr Optimal algorithms for self-reducible problems . In Proceedings of the Third International Colloquium on Automata, Languages and Programming , Cited by: Definition C.15 , Definition 4.1 .

Stockmeyer and Vishkin (1984) L. Stockmeyer and U. Vishkin Simulation of parallel random access machines by circuits . SIAM Journal on Computing 13 ( 2 ), pp. 409–422 . Cited by: §3.3 .

Svete and Sabharwal (2025) A. Svete and A. Sabharwal On the reasoning abilities of masked diffusion language models . arXiv preprint arXiv:2510.13117 . Cited by: Table 1 .

Valiant (1979) L. G. Valiant The complexity of enumeration and reliability problems . siam Journal on Computing 8 ( 3 ), pp. 410–421 . Cited by: §C.3 .

Vaswani et al. (2017) A. Vaswani, N. Shazeer, N. Parmar, J. Uszkoreit, L. Jones, A. N. Gomez, Ł. Kaiser, and I. Polosukhin Attention is all you need . Advances in neural information processing systems 30 . Cited by: §1 , §2.1 .

Wei et al. (2022) J. Wei, X. Wang, D. Schuurmans, M. Bosma, F. Xia, E. Chi, Q. V. Le, D. Zhou, et al. Chain-of-thought prompting elicits reasoning in large language models . Advances in neural information processing systems 35 , pp. 24824–24837 . Cited by: §1 .

Xu and Sato (2025) K. Xu and I. Sato On expressive power of looped transformers: theoretical analysis and enhancement via timestep encoding . In Forty-second International Conference on Machine Learning , External Links: Link Cited by: §D.1.2 , §1 .

Yang et al. (2024) L. Yang, K. Lee, R. D. Nowak, and D. Papailiopoulos Looped transformers are better at learning learning algorithms . In The Twelfth International Conference on Learning Representations , External Links: Link Cited by: §2.2 .

Zhu et al. (2025a) H. Zhu, S. Hao, Z. Hu, J. Jiao, S. Russell, and Y. Tian Reasoning by superposition: a theoretical perspective on chain of continuous thought . In The Thirty-ninth Annual Conference on Neural Information Processing Systems , External Links: Link Cited by: §1 , §2.2 , Table 1 .

Zhu et al. (2025b) R. Zhu, Z. Wang, K. Hua, T. Zhang, Z. Li, H. Que, B. Wei, Z. Wen, F. Yin, H. Xing, et al. Scaling latent reasoning via looped language models . arXiv preprint arXiv:2510.25741 . Cited by: §1 .

## Appendix A Formal Definitions

### A.1 Notation

Vectors are written in lowercase bold letters (e.g., 𝒙 {\bm{x}} ) and matrices in uppercase bold letters (e.g., 𝑾 {\bm{W}} ). The i i -th entry of a vector 𝒙 {\bm{x}} is 𝒙 i {\bm{x}}_{i} , the vector from the i i -th to the j j -th entry is denoted by 𝒙 i : j {\bm{x}}_{i:j} , and the ( i , j ) (i,j) -th entry of a matrix 𝑾 {\bm{W}} is 𝑾 i , j {\bm{W}}_{i,j} . We use the symbol ∗ * to denote a “don’t care” value (or block of values). For n ∈ ℕ + n\in\mathbb{N}^{+} , let [ n ] ≔ { 1 , 2 , … , n } [n]\coloneq\{1,2,\ldots,n\} . We sometimes write column vectors horizontally, e.g., 𝒙 = ( x 1 , … , x n ) {\bm{x}}=(x_{1},\ldots,x_{n}) , for brevity. The Hadamard (element-wise) product is ⊙ \odot . 𝒆 i ∈ { 0 , 1 } d {\bm{e}}_{i}\in\{0,1\}^{d} is the i i -th standard basis vector, 𝟏 d ∈ ℝ d {\bm{1}}_{d}\in\mathbb{R}^{d} (or 1 d 1_{d} ) the all-ones vector, and 𝟎 d ∈ ℝ d {\bm{0}}_{d}\in\mathbb{R}^{d} the zero vector. 𝑰 d ∈ ℝ d × d {\bm{I}}_{d}\in\mathbb{R}^{d\times d} denotes the d × d d\times d identity matrix, and 𝟎 m × n ∈ ℝ m × n \mathbf{0}_{m\times n}\in\mathbb{R}^{m\times n} the m × n m\times n zero matrix. The indicator function is 𝟏 ​ [ ⋅ ] {\bm{1}}[\cdot] , and ⨁ \bigoplus denotes block-diagonal concatenation. Functions on scalars or vectors are written in upright letters (e.g., FFN \mathrm{FFN} ), while functions on matrices are boldface (e.g., 𝐀𝐓𝐓𝐍 \mathbf{ATTN} ). Boldface is also used when scalar- or vector-level functions are extended to sequence level and applied independently to each token (e.g., 𝐅𝐅𝐍 \mathbf{FFN} ). Finally, 𝗉𝗈𝗅𝗒 ⁡ ( n ) \mathsf{poly}(n) denotes the set of functions growing at most polynomially: 𝗉𝗈𝗅𝗒 ( n ) ≔ { f : ℕ → ℕ | ∃ k ∈ ℕ , ∃ c > 0 , ∀ n ∈ ℕ , f ( n ) ≤ c ⋅ n k } . \mathsf{poly}(n)\coloneq\left\{f:\mathbb{N}\to\mathbb{N}\;\middle|\;\exists k\in\mathbb{N},\;\exists c>0,\;\forall n\in\mathbb{N},\;f(n)\leq c\cdot n^{k}\right\}.

### A.2 Transformer Block

We define the computational components of a Transformer block using the notation of ( Merrill and Sabharwal, 2025a ) . Let 𝔽 s \mathbb{F}_{s} denote the set of s s -bit floating-point numbers with truncated arithmetic ( Definition B.1 ).

###### Definition A.1 (Transformer) .

A Transformer consists of the following components: 1. A word embedding function WE : 𝒱 → 𝔽 s m \mathrm{WE}:{\mathcal{V}}\to\mathbb{F}_{s}^{m} , where 𝒱 {\mathcal{V}} denotes the vocabulary set.

2. A positional embedding function PE : ℕ → 𝔽 s m \mathrm{PE}:\mathbb{N}\to\mathbb{F}_{s}^{m} .

3. A multi-head self-attention layer 𝐒𝐀 : 𝔽 s m × N → 𝔽 s m × N \mathbf{SA}:\mathbb{F}_{s}^{m\times N}\to\mathbb{F}_{s}^{m\times N} for arbitrary sequence length N N , parameterized by a matrix 𝑶 : 𝔽 s s × H → 𝔽 s m {\bm{O}}:\mathbb{F}_{s}^{s\times H}\to\mathbb{F}_{s}^{m} and, for each head h ∈ [ H ] h\in[H] with head size s s , matrices 𝑸 h , 𝑲 h , 𝑽 h : 𝔽 s m → 𝔽 s s {\bm{Q}}_{h},{\bm{K}}_{h},{\bm{V}}_{h}:\mathbb{F}_{s}^{m}\to\mathbb{F}_{s}^{s} . Given an input 𝒙 i ∈ 𝔽 s m {\bm{x}}_{i}\in\mathbb{F}_{s}^{m} for each position i ∈ [ N ] i\in[N] , it computes the query 𝐪 i , h = 𝑸 h ​ 𝒙 i \mathbf{q}_{i,h}={\bm{Q}}_{h}{\bm{x}}_{i} , key 𝒌 i , h = 𝑲 h ​ 𝒙 i {\bm{k}}_{i,h}={\bm{K}}_{h}{\bm{x}}_{i} , and value 𝐯 i , h = 𝑽 h ​ 𝒙 i \mathbf{v}_{i,h}={\bm{V}}_{h}{\bm{x}}_{i} , and outputs 𝑶 ⋅ ( 𝒂 i , 1 , … , 𝒂 i , H ) , {\bm{O}}\cdot({\bm{a}}_{i,1},\ldots,{\bm{a}}_{i,H}), where each attention output 𝒂 i , h {\bm{a}}_{i,h} is defined, for softmax function, as: 𝒂 i , h = ∑ j = 1 c ⁡ ( i ) exp ⁡ ( 𝐪 i , h ⊤ ​ 𝒌 j , h ) Z i , h ⋅ 𝐯 j , h , Z i , h = ∑ j = 1 c ⁡ ( i ) exp ⁡ ( 𝐪 i , h ⊤ ​ 𝒌 j , h ) , {\bm{a}}_{i,h}=\sum_{j=1}^{c(i)}\frac{\exp(\mathbf{q}_{i,h}^{\top}{\bm{k}}_{j,h})}{Z_{i,h}}\cdot\mathbf{v}_{j,h},\quad Z_{i,h}=\sum_{j=1}^{c(i)}\exp(\mathbf{q}_{i,h}^{\top}{\bm{k}}_{j,h}), (1) with c ⁡ ( i ) = i c(i)=i for causal attention and c ⁡ ( i ) = N c(i)=N for full attention. For the saturated hardmax attention ( Merrill et al., 2022 ) , each attention output 𝒂 i , h {\bm{a}}_{i,h} is defined as: 𝒂 i , h = ∑ j ∈ M i , h 1 | M i , h | ​ 𝐯 j , h , M i , h = { j ∈ [ c ⁡ ( i ) ] | 𝐪 i , h ⊤ ​ 𝒌 j , h = max j ′ ⁡ 𝐪 i , h ⊤ ​ 𝒌 j ′ , h } . {\bm{a}}_{i,h}=\sum_{j\in M_{i,h}}\frac{1}{|M_{i,h}|}\,\mathbf{v}_{j,h},\quad M_{i,h}=\left\{j\in[c(i)]\;\middle|\;\mathbf{q}_{i,h}^{\top}{\bm{k}}_{j,h}=\max_{j^{\prime}}\mathbf{q}_{i,h}^{\top}{\bm{k}}_{j^{\prime},h}\right\}. (2)

4. A feedforward layer FF : 𝔽 s m → 𝔽 s m \mathrm{FF}:\mathbb{F}_{s}^{m}\to\mathbb{F}_{s}^{m} with parameter 𝑾 1 : 𝔽 s m → 𝔽 s w {\bm{W}}_{1}:\mathbb{F}_{s}^{m}\to\mathbb{F}_{s}^{w} , 𝑾 2 : 𝔽 s w → 𝔽 s m {\bm{W}}_{2}:\mathbb{F}_{s}^{w}\to\mathbb{F}_{s}^{m} , and 𝒃 ∈ 𝔽 s m {\bm{b}}\in\mathbb{F}_{s}^{m} , where w w is the hidden dimension. Given an input 𝒙 i ∈ 𝔽 s m {\bm{x}}_{i}\in\mathbb{F}_{s}^{m} , it outputs 𝑾 2 ​ ReLU ​ ( 𝑾 1 ​ 𝒙 i + 𝒃 ) {\bm{W}}_{2}\mathrm{ReLU}({\bm{W}}_{1}{\bm{x}}_{i}+{\bm{b}}) , where ReLU ⁡ ( 𝒙 ) = ( max ⁡ { 0 , 𝒙 1 } , … , max ⁡ { 0 , 𝒙 m } ) ⊤ \mathrm{ReLU}({\bm{x}})=(\max\{0,{\bm{x}}_{1}\},\ldots,\max\{0,{\bm{x}}_{m}\})^{\top} .

5. An output function 𝐎𝐔𝐓 : 𝔽 s m → 𝔽 s | 𝒱 | \mathbf{OUT}:\mathbb{F}_{s}^{m}\to\mathbb{F}_{s}^{|{\mathcal{V}}|} , parameterized as a linear transformation.

### A.3 Chain of Thought

###### Definition A.2 (CoT) .

Let the Transformer be defined as the composition: TF dec ≔ 𝐎𝐔𝐓 ∘ ( id + 𝐅𝐅 L ) ∘ ( id + 𝐒𝐀 L ) ∘ ⋯ ∘ ( id + 𝐅𝐅 1 ) ∘ ( id + 𝐒𝐀 1 ) ∘ ( 𝐖𝐄 + 𝐏𝐄 ) , \mathrm{TF}_{\mathrm{dec}}\coloneq\mathbf{OUT}\circ(\id+\mathbf{FF}_{L})\circ(\id+\mathbf{SA}_{L})\circ\cdots\circ(\id+\mathbf{FF}_{1})\circ(\id+\mathbf{SA}_{1})\circ(\mathbf{WE}+\mathbf{PE}), (3) where 𝐒𝐀 ℓ \mathbf{SA}_{\ell} and 𝐅𝐅 ℓ \mathbf{FF}_{\ell} denote the causal attention and the feedforward layers at depth ℓ ∈ [ L ] \ell\in[L] , respectively, and id \id denotes the identity function. The input tokens are first embedded via the word embedding function 𝐖𝐄 \mathbf{WE} and the positional encoding 𝐏𝐄 \mathbf{PE} , and the final output is produced by a linear projection 𝐎𝐔𝐓 \mathbf{OUT} . Given an input sequence x = ( x 1 , … , x n ) ∈ 𝒱 n x=(x_{1},\dots,x_{n})\in{\mathcal{V}}^{n} , we define the initial sequence as: f cot 0 ​ ( x ) ≔ x . f_{\mathrm{cot}}^{0}(x)\coloneq x. Then, the CoT computes recursively as: f cot k + 1 ​ ( x ) ≔ f cot k ​ ( x ) ⋅ Dec ⁡ ( TF dec ​ ( f cot k ​ ( x ) ) ) , f_{\mathrm{cot}}^{k+1}(x)\coloneq f_{\mathrm{cot}}^{k}(x)\cdot\mathrm{Dec}\,(\mathrm{TF}_{\mathrm{dec}}(f_{\mathrm{cot}}^{k}(x))), (4) where ⋅ \cdot denotes concatenation, and Dec ⁡ ( ⋅ ) \mathrm{Dec}(\cdot) is a decoding function that maps the output logits to a token in 𝒱 {\mathcal{V}} : in the deterministic model, Dec ⁡ ( z ) ≔ arg ⁡ max i ∈ [ | 𝒱 | ] ⁡ z i \mathrm{Dec}(z)\coloneq\arg\max_{i\in[|{\mathcal{V}}|]}z_{i} ; in the stochastic model, Dec ⁡ ( z ) ∼ Multinomial ⁡ ( z i / ∑ j z j ) \mathrm{Dec}(z)\sim\mathrm{Multinomial}({z_{i}}/{\sum_{j}z_{j}}) , assuming z i > 0 z_{i}>0 for all i i . The final output of the CoT model after T ⁡ ( n ) T(n) steps is defined as the last output length m m tokens of f cot T ⁡ ( n ) ​ ( x ) f_{\mathrm{cot}}^{T(n)}(x) .

### A.4 Continuous Thought

###### Definition A.3 (Coconut) .

Let the Transformer block be defined as the composition: TF dec ≔ ( id + 𝐅𝐅 L ) ∘ ( id + 𝐒𝐀 L ) ∘ ⋯ ∘ ( id + 𝐅𝐅 1 ) ∘ ( id + 𝐒𝐀 1 ) , \mathrm{TF}_{\mathrm{dec}}\coloneq(\id+\mathbf{FF}_{L})\circ(\id+\mathbf{SA}_{L})\circ\cdots\circ(\id+\mathbf{FF}_{1})\circ(\id+\mathbf{SA}_{1}), (5) where 𝐒𝐀 ℓ \mathbf{SA}_{\ell} and 𝐅𝐅 ℓ \mathbf{FF}_{\ell} denote the causal attention and the feedforward layers at depth ℓ ∈ [ L ] \ell\in[L] , respectively, and id \id denotes the identity function. Given an input sequence x = ( x 1 , … , x n ) ∈ 𝒱 n x=(x_{1},\dots,x_{n})\in{\mathcal{V}}^{n} , we define the initial sequence as: f cot 0 ​ ( x ) ≔ 𝐖𝐄 ⁡ ( x ) + 𝐏𝐄 ⁡ ( [ n ] ) , f_{\mathrm{cot}}^{0}(x)\coloneq\mathbf{WE}(x)+\mathbf{PE}([n]), where the input tokens are first embedded via the word embedding function 𝐖𝐄 \mathbf{WE} and the positional encoding 𝐏𝐄 \mathbf{PE} Then, the continuous thought (Coconut) computes recursively as: f ct k + 1 ​ ( x ) ≔ f ct k ​ ( x ) ⋅ ( TF dec ​ ( f cot k ​ ( x ) + 𝐏𝐄 ⁡ ( k ) ) ) , f_{\mathrm{ct}}^{k+1}(x)\coloneq f_{\mathrm{ct}}^{k}(x)\cdot(\mathrm{TF}_{\mathrm{dec}}(f_{\mathrm{cot}}^{k}(x)+\mathbf{PE}(k))), (6) where ⋅ \cdot denotes concatenation. The final output of the model after T ⁡ ( n ) T(n) steps is defined as the last output length m m tokens of OPEN Dec ⁡ ( 𝐎𝐔𝐓 ⁡ ( f ct T ⁡ ( n ) ​ ( x ) ) ) ) , \mathrm{Dec}\,\left(\mathbf{OUT}\,\left(f_{\mathrm{ct}}^{T(n)}(x))\right)\right), where the final output is produced by a linear projection 𝐎𝐔𝐓 \mathbf{OUT} and Dec ⁡ ( ⋅ ) \mathrm{Dec}(\cdot) is a decoding function that maps the output logits to a token in 𝒱 {\mathcal{V}} : in the deterministic model, Dec ⁡ ( z ) ≔ arg ⁡ max i ∈ [ | 𝒱 | ] ⁡ z i \mathrm{Dec}(z)\coloneq\arg\max_{i\in[|{\mathcal{V}}|]}z_{i} ; in the stochastic model, Dec ⁡ ( z ) ∼ Multinomial ⁡ ( z i / ∑ j z j ) \mathrm{Dec}(z)\sim\mathrm{Multinomial}({z_{i}}/{\sum_{j}z_{j}}) , assuming z i > 0 z_{i}>0 for all i i .

### A.5 Looped Transformer

###### Definition A.4 (Looped TF) .

Let the Transformer block be defined as the composition: TF ≔ ( id + 𝐅𝐅 L ) ∘ ( id + 𝐒𝐀 L ) ∘ ⋯ ∘ ( id + 𝐅𝐅 1 ) ∘ ( id + 𝐒𝐀 1 ) , \mathrm{TF}\coloneq(\id+\mathbf{FF}_{L})\circ(\id+\mathbf{SA}_{L})\circ\cdots\circ(\id+\mathbf{FF}_{1})\circ(\id+\mathbf{SA}_{1}), (7) where 𝐒𝐀 ℓ \mathbf{SA}_{\ell} and 𝐅𝐅 ℓ \mathbf{FF}_{\ell} denote the (non-causal) self-attention and feedforward layers at depth ℓ ∈ [ L ] \ell\in[L] .

Given an input token sequence x = ( x 1 , … , x n ) ∈ 𝒱 n x=(x_{1},\dots,x_{n})\in{\mathcal{V}}^{n} , the initial hidden state is: f loop 0 ​ ( x ) ≔ 𝐖𝐄 ⁡ ( x ) . f_{\mathrm{loop}}^{0}(x)\coloneq\mathbf{WE}(x). At each loop iteration k k , the hidden state is updated by: f loop k + 1 ​ ( x ) ≔ TF ⁡ ( f loop k ​ ( x ) ) . f_{\mathrm{loop}}^{k+1}(x)\coloneq\mathrm{TF}\left(f_{\mathrm{loop}}^{k}(x)\right). (8) The final outputs after T ⁡ ( n ) T(n) loop iterations are decoded as Dec ∘ 𝐎𝐔𝐓 ∘ f loop T ⁡ ( n ) ​ ( x ) , \mathrm{Dec}\circ\mathbf{OUT}\circ f_{\mathrm{loop}}^{T(n)}(x), and the model’s prediction is defined as the last output length m ≤ n m\leq n tokens of this projected sequence.

## Appendix B Deferred Proofs for Section 3

### B.1 Precision Modeling

We focus on signed floating-point numbers, following ( Li et al., 2024 ) , but omit exponents for simplicity.

###### Definition B.1 (Floating-point Representation, cf. ( Li et al., 2024 ) ) .

Consider floating-point numbers with a mantissa part of s s bits and a sign bit of 1, totaling ( s + 1 ) (s+1) bits. We denote the set of such floating-point numbers by 𝔽 s \mathbb{F}_{s} , and define B s ≜ max ⁡ 𝔽 s . B_{s}\triangleq\max\mathbb{F}_{s}.

###### Definition B.2 (Correct Rounding, cf. ( Li et al., 2024 ) ) .

For any x ∈ ℝ x\in\mathbb{R} and any closed subset 𝔽 ⊂ ℝ \mathbb{F}\subset\mathbb{R} containing 0 0 , we define the correct rounding round ⁡ ( x , 𝔽 ) \operatorname{round}(x,\mathbb{F}) as the number in 𝔽 \mathbb{F} closest to x x . In particular, rounding to a floating-point number with mantissa part s s bits is denoted by [ ⋅ ] s [\cdot]_{s} . Rounding applied to vectors is to be operated coordinate-wise.

They also define primitive arithmetic under finite precision by applying rounding after each basic operation. In particular, for multi-operand operations, rounding is applied after each binary operation. Finite-precision summation over more than two numbers is thus defined as follows.

###### Definition B.3 (Summation with Iterative Rounding ( Li et al., 2024 ) ) .

For any s , n ∈ ℕ + s,n\in\mathbb{N}^{+} and vector 𝒙 ∈ ℝ n {\bm{x}}\in\mathbb{R}^{n} , define the summation with iterative rounding to s s -bit precision sum s : ⋃ n ∈ ℕ + ( 𝔽 s ) n → 𝔽 s , \mathrm{sum}_{s}:\ \bigcup_{n\in\mathbb{N}^{+}}(\mathbb{F}_{s})^{n}\to\mathbb{F}_{s}, (9) where, for any n ∈ ℕ + n\in\mathbb{N}^{+} and 𝒙 = ( x 1 , … , x n ) ∈ ℝ n {\bm{x}}=(x_{1},\dots,x_{n})\in\mathbb{R}^{n} , sum s ( x ) ≔ [ [ ⋯ [ [ x 1 + x 2 ] s + x 3 ] s + ⋯ + x n − 1 ] s + x n ] s . \mathrm{sum}_{s}(x)\coloneqq\Bigl[\;\Bigl[\;\cdots\Bigl[\,[x_{1}+x_{2}]_{s}+x_{3}\Bigr]_{s}+\cdots+x_{n-1}\Bigr]_{s}+x_{n}\;\Bigr]_{s}. (10)

Based on this definition, all computations in the Transformer block of Definition A.1 can be represented in finite precision. The inner product and the matrix product are defined as 𝒙 ⊤ 𝒚 ≔ sum s ( 𝒙 ⊙ 𝒚 ) , ( 𝑨 𝑩 ) i , j ≔ 𝑨 i , : ⊤ 𝑩 : , j . {\bm{x}}^{\top}{\bm{y}}\coloneqq\operatorname{sum}_{s}({\bm{x}}\odot{\bm{y}}),\qquad({\bm{A}}{\bm{B}})_{i,j}\coloneqq{\bm{A}}_{i,:}^{\top}{\bm{B}}_{:,j}. (11) Throughout this section, we interpret all operations as finite-precision computations as defined above.

### B.2 Definition of Assumption 3.4

Our definition of polynomially efficient approximation follows that of Feng et al. (2023) , but differs in scope: while their framework targets real-valued functions, ours applies to symbolic functions.

###### Definition B.4 (Polynomially-efficient approximation) .

We say that a function f n : Σ ℓ ⁡ ( n ) → Σ f_{n}:\Sigma^{\ell(n)}\to\Sigma admits a polynomially efficient approximation if, for a sufficiently small error tolerance 0 < δ ≤ 1 3 0<\delta\leq\tfrac{1}{3} , there exists a feedforward network FF : 𝔽 s ⁡ ( n ) ℓ ⁡ ( n ) ⋅ | Σ | → 𝔽 s ⁡ ( n ) | Σ | , s ⁡ ( n ) = O ⁡ ( log ⁡ n ) , \mathrm{FF}:\mathbb{F}_{s(n)}^{\ell(n)\cdot|\Sigma|}\to\mathbb{F}_{s(n)}^{|\Sigma|},\ s(n)=O(\log n), such that the following holds: for every input 𝒙 = ( x 1 , … , x ℓ ⁡ ( n ) ) ∈ Σ ℓ ⁡ ( n ) {\bm{x}}=(x_{1},\ldots,x_{\ell(n)})\in\Sigma^{\ell(n)} , FF ​ ( 𝒆 ⁡ ( x 1 ) , … , 𝒆 ⁡ ( x ℓ ⁡ ( n ) ) ) i = { ≥ 1 − δ if 𝒆 ⁡ ( f n ​ ( 𝒙 ) ) = 𝒆 i , ≤ δ else , \mathrm{FF}(\bm{e}(x_{1}),\ldots,\bm{e}(x_{\ell(n)}))_{i}\;=\;\begin{cases}\;\geq 1-\delta&\text{if}\quad\bm{e}(f_{n}({\bm{x}}))={\bm{e}}_{i},\\ \;\leq\delta&\text{else },\end{cases} (12) where 𝒆 : Σ → { 0 , 1 } | Σ | \bm{e}:\Sigma\to\{0,1\}^{|\Sigma|} denote the one-hot encoding. Moreover, the number of parameters of the feedforward network is bounded by a polynomial in ℓ ⁡ ( n ) \ell(n) and 1 / δ 1/\delta .

### B.3 Technical lemmas

In this section, we provide the key components for our constructive proofs.

#### B.3.1 Orthogonal Vectors

We follow the notation of ( Li et al., 2024 ) . For any positive integer s ∈ ℕ + s\in\mathbb{N}^{+} and x ∈ { 0 , 1 , … , 2 s − 1 } x\in\{0,1,\dots,2^{s}-1\} , we denote by 𝖻𝗂𝗇 s ​ ( x ) ∈ { 0 , 1 } s \mathsf{bin}_{s}(x)\in\{0,1\}^{s} the standard binary representation of x x using s s bits, defined such that x = ∑ i = 1 s 2 i ⋅ ( 𝖻𝗂𝗇 s ​ ( x ) ) i . x=\sum_{i=1}^{s}2^{i}\cdot(\mathsf{bin}_{s}(x))_{i}. We further define the signed binary encoding of x x , denoted by 𝗌𝖻𝗂𝗇 s ​ ( x ) ∈ { − 1 , 1 } s \mathsf{sbin}_{s}(x)\in\{-1,1\}^{s} , as 𝗌𝖻𝗂𝗇 s ​ ( x ) = 2 ⋅ 𝖻𝗂𝗇 s ​ ( x ) − ( 1 , … , 1 ) . \mathsf{sbin}_{s}(x)=2\cdot\mathsf{bin}_{s}(x)-(1,\ldots,1). Let 𝒙 , 𝒚 ∈ ℝ s {\bm{x}},{\bm{y}}\in\mathbb{R}^{s} be two vectors of the same length. We define their interleaving, denoted by 𝒙 ⌢ ​ 𝒚 ∈ ℝ 2 ​ s {{\bm{x}}}^{\frown}{{\bm{y}}}\in\mathbb{R}^{2s} , as follows: ( 𝒙 ⌢ ​ 𝒚 ) 2 ​ i − 1 = x i , ( 𝒙 ⌢ ​ 𝒚 ) 2 ​ i = 𝒚 i ({{\bm{x}}}^{\frown}{{\bm{y}}})_{2i-1}=x_{i},({{\bm{x}}}^{\frown}{{\bm{y}}})_{2i}={\bm{y}}_{i} for all i ∈ [ s ] . i\in[s]. The orthogonal vectors under finite-precision arithmetic can be:

###### Lemma B.5 ( Li et al., 2024 ) .

For any s ∈ ℕ + s\in\mathbb{N}^{+} , let 𝐪 i = 𝗌𝖻𝗂𝗇 s ​ ( i ) ⌢ ​ 1 s {\bm{q}}_{i}={\mathsf{sbin}_{s}(i)}^{\frown}{1_{s}} and 𝐤 i = 2 s + 1 ⋅ ( 𝗌𝖻𝗂𝗇 s ​ ( i ) ⌢ ​ ( − 1 s ) ) {\bm{k}}_{i}=2^{s+1}\cdot({\mathsf{sbin}_{s}(i)}^{\frown}{(-1_{s})}) for all i ∈ [ 2 s − 1 ] i\in[2^{s}-1] , it holds that ⟨ 𝐪 i , 𝐤 j ⟩ s = − B s \left\langle{\bm{q}}_{i},{\bm{k}}_{j}\right\rangle_{s}=-B_{s} if i ≠ j i\neq j and ⟨ 𝐪 i , 𝐤 j ⟩ s = 0 \left\langle{\bm{q}}_{i},{\bm{k}}_{j}\right\rangle_{s}=0 if i = j i=j . Since [ exp ⁡ ( − B s ) ] s ≤ [ 2 − s − 1 ] s = 0 \bigl[\exp(-B_{s})\bigr]_{s}\leq\bigl[2^{-s-1}]_{s}=0 , it follows that [ exp ( ⟨ 𝐪 i , 𝐤 j ⟩ s ) ] s = 𝟏 [ i = j ] \left[\exp(\left\langle{\bm{q}}_{i},{\bm{k}}_{j}\right\rangle_{s})\right]_{s}=\mathbf{1}[i=j] for all i , j ∈ [ 2 s − 1 ] i,j\in[2^{s}-1] .

#### B.3.2 Position Selector

###### Lemma B.6 .

For any m ∈ ℕ + m\in\mathbb{N}^{+} and 𝐱 ∈ 𝔽 s m {\bm{x}}\in\mathbb{F}_{s}^{m} with x i > 0 x_{i}>0 for all i ∈ [ m ] i\in[m] , there exists a feedforward layer FF : 𝔽 s 2 ​ m → 𝔽 s 2 ​ m \mathrm{FF}:\mathbb{F}_{s}^{2m}\to\mathbb{F}_{s}^{2m} , for any i ∈ [ m ] i\in[m] , such that ( id + FF ) ​ ( ( 𝒙 , 𝒆 i ) ) = ( 𝒙 ⊙ 𝒆 i , 𝒆 i ) . (\id+\mathrm{FF})(({\bm{x}},{\bm{e}}_{i}))=({\bm{x}}\odot{\bm{e}}_{i},{\bm{e}}_{i})\,. (13)

###### Proof.

Let the input be 𝒛 = ( 𝒙 , 𝒆 i ) ∈ 𝔽 s 2 ​ m {\bm{z}}=({\bm{x}},{\bm{e}}_{i})\in\mathbb{F}_{s}^{2m} . Set the weight 𝑾 1 ∈ 𝔽 s m × 2 ​ m {\bm{W}}_{1}\in\mathbb{F}_{s}^{m\times 2m} and bias 𝒃 ∈ m ​ a ​ t ​ h ​ b ​ b ​ F s m {\bm{b}}\in\\ mathbb{F}_{s}^{m} by 𝑾 1 = [ 𝑰 m − B s ​ 𝑰 m ] , 𝒃 = 𝟎 , {\bm{W}}_{1}=\bigl[\,{\bm{I}}_{m}\;\;\;-B_{s}{\bm{I}}_{m}\,\bigr],\qquad{\bm{b}}={\bm{0}}, (14) to have 𝑾 1 ​ 𝒛 + 𝒃 = 𝒙 − B s ​ 𝒆 i . {\bm{W}}_{1}{\bm{z}}+{\bm{b}}={\bm{x}}-B_{s}{\bm{e}}_{i}. Applying the ReLU activation coordinate-wise gives ReLU ​ ( 𝒙 − B s ​ 𝒆 i ) j = { 0 , j = i , x j , j ≠ i . \mathrm{ReLU}({\bm{x}}-B_{s}{\bm{e}}_{i})_{j}=\begin{cases}0,&j=i,\\ x_{j},&j\neq i.\end{cases} (15) Hence, 𝒉 ≔ ReLU ⁡ ( 𝑾 1 ​ 𝒛 + 𝒃 ) = 𝒙 ⊙ ( 𝟏 − 𝒆 i ) . {\bm{h}}\coloneqq\mathrm{ReLU}({\bm{W}}_{1}{\bm{z}}+{\bm{b}})={\bm{x}}\odot({\bm{1}}-{\bm{e}}_{i}). (16)

Next, set the second linear layer 𝑾 2 ∈ 𝔽 s 2 ​ m × m {\bm{W}}_{2}\in\mathbb{F}_{s}^{2m\times m} by 𝑾 2 = [ − 𝑰 m 𝟎 m × m ] . {\bm{W}}_{2}=\begin{bmatrix}-{\bm{I}}_{m}\\ \mathbf{0}_{m\times m}\end{bmatrix}. (17) Thus we have 𝒛 + 𝑾 2 ​ 𝒉 = [ 𝒙 𝒆 i ] + [ − 𝒉 𝟎 ] = [ 𝒙 𝒆 i ] + [ − 𝒙 ⊙ ( 𝟏 − 𝒆 i ) 𝟎 ] = [ 𝒙 ⊙ 𝒆 i 𝒆 i ] . {\bm{z}}+{\bm{W}}_{2}{\bm{h}}=\begin{bmatrix}{\bm{x}}\\ {\bm{e}}_{i}\end{bmatrix}+\begin{bmatrix}-{\bm{h}}\\ {\bm{0}}\end{bmatrix}=\begin{bmatrix}{\bm{x}}\\ {\bm{e}}_{i}\end{bmatrix}+\begin{bmatrix}-{\bm{x}}\odot({\bm{1}}-{\bm{e}}_{i})\\ {\bm{0}}\end{bmatrix}=\begin{bmatrix}{\bm{x}}\odot{\bm{e}}_{i}\\ {\bm{e}}_{i}\end{bmatrix}. (18) ∎

#### B.3.3 Feedforward layers

###### Lemma B.7 .

Let N ∈ ℕ + N\in\mathbb{N}^{+} . For each i ∈ [ N ] i\in[N] , let f i : Σ ℓ i → Σ f_{i}:\Sigma^{\ell_{i}}\to\Sigma admit polynomially-efficient approximation by FF i \mathrm{FF}_{i} . Then there exists a feedforward layer FF : 𝔽 s ∑ i = 1 N ℓ i ​ | Σ | → 𝔽 s N ​ | Σ | \mathrm{FF}:\ \mathbb{F}_{s}^{\sum_{i=1}^{N}\ell_{i}|\Sigma|}\to\mathbb{F}_{s}^{N|\Sigma|} such that for every input tuple 𝐱 i = ( x 1 ( i ) , … , x ℓ i ( i ) ) ∈ Σ ℓ i {\bm{x}}_{i}=(x^{(i)}_{1},\ldots,x^{(i)}_{\ell_{i}})\in\Sigma^{\ell_{i}} , FF ( ∥ i = 1 N ( 𝒆 ( x 1 ( i ) ) , … , 𝒆 ( x ℓ i ( i ) ) ) ) = ∥ i = 1 N FF i ( 𝒙 i ) , \mathrm{FF}\!\left(\big\|_{i=1}^{N}\,(\bm{e}(x^{(i)}_{1}),\ldots,\bm{e}(x^{(i)}_{\ell_{i}}))\right)\;=\;\big\|_{i=1}^{N}\,\mathrm{FF}_{i}({\bm{x}}_{i}), (19) where ∥ \| denotes concatenation.

###### Proof.

For each i ∈ [ N ] i\in[N] , by Definition B.4 , there exist width w i ∈ ℕ w_{i}\in\mathbb{N} and parameters 𝑾 1 ( i ) ∈ 𝔽 s w i × ℓ i ​ | Σ | , 𝑾 2 ( i ) ∈ 𝔽 s | Σ | × w i , 𝒃 ( i ) ∈ 𝔽 s w i {\bm{W}}^{(i)}_{1}\in\mathbb{F}_{s}^{w_{i}\times\ell_{i}|\Sigma|},\quad{\bm{W}}^{(i)}_{2}\in\mathbb{F}_{s}^{|\Sigma|\times w_{i}},\quad{\bm{b}}^{(i)}\in\mathbb{F}_{s}^{w_{i}} (20) such that FF i ​ ( 𝒙 i ) = 𝑾 2 ( i ) ​ ReLU ​ ( 𝑾 1 ( i ) ​ 𝒆 ​ ( 𝒙 i ) + 𝒃 ( i ) ) . \mathrm{FF}_{i}({\bm{x}}_{i})={\bm{W}}^{(i)}_{2}\mathrm{ReLU}({\bm{W}}^{(i)}_{1}\,\bm{e}({\bm{x}}_{i})+{\bm{b}}^{(i)}).

Now, define block-diagonal matrices 𝑾 1 ≔ ⨁ i = 1 N 𝑾 1 ( i ) , 𝑾 2 ≔ ⨁ i = 1 N 𝑾 2 ( i ) , 𝒃 ≔ ⨁ i = 1 N 𝒃 ( i ) . {\bm{W}}_{1}\coloneqq\bigoplus_{i=1}^{N}{\bm{W}}^{(i)}_{1},\qquad{\bm{W}}_{2}\coloneqq\bigoplus_{i=1}^{N}{\bm{W}}^{(i)}_{2},\qquad{\bm{b}}\coloneqq\bigoplus_{i=1}^{N}{\bm{b}}^{(i)}. (21) Then the single feedforward layer FF ⁡ ( 𝒙 ) ≔ 𝑾 2 ​ ReLU ​ ( 𝑾 1 ​ 𝒙 + 𝒃 ) \mathrm{FF}({\bm{x}})\coloneqq{\bm{W}}_{2}\mathrm{ReLU}({\bm{W}}_{1}{\bm{x}}+{\bm{b}}) (22) applies each block independently to its corresponding input, yielding exactly FF ( 𝒙 ) = ∥ i = 1 N FF i ( 𝒙 i ) . \mathrm{FF}({\bm{x}})=\big\|_{i=1}^{N}\mathrm{FF}_{i}({\bm{x}}_{i}). ∎

###### Lemma B.8 .

Let f : Σ ℓ → Σ f:\Sigma^{\ell}\to\Sigma be a function that admits polynomially-efficient approximation ( Definition B.4 ). Then, there exist two feedforward layers FF 1 : 𝔽 s ( 1 + ℓ ) ​ | Σ | + 1 → 𝔽 s ( 1 + ℓ ) ​ | Σ | + 1 , FF 2 : 𝔽 s ( 1 + ℓ ) ​ | Σ | + 1 → 𝔽 s ( 1 + ℓ ) ​ | Σ | + 1 , \mathrm{FF}_{1}:\mathbb{F}_{s}^{(1+\ell)|\Sigma|+1}\to\mathbb{F}_{s}^{(1+\ell)|\Sigma|+1},\quad\mathrm{FF}_{2}:\mathbb{F}_{s}^{(1+\ell)|\Sigma|+1}\to\mathbb{F}_{s}^{(1+\ell)|\Sigma|+1}, (23) such that, for every 𝐱 = ( x 1 , … , x ℓ ) ∈ Σ ℓ {\bm{x}}=(x_{1},\ldots,x_{\ell})\in\Sigma^{\ell} and t ∈ { 0 , 1 } t\in\{0,1\} , ( id + FF 2 ) ∘ ( id + FF 1 ) ​ ( 𝟎 , 𝒆 ⁡ ( x 1 ) , … , 𝒆 ⁡ ( x ℓ ) , t ) = ( t ⋅ 𝒆 ⁡ ( f ⁡ ( 𝒙 ) ) , 𝒆 ⁡ ( x 1 ) , … , 𝒆 ⁡ ( x ℓ ) , t ) . (\id+\mathrm{FF}_{2})\circ(\id+\mathrm{FF}_{1})\big({\bm{0}},\ \bm{e}(x_{1}),\ldots,\bm{e}(x_{\ell}),\ t\big)\;=\;(t\cdot\bm{e}(f({\bm{x}})),\ \bm{e}(x_{1}),\ldots,\bm{e}(x_{\ell}),\ t). (24)

###### Proof.

Let n ≔ | Σ | n\coloneqq|\Sigma| and L ≔ ℓ ​ n L\coloneqq\ell n . Write 𝒖 = ( 𝒆 ⁡ ( x 1 ) , … , 𝒆 ⁡ ( x ℓ ) ) ∈ { 0 , 1 } L {\bm{u}}=(\bm{e}(x_{1}),\ldots,\bm{e}(x_{\ell}))\in\{0,1\}^{L} . By Definition B.4 , there exist w f ∈ ℕ w_{f}\in\mathbb{N} , matrices 𝑾 1 ( f ) ∈ 𝔽 s w f × L {\bm{W}}^{(f)}_{1}\in\mathbb{F}_{s}^{w_{f}\times L} , 𝑾 2 ( f ) ∈ 𝔽 s n × w f {\bm{W}}^{(f)}_{2}\in\mathbb{F}_{s}^{n\times w_{f}} , and bias 𝒃 ( f ) ∈ 𝔽 s w f {\bm{b}}^{(f)}\in\mathbb{F}_{s}^{w_{f}} such that FF f ​ ( 𝒖 ) ≔ 𝑾 2 ( f ) ​ ReLU ​ ( 𝑾 1 ( f ) ​ 𝒖 + 𝒃 ( f ) ) , FF f ​ ( 𝒖 ) i = { ≥ 1 − δ if ​ 𝒆 ​ ( f ⁡ ( 𝒙 ) ) = 𝒆 i , ≤ δ otherwise . \mathrm{FF}_{f}({\bm{u}})\coloneqq{\bm{W}}^{(f)}_{2}\,\mathrm{ReLU}({\bm{W}}^{(f)}_{1}{\bm{u}}+{\bm{b}}^{(f)}),\quad\mathrm{FF}_{f}({\bm{u}})_{i}=\begin{cases}\geq 1-\delta&\text{if }\ \bm{e}(f({\bm{x}}))={\bm{e}}_{i},\\ \leq\delta&\text{otherwise}.\end{cases} (25)

Set the first layer as 𝑾 1 ( 1 ) = [ 𝟎 𝑾 1 ( f ) 𝟎 w f × 1 𝟎 𝑰 L 𝟎 L × 1 ] , 𝒃 ( 1 ) = [ 𝒃 ( f ) 𝟎 L ] , 𝑾 2 ( 1 ) = [ 𝑾 2 ( f ) 0 𝟎 L × w f 0 𝟎 1 × w f 𝟎 ] , {\bm{W}}^{(1)}_{1}=\begin{bmatrix}{\bm{0}}&{\bm{W}}^{(f)}_{1}&\mathbf{0}_{\,w_{f}\times 1}\\ {\bm{0}}&{\bm{I}}_{L}&\mathbf{0}_{\,L\times 1}\end{bmatrix},\quad{\bm{b}}^{(1)}=\begin{bmatrix}{\bm{b}}^{(f)}\\ {\bm{0}}_{L}\end{bmatrix},\quad{\bm{W}}^{(1)}_{2}=\begin{bmatrix}{\bm{W}}^{(f)}_{2}&\,{\bm{0}}\\ \mathbf{0}_{\,L\times w_{f}}&\,{\bm{0}}\\ \mathbf{0}_{\,1\times w_{f}}&{\bm{0}}\end{bmatrix}, (26) and define FF 1 ​ ( 𝟎 , 𝒖 , t ) ≔ 𝑾 2 ( 1 ) ​ ReLU ​ ( 𝑾 1 ( 1 ) ​ ( 𝟎 , 𝒖 , t ) + 𝒃 ( 1 ) ) \mathrm{FF}_{1}({\bm{0}},{\bm{u}},t)\coloneqq{\bm{W}}^{(1)}_{2}\,\mathrm{ReLU}\big({\bm{W}}^{(1)}_{1}({\bm{0}},{\bm{u}},t)+{\bm{b}}^{(1)}\big) . Then, it holds that FF 1 ​ ( 𝟎 , 𝒖 , t ) \displaystyle\mathrm{FF}_{1}({\bm{0}},{\bm{u}},t) = 𝑾 2 ( 1 ) ​ ReLU ​ ( [ 𝑾 1 ( f ) ​ 𝒖 + 𝒃 ( f ) 𝒖 ] ) \displaystyle={\bm{W}}^{(1)}_{2}\,\mathrm{ReLU}\left(\begin{bmatrix}{\bm{W}}^{(f)}_{1}{\bm{u}}+{\bm{b}}^{(f)}\\ {\bm{u}}\end{bmatrix}\right) (27) = [ 𝑾 2 ( f ) ​ ReLU ​ ( 𝑾 1 ( f ) ​ 𝒖 + 𝒃 ( f ) ) 𝟎 ] \displaystyle=\begin{bmatrix}{\bm{W}}^{(f)}_{2}\mathrm{ReLU}({\bm{W}}^{(f)}_{1}{\bm{u}}+{\bm{b}}^{(f)})\\ {\bm{0}}\end{bmatrix} (28) = [ FF f ​ ( 𝒖 ) 𝟎 ] . \displaystyle=\begin{bmatrix}\mathrm{FF}_{f}({\bm{u}})\\ {\bm{0}}\end{bmatrix}. (29) Thus we have ( id + FF 1 ) ​ ( 𝟎 , 𝒖 , t ) = ( FF f ​ ( 𝒖 ) , 𝒖 , t ) . (\id+\mathrm{FF}_{1})({\bm{0}},{\bm{u}},t)=\bigl(\mathrm{FF}_{f}({\bm{u}}),\,{\bm{u}},\,t\bigr).

For the second layer, choose δ ≤ 1 3 \delta\leq\tfrac{1}{3} and M ≥ 1 M\geq 1 and set 𝑾 1 ( 2 ) = [ 2 ​ 𝑰 n 𝟎 n × L M ​ 𝟏 n 2 ​ 𝑰 n 𝟎 n × L M ​ 𝟏 n 𝑰 n 𝟎 n × L 𝟎 n × 1 − 𝑰 n 𝟎 n × L 𝟎 n × 1 ] , 𝒃 ( 2 ) = [ − M ​ 𝟏 n ( 1 − M ) ​ 𝟏 n 𝟎 n 𝟎 n ] , 𝑾 2 ( 2 ) = [ 𝑰 n − 𝑰 n − 𝑰 n 𝑰 n 0 L × n 𝟎 L × n 𝟎 L × n 𝟎 L × n 0 1 × n 𝟎 1 × n 𝟎 1 × n 𝟎 1 × n ] . {\bm{W}}^{(2)}_{1}=\begin{bmatrix}2{\bm{I}}_{n}&\mathbf{0}_{n\times L}&M{\bm{1}}_{n}\\ 2{\bm{I}}_{n}&\mathbf{0}_{n\times L}&M{\bm{1}}_{n}\\ {\bm{I}}_{n}&\mathbf{0}_{n\times L}&\mathbf{0}_{n\times 1}\\ -{\bm{I}}_{n}&\mathbf{0}_{n\times L}&\mathbf{0}_{n\times 1}\end{bmatrix},\ {\bm{b}}^{(2)}=\begin{bmatrix}-M{\bm{1}}_{n}\\ (1-M){\bm{1}}_{n}\\ {\bm{0}}_{n}\\ {\bm{0}}_{n}\end{bmatrix},\ {\bm{W}}^{(2)}_{2}=\begin{bmatrix}\ {\bm{I}}_{n}&-{\bm{I}}_{n}&-{\bm{I}}_{n}&\ {\bm{I}}_{n}\ \\ \ \mathbf{0}_{\,L\times n}&\mathbf{0}_{\,L\times n}&\mathbf{0}_{\,L\times n}&\mathbf{0}_{\,L\times n}\\ \ \mathbf{0}_{\,1\times n}&\mathbf{0}_{\,1\times n}&\mathbf{0}_{\,1\times n}&\mathbf{0}_{\,1\times n}\end{bmatrix}. (30) and define FF 2 ​ ( 𝒚 ) ≔ 𝑾 2 ( 2 ) ​ ReLU ​ ( 𝑾 1 ( 2 ) ​ 𝒚 + 𝒃 ( 2 ) ) \mathrm{FF}_{2}({\bm{y}})\coloneqq{\bm{W}}^{(2)}_{2}\,\mathrm{ReLU}\big({\bm{W}}^{(2)}_{1}{\bm{y}}+{\bm{b}}^{(2)}\big) . Then it holds that, for 𝒛 ≔ FF f ​ ( 𝒖 ) {\bm{z}}\coloneqq\mathrm{FF}_{f}({\bm{u}}) , FF 2 ​ ( 𝒛 , 𝒖 , t ) \displaystyle\mathrm{FF}_{2}({\bm{z}},{\bm{u}},t) = 𝑾 2 ( 2 ) ​ [ ReLU ⁡ ( 2 ​ 𝒛 + M ​ t ​ 𝟏 n − M ​ 𝟏 n ) ReLU ⁡ ( 2 ​ 𝒛 + M ​ t ​ 𝟏 n + ( 1 − M ) ​ 𝟏 n ) ReLU ⁡ ( 𝒛 ) ReLU ⁡ ( − 𝒛 ) ] \displaystyle={\bm{W}}^{(2)}_{2}\,\begin{bmatrix}\mathrm{ReLU}\bigl(2{\bm{z}}+Mt{\bm{1}}_{n}-M{\bm{1}}_{n}\bigr)\\ \mathrm{ReLU}\bigl(2{\bm{z}}+Mt{\bm{1}}_{n}+(1-M){\bm{1}}_{n}\bigr)\\ \mathrm{ReLU}({\bm{z}})\\ \mathrm{ReLU}(-{\bm{z}})\end{bmatrix} (31) = 𝑾 2 ( 2 ) ​ [ ReLU ⁡ ( 2 ​ 𝒛 + M ⁡ ( t − 1 ) ​ 𝟏 n ) ReLU ⁡ ( 2 ​ 𝒛 + 1 + M ⁡ ( t − 1 ) ​ 𝟏 n ) 𝒛 𝟎 ] \displaystyle={\bm{W}}^{(2)}_{2}\,\begin{bmatrix}\mathrm{ReLU}\bigl(2{\bm{z}}+M(t-1){\bm{1}}_{n}\bigr)\\ \mathrm{ReLU}\bigl(2{\bm{z}}+1+M(t-1){\bm{1}}_{n}\bigr)\\ {\bm{z}}\\ {\bm{0}}\end{bmatrix} (32) = [ ReLU ⁡ ( 𝒛 − δ + M ⁡ ( t − 1 ) ) − ReLU ⁡ ( 𝒛 − 1 + M ⁡ ( t − 1 ) ) − 𝒛 𝟎 0 ] , \displaystyle=\begin{bmatrix}\mathrm{ReLU}\bigl({\bm{z}}-\delta+M(t-1)\bigr)-\mathrm{ReLU}\bigl({\bm{z}}-1+M(t-1)\bigr)-{\bm{z}}\\ \mathbf{0}\\ 0\end{bmatrix}, (33) where it satisfies that ReLU ⁡ ( 𝒛 − δ + M ⁡ ( t − 1 ) ) − ReLU ⁡ ( 𝒛 − δ − 1 + M ⁡ ( t − 1 ) ) = { 𝒆 ⁡ ( f ⁡ ( 𝒙 ) ) if t = 1 , 0 if t = 0 . \mathrm{ReLU}\bigl({\bm{z}}-\delta+M(t-1)\bigr)-\mathrm{ReLU}\bigl({\bm{z}}-\delta-1+M(t-1)\bigr)\;=\;\begin{cases}\;\bm{e}(f({\bm{x}}))&\text{if}\quad t=1,\\ \;{\bm{0}}&\text{if}\quad t=0.\end{cases} (34)

Therefore, the composition satisfies ( id + FF 2 ) ∘ ( id + FF 1 ) ​ ( 𝟎 , 𝒖 , t ) = ( t ⋅ 𝒆 ⁡ ( f ⁡ ( 𝒙 ) ) , 𝒖 , t ) . (\id+\mathrm{FF}_{2})\circ(\id+\mathrm{FF}_{1})\bigl({\bm{0}},{\bm{u}},t\bigr)=(t\cdot\bm{e}(f({\bm{x}})),\ {\bm{u}},\ t). ∎

### B.4 Proof for Theorem 3.5

###### Proof.

Let G n = ( V n , E n ) G_{n}=(V_{n},E_{n}) be a computation graph, where ℱ = { f 1 , f 2 , … , f | ℱ | } \mathcal{F}=\{f_{1},f_{2},\dots,f_{|\mathcal{F}|}\} . Each node v ∈ V n v\in V_{n} is labeled by a one-hot vector 𝒆 ⁡ ( v ) ∈ { 0 , 1 } | ℱ | \bm{e}(v)\in\{0,1\}^{|\mathcal{F}|} indicating the function assigned to v v from the finite set ℱ \mathcal{F} . Let v 1 , v 2 , … , v | V n | v_{1},v_{2},\dots,v_{|V_{n}|} denote a fixed topological ordering of V n V_{n} , with inputs appearing first and outputs last. For each function f i ∈ ℱ f_{i}\in\mathcal{F} , let C f i ( n ) ≔ max { | pred ( v ) | : v ∈ V n , 𝒆 ( v ) = 𝒆 i } . C_{f_{i}}(n)\coloneqq\max\{\,|\mathrm{pred}(v)|:v\in V_{n},\;\bm{e}(v)={\bm{e}}_{i}\,\}. and define C sum ​ ( n ) ≔ ∑ f ∈ ℱ C f ​ ( n ) , C max ​ ( n ) ≔ max f ∈ ℱ ⁡ C f ​ ( n ) . C_{\mathrm{sum}}(n)\coloneqq\sum_{f\in\mathcal{F}}C_{f}(n),\ C_{\mathrm{max}}(n)\coloneqq\max_{f\in\mathcal{F}}C_{f}(n).

Let the precision be s ⁡ ( n ) = C ⋅ ⌈ log 2 ⁡ n ⌉ s(n)=C\cdot\lceil\log_{2}n\rceil where C ∈ ℕ C\in\mathbb{N} is a sufficiently large integer such that 2 s ⁡ ( n ) ≥ n C 2^{s(n)}\;\geq\;n^{C} exceeds the maximum polynomial step bound under consideration. We denote by pred ⁡ ( v i ) ∈ 𝔽 s ⁡ ( n ) C max ​ ( n ) \mathrm{pred}(v_{i})\in\mathbb{F}_{s(n)}^{C_{\max}(n)} the vector of predecessor indices of node v i v_{i} ; that is, if v i v_{i} has d ≤ C max ​ ( n ) d\leq C_{\max}(n) incoming edges from nodes v j 1 , … , v j d v_{j_{1}},\dots,v_{j_{d}} , then pred ⁡ ( v i ) = ( j 1 , … , j d , 𝟎 ) \mathrm{pred}(v_{i})=(j_{1},\dots,j_{d},{\bm{0}}) , where zeros are used for padding so that the length is exactly C max ​ ( n ) C_{\max}(n) .

Let the vocabulary be 𝒱 = Σ {\mathcal{V}}=\Sigma . At decoding step k k , the model has access to the concatenated sequence ( x 1 , x 2 , … , x n , y 1 , y 2 , … , y k ) ∈ Σ n + k , (x_{1},x_{2},\ldots,x_{n},\,y_{1},y_{2},\ldots,y_{k})\in\Sigma^{n+k}, (35) where x = ( x 1 , … , x n ) ∈ Σ n x=(x_{1},\ldots,x_{n})\in\Sigma^{n} denotes the input, and y i y_{i} is the token generated at the i i -th CoT step. For each node v j v_{j} , let v j ​ ( x ) v_{j}(x) denote its value on input x x . We assume that every intermediate output satisfies y i = v n + i ​ ( x ) . y_{i}=v_{n+i}(x). Under this assumption, we prove by induction that the model generates the next token correctly, i.e., y k + 1 = v n + k + 1 ​ ( x ) . y_{k+1}=v_{n+k+1}(x).

##### Embedding

The embedding at position i ∈ [ n + k ] i\in[n+k] , denoted by 𝒉 i ( 0 ) ∈ 𝔽 s ⁡ ( n ) m {\bm{h}}^{(0)}_{i}\in\mathbb{F}_{s(n)}^{m} , where m ≔ | Σ | + | ℱ | + ( 1 + C max ​ ( n ) ) ​ s ​ ( n ) + | Σ | ​ C sum ​ ( n ) m\coloneq|\Sigma|+|\mathcal{F}|+(1+C_{\mathrm{max}}(n))s(n)+|\Sigma|C_{\mathrm{sum}}(n) is defined as 𝒉 i ( 0 ) = ( 𝒆 ⁡ ( v i ​ ( x ) ) , 𝒆 ⁡ ( v i + 1 ) , 𝗌𝖻𝗂𝗇 s ⁡ ( n ) ​ ( i ) , 𝐬𝐛𝐢𝐧𝐩𝐫𝐞𝐝 s ⁡ ( n ) ​ ( v i + 1 ) , 0 | Σ | ​ C sum ​ ( n ) ) , {\bm{h}}^{(0)}_{i}=\left(\bm{e}(v_{i}(x)),\,\bm{e}(v_{i+1}),\,\mathsf{sbin}_{s(n)}(i),\,\bm{\mathrm{sbinpred}}_{s(n)}(v_{i+1}),\,{\bm{0}}_{|\Sigma|C_{\mathrm{sum}}(n)}\right), (36) where 𝒆 : Σ → { 0 , 1 } | Σ | \bm{e}\colon\Sigma\to\{0,1\}^{|\Sigma|} denote the one-hot encoding of the symbol and, 𝐬𝐛𝐢𝐧𝐩𝐫𝐞𝐝 s ⁡ ( n ) ​ ( v ) ∈ 𝔽 s ⁡ ( n ) C max ​ ( n ) ⋅ s ​ ( n ) \bm{\mathrm{sbinpred}}_{s(n)}(v)\in\mathbb{F}^{C_{\mathrm{max}}(n)\cdot s(n)}_{s(n)} encodes the binary representations of the predecessor indices: 𝐬𝐛𝐢𝐧𝐩𝐫𝐞𝐝 s ⁡ ( n ) ​ ( v i ) ≔ ( 𝗌𝖻𝗂𝗇 s ⁡ ( n ) ​ ( pred ​ ( v i ) 0 ) , … , 𝗌𝖻𝗂𝗇 s ⁡ ( n ) ​ ( pred ​ ( v i ) C max ​ ( n ) ) ) . \bm{\mathrm{sbinpred}}_{s(n)}(v_{i})\coloneq\left(\mathsf{sbin}_{s(n)}(\mathrm{pred}(v_{i})_{0}),\,\ldots,\,\mathsf{sbin}_{s(n)}(\mathrm{pred}(v_{i})_{C_{\mathrm{max}}(n)})\right). (37)

This embedding is constructed, for z ∈ Σ z\in\Sigma , as 𝐖𝐄 ⁡ ( z ) = ( 𝒆 ⁡ ( z ) , 0 ) , 𝐏𝐄 ⁡ ( i ) = ( 𝟎 , 𝒆 ⁡ ( v i + 1 ) , 𝗌𝖻𝗂𝗇 s ⁡ ( n ) ​ ( i ) , 𝐬𝐛𝐢𝐧𝐩𝐫𝐞𝐝 s ⁡ ( n ) ​ ( v i + 1 ) , 0 ) . \mathbf{WE}(z)=\left(\bm{e}(z),\,{\bm{0}}\right),\quad\mathbf{PE}(i)=\left({\bm{0}},\,\bm{e}(v_{i+1}),\,\mathsf{sbin}_{s(n)}(i),\,\bm{\mathrm{sbinpred}}_{s(n)}(v_{i+1}),\,\mathbf{0}\right). (38)

##### Attention layer

The first attention layer consists of C max ⁡ ( n ) C_{\mathrm{max}(n)} heads. The h h -th head is configured to attend to the position corresponding to the h h -th predecessor. Specifically, for each position i i and head h ∈ [ C max ⁡ ( n ) ] h\in[C_{\mathrm{max}(n)}] , the attention vectors are defined as: 𝒒 i , h \displaystyle{\bm{q}}_{i,h} = 𝗌𝖻𝗂𝗇 s ⁡ ( n ) ​ ( pred ​ ( v i + 1 ) h ) ⌢ ​ 1 s ⁡ ( n ) , \displaystyle={\mathsf{sbin}_{s(n)}(\mathrm{pred}(v_{i+1})_{h})}^{\frown}{1_{s(n)}}, (39) 𝒌 i , h \displaystyle{\bm{k}}_{i,h} = 2 s ⁡ ( n ) + 1 ⋅ 𝗌𝖻𝗂𝗇 s ⁡ ( n ) ​ ( i ) ⌢ ​ ( − 1 s ⁡ ( n ) ) , \displaystyle=2^{s(n)+1}\cdot{\mathsf{sbin}_{s(n)}(i)}^{\frown}{(-1_{s(n)})}, (40) 𝐯 i , h \displaystyle\mathbf{v}_{i,h} = 𝒆 ​ ( v i ​ ( x ) ) , \displaystyle=\bm{e}(v_{i}(x)), (41) where vectors of different lengths are zero-padded to match the dimension. By Lemma B.5 , each attention head of the last position i = n + k i=n+k retrieves the predecessor’s value of v n + k v_{n+k} 𝒂 n + k , h = 𝒆 ⁡ ( v pred ​ ( v n + k + 1 ) h ​ ( x ) ) {\bm{a}}_{n+k,h}=\bm{e}\bigl(v_{\mathrm{pred}(v_{n+k+1})_{h}}(x)\bigr) (42) With an appropriate output projection 𝑶 {\bm{O}} such that 𝑶 ⁡ ( 𝒂 i , 1 , … , 𝒂 i , H ) = ( 𝟎 , 𝒆 ⁡ ( v pred ​ ( v n + k + 1 ) 0 ​ ( x ) ) , … , 𝒆 ⁡ ( v pred ​ ( v n + k + 1 ) C max ⁡ ( n ) ​ ( x ) ) , 0 ) , {\bm{O}}({\bm{a}}_{i,1},\ldots,{\bm{a}}_{i,H})=({\bm{0}},\,\bm{e}(v_{\mathrm{pred}(v_{n+k+1})_{0}}(x)),\,\ldots,\,\bm{e}(v_{\mathrm{pred}(v_{n+k+1})_{C_{\mathrm{max}(n)}}}(x)),\,{\bm{0}}), (43) the hidden state at position n + k n+k after the attention layer is given by 𝒉 n + k ( 0.5 ) = ( 𝒆 ⁡ ( v n + k ​ ( x ) ) , 𝒆 ⁡ ( v n + k + 1 ) , 𝗌𝖻𝗂𝗇 s ⁡ ( n ) ​ ( n + k ) , 𝐬𝐛𝐢𝐧𝐩𝐫𝐞𝐝 s ⁡ ( n ) ​ ( v n + k + 1 ) CLOSE , \displaystyle{\bm{h}}^{(0.5)}_{n+k}=\Big(\bm{e}(v_{n+k}(x)),\,\bm{e}(v_{n+k+1}),\,\mathsf{sbin}_{s(n)}(n+k),\,\bm{\mathrm{sbinpred}}_{s(n)}(v_{n+k+1}),\, (44) OPEN 𝒆 ⁡ ( v pred ​ ( v n + k + 1 ) 0 ​ ( x ) ) , … , 𝒆 ⁡ ( v pred ​ ( v n + k + 1 ) C max ⁡ ( n ) ​ ( x ) ) ⏟ updated , 𝟎 C sum ​ ( n ) ​ | Σ | ) . \displaystyle\underbrace{\bm{e}(v_{\mathrm{pred}(v_{n+k+1})_{0}}(x)),\,\ldots,\,\bm{e}(v_{\mathrm{pred}(v_{n+k+1})_{C_{\mathrm{max}(n)}}}(x))}_{\text{updated}}\,,{\bm{0}}_{C_{\mathrm{sum}}(n)|\Sigma|}\Big). (45) The second and third attention layers are disabled (i.e., all attention weights are set to zero).

##### Feed-forward layer

By Lemma B.7 , a single feed-forward layer can approximate multiple functions by partitioning the input into blocks. The first feed-forward layer then places the arguments, gathered by attention, into the correct positions. By Lemma B.6 , where the vector 𝒆 i {\bm{e}}_{i} therein corresponds to 𝟏 | Σ | {\bm{1}}_{|\Sigma|} here, the hidden state at the last position, denoted by 𝒉 n + k ( 1 ) {\bm{h}}^{(1)}_{n+k} , becomes ( ( 𝒉 n + k ( 0.5 ) ) 1 : r , ∥ j = 1 | ℱ | ( 𝒆 ( v pred ​ ( v n + k + 1 ) 1 ( x ) ) ⋅ 1 , … , 𝒆 ( v pred ​ ( v n + k + 1 ) C j ​ ( n ) ( x ) ) ⋅ 1 ) , \displaystyle\Big(({\bm{h}}^{(0.5)}_{n+k})_{1:r},\big\|_{j=1}^{|\mathcal{F}|}\,\big(\bm{e}(v_{\mathrm{pred}(v_{n+k+1})_{1}}(x))\cdot 1,\ldots,\bm{e}(v_{\mathrm{pred}(v_{n+k+1})_{C_{j}(n)}}(x))\cdot 1\Big), (46) where r = | Σ | + | ℱ | + ( 1 + C max ) ​ ( n ) ​ s ​ ( n ) r=|\Sigma|+|\mathcal{F}|+(1+C_{\mathrm{max}})(n)s(n) .

By Assumption 3.4 and Lemmas B.8 and B.7 , there exist feed-forward layers FF 2 , FF 3 : 𝔽 s ⁡ ( n ) m → 𝔽 s ⁡ ( n ) m \mathrm{FF}_{2},\mathrm{FF}_{3}:\mathbb{F}_{s(n)}^{m}\to\mathbb{F}_{s(n)}^{m} such that, for every input tuple 𝒙 j ≔ ( x 1 ( j ) , … , x C j ​ ( n ) ( j ) ) ∈ Σ C j ​ ( n ) {\bm{x}}_{j}\coloneq(x^{(j)}_{1},\ldots,x^{(j)}_{C_{j}(n)})\in\Sigma^{C_{j}(n)} for j ∈ [ | ℱ | ] j\in[|\mathcal{F}|] and every 𝒕 ∈ { 0 , 1 } | ℱ | {\bm{t}}\in\{0,1\}^{|\mathcal{F}|} , the composition ℱ ​ ℱ ≔ ( id + FF 3 ) ∘ ( id + FF 2 ) \mathcal{FF}\coloneq(\id+\mathrm{FF}_{3})\circ(\id+\mathrm{FF}_{2}) satisfies ℱ ℱ ( ∗ , 𝒕 , ∗ , ∥ j = 1 | ℱ | ( 𝒆 ( x 1 ( j ) ) , … , 𝒆 ( x C j ​ ( n ) ( j ) ) ) ) = ( ∑ j | ℱ | 𝒕 j ⋅ 𝒆 ( f j ( 𝒙 j ) ) , ∗ ) , \mathcal{FF}\left(*,\,{\bm{t}},\,*,\,\big\|_{j=1}^{|\mathcal{F}|}\,(\bm{e}(x^{(j)}_{1}),\ldots,\bm{e}(x^{(j)}_{C_{j}(n)}))\right)\;=\;\left(\sum^{|\mathcal{F}|}_{j}{\bm{t}}_{j}\cdot\bm{e}(f_{j}({\bm{x}}_{j})),*\right), (47) zwhere ∗ * denotes an unspecified vector. Since the second and third attention layers are disabled, after the third layer, applying the second and third feed-forward layers FF 2 , FF 3 \mathrm{FF}_{2},\mathrm{FF}_{3} , the hidden state becomes 𝒉 n + k ( 3 ) \displaystyle{\bm{h}}^{(3)}_{n+k} = ℱ ​ ℱ ​ ( 𝒉 n + k ( 1 ) ) \displaystyle=\mathcal{FF}\left({\bm{h}}^{(1)}_{n+k}\right) (48) = ℱ ℱ ( ∗ , 𝒆 ( v n + k + 1 ) , ∗ , ∥ j = 1 | ℱ | ( 𝒆 ( v pred ​ ( v n + k + 1 ) 1 ( x ) ) , … , 𝒆 ( v pred ​ ( v n + k + 1 ) C j ​ ( n ) ( x ) ) ) ) \displaystyle=\mathcal{FF}\left(*,\,\bm{e}(v_{n+k+1}),\,*,\,\bigg\|_{j=1}^{|\mathcal{F}|}\,\big(\bm{e}(v_{\mathrm{pred}(v_{n+k+1})_{1}}(x)),\ldots,\bm{e}(v_{\mathrm{pred}(v_{n+k+1})_{C_{j}(n)}}(x))\big)\right) (49) = ( ∑ j = 1 | ℱ | 𝒆 ​ ( v n + k + 1 ) j ⋅ 𝒆 ⁡ ( f j ​ ( 𝒆 ⁡ ( v pred ​ ( v n + k + 1 ) 1 ​ ( x ) ) , … , 𝒆 ⁡ ( v pred ​ ( v n + k + 1 ) C j ​ ( n ) ​ ( x ) ) ) ) , ∗ ) \displaystyle=\Biggl(\sum_{j=1}^{|\mathcal{F}|}\bm{e}(v_{n+k+1})_{j}\cdot\bm{e}\Big(f_{j}\big(\bm{e}(v_{\mathrm{pred}(v_{n+k+1})_{1}}(x)),\ldots,\bm{e}(v_{\mathrm{pred}(v_{n+k+1})_{C_{j}(n)}}(x))\big)\Big),\;*\Biggr) (50) = ( 𝒆 ⁡ ( f l ​ ( 𝒆 ⁡ ( v pred ​ ( v n + k + 1 ) 1 ​ ( x ) ) , … , 𝒆 ⁡ ( v pred ​ ( v n + k + 1 ) C l ​ ( n ) ​ ( x ) ) ) ) , ∗ ) , where 𝒆 ⁡ ( v n + k + 1 ) = 𝒆 l \displaystyle=\Biggl(\bm{e}\Big(f_{l}\big(\bm{e}(v_{\mathrm{pred}(v_{n+k+1})_{1}}(x)),\ldots,\bm{e}(v_{\mathrm{pred}(v_{n+k+1})_{C_{l}(n)}}(x))\big)\Big),\;*\Biggr),\,\text{where}\quad\bm{e}(v_{n+k+1})={\bm{e}}_{l} (51) = ( 𝒆 ⁡ ( v n + k + 1 ​ ( x ) ) , ∗ ) . \displaystyle=\Big(\bm{e}\big(v_{n+k+1}(x)\big),\;*\Big). (52)

##### Output layer

The final output is given by 𝒉 n + k = 𝐎𝐔𝐓 ⁡ ( 𝒉 n + k ( 3 ) ) = [ 𝑰 | Σ | 𝟎 ] ​ 𝒉 n + k ( 3 ) = 𝒆 ⁡ ( v n + k + 1 ​ ( x ) ) . {\bm{h}}_{n+k}=\mathbf{OUT}({\bm{h}}^{(3)}_{n+k})=\begin{bmatrix}{\bm{I}}_{|\Sigma|}&\mathbf{0}\end{bmatrix}{\bm{h}}^{(3)}_{n+k}=\bm{e}\!\left(v_{n+k+1}(x)\right). (53) The decoding function then outputs the symbol corresponding to the maximum score, y n + k + 1 = Dec ⁡ ( 𝒉 n + k ) = arg ⁡ max j ∈ [ | Σ | ] ⁡ 𝒆 ⁡ ( v n + k + 1 ​ ( x ) ) = v n + k + 1 ​ ( x ) . y_{n+k+1}=\mathrm{Dec}({\bm{h}}_{n+k})=\arg\max_{j\in[|\Sigma|]}\bm{e}(v_{n+k+1}(x))=v_{n+k+1}(x). (54) By induction on k k , the model computes the values at all nodes in topological order. The parameter size of the model is determined by the requirements of the feedforward layers, O ⁡ ( ff ​ _ ​ param ​ ( G n ) ) . O(\mathrm{ff\_param}(G_{n}))\,. While the dimensions and heads of the attention layers depend on C max ​ ( n ) C_{\max}(n) , which is precisely what is already required for the feedforward layers to approximate the target functions. ∎

### B.5 Proof of Theorem 3.6 for Looped Transformer

###### Proof.

In the proof, we assume that the computation graph contains at most n n output nodes. This assumption is without loss of generality: if the number of output nodes exceeds the number of input nodes, we can simply pad the input with dummy nodes (e.g., fixed zeros), thereby reducing the setting to the same case.

We construct a model in which (1) the attention layer aggregates the inputs, and (2) the looped feed-forward layer performs the computation of all nodes in parallel, as illustrated in Figure 9 . We first show that a feedforward layer followed by an attention layer can copy all input tokens to each position. Assume, given an input sequence x = ( x 1 , x 2 , … , x n ) ∈ Σ n x=(x_{1},x_{2},\ldots,x_{n})\in\Sigma^{n} and one-hot encoding 𝒆 : Σ → { 0 , 1 } | Σ | \bm{e}:\Sigma\to\{0,1\}^{|\Sigma|} . Assume each input at position i ∈ [ n ] i\in[n] is embedded as 𝒉 i = ( 0 , 𝒆 ⁡ ( x i ) , 𝒆 i ) ∈ { 0 , 1 } n ​ | Σ | + | Σ | + n , {\bm{h}}_{i}=\bigl(\,{\bm{0}},\;\bm{e}(x_{i}),\;{\bm{e}}_{i}\,\bigr)\in\{0,1\}^{n|\Sigma|+|\Sigma|+n}, (55) where 𝒆 i ∈ { 0 , 1 } n {\bm{e}}_{i}\in\{0,1\}^{n} . By Lemma B.6 , when substituting 𝒙 = ( 𝒆 ⁡ ( x 1 ) , … , 𝒆 ⁡ ( x n ) ) {\bm{x}}=(\bm{e}(x_{1}),\ldots,\bm{e}(x_{n})) into the lemma, there exists a feed-forward layer FF 1 \mathrm{FF}_{1} such that ( id + FF 1 ) ​ ( 𝒉 i ) = ( ( 𝒆 i ) 1 ⋅ 𝒆 ⁡ ( x i ) , ( 𝒆 i ) 2 ⋅ 𝒆 ⁡ ( x i ) , … , ( 𝒆 i ) n ⋅ 𝒆 ⁡ ( x i ) , 𝒆 ⁡ ( x i ) , 𝒆 i ) . (\id+\mathrm{FF}_{1})({\bm{h}}_{i})=\bigl(\,({\bm{e}}_{i})_{1}\cdot\bm{e}(x_{i}),\;({\bm{e}}_{i})_{2}\cdot\bm{e}(x_{i}),\;\ldots,\;({\bm{e}}_{i})_{n}\cdot\bm{e}(x_{i}),\;\bm{e}(x_{i}),\;{\bm{e}}_{i}\,\bigr). (56) To aggregate all positions via uniform attention, we use a single-head attention layer with: 𝐪 i = 𝒌 i = 𝟏 n ​ | Σ | , 𝐯 i = n ⁡ ( ( 𝒆 i ) 1 ⋅ 𝒆 ⁡ ( x i ) , ( 𝒆 i ) 2 ⋅ 𝒆 ⁡ ( x i ) , … , ( 𝒆 i ) n ⋅ 𝒆 ⁡ ( x i ) ) for all ​ i ∈ [ n ] , \mathbf{q}_{i}={\bm{k}}_{i}=\mathbf{1}_{n|\Sigma|},\quad\mathbf{v}_{i}=n\big(({\bm{e}}_{i})_{1}\cdot\bm{e}(x_{i}),\;({\bm{e}}_{i})_{2}\cdot\bm{e}(x_{i}),\;\ldots,\;({\bm{e}}_{i})_{n}\cdot\bm{e}(x_{i})\big)\quad\text{for all }i\in[n], (57) with an appropriate output projection, the output of the attention layer, at position i i , becomes 1 n ​ ∑ j = 1 n 1 ⋅ n ​ 𝒉 j \displaystyle\frac{1}{n}\sum^{n}_{j=1}1\cdot n{\bm{h}}_{j} = ( ∑ j = 1 n ( 𝒆 j ) 1 ​ 𝒆 ​ ( x j ) , ∑ j = 1 n ( 𝒆 j ) 2 ​ 𝒆 ​ ( x j ) , … , ∑ j = 1 n ( 𝒆 j ) n ​ 𝒆 ​ ( x j ) ) \displaystyle\;=\;\Bigl(\sum_{j=1}^{n}({\bm{e}}_{j})_{1}\,\bm{e}(x_{j}),\;\;\sum_{j=1}^{n}({\bm{e}}_{j})_{2}\,\bm{e}(x_{j}),\;\;\ldots,\;\;\sum_{j=1}^{n}({\bm{e}}_{j})_{n}\,\bm{e}(x_{j})\Bigr) (58) = ( 𝒆 ⁡ ( x 1 ) , 𝒆 ⁡ ( x 2 ) , … , 𝒆 ⁡ ( x n ) ) . \displaystyle\;=\;\bigl(\,\bm{e}(x_{1}),\;\bm{e}(x_{2}),\;\ldots,\;\bm{e}(x_{n})\,\bigr). (59)

Then, we show that the feed-forward layer can encode the entire computation graph into its weights and simulate all nodes simultaneously. Let the flag vector for each node be ( t 1 , … , t N ) ∈ { 0 , 1 } N (t_{1},\ldots,t_{N})\in\{0,1\}^{N} , where N ≔ | V n | = size ⁡ ( G n ) N\coloneqq|V_{n}|=\mathrm{size}(G_{n}) . By Lemmas B.7 and B.8 , there exist feed-forward layers FF 2 , FF 3 : 𝔽 s N ⁡ ( | Σ | + 1 ) → 𝔽 s N ⁡ ( | Σ | + 1 ) \mathrm{FF}_{2},\mathrm{FF}_{3}:\mathbb{F}_{s}^{N(|\Sigma|+1)}\to\mathbb{F}_{s}^{N(|\Sigma|+1)} such that, for the input vector ( z 1 , … , z N ) ∈ Σ N . (z_{1},\ldots,z_{N})\in\Sigma^{N}. , ℱ ​ ℱ ​ ( 𝒆 ⁡ ( z 1 ) , t 1 , … , 𝒆 ⁡ ( z N ​ ( x ) ) , t N ) \displaystyle\mathcal{FF}\Bigl(\,\bm{e}(z_{1}),t_{1},\ldots,\bm{e}(z_{N}(x)),t_{N}\Bigr) = ∥ i = 1 N ( t i ⋅ 𝒆 ( f v i ( 𝒛 ( i ) ) ) , 1 m i ∑ j = 1 m i t p i , j ) , \displaystyle=\big\|_{i=1}^{N}\,\Bigl(t_{i}\cdot\bm{e}\bigl(f_{v_{i}}({\bm{z}}^{(i)})\bigr),\;\frac{1}{m_{i}}\sum_{j=1}^{m_{i}}t_{p_{i,j}}\Bigr), (60) where ℱ ​ ℱ ≔ ( id + FF 3 ) ∘ ( id + FF 2 ) \mathcal{FF}\coloneq(\id+\mathrm{FF}_{3})\circ(\id+\mathrm{FF}_{2}) . Here, f v i f_{v_{i}} denotes the function associated with node v i v_{i} , and p i , 1 , … , p i , m i p_{i,1},\ldots,p_{i,m_{i}} denote the indices of the predecessor nodes of v i v_{i} , and 𝒛 ( i ) = ( z p i , 1 , … , z p i , m i ) {\bm{z}}^{(i)}=(z_{p_{i,1}},\ldots,z_{p_{i,m_{i}}}) denotes their values. The last term 1 m i ​ ∑ j = 1 m i t p i , j \frac{1}{m_{i}}\sum_{j=1}^{m_{i}}t_{p_{i,j}} can be obtained using a linear layer.

For the k k -th loop, assume by induction that the hidden state is 𝒉 ⁡ ( k ) ≔ ( t 1 , k − 1 ⋅ 𝒆 ⁡ ( v 1 ​ ( x ) ) , t 1 , k , t 2 , k − 1 ⋅ 𝒆 ⁡ ( v 2 ​ ( x ) ) , t 2 , k , … , t N , k − 1 ⋅ 𝒆 ⁡ ( v N ​ ( x ) ) , t N , k ) , {\bm{h}}(k)\coloneq\bigl(t_{1,k-1}\cdot\bm{e}(v_{1}(x)),\,t_{1,k},\,t_{2,k-1}\cdot\bm{e}(v_{2}(x)),\,t_{2,k},\,\ldots,\,t_{N,k-1}\cdot\bm{e}(v_{N}(x)),\,t_{N,k}\bigr), (61) where v i ​ ( x ) ∈ Σ v_{i}(x)\in\Sigma denotes the value computed by node v i v_{i} given the input x x , and t i , k ∈ { 0 , 1 } t_{i,k}\in\{0,1\} indicates whether node v i v_{i} lies within depth at most k k . Under this assumption, it holds that ℱ ​ ℱ ​ ( 𝒉 ⁡ ( k ) ) \displaystyle\mathcal{FF}({\bm{h}}(k)) = ∥ i = 1 N ( t i , k ⋅ 𝒆 ( f v i ( v p i , 1 ( x ) , v p i , 2 ( x ) , … , v p i , m i ( x ) ) ) , 1 m i ∑ j = 1 m i t ( p i , j , k ) ) , \displaystyle\;=\;\big\|_{i=1}^{N}\,\Bigl(t_{i,k}\cdot\bm{e}\bigl(f_{v_{i}}(v_{p_{i,1}}(x),v_{p_{i,2}}(x),\ldots,v_{p_{i,m_{i}}}(x))\bigr),\;\frac{1}{m_{i}}\sum_{j=1}^{m_{i}}t_{(p_{i,j},k)}\Bigr), (62) = ∥ i = 1 N ( t i , k ⋅ 𝒆 ( v i ( x ) ) ) , t i , k + 1 ) = 𝒉 ( k + 1 ) . \displaystyle\;=\;\big\|_{i=1}^{N}\,\Bigl(t_{i,k}\cdot\bm{e}\bigl(v_{i}(x))\bigr),\;t_{i,k+1}\Bigr)\;=\;{\bm{h}}(k+1). (63)

To extract the output node corresponding to each position denoted by o i o_{i} , in the final loop iteration, by Lemma B.6 , there exists a feedforward layer FF 4 \mathrm{FF}_{4} such that ( id + FF 4 ) ​ ( 𝒉 ⁡ ( k ) , 𝒆 o i ) = ( t o i , k ⋅ 𝒆 ⁡ ( v o i ​ ( x ) ) , ∗ ) . (\id+\mathrm{FF}_{4})({\bm{h}}(k),{\bm{e}}_{o_{i}})=\bigl(t_{o_{i},k}\cdot\bm{e}(v_{o_{i}}(x)),\;*\bigr)\,. (64)

##### Summary

We construct the looped model as follows. Each input token x i ∈ Σ x_{i}\in\Sigma at position i ∈ [ n ] i\in[n] is embedded as 𝒉 i ( 0 ) = ( 𝒆 i , 𝒆 o i , 𝒆 ⁡ ( x i ) , 0 , 𝒆 ⁡ ( x i ) , 0 , … , 𝒆 ⁡ ( x i ) , 0 , 0 ( 1 + | Σ | ) ​ ( N − n ) + | Σ | ) ∈ { 0 , 1 } 2 ​ n + ( 1 + | Σ | ) ​ N + | Σ | . {\bm{h}}^{(0)}_{i}=\bigl(\,{\bm{e}}_{i},\;{\bm{e}}_{o_{i}},\;\bm{e}(x_{i}),\;0,\;\bm{e}(x_{i}),\;0,\;\ldots,\;\bm{e}(x_{i}),\;0,\;{\bm{0}}_{(1+|\Sigma|)(N-n)+|\Sigma|}\bigr)\in\{0,1\}^{2n+(1+|\Sigma|)N+|\Sigma|}. (65)

The first attention layer is an identity map, while the first feedforward layers compute 𝒉 i ( 1 ) = ( 𝒆 i , 𝒆 o i , ( 𝒆 i ) 1 ⋅ 𝒆 ⁡ ( x i ) , 0 , ( 𝒆 i ) 2 ⋅ 𝒆 ⁡ ( x i ) , 0 , … , ( 𝒆 i ) n ⋅ 𝒆 ⁡ ( x i ) , 0 , 0 ( 1 + | Σ | ) ​ ( N − n ) + | Σ | ) . {\bm{h}}^{(1)}_{i}\;=\;\bigl(\,{\bm{e}}_{i},\;{\bm{e}}_{o_{i}},\;({\bm{e}}_{i})_{1}\cdot\bm{e}(x_{i}),\;0,\;({\bm{e}}_{i})_{2}\cdot\bm{e}(x_{i}),\;0,\;\ldots,\;({\bm{e}}_{i})_{n}\cdot\bm{e}(x_{i}),\;0,\;{\bm{0}}_{(1+|\Sigma|)(N-n)+|\Sigma|}\,\bigr). (66)

The second attention layer uniformly gathers all positions and appends a constant 1 1 to each block: 𝒉 i ( 1.5 ) \displaystyle{\bm{h}}^{(1.5)}_{i} = ( 𝒆 i , 𝒆 o i , 𝒆 ⁡ ( x 1 ) , 1 , 𝒆 ⁡ ( x 2 ) , 1 , … , 𝒆 ⁡ ( x n ) , 1 , 0 ( 1 + | Σ | ) ​ ( N − n ) + | Σ | ) \displaystyle\;=\;\bigl(\,{\bm{e}}_{i},\;{\bm{e}}_{o_{i}},\;\bm{e}(x_{1}),\;1,\;\bm{e}(x_{2}),\;1,\;\ldots,\;\bm{e}(x_{n}),\;1,\;{\bm{0}}_{(1+|\Sigma|)(N-n)+|\Sigma|}\,\bigr) (67) = ( 𝒆 i , 𝒆 o i , 𝒉 ⁡ ( 0 ) , 0 | Σ | ) . \displaystyle\;=\;\bigl(\,{\bm{e}}_{i},\;{\bm{e}}_{o_{i}},\;{\bm{h}}(0),\;{\bm{0}}_{|\Sigma|}\,\bigr). (68)

We now proceed by induction. Assume that at the k k -th iteration, the output after the second attention layer at position i i is 𝒉 k , i ( 1.5 ) = ( 𝒆 i , 𝒆 o i , 𝒉 ⁡ ( k ) , t o i , k − 1 ⋅ 𝒆 ⁡ ( v o i ​ ( x ) ) ) , {\bm{h}}^{(1.5)}_{k,i}\;=\;\bigl(\,{\bm{e}}_{i},\;{\bm{e}}_{o_{i}},\;{\bm{h}}(k),\;t_{o_{i},k-1}\cdot\bm{e}(v_{o_{i}}(x))\bigr), (69) where t o i , k − 1 ≔ ( 𝒉 k − 1 , i ( 1.5 ) ) 2 ​ n + ( 1 + | Σ | ) ​ ( o i − 1 ) t_{o_{i},k-1}\coloneq\bigl({\bm{h}}^{(1.5)}_{k-1,i}\bigr)_{\,2n+(1+|\Sigma|)(o_{i}-1)} denotes the indicator flag showing whether the o i o_{i} -th node has been reached, i.e., whether it lies at depth k − 1 k-1 .

After passing through the second feedforward layer, the third attention layer with all weights set to zero, and the third feedforward layer, the hidden state updates to 𝒉 k , i ( 3 ) = ( 𝒆 i , 𝒆 o i , 𝒉 ⁡ ( k + 1 ) , t o i , k − 1 ⋅ 𝒆 ⁡ ( v o i ​ ( x ) ) ) . {\bm{h}}^{(3)}_{k,i}\;=\;\bigl(\,{\bm{e}}_{i},\;{\bm{e}}_{o_{i}},\;{\bm{h}}(k+1),\;t_{o_{i},k-1}\cdot\bm{e}(v_{o_{i}}(x))\,\bigr). (70)

After the fourth feedforward layer, the hidden state becomes 𝒉 k , i ( 4 ) = ( 𝒆 i , 𝒆 o i , 𝒉 ⁡ ( k + 1 ) , t o i , k ⋅ 𝒆 ⁡ ( v o i ​ ( x ) ) ) . {\bm{h}}^{(4)}_{k,i}\;=\;\bigl(\,{\bm{e}}_{i},\;{\bm{e}}_{o_{i}},\;{\bm{h}}(k+1),\;t_{o_{i},k}\cdot\bm{e}(v_{o_{i}}(x))\bigr). (71)

By induction, after the final iteration of depth depth ⁡ ( G n ) \mathrm{depth}(G_{n}) of the computation graph G n G_{n} , we obtain 𝒉 depth ⁡ ( G n ) , i ( 4 ) = ( ∗ , t o i , depth ⁡ ( G n ) ⋅ 𝒆 ⁡ ( v o i ​ ( x ) ) ) = ( ∗ , 𝒆 ⁡ ( v o i ​ ( x ) ) ) . {\bm{h}}^{(4)}_{\mathrm{depth}(G_{n}),i}\;=\;\bigl(\,*,\;t_{o_{i},\mathrm{depth}(G_{n})}\cdot\bm{e}(v_{o_{i}}(x))\bigr)\;=\;\bigl(\,*,\;\bm{e}(v_{o_{i}}(x))\bigr). (72)

The final output is given by z i = 𝐎𝐔𝐓 ⁡ ( 𝒉 depth ⁡ ( G n ) , i ( 4 ) ) = [ 𝟎 𝑰 | Σ | ] ⁡ ( 𝒉 depth ⁡ ( G n ) , i ( 4 ) ) = 𝒆 ⁡ ( v o i ​ ( x ) ) . z_{i}=\mathbf{OUT}({\bm{h}}^{(4)}_{\mathrm{depth}(G_{n}),i})=\begin{bmatrix}{\bm{0}}&{\bm{I}}_{|\Sigma|}\end{bmatrix}({\bm{h}}^{(4)}_{\mathrm{depth}(G_{n}),i})=\bm{e}(v_{o_{i}}(x)). (73)

The decoding function then selects the symbol corresponding to the maximum score: y i = Dec ⁡ ( z i ) = arg ⁡ max j ∈ [ | Σ | ] ⁡ ( 𝒆 ⁡ ( v o i ​ ( x ) ) ) j = v o i ​ ( x ) . y_{i}\;=\;\mathrm{Dec}(z_{i})=\arg\max_{j\in[|\Sigma|]}\,\bigl(\bm{e}(v_{o_{i}}(x))\bigr)_{j}=v_{o_{i}}(x). (74)

The parameter size grows proportionally with the input dimension size ⁡ ( G n ) \mathrm{size}(G_{n}) , since the function must be approximated along each dimension. Therefore, it can be bounded by O ⁡ ( ff ​ _ ​ param ​ ( G n ) ⋅ size ⁡ ( G n ) ) . O\!\left(\mathrm{ff\_param}(G_{n})\cdot\mathrm{size}(G_{n})\right). ∎

Discussion: Our proof compresses the entire input into a single position before applying an arbitrary feed-forward computation, which may appear to deviate from the standard Transformer architecture. An alternative approach is to distribute computation across multiple positions, as shown by ( Sanford et al., 2024b ) , which can reduce the required embedding dimension. We nevertheless adopt the single-position construction to isolate the core characteristics of looped models: attention is used purely as an information aggregation mechanism, a single Transformer layer suffices, and all computation is carried out by the feed-forward network in latent space. This latent-space computation is strictly more expressive than computation in the language space. This is supported by recent work for looped ReLUs ( Liang et al., 2024 ) .

### B.6 Proof of Theorem 3.6 for Continuous Thought

###### Proof.

The proofs are based on the construction for CoT and looped TF. Let the vocabulary be 𝒱 = Σ {\mathcal{V}}=\Sigma and each node v ∈ V n v\in V_{n} is labeled by a one-hot vector 𝒆 ⁡ ( v ) ∈ { 0 , 1 } | ℱ | \bm{e}(v)\in\{0,1\}^{|\mathcal{F}|} . At decoding step k k , the model has access to the concatenated sequence ( x 1 , x 2 , … , x n , h 1 , h 2 , … , h k ) (x_{1},x_{2},\ldots,x_{n},\,h_{1},h_{2},\ldots,h_{k}) (75) where x = ( x 1 , … , x n ) ∈ Σ n x=(x_{1},\ldots,x_{n})\in\Sigma^{n} denotes the input, and h i ∈ 𝔽 s m h_{i}\in\mathbb{F}_{s}^{m} is the hidden state generated at the i i -th Coconut step. For each node v j v_{j} , let v j ​ ( x ) v_{j}(x) denote its value on input x x . We assume that h k ≔ ( t 1 , k − 1 ⋅ 𝒆 ⁡ ( v 1 ​ ( x ) ) , t 1 , k , t 2 , k − 1 ⋅ 𝒆 ⁡ ( v 2 ​ ( x ) ) , t 2 , k , … , t N , k − 1 ⋅ 𝒆 ⁡ ( v N ​ ( x ) ) , t N , k , 𝒆 k ′ , 0 | Σ | ) , h_{k}\coloneq\bigl(t_{1,k-1}\cdot\bm{e}(v_{1}(x)),\,t_{1,k},\,t_{2,k-1}\cdot\bm{e}(v_{2}(x)),\,t_{2,k},\,\ldots,\,t_{N,k-1}\cdot\bm{e}(v_{N}(x)),\,t_{N,k},\,{\bm{e}}^{\prime}_{k},\,{\bm{0}}_{|\Sigma|}\bigr), where N ≔ size ⁡ ( G n ) N\coloneqq\mathrm{size}(G_{n}) , t i , k ∈ { 0 , 1 } t_{i,k}\in\{0,1\} indicates whether node v i v_{i} lies within depth at most k k , and 𝒆 : Σ → { 0 , 1 } | Σ | \bm{e}:\Sigma\to\{0,1\}^{|\Sigma|} denotes one-hot encoding, and the vector 𝒆 k ′ ∈ { 0 , 1 } N {\bm{e}}^{\prime}_{k}\in\{0,1\}^{N} is defined by 𝒆 k ′ = { 𝟎 k < depth ⁡ ( G n ) , 𝒆 ⁡ ( v o i ) k = depth ⁡ ( G n ) + i , {\bm{e}}^{\prime}_{k}=\begin{cases}\mathbf{0}&k<\mathrm{depth}(G_{n}),\\[4.0pt] \bm{e}(v_{o_{i}})&k=\mathrm{depth}(G_{n})+i,\end{cases} (76) where v o i v_{o_{i}} denotes the i i -th output node, and 𝒆 k ′ {\bm{e}}^{\prime}_{k} can be encoded by positional embeddings. Under this assumption, we prove by induction that the model generates h k + 1 ​ ( x ) h_{k+1}(x) .

We first consider the base case k = 1 k=1 , in which the model receives only 𝒙 {\bm{x}} . We focus on the final token. Using the same construction as in the looped TF, we can show that a single feed-forward layer followed by an attention layer suffices to copy all input tokens to every position. Specifically, the hidden representation at the last position becomes h 1 = ( 𝒆 ( v 1 ( x ) ) , 1 , … , 𝒆 ( v n ( x ) ) , 1 , 0 , 1 , 0 , 𝒆 0 ′ , 0 ) , h_{1}=\bigl(\bm{e}(v_{1}(x)),\,1,\,\ldots,\,\bm{e}(v_{n}(x)),\,1,\,{\bm{0}},\ 1,\,{\bm{0}},\,{\bm{e}}^{\prime}_{0},\,{\bm{0}}\bigl), (77) where v i ​ ( x ) = x i v_{i}(x)=x_{i} for all i ∈ [ n ] i\in[n] , corresponding to the input nodes. In what follows, we consider the case k > 1 k>1 . By the same argument as for Looped TF, based on Equation 62 , we show that the feed-forward layers can encode the entire computation graph into their weights and simulate all nodes simultaneously. That is, there exist two feed-forward layers whose composition, denoted by ℱ ​ ℱ \mathcal{FF} , satisfies ℱ ​ ℱ ​ ( h k ) = h k + 1 . \mathcal{FF}(h_{k})=h_{k+1}.

Consider the last feed-forward layer applied after the zero-weight attention layer. By substituting 𝒆 i = 𝒆 k ′ {\bm{e}}_{i}={\bm{e}}_{k}^{\prime} and 𝒙 = ( h k ) 1 : m − | Σ | {\bm{x}}={(h_{k})}_{1:m-|\Sigma|} into Lemma B.6 , there exists a feed-forward network FF \mathrm{FF} such that ( id + FF ) ( h k ) = { h k + 1 , if ​ k < depth ⁡ ( G n ) , ( ( h k + 1 ) 1 : m − | Σ | , 𝒆 ( v o i ( x ) ) ) , if ​ k = depth ⁡ ( G n ) + i . (\id+\mathrm{FF})(h_{k})=\begin{cases}h_{k+1},&\text{if }k<\mathrm{depth}(G_{n}),\\[6.0pt] \Bigl({(h_{k+1})}_{1:m-|\Sigma|},\,\bm{e}(v_{o_{i}}(x))\Bigr),&\text{if }k=\mathrm{depth}(G_{n})+i.\end{cases} (78) In particular, for all k < depth ⁡ ( G n ) k<\mathrm{depth}(G_{n}) , the output of the last token, for the input ( x 1 , x 2 , … , x n , h 1 , h 2 , … , h k ) (x_{1},x_{2},\ldots,x_{n},\;h_{1},h_{2},\ldots,h_{k}) is h k + 1 h_{k+1} . For the final positions corresponding to output nodes, namely k = depth ⁡ ( G n ) + i k=\mathrm{depth}(G_{n})+i , the hidden state 𝒉 k {\bm{h}}_{k} contains the embedding of the output symbol v o i ​ ( x ) v_{o_{i}}(x) . Applying the output projection yields 𝐎𝐔𝐓 ⁡ ( 𝒉 k ) = [ 𝟎 𝑰 | Σ | ] ​ 𝒉 k = 𝒆 ⁡ ( v o i ​ ( x ) ) . \mathbf{OUT}({\bm{h}}_{k})=\begin{bmatrix}\mathbf{0}&{\bm{I}}_{|\Sigma|}\end{bmatrix}{\bm{h}}_{k}=\bm{e}\!\left(v_{o_{i}}(x)\right). (79)

Finally, the decoding function outputs the symbol in Σ \Sigma corresponding to the maximum coordinate of 𝐎𝐔𝐓 ⁡ ( 𝒉 k ) \mathbf{OUT}({\bm{h}}_{k}) . ∎

### B.7 Proof for Theorem 3.12

For the upper bound 𝖫𝗈𝗈𝗉 [ log k n , 𝗉𝗈𝗅𝗒 ( n ) , 1 (resp. log n ) ] ⊆ 𝖠𝖢 k (resp. 𝖳𝖢 k ) , \mathsf{Loop}[\log^{k}n,\,\mathsf{poly}(n),\,1\ \textup{(resp.\ }\log n)]\subseteq\mathsf{AC}^{k}\ \textup{(resp.\ }\mathsf{TC}^{k}), we follow the argument of ( Li et al., 2024 ) . Their key observation is that a restricted form of automaton can model iterative computation under constant precision: the rounding operation preserves monotonicity, and constant precision yields counter-free, restricted state spaces, which are therefore computable by 𝖠𝖢 0 \mathsf{AC}^{0} circuits. In the case of polynomial precision, prefix summation can be simulated by 𝖳𝖢 0 \mathsf{TC}^{0} , which also allows the detection and correction of rounding in floating-point arithmetic.

###### Theorem B.9 ( Li et al., 2024 ) .

For s ⁡ ( n ) ∈ 𝗉𝗈𝗅𝗒 ⁡ ( n ) s(n)\in\mathsf{poly}(n) , sum s ⁡ ( n ) : ( 𝔽 s ⁡ ( n ) ) n → 𝔽 s ⁡ ( n ) \mathrm{sum}_{s(n)}:(\mathbb{F}_{s(n)})^{n}\to\mathbb{F}_{s(n)} is computable by 𝖳𝖢 0 \mathsf{TC}^{0} circuits, and by 𝖠𝖢 0 \mathsf{AC}^{0} circuits when s ⁡ ( n ) s(n) is constant.

It has also been shown that gates can be efficiently simulated by feedforward layers.

###### Lemma B.10 ( Li et al., 2024 ) .

Unbounded-fanin and , 𝖮𝖱 \and,\mathsf{OR} (resp. 𝑂𝑃𝐸𝑁 𝖬𝖠𝖩𝖮𝖱𝖨𝖳𝖸 ) : { 0 , 1 } n → { 0 , 1 } \mathsf{MAJORITY}):\{0,1\}^{n}\to\{0,1\} can be simulated by a two-layer feedforward ReLU network with constant (resp. log ⁡ n \log{n} ) bits of precision constant hidden dimension and additional n n constant inputs of value 1 1 .

###### Proof for Theorem 3.12 .

𝖫𝗈𝗈𝗉 [ log k n , 𝗉𝗈𝗅𝗒 ( n ) , 1 (resp. log n ) ] ⊆ 𝖠𝖢 k (resp. 𝖳𝖢 k ) : \mathsf{Loop}[\log^{k}n,\,\mathsf{poly}(n),\,1\ \textup{(resp.\ }\log n)]\subseteq\mathsf{AC}^{k}\ \textup{(resp.\ }\mathsf{TC}^{k}): In Transformers, constant-depth computation is defined by Summation with Iterative Rounding (see Definition B.3 ), which by Theorem B.9 can be simulated in 𝖠𝖢 0 \mathsf{AC}^{0} (resp. 𝖳𝖢 0 \mathsf{TC}^{0} ). A looped TF simply stacks these computations vertically through iteration, and thus the result follows.

𝖠𝖢 k (resp. 𝖳𝖢 k ) ⊆ 𝖫𝗈𝗈𝗉 [ log k n , 𝗉𝗈𝗅𝗒 ( n ) , 1 (resp. log n ) ] : \mathsf{AC}^{k}\ \textup{(resp.\ }\mathsf{TC}^{k})\subseteq\mathsf{Loop}[\log^{k}n,\,\mathsf{poly}(n),\,1\ \textup{(resp.\ }\log n)]: Since Boolean circuits are DAGs, the claim follows directly from Theorem 3.10 together with Lemma B.10 . ∎

## Appendix C Deferred Proofs for Section 4

### C.1 Definition for Models of Computation

We model a language model as a probabilistic process that, given an input and a generated prefix, produces either an internal reasoning state or an output token. This process induces a probability distribution over final outputs. We first formalize CoT under this setting. We focus on the saturated hardmax attention as in ( Merrill et al., 2022 ; Nowak et al., 2024 ) .

###### Definition C.1 (Language model with CoT) .

Let 𝒱 {\mathcal{V}} be a vocabulary. Given an input x ∈ 𝒱 ∗ x\in{\mathcal{V}}^{*} , a language model with CoT stochastically generates a sequence of output blocks of the form ( r 1 , e , y 1 , e ′ , r 2 , e , y 2 , e ′ , ⋯ r m , e , y m , e ′ ) , \Big(r_{1},\,e,\,y_{1},\,e^{\prime},\;r_{2},\,e,\,y_{2},\,e^{\prime},\;\cdots\;r_{m},\,e,\,y_{m},\,e^{\prime}\Big), (80) where each r i ∈ 𝒱 ∗ r_{i}\in{\mathcal{V}}^{*} represents an explicit reasoning trace, y i ∈ 𝒱 y_{i}\in{\mathcal{V}} is an output token, and e , e ′ ∈ 𝒱 e,e^{\prime}\in{\mathcal{V}} are special delimiter tokens. The final output is the string y 1 ⋯ y m y_{1}\cdots y_{m} . Generation proceeds autoregressively: at iteration i i , the model generates a reasoning segment r i r_{i} followed by an output token y i y_{i} , conditioned on the input x x , the previously generated outputs y < i y_{<i} , and prior reasoning segments r < i r_{<i} . We denote by p ⁡ ( y ∣ x ) p(y\mid x) the resulting distribution over final outputs.

Then we define the language models with latent thought reasoning: Coconut and looped TF.

###### Definition C.2 (Language model with Coconut) .

Let 𝒱 {\mathcal{V}} be a vocabulary. Given an input x ∈ 𝒱 ∗ x\in{\mathcal{V}}^{*} , a language model with Coconut generates a sequence of blocks ( r 1 , y 1 , r 2 , y 2 , … , r m , y m ) , \Big(r_{1},\,y_{1},\,r_{2},\,y_{2},\,\ldots,\,r_{m},\,y_{m}\Big), (81) where each r i ∈ 𝔽 d ∗ r_{i}\in{\mathbb{F}^{d}}^{*} represents an internal continuous reasoning state, and each y i ∈ 𝒱 y_{i}\in{\mathcal{V}} is an output token.

Generation proceeds autoregressively. At each iteration, the internal continuous reasoning state r i r_{i} is generated deterministically as a function of the input x x , the previously generated outputs y < i y_{<i} , and the prior internal states r < i r_{<i} , while the output token y i y_{i} is generated stochastically. The decision of when to emit an output token is determined internally by the model.

For looped TF models, the computation proceeds through internally repeated iterations before producing any output tokens. The number of iterations is determined by the model as a function of the input.

###### Definition C.3 (Language model with looped TF) .

Given an input x ∈ 𝒱 ∗ x\in{\mathcal{V}}^{*} , a looped TF produces an output sequence autoregressively. At each iteration i ∈ [ m ] i\in[m] , the model internally performs a number of repeated transformation steps before emitting an output token y i y_{i} , conditioned on the input x x and the previously generated outputs y < i y_{<i} . The number of internal loop iterations required to generate each output token is determined internally by the model as a function of the input x x and the generated prefix y < i y_{<i} .

We define complexity classes corresponding to language models under different reasoning paradigms. In contrast to the non-uniform models typically used in parallel computation analysis, we adopt a uniform setting analogous to Turing machines: a single model with a fixed set of parameters is applied to all input lengths, while the number of reasoning steps is allowed to grow as a function of the input size n n . Following the convention in ( Merrill and Sabharwal, 2024 ) , we allow O ⁡ ( log ⁡ n ) O(\log n) bits of numerical precision to represent positional embeddings and internal activations. Furthermore, we extend the output space beyond simple binary decisions. Specifically, the model’s output is not restricted to Σ k \Sigma^{k} , but can be an arbitrary finite binary string in Σ ∗ \Sigma^{*} . This extension enables the model to represent functions of the form f : Σ ∗ → ℝ f:\Sigma^{*}\to\mathbb{R} , thereby capturing counting, probabilistic modeling, and approximation tasks.

###### Definition C.4 (Complexity Classes 𝗉𝖢𝗈𝖳 \mathsf{pCoT} , 𝗉𝖢𝖳 \mathsf{pCT} , and 𝗉𝖫𝖮𝖮𝖯 \mathsf{pLOOP} ) .

Let 𝗉𝖢𝗈𝖳 ⁡ [ T ⁡ ( n ) ] \mathsf{pCoT}[T(n)] , 𝗉𝖢𝖳 ⁡ [ T ⁡ ( n ) ] \mathsf{pCT}[T(n)] , and 𝗉𝖫𝖮𝖮𝖯 ⁡ [ T ⁡ ( n ) ] \mathsf{pLOOP}[T(n)] denote the classes of probabilistic computations that define an output distribution p : Σ ∗ × Σ ∗ → [ 0 , 1 ] p:\Sigma^{*}\times\Sigma^{*}\to[0,1] . A function f f belongs to such a class if there exists a language model ℳ \mathcal{M} , employing CoT, Coconut, or looped TF, respectively, such that for any input x ∈ Σ n x\in\Sigma^{n} , the model induces the distribution p ⁡ ( x , ⋅ ) p(x,\cdot) within O ⁡ ( T ⁡ ( n ) ) O(T(n)) steps using O ⁡ ( log ⁡ n ) O(\log n) bits of numerical precision.

### C.2 Lemma: Universality of Chain of Thought

###### Definition C.5 .

A probabilistic Turing machine M = ( Q , Σ , Γ , q 0 , q 1 , δ 1 , δ 2 ) M=(Q,\Sigma,\Gamma,q_{0},q_{1},\delta_{1},\delta_{2}) is defined as: • Q Q is a finite set of states,

• Σ \Sigma is the input/output alphabet,

• Γ \Gamma is the tape alphabet, with Σ ⊆ Γ \Sigma\subseteq\Gamma and a distinguished blank symbol ⊔ ∈ Γ \sqcup\in\Gamma ,

• q 0 ∈ Q q_{0}\in Q denotes the initial state, and q 1 ∈ Q q_{1}\in Q denotes the final state,

• δ 1 , δ 2 : Q × Γ → Q × Γ × ( Σ ∪ { ε } ) × { L , S , R } \delta_{1},\delta_{2}:Q\times\Gamma\to Q\times\Gamma\times(\Sigma\cup\{\varepsilon\})\times\{L,S,R\} are two transition functions.

At each step, M M chooses uniformly at random between δ 1 \delta_{1} and δ 2 \delta_{2} . Each transition δ i ​ ( q , a ) = ( q ′ , b , σ , D ) \delta_{i}(q,a)=(q^{\prime},b,\sigma,D) is interpreted as: writing b ∈ Γ b\in\Gamma on the work tape, writing σ ∈ Σ \sigma\in\Sigma on the output tape, where ε \varepsilon means that nothing is written, and moving the tape head in direction D ∈ { L , S , R } D\in\{L,S,R\} , where L L = left, R R = right, and S S = stay. The output of M M is defined to be the string remaining on the output tape when the machine halts.

Prior work has shown that probabilistic CoT can simulate any such PTM, thereby demonstrating its universality.

###### Lemma C.6 ( Nowak et al., 2024 ) .

Let M M be a PTM with input and output alphabet Σ \Sigma , and running time bounded by T ⁡ ( n ) T(n) on inputs of length n n . Then there exists a log-precision CoT model with stochastic decoding, denoted 𝖢𝗈𝖳 M \mathsf{CoT}_{M} , such that the induced output distribution of 𝖢𝗈𝖳 M \mathsf{CoT}_{M} coincides exactly with that of M M . Formally, for every input string x ∈ Σ ∗ x\in\Sigma^{*} and output string y ∈ Σ ∗ y\in\Sigma^{*} , Pr [ 𝖢𝗈𝖳 M ( x ) = y ] = Pr [ M ( x ) = y ] . \Pr\bigl[\mathsf{CoT}_{M}(x)=y\bigr]\;=\;\Pr\bigl[M(x)=y\bigr]. (82) Moreover, the number of reasoning steps of 𝖢𝗈𝖳 M \mathsf{CoT}_{M} is bounded by 𝗉𝗈𝗅𝗒 ⁡ ( | x | ) \mathsf{poly}(|x|) .

### C.3 Self-Reducibility and Complexity of Approximate Counting

Here, we provide the definitions of relation and associated counting problems.

###### Definition C.7 (Relation) .

A relation over an alphabet Σ \Sigma is a subset R ⊆ Σ ∗ × Σ ∗ . R\subseteq\Sigma^{*}\times\Sigma^{*}. For an input x ∈ Σ ∗ x\in\Sigma^{*} , we denote R ⁡ ( x ) := { y ∈ Σ ∗ : ( x , y ) ∈ R } . R(x):=\{\,y\in\Sigma^{*}:(x,y)\in R\,\}.

###### Definition C.8 (Counting) .

Given a relation R R , the associated counting function is defined as N R : Σ ∗ → ℕ , N R ​ ( x ) := | R ⁡ ( x ) | . N_{R}:\Sigma^{*}\to\mathbb{N},\qquad N_{R}(x):=|R(x)|.

###### Definition C.9 ( p p -relation) .

A relation R ⊆ Σ ∗ × Σ ∗ R\subseteq\Sigma^{*}\times\Sigma^{*} is called a p p -relation if • the membership ( x , y ) ∈ R (x,y)\in R can be decided in time polynomial in | x | |x| , and

• there exists a polynomial p p such that for all ( x , y ) ∈ R (x,y)\in R , we have | y | ≤ p ⁡ ( | x | ) |y|\leq p(|x|) .

###### Definition C.10 .

The extension counting function associated with a relation R ⊆ Σ ∗ × Σ ∗ R\subseteq\Sigma^{*}\times\Sigma^{*} is EXT R : Σ ∗ × Σ ∗ → ℕ , EXT R ⁡ ( x , w ) := | { z ∈ Σ ∗ : ( x , w ​ z ) ∈ R } | . \operatorname{EXT}_{R}:\Sigma^{*}\times\Sigma^{*}\to\mathbb{N},\qquad\operatorname{EXT}_{R}(x,w):=\bigl|\{\,z\in\Sigma^{*}:(x,wz)\in R\,\}\bigr|.

The complexity class # ​ 𝖯 \#\mathsf{P} consists of counting problems associated with p p -relations ( Valiant, 1979 ) . Then, we provide definitions of schemes for approximate counting. In the remainder of this paper, we say that an algorithm produces an output approximating f ⁡ ( x ) f(x) within ratio 1 + ε 1+\varepsilon if its output f ^ ​ ( x ) \hat{f}(x) satisfies ( 1 − ε ) ​ f ​ ( x ) ≤ f ^ ​ ( x ) ≤ ( 1 + ε ) ​ f ​ ( x ) , (1-\varepsilon)f(x)\leq\hat{f}(x)\leq(1+\varepsilon)f(x),

###### Definition C.11 (FPTAS) .

An algorithm is called a fully polynomial-time approximation scheme (FPTAS) for a function f f if, for any input x x and any ε > 0 \varepsilon>0 , it produces an output approximating f ⁡ ( x ) f(x) within ratio 1 + ε 1+\varepsilon , and runs in time polynomial in | x | |x| and 1 / ε 1/\varepsilon .

###### Definition C.12 (FPRAS) .

An algorithm is a fully polynomial-time randomized approximation scheme (FPRAS) for a function f f if, for any input x x and any ε > 0 \varepsilon>0 and δ > 0 \delta>0 , it produces an output approximating f ⁡ ( x ) f(x) within ratio 1 + ε 1+\varepsilon with probability at least 1 − δ 1-\delta , and runs in time polynomial in | x | |x| , 1 / ε 1/\varepsilon , and log ⁡ ( 1 / δ ) \log(1/\delta) .

The following proposition formalizes the relationship between approximate counting and the extension counting function.

###### Proposition C.13 ( Jerrum et al., 1986 ) .

Let R R be a p p -relation and let x ∈ Σ n x\in\Sigma^{n} . Let m = p ⁡ ( n ) m=p(n) and define r = 1 + ε 2 ​ m r=1+\frac{\varepsilon}{2m} . If there exists a FPRAS that approximates Ext R ​ ( x , w ) \mathrm{Ext}_{R}(x,w) within ratio r r for all prefixes w w with probability at least 1 − δ / m 1-\delta/m , then there exists an FPRAS that approximates N R ​ ( x ) N_{R}(x) within ratio 1 + ε 1+\varepsilon with probability at least 1 − δ 1-\delta .

This reduction transforms the global counting problem into a sequence of local estimation steps.

###### Proposition C.14 .

For any 0 < ε ≤ 1 0<\varepsilon\leq 1 and any integer m ≥ 1 m\geq 1 , it holds that ( 1 + ε 2 ​ m ) m < 1 + ε . \left(1+\frac{\varepsilon}{2m}\right)^{m}<1+\varepsilon. (83)

###### Proof.

We use the standard inequality 1 + x ≤ e x 1+x\leq e^{x} , which holds for all x ∈ ℝ x\in\mathbb{R} . Substituting x = ε 2 ​ m x=\frac{\varepsilon}{2m} , we have: ( 1 + ε 2 ​ m ) m ≤ ( exp ⁡ ( ε 2 ​ m ) ) m = e ε / 2 . \left(1+\frac{\varepsilon}{2m}\right)^{m}\leq\left(\exp\left(\frac{\varepsilon}{2m}\right)\right)^{m}=e^{\varepsilon/2}. (84) For 0 < ε ≤ 1 0<\varepsilon\leq 1 , we show that e ε / 2 < 1 + ε e^{\varepsilon/2}<1+\varepsilon . Let f ⁡ ( ε ) = 1 + ε − e ε / 2 f(\varepsilon)=1+\varepsilon-e^{\varepsilon/2} . Then f ⁡ ( 0 ) = 0 f(0)=0 and f ′ ​ ( ε ) = 1 − 1 2 ​ e ε / 2 f^{\prime}(\varepsilon)=1-\frac{1}{2}e^{\varepsilon/2} . Since e ε / 2 ≤ e 1 / 2 < 2 e^{\varepsilon/2}\leq e^{1/2}<2 for all ε ∈ [ 0 , 1 ] \varepsilon\in[0,1] , it follows that f ′ ​ ( ε ) > 0 f^{\prime}(\varepsilon)>0 . Thus, f f is strictly increasing on [ 0 , 1 ] [0,1] , implying f ⁡ ( ε ) > f ⁡ ( 0 ) = 0 f(\varepsilon)>f(0)=0 , or equivalently e ε / 2 < 1 + ε e^{\varepsilon/2}<1+\varepsilon . ∎

###### Proof for Proposition C.13 .

Let x ∈ Σ n x\in\Sigma^{n} and m = p ⁡ ( n ) m=p(n) . We express N R ​ ( x ) N_{R}(x) as a product of m m ratios. Let w = y 1 ​ y 2 ​ … ​ y m w=y_{1}y_{2}\dots y_{m} be a witness, and let w ( i ) w^{(i)} denote its prefix of length i i . We can write: N R ​ ( x ) = Ext R ​ ( x , λ ) = ∏ i = 1 m Ext R ​ ( x , w ( i − 1 ) ) Ext R ​ ( x , w ( i ) ) ⋅ Ext R ​ ( x , w ( m ) ) . N_{R}(x)=\mathrm{Ext}_{R}(x,\lambda)=\prod_{i=1}^{m}\frac{\mathrm{Ext}_{R}(x,w^{(i-1)})}{\mathrm{Ext}_{R}(x,w^{(i)})}\cdot\mathrm{Ext}_{R}(x,w^{(m)}). (85) In the standard self-reducibility framework, we estimate each ratio ρ i = Ext R ​ ( x , w ( i − 1 ) ) / Ext R ​ ( x , w ( i ) ) \rho_{i}=\mathrm{Ext}_{R}(x,w^{(i-1)})/\mathrm{Ext}_{R}(x,w^{(i)}) using the assumed approximation scheme. Let A i A_{i} be the estimator for the i i -th ratio such that: ℙ [ 1 r ≤ A i ρ i ≤ r ] ≥ 1 − δ m . \mathbb{P}\left[\frac{1}{r}\leq\frac{A_{i}}{\rho_{i}}\leq r\right]\geq 1-\frac{\delta}{m}. (86) By the union bound, the probability that at least one of these m m estimations fails to stay within the ratio r r is at most m ⋅ ( δ / m ) = δ m\cdot(\delta/m)=\delta . Therefore, with probability at least 1 − δ 1-\delta , all m m estimations are successful. Under this condition, the final estimate N ^ = ∏ i = 1 m A i \hat{N}=\prod_{i=1}^{m}A_{i} satisfies: 1 r m ≤ N ^ N R ​ ( x ) ≤ r m . \frac{1}{r^{m}}\leq\frac{\hat{N}}{N_{R}(x)}\leq r^{m}. (87) From Proposition C.14 , we have r m = ( 1 + ε 2 ​ m ) m < 1 + ε r^{m}=(1+\frac{\varepsilon}{2m})^{m}<1+\varepsilon . Furthermore, for 0 < ε ≤ 1 0<\varepsilon\leq 1 , it holds that 1 / r m > ( 1 + ε ) − 1 ≥ 1 − ε 1/r^{m}>(1+\varepsilon)^{-1}\geq 1-\varepsilon , ensuring a relative error of at most ε \varepsilon .

Regarding complexity, each of the m m calls to the FPRAS for Ext R \mathrm{Ext}_{R} runs in time poly ⁡ ( n , ( r − 1 ) − 1 , log ⁡ ( m / δ ) ) \mathrm{poly}(n,(r-1)^{-1},\log(m/\delta)) . Substituting r − 1 = ε / 2 ​ m r-1=\varepsilon/2m , the runtime per call is poly ⁡ ( n , m / ε , log ⁡ ( m / δ ) ) \mathrm{poly}(n,m/\varepsilon,\log(m/\delta)) . Since m = p ⁡ ( n ) m=p(n) is a polynomial in n n , the total running time is poly ⁡ ( n , 1 / ε , log ⁡ ( 1 / δ ) ) \mathrm{poly}(n,1/\varepsilon,\log(1/\delta)) , which satisfies the requirements for an FPRAS. ∎

We have shown that approximate counting reduces to approximating the extension counting function . For a general relation R R , however, the connection between the extension counting function and the original counting problem for R R remains unclear. This gap is bridged by the notion of self-reducibility : for self-reducible relations, the extension counting function can be reduced back to the original counting problem for R R .

###### Definition C.15 ( Schnorr, 1976 ) .

A relation R ⊆ Σ ∗ × Σ ∗ R\subseteq\Sigma^{*}\times\Sigma^{*} is self-reducible if: 1. There exists a polynomial-time computable function g ∈ Σ ∗ → ℕ g\in\Sigma^{*}\to\mathbb{N} s.t., ( x , y ) ∈ R ⇒ | y | = g ⁡ ( x ) ; (x,y)\in R\Rightarrow|y|=g(x);

2. There exists a polynomial-time Turing machine that decides membership in R R .

3. There exist polynomial-time computable functions ψ ∈ Σ ∗ × Σ ∗ → Σ ∗ \psi\in\Sigma^{*}\times\Sigma^{*}\to\Sigma^{*} and σ ∈ Σ ∗ → ℕ \sigma\in\Sigma^{*}\to\mathbb{N} s.t. σ ⁡ ( x ) \displaystyle\sigma(x) = O ⁡ ( log ⁡ | x | ) , \displaystyle=O(\log|x|), (88) g ⁡ ( x ) > 0 \displaystyle g(x)>0 ⇒ σ ⁡ ( x ) > 0 ∀ x ∈ Σ ∗ , \displaystyle\Rightarrow\sigma(x)>0\quad\forall x\in\Sigma^{*}, (89) | ψ ⁡ ( x , w ) | \displaystyle|\psi(x,w)| ≤ | x | ∀ x , w ∈ Σ ∗ , \displaystyle\leq|x|\quad\forall x,w\in\Sigma^{*}, (90) and such that, for all x ∈ Σ ∗ x\in\Sigma^{*} , y = y 1 ​ … ​ y n ∈ Σ ∗ y=y_{1}\dots y_{n}\in\Sigma^{*} , ⟨ x , y 1 , … , y n ⟩ ∈ R ⇔ ⟨ ψ ⁡ ( x , y 1 ​ … ​ y σ ⁡ ( x ) ) , y σ ⁡ ( x ) + 1 , … , y n ⟩ ∈ R . \langle x,y_{1},\dots,y_{n}\rangle\in R\iff\langle\psi(x,y_{1}\dots y_{\sigma(x)}),y_{\sigma(x)+1},\dots,y_{n}\rangle\in R. (91)

For example, SAT is self-reducible: by fixing a prefix of variables and applying the reduction map ψ \psi , the problem is simplified to a smaller instance whose solutions extend the chosen prefix. Consider the Boolean formula F = ( x 1 ∨ x 2 ) ∧ ( ¬ x 1 ∨ x 3 ) ∧ ( ¬ x 2 ∨ ¬ x 3 ) , F=(x_{1}\vee x_{2})\ \wedge\ (\neg x_{1}\vee x_{3})\ \wedge\ (\neg x_{2}\vee\neg x_{3}), and suppose we fix the first variable to x 1 = 1 x_{1}=1 . The residual instance is obtained by applying ψ ⁡ ( F , ( 1 ) ) \psi(F,(1)) , which substitutes x 1 = 1 x_{1}=1 and simplifies the formula by deleting satisfied clauses and removing falsified literals: ψ ⁡ ( F , ( 1 ) ) = ( x 3 ) ∧ ( ¬ x 2 ∨ ¬ x 3 ) . \psi(F,(1))\;=\;(x_{3})\ \wedge\ (\neg x_{2}\vee\neg x_{3}). The unit clause ( x 3 ) (x_{3}) forces x 3 = 1 x_{3}=1 , which in turn simplifies ( ¬ x 2 ∨ ¬ x 3 ) (\neg x_{2}\vee\neg x_{3}) to ¬ x 2 \neg x_{2} , yielding x 2 = 0 x_{2}=0 . Hence the unique residual assignment is ( x 2 , x 3 ) = ( 0 , 1 ) (x_{2},x_{3})=(0,1) , and together with the prefix x 1 = 1 x_{1}=1 , we obtain the satisfying assignment ( x 1 , x 2 , x 3 ) = ( 1 , 0 , 1 ) . (x_{1},x_{2},x_{3})=(1,0,1).

For self-reducible relations, the extension counting function is no harder to approximate than the original counting problem.

###### Proposition C.16 ( Jerrum et al., 1986 ) .

Let R R be self-reducible. If there exists an FPRAS for N R N_{R} , then there exists an FPRAS for Ext R \mathrm{Ext}_{R} .

###### Proof.

By the definition of self-reducibility, the extension function Ext R ​ ( x , w ) \mathrm{Ext}_{R}(x,w) , which counts the number of strings y y such that ( x , w ​ y ) ∈ R (x,wy)\in R , can be mapped to the counting problem of a modified instance. Specifically, for any prefix w w where | w | ≤ σ ⁡ ( x ) |w|\leq\sigma(x) , there exists a polynomial-time computable mapping ψ \psi such that: Ext R ​ ( x , w ) = | { y ∈ Σ σ ⁡ ( x ) − | w | : ( x , w ​ y ) ∈ R } | = N R ​ ( ψ ⁡ ( x , w ) ) . \mathrm{Ext}_{R}(x,w)=|\{y\in\Sigma^{\sigma(x)-|w|}:(x,wy)\in R\}|=N_{R}(\psi(x,w)). (92) Since R R is self-reducible, the instance x w = ψ ⁡ ( x , w ) x_{w}=\psi(x,w) can be constructed in polynomial time relative to | x | |x| . By the hypothesis, there exists an FPRAS for N R N_{R} , which provides a randomized ( 1 ± ϵ ) (1\pm\epsilon) -approximation of N R ​ ( x w ) N_{R}(x_{w}) in time polynomial in | x w | |x_{w}| and 1 / ϵ 1/\epsilon . Consequently, this algorithm serves as an FPRAS for Ext R ​ ( x , w ) \mathrm{Ext}_{R}(x,w) , as it runs in polynomial time and satisfies the required approximation guarantees. ∎

### C.4 Proof for Theorem 4.3

###### Lemma C.17 (Formal Statement of Lemma 4.3 ) .

Assume that 𝖥𝖯𝖳𝖠𝖲 ⊊ 𝖥𝖯𝖱𝖠𝖲 \mathsf{FPTAS}\subsetneq\mathsf{FPRAS} for self-reducible relations. There exists a self-reducible relation R R and an associated function Ext R : Σ ∗ × Σ ∗ → ℕ \mathrm{Ext}_{R}:\Sigma^{*}\times\Sigma^{*}\to\mathbb{N} defined by Ext R ​ ( x , y < i ) ≔ | { z ∈ Σ ∗ : ( x , y < i ​ z ) ∈ R } | \mathrm{Ext}_{R}(x,y_{<i})\coloneqq|\{\,z\in\Sigma^{*}:(x,y_{<i}z)\in R\,\}| such that language models with CoT using polynomially many reasoning steps, which output a distribution for a given input ( x , y < i ) ∈ Σ n × Σ ∗ (x,y_{<i})\in\Sigma^{n}\times\Sigma^{*} by using a linear head for the last hidden state before emitting the output token, admit an FPRAS for Ext R \mathrm{Ext}_{R} , whereas no latent thought with polynomially many iterations admits the same approximation guarantee using a linear head for the last hidden state before emitting the output token.

###### Proof.

By Lemma C.6 , CoT can simulate any probabilistic Turing machine running in polynomial time; thus, it can implement an FPRAS for N R N_{R} . By Proposition C.16 , the existence of an FPRAS for N R N_{R} further implies the existence of an FPRAS for the extension function Ext R \mathrm{Ext}_{R} . On the other hand, latent thought consisting of a polynomial number of iterations can always be simulated by a deterministic polynomial-time Turing machine, provided that all state transitions in the latent computation are deterministic. Consequently, if such a latent thought process were to admit an FPRAS for Ext R \mathrm{Ext}_{R} , it would effectively yield a deterministic polynomial-time approximation scheme. By Proposition C.16 , the existence of such a scheme for Ext R \mathrm{Ext}_{R} would imply the existence of an FPTAS for N R N_{R} . However, under the standard complexity-theoretic assumption that 𝖥𝖯𝖳𝖠𝖲 ⊊ 𝖥𝖯𝖱𝖠𝖲 \mathsf{FPTAS}\subsetneq\mathsf{FPRAS} for self-reducible relations, there exists a self-reducible relation R R whose counting function admits an FPRAS but no FPTAS. This yields a contradiction. ∎

### C.5 Proof for Theorem 4.4

###### Definition C.18 (FPAUS) .

Uniform generation asks to sample an element y y uniformly at random from R ⁡ ( x ) R(x) . A fully polynomial almost uniform sampler (FPAUS) for R R is a randomized algorithm that, given an input x ∈ Σ ∗ x\in\Sigma^{*} and an accuracy parameter ε > 0 \varepsilon>0 , runs in time polynomial in | x | |x| and log ⁡ ( 1 / ε ) \log(1/\varepsilon) , and outputs a distribution q ( ⋅ ∣ x ) q(\cdot\mid x) such that ∥ q ( ⋅ ∣ x ) − U ( R ( x ) ) ∥ TV ≤ ε , \bigl\|q(\cdot\mid x)-U(R(x))\bigr\|_{\mathrm{TV}}\;\leq\;\varepsilon, where U ⁡ ( R ⁡ ( x ) ) U(R(x)) denotes the uniform distribution over the set R ⁡ ( x ) R(x) , and ∥ ⋅ ∥ TV \|\cdot\|_{\mathrm{TV}} denotes total variation distance.

For self-reducible relations, the following holds.

###### Theorem C.19 ( Jerrum et al., 1986 ) .

Let R R be a self-reducible relation. There exists an FPRAS for approximating | R ⁡ ( x ) | |R(x)| if and only if there exists an FPAUS for sampling uniformly from R ⁡ ( x ) R(x) .

###### Proof of Theorem 4.4 .

The target uniform conditional distribution is defined as follows: p ⁡ ( y i ∣ x , y < i ) := EXT R ⁡ ( x , y < i ​ y i ) ∑ u ∈ Σ EXT R ⁡ ( x , y < i ​ u ) ( y i ∈ Σ ) . p(y_{i}\mid x,y_{<i})\;:=\;\frac{\operatorname{EXT}_{R}(x,y_{<i}y_{i})}{\sum_{u\in\Sigma}\operatorname{EXT}_{R}(x,y_{<i}u)}\qquad(y_{i}\in\Sigma). (93) Assume an FPRAS 𝒜 ⁡ ( x , ε , δ ) \mathcal{A}(x,\varepsilon,\delta) exists for the self-reducible relation | R ⁡ ( x ) | |R(x)| . By Proposition C.16 , the existence of an FPRAS for | R ⁡ ( x ) | |R(x)| implies the existence of an FPRAS for the extension function EXT R \operatorname{EXT}_{R} . We construct a CoT that samples y ∈ R ⁡ ( x ) y\in R(x) by sequentially approximating these conditional probabilities. For each step i ∈ { 1 , … , m ⁡ ( n ) } i\in\{1,\dots,m(n)\} , the CoT computes ( 1 ± ε ) (1\pm\varepsilon) -accurate estimates EXT ^ R ​ ( x , y < i ​ u ) \widehat{\operatorname{EXT}}_{R}(x,y_{<i}u) for all u ∈ Σ u\in\Sigma using 𝒜 \mathcal{A} , and induces the following distribution: π ⁡ ( y i ∣ x , y < i ) := EXT ^ R ​ ( x , y < i ​ y i ) ∑ u ∈ Σ EXT ^ R ​ ( x , y < i ​ u ) . \pi(y_{i}\mid x,y_{<i})\;:=\;\frac{\widehat{\operatorname{EXT}}_{R}(x,y_{<i}y_{i})}{\sum_{u\in\Sigma}\widehat{\operatorname{EXT}}_{R}(x,y_{<i}u)}. (94) Conditioned on the event that all estimates in Equation 94 are ( 1 ± ε ) (1\pm\varepsilon) -accurate, the multiplicative error is bounded by: 1 − ε 1 + ε ≤ π ⁡ ( y i ∣ x , y < i ) p ⁡ ( y i ∣ x , y < i ) ≤ 1 + ε 1 − ε . \frac{1-\varepsilon}{1+\varepsilon}\leq\frac{\pi(y_{i}\mid x,y_{<i})}{p(y_{i}\mid x,y_{<i})}\leq\frac{1+\varepsilon}{1-\varepsilon}. (95) To ensure the cumulative approximation error remains within ( 1 ± ε ′ ) (1\pm\varepsilon^{\prime}) , we set the local precision to ε ≤ ε ′ 2 + ε ′ \varepsilon\leq\frac{\varepsilon^{\prime}}{2+\varepsilon^{\prime}} , which yields 1 + ε 1 − ε ≤ 1 + ε ′ \frac{1+\varepsilon}{1-\varepsilon}\leq 1+\varepsilon^{\prime} and 1 − ε 1 + ε ≥ 1 − ε ′ \frac{1-\varepsilon}{1+\varepsilon}\geq 1-\varepsilon^{\prime} . To ensure the failure probability is at most δ ′ \delta^{\prime} , we apply a union bound over the m ⁡ ( n ) m(n) generation steps and the | Σ | |\Sigma| calls per step. By setting the local confidence to δ ≤ δ ′ m ​ ( n ) ​ ( | Σ | + 1 ) \delta\leq\frac{\delta^{\prime}}{m(n)(|\Sigma|+1)} , the joint success event holds with probability at least 1 − δ ′ 1-\delta^{\prime} . Under this event, the CoT correctly simulates an FPRAS for p ⁡ ( y i ∣ x , y < i ) p(y_{i}\mid x,y_{<i}) in total time poly ​ ( n , 1 / ε ′ , log ⁡ ( 1 / δ ′ ) ) \text{poly}(n,1/\varepsilon^{\prime},\log(1/\delta^{\prime})) . Finally, since CoT can represent an FPRAS by Lemma 4.3 , it satisfies the requirements for the construction.

On the other hand, we show that latent thought cannot compute such an approximation. Suppose, for contradiction, that the model could compute the conditional distribution π ⁡ ( y i ∣ x , y < i ) \pi(y_{i}\mid x,y_{<i}) to within a ( 1 ± ε ) (1\pm\varepsilon) relative error in a single step. We define the estimator for the total count Z ⁡ ( x ) = | R ⁡ ( x ) | Z(x)=|R(x)| as: Z ^ ​ ( x ) ≔ ( ∏ i = 1 m ⁡ ( n ) π ⁡ ( y i ∣ x , y < i ) ) − 1 . \widehat{Z}(x)\;\coloneq\;\Biggl(\prod_{i=1}^{m(n)}\pi(y_{i}\mid x,y_{<i})\Biggr)^{-1}. (96) Since the true distribution satisfies p ⁡ ( y ∣ x ) = 1 / | R ⁡ ( x ) | = ∏ i p ⁡ ( y i ∣ x , y < i ) p(y\mid x)=1/|R(x)|=\prod_{i}p(y_{i}\mid x,y_{<i}) , the relative error of Z ^ ​ ( x ) \widehat{Z}(x) is governed by the product of local errors: ( 1 + ε ) − m ⁡ ( n ) ​ | R ⁡ ( x ) | ≤ Z ⁡ ( x ) ≤ ( 1 − ε ) − m ⁡ ( n ) ​ | R ⁡ ( x ) | , (1+\varepsilon)^{-m(n)}|R(x)|\leq Z(x)\leq(1-\varepsilon)^{-m(n)}|R(x)|, (97) By setting ε ≤ ε ′ 2 ​ m ​ ( n ) \varepsilon\leq\frac{\varepsilon^{\prime}}{2m(n)} , we apply Proposition C.14 and the properties of multiplicative error: ( 1 + ε ) − m ⁡ ( n ) ≥ 1 − m ⁡ ( n ) ​ ε ≥ 1 − ε ′ / 2 > 1 − ε ′ , (1+\varepsilon)^{-m(n)}\geq 1-m(n)\varepsilon\geq 1-\varepsilon^{\prime}/2>1-\varepsilon^{\prime}, (98) and for sufficiently small ε \varepsilon , ( 1 − ε ) − m ⁡ ( n ) ≤ 1 + 2 ​ m ​ ( n ) ​ ε ≤ 1 + ε ′ . (1-\varepsilon)^{-m(n)}\leq 1+2m(n)\varepsilon\leq 1+\varepsilon^{\prime}. (99) Substituting these into Equation 96 , we obtain: ( 1 − ε ′ ) ​ | R ⁡ ( x ) | ≤ Z ^ ​ ( x ) ≤ ( 1 + ε ′ ) ​ | R ⁡ ( x ) | . (1-\varepsilon^{\prime})|R(x)|\leq\widehat{Z}(x)\leq(1+\varepsilon^{\prime})|R(x)|. (100) This implies that if the model could compute π \pi accurately, Z ^ ​ ( x ) \widehat{Z}(x) would constitute an FPTAS for | R ⁡ ( x ) | |R(x)| . However, under the standard complexity-theoretic assumption that 𝖥𝖯𝖳𝖠𝖲 ⊊ 𝖥𝖯𝖱𝖠𝖲 \mathsf{FPTAS}\subsetneq\mathsf{FPRAS} for self-reducible relations, this yields a contradiction. ∎

## Appendix D Experimental Details

### D.1 Fundamental Algorithmic Reasoning Tasks

#### D.1.1 Task Settings

##### Word Problem

We define a sequence prediction task based on finite groups such as the symmetric group S 5 S_{5} . Given a sequence of group elements of length k k , the model is required to output the cumulative products obtained by scanning the sequence from left to right. Formally, for an input sequence ( g 1 , g 2 , … , g k ) (g_{1},g_{2},\ldots,g_{k}) , the target sequence is ( g 1 , g 1 g 2 , g 1 g 2 g 3 , … , g 1 g 2 ⋯ g k ) . (g_{1},\;g_{1}g_{2},\;g_{1}g_{2}g_{3},\;\ldots,\;g_{1}g_{2}\cdots g_{k}). We follow the setting of ( Merrill and Sabharwal, 2025b ) .

##### Connectivity

To ensure that the reachability labels are approximately balanced, we generate undirected graphs according to the Erdős–Rényi model ( Erdos and Renyi, 1959 ) G ⁡ ( n , p ) G(n,p) , where n n is the number of vertices and each possible edge is included independently with probability p p . In the supercritical regime ( p ​ n = c > 1 pn=c>1 ), a single “giant” connected component emerges, occupying a fraction s ∈ ( 0 , 1 ) s\in(0,1) of the vertices, which satisfies s = 1 − e − c ​ s . s=1-e^{-cs}. Consequently, the probability that two uniformly random vertices are both in this component—and hence mutually reachable—is approximately s 2 s^{2} . To target a reachability probability of 1 / 2 1/2 , we set s ≈ 1 2 ≈ 0.707 , c ≈ − ln ⁡ ( 1 − s ) s ≈ 1.74 , s\approx\sqrt{\tfrac{1}{2}}\approx 0.707,c\approx\tfrac{-\ln(1-s)}{s}\approx 1.74, and thus p = c n ≈ 1.7 n . p=\tfrac{c}{n}\approx\tfrac{1.7}{n}. In practice, for each graph of size n n we fix p = 1.7 / n p=1.7/n , which empirically yields Pr ⁡ [ reachable ] ≈ 50 % \Pr[\text{reachable}]\approx 50\% for n ∈ [ 50,100 ] n\in[50,100] . We follow the encoding scheme of Sanford et al. (2024a) . The input to the model is serialized as a flat token sequence consisting of three parts: v 0 v 1 ⋯ v n − 1 e 1 e 2 ⋯ e m s , t v_{0}\,v_{1}\,\cdots\,v_{n-1}\;e_{1}\,e_{2}\,\cdots\,e_{m}\;s,t where each vertex is denoted by a token v i v_{i} , each edge is represented as a pair “ u,v ” with u < v u<v , and the final token “ s,t ” specifies the source–target pair for the reachability query.

##### Arithmetic Expression Evaluation

Following ( Feng et al., 2023 ) , we generate expressions over integers modulo r r using the four operations + , − , × , ÷ {+,-,\times,\div} , where multiplication and division are defined via precomputed modular tables. To guarantee that each expression evaluates to a specific target value, we grow expressions backwards : starting from a sampled number, we iteratively replace it with a binary sub-expression that preserves its value under modular arithmetic. Different from ( Feng et al., 2023 ) , we fix the modulus to r = 3 r=3 , as our focus lies in evaluating the reasoning over expressions rather than exploring the properties of each modular arithmetic system.

##### Edit Distance

The Edit Distance task requires computing the minimum number of edit operations needed to transform one string into another. The allowed operations are insertion, deletion, and replacement of a single character, and the objective is to predict the total edit distance given two input strings. To build the dataset, we follow ( Feng et al., 2023 ) . We first generate two strings over a randomly sampled alphabet. The first string has a fixed length, while the second string is produced in two possible ways: with probability 0.4 0.4 , it is drawn as a random string of nearly the same length (within ± 3 \pm 3 characters), and with probability 0.6 0.6 , it is derived from the first string by applying a given number of random edit operations. Each edit operation is chosen uniformly among deletion, replacement, and insertion. To avoid trivial cases, string pairs that are identical or whose lengths differ excessively are rejected and resampled. Finally, the shorter string is always placed first to maintain a consistent input format. An example instance in the format is shown below: s v d h s s e e … v e | s h d s s s s … e s e <sep> 20 Here, the two input strings are separated by the token “ | ”, “ <sep> ” marks the end of the inputs, and the final number “ 20 ” denotes the computed edit distance.

#### D.1.2 Training Configuration

##### Configuration of chain of thought

For CoT models, training is performed with supervision of step-by-step algorithms. (1) Word problem: for this task, the CoT algorithm proceeds by sequentially scanning the token sequence and producing at each prefix the evaluation result of the expression step by step. Thus, the overall length of the CoT sequence matches the input length. (2) Graph connectivity: Following Bavandpour et al. (2025) , the algorithm sequence is simply the trace of a breadth-first search (BFS) starting from the source s s . At each step, the model emits the incident edges of the currently expanded node in the order they are visited. The sequence terminates as soon as the target t t is discovered. To implement this algorithm, we maintain a list (“scratchpad”) initialized with a dummy marker and the source, ( N , s ) (\texttt{N},s) . We iterate through this list from left to right (i.e., queue order). Whenever the current node u u is expanded, we append to the end of the list all incident edges ( u , v ) (u,v) for neighbors v v , followed by a separator token ( u , N ) (u,\texttt{N}) . (3) Arithmetic expression evaluation: Following ( Feng et al., 2023 ) , the CoT takes the fully expanded expression and repeatedly evaluates one innermost subexpression, writing down the simplified expression at each step until only a single numeral remains. For example, 2 ∗ ( 0 + 1 ) / 2 → 2 ∗ 1 / 2 → 2 / 2 → 1 . 2*(0+1)/2\to 2*1/2\to 2/2\to 1. The overall CoT sequence has quadratic length. (4) Edit distance: Following ( Feng et al., 2023 ) , the CoT algorithm outputs the DP table entries in the same order they are computed, i.e., row by row from top-left to bottom-right (topological order). This yields a quadratic number of steps in the input length.

##### Optimization and model details.

We trained all models using the AdamW optimizer with a linear learning rate schedule. The initial learning rate was set to 1 × 10 − 4 1\times 10^{-4} with a weight decay of 0.01 0.01 , and a batch size of 256 256 . Training was continued until the training loss plateaued. For looped TFs, curriculum learning was applied to all tasks except edit distance: the input size was increased by 2 2 for the word problem task, and by 4 4 for the connectivity and arithmetic evaluation tasks. The model architecture was based on standard Transformers with an embedding dimension of 256 256 . We used 4 4 attention heads, and varied the number of Transformer layers depending on the task: two layers for word problems, a single layer for connectivity, and time-modulated ( Xu and Sato, 2025 ) model with a single layer for looped TF, to stabilize training, on both arithmetic evaluation and the edit distance task. For CoT, we use the same configuration of the Transformer block.

##### Uniform selection.

To estimate a lower bound on the number of reasoning steps required by CoT for each task, we first follow the procedure introduced in prior work ( Bavandpour et al., 2025 ) . Specifically, given a complete CoT trajectory consisting of T T intermediate reasoning steps, we construct shortened trajectories by uniformly selecting k k step indices from { 1 , … , T } \{1,\dots,T\} , i.e., by taking a uniformly spaced subsequence of the original trajectory. Only the selected intermediate steps are used, while the remaining steps are removed. We then evaluate task performance as a function of k k , as shown in Table 3 .

##### Stepwise internalization.

We adopt stepwise internalization proposed by ( Deng et al., 2024 ) , a curriculum-based training procedure that gradually removes CoT tokens and encourages the model to internalize intermediate reasoning within its hidden states. Starting from a model trained on full CoT trajectories, we progressively truncate intermediate reasoning tokens according to a predefined schedule and finetune the model at each stage. Specifically, when the CoT length is greater than 128 128 , we remove 16 16 tokens per stage until the remaining CoT length reaches 128 128 . We then continue removing 8 8 tokens per stage until the CoT length is reduced to 8 8 , training the model for 16 16 epochs at each stage. The results for each fundamental algorithmic reasoning task are shown in Fig. 10 .

### D.2 Approximate Counting and Approximate Sampling

#### D.2.1 Approximate Counting of DNF Formulas

To generate the dataset, we first construct a DNF formula F F by sampling m m clauses, each consisting of w w distinct literals over n n Boolean variables. Each literal is independently assigned to be either positive or negated. The formula is then serialized into a token sequence in which each clause is represented by its index together with variable–value pairs such as “ 2 = 2= + 1 +1 ” or “ 4 = 4= − 1 -1 ”. For looped TFs, we prepare 100,000 100{,}000 training samples and 1,000 1{,}000 test samples. For CoT models, we instead generate an online dataset with the following structure. To train the CoT models, we simulate a single trial of the randomized counting algorithm of Karp and Luby (1983) . The sequence concatenates the serialized formula, the sampled clause, the full assignment, and the verification outcome, separated by <sep> tokens and terminated by <eos> . CoT model is trained in an autoregressive manner, where prediction targets are defined by shifting the token sequence while masking out the formula description. We trained the models using the AdamW optimizer with a linear learning rate schedule. The initial learning rate was set to 1 × 10 − 4 1\times 10^{-4} , with a weight decay of 0.01 0.01 . We used a batch size of 256 256 (reduced to 32 32 for the 1000 1000 -loop setting) and trained for 10,000 10{,}000 iterations. For inference, we count the total number of iterations used for summing output tokens (steps) in CoT across trials, and the number of loop iterations in the looped TF.

#### D.2.2 Approximate Sampling of Graph Colorings

We consider the problem of approximately sampling a proper k k -coloring of a graph, also known as almost-uniform generation , a canonical randomized task closely related to # ​ 𝖯 \#\mathsf{P} -hard counting problems. Given an undirected graph G = ( V , E ) G=(V,E) with n = | V | n=|V| vertices and maximum degree Δ \Delta , a proper k k -coloring is an assignment of colors from { 1 , … , k } \{1,\dots,k\} to vertices such that no adjacent vertices share the same color. Let Ω k ​ ( G ) \Omega_{k}(G) denote the set of all proper k k -colorings of G G . We restrict attention to graphs of bounded degree and assume k ≥ 2 ​ Δ + 1 . k\geq 2\Delta+1. Under this condition, classical results in approximate counting show that the number of proper k k -colorings admits a FPAUS ( Jerrum, 1995 ) . The approximation relies on Markov Chain Monte Carlo (MCMC) sampling using Glauber dynamics for graph colorings. Starting from an arbitrary proper coloring, the Markov chain repeatedly selects a vertex uniformly at random and proposes to recolor it with a randomly chosen color, accepting the update only if the resulting coloring remains proper. When k ≥ 2 ​ Δ + 1 k\geq 2\Delta+1 , this Markov chain is known to be rapidly mixing, converging to the uniform distribution over Ω k ​ ( G ) \Omega_{k}(G) in polynomial time. For our experiments, we generate an undirected Erdős–Rényi random graph, where each edge is included independently with probability p = 1.7 n , p=\frac{1.7}{n}, using a fixed random seed for reproducibility. For simplicity and ease of analysis, we focus on small graphs with n = 3 n=3 and set the number of colors to k = 5 k=5 .

Each sample is generated by running T T steps of Glauber dynamics on the space Ω k ​ ( G ) \Omega_{k}(G) of proper k k -colorings. Starting from a greedy proper initialization, at each step we uniformly select a vertex and a color; the recoloring is accepted if and only if it preserves properness. The final state of the Markov chain is treated as an approximate sample from the uniform distribution over Ω k ​ ( G ) \Omega_{k}(G) . In addition to the final coloring, we optionally record the entire sequence of proposals and accept/reject outcomes for CoT and use it as supervision, which is not included for latent thought. To train sequence models, we serialize the graph structure, the initial coloring, and either the MCMC history or the final coloring into a single token sequence. We evaluate the distribution of solutions generated by the model rather than only solution accuracy. Given an input x x , we draw N N independent samples from the model using ancestral decoding. Generation continues until an end-of-sequence (EOS) token is produced, and from each generated sequence we extract the final n n tokens immediately preceding the first EOS token, which encode a candidate solution. The resulting samples define an empirical distribution P ^ \hat{P} over generated solutions via normalized occurrence counts. For each instance, the task provides an exact enumeration 𝒴 \mathcal{Y} of all valid solutions. We define the reference distribution P true P_{\mathrm{true}} as the uniform distribution over this solution set, assigning probability 1 / | 𝒴 | 1/|\mathcal{Y}| to each y ∈ 𝒴 y\in\mathcal{Y} and zero otherwise. We quantify the discrepancy between the empirical distribution P ^ \hat{P} and the uniform reference distribution using the total variation distance 1 2 ​ ∑ y ∈ 𝒴 ∪ 𝒴 ^ | P ^ ​ ( y ) − P true ​ ( y ) | . \frac{1}{2}\sum_{y\in\mathcal{Y}\cup\hat{\mathcal{Y}}}\left|\hat{P}(y)-P_{\mathrm{true}}(y)\right|. We trained the models using the AdamW optimizer with a linear learning rate schedule. The initial learning rate was set to 1 × 10 − 4 1\times 10^{-4} , with a weight decay of 0.01 0.01 . We used a batch size of 256 256 and trained for 5,000 5{,}000 iterations. For inference, we measure the average number of steps (loops) per generation. We generate N = 50,000 N=50{,}000 samples for CoT and N = 10,000 N=10{,}000 samples for looped TFs. The resulting histograms of CoT outputs over the target support are shown in Figure 11 .

## Instructions for reporting errors

We are continuing to improve HTML versions of papers, and your feedback helps enhance accessibility and mobile support. To report errors in the HTML that will help us improve conversion and rendering, choose any of the methods listed below:

Click the "Report Issue" ( ) button, located in the page header.

Tip: You can select the relevant text first, to include it in your report.

Our team has already identified the following issues . We appreciate your time reviewing and reporting rendering errors we may not have found yet. Your efforts will help us improve the HTML versions for all readers, because disability should not be a barrier to accessing research. Thank you for your continued support in championing open access for all.

Have a free development cycle? Help support accessibility at arXiv! Our collaborators at LaTeXML maintain a list of packages that need conversion , and welcome developer contributions .
