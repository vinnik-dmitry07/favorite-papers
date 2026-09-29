##### Report GitHub Issue

Content selection saved. Describe the issue below:

# The Topological Trouble With Transformers

###### Abstract

Transformers encode structure in sequences via an expanding contextual history. However, their purely feedforward architecture fundamentally limits dynamic state tracking. State tracking—the iterative updating of latent variables reflecting an evolving environment—involves inherently sequential dependencies that feedforward networks struggle to maintain. Consequently, feedforward models push evolving state representations deeper into their layer stack with each new input step, rendering information inaccessible in shallow layers and ultimately exhausting the model’s depth. While this depth limit can be bypassed by dynamic depth models and by explicit or latent thinking that externalizes state representations, these solutions are computationally and memory inefficient. In this article, we argue that temporally extended cognition requires refocusing from explicit thought traces to implicit activation dynamics via recurrent architectures. We introduce a taxonomy of recurrent and continuous-thought transformer architectures, categorizing them by their recurrence axis (depth versus step) and their ratio of input tokens to recurrence steps. Finally, we outline promising research directions, including enhanced state-space models and coarse-grained recurrence, to better integrate state tracking into modern foundation models.

## 1 Introduction

Progress in understanding human cognition has resulted from conceptualizing the brain as a dynamical system. In terms of its hardware, the physical brain is composed of billions of interacting neurons whose collective behavior is inherently dynamical. In terms of its function, the emergent mind can be usefully modeled as a dynamical process with a high-dimensional state, s s , that evolves over time, modulated by external stimuli, x x . These levels can be bridged by formalizing the state progression as s t = f ⁡ ( s t − 1 , x t ) s_{t}=f(s_{t-1},x_{t}) , assuming discrete time t t .

From this perspective, an ideal architecture for modeling temporally extended cognition would be a recurrent neural network (RNN), which explicitly performs such a state-update operation. In principle, gradient-based training procedures might discover the function f f from data such that the important input signals would be integrated into the state representation and held until later required. The appeal of RNNs was somewhat dampened in the 1990s by the inherent limitations of gradient-based training ( Mozer, 1992 ; Hochreiter, 1998 ; Hochreiter et al., 2001 ) .

Until the transformer ( Vaswani et al., 2017 ) came along, feedforward nets did not seem like a viable approach to replicating human thought and reasoning. The transformer, with an audaciously long context window, retains all information in its history, often postponing the selection of relevant data until required for inference ( Meng et al., 2022 ) . In contrast, RNNs filter information as it arrives into a bottlenecked state representation ( Hochreiter and Schmidhuber, 1997 ) . This article is about what can go wrong with the transformer’s strategy and approaches that can address its limitations.

## 2 State tracking

Tracking the evolving world state is an essential ingredient for language understanding and reasoning, regardless of how tracking is achieved. The transformer’s strategy often leverages its capacity to retrieve static, previously observed information from a context window. The attention mechanism of transformers is highly effective at retrieving past tokens ( Olsson et al., 2022 ) . However, this lookup mechanism is conceptually distinct from the explicit maintenance of a dynamic state—the iterative, inherently sequential updating of latent variables that reflect a changing environment. The term belief state is often used to refer to this compact, sufficient summary of the knowledge an AI agent has about its environment ( Chrisman, 1992 ; Kaelbling et al., 1998 ) . Belief state can be a set of facts or it can be a probability distribution over possible worlds.

To illustrate, consider the game of twenty questions. Each answer to a question narrows the hypothesis space, and each subsequent question should be designed to shrink the hypothesis space further. In a game where one is asked to guess a number, if one is told that the number is larger than 50, it would make no sense to follow up it with a guess of 25. And on the flip side, if one is asked to think of a number between 1 and 100 and respond ‘higher’ or ‘lower’ to guesses, maintaining the state---the hidden number---is critical to preventing inconsistent answers. Yet, here is a trace from Gemini 3 (Fast) revealing a failure mode of models: 1 1 1 This example was originally suggested by Gamal ElSayed circa 2020, still causing some modern foundation models to fail. Other models may have been trained to address this particular failure mode. Baldelli et al. (2026) formally address the failure of standard models to reliably maintain a consistent hidden state over sequential interactions.

Even though the model cannot generate a random number internally, it can play the game without actually having a number in mind simply by choosing responses consistent with its previous responses. However, consistency requires tracking the valid range. Gemini 3 Thinking does generate an explicit target, but then it fails to make use of the generated target even though it is also a part of the input token stream in this case:

Beyond games, state tracking is essential to understanding the ever-changing world, the structure of arguments, and social interactions. State tracking failures in foundation models lead to loss of coherence in multi-turn conversations ( Laban et al., 2025 ) , inefficiency in information gathering ( Sawyer et al., 2025 ) , and breakdowns in communication and cooperation in multi-agent settings ( Davidson et al., 2025 ; Khatua et al., 2026 ) .

Without proper state tracking, models flip-flop in their interpretations and fail to detect their inconsistencies, e.g., the meaning of a polysemous word ( Lepori et al., 2025 ) : 2 2 2 The example that follows was produced by Gemini 2.5 Flash in 2025. Although the model sometimes responded correctly, and newer and more powerful models are much less susceptible to this error, the example reveals a fundamental limitation of the core architecture.

In this example, the model jumps from one interpretation of bank to the other without a human-like acknowledgment of the reversal (e.g., “Oh wait, I misinterpreted. You must have been talking about a financial institution.”). We consider this flip-flop a failure to track the world situation, the model’s earlier responses, and the listener’s expectations.

While tracking Fred’s location in the above example should not be challenging, in the most general case, it is untenable for models—and people—to maintain and track probabilistic belief states over all environmental possibilities because the distributions explode in dimensionality. People adopt heuristics such as sampling ( Vul et al., 2014 , e.g.,) , collapsing distributions into prototypical cases ( Tversky and Kahneman, 1971 ) , or forming concrete mental models most consistent with premises ( Johnson-Laird, 1983 ) , like a MAP estimate. Nonetheless, even finite-memory, deterministic state tracking can be unreliable in a transformer decoder.

We will use a schematic to explain the challenge of state tracking. In Figure 1 a, we depict the transformer with input steps shown along the horizontal axis and blocks (or layers) of the transformer along the vertical axis. Activation propagates from bottom to top (shallow to deep layers). For three selected blocks, we use color to indicate the functional connectivity of a causal transformer: activation in a block is influenced by all blocks immediately below and below to the left. In Figure 1 b, we depict the flow of state information, indicated by the green rectangles. The integration of the state representation and a new input (purple arrows) leads to a new state representation, s t = f ⁡ ( s t − 1 , x t ) s_{t}=f(s_{t-1},x_{t}) . Because the architecture is feedforward, s t s_{t} must lie deeper in the stack than s t − 1 s_{t-1} , eventually topping out of the model. Figure 2 shows examples from several recent articles matching this upward activation flow. This flow can make the integration of information over the sequence unreliable ( Biran et al., 2024 ; Grant et al., 2025 ; Lepori et al., 2025 ; Sawyer et al., 2025 ; Venhoff et al., 2025 ; Baldelli et al., 2026 ) .

