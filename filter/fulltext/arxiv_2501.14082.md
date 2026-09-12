##### Report GitHub Issue

Content selection saved. Describe the issue below:

# Communicating Activations Between Language Model Agents

###### Abstract

Communication between multiple language model (LM) agents has been shown to scale up the reasoning ability of LMs. While natural language has been the dominant medium for inter-LM communication, it is not obvious this should be the standard: not only does natural language communication incur high inference costs that scale quickly with the number of both agents and messages, but also the decoding process abstracts away too much rich information that could be otherwise accessed from the internal activations. In this work, we propose a simple technique whereby LMs communicate via activations ; concretely, we pause an LM B B ’s computation at an intermediate layer, combine its current activation with another LM A A ’s intermediate activation via some function f f , then pass f f ’s output into the next layer of B B and continue the forward pass till decoding is complete. This approach scales up LMs on new tasks with zero additional parameters and data, and saves a substantial amount of compute over natural language communication. We test our method with various functional forms f f on two experimental setups—multi-player coordination games and reasoning benchmarks—and find that it achieves up to 27.0 % 27.0\% improvement over natural language communication across datasets with < < 1 / 4 1/4 the compute, illustrating the superiority and robustness of activations as an alternative “language” for communication between LMs.

###### Keywords:

## 1 Introduction

Language is for the purpose of communication. As large language models (LLMs) have been increasingly used to power autonomous, goal-driven agents capable of reasoning, tool usage, and adaptive decision-making ( Yao et al., 2023 ; Xi et al., 2023 ; Wang et al., 2024 ; Ahn et al., 2022 ; Schick et al., 2023 ; Shen et al., 2023 ; Park et al., 2023 ; Nakano et al., 2022 ) , communication between multiple cooperating agents has emerged as an intuitive approach to amplify the reasoning capabilities of LLMs ( Wu et al., 2023 ) . Explicit communication in natural language between multiple LLMs has been shown to encourage divergent thinking ( Liang et al., 2023 ) , improve factuality and reasoning ( Du et al., 2023 ) , enable integration of cross-domain knowledge ( Sukhbaatar et al., 2024 ) , and allow for modular composition of abilities in a complementary manner ( Wu et al., 2023 ; Prasad et al., 2023 ) .

A critical problem with natural language communication, however, is that it incurs extremely high inference costs that scale quickly with the number of agents as well as length and number of messages ( Du et al., 2023 ; Yang et al., 2023 ; Wu et al., 2023 ) . Restricting LLM communication to natural language also raises the question: as LLMs are increasingly capable of handling larger, more complex tasks (sometimes with “super-human” ability) ( Wei et al., 2022 ; Burns et al., 2023 ) , might they communicate more effectively in representations of higher dimension than natural language? While using natural language as a communicative medium is appealing due to its interpretability, we claim that it may not be optimal for inter-LLM communication. Natural language generation uses only one token to represent the model’s belief over the entire vocabulary, which risks losing information embedded within the model output logits ( Pham et al., 2024 ) ; furthermore, a model’s belief over the entire vocabulary is itself not always better (for communicative purposes) than the model’s (often richer) representation of the input in earlier layers. Indeed, Hernandez et al. (2024) find that by around the halfway point of an LM’s computation, it has developed “enriched entity representations” of the input, where entities in the prompt are populated with additional facts about that entity encoded in the model’s weights; but by the later layers these embeddings are transformed into a representation of the next word which leverages only parts of the previous, richer representations, when that full embedding would be quite useful for communication.

Motivated by these concerns, this work outlines a simple technique whereby LLM agents communicate via activations , thus enabling more efficient (i.e., higher-entropy) communication at a fraction of the number of forward passes required at inference time. Concretely, we (1) pause a Transformer LM B B ’s computation at intermediate layer j j in the residual stream; (2) combine its post-layer j j activation with another LM A A ’s post-layer k k activation via some function f f ; and then (3) pass f f ’s output into the next layer j + 1 j+1 of B B and continue its forward pass till decoding is complete. This approach scales up LLMs on new tasks by leveraging existing, frozen LLMs along with zero task-specific parameters and data, applying to diverse domains and settings. Furthermore, in requiring only a partial forward pass through A A and one forward pass through B B , this method saves a substantial amount of compute over traditional natural language communication, which we quantify in Section 3.2 .

We validate our method by testing this approach with various functional forms f f on two experimental setups: two multi-player coordination games, where B B is asked to complete a task requiring information provided in a prompt to A A ; and seven reasoning benchmarks spanning multiple domains: Biographies ( Du et al., 2023 ) , GSM8k ( Cobbe et al., 2021 ) , MMLU High School Psychology, MMLU Formal Logic, MMLU College Biology, MMLU Professional Law, and MMLU Public Relations ( Hendrycks et al., 2021 ) . Our activation communication protocol exhibits up to 27.0 % 27.0\% improvement over natural language communication across these datasets, using < < 1 / 4 1/4 the compute. Critically, unlike prior work which test inter-LLM communication only on large-scale ( > > 70 70 B) models ( Du et al., 2023 ; Liang et al., 2023 ) , we find that our approach generalizes across a wide array of LLM suites and sizes, enabling even smaller LLMs to unlock the benefits of communication.

In summary, our contributions are two-fold: • We propose a novel inter-model communication protocol for LLM agents that is purely activation-based.

• We perform comprehensive experiments to validate the improved performance of activation communication over traditional natural language communication. We also formally quantify our approach’s compute savings over natural language communication, illustrating the superiority and robustness of activations as an alternative “language” for communication between LMs.

## 2 Related Work

#### Multi-agent communication

The field of multi-agent communication has a long-standing history. Notably, prior works on emergent communication have showed that agents can autonomously evolve communication protocols when deployed in multi-agent environments that enable cooperative and competitive game-play ( Sukhbaatar et al., 2016 ; Foerster et al., 2016 ; Lazaridou et al., 2017 ) . However, recent experiments have demonstrated that learning meaningful languages from scratch, even with centralized training, remains difficult ( Lowe et al., 2020 ; Chaabouni et al., 2019 ; Jaques et al., 2019 ) .

With the emergence of large pre-trained language models, allowing communication between LLMs in natural language has hence become a promising approach to enable coordination among multiple LLM agents ( Li et al., 2023 ) . Recent works have demonstrated that such conversations enable integration of cross-domain knowledge ( Sukhbaatar et al., 2024 ) , modular composition of abilities in a complementary manner ( Wu et al., 2023 ) , and improved task performance via splitting into subtasks ( Prasad et al., 2023 ) . Most notable is multiagent debate introduced by Du et al. (2023) , where LLMs provide initial responses and then make refinements by iteratively considering inputs from peers. While such methods have been shown to improve performance on various tasks over vanilla and majority-vote ( Wang et al., 2023 ) style prompting, these experiments have only focused on large models ( 𝙶𝙿𝚃 \mathtt{GPT} - 3.5 / 𝟺 \mathtt{3.5/4} , 𝙻𝙻𝚊𝙼𝙰𝟸 \mathtt{LLaMA2} - 𝟽𝟶 ​ 𝙱 \mathtt{70B} and up), leaving the efficacy of debate on smaller, open-source models underexplored; our study addresses this gap by reimplementing Du et al. (2023) in experiments with smaller-scale ( 1 − 70 1-70 B) models. More crucially, debate and similar natural language communication methods are extremely computationally expensive , which this work addresses ( Yang et al., 2023 ; Wu et al., 2023 ) .

Notably, Pham et al. (2024) propose CIPHER, which uses input (tokenizer) embeddings (as opposed to activations) to enable multi-agent communication; specifically, CIPHER passes the average tokenizer embedding (weighted by the LLM’s next-token probabilities) between models. While ( Pham et al., 2024 ) show this approach outperforms natural language debate, it (i) still faces substantial information loss relative to the model activations and (ii) does not save compute, as the number of these “average embeddings” passed between models is the same as the number of tokens passed between models in natural language communication.

A related class of methods involves spending extra test-time compute reasoning in latent space ( Geiping et al., 2025 ; Hao et al., 2024 ) . Such latent reasoning approaches involving doing ”chain-of-thought in activation space,” e.g. by grafting LM activations into other layers/later forward passes through the same model (e.g., a form of “recurrent AC” within a single model); our approach can be viewed as doing exactly the same thing, but instead ”outsourcing” the CoT to another model (and thus reaping benefits from greater diversity of thoughts/reasoning paths from distinct models).

#### Activation engineering