Not every state-tracking problem requires depth linear in the number of layers. Merrill and Sabharwal (2025) prove the necessity and sufficiency of log ⁡ n \log n layers to recognize regular language strings of up to length n n and graph-connectivity problems with n n vertices. However, this proof addresses only the constructability of solutions, not their learnability. Fagnou et al. (2024) prove log ⁡ n + 1 \log n+1 layers are required for an entity tracking task with n n state changes and obtain empirical results consistent with this theory.

In practice, many researchers have identified clever solutions obtained by training depth-limited models on specific finite sequence-length problems ( Li et al., 2025a ; Piotrowski et al., 2025 ; Prakash et al., 2026 ; Shai et al., 2024 ) . Essentially, when the state update function, f f is of a certain form, the sequence of state updates may be composed into a simpler one-step function, e.g., there exists a function g g computable by a transformer layer such that s t = f ⁡ ( … ​ f ​ ( f ⁡ ( s 0 , x 1 ) , x 2 ) , … , x t ) = g ⁡ ( s 0 , x 1 , … , x t ) . s_{t}=f(\dots f(f(s_{0},x_{1}),x_{2}),\dots,x_{t})=g(s_{0},x_{1},\dots,x_{t}). Training losses have been proposed that aim to steer models toward such solutions, to the extent they exist exactly or approximately ( Hu et al., 2025 ; Teoh et al., 2025b ; Huang et al., 2026 ) . However, when belief-state cascades push deeper and deeper into a network, computational limitations arise because the resulting representations are unavailable to shallower layers. To illustrate, Figure 3 depicts the processing of the bank dialog. Using a technique called Patchscopes ( Ghandeharioun et al., 2024 ) , Lepori et al. (2025) observed that the embedding of the polysemous word ‘bank’ was ambiguous (i.e., a mixture of money bank vs. river bank) at shallow layers of the network, but deep in the network, the model selected the river bank interpretation. The previous sentences provided context (e.g., ‘took the day off work’, ’fishing pole’) to support one interpretation over the other. In the Figure, we depict this contextualization as occurring at the sixth block of the transformer stack, which means that when subsequent tokens are processed, the disambiguation is not available in blocks 1-5. Lepori et al. (2025) show that this delayed disambiguation leads to downstream errors whenever the response generation outpaces the model’s internal semantic convergence, such as when the model forms its yes/no response to the question about an ATM at the bank.

If reasonable models make errors when the inference cascade is just two steps ( Lepori et al. studied Gemma2-9B), it should be no surprise that models produce more severe failures in comprehending extended multi-agent conversations.

One solution to the depth dilemma is chain-of-thought style “thinking” where the model recasts a deep representation as one or more output tokens, which are then available to the model on its input ( Wei et al., 2022 ) . For ordinary, step-by-step microcognition, this solution is a cop out. Inferences that people make automatically and unconsciously and then utilize consistently, such as the selection of a polysemous word’s meaning, should not require elaborated, extended cognition. Even those who disagree with this desideratum should agree that if cognition in a transformer can be shifted from explicit thought traces to implicit activation dynamics, the resulting model will be more powerful.

## 3 Recurrent architectures

As we previously mentioned, the state tracking ability of a feedforward model is limited by model depth ( Merrill and Sabharwal, 2023 ; Strobl et al., 2024 ; Merrill and Sabharwal, 2025 , e.g.,) and by the fact that effectively utilizing the state representation becomes more challenging as it shifts upwards to deeper layers ( Biran et al., 2024 ; Lepori et al., 2025 ; Sawyer et al., 2025 ; Venhoff et al., 2025 ) .

The alternative is a recurrent model, which is necessary to express arbitrary state dynamics, i.e., s t = f ⁡ ( s t − 1 , x t ) s_{t}=f(s_{t-1},x_{t}) . In this section, we explore how to combine recurrence with transformers. Given the subtle yet critical differences among varieties of recurrence, they are easily conflated and mistakenly treated as equivalent. This equivalence is problematic because recurrence is not in itself sufficient for state tracking; the most popular form of recurrence is unable to track state ( Merrill et al., 2025 ) .

Figure 4 , adapted from Rumelhart et al. (1986) , shows a simple recurrent net (left) and the net unrolled t t steps to form a weight-constrained feedforward net (right).

Unrolling the net requires making a copy of all neurons in the network for each step of recurrence. At each step, activation flows through each connection.

Now consider a transformer with some recurrent connections, as depicted in Figure 5 a. As before, each box denotes a transformer block and the horizontal and vertical axes correspond to input tokens and layers, respectively. The additional arrows are meant to illustrate one possible type of recurrence involving activation flow from a deep layer to a shallow layer at every input step. The nature of the activation flow is not important for our purposes; for example, the shallow layer may generate queries that allow it to cross attend to keys and values from the deep layer ( Fan et al., 2021 , e.g.,) .

Unlike the simple RNN in Figure 4 , which can be unrolled in only one way, unrolling the recurrent transformer in Figure 5 a results in ambiguity due to the fact that that the transformer architecture incorporates three distinct ordered dimensions: (1) the layers of the architecture, bottom to top (shallow to deep) in the Figure; (2) the input steps of the architecture, left to right in the Figure; and (3) autoregressive steps performed at execution. During model pretraining, an ordinary (feedforward) transformer has only a single autoregressive step because all input steps are run in parallel; and during inference, autoregressive steps are typically confounded with input steps, although multi-token prediction allows for multiple input/output steps per autoregressive step ( Gloeckle et al., 2024 ) . However, recurrence allows for further decoupling. In particular, many forms of recurrence require that even when a model is trained via teacher forcing, it must still be unrolled autoregressively ( Teoh et al., 2025a ) . This necessary sequentiality is what we mean by autoregressive unrolling , not the sequentiality that arises from token-by-token generation in a pure feedforward model.

Figure 5 b depicts a transformer unrolled in depth, sometimes referred to as a looped transformer . Depth recurrence—whether of individual layers or ranges of layers, and whether deterministic or adaptive—is a very popular and successful approach. Some methods are designed and trained to allow for inference time scaling ( Yang et al., 2024a ; Nowak et al., 2024 ; Raposo et al., 2024 ; Alabdulmohsin and Zhai, 2025 ; Bae et al., 2025 ; Chen et al., 2025a ; Geiping et al., 2025 ; Rodkin et al., 2025 ; Yu et al., 2025 ; Zhu et al., 2025 ; Zeng et al., 2026 ; Jeddi et al., 2026 , e.g.,) ; others incorporate recurrence via pretraining ( Sanyal, 2026 ) or fine tuning a pretrained model ( Koishekenov et al., 2025 ; McLeish et al., 2025 ) ; and surprisingly, several operate purely as an inference-time method to improve reasoning ( Li et al., 2025b ; Chen et al., 2026 ; Ng, 2026 ) .

While depth recurrence can increase the expressivity of a transformer ( Saunshi et al., 2025 ) , it does not enable indefinite state tracking; the propagation is still depth limited. To appreciate this fact, pick any layer l l in the lower or upper stack as the representation of s ⁡ ( 0 ) s(0) , the state at the first stack. Then note that any s ⁡ ( t + 1 ) s(t+1) , if it is to depend arbitrarily on s ⁡ ( t ) s(t) recursively, must be in a higher layer. The state representation still shifts upward due to the parallel propagation of activation across steps t t , regardless of how deep the transformer is made to be with recurrent depth (Figure 1 b).

Indefinite tracking of state with an arbitrary state update function requires sequential dependency that precludes parallelization across the sequence length during training . Two examples of autoregressive updates are presented in Figures 5 c,d. Figure 5 c depicts a blockwise-recurrent model ( Hutchins et al., 2022 ; Chevalier et al., 2023 ; Chen et al., 2025b ; Borazjanizadeh and McClelland, 2025 ) in which a subsequence of input steps is run in parallel (two in the Figure) followed by an autoregressive iteration; Figure 5 d shows a model in which one input step is presented per autoregressive step, and at step t t , all stacks up to t − 1 t-1 send a signal from the deep layer to the shallow layer, yielding a fully recurrent model. This model may have attractor dynamics since each layer continues to update, converging only when all previous steps have reached asymptote.

Having addressed recurrence with multiple input steps per autoregressive step (Figure 5 c) and a standard one-to-one mapping (Figure 5 d), we can also consider a setup where multiple autoregressive steps are executed for each input step (Figure 6 ). Latent-thought models have this form ( Hao et al., 2025 ; Jolicoeur-Martineau, 2025 , e.g.,) . Some of these models can track state, whereas others do not ( Galashov et al., 2025 , e.g.,) .

The examples of recurrence we have given all involve signal propagation from deeper layers to shallower layers, but within-layer propagation over inputs steps (Figure 7 ) also yields state dynamics ( Allen-Zhu, 2025 ; Gu and Dao, 2024 ; Fagnou et al., 2026 , e.g.,) .

Table 1 attempts to lay out a taxonomy of recurrent transformer architectures that includes the cases we have considered so far. We characterize architectures along two dimensions: recurrence axis and input tokens per recurrence step . The axis can be depth alone (Figures 5 b,c,d), in step alone (Figure 7 ), and in both depth and step (Figure 6 ). The ratio of input tokens to recurrence steps can be greater than one (Figure 5 b,c), equal to one (Figure 5 d, 7 ), or less than one (Figure 6 ). 3 3 3 We define a ‘recurrence step’ strictly as a sequential dependency that precludes parallelization across the sequence length during training. In cells of the taxonomy, we list some popular and representative transformer-based architectures. We omit architectures that are described as “recurrent” in the sense that processing is iterative, but that are neither recurrent in depth nor step, e.g., Transformer-XL ( Dai et al., 2019 ) . Being recurrent in depth and/or step is necessary for state tracking but is not sufficient. Essentially, full-fledged state tracking requires sequential dynamics during training; any model that can be entirely parallelized across the context has limitations in updating state.

While we have not shown all such architectures, we have not succeeded in identifying any examples of work that lies in the empty cells of the taxonomy. Some of these cells would be worth exploration. For example, architectures in the second row, third column, could include ones with within-layer attractor dynamics, where the model’s activation may iterate to convergence before advancing to the next token. Architectures in the first row, second and third columns, are interesting because they feed activation from a deep layer to a shallow layer (once for ratio = 1 \text{ratio}=1 , multiple times for ratio > 1 \text{ratio}>1 ) in a manner that—unlike the looped transformer—does allow for indefinite state propagation.

We have deliberately sidestepped the question of what a recurrent arrow signifies in terms of activation dynamics. Different models make different proposals. The arrow could indicate copying key-value cache ( Yang et al., 2024c ) , it could represent a source of keys and values for cross attention ( Fan et al., 2021 ) or self attention ( Oncescu et al., 2026 ) , or it might represent a direct connection through a linear layer, an MLP, or an adapter such as LoRA ( Hu et al., 2022 ) . The coupling of step-to-step recurrence with attention—which gives neurons direct visibility to the entire step history—prevents credit assignment bottlenecks that arise when training traditional recurrent neural networks ( Ke et al., 2018 ; Oncescu et al., 2026 ) .

## 4 Architectural limitations and workarounds

Liu et al. (2026) point to the weakness of modern massively parallel architectures on problems that are inherently sequential, problems where combinatorics make it impractical to parallelize, such as state tracking, multihop inference, and planning. Formal analyses point to bounds on serial capacity for transformers ( Merrill and Sabharwal, 2023 ) . State-space models (SSMs) are often touted as a means of state propagation, but SSMs with linear updates are no more expressive than an ordinary transformer ( Merrill et al., 2025 ) . In contrast, chain of thought does enhance model expressivity ( Li et al., 2024 ; Merrill and Sabharwal, 2024 ) , as one would intuit: Allowing a model to talk to itself, whether in natural language or latent space, sends signals from deep in the transformer to shallow layers, thereby propagating state forward. It is no wonder that frontier models have become increasingly reliant on internal ‘thinking’. However, the reliance on intermediate outputs to track micro-state may perform wasteful computation steps and unnecessarily consume the context window. Implicit activation dynamics—albeit recurrent—might be adequate to efficiently update mundane state information of the sort that people can process unconsciously and automatically. In human terms, it is fine to talk to yourself if you are reasoning through a calculus problem, but it is a bit weird to have to continually remind yourself of the relationship between two characters in a book you are reading.

Given their limitations in state tracking, why are transformers as successful as they are? The short answer is that by being able to reexamine their entire input history, they can often turn a state-tracking problem into a working memory problem, i.e., into retrieval from the context window. For example, consider the latch problem from the 1990s that required a sequence-processing model latch on to a bit of information early in a sequence and to retain it over a long time gap ( Mozer, 1991 ; Bengio et al., 1994 ) . This problem in large part motivated LSTM but is entirely trivial for a transformer that can re-index into its input history to retrieve the early information. Transformers learn many clever strategies including this sort of lookback ( Prakash et al., 2026 ) , associatve scans ( Li et al., 2025a ) , more specialized algorithms for formal language understanding ( Allen-Zhu and Li, 2025 ; Piotrowski et al., 2025 ) , including belief updating that reflects state uncertainty ( Shai et al., 2024 ) . A simple illustration is the computation of parity from an input sequence of 0 0 ’s and 1 1 ’s. Instead of maintaining a parity state, the model can compute pairwise parity in the first layer of a transformer, then combine the pairs into four-bit parity in the second layer, and so forth, achieving a computation from scratch in log 2 ⁡ n \log_{2}n feedforward layers for a sequence of maximum length n n . Such alternate and even shortcut solutions are common for transformers to develop in practice ( Liu et al., 2022 ) .

Another factor in the success of transformers is their support of state compositionality . State need not be—as we have depicted it in Figure 1 —a monolithic representation. The representation of state can be split across embeddings and updated asynchronously for each component. For example, if the model needs to track the changing locations of two entities, those state variables can be updated independently for each entity.

## 5 Promising directions

In addition to the native mechanisms that transformers have to estimate state, several emerging research directions seem particularly promising for promoting state maintenance and updating. These directions balance the need for expressivity with computational feasibility.

### 5.1 Enhanced State-Space Models

While most linear SSMs do not exceed the expressivity of standard transformers, Delta Net ( Schlag et al., 2021 ) , when its eigenvalue range is extended to include negative values ( Grazzi et al., 2025 ) , maintains the highly desirable property of being trainable in parallel while simultaneously achieving greater expressivity than a standard transformer. The delta rule underlying Delta Net has inspired a range of further developments, including RWKV-7 ( Peng et al., 2025 ) and PaTH attention ( Yang et al., 2025b ) , that also achieve state tracking beyond the capability of ordinary transformers while demonstrating competitive language modeling at scale. Similarly, other new forms of attention are being developed with sequential dependencies that promise to be more powerful in stateful tasks ( Beltagy et al., 2020 ; Fagnou et al., 2024 ; Lin et al., 2025 ; Leviathan et al., 2025 ; Fagnou et al., 2026 ) , including the notion of gated linear attention ( Yang et al., 2024b ) and gated Delta Net ( Yang et al., 2025a ) that, when mixed with standard transformer blocks is more powerful than either, both in theory and practice ( Merrill et al., 2026 ) .