Activation engineering involves editing an LLM’s intermediate layer representations during a forward pass to create desired changes to output text ( Li et al., 2024 ; Turner et al., 2023 ) . Past work has explored extracting latent steering vectors from a frozen LLM to control quality and content of completions ( Subramani et al., 2022 ) , as well as using “direction” vectors (computed as the difference in activations between two prompts) that enable inference-time control over high-level properties of generations ( Li et al., 2024 ; Turner et al., 2023 ) . This work involves activation editing that is similar to such prior works at a high level, though for the purpose of communication between LLM agents.

#### Model composition and grafting

Composing expert models has been a recurring strategy to improve large models, with different methods imposing different restrictions on the types of base LLMs that can be combined. Mixture of Experts ( Shazeer et al., 2017 ) requires that all experts are trained simultaneously using the same data; Branch-Train-Mix ( Sukhbaatar et al., 2024 ) trains a single base LM multiple times on different datasets, then learns a router on outputs. Crucially, these methods do not work when neither model can do the task at hand well (i.e., they solve the problem of choosing which of several outputs is best, not that of generating a high-quality output by recombining the disparate abilities of the various base LMs).

Model grafting, in contrast, seeks to merge different models immediately prior to or at inference-time. Past works have explored this at the parameter level (e.g., task vector averaging as in Ilharco et al. (2023) , which requires that the base models be well aligned), probability distribution / token level as in Shen et al. (2024) (which imposes few restrictions on the relationship between the base models, but by virtue of being token-based can result in cascading errors during decoding), and activation level (e.g., CALM ( Bansal et al., 2024 ) which learns an attention layer on top of two models’ intermediate layer activations and thus enables broader integration of model abilities than token-level methods, but requires re-tuning of the attention mechanism for every model pair). In this work, we seek to unify CALM and other activation-level grafting techniques under a single framework, parameterized by the function f f used to combine activations; crucially, we explore simple forms of f f (e.g., sum, mean) that—unlike Bansal et al. (2024) —require zero additional task-specific parameters and data , and are far more compute-efficient.

## 3 Communicating Activations Between Language Models

We propose a simple yet effective technique whereby language models communicate via activations . We detail our approach in Section 3.1 ; provide analytical models of the compute saved over natural language communication in Section 3.2 ; and discuss the intuition behind this approach in Section 3.3 .

### 3.1 Method

Consider two language models, A A and B B , and some setting in which B B must perform a task where it would benefit from knowledge given to A A as a prompt/encoded in A A ’s weights (example settings in Section 4.1 / Section 4.2 respectively). We propose incorporating information from A A ’s post-layer k k activation 𝒉 A , k \bm{h}_{A,k} into B B ’s post-layer j j activation 𝒉 B , j \bm{h}_{B,j} (and vice versa, though for simplicity we henceforth only discuss the first direction) ( Figure 1 , left).

More formally, suppose A A and B B (which have model dimensions d A d_{A} and d B d_{B} respectively) are given prompts x A x_{A} and x B x_{B} respectively, where x A x_{A} is of length t A t_{A} tokens and x B x_{B} is of length t B t_{B} tokens. We first run a partial forward pass of B B until layer j j (henceforth denoted B ≤ j ​ ( x B ) B_{\leq j}(x_{B}) ) to get 𝒉 B , j ∈ ℝ t B × d B \bm{h}_{B,j}\in\mathbb{R}^{t_{B}\times d_{B}} . Then we (1) run a partial forward pass of A A until layer k k to get A ≤ k ​ ( x 1 ) := 𝒉 A , k ∈ ℝ t A × d A A_{\leq k}(x_{1}):=\bm{h}_{A,k}\in\mathbb{R}^{t_{A}\times d_{A}} ; (2) replace the activation of the last token ( 𝒉 B , j ) t B ∈ ℝ d B (\bm{h}_{B,j})_{t_{B}}\in\mathbb{R}^{d_{B}} ⟵ f ⁡ ( ( 𝒉 A , k ) t A , ( 𝒉 B , j ) t B ) \longleftarrow f((\bm{h}_{A,k})_{t_{A}},(\bm{h}_{B,j})_{t_{B}}) for some function f : ℝ d A + d B → ℝ d B f:\mathbb{R}^{d_{A}+d_{B}}\to\mathbb{R}^{d_{B}} ; then (3) continue B B ’s forward pass till decoding is complete, resulting in an output y = B > k ​ ( 𝒉 B , j ) y=B_{>k}(\bm{h}_{B,j}) .

Let 𝒂 = ( 𝒉 A , k ) t A \bm{a}=(\bm{h}_{A,k})_{t_{A}} , 𝒃 = ( 𝒉 B , j ) t B \bm{b}=(\bm{h}_{B,j})_{t_{B}} . For sake of simplicity assume d A = d B d_{A}=d_{B} . 1 1 1 When d A ≠ d B d_{A}\neq d_{B} , the 𝚜𝚞𝚖 \mathtt{sum} , 𝚖𝚎𝚊𝚗 \mathtt{mean} , and 𝚛𝚎𝚙𝚕𝚊𝚌𝚎 \mathtt{replace} functions are defined as follows. Let d = min ⁡ ( d A , d B ) d=\min(d_{A},d_{B}) and ∘ \circ the concatenation operator. Then f ( 𝒂 , 𝒃 ) = 𝒃 1 : max ⁡ ( d B − d , 0 ) ∘ ( 𝒃 max ⁡ ( d B − d , 0 ) + 1 : d B + 𝒂 max ⁡ ( d A − d , 0 ) + 1 : d A ) f(\bm{a},\bm{b})=\bm{b}_{1:\max(d_{B}-d,0)}\circ\left(\bm{b}_{\max(d_{B}-d,0)+1:d_{B}}+\bm{a}_{\max(d_{A}-d,0)+1:d_{A}}\right) ( 𝚜𝚞𝚖 ) \mathtt{(sum)} , f ( 𝒂 , 𝒃 ) = 𝒃 1 : max ⁡ ( d B − d , 0 ) ∘ 1 2 ( 𝒃 max ⁡ ( d B − d , 0 ) + 1 : d B + 𝒂 max ⁡ ( d A − d , 0 ) + 1 : d A ) f(\bm{a},\bm{b})=\bm{b}_{1:\max(d_{B}-d,0)}\circ\frac{1}{2}\left(\bm{b}_{\max(d_{B}-d,0)+1:d_{B}}+\bm{a}_{\max(d_{A}-d,0)+1:d_{A}}\right) ( 𝚖𝚎𝚊𝚗 ) \mathtt{(mean)} , and f ( 𝒂 , 𝒃 ) = 𝒃 1 : max ⁡ ( d B − d , 0 ) ∘ 𝒂 max ⁡ ( d A − d , 0 ) + 1 : d A f(\bm{a},\bm{b})=\bm{b}_{1:\max(d_{B}-d,0)}\circ\bm{a}_{\max(d_{A}-d,0)+1:d_{A}} ( 𝚛𝚎𝚙𝚕𝚊𝚌𝚎 ) \mathtt{(replace)} . We consider three non-learned functions f f : f ⁡ ( 𝒂 , 𝒃 ) \displaystyle f(\bm{a},\bm{b}) = 𝒂 + 𝒃 ( 𝚜𝚞𝚖 ) \displaystyle=\bm{a}+\bm{b}\>\>\qquad\qquad\mathtt{(sum)} f ⁡ ( 𝒂 , 𝒃 ) \displaystyle f(\bm{a},\bm{b}) = 1 2 ( 𝒂 + 𝒃 ) ( 𝚖𝚎𝚊𝚗 ) \displaystyle=\frac{1}{2}(\bm{a}+\bm{b})\>\>\qquad\mathtt{(mean)} f ⁡ ( 𝒂 , 𝒃 ) \displaystyle\qquad f(\bm{a},\bm{b}) = 𝒂 ( 𝚛𝚎𝚙𝚕𝚊𝚌𝚎 ) \displaystyle=\bm{a}\>\>\qquad\qquad\mathtt{(replace)}

For cases where, due to differences in A A and B B ’s training, A A and B B ’s activation spaces are quite different, we propose learning a task-agnostic (depends only on the models A A and B B ) linear layer 𝑾 ∈ ℝ d B × ℝ d A \bm{W}\in\mathbb{R}^{d_{B}}\times\mathbb{R}^{d_{A}} that projects 𝒂 \bm{a} onto B B ’s activation space. Note that this introduces zero additional task-specific parameters and data, as we propose learning this “mapping matrix” 𝑾 \bm{W} only once for each model pair ( A , B ) (A,B) using general text, e.g. sequences from A A and/or B B ’s pretraining data mixes. We can then perform 𝚜𝚞𝚖 \mathtt{sum} , 𝚖𝚎𝚊𝚗 \mathtt{mean} , or 𝚛𝚎𝚙𝚕𝚊𝚌𝚎 \mathtt{replace} with 𝑾 ​ 𝒂 , 𝒃 \bm{W}\bm{a},\bm{b} instead of 𝒂 , 𝒃 \bm{a},\bm{b} . We propose training 𝑾 \bm{W} to minimize MSE loss over a dataset of N N sentences ℒ MSE ​ ( { 𝒚 ( i ) } i = 1 N , { 𝒛 ( i ) } i = 1 N ) = 1 N ​ ∑ i = 1 N ‖ 𝒛 ( i ) − 𝑾 ​ 𝒚 ( i ) ‖ 2 2 \mathcal{L}_{\rm MSE}\left(\{\bm{y}^{(i)}\}_{i=1}^{N},\{\bm{z}^{(i)}\}_{i=1}^{N}\right)=\frac{1}{N}\sum_{i=1}^{N}\left\|\bm{z}^{(i)}-\bm{W}\bm{y}^{(i)}\right\|_{2}^{2} where each ( 𝒚 ( i ) , 𝒛 ( i ) ) (\bm{y}^{(i)},\bm{z}^{(i)}) pair denotes the final-token layer- 26 26 activations of A A and B B at layers k k and j j respectively given the same sentence as input.

### 3.2 Compute Analysis

To understand the significance of activation communication, we must formally quantify the compute this procedure saves over natural language communication. For simplicity suppose the following (similar calculations can be made for the cases where A A and B B have differing model architectures and/or are given different prompts): • A A and B B both have L L layers (each with H H attention heads, key size K K , and feedforward size F F ), dimension D D , and vocab size V V

• A A and B B are both given a prompt of P P tokens

• A A can send B B a single M M -token message

• B B must produce an output of T T tokens, given its prompt and A A ’s message

Traditional methods require M M forward passes of A A given a P P -length input, plus T T forward passes of B B given a ( P + M ) (P+M) -length input. Following Hoffmann et al. (2022) , this requires M ⁡ ( 4 ​ P ​ V ​ D + L ⁡ ( 8 ​ P ​ D ​ K ​ H + 4 ​ P 2 ​ K ​ H + 3 ​ H ​ P 2 CLOSE CLOSE \displaystyle M\big(4PVD+L(8PDKH+4P^{2}KH+3HP^{2} (1) OPEN OPEN + 4 ​ P ​ D ​ F ) ) + T ⁡ ( 4 ​ ( P + M ) ​ V ​ D + L ⁡ ( 8 ​ ( P + M ) ​ D ​ K ​ H CLOSE CLOSE \displaystyle+4PDF)\big)+T\big(4(P+M)VD+L(8(P+M)DKH OPEN OPEN + 4 ​ ( P + M ) 2 ​ K ​ H + 3 ​ H ​ ( P + M ) 2 + 4 ​ ( P + M ) ​ D ​ F ) ) \displaystyle+4(P+M)^{2}KH+3H(P+M)^{2}+4(P+M)DF)\big) FLOPs. In contrast, at inference time, our method requires only 1 partial (up till the k k th layer) forward pass of A A given a P P -length input, T T forward passes of B B given a P P -length input, and the activation replacement procedure. This requires 2 ​ P ​ V ​ D + k ⁡ ( 8 ​ P ​ D ​ K ​ H + 4 ​ P 2 ​ K ​ H + 3 ​ H ​ P 2 CLOSE \displaystyle 2PVD+k(8PDKH+4P^{2}KH+3HP^{2} (2) OPEN + 4 ​ P ​ D ​ F ) + T ⁡ ( 4 ​ P ​ V ​ D + L ⁡ ( 8 ​ P ​ D ​ K ​ H + 4 ​ P 2 ​ K ​ H CLOSE CLOSE \displaystyle+4PDF)+T\big(4PVD+L(8PDKH+4P^{2}KH OPEN OPEN + 3 ​ H ​ P 2 + 4 ​ P ​ D ​ F ) ) + ℱ ⁡ ( D ) \displaystyle+3HP^{2}+4PDF)\big)+\mathcal{F}(D) FLOPs, where ℱ ⁡ ( D ) = O ⁡ ( D ) \mathcal{F}(D)=O(D) for non-learned f f and O ⁡ ( D 2 ) O(D^{2}) when f f is the mapping matrix.

In all practical cases, (2) is substantially lower than (1).

### 3.3 Why should this work?

Recall that Pham et al. (2024) propose CIPHER—communicating the average tokenizer embedding (weighted by the LLM’s next-token probabilities) between models. We build upon the intuition behind CIPHER, which goes as follows: the token sampling process during decoding risks substantial information loss from the model’s output logits, and communicating a model’s weighted-average tokenizer embedding essentially entails communicating both that model’s final answer and its belief in that answer (over the entire vocabulary).

Communicating activations, then, can be thought of as communicating a strict superset of {next-token prediction, belief over entire vocabulary}, as activations of late-enough layers essentially encode the model’s entire knowledge about the provided context as well as its predicted completion and confidence in that completion (see Figures 1 and 7 in Hewitt & Manning (2019) and Hernandez et al. (2024) , respectively, which show that linear probes tasked with predicting certain output characteristics from a Transformer’s intermediate layer embeddings of its input work poorly for early layers, extremely well after around the halfway point of computation, but then probe accuracy drops closer to the final layers). 2 2 2 Note one important critique of multiagent debate: that in cases where multiple agents are uncertain about the answer, there is no reason why referencing other agents’ answers would generate more factual reasoning. Both CIPHER and activation communication solve this problem, as some notion of model confidence is being communicated along with its next-token prediction. Indeed, these curves of probe accuracy by layer indicate that the final layers and LM head “ throw away ” information not useful for next-token prediction that very well could be useful for communicative purposes; this is precisely why our proposed activation communication technique is not an iterative approach (there is no notion of “rounds” like in debate and CIPHER, which require an additional token budget to extract more and more information out of the LM), as one activation grafting step from A A to B B inherently communicates to B B all of A A ’s knowledge/beliefs about the prompt it was given. Moreover, the extra information over the model’s next-token prediction and confidence that is encoded in its activations is what makes activation communication more performant than its natural language counterpart, as we will see in Section 4 .

## 4 Experiments

We test our method on two distinct experimental setups: multi-player coordination games ( Section 4.1 ) and reasoning benchmarks ( Section 4.2 ). Qualitative results are available in Appendix A .

### 4.1 Multi-player coordination games

Drawing from existing literature on multi-agent communication, we design two Lewis signaling games ( Lewis, 2008 ; Lazaridou et al., 2016 ) to test the efficacy of activation communication (example prompts and answers in Table 1 ): 1. Countries , where A A is given as input a string of the format “ [ 𝙿𝙴𝚁𝚂𝙾𝙽 ] 𝚒𝚜 𝚊𝚝 𝚝𝚑𝚎 [ 𝙻𝙰𝙽𝙳𝙼𝙰𝚁𝙺 ] \mathtt{[PERSON]\text{ }is\text{ }at\text{ }the\text{ }[LANDMARK]} ” and B B is asked “ 𝚆𝚑𝚒𝚌𝚑 𝚌𝚘𝚞𝚗𝚝𝚛𝚢 𝚒𝚜 [ 𝙿𝙴𝚁𝚂𝙾𝙽 ] 𝚕𝚘𝚌𝚊𝚝𝚎𝚍 𝚒𝚗 ? \mathtt{Which\text{ }country\text{ }is\text{ }[PERSON]\text{ }located\text{ }in?} ”

2. Tip Sheets (inspired by Lewis et al. (2017) ), where A A is given a simulated “tip sheet” and B B is asked to make an informed investment decision in accordance with the information in the tip sheet.

We synthetically generate 100 100 ( Countries ) and 70 70 ( Tip Sheets ) different prompts and answers of the same format as the samples in Table 1 , and report the proportion out of those samples that B B responds with an exact string match to the ground truth answer. As baselines, we consider a “silent” (✗) setup, where the agents are not allowed to communicate; a “single-agent skyline,” where a single LLM is given the concatenation of A A and B B ’s prompts; and traditional natural language communication, where A A is asked to output a message that is then given to B B along with x B x_{B} . All decoding is done greedily.