### 5.2 Approximating state tracking in feedforward transformers

Rather than incorporating recurrence, feedforward transformers can be steered to better approximate state tracking through specialized training objectives and structural priors ( Hu et al., 2025 ; Teoh et al., 2025b ; Huang et al., 2026 ) . The promise is that such biases will encourage models to bolster their native lookback abilities. However, we hope that future research will take into account structured, compositional state representations.

### 5.3 Coarse recurrence

Introducing recurrence at a coarser granularity than individual tokens can mitigate the computational burden of token-by-token state updates. In the past, block-recurrent models have operated on this principle by compressing and passing memory forward in fixed- length chunks. A promising approach is to consider linguistic structure in identifying the chunks: Borazjanizadeh and McClelland (2025) have modeled language as a sequence of discrete ‘thoughts’ by chunking at the sentence level.

### 5.4 Leveraging representational alignment

Variable-depth models dynamically select the number of iterations of a layer or the number of times a range of layers repeats. The fact that this approach succeeds with only fine tuning—and sometimes with no training whatsoever—suggests that the model is well predisposed to communication of representations across layers, due to the alignment resulting from the residual connections. Similarly, canon layers ( Allen-Zhu and Li, 2025 ) leverage alignment of representations from one input step to the next. We speculate that there are additional means of leveraging this alignment.

### 5.5 Efficient training of recurrence

Any architecture which is capable of indefinite, arbitrary state propagation requires autoregressive processing. Autoregressive pretraining is computationally inefficient and limits parallelization ( Chevalier et al., 2023 ) . One potential solution is a multi-stage training scheme in which initial pretraining relies entirely on standard, parallelizable feedforward transformer architectures. Recurrent mechanisms are then introduced only at a later training stage. To ensure training efficiency during these subsequent recurrent stages, optimization techniques such as truncated gradient methods and—for training attractor dynamics—recurrent backpropagation ( Almeida, 1987 ; Pineda, 1987 ; Liao et al., 2018 ) . Methods have also been proposed to increase arithmetic intensity to obtain scaling that is near linear time in context length versus quadratic for a naive implementation ( Oncescu et al., 2026 ) .

## 6 Conclusions

Although the transformer’s feedforward design has expanded the limits of context-based retrieval, its topological structure remains fundamentally at odds with the iterative nature of state tracking. As we have argued, the current reliance on explicit natural-language-like “thought” to bypass depth limitations is an inefficient workaround for a structural deficiency. By transitioning toward implicit, recurrent activation dynamics, we can move beyond these depth-limited constraints to attain robust long-term coherence and multihop inference.

The taxonomy and research directions proposed in this article provide a roadmap for improving sequential inference dependencies without sacrificing the foundational strengths of modern models. Ultimately, bridging the gap between the transformer’s parallel efficiency and the brain’s inherent dynamical nature is essential. The next generation of foundation models must do more than simply re-scan the past; they must maintain a fluid, evolving representation of reality that persists across the many time scales required for temporally extended cognition.

## Acknowledgments and Disclosure of Funding

Many thanks to Sunny Sanyal, Kazuki Irie, Kevin Murphy, Jay McClelland, and Chris Williams for helpful feedback on earlier drafts of the manuscript.

## References

Alabdulmohsin and Zhai (2025) I. Alabdulmohsin and X. Zhai Recursive inference scaling: a winning path to scalable inference in language and multimodal systems . In The Thirty-ninth Annual Conference on Neural Information Processing Systems , External Links: Link Cited by: Table 1 , §3 .

Allen-Zhu and Li (2025) Z. Allen-Zhu and Y. Li Physics of language models: part 1, learning hierarchical language structures . Note: arXiv:2305.13673 [cs.CL] External Links: 2305.13673 , Link Cited by: §4 , §5.4 .

Allen-Zhu (2025) Z. Allen-Zhu Physics of language models: part 4.1, architecture design and the magic of canon layers . Note: arXiv:2512.17351 [cs.CL] External Links: 2512.17351 , Link Cited by: Figure 7 , Figure 7 , Table 1 , §3 .

Almeida (1987) L. B. Almeida A learning rule for asynchronous perceptrons with feedback in a combinatorial environment . In Proceedings of the IEEE First International Conference on Neural Networks , Vol. 2 , San Diego, CA, USA , pp. 609–618 . Cited by: §5.5 .

Bae et al. (2025) S. Bae, Y. Kim, R. Bayat, S. Kim, J. Ha, T. Schuster, A. Fisch, H. Harutyunyan, Z. Ji, A. Courville, and S. Yun Mixture-of-recursions: learning dynamic recursive depths for adaptive token-level computation . In The Thirty-ninth Annual Conference on Neural Information Processing Systems , External Links: Link Cited by: §3 .

Baldelli et al. (2026) D. Baldelli, A. Parviz, A. Zouaq, and S. Chandar LLMs can’t play hangman: on the necessity of a private working memory for language agents . Note: arXiv:2601.06973 [cs.CL] External Links: 2601.06973 , Link Cited by: §2 , footnote 1 .

Beltagy et al. (2020) I. Beltagy, M. E. Peters, and A. Cohan Longformer: the long-document transformer . arXiv preprint arXiv:2004.05150 . Cited by: §5.1 .

Bengio et al. (1994) Y. Bengio, P. Simard, and P. Frasconi Learning long-term dependencies with gradient descent is difficult . IEEE Transactions on Neural Networks 5 ( 2 ), pp. 157–166 . External Links: Document Cited by: §4 .

Biran et al. (2024) E. Biran, D. Gottesman, S. Yang, M. Geva, and A. Globerson Hopping too late: exploring the limitations of large language models on multi-hop queries . In Proceedings of the 2024 Conference on Empirical Methods in Natural Language Processing , Y. Al-Onaizan, M. Bansal, and Y. Chen (Eds.) , Miami, Florida, USA , pp. 14113–14130 . External Links: Link , Document Cited by: §2 , §3 .

Borazjanizadeh and McClelland (2025) N. Borazjanizadeh and J. McClelland Modeling language as a sequence of thoughts . Note: arXiv:2512.25026 [cs.CL] External Links: 2512.25026 , Link Cited by: Table 1 , §3 , §5.3 .

Bulatov et al. (2022) A. Bulatov, Y. Kuratov, and M. Burtsev Recurrent memory transformer . In Advances in Neural Information Processing Systems , S. Koyejo, S. Mohamed, A. Agarwal, D. Belgrave, K. Cho, and A. Oh (Eds.) , Vol. 35 , pp. 11079–11091 . External Links: Link Cited by: Table 1 .

Cai et al. (2026) Z. Cai, X. Zhu, Y. Dong, Y. He, and S. Arora T 2 {}^{2} mlr: transformer with temporal middle-layer recurrence . Note: arXiv:2607.15178 [cs.CL] External Links: 2607.15178 , Link Cited by: Table 1 .