Table 2 presents the results for both coordination games using 2 different instances of the same model as the agents ( A = B A=B ). Across the 3B and 8B model sizes, activation communication (AC) with f = 𝚛𝚎𝚙𝚕𝚊𝚌𝚎 f=\mathtt{replace} almost completely recovers the gap between the zero-communication (✗) and the single-agent skyline ( Skyline ), outperforming natural language communication (NL) using far less compute. We hypothesize that 𝚛𝚎𝚙𝚕𝚊𝚌𝚎 \mathtt{replace} is more effective than 𝚖𝚎𝚊𝚗 \mathtt{mean} and 𝚜𝚞𝚖 \mathtt{sum} as the former is guaranteed to output a vector within B B ’s activation space, while the latter two likely do not (e.g., the norm of the vector outputted by 𝚜𝚞𝚖 \mathtt{sum} will be around double that of a typical activation). Furthermore, most of the information B B needs is likely contained in its representations of previous tokens in the sequence, hence losing its final-token representation does not hurt.

### 4.2 Reasoning Benchmarks

Next, we test our methods on a variety of reasoning benchmarks, spanning several real-world tasks and domains.

#### Baselines

We benchmark activation communication against the following two baselines:

• Single Model : A single LLM responds to the prompt in natural language.

• Natural Language Debate (NLD) ( Du et al., 2023 ) : Each LLM provides an initial response to the given prompt. Then, for each of r − 1 r-1 subsequent rounds, each LLM is prompted to refine its previous response given the other agents’ responses as input. Note that NLD is the most direct baseline for our approach, as it is a state-of-the-art natural language communication protocol. We fix r = 2 r=2 in our experiments.

Note that we do not compare to Pham et al. (2024) , as they communicate the input (tokenizer) embeddings rather than activations/output embeddings between models, and hence require a shared tokenizer and embedding table between agents which is extremely restrictive and prevents applicability to our experimental setup.

To determine the values of k k and j j for activation communication (AC), we compute the accuracy on Countries and Tip Sheets for every pair ( k , j ) ∈ { 1 , … , 30 } 2 (k,j)\in\{1,\dots,30\}^{2} . Based on these results (shown in Figure 2 ) as well as Table 2 , we fix k = j = 26 k=j=26 and f f = = 𝚛𝚎𝚙𝚕𝚊𝚌𝚎 \mathtt{replace} for the following experiments.

Across all experiment configurations, we fix the decoding strategy to nucleus sampling with p = 0.9 p=0.9 .

#### Models

We conduct most of our experiments using 𝙻𝙻𝚊𝙼𝙰 \mathtt{LLaMA} - 3.2 \mathtt{3.2} - 𝟹 ​ 𝙱 \mathtt{3B} and 𝙻𝙻𝚊𝙼𝙰 \mathtt{LLaMA} - 3.1 \mathtt{3.1} - 𝟾 ​ 𝙱 \mathtt{8B} as the two agents. Additionally, to test our approach’s robustness and generalizability, we conduct experiments with models belonging to various other suites within the 𝙻𝙻𝚊𝙼𝙰 \mathtt{LLaMA} family and of several different sizes.

Note that for these experiments, we restrict the setting to communication between different models (rather than multiple instances of the same model in Section 4.1 ), since the same model would have identical activations for the same prompts, meaning no information would be communicated in the grafting process. We argue that the multiple-model setting is realistic (perhaps more so than the setting of multiple instances of the same model), as recent advances in LLM development have led to the release of models with specialized abilities ( Singhal et al., 2023 ) and of different sizes ( Dubey et al., 2024 ) that merit complementary usage. Our work thus answers the question: How can we get the best performance by leveraging multiple models of distinct capabilities and sizes, relative to the added inference-time compute over a single forward pass through any single model?

#### Datasets

We evaluate our technique on seven reasoning datasets that span various real-world tasks and domains: (i) Biographies ( Du et al., 2023 ) , which asks the LLM to generate a factual biography of a famous computer scientist; (ii) GSM8k ( Cobbe et al., 2021 ) , a variety of grade school math problems created by human problem writers; and (iii) 5 datasets randomly drawn from MMLU ( Hendrycks et al., 2021 ) : High School Psychology (from the Social Sciences category), Formal Logic (from the Humanities category), College Biology (from the STEM category), Professional Law (from the Humanities Category), and Public Relations (from the Social Sciences category). We evaluate on a randomly-sampled size- 100 100 subset of each dataset.

In experiments involving the mapping matrix 𝑾 \bm{W} , we instantiate 𝑾 ∈ ℝ 4096 × 3072 \bm{W}\in\mathbb{R}^{4096\times 3072} using Xavier initialization and train for 10 10 epochs on a dataset of 3072 3072 sentences 3 3 3 We use 3072 3072 sentences as linear regression with d d -dimensional input has a sample complexity of O ⁡ ( d ) O(d) ( Vapnik, 1999 ) . randomly drawn from the Colossal Clean Crawled Corpus (C4) ( Dodge et al., 2021 ) . We use batch size 32 32 and the Adam optimizer with learning rate 0.001 0.001 .

#### Metrics

We measure the accuracy of the final response for the single models and AC. For NLD, we measure the accuracy of the majority-held final-round answer across agents when the answer is automatically verifiable (numeric in GSM8k, multiple choice for the MMLU datasets) or the average final-round answer across agents otherwise (Biographies).

For GSM8k and the MMLU datasets, we report the proportion of samples in the dataset for which the generated answer exactly matches the ground-truth answer. For Biographies, following Du et al. (2023) , we prompt an LLM judge ( 𝙻𝙻𝚊𝙼𝙰 \mathtt{LLaMA} - 3.1 \mathtt{3.1} - 𝟾 ​ 𝙱 \mathtt{8B} ) to check whether each manually-decomposed fact in a ground-truth biography is supported ( 1 1 ), partially supported ( 0.5 0.5 ), or unsupported ( 0 0 ) in the generated biography, taking the mean of these scores over all facts as the per-biography accuracy and the mean over all dataset samples as the total accuracy.

#### Comprehensive evaluation with the 𝙻𝙻𝚊𝙼𝙰 \mathtt{LLaMA} family

Table 3 presents results on each of the seven reasoning benchmarks across various baselines and activation communication. Notably, while NLD consistently outperforms 𝙻𝙻𝚊𝙼𝙰 \mathtt{LLaMA} - 3.2 \mathtt{3.2} - 𝟹 ​ 𝙱 \mathtt{3B} , it does not always display a performance improvement over 𝙻𝙻𝚊𝙼𝙰 \mathtt{LLaMA} - 3.1 \mathtt{3.1} - 𝟾 ​ 𝙱 \mathtt{8B} ; but remarkably, AC consistently outperforms both single-model baselines . In fact, AC offers an up to 27.0 % 27.0\% improvement over NLD across six of the seven reasoning datasets. When applying 𝑾 \bm{W} to A A ’s activation before performing the replacement function, we see even further gains of 2.6 − 50.0 % 2.6-50.0\% over vanilla AC for four of the seven datasets. We hypothesize that the benefits from the learned linear layer are less consistent across datasets because the subset of C4 data used to train 𝑾 \bm{W} likely contains text more semantically similar to some datasets than others, hence some datasets provide 𝑾 \bm{W} with out-of-distribution inputs which reduces performance compared to vanilla AC.

While we fix A A as the smaller model and B B as the larger model in Table 3 (so as to ensure decoding happens with the presumably more capable model), this need not be the case; swapping A A and B B yields results of 81.5 ± 0.0 81.5\pm 0.0 and 61.0 ± 4.8 61.0\pm 4.8 on Biographies and GSM8k respectively (without the linear layer). While these accuracies are lower than their non-swapped counterparts, notably they still are higher than both single-model baselines (and higher than NLD for Biographies); plus this is much more compute-efficient as the smaller model is now the one requiring the full instead of partial forward pass.

Note that we find AC outperforms NLD on 48 of the 57 datasets in the full MMLU benchmark ; complete MMLU results, as well as a suite of additional experiments, are shown in Appendix B .

#### Performance-compute tradeoff and generalization to different model scales

Thus far, we have been considering the absolute performance of AC with respect to NLD, for which our method attains state-of-the-art results; however the superiority of activations as a language for inter-LLM communication is further illustrated by AC’s larger ratio of performance improvement to added inference-time compute over individual LMs. Figure 3 displays the results of single models, AC, and NLD across model scales and suites within the 𝙻𝙻𝚊𝙼𝙰 \mathtt{LLaMA} family on the Biographies dataset. Incoming arrows to AC and NLD nodes denote the base models between which communication occurred. Not only does AC consistently outperform both single-model baselines unlike NLD, but also notice that the slope of each black line is far greater than the slope of each gray line, indicating that AC consistently achieves greater increases in accuracy per additional unit of inference-time compute (normalized by the compute of a single forward pass through 𝙻𝙻𝚊𝙼𝙰 \mathtt{LLaMA} - 3.2 \mathtt{3.2} - 𝟷 ​ 𝙱 \mathtt{1B} on the given prompt) compared to NLD.

#### Communication across model families

Table 4 displays results for AC between models from the 𝚀𝚠𝚎𝚗 \mathtt{Qwen} - 2.5 \mathtt{2.5} , 𝙶𝚎𝚖𝚖𝚊 \mathtt{Gemma} - 𝟸 \mathtt{2} , and 𝙻𝙻𝚊𝙼𝙰 \mathtt{LLaMA} - 𝟹 \mathtt{3} families. We see that AC beats NLD across the board , and beats both individual models for 4 / 5 4/5 of the 6 6 model pairs on Biographies/GSM8k respectively —demonstrating the efficacy of AC irrespective of model architecture, size, tokenizer, and training data. Moreover, these results are obtained without training 𝑾 \bm{W} , meaning we do not need a separate projection layer between activation spaces to attain SOTA results, even for extremely distinct models! (We hypothesize this is because we are only replacing B B ’s last-token activation, hence B B can learn from A A without an extreme alteration to its activation distribution. An alternative explanation is to see this result as proof of the platonic representation hypothesis ( Huh et al., 2024 ) , which historical deep learning works have oft alluded to, including in the context of cross-model representation stitching ( Moschella et al., 2023 ; Kornblith et al., 2019 ) .)

## 5 Conclusion

We present a simple approach to enable effective and computationally efficient communication between language models by injecting information from the activations of one model into the activations of another during the forward pass. Salient features of this approach include: (i) Scales up LLMs on new tasks by leveraging existing, frozen LLMs along with zero additional task-specific parameters and data, (ii) Applies to diverse domains and settings, and (iii) Saves a substantial amount of compute .

There are some limitations to this method. First, when not using the learned model-specific mapping discussed in Section 3.1 , our method requires both models to have aligned embedding spaces, such that the activation of one model roughly retains its meaning in the other’s activation space (note that unlike past works such as Pham et al. (2024) we do not require shared tokenizers or aligned vocabularies, only aligned embeddings). While less restrictive than past works ( Pham et al., 2024 ) , this assumption is somewhat limiting, but can be relaxed when we let f f be the learned model-specific mapping; and in practice we find that even amongst different models in the 𝙻𝙻𝚊𝙼𝙰 \mathtt{LLaMA} family, no such mapping is required for state-of-the-art results.

Second, this method requires access to embeddings and will not work with black-box API access; however exploring API-only approaches is highly limiting, and recent releases of powerful open-source models ( Dubey et al., 2024 ) merit the development of embedding-based techniques.

Third, while a concern might be the limited interpretability of communicating activations as opposed to natural language, we note the following. First, there is a fundamental tradeoff between interpretability and information preservation (as activations, by virtue of being much higher-dimensional than the space of natural language, allow proportionally higher-entropy communication) ( Pham et al., 2024 ) , which merits discussion beyond the scope of this work. But second, we actually posit that our method suggests a new avenue towards interpreting LM activations: “translating” activations based on the beliefs they induce as messages in listening agents, similar to the method put forward in Andreas et al. (2018) . We recognize this as a promising avenue for future research.

Additional directions of future work include using AC to allow large LMs to leverage small, tunable LMs as “knowledge bases” during decoding ( Lee et al., 2024 ) , as in collaborative decoding ( Shen et al., 2024 ) setups; and testing our approach on more complex coordination games (e.g., Lewis-style negotiation games ( Lewis et al., 2017 ) , Diplomacy).

## Impact Statement

This paper presents work whose goal is to advance the field of Machine Learning. There are many potential societal consequences of our work, none which we feel must be specifically highlighted here.

## Acknowledgements

The authors are grateful to Jacob Andreas, Yoon Kim, and Sham Kakade for their valuable discussions and feedback.

## References

Ahn et al. (2022) Ahn, M., Brohan, A., Brown, N., Chebotar, Y., Cortes, O., David, B., Finn, C., Fu, C., Gopalakrishnan, K., Hausman, K., Herzog, A., Ho, D., Hsu, J., Ibarz, J., Ichter, B., Irpan, A., Jang, E., Ruano, R. J., Jeffrey, K., Jesmonth, S., Joshi, N. J., Julian, R., Kalashnikov, D., Kuang, Y., Lee, K.-H., Levine, S., Lu, Y., Luu, L., Parada, C., Pastor, P., Quiambao, J., Rao, K., Rettinghouse, J., Reyes, D., Sermanet, P., Sievers, N., Tan, C., Toshev, A., Vanhoucke, V., Xia, F., Xiao, T., Xu, P., Xu, S., Yan, M., and Zeng, A. Do as i can, not as i say: Grounding language in robotic affordances, 2022.

Andreas et al. (2018) Andreas, J., Dragan, A., and Klein, D. Translating neuralese, 2018.

Bansal et al. (2024) Bansal, R., Samanta, B., Dalmia, S., Gupta, N., Vashishth, S., Ganapathy, S., Bapna, A., Jain, P., and Talukdar, P. Llm augmented llms: Expanding capabilities through composition, 2024.

Burns et al. (2023) Burns, C., Izmailov, P., Kirchner, J. H., Baker, B., Gao, L., Aschenbrenner, L., Chen, Y., Ecoffet, A., Joglekar, M., Leike, J., Sutskever, I., and Wu, J. Weak-to-strong generalization: Eliciting strong capabilities with weak supervision, 2023.

Chaabouni et al. (2019) Chaabouni, R., Kharitonov, E., Lazaric, A., Dupoux, E., and Baroni, M. Word-order biases in deep-agent emergent communication. In Korhonen, A., Traum, D., and Màrquez, L. (eds.), Proceedings of the 57th Annual Meeting of the Association for Computational Linguistics , pp. 5166–5175, Florence, Italy, July 2019. Association for Computational Linguistics. doi: 10.18653/v1/P19-1509 . URL https://aclanthology.org/P19-1509 .

Cobbe et al. (2021) Cobbe, K., Kosaraju, V., Bavarian, M., Chen, M., Jun, H., Kaiser, L., Plappert, M., Tworek, J., Hilton, J., Nakano, R., Hesse, C., and Schulman, J. Training verifiers to solve math word problems, 2021.

Dodge et al. (2021) Dodge, J., Sap, M., Marasović, A., Agnew, W., Ilharco, G., Groeneveld, D., Mitchell, M., and Gardner, M. Documenting large webtext corpora: A case study on the colossal clean crawled corpus, 2021. URL https://arxiv.org/abs/2104.08758 .

Du et al. (2023) Du, Y., Li, S., Torralba, A., Tenenbaum, J. B., and Mordatch, I. Improving factuality and reasoning in language models through multiagent debate, 2023.