Chen et al. (2026) L. Chen, J. Li, C. Liang, N. Lao, and Q. Liu Training-free looped transformers . Note: arXiv:2605.23872 [cs.CL] External Links: 2605.23872 , Link Cited by: §3 .

Chen et al. (2025a) Y. Chen, J. Shang, Z. Zhang, Y. Xie, J. Sheng, T. Liu, S. Wang, Y. Sun, H. Wu, and H. Wang Inner thinking transformer: leveraging dynamic depth scaling to foster adaptive internal thinking . Note: arXiv:2502.13842 [cs.CL] External Links: 2502.13842 Cited by: §3 .

Chen et al. (2025b) Y. Chen, D. Hutchins, A. Jansen, A. Zhmoginov, D. Racz, and J. S. Andersen MELODI: exploring memory compression for long contexts . In The Thirteenth International Conference on Learning Representations , External Links: Link Cited by: §3 .

Chevalier et al. (2023) A. Chevalier, A. Wettig, A. Ajith, and D. Chen Adapting language models to compress contexts . Note: arXiv:2305.14788 [cs.CL] External Links: 2305.14788 , Link Cited by: §3 , §5.5 .

Chrisman (1992) L. Chrisman Reinforcement learning with perceptual aliasing: the perceptual distinctions approach . In Proceedings of the Tenth National Conference on Artificial Intelligence , AAAI’92 , pp. 183–188 . External Links: ISBN 0262510634 Cited by: §2 .

Dai et al. (2019) Z. Dai, Z. Yang, Y. Yang, J. Carbonell, Q. V. Le, and R. Salakhutdinov Transformer-xl: attentive language models beyond a fixed-length context . Note: arXiv:1901.02860 [cs.LG] External Links: 1901.02860 , Link Cited by: §3 .

Davidson et al. (2025) T. R. Davidson, A. Fourney, S. Amershi, R. West, E. Horvitz, and E. Kamar The collaboration gap . Note: arXiv:2511.02687 [cs.AI] External Links: 2511.02687 , Link Cited by: §2 .

Dehghani et al. (2019) M. Dehghani, S. Gouws, O. Vinyals, J. Uszkoreit, and L. Kaiser Universal transformers . In International Conference on Learning Representations , External Links: Link Cited by: Table 1 .

Fagnou et al. (2024) E. Fagnou, P. Caillon, B. Delattre, and A. Allauzen Chain and causal attention for efficient entity tracking . In Proceedings of the 2024 Conference on Empirical Methods in Natural Language Processing , Y. Al-Onaizan, M. Bansal, and Y. Chen (Eds.) , Miami, Florida, USA , pp. 13174–13188 . External Links: Link , Document Cited by: §2 , §5.1 .

Fagnou et al. (2026) E. Fagnou, P. Caillon, B. Delattre, and A. Allauzen Trading complexity for expressivity through structured generalized linear token mixing . ICML’26 , JMLR.org . Cited by: §3 , §5.1 .

Fan et al. (2021) A. Fan, T. Lavril, E. Grave, A. Joulin, and S. Sukhbaatar Addressing some limitations of transformers with feedback memory . Note: arXiv:2002.09402 [cs.CL] External Links: 2002.09402 , Link Cited by: Table 1 , §3 , §3 .

Galashov et al. (2025) A. Galashov, M. Jones, R. Ke, Y. Cao, V. Nagarajan, and M. C. Mozer Catch your breath: adaptive computation for self-paced sequence production . Note: arXiv:2510.13879 [cs.CL] External Links: 2510.13879 , Link Cited by: Table 1 , §3 .

Geiping et al. (2025) J. Geiping, S. M. McLeish, N. Jain, J. Kirchenbauer, S. Singh, B. R. Bartoldson, B. Kailkhura, A. Bhatele, and T. Goldstein Scaling up test-time compute with latent reasoning: a recurrent depth approach . In The Thirty-ninth Annual Conference on Neural Information Processing Systems , External Links: Link Cited by: §3 .

Ghandeharioun et al. (2024) A. Ghandeharioun, A. Caciularu, A. Pearce, L. Dixon, and M. Geva Patchscopes: a unifying framework for inspecting hidden representations of language models . In Proceedings of the 41st International Conference on Machine Learning , ICML’24 . Cited by: §2 .

Giannou et al. (2023) A. Giannou, S. Rajput, J. Sohn, K. Lee, J. D. Lee, and D. Papailiopoulos Looped transformers as programmable computers . In International Conference on Machine Learning , pp. 11398–11442 . Cited by: Table 1 .

Gloeckle et al. (2024) F. Gloeckle, B. Y. Idrissi, B. Rozière, D. Lopez-Paz, and G. Synnaeve Better and faster large language models via multi-token prediction . arXiv preprint arXiv:2404.19737 . Cited by: §3 .

Grant et al. (2025) S. Grant, N. D. Goodman, and J. L. McClelland Emergent symbol-like number variables in artificial neural networks . External Links: 2501.06141 , Link Cited by: §2 .

Grazzi et al. (2025) R. Grazzi, J. Siems, A. Zela, J. K. H. Franke, F. Hutter, and M. Pontil Unlocking state-tracking in linear rnns through negative eigenvalues . Note: arXiv:2411.12537 [cs.LG] External Links: 2411.12537 , Link Cited by: §5.1 .

Gu and Dao (2024) A. Gu and T. Dao Mamba: linear-time sequence modeling with selective state spaces . In First Conference on Language Modeling , External Links: Link Cited by: Figure 7 , Figure 7 , Table 1 , §3 .

Hao et al. (2025) S. Hao, S. Sukhbaatar, D. Su, X. Li, Z. Hu, J. E. Weston, and Y. Tian Training large language models to reason in a continuous latent space . In Second Conference on Language Modeling , External Links: Link Cited by: Figure 6 , Figure 6 , Table 1 , §3 .

Hochreiter et al. (2001) S. Hochreiter, Y. Bengio, P. Frasconi, and J. Schmidhuber J. F. Kolen and S. C. Kremer (Eds.) Gradient flow in recurrent nets: the difficulty of learning long-term dependencies . A field guide to dynamical recurrent neural networks. IEEE Press In . Cited by: §1 .

Hochreiter and Schmidhuber (1997) S. Hochreiter and J. Schmidhuber Long short-term memory . Neural computation 9 ( 8 ), pp. 1735–1780 . Cited by: §1 .

Hochreiter (1998) S. Hochreiter The vanishing gradient problem during learning recurrent neural nets and problem solutions . International Journal of Uncertainty, Fuzziness and Knowledge-Based Systems 6 ( 02 ), pp. 107–116 . Cited by: §1 .

Hu et al. (2022) E. J. Hu, Y. Shen, P. Wallis, Z. Allen-Zhu, Y. Li, S. Wang, L. Wang, W. Chen, et al. Lora: low-rank adaptation of large language models. . Iclr 1 ( 2 ), pp. 3 . Cited by: §3 .

Hu et al. (2025) E. S. Hu, K. Ahn, Q. Liu, H. Xu, M. Tomar, A. Langford, D. Jayaraman, A. Lamb, and J. Langford The belief state transformer . In The Thirteenth International Conference on Learning Representations , External Links: Link Cited by: §2 , §5.2 .