Dubey et al. (2024) Dubey, A., Jauhri, A., Pandey, A., Kadian, A., Al-Dahle, A., Letman, A., Mathur, A., Schelten, A., Yang, A., Fan, A., Goyal, A., Hartshorn, A., Yang, A., Mitra, A., Sravankumar, A., Korenev, A., Hinsvark, A., Rao, A., Zhang, A., Rodriguez, A., Gregerson, A., Spataru, A., Roziere, B., Biron, B., Tang, B., Chern, B., Caucheteux, C., Nayak, C., Bi, C., Marra, C., McConnell, C., Keller, C., Touret, C., Wu, C., Wong, C., Ferrer, C. C., Nikolaidis, C., Allonsius, D., Song, D., Pintz, D., Livshits, D., Esiobu, D., Choudhary, D., Mahajan, D., Garcia-Olano, D., Perino, D., Hupkes, D., Lakomkin, E., AlBadawy, E., Lobanova, E., Dinan, E., Smith, E. M., Radenovic, F., Zhang, F., Synnaeve, G., Lee, G., Anderson, G. L., Nail, G., Mialon, G., Pang, G., Cucurell, G., Nguyen, H., Korevaar, H., Xu, H., Touvron, H., Zarov, I., Ibarra, I. A., Kloumann, I., Misra, I., Evtimov, I., Copet, J., Lee, J., Geffert, J., Vranes, J., Park, J., Mahadeokar, J., Shah, J., van der Linde, J., Billock, J., Hong, J., Lee, J., Fu, J., Chi, J., Huang, J., Liu, J., Wang, J., Yu, J., Bitton, J., Spisak, J., Park, J., Rocca, J., Johnstun, J., Saxe, J., Jia, J., Alwala, K. V., Upasani, K., Plawiak, K., Li, K., Heafield, K., Stone, K., El-Arini, K., Iyer, K., Malik, K., Chiu, K., Bhalla, K., Rantala-Yeary, L., van der Maaten, L., Chen, L., Tan, L., Jenkins, L., Martin, L., Madaan, L., Malo, L., Blecher, L., Landzaat, L., de Oliveira, L., Muzzi, M., Pasupuleti, M., Singh, M., Paluri, M., Kardas, M., Oldham, M., Rita, M., Pavlova, M., Kambadur, M., Lewis, M., Si, M., Singh, M. K., Hassan, M., Goyal, N., Torabi, N., Bashlykov, N., Bogoychev, N., Chatterji, N., Duchenne, O., Çelebi, O., Alrassy, P., Zhang, P., Li, P., Vasic, P., Weng, P., Bhargava, P., Dubal, P., Krishnan, P., Koura, P. S., Xu, P., He, Q., Dong, Q., Srinivasan, R., Ganapathy, R., Calderer, R., Cabral, R. S., Stojnic, R., Raileanu, R., Girdhar, R., Patel, R., Sauvestre, R., Polidoro, R., Sumbaly, R., Taylor, R., Silva, R., Hou, R., Wang, R., Hosseini, S., Chennabasappa, S., Singh, S., Bell, S., Kim, S. S., Edunov, S., Nie, S., Narang, S., Raparthy, S., Shen, S., Wan, S., Bhosale, S., Zhang, S., Vandenhende, S., Batra, S., Whitman, S., Sootla, S., Collot, S., Gururangan, S., Borodinsky, S., Herman, T., Fowler, T., Sheasha, T., Georgiou, T., Scialom, T., Speckbacher, T., Mihaylov, T., Xiao, T., Karn, U., Goswami, V., Gupta, V., Ramanathan, V., Kerkez, V., Gonguet, V., Do, V., Vogeti, V., Petrovic, V., Chu, W., Xiong, W., Fu, W., Meers, W., Martinet, X., Wang, X., Tan, X. E., Xie, X., Jia, X., Wang, X., Goldschlag, Y., Gaur, Y., Babaei, Y., Wen, Y., Song, Y., Zhang, Y., Li, Y., Mao, Y., Coudert, Z. D., Yan, Z., Chen, Z., Papakipos, Z., Singh, A., Grattafiori, A., Jain, A., Kelsey, A., Shajnfeld, A., Gangidi, A., Victoria, A., Goldstand, A., Menon, A., Sharma, A., Boesenberg, A., Vaughan, A., Baevski, A., Feinstein, A., Kallet, A., Sangani, A., Yunus, A., Lupu, A., Alvarado, A., Caples, A., Gu, A., Ho, A., Poulton, A., Ryan, A., Ramchandani, A., Franco, A., Saraf, A., Chowdhury, A., Gabriel, A., Bharambe, A., Eisenman, A., Yazdan, A., James, B., Maurer, B., Leonhardi, B., Huang, B., Loyd, B., Paola, B. D., Paranjape, B., Liu, B., Wu, B., Ni, B., Hancock, B., Wasti, B., Spence, B., Stojkovic, B., Gamido, B., Montalvo, B., Parker, C., Burton, C., Mejia, C., Wang, C., Kim, C., Zhou, C., Hu, C., Chu, C.-H., Cai, C., Tindal, C., Feichtenhofer, C., Civin, D., Beaty, D., Kreymer, D., Li, D., Wyatt, D., Adkins, D., Xu, D., Testuggine, D., David, D., Parikh, D., Liskovich, D., Foss, D., Wang, D., Le, D., Holland, D., Dowling, E., Jamil, E., Montgomery, E., Presani, E., Hahn, E., Wood, E., Brinkman, E., Arcaute, E., Dunbar, E., Smothers, E., Sun, F., Kreuk, F., Tian, F., Ozgenel, F., Caggioni, F., Guzmán, F., Kanayet, F., Seide, F., Florez, G. M., Schwarz, G., Badeer, G., Swee, G., Halpern, G., Thattai, G., Herman, G., Sizov, G., Guangyi, Zhang, Lakshminarayanan, G., Shojanazeri, H., Zou, H., Wang, H., Zha, H., Habeeb, H., Rudolph, H., Suk, H., Aspegren, H., Goldman, H., Damlaj, I., Molybog, I., Tufanov, I., Veliche, I.-E., Gat, I., Weissman, J., Geboski, J., Kohli, J., Asher, J., Gaya, J.-B., Marcus, J., Tang, J., Chan, J., Zhen, J., Reizenstein, J., Teboul, J., Zhong, J., Jin, J., Yang, J., Cummings, J., Carvill, J., Shepard, J., McPhie, J., Torres, J., Ginsburg, J., Wang, J., Wu, K., U, K. H., Saxena, K., Prasad, K., Khandelwal, K., Zand, K., Matosich, K., Veeraraghavan, K., Michelena, K., Li, K., Huang, K., Chawla, K., Lakhotia, K., Huang, K., Chen, L., Garg, L., A, L., Silva, L., Bell, L., Zhang, L., Guo, L., Yu, L., Moshkovich, L., Wehrstedt, L., Khabsa, M., Avalani, M., Bhatt, M., Tsimpoukelli, M., Mankus, M., Hasson, M., Lennie, M., Reso, M., Groshev, M., Naumov, M., Lathi, M., Keneally, M., Seltzer, M. L., Valko, M., Restrepo, M., Patel, M., Vyatskov, M., Samvelyan, M., Clark, M., Macey, M., Wang, M., Hermoso, M. J., Metanat, M., Rastegari, M., Bansal, M., Santhanam, N., Parks, N., White, N., Bawa, N., Singhal, N., Egebo, N., Usunier, N., Laptev, N. P., Dong, N., Zhang, N., Cheng, N., Chernoguz, O., Hart, O., Salpekar, O., Kalinli, O., Kent, P., Parekh, P., Saab, P., Balaji, P., Rittner, P., Bontrager, P., Roux, P., Dollar, P., Zvyagina, P., Ratanchandani, P., Yuvraj, P., Liang, Q., Alao, R., Rodriguez, R., Ayub, R., Murthy, R., Nayani, R., Mitra, R., Li, R., Hogan, R., Battey, R., Wang, R., Maheswari, R., Howes, R., Rinott, R., Bondu, S. J., Datta, S., Chugh, S., Hunt, S., Dhillon, S., Sidorov, S., Pan, S., Verma, S., Yamamoto, S., Ramaswamy, S., Lindsay, S., Lindsay, S., Feng, S., Lin, S., Zha, S. C., Shankar, S., Zhang, S., Zhang, S., Wang, S., Agarwal, S., Sajuyigbe, S., Chintala, S., Max, S., Chen, S., Kehoe, S., Satterfield, S., Govindaprasad, S., Gupta, S., Cho, S., Virk, S., Subramanian, S., Choudhury, S., Goldman, S., Remez, T., Glaser, T., Best, T., Kohler, T., Robinson, T., Li, T., Zhang, T., Matthews, T., Chou, T., Shaked, T., Vontimitta, V., Ajayi, V., Montanez, V., Mohan, V., Kumar, V. S., Mangla, V., Albiero, V., Ionescu, V., Poenaru, V., Mihailescu, V. T., Ivanov, V., Li, W., Wang, W., Jiang, W., Bouaziz, W., Constable, W., Tang, X., Wang, X., Wu, X., Wang, X., Xia, X., Wu, X., Gao, X., Chen, Y., Hu, Y., Jia, Y., Qi, Y., Li, Y., Zhang, Y., Zhang, Y., Adi, Y., Nam, Y., Yu, Wang, Hao, Y., Qian, Y., He, Y., Rait, Z., DeVito, Z., Rosnbrick, Z., Wen, Z., Yang, Z., and Zhao, Z. The llama 3 herd of models, 2024. URL https://arxiv.org/abs/2407.21783 .

Foerster et al. (2016) Foerster, J. N., Assael, Y. M., de Freitas, N., and Whiteson, S. Learning to communicate with deep multi-agent reinforcement learning, 2016.

Geiping et al. (2025) Geiping, J., McLeish, S., Jain, N., Kirchenbauer, J., Singh, S., Bartoldson, B. R., Kailkhura, B., Bhatele, A., and Goldstein, T. Scaling up test-time compute with latent reasoning: A recurrent depth approach, 2025. URL https://arxiv.org/abs/2502.05171 .

Hao et al. (2024) Hao, S., Sukhbaatar, S., Su, D., Li, X., Hu, Z., Weston, J., and Tian, Y. Training large language models to reason in a continuous latent space, 2024. URL https://arxiv.org/abs/2412.06769 .

Hendrycks et al. (2021) Hendrycks, D., Burns, C., Basart, S., Zou, A., Mazeika, M., Song, D., and Steinhardt, J. Measuring massive multitask language understanding, 2021. URL https://arxiv.org/abs/2009.03300 .