Huang et al. (2026) H. Huang, Y. LeCun, and R. Balestriero Semantic tube prediction: beating LLM data efficiency with JEPA . Note: arXiv:2602.22617 [cs.LG] External Links: 2602.22617 , Link Cited by: §2 , §5.2 .

Hutchins et al. (2022) D. Hutchins, I. Schlag, Y. Wu, E. Dyer, and B. Neyshabur Block-recurrent transformers . In Advances in Neural Information Processing Systems , S. Koyejo, S. Mohamed, A. Agarwal, D. Belgrave, K. Cho, and A. Oh (Eds.) , Vol. 35 , pp. 33248–33261 . External Links: Link Cited by: Table 1 , §3 .

Jabri et al. (2023) A. Jabri, D. Fleet, and T. Chen Scalable adaptive computation for iterative generation . Note: arXiv:2212.11972 [cs.LG] External Links: 2212.11972 , Link Cited by: Table 1 .

Jeddi et al. (2026) A. Jeddi, M. Ciccone, and B. Taati LoopFormer: elastic-depth looped transformers for latent reasoning via shortcut modulation . In The Fourteenth International Conference on Learning Representations , External Links: Link Cited by: §3 .

Johnson-Laird (1983) P.N. Johnson-Laird Mental models: towards a cognitive science of language, inference, and consciousness . Cognitive science series , Harvard University Press . External Links: ISBN 9780674568822 , LCCN 83004333 , Link Cited by: §2 .

Jolicoeur-Martineau (2025) A. Jolicoeur-Martineau Less is more: recursive reasoning with tiny networks . Note: arXiv:2510.04871 [cs.LG] External Links: 2510.04871 , Link Cited by: Figure 6 , Figure 6 , Table 1 , §3 .

Kaelbling et al. (1998) L. P. Kaelbling, M. L. Littman, and A. R. Cassandra Planning and acting in partially observable stochastic domains . Artificial Intelligence 101 ( 1 ), pp. 99–134 . External Links: ISSN 0004-3702 , Document , Link Cited by: §2 .

Katharopoulos et al. (2020) A. Katharopoulos, A. Vyas, N. Pappas, and F. Fleuret Transformers are RNNs: fast autoregressive transformers with linear attention . In Proceedings of the 37th International Conference on Machine Learning , Proceedings of Machine Learning Research , Vol. 119 , pp. 5156–5165 . Cited by: Table 1 .

Ke et al. (2018) N. R. Ke, A. G. ALIAS PARTH GOYAL, O. Bilaniuk, J. Binas, M. C. Mozer, C. Pal, and Y. Bengio Sparse attentive backtracking: temporal credit assignment through reminding . In Advances in Neural Information Processing Systems , S. Bengio, H. Wallach, H. Larochelle, K. Grauman, N. Cesa-Bianchi, and R. Garnett (Eds.) , Vol. 31 , pp. . External Links: Link Cited by: §3 .

Khatua et al. (2026) A. Khatua, H. Zhu, P. Tran, A. Prabhudesai, F. Sadrieh, J. K. Lieberwirth, X. Yu, Y. Fu, M. J. Ryan, J. Pei, and D. Yang CooperBench: why coding agents cannot be your teammates yet . External Links: 2601.13295 , Link Cited by: §2 .

Koishekenov et al. (2025) Y. Koishekenov, A. Lipani, and N. Cancedda Encode, think, decode: scaling test-time reasoning with recursive latent thoughts . Note: arXiv:2510.07358 [cs.LG] External Links: 2510.07358 , Link Cited by: §3 .

Laban et al. (2025) P. Laban, H. Hayashi, Y. Zhou, and J. Neville LLMs get lost in multi-turn conversation . Note: arXiv:2505.06120 [cs.CL] External Links: 2505.06120 , Link Cited by: §2 .

Lepori et al. (2025) M. A. Lepori, M. C. Mozer, and A. Ghandeharioun Racing thoughts: explaining contextualization errors in large language models . In Proceedings of the 2025 Conference of the Nations of the Americas Chapter of the Association for Computational Linguistics: Human Language Technologies (Volume 1: Long Papers) , L. Chiruzzo, A. Ritter, and L. Wang (Eds.) , Albuquerque, New Mexico , pp. 3020–3036 . External Links: Link , Document , ISBN 979-8-89176-189-6 Cited by: Figure 3 , Figure 3 , §2 , §2 , §2 , §2 , §3 .

Leviathan et al. (2025) Y. Leviathan, M. Kalman, and Y. Matias Selective attention improves transformer . In The Thirteenth International Conference on Learning Representations , External Links: Link Cited by: §5.1 .

Li et al. (2025a) B. Z. Li, Z. C. Guo, and J. Andreas (How) do language models track state? . In Forty-second International Conference on Machine Learning , External Links: Link Cited by: Figure 2 , Figure 2 , §2 , §4 .

Li et al. (2024) Z. Li, H. Liu, D. Zhou, and T. Ma Chain of thought empowers transformers to solve inherently serial problems . In The Twelfth International Conference on Learning Representations , External Links: Link Cited by: §4 .

Li et al. (2025b) Z. Li, Y. Li, and T. Zhou Skip a layer or loop it? test-time depth adaptation of pretrained llms . Note: arXiv:2507.07996 [cs.LG] External Links: 2507.07996 , Link Cited by: §3 .

Liao et al. (2018) R. Liao, Y. Xiong, E. Fetaya, L. Zhang, K. Yoon, X. Pitkow, R. Urtasun, and R. Zemel Reviving and improving recurrent back-propagation . In Proceedings of the 35th International Conference on Machine Learning , J. Dy and A. Krause (Eds.) , Proceedings of Machine Learning Research , Vol. 80 , pp. 3082–3091 . External Links: Link Cited by: §5.5 .

Lin et al. (2025) Z. Lin, E. Nikishin, X. He, and A. Courville Forgetting transformer: softmax attention with a forget gate . In The Thirteenth International Conference on Learning Representations , External Links: Link Cited by: §5.1 .

Lindsey et al. (2025) J. Lindsey, W. Gurnee, E. Ameisen, B. Chen, A. Pearce, N. L. Turner, C. Citro, et al. On the biology of a large language model . Transformer Circuits Thread . External Links: Link Cited by: Figure 2 , Figure 2 .

Liu et al. (2022) B. Liu, J. T. Ash, S. Goel, A. Krishnamurthy, and C. Zhang Transformers learn shortcuts to automata . arXiv preprint arXiv:2210.10749 . Cited by: §4 .

Liu et al. (2026) Y. Liu, K. Preechakul, K. Kuwaranancharoen, and Y. Bai The serial scaling hypothesis . External Links: 2507.12549 , Link Cited by: §4 .

McLeish et al. (2025) S. McLeish, A. Li, J. Kirchenbauer, D. S. Kalra, B. R. Bartoldson, B. Kailkhura, A. Schwarzschild, J. Geiping, T. Goldstein, and M. Goldblum Teaching pretrained language models to think deeper with retrofitted recurrence . External Links: 2511.07384 , Link Cited by: §3 .

Meng et al. (2022) K. Meng, D. Bau, A. Andonian, and Y. Belinkov Locating and editing factual associations in gpt . Advances in neural information processing systems 35 , pp. 17359–17372 . Cited by: §1 .