Hernandez et al. (2024) Hernandez, E., Sharma, A. S., Haklay, T., Meng, K., Wattenberg, M., Andreas, J., Belinkov, Y., and Bau, D. Linearity of relation decoding in transformer language models, 2024.

Hewitt & Manning (2019) Hewitt, J. and Manning, C. D. A structural probe for finding syntax in word representations. In Burstein, J., Doran, C., and Solorio, T. (eds.), Proceedings of the 2019 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies, Volume 1 (Long and Short Papers) , pp. 4129–4138, Minneapolis, Minnesota, June 2019. Association for Computational Linguistics. doi: 10.18653/v1/N19-1419 . URL https://aclanthology.org/N19-1419 .

Hoffmann et al. (2022) Hoffmann, J., Borgeaud, S., Mensch, A., Buchatskaya, E., Cai, T., Rutherford, E., de Las Casas, D., Hendricks, L. A., Welbl, J., Clark, A., Hennigan, T., Noland, E., Millican, K., van den Driessche, G., Damoc, B., Guy, A., Osindero, S., Simonyan, K., Elsen, E., Rae, J. W., Vinyals, O., and Sifre, L. Training compute-optimal large language models, 2022.

Huh et al. (2024) Huh, M., Cheung, B., Wang, T., and Isola, P. The platonic representation hypothesis, 2024. URL https://arxiv.org/abs/2405.07987 .

Ilharco et al. (2023) Ilharco, G., Ribeiro, M. T., Wortsman, M., Gururangan, S., Schmidt, L., Hajishirzi, H., and Farhadi, A. Editing models with task arithmetic, 2023.

Jaques et al. (2019) Jaques, N., Lazaridou, A., Hughes, E., Gulcehre, C., Ortega, P. A., Strouse, D., Leibo, J. Z., and de Freitas, N. Social influence as intrinsic motivation for multi-agent deep reinforcement learning, 2019.

Kornblith et al. (2019) Kornblith, S., Norouzi, M., Lee, H., and Hinton, G. Similarity of neural network representations revisited, 2019. URL https://arxiv.org/abs/1905.00414 .

Lazaridou et al. (2016) Lazaridou, A., Peysakhovich, A., and Baroni, M. Multi-agent cooperation and the emergence of (natural) language. arXiv preprint arXiv:1612.07182 , 2016.

Lazaridou et al. (2017) Lazaridou, A., Peysakhovich, A., and Baroni, M. Multi-agent cooperation and the emergence of (natural) language, 2017.

Lee et al. (2024) Lee, J., Yang, F., Tran, T., Hu, Q., Barut, E., Chang, K.-W., and Su, C. Can small language models help large language models reason better?: Lm-guided chain-of-thought, 2024. URL https://arxiv.org/abs/2404.03414 .

Lewis (2008) Lewis, D. Convention: A philosophical study . John Wiley & Sons, 2008.

Lewis et al. (2017) Lewis, M., Yarats, D., Dauphin, Y. N., Parikh, D., and Batra, D. Deal or no deal? end-to-end learning for negotiation dialogues, 2017.

Li et al. (2023) Li, G., Hammoud, H. A. A. K., Itani, H., Khizbullin, D., and Ghanem, B. Camel: Communicative agents for ”mind” exploration of large language model society, 2023. URL https://arxiv.org/abs/2303.17760 .

Li et al. (2024) Li, K., Patel, O., Viégas, F., Pfister, H., and Wattenberg, M. Inference-time intervention: Eliciting truthful answers from a language model. Advances in Neural Information Processing Systems , 36, 2024.

Liang et al. (2023) Liang, T., He, Z., Jiao, W., Wang, X., Wang, Y., Wang, R., Yang, Y., Tu, Z., and Shi, S. Encouraging divergent thinking in large language models through multi-agent debate, 2023.

Lowe et al. (2020) Lowe, R., Wu, Y., Tamar, A., Harb, J., Abbeel, P., and Mordatch, I. Multi-agent actor-critic for mixed cooperative-competitive environments, 2020.

Moschella et al. (2023) Moschella, L., Maiorca, V., Fumero, M., Norelli, A., Locatello, F., and Rodolà, E. Relative representations enable zero-shot latent space communication, 2023. URL https://arxiv.org/abs/2209.15430 .

Nakano et al. (2022) Nakano, R., Hilton, J., Balaji, S., Wu, J., Ouyang, L., Kim, C., Hesse, C., Jain, S., Kosaraju, V., Saunders, W., Jiang, X., Cobbe, K., Eloundou, T., Krueger, G., Button, K., Knight, M., Chess, B., and Schulman, J. Webgpt: Browser-assisted question-answering with human feedback, 2022.

Park et al. (2023) Park, J. S., O’Brien, J. C., Cai, C. J., Morris, M. R., Liang, P., and Bernstein, M. S. Generative agents: Interactive simulacra of human behavior, 2023.

Pham et al. (2024) Pham, C., Liu, B., Yang, Y., Chen, Z., Liu, T., Yuan, J., Plummer, B. A., Wang, Z., and Yang, H. Let models speak ciphers: Multiagent debate through embeddings, 2024.

Prasad et al. (2023) Prasad, A., Koller, A., Hartmann, M., Clark, P., Sabharwal, A., Bansal, M., and Khot, T. Adapt: As-needed decomposition and planning with language models, 2023.

Schick et al. (2023) Schick, T., Dwivedi-Yu, J., Dessì, R., Raileanu, R., Lomeli, M., Zettlemoyer, L., Cancedda, N., and Scialom, T. Toolformer: Language models can teach themselves to use tools, 2023.

Shazeer et al. (2017) Shazeer, N., Mirhoseini, A., Maziarz, K., Davis, A., Le, Q., Hinton, G., and Dean, J. Outrageously large neural networks: The sparsely-gated mixture-of-experts layer, 2017.

Shen et al. (2024) Shen, S. Z., Lang, H., Wang, B., Kim, Y., and Sontag, D. Learning to decode collaboratively with multiple language models, 2024.

Shen et al. (2023) Shen, Y., Song, K., Tan, X., Li, D., Lu, W., and Zhuang, Y. Hugginggpt: Solving ai tasks with chatgpt and its friends in hugging face, 2023.

Singhal et al. (2023) Singhal, K., Tu, T., Gottweis, J., Sayres, R., Wulczyn, E., Hou, L., Clark, K., Pfohl, S., Cole-Lewis, H., Neal, D., Schaekermann, M., Wang, A., Amin, M., Lachgar, S., Mansfield, P., Prakash, S., Green, B., Dominowska, E., y Arcas, B. A., Tomasev, N., Liu, Y., Wong, R., Semturs, C., Mahdavi, S. S., Barral, J., Webster, D., Corrado, G. S., Matias, Y., Azizi, S., Karthikesalingam, A., and Natarajan, V. Towards expert-level medical question answering with large language models, 2023. URL https://arxiv.org/abs/2305.09617 .

Subramani et al. (2022) Subramani, N., Suresh, N., and Peters, M. E. Extracting latent steering vectors from pretrained language models, 2022.

Sukhbaatar et al. (2016) Sukhbaatar, S., Szlam, A., and Fergus, R. Learning multiagent communication with backpropagation, 2016.

Sukhbaatar et al. (2024) Sukhbaatar, S., Golovneva, O., Sharma, V., Xu, H., Lin, X. V., Rozière, B., Kahn, J., Li, D., tau Yih, W., Weston, J., and Li, X. Branch-train-mix: Mixing expert llms into a mixture-of-experts llm, 2024.

Turner et al. (2023) Turner, A. M., Thiergart, L., Udell, D., Leech, G., Mini, U., and MacDiarmid, M. Activation addition: Steering language models without optimization, 2023.

Vapnik (1999) Vapnik, V. N. An overview of statistical learning theory. IEEE transactions on neural networks , 10(5):988–999, 1999.

Wang et al. (2024) Wang, L., Ma, C., Feng, X., Zhang, Z., Yang, H., Zhang, J., Chen, Z., Tang, J., Chen, X., Lin, Y., Zhao, W. X., Wei, Z., and Wen, J.-R. A survey on large language model based autonomous agents, 2024.

Wang et al. (2023) Wang, X., Wei, J., Schuurmans, D., Le, Q., Chi, E., Narang, S., Chowdhery, A., and Zhou, D. Self-consistency improves chain of thought reasoning in language models, 2023. URL https://arxiv.org/abs/2203.11171 .

Wei et al. (2022) Wei, J., Tay, Y., Bommasani, R., Raffel, C., Zoph, B., Borgeaud, S., Yogatama, D., Bosma, M., Zhou, D., Metzler, D., Chi, E. H., Hashimoto, T., Vinyals, O., Liang, P., Dean, J., and Fedus, W. Emergent abilities of large language models, 2022.

Wu et al. (2023) Wu, Q., Bansal, G., Zhang, J., Wu, Y., Li, B., Zhu, E., Jiang, L., Zhang, X., Zhang, S., Liu, J., Awadallah, A. H., White, R. W., Burger, D., and Wang, C. Autogen: Enabling next-gen llm applications via multi-agent conversation, 2023.

Xi et al. (2023) Xi, Z., Chen, W., Guo, X., He, W., Ding, Y., Hong, B., Zhang, M., Wang, J., Jin, S., Zhou, E., Zheng, R., Fan, X., Wang, X., Xiong, L., Zhou, Y., Wang, W., Jiang, C., Zou, Y., Liu, X., Yin, Z., Dou, S., Weng, R., Cheng, W., Zhang, Q., Qin, W., Zheng, Y., Qiu, X., Huang, X., and Gui, T. The rise and potential of large language model based agents: A survey, 2023.

Yang et al. (2023) Yang, H., Yue, S., and He, Y. Auto-gpt for online decision making: Benchmarks and additional opinions, 2023.

Yao et al. (2023) Yao, S., Zhao, J., Yu, D., Du, N., Shafran, I., Narasimhan, K., and Cao, Y. React: Synergizing reasoning and acting in language models, 2023.

## Appendix A Qualitative Results

## Appendix B Additional Experiments

### B.1 Modifying Activations of All Tokens

Recall that AC grafts the last-token layer- k k activation of A A into B B ’s last-token layer- j j activation. But is modifying just the last token activation enough to communicate information from A A to B B ?

Note that after applying masked attention in each of the previous Transformer layers, the last token activation of A A attends to all tokens before it, hence incorporating information from the entire sequence. Indeed, this must be the case for activation communication to recover the gap between the zero-communication and skyline setups on both coordination games, which (for Tip Sheets in particular) require information starting at the first few tokens of A A ’s prompt to be communicated.

To verify this empirically, we experiment with summing the activations of all tokens in the sequence rather than just the last (we cannot replace all tokens as this would just replace B B ’s layer- j j activation with A A ’s layer k k -activation). Results are shown in Table 5 .

Indeed, applying f f to all tokens decreases performance relative to applying f f to just the last token. Note that the fact performance generally decreases from f = f= 𝚛𝚎𝚙𝚕𝚊𝚌𝚎 \mathtt{replace} to f = f= 𝚜𝚞𝚖 \mathtt{sum} , and further with all tokens, is expected. The high performance of AC with f = f= 𝚛𝚎𝚙𝚕𝚊𝚌𝚎 \mathtt{replace} means that the edited last-token activation 𝒃 \bm{b} retains some meaning in B B ’s activation space; it is less likely for this to be the case when f = f= 𝚜𝚞𝚖 \mathtt{sum} (at the very least 𝒃 \bm{b} has norm roughly 2 × 2\times that of B B ’s original last-token activation), and when doing this for all tokens we’d expect performance to decrease even further as now all activation vectors, not just the last, are out-of-distribution with respect to B B ’s activation space.

### B.2 Incorporating Chain-of-Thought Prompting

How does AC perform in relation to NLD in cases where A A might incur a long response (possibly with chain-of-thought for intermediate answer computation)? I.e., does AC lose out on the benefits of CoT?

First, note that we still reap the benefits of CoT when we sample a completion from B B after AC ( where B B gets all the information encoding A A ’s “beliefs” about the prompt via AC, hence CoT on A A ’s side is not needed ). To verify this, we experiment with prompting A A with CoT, generating a full response, and then passing the layer- k k last-token activation of the CoT response to B B as part of AC. Results are shown in Table 6 .

Indeed, we empirically find our above intuition (in orange ) to hold, as there is no significant improvement over vanilla AC when generating from A A using CoT.

### B.3 Learning 𝑾 \bm{W} In-Distribution

Recall our reasoning about the AC ( 𝑾 ) (\bm{W}) results from Section 4.2 : “We hypothesize that the benefits from the learned linear layer are less consistent across datasets because the subset of C4 data used to train 𝑾 \bm{W} likely contains text more semantically similar to some datasets than others, hence some datasets provide 𝑾 \bm{W} with out-of-distribution inputs which reduces performance compared to vanilla AC.”

Indeed, we verify this hypothesis by training 𝑾 \bm{W} on the GSM8k train set (to produce 𝑾 in dist \bm{W}_{\textrm{in dist}} ) and then evaluating with this task-specific linear layer on the GSM8k test set. Results are shown in Table 7 .

Indeed, learning 𝑾 \bm{W} in-distribution significantly boosts performance, confirming our hypothesis. Unfortunately we cannot run this experiment for the other datasets, as there is no in-distribution training data available for MMLU (we use all public data for testing).

Hence, this suggests that AC ( 𝑾 \bm{W} ) should unilaterally improve over vanilla AC if we choose a training set with good coverage across many tasks and distributions, such that there are sentences semantically similar to prompts across the span of downstream task datasets.

### B.4 Activation Space Similarity ∝ \propto AC Performance Gain

We conduct the following experiment: for each of the six pairs of models A , B A,B in the above experiment (see Table 4 ), we compute the increase in Biographies performance with AC relative to the average individual performance of A A and B B . We also compute the matrix analogue of the squared cosine similarity between the models’ activation spaces, ∥ Y ⊤ ​ X ∥ F 2 ∥ X ∥ F 2 ​ ∥ Y ∥ F 2 , \frac{\lVert Y^{\top}X\rVert_{F}^{2}}{\lVert X\rVert_{F}^{2}\,\lVert Y\rVert_{F}^{2}}, where X X is the matrix of A A ’s activations on 3072 3072 sentences from C4 (the same dataset used to train 𝑾 \bm{W} ), Y Y is the corresponding matrix for B B , and ∥ ⋅ ∥ F \lVert\cdot\rVert_{F} denotes the Frobenius norm. This yields the plot in Figure 11 .

There is a clear positive correlation between the similarity of the activation distributions and the AC performance gain, as expected; the more aligned A A and B B ’s activation spaces are, the more semantically meaningful and useful the embedding we graft from A A to B B becomes.

### B.5 Communicating Activations Between Identical Models

Note that AC as described in Section 3.1 only supports communication between distinct models. We can extend AC to work for communication between identical models as follows: let A A and B B be instances of the same model. We can sample a completion from A A with temperature and graft the last-token layer- k k activation of the completion into B B at layer j j as part of the AC procedure. This still saves a substantial amount of compute over NLD between 2 model instances, showing our technique can apply to this setting. Table 8 shows the results of this experiment.

Indeed, while communication between multiple model instances doesn’t always show improvement over the single model itself (a well-known result from ( Du et al., 2023 ) ), AC matches/outperforms NLD on five of the seven datasets .

The intuition behind debate between multiple identical model instances is that sampling multiple completions (with temperature) from the same model yields diverse reasoning paths that can be recombined into a stronger final answer. The above experiment shows that the same intuition holds for AC—we are sampling multiple times from the same model, but passing responses between agents via AC rather than as NL messages.

### B.6 Additional Rounds of Natural Language Debate

In Section 4.2 we fix NLD to 2 2 agents and 2 2 rounds, however we find in additional experiments that AC outperforms NLD even with additional rounds, highlighting the superiority and robustness of activations as an alternative “language” for inter-LM communication. Results are shown in Table 9 ; we see that for 5 of the 7 reasoning benchmarks, AC beats NLD even with 3 3 - 4 4 rounds while using substantially less compute.

∗ Runs required too much compute

### B.7 Full MMLU Benchmark Results

Table 10 below displays complete results of both AC and NLD on the full MMLU benchmark. Notably, AC matches/outperforms NLD on 48/57 datasets, with substantially less compute used , indicating its superiority and robustness as an alternative “language” for inter-LLM communication.

## Instructions for reporting errors

We are continuing to improve HTML versions of papers, and your feedback helps enhance accessibility and mobile support. To report errors in the HTML that will help us improve conversion and rendering, choose any of the methods listed below:

Click the "Report Issue" ( ) button, located in the page header.

Tip: You can select the relevant text first, to include it in your report.

Our team has already identified the following issues . We appreciate your time reviewing and reporting rendering errors we may not have found yet. Your efforts will help us improve the HTML versions for all readers, because disability should not be a barrier to accessing research. Thank you for your continued support in championing open access for all.

Have a free development cycle? Help support accessibility at arXiv! Our collaborators at LaTeXML maintain a list of packages that need conversion , and welcome developer contributions .