Merrill et al. (2026) W. Merrill, Y. Li, T. Romero, A. Svete, C. Costello, P. Dasigi, D. Groeneveld, D. Heineman, B. Kuehl, N. Lambert, C. Li, K. Lo, S. Malik, D. Matusz, B. Minixhofer, J. Morrison, L. Soldaini, F. Timbers, P. Walsh, N. A. Smith, H. Hajishirzi, and A. Sabharwal Olmo hybrid: from theory to practice and back . Technical report Allen Institute for AI . Note: Technical Report External Links: Link Cited by: §5.1 .

Merrill et al. (2025) W. Merrill, J. Petty, and A. Sabharwal The illusion of state in state-space models . Note: arXiv:2404.08819 [cs.LG] External Links: 2404.08819 , Link Cited by: §3 , §4 .

Merrill and Sabharwal (2023) W. Merrill and A. Sabharwal The parallelism tradeoff: limitations of log-precision transformers . Transactions of the Association for Computational Linguistics 11 , pp. 531–545 . External Links: Link , Document Cited by: §3 , §4 .

Merrill and Sabharwal (2024) W. Merrill and A. Sabharwal The expressive power of transformers with chain of thought . In The Twelfth International Conference on Learning Representations , External Links: Link Cited by: §4 .

Merrill and Sabharwal (2025) W. Merrill and A. Sabharwal A little depth goes a long way: the expressive power of log-depth transformers . Note: arXiv:2503.03961 [cs.LG] External Links: 2503.03961 , Link Cited by: §2 , §3 .

Mozer et al. (2026) M. C. Mozer, S. A. Siddiqui, D. Sawyer, S. Sanyal, and R. Liu Recirculation . Note: arXiv:2608.17981 [cs.LG] External Links: 2608.17981 , Link Cited by: Table 1 .

Mozer (1992) M. C. Mozer The induction of multiscale temporal structure . In Advances in Neural Information Processing Systems 4 , J. E. Moody, S. J. Hanson, and R. P. Lippmann (Eds.) , San Mateo, CA , pp. 275–282 . Cited by: §1 .

Mozer (1991) M. C. Mozer Induction of multiscale temporal structure . Advances in neural information processing systems 4 . Cited by: §4 .

Ng (2026) D. N. Ng LLM neuroanatomy: how I topped the LLM leaderboard without changing a single weight . Note: https://dnhkng.github.io/posts/rys/ Cited by: §3 .

Nowak et al. (2024) A. I. Nowak, O. Mercea, A. Arnab, J. Pfeiffer, Y. Dauphin, and U. Evci Towards optimal adapter placement for efficient transfer learning . Note: arXiv:2410.15858 [cs.LG] External Links: 2410.15858 , Link Cited by: §3 .

Olsson et al. (2022) C. Olsson, N. Elhage, N. Nanda, N. Joseph, N. DasSarma, T. Henighan, B. Mann, A. Askell, Y. Bai, A. Chen, T. Conerly, D. Drain, D. Ganguli, Z. Hatfield-Dodds, D. Hernandez, S. Johnston, A. Jones, J. Kernion, L. Lovitt, K. Ndousse, D. Amodei, T. Brown, J. Clark, J. Kaplan, S. McCandlish, and C. Olah In-context learning and induction heads . Transformer Circuits Thread . Note: https://transformer-circuits.pub/2022/in-context-learning-and-induction-heads/index.html Cited by: §2 .

Oncescu et al. (2026) C. Oncescu, D. Morwani, S. Jelassi, A. Meterez, M. Kwun, and S. Kakade The recurrent transformer: greater effective depth and efficient decoding . Note: arXiv:2604.21215 [cs.LG] External Links: 2604.21215 , Link Cited by: §3 , §5.5 .

Peng et al. (2025) B. Peng, R. Zhang, D. Goldstein, E. Alcaide, X. Du, H. Hou, J. Lin, J. Liu, J. Lu, W. Merrill, G. Song, K. Tan, S. Utpala, N. Wilce, J. S. Wind, T. Wu, D. Wuttke, and C. Zhou-Zheng RWKV-7 ”goose” with expressive dynamic state evolution . In Second Conference on Language Modeling , External Links: Link Cited by: Table 1 , §5.1 .

Pineda (1987) F. Pineda Generalization of back-propagation to recurrent neural networks . Physical Review Letters 59 ( 19 ), pp. 2229–2232 . External Links: Document Cited by: §5.5 .

Piotrowski et al. (2025) M. Piotrowski, P. M. Riechers, D. Filan, and A. S. Shai Constrained belief updates explain geometric structures in transformer representations . Note: arXiv:2502.01954 [cs.LG] External Links: 2502.01954 , Link Cited by: §2 , §4 .

Prakash et al. (2026) N. Prakash, N. Shapira, A. S. Sharma, C. Riedl, Y. Belinkov, T. R. Shaham, D. Bau, and A. Geiger Language models use lookbacks to track beliefs . In The Fourteenth International Conference on Learning Representations , External Links: Link Cited by: §2 , §4 .

Raposo et al. (2024) D. Raposo, S. Ritter, B. Richards, T. Lillicrap, P. C. Humphreys, and A. Santoro Mixture-of-depths: dynamically allocating compute in transformer-based language models . Note: arXiv:2404.02258 [cs.LG] External Links: 2404.02258 , Link Cited by: §3 .

Rodkin et al. (2025) I. Rodkin, D. Orel, K. Smirnov, A. Bolatov, B. Elbouardi, B. Hassan, Y. Kuratov, A. Bulatov, P. Nakov, T. Baldwin, A. Shelmanov, and M. Burtsev Beyond memorization: extending reasoning depth with recurrence, memory and test-time compute scaling . Note: arXiv:2508.16745 [cs.LG] External Links: 2508.16745 , Link Cited by: §3 .

Rumelhart et al. (1986) D. E. Rumelhart, G. E. Hinton, and R. J. Williams Learning representations by back-propagating errors . nature 323 ( 6088 ), pp. 533–536 . Cited by: Figure 4 , Figure 4 , §3 .

Sanyal (2026) S. Sanyal Looped-gpt: looping during pre-training improves generalization . Blog . External Links: Link Cited by: §3 .

Saunshi et al. (2025) N. Saunshi, N. Dikkala, Z. Li, S. Kumar, and S. J. Reddi Reasoning with latent thoughts: on the power of looped transformers . In The Thirteenth International Conference on Learning Representations , External Links: Link Cited by: §3 .

Sawyer et al. (2025) D. P. Sawyer, N. R. Ke, H. Soyer, M. Engelcke, J. Reid, D. P. Reichert, D. A. Hudson, A. Lerchner, D. J. Rezende, T. P. Lillicrap, M. C. Mozer, and J. X. Wang Exploring exploration with foundation agents in interactive environments . In NeurIPS 2025 Workshop on Embodied World Models for Decision Making , External Links: Link Cited by: §2 , §2 , §3 .

Schlag et al. (2021) I. Schlag, K. Irie, and J. Schmidhuber Linear transformers are secretly fast weight programmers . arXiv preprint arXiv:2102.11174 . Cited by: Table 1 , §5.1 .

Shai et al. (2024) A. Shai, P. M. Riechers, L. Teixeira, A. G. Oldenziel, and S. Marzen Transformers represent belief state geometry in their residual stream . In The Thirty-eighth Annual Conference on Neural Information Processing Systems , External Links: Link Cited by: §2 , §4 .

Siems et al. (2025) J. Siems, T. Carstensen, A. Zela, F. Hutter, M. Pontil, and R. Grazzi DeltaProduct: improving state-tracking in linear RNNs via householder products . In The Thirty-ninth Annual Conference on Neural Information Processing Systems , External Links: Link Cited by: Table 1 .

Strobl et al. (2024) L. Strobl, W. Merrill, G. Weiss, D. Chiang, and D. Angluin What formal languages can transformers express? a survey . Transactions of the Association for Computational Linguistics 12 , pp. 543–561 . External Links: ISSN 2307-387X , Document , Link , https://direct.mit.edu/tacl/article-pdf/doi/10.1162/tacl_a_00663/2370911/tacl_a_00663.pdf Cited by: §3 .

Sun et al. (2025) Y. Sun, X. Li, K. Dalal, J. Xu, A. Vikram, G. Zhang, Y. Dubois, X. Chen, X. Wang, S. Koyejo, T. Hashimoto, and C. Guestrin Learning to (learn at test time): RNNs with expressive hidden states . In Forty-second International Conference on Machine Learning , External Links: Link Cited by: Table 1 .

Takashiro et al. (2026) S. Takashiro, M. Koyama, T. Miyato, Y. Iwasawa, Y. Matsuo, and K. Hayashi Exploration of fast-slow latent recurrence for train-short, test-long generalization . External Links: 2604.01577 , Link Cited by: Table 1 .

Teoh et al. (2025a) J. Teoh, M. Tomar, K. Ahn, E. S. Hu, P. Sharma, R. Islam, A. Lamb, and J. Langford Next-latent prediction transformers learn compact world models . arXiv preprint arXiv:2511.05963 . Cited by: §3 .

Teoh et al. (2025b) J. Teoh, M. Tomar, K. Ahn, E. S. Hu, P. Sharma, R. Islam, A. Lamb, and J. Langford Next-latent prediction transformers learn compact world models . External Links: 2511.05963 , Link Cited by: §2 , §5.2 .

Tversky and Kahneman (1971) A. Tversky and D. Kahneman Belief in the law of small numbers . Psychological Bulletin 76 ( 2 ), pp. 105–110 . External Links: Document Cited by: §2 .

Vaswani et al. (2017) A. Vaswani, N. Shazeer, N. Parmar, J. Uszkoreit, L. Jones, A. N. Gomez, Ł. Kaiser, and I. Polosukhin Attention is all you need . In Advances in Neural Information Processing Systems , I. Guyon, U. V. Luxburg, S. Bengio, H. Wallach, R. Fergus, S. Vishwanathan, and R. Garnett (Eds.) , Vol. 30 , pp. 5998–6008 . External Links: Link Cited by: §1 .

Venhoff et al. (2025) C. Venhoff, A. Khakzar, S. Joseph, P. Torr, and N. Nanda Too late to recall: explaining the two-hop problem in multimodal knowledge retrieval . In The Thirty-ninth Annual Conference on Neural Information Processing Systems , External Links: Link Cited by: §2 , §3 .

Vul et al. (2014) E. Vul, N. Goodman, T. L. Griffiths, and J. B. Tenenbaum One and done? Optimal decisions from very few samples . Cognitive Science 38 ( 4 ), pp. 599–637 . External Links: Document Cited by: §2 .

Wang et al. (2026) X. Wang, Z. Cai, Z. Zhan, H. Dong, Y. Fan, G. de Rosa, T. Pearce, and J. Langford Full-bandwidth transformer . Note: arXiv:2608.08888 [cs.AI] External Links: 2608.08888 , Link Cited by: Table 1 .

Wei et al. (2022) J. Wei, X. Wang, D. Schuurmans, M. Bosma, F. Xia, E. Chi, Q. V. Le, D. Zhou, et al. Chain-of-thought prompting elicits reasoning in large language models . Advances in neural information processing systems 35 , pp. 24824–24837 . Cited by: §2 .

Yang et al. (2024a) L. Yang, K. Lee, R. D. Nowak, and D. Papailiopoulos Looped transformers are better at learning learning algorithms . In The Twelfth International Conference on Learning Representations , External Links: Link Cited by: §3 .

Yang et al. (2025a) S. Yang, J. Kautz, and A. Hatamizadeh Gated delta networks: improving mamba2 with delta rule . In The Thirteenth International Conference on Learning Representations , External Links: Link Cited by: §5.1 .

Yang et al. (2025b) S. Yang, Y. Shen, K. Wen, S. Tan, M. Mishra, L. Ren, R. Panda, and Y. Kim PaTH attention: position encoding via accumulating householder transformations . In The Thirty-ninth Annual Conference on Neural Information Processing Systems , External Links: Link Cited by: Table 1 , §5.1 .

Yang et al. (2024b) S. Yang, B. Wang, Y. Shen, R. Panda, and Y. Kim Gated linear attention transformers with hardware-efficient training . In Proceedings of the 41st International Conference on Machine Learning , ICML’24 . Cited by: §5.1 .

Yang et al. (2024c) Y. Yang, Z. Cao, Q. Chen, L. Qin, D. Yang, H. Zhao, and Z. Chen Kvsharer: efficient inference via layer-wise dissimilar kv cache sharing . arXiv preprint arXiv:2410.18517 . Cited by: §3 .

Yu et al. (2025) Z. Yu, Y. Belinkov, and S. Ananiadou Back attention: understanding and enhancing multi-hop reasoning in large language models . In Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing , C. Christodoulopoulos, T. Chakraborty, C. Rose, and V. Peng (Eds.) , Suzhou, China , pp. 11257–11272 . External Links: Link , Document , ISBN 979-8-89176-332-6 Cited by: §3 .

Zeng et al. (2026) B. Zeng, S. Song, S. Huang, Y. Wang, H. Li, Z. He, X. Wang, Z. li, and Z. Lin PonderLM: pretraining language models to ponder in continuous space . In The Fourteenth International Conference on Learning Representations , External Links: Link Cited by: §3 .

Zhu et al. (2025) R. Zhu, Z. Wang, K. Hua, T. Zhang, Z. Li, H. Que, B. Wei, Z. Wen, F. Yin, H. Xing, L. Li, J. Shi, K. Ma, S. Li, T. Kergan, A. Smith, X. Qu, M. Hui, B. Wu, Q. Min, H. Huang, X. Zhou, W. Ye, J. Liu, J. Yang, Y. Shi, C. Lin, E. Zhao, T. Cai, G. Zhang, W. Huang, Y. Bengio, and J. Eshraghian Scaling latent reasoning via looped language models . Note: arXiv:2510.25741 [cs.LG] External Links: 2510.25741 , Link Cited by: §3 .

## Instructions for reporting errors

We are continuing to improve HTML versions of papers, and your feedback helps enhance accessibility and mobile support. To report errors in the HTML that will help us improve conversion and rendering, choose any of the methods listed below:

Click the "Report Issue" ( ) button, located in the page header.

Tip: You can select the relevant text first, to include it in your report.

Our team has already identified the following issues . We appreciate your time reviewing and reporting rendering errors we may not have found yet. Your efforts will help us improve the HTML versions for all readers, because disability should not be a barrier to accessing research. Thank you for your continued support in championing open access for all.

Have a free development cycle? Help support accessibility at arXiv! Our collaborators at LaTeXML maintain a list of packages that need conversion , and welcome developer contributions .
