##### Report GitHub Issue

Content selection saved. Describe the issue below:

# Skip a Layer or Loop It? Learning Program-of-Layers in LLMs

###### Abstract

Large language models (LLMs) perform inference by following a fixed depth and order, non-recurrent execution of all layers. We reveal the wide existence of training-free, flexible, dynamic “program-of-layers ( PoLar )”, where pretrained layers can be packed as modules and then skipped or looped to form a customized program for each input. For most inputs, substantially shorter program executions can achieve the same or better accuracy, while incorrect predictions of the original LLM can be corrected by alternative programs with fewer layers. These observations indicate that inference admits multiple valid latent computations beyond the standard forward pass. To efficiently achieve PoLar in practice, we propose a lightweight PoLar prediction network, which learns to generate execution programs that dynamically skip or repeat pretrained layers for each input. Experiments on mathematical reasoning benchmarks demonstrate that PoLar consistently improves accuracy over standard inference and prior dynamic-depth methods, often while executing fewer layers, and that these gains persist under out-of-distribution evaluation. Our results suggest that fixed-depth execution captures only a narrow subset of an LLM’s latent reasoning capacity.

###### Keywords:

Project: https://github.com/tianyi-lab/PoLar

## 1 Introduction

Generalist foundation models, e.g., LLMs and VLMs, uniformly deploy a static, pre-defined architecture to all inputs, despite their diversity and high variance in complexity and difficulty ( Liu et al., 2020 ; Xin et al., 2020 ; Zhou et al., 2020 ; Liu et al., 2021a ) . In contrast, conventional problem solving by programs can be more flexible and adaptive in algorithmic structures and complexity. For example, an experienced programmer can save more steps and compute on easier tasks, and meanwhile knows how to scale up the space/time complexity to address more challenging problems. However, these programs are specifically designed and optimized for every problem class, so they are not as general as LLMs. This raises the questions: Is it always optimal and efficient to apply the same architecture or “program”, i.e., forward pass through all the layers in a fixed order, to different tasks? Can a generalist model further optimize its “program” applied to each input?

In this paper, we formulate layers in a pretrained LLM as a library of atomic functions that a program can call in arbitrary order for arbitrary times. This formulation allows us to represent a dynamic model architecture during inference as a program-of-layers ( PoLar ) for each input, as illustrated in Figure 1 . As the first empirical study of its kind, we investigate PoLar beyond the standard forward pass by Monte-Carlo Tree Search (MCTS) and find that better (more accurate and/or shorter) programs almost always exist for every input task evaluated. Unlike previous works on layer-skipping/recurrence, early exit, and looped transformer ( Liu et al., 2020 ; Xin et al., 2020 ; Zhou et al., 2020 ; Fan et al., 2019 ; Fan et al., 2024 ; Yang et al., 2023 ) , which only adopt one operation (either skip or repeat) to produce architectures of dynamic depths, our empirical study on the MCTS-searched programs reveals that searching in a joint space of layer-skip/repeat often discovers much better programs than those found in separate spaces. While most effective programs can be shorter than the default, increasing program complexity via skip/repeat operations can substantially improve the output quality, especially on more difficult tasks. In addition, most successful programs are predominantly composed of contiguous layer segments. These observations not only verify the broad existence of better PoLar without requiring any training, but also motivate a practical PoLar prediction method that avoids the expensive cost of MCTS in PoLar ’s large search space. In particular, we aim to replace search-based program discovery with a direct, inference-time mechanism for generating execution programs. Instead of enumerating or exploring execution paths for each input ( Li et al., 2025 ) , our goal is to predict an input-specific program-of-layers that determines how pretrained layers are executed during inference. This shifts program selection from an online search problem to a single-shot prediction problem, enabling practical deployment of program-of-layers inference in LLMs.

To this end, we propose a PoLar algorithm that predicts execution programs over frozen pretrained layers at inference time. The predicted execution program specifies how pretrained layers are selectively skipped or recurrently applied and is executed once to produce the final output. This design offers several advantages. First, it makes program-of-layers inference computationally feasible by eliminating the need for expensive per-input search. Second, by jointly supporting layer skipping and recurrence within a unified execution framework, PoLar strictly generalizes prior dynamic-depth methods that are limited to a single form of execution control. Third, it enables flexible test-time computation scaling in fully frozen models, allowing inference to adapt to input difficulty while preserving model generality.

We evaluate PoLar on a range of mathematical reasoning benchmarks using multiple pretrained LLMs. Our results show that PoLar consistently improves accuracy over standard inference and prior dynamic-depth methods, often while executing fewer layers on average. Moreover, increasing the number of candidate execution programs yields strong test-time computation scaling, and execution programs learned on in-distribution data generalize effectively to out-of-distribution benchmarks across diverse domains.

## 2 Dynamic Inference as a Program-of-Layers ( PoLar ) in Large Language Models

Inference in pretrained LLMs is implemented as a fixed-depth, fixed-order forward pass: every input is processed by executing the same sequence of transformer layers. Yet inputs to LLMs vary dramatically in difficulty. Some are answered correctly with minimal reasoning, while others require complex, multi-step computation. This discrepancy raises a basic question: Is the standard forward pass sufficient for correct inference across diverse inputs?

One possibility is that this fixed computation is indeed sufficient for all cases. Another is that correct prediction requires input-dependent variation in computation. In this work, we investigate the latter possibility. Such variation can occur either in token space, through longer and more explicit chains of thought, or within the model’s hidden states, a form of computation we refer to as latent reasoning .

Inference as the execution of a program . In this view, inference is a step-by-step procedure that selects and composes pretrained modules. The execution may vary across inputs in both length and order, while each module remains a fixed, pretrained function.

Consider a pretrained LLM with D D transformer layers, where each layer defines a fixed computation function f i : ℝ T × d → ℝ T × d , i ∈ { 0 , … , D − 1 } . \textstyle f_{i}:\mathbb{R}^{T\times d}\rightarrow\mathbb{R}^{T\times d},\quad i\in\{0,\ldots,D-1\}. A program is defined as a finite sequence of layer indices π = ( i 1 , i 2 , … , i K ) , i k ∈ { 0 , … , D − 1 } , \textstyle\pi=(i_{1},i_{2},\ldots,i_{K}),\quad i_{k}\in\{0,\ldots,D-1\}, which induces the composed computation F π = f i K ∘ ⋯ ∘ f i 1 . \textstyle F_{\pi}=f_{i_{K}}\circ\cdots\circ f_{i_{1}}. Executing a program applies this composition to the input and produces a prediction. A program is considered valid if it yields a correct prediction for a given input.

Searching for valid execution programs. We explore the space of execution programs using MCTS. Execution programs are variable-length sequences over pretrained transformer layers, allowing both skipping and repetition. This space is large, discrete, and highly non-convex, making exhaustive search infeasible. MCTS provides a principled way to prioritize promising partial programs, enabling us to verify the existence of valid programs and analyze their structural properties. We use MCTS strictly as a diagnostic tool rather than a practical inference-time method; implementation details are given in Appendix B . All experiments are conducted on DART-Math ( Tong et al., 2024 ) , a structured mathematical reasoning benchmark with five difficulty levels (DM-1 to DM-5). We evaluate four pretrained transformer models: LLaMA-3.2-3B-Instruct , Qwen1.5-MoE-A2.7B-Chat , Qwen2.5-3B-Instruct , and Qwen3-8B .

We summarize our empirical findings below.

As shown in Table 1 , execution programs that allow layer recurrence ( Loop ) consistently outperform those that allow only layer skipping ( Skip ) across all evaluated models and difficulty levels. Moreover, combining skipping with recurrence ( Skip&Loop ) yields substantially larger gains than either operation alone, achieving the highest accuracy in every setting reported in Table 1 . These results indicate that recurrence provides a stronger mechanism for improving inference than skipping alone, while the two operations play complementary roles when combined.

As shown in Figure 3 , which reports the best accuracy obtained by MCTS under explicit budgets on total layer executions, many inputs remain solvable even when the overall computation is constrained to be significantly shorter than the standard forward pass. Consistent with this trend, Figure 4 shows that across models we frequently discover valid execution programs that require fewer layer applications than standard inference. In particular, among inputs already solved correctly by standard inference (C → \rightarrow C), 71.9% admit shorter valid programs. Even for inputs initially solved incorrectly (W → \rightarrow C), 34.0% admit shorter programs that correct the model’s prediction. These results indicate that standard inference often over-computes, and that correct inference can frequently be achieved with substantially fewer latent computation steps.

While simple inputs often admit short execution programs (Finding 2), harder inputs demand greater test-time execution complexity. Across models and datasets, increasing execution depth and structural flexibility systematically expands valid program space and improves inference accuracy.

(a) Test-time scaling expands the space of valid execution programs for latent reasoning. As shown in Figure 5 (a), allocating more test-time computation—via recurrence—monotonically increases the existence of valid execution programs across models. This establishes test-time scaling at latent reasoning: greater computation yields a larger feasible program space and higher correctness.

(b) Harder inputs require more complex execution programs. Figure 5 (b) shows that the fraction of solvable inputs that require recurrence and/or skipping generally increases with dataset difficulty for most models. As task difficulty grows, valid execution programs become more constrained and increasingly rely on non-trivial execution structures rather than standard inference. This indicates that higher latent execution complexity is not merely helpful, but often necessary for solving harder inputs. The different trend observed for LLaMA-3.2-3B-Instruct is explained by a mismatch between dataset-defined difficulty and the model’s effective difficulty (Table 1 ).

(c) Inference accuracy improves systematically with execution depth. As shown in Figure 6 , for all models and difficulty levels, the average accuracy of valid execution programs increases with total execution depth, measured relative to the original forward-pass depth. This reveals a consistent computation–accuracy trade-off: while many inputs admit short execution programs (Finding 2), harder inputs benefit from—and often require— deeper or recurrent execution to achieve correct inference.

Latent execution programs reveal a continuum of test-time inference behaviors that standard inference cannot access. Allocating more execution complexity enables harder inputs to be solved and yields higher accuracy.

As shown in Figure 7 , valid execution programs discovered by pretrained models exhibit a strong structural bias toward simplicity. A segment denotes a set of layers executed as a unit and need not be contiguous, while recurrence always corresponds to re-execution of the same segment. We therefore analyze segment structure by measuring the number of consecutive layers within each segment. Most valid programs are dominated by highly local segments and involve at most a single recurrence; long-range jumps and deep iterative reuse are rare. Figure 7 (a) shows that 57.7% of segments consist of a single layer, and over two-thirds contain at most two consecutive layers, whereas segments with predominantly non-consecutive layers account for less than 2.9% of cases. Consistently, Figure 7 (b) indicates that most segments are repeated at most once. Together, these results reveal an inherent limitation of pretrained models as execution-program generators: their training objectives favor short-range, local reuse over rich program composition and complex control flow.

These findings show that standard inference selects only one execution from a vast space of valid latent programs. While MCTS reveals this space, its reliance on sequential search over an exponentially large program space makes it impractical for inference. This motivates a different approach: rather than searching over programs at test time, we ask whether a lightweight model can directly predict execution programs. Figure 2 contrasts the MCTS-based sequential search with our proposed direct program prediction approach. In the remainder of this work, we pursue this learning-based alternative, retaining the benefits of latent program selection uncovered by MCTS while eliminating sequential search.

## 3 Learning Program-of-Layers ( PoLar ) in Large Language Models

Building on our empirical analysis (Section 2 ), we propose PoLar , a method for programming pretrained language models at inference time by predicting input-specific execution programs (Figure 2 ). PoLar dynamically segments and composes pretrained layers into reusable modules, enabling flexible computation without parameter updates.

### 3.1 Program Representation

We instantiate the function library using packed modules , which segment contiguous pretrained transformer layers into reusable computation units. For a pretrained model of depth D D , an execution program specifies (i) a segmentation of layers into modules and (ii) an operation applied to each segment. Each execution program is represented by two discrete structures: a binary boundary mask encoding the segmentation, and an operation label vector specifying the segment-level operations.

Segmentation. We partition the D D layers of a pretrained model into contiguous segments [ 0 = s 1 , s 2 ) , [ s 2 , s 3 ) , … , [ s M , s M + 1 = D ) , \textstyle[0=s_{1},s_{2}),\ [s_{2},s_{3}),\ \ldots,\ [s_{M},s_{M+1}=D), with each segment length bounded by s j + 1 − s j ≤ K max s_{j+1}-s_{j}\leq K_{\max} . Segmentation is represented by a binary boundary mask 𝐳 seg ​ ( x ) ∈ { 0 , 1 } D , \textstyle\mathbf{z}^{\text{seg}}(x)\in\{0,1\}^{D}, where 𝐳 i seg = 1 \mathbf{z}^{\text{seg}}_{i}=1 indicates that layer index i i starts a new segment, and 𝐳 i seg = 0 \mathbf{z}^{\text{seg}}_{i}=0 otherwise.

We set K max = 4 K_{\max}=4 based on empirical evidence. Finding 4 in Section 2 shows that valid execution programs are dominated by short, contiguous layer segments. Bounding the segment length therefore captures the dominant local execution structures while substantially reducing the complexity of the program space. Although this representation restricts the set of admissible programs, it preserves the most prevalent compositional patterns in practice and enables stable learning with strong empirical performance.

Operations. For each segment [ s j , s j + 1 ) [s_{j},s_{j+1}) , the execution program assigns one of three operations { skip , keep , repeat } \{\textsf{skip},\textsf{keep},\textsf{repeat}\} , which determines how the segment is executed: skip \displaystyle\textsf{skip} : ∅ , \displaystyle:\emptyset, keep \displaystyle\textsf{keep} : [ s j , … , s j + 1 − 1 ] , \displaystyle:[s_{j},\ldots,s_{j+1}-1], repeat \displaystyle\textsf{repeat} : [ s j , … , s j + 1 − 1 , s j , … , s j + 1 − 1 ] . \displaystyle:[s_{j},\ldots,s_{j+1}-1,\ s_{j},\ldots,s_{j+1}-1]. The skip operator omits a segment to reduce computation, while repeat applies a single additional pass. Operations are represented by a categorical label vector 𝐳 op ​ ( x ) ∈ { skip , keep , repeat } D , \textstyle\mathbf{z}^{\text{op}}(x)\in\{\textsf{skip},\textsf{keep},\textsf{repeat}\}^{D}, where 𝐳 i op \mathbf{z}^{\text{op}}_{i} is defined only when 𝐳 i seg = 1 \mathbf{z}^{\text{seg}}_{i}=1 (i.e., at segment start positions); labels at all other positions are ignored.

This operator set is intentionally minimal and empirically grounded. Finding 4 in Section 2 shows valid execution programs rarely require more than a single re-execution within a segment, and that skip and repeat account for the most effective execution patterns, offering strong performance–efficiency trade-offs. The keep operator preserves the original computation when no modification is needed. Although our implementation allows at most one additional execution through repeat , the representation is not fundamentally limited to a single recurrence. The operation vocabulary can be extended to { repeat - ​ 2 , … , repeat - ​ k } \{\textsf{repeat}\text{-}2,\ldots,\textsf{repeat}\text{-}k\} to support multiple recurrences per segment. We use a single-repeat operator because the MCTS traces in Section 2 show that effective programs rarely benefit from deeper repeated execution of the same segment. This choice keeps the prediction space tractable while covering the dominant valid programs.

### 3.2 Program-of-Layers ( PoLar ) Prediction Network

We train a lightweight predictor to output logits for the program representation defined in Section 3.1 .

Architecture. Given an input x x , we first encode it using a frozen embedding model ( Qwen3-Embedding-0.6B ), as token-level representations 𝐇 = E ⁡ ( x ) ∈ ℝ T × d q , \textstyle\mathbf{H}=E(x)\in\mathbb{R}^{T\times d_{q}}, where T T is the token length and d q d_{q} is the hidden size of the embedding model. We project token representations to a working dimension d d : 𝐇 ~ = 𝐇𝐖 h ∈ ℝ T × d . \textstyle\tilde{\mathbf{H}}=\mathbf{H}\mathbf{W}_{h}\in\mathbb{R}^{T\times d}.

Layer queries. We associate each pretrained transformer layer index i ∈ { 0 , … , D − 1 } i\in\{0,\ldots,D-1\} with a learnable embedding 𝐞 i ∈ ℝ d \mathbf{e}_{i}\in\mathbb{R}^{d} , and stack them as 𝐄 ∈ ℝ D × d \mathbf{E}\in\mathbb{R}^{D\times d} . These embeddings act as layer-specific queries.

Cross-attention. We apply multi-head cross-attention with layer embeddings as queries and token embeddings as keys/values: 𝐗 = MHA ​ ( 𝐐 , 𝐊 , 𝐕 ) , 𝐐 = 𝐄 , 𝐊 = 𝐇 ~ , 𝐕 = 𝐇 ~ , \textstyle\mathbf{X}=\textsc{MHA}(\mathbf{Q},\mathbf{K},\mathbf{V}),\mathbf{Q}=\mathbf{E},\ \mathbf{K}=\tilde{\mathbf{H}},\ \mathbf{V}=\tilde{\mathbf{H}}, where padding tokens are masked using the input attention mask. The output 𝐗 ∈ ℝ D × d \mathbf{X}\in\mathbb{R}^{D\times d} provides an input-conditioned representation for each layer index.

Cross-layer encoder. To model dependencies across model depth, we apply a lightweight transformer encoder over the layer dimension: 𝐗 ′ = Enc layer ​ ( 𝐗 ) ∈ ℝ D × d . \textstyle\mathbf{X}^{\prime}=\textsc{Enc}_{\text{layer}}(\mathbf{X})\in\mathbb{R}^{D\times d}. This enables self-attention across layers, allowing decisions at each layer to depend on global depth context.

Prediction heads. Two linear heads produce logits for segmentation boundaries and operations: ℓ seg = 𝐗 ′ ​ 𝐖 seg + 𝐛 seg ∈ ℝ D , ℓ op = 𝐗 ′ ​ 𝐖 op + 𝐛 op ∈ ℝ D × 3 . \bm{\ell}^{\text{seg}}=\mathbf{X}^{\prime}\mathbf{W}_{\text{seg}}+\mathbf{b}_{\text{seg}}\in\mathbb{R}^{D},\bm{\ell}^{\text{op}}=\mathbf{X}^{\prime}\mathbf{W}_{\text{op}}+\mathbf{b}_{\text{op}}\in\mathbb{R}^{D\times 3}.

Supervision from Valid Execution Programs. We supervise training using valid execution programs collected offline via MCTS (Section 2 ). Each program is deterministically parsed into program representation, producing ground-truth segmentation and operation labels 𝐳 seg ​ ( x ) \mathbf{z}^{\text{seg}}(x) and 𝐳 op ​ ( x ) \mathbf{z}^{\text{op}}(x) in the format defined in Section 3.1 . When multiple valid programs are available for an input and at least one is shorter than the full model depth, we down-weight the loss of the full-depth execution. This choice follows Finding 2 , which shows that shorter valid programs are preferred while still preserving supervision from the original computation.

Training Objective. We train the predictor to match the ground-truth execution program, specified by segmentation and operation labels ( 𝐳 seg ∗ ( x ) , 𝐳 op ∗ ( x ) ) \big(\mathbf{z}^{\text{seg}*}(x),\mathbf{z}^{\text{op}*}(x)\big) . Let p i seg = σ ⁡ ( ℓ i seg ) p^{\text{seg}}_{i}=\sigma(\ell^{\text{seg}}_{i}) and 𝐩 i op = Softmax ​ ( ℓ i op ) \mathbf{p}^{\text{op}}_{i}=\textsc{Softmax}(\bm{\ell}^{\text{op}}_{i}) . Segmentation is supervised with binary cross-entropy over boundary indicators: ℒ seg = − ∑ i = 0 D − 1 [ 𝐳 i seg ∗ log p i seg + ( 1 − 𝐳 i seg ∗ ) log ( 1 − p i seg ) ] . \textstyle\mathcal{L}_{\text{seg}}=-\sum_{i=0}^{D-1}\Big[\mathbf{z}^{\text{seg}*}_{i}\log p^{\text{seg}}_{i}+(1-\mathbf{z}^{\text{seg}*}_{i})\log(1-p^{\text{seg}}_{i})\Big]. Operation prediction uses a masked cross-entropy applied only at segment start positions. With mask m i = 𝐳 seg ∗ i m_{i}=\mathbf{z}^{\text{seg}*}_{i} , we compute ℒ op = − ∑ i = 0 D − 1 m i ⋅ log 𝐩 i op [ 𝐳 i op ∗ ] . \textstyle\mathcal{L}_{\text{op}}=-\sum_{i=0}^{D-1}m_{i}\cdot\log\mathbf{p}^{\text{op}}_{i}\big[\mathbf{z}^{\text{op}*}_{i}\big]. The final objective is ℒ = ℒ seg + ℒ op . \mathcal{L}=\mathcal{L}_{\text{seg}}+\mathcal{L}_{\text{op}}.

Inference-Time Program Decoding. At inference time, execution programs are decoded in two stages. First, segment boundaries are determined deterministically by thresholding the predicted segmentation logits ℓ seg \bm{\ell}^{\text{seg}} . If any resulting segment exceeds the maximum length constraint K max K_{\max} , additional boundaries are inserted to enforce it, yielding segment start positions { s j } \{s_{j}\} . Conditioned on this segmentation, we compute operation log-probabilities at each segment start from the predicted logits: log ⁡ p ⁡ ( o j ∣ x , s j ) = log ⁡ Softmax ​ ( ℓ s j op ) ​ [ o j ] . \textstyle\log p(o_{j}\mid x,s_{j})=\log\textsc{Softmax}\!\big(\bm{\ell}^{\text{op}}_{s_{j}}\big)[o_{j}]. Rather than selecting operations independently via local argmax, we apply a small beam search over segment-level operation choices to account for non-local interactions between segments and to ensure globally consistent execution programs. This search operates over a highly constrained space and produces a ranked set of candidate execution programs π ⁡ ( x ) \pi(x) . Finally, each candidate program is mapped deterministically to a concrete executed program using the segment-to-path rules in Section 3.1 .

## 4 Experiments

We evaluate PoLar across both in-distribution and out-of-distribution benchmarks to assess whether learning latent execution programs provides a practical and transferable alternative to search-based test-time computation.

### 4.1 Experimental Setup

Models. We evaluate PoLar on a diverse set of pretrained, instruction-tuned LLMs spanning different architectures and scales: LLaMA-3.2-3B-Instruct , Qwen1.5-MoE-A2.7B-Chat , Qwen2.5-3B-Instruct , and Qwen3-8B . All models are used in a fully frozen setting with no parameter updates.

Datasets. We use DART-Math ( Tong et al., 2024 ) , a structured mathematical reasoning dataset with five difficulty levels (DM-1 to DM-5), as in-distribution benchmark. For out-of-distribution (OOD) evaluation, we use ASDiv ( Miao et al., 2020 ) and MAWPS ( Kadlčík et al., 2023 ) , which focus on arithmetic word problems, as well as subject subsets from MMLU-Pro ( Wang et al., 2024 ) spanning mathematics, natural sciences, social sciences, and humanities. These benchmarks differ substantially from DART-Math in both format and domain coverage.

In-distribution evaluation. For DART-Math, we first deduplicate examples within each difficulty level by question text and then adopt a difficulty-wise train/test split: each difficulty level is split independently, and models are trained and evaluated within the same difficulty distribution.

Out-of-distribution (OOD) evaluation. For OOD evaluation, PoLar is trained on the union of DART-Math training data across all difficulty levels and evaluated zero-shot. This setting directly tests whether PoLar learns transferable computation control strategies rather than heuristics specific to a dataset or difficulty level.

Metric. We report pass@ k k accuracy , defined as the probability that at least one of the top- k k candidates produces a correct answer. For PoLar , the k k candidates correspond to the top- k k predicted execution programs selected via beam search. For sampling-based baselines, k k corresponds to the number of stochastic decoding samples. Unless otherwise stated, OOD results are reported using pass@1.

Baselines. We compare PoLar against standard inference and representative dynamic-computation methods. Base ( τ = 0 \tau=0 ) uses greedy decoding with temperature τ = 0 \tau=0 . Base (sampling) samples k k outputs using stochastic decoding with τ ∈ { 0.3 , 0.7 , 1.0 } \tau\in\{0.3,0.7,1.0\} and reports the best result across temperatures, increasing output diversity without altering internal execution. DR.LLM ( Heakl et al., 2025 ) learns layer-routing policies from execution paths and applies them at inference time. ShortGPT ( Men et al., 2025 ) statically prunes layers based on estimated importance, yielding a reduced-depth model. MindSkip ( He et al., 2024 ) and FlexiDepth ( Luo et al., 2025 ) learn router-based dynamic-depth policies, primarily optimized for inference efficiency. Several approaches, such as Mixture-of-Depths ( Raposo et al., 2024 ) , LaCo ( Yang et al., 2024 ) , and Mixture-of-Recursions ( Bae et al., 2025 ) , require substantial additional training or architectural modification. In contrast, PoLar performs lightweight test-time program selection without modifying pretrained model parameters.

More dataset and training details are in Appendix D .

### 4.2 Main Results

We evaluate in-distribution performance on DART-Math. Table 2 reports pass@ k k results using LLaMA-3.2-3B-Instruct , with complete results provided in Appendix C.1 .

Accuracy gains arise from improved latent execution within the frozen model. At pass@1, PoLar outperforms Base (sampling) across all difficulty levels. For example, on DM-1, accuracy improves from 48.9% to 54.6%, yielding an absolute pass@1 gain of +5.7 percentage points. Since pass@1 evaluates a single decoded output, this gain reflects more effective latent execution selection rather than output-space diversity.

Exploring the execution-program space enables effective test-time scaling. Increasing the number of candidate execution programs ( k k ) monotonically improves PoLar , evidencing effective test-time computation scaling through execution-program exploration. Figure 8 (a) illustrates this behavior on LLaMA-3.2-3B-Instruct, macro-averaged across DART-Math DM-1 to DM-5: Base (sampling) improves from 32.8% at pass@1 to 43.8% at pass@5, while PoLar improves from 35.1% to 51.2%. Thus, at pass@5, PoLar achieves an average absolute gain of +7.4 percentage points over Base (sampling). Crucially, Figure 8 (b) shows that among successful top-5 candidates, PoLar often finds execution programs that use fewer unique layers than a standard forward pass, indicating that the gains arise from better latent execution programs rather than simply executing the full depth. In contrast, Base (sampling) explores output-space diversity under a fixed computation graph and therefore always uses the original full-depth execution. These results show that structured execution-program exploration can outperform output sampling under the same frozen model.

Program-level execution exploration is more effective than local routing decisions. Existing dynamic-depth methods primarily make local, layer-wise routing decisions, which restrict inference to a limited execution space and often degrade accuracy in our setting. DR.LLM supports both layer skipping and repetition but operates at the individual-layer level, limiting global coordination across depth. In contrast, PoLar formulates inference as program-level exploration over execution programs defined on packed contiguous segments, enabling coordinated skip and repeat patterns across depth. This design directly reflects the execution structures uncovered by MCTS, while replacing expensive search with a lightweight, learned predictor.

PoLar incurs negligible inference overhead and reduces end-to-end latency. Beyond counting executed layers, we measure wall-clock latency on Qwen1.5-MoE-A2.7B-Chat with 24 layers. As shown in Table 4 , the encoder, predictor head, and beam search introduce a total additional overhead of only 3.05 ms, corresponding to 0.8% of a standard forward pass and approximately 0.23 LLM layers. This overhead is small compared with the latency reduction achieved by executing fewer layers. Consequently, PoLar reduces end-to-end latency while improving accuracy: it achieves 0.83 × \times the base runtime on easier inputs and 0.95 × \times on harder inputs. The learned predictor is also lightweight in parameter count: across all evaluated backbones, it contains approximately 2.1M parameters, corresponding to only 0.01%–0.06% of the base LLM size. Full parameter counts are provided in Appendix D.3 .

### 4.3 Out-of-Distribution Performance

We evaluate the OOD generalization of execution programs learned from in-distribution data. As shown in Table 3 , PoLar consistently outperforms standard inference on all OOD benchmarks using Qwen1.5-MoE-A2.7B-Chat , with full results reported in Appendix C.2 .

Execution programs learned on mathematical datasets transfer across domains. On arithmetic word problem benchmarks such as ASDiv and MAWPS, PoLar achieves clear improvements over the standard forward pass. More notably, on MMLU-Pro, PoLar improves accuracy across diverse subject areas. We conjecture that this cross-domain transfer comes from two complementary sources. First, the external input representation maps examples from different domains into a shared semantic space, allowing the small PoLar prediction head trained on mathematics to generalize beyond its training distribution. Second, the predicted programs are constrained to simple structural patterns, namely contiguous segments with limited recurrence, which encourages reusable computation strategies rather than benchmark-specific execution heuristics.

## 5 Related Works

Transformers process inputs through sequential layer stacks, making layer-level computation reduction a critical research direction. Early-exit and layer skipping methods ( Liu et al., 2020 ; Xin et al., 2020 ; Zhou et al., 2020 ; Liu et al., 2021a ) dynamically terminate computation at intermediate layers using auxiliary classifiers and confidence metrics, allowing easy inputs to exit early. LayerSkip ( Elhoushi et al., 2024 ) shares classifiers across layers to reduce overhead. LayerDrop ( Fan et al., 2019 ) trains models so arbitrary layer subsets can be skipped during inference. ShortGPT ( Men et al., 2025 ) assesses layer importance based on input-output similarity and drops low-importance layers. LaCo ( Yang et al., 2024 ) merges layers using weight arithmetic. Recent work introduces learned routing for adaptive skipping: FlexiDepth ( Luo et al., 2025 ) and MindSkip ( He et al., 2024 ) attach lightweight routers to pretrained models for input-adaptive layer skipping.

In addition to skipping layers, another line of research explores layer reuse and recurrence. Universal Transformers ( Dehghani et al., 2018 ) apply self-attention blocks recurrently with halting mechanisms to adapt depth per token. Recent looped transformers ( Fan et al., 2024 ; Yang et al., 2023 ) repeatedly apply single blocks to achieve better length generalization on algorithmic tasks by adjusting loop counts during inference. The Inner Thinking Transformer ( Chen et al., 2025 ) interleaves adaptive loops with residual ”thinking” connections and per-token routing, devoting extra computation to difficult tokens. While these approaches demonstrate the value of recurrence, they require architectural redesign and training from scratch.

Li et al. (2025) studies test-time depth adaptation by using search to dynamically skip or repeat pretrained transformer layers without finetuning. Their work demonstrates that alternative execution paths can improve inference, but the method remains search-based and requires expensive per-input program discovery. In contrast, we use MCTS only as an offline diagnostic tool to characterize the structure of the program space, and then replace search with a learned predictor that generates execution programs in a single shot.

Following this direction, DR.LLM ( Heakl et al., 2025 ) learns routing policies from MCTS-generated supervision and supports both skipping and repeating layers. However, DR.LLM performs sequential layer-wise routing, where each decision is made locally during the forward pass and depends on intermediate hidden states. In contrast, PoLar predicts the entire execution program upfront, before executing the frozen LLM. This avoids interleaving routing with layer execution and enables more efficient inference. Moreover, DR.LLM is limited to single-layer recurrence, whereas PoLar operates on contiguous layer segments; for example, PoLar can represent multi-layer recurrent modules such as 4 → 5 → 4 → 5 4{\rightarrow}5{\rightarrow}4{\rightarrow}5 , which are outside the single-layer routing space. Thus, PoLar provides a more coordinated and expressive program space while preserving fully frozen base model parameters.

## 6 Conclusion

We show that inference in LLMs need not be limited to a fixed-depth forward pass. By viewing pretrained transformer layers as reusable functions, we uncover multiple valid execution programs for a single input, many of which are shorter than standard execution and can correct model errors. Motivated by this insight, we introduce PoLar , a lightweight framework that predicts input-dependent execution programs by selectively skipping or repeating contiguous layer segments at inference time, without modifying model parameters. Across models and both in-distribution and out-of-distribution benchmarks, PoLar consistently outperforms standard inference and prior dynamic-depth methods. These findings suggest that fixed-depth execution captures only a narrow subset of an LLM’s latent reasoning capacity. Enabling flexible, programmatic execution over pretrained layers reallocates computation at inference time, offering a simple and effective route to more expressive and efficient inference in foundation models.

## Impact Statement

This work adapts the internal computation of pretrained LLMs at inference time by dynamically skipping or repeating layer segments. Its main potential benefit is improved efficiency: PoLar can reduce unnecessary computation on easier inputs while allocating more latent computation to harder ones, lowering inference cost, latency, and energy use without retraining the base model. This may make capable LLMs more accessible to researchers and practitioners with limited compute, and may support more sustainable deployment of foundation models. As with other methods that improve LLM capability or efficiency, broader deployment may amplify both beneficial and harmful uses. Potential benefits include education, scientific reasoning, and software assistance, while potential misuse includes scalable generation of misleading or harmful content. These risks largely arise from the underlying pretrained models and their applications rather than from dynamic execution itself. Since PoLar changes the execution path in an input-dependent manner, future work may further study how such paths can be audited or interpreted. Our experiments focus on mathematical reasoning and related benchmarks. Before applying dynamic execution in high-stakes domains, future work should evaluate robustness, calibration, interpretability, and safety alongside accuracy and efficiency. We hope this work encourages more responsible test-time computation methods that improve model performance while making compute allocation more transparent and efficient.

## References

Andreas et al. (2016) J. Andreas, M. Rohrbach, T. Darrell, and D. Klein Neural module networks . In Proceedings of the IEEE conference on computer vision and pattern recognition , pp. 39–48 . Cited by: Appendix A .

Bae et al. (2025) S. Bae, Y. Kim, R. Bayat, S. Kim, J. Ha, T. Schuster, A. Fisch, H. Harutyunyan, Z. Ji, A. Courville, et al. Mixture-of-recursions: learning dynamic recursive depths for adaptive token-level computation . arXiv preprint arXiv:2507.10524 . Cited by: §4.1 .

Chen et al. (2025) Y. Chen, J. Shang, Z. Zhang, Y. Xie, J. Sheng, T. Liu, S. Wang, Y. Sun, H. Wu, and H. Wang Inner thinking transformer: leveraging dynamic depth scaling to foster adaptive internal thinking . arXiv preprint arXiv:2502.13842 . Cited by: Appendix A , §5 .

Dehghani et al. (2018) M. Dehghani, S. Gouws, O. Vinyals, J. Uszkoreit, and Ł. Kaiser Universal transformers . arXiv preprint arXiv:1807.03819 . Cited by: Appendix A , §5 .

Elhoushi et al. (2024) M. Elhoushi, A. Shrivastava, D. Liskovich, B. Hosmer, B. Wasti, L. Lai, A. Mahmoud, B. Acun, S. Agarwal, A. Roman, et al. Layerskip: enabling early exit inference and self-speculative decoding . In Proceedings of the 62nd Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers) , pp. 12622–12642 . Cited by: §5 .

Eyzaguirre et al. (2022) C. Eyzaguirre, F. Del Rio, V. Araujo, and A. Soto DACT-bert: differentiable adaptive computation time for an efficient bert inference . In Proceedings of NLP Power! The First Workshop on Efficient Benchmarking in NLP , pp. 93–99 . Cited by: Appendix A .

Fan et al. (2019) A. Fan, E. Grave, and A. Joulin Reducing transformer depth on demand with structured dropout . arXiv preprint arXiv:1909.11556 . Cited by: Appendix A , §1 , §5 .

Fan et al. (2024) Y. Fan, Y. Du, K. Ramchandran, and K. Lee Looped transformers for length generalization . arXiv preprint arXiv:2409.15647 . Cited by: Appendix A , §1 , §5 .

Gordon et al. (2020) M. Gordon, K. Duh, and N. Andrews Compressing bert: studying the effects of weight pruning on transfer learning . In Proceedings of the 5th Workshop on Representation Learning for NLP , pp. 143–155 . Cited by: Appendix A .

He et al. (2024) S. He, T. Ge, G. Sun, B. Tian, X. Wang, and D. Yu Router-tuning: a simple and effective approach for enabling dynamic-depth in transformers . arXiv preprint arXiv:2410.13184 . Cited by: §4.1 , §5 .

Heakl et al. (2025) A. Heakl, M. Gubri, S. Khan, S. Yun, and S. J. Oh Dr. llm: dynamic layer routing in llms . arXiv preprint arXiv:2510.12773 . Cited by: §4.1 , §5 .

Jain et al. (2024) G. Jain, N. Hegde, A. Kusupati, A. Nagrani, S. Buch, P. Jain, A. Arnab, and S. Paul Mixture of nested experts: adaptive processing of visual tokens . Advances in Neural Information Processing Systems 37 , pp. 58480–58497 . Cited by: Appendix A .

Kadlčík et al. (2023) M. Kadlčík, M. Štefánik, O. Sotolár, and V. Martinek Calc-x and calcformers: empowering arithmetical chain-of-thought through interaction with symbolic systems . In Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing , pp. 12101–12108 . Cited by: §4.1 .

Li et al. (2025) Z. Li, Y. Li, and T. Zhou Skip a layer or loop it? test-time depth adaptation of pretrained llms . arXiv preprint arXiv:2507.07996 . Cited by: §1 , §5 .

Liu et al. (2020) W. Liu, P. Zhou, Z. Wang, Z. Zhao, H. Deng, and Q. Ju Fastbert: a self-distilling bert with adaptive inference time . In Proceedings of the 58th annual meeting of the association for computational linguistics , pp. 6035–6044 . Cited by: Appendix A , §1 , §1 , §5 .

Liu et al. (2021a) Y. Liu, F. Meng, J. Zhou, Y. Chen, and J. Xu Faster depth-adaptive transformers . In Proceedings of the AAAI Conference on Artificial Intelligence , Vol. 35 , pp. 13424–13432 . Cited by: Appendix A , §1 , §5 .

Liu et al. (2021b) Z. Liu, F. Li, G. Li, and J. Cheng EBERT: efficient bert inference with dynamic structured pruning . In Findings of the Association for Computational Linguistics: ACL-IJCNLP 2021 , pp. 4814–4823 . Cited by: Appendix A .

Luo et al. (2025) X. Luo, W. Wang, and X. Yan Adaptive layer-skipping in pre-trained llms . arXiv preprint arXiv:2503.23798 . Cited by: §4.1 , §5 .

Men et al. (2025) X. Men, M. Xu, Q. Zhang, Q. Yuan, B. Wang, H. Lin, Y. Lu, X. Han, and W. Chen Shortgpt: layers in large language models are more redundant than you expect . In Findings of the Association for Computational Linguistics: ACL 2025 , pp. 20192–20204 . Cited by: §4.1 , §5 .

Miao et al. (2020) S. Miao, C. Liang, and K. Su A diverse corpus for evaluating and developing english math word problem solvers . In Proceedings of the 58th annual meeting of the Association for Computational Linguistics , pp. 975–984 . Cited by: §4.1 .

Raposo et al. (2024) D. Raposo, S. Ritter, B. Richards, T. Lillicrap, P. C. Humphreys, and A. Santoro Mixture-of-depths: dynamically allocating compute in transformer-based language models . arXiv preprint arXiv:2404.02258 . Cited by: §4.1 .

Tang et al. (2023) S. Tang, Y. Wang, Z. Kong, T. Zhang, Y. Li, C. Ding, Y. Wang, Y. Liang, and D. Xu You need multiple exiting: dynamic early exiting for accelerating unified vision language model . In Proceedings of the IEEE/CVF conference on computer vision and pattern recognition , pp. 10781–10791 . Cited by: Appendix A .

Tong et al. (2024) Y. Tong, X. Zhang, R. Wang, R. Wu, and J. He Dart-math: difficulty-aware rejection tuning for mathematical problem-solving . Advances in Neural Information Processing Systems 37 , pp. 7821–7846 . Cited by: §2 , §4.1 .

Wang et al. (2024) Y. Wang, X. Ma, G. Zhang, Y. Ni, A. Chandra, S. Guo, W. Ren, A. Arulraj, X. He, Z. Jiang, et al. Mmlu-pro: a more robust and challenging multi-task language understanding benchmark . Advances in Neural Information Processing Systems 37 , pp. 95266–95290 . Cited by: §4.1 .

Wu et al. (2024) Q. Wu, Z. Ke, Y. Zhou, X. Sun, and R. Ji Routing experts: learning to route dynamic experts in multi-modal large language models . arXiv preprint arXiv:2407.14093 . Cited by: Appendix A .

Xin et al. (2020) J. Xin, R. Tang, J. Lee, Y. Yu, and J. Lin DeeBERT: dynamic early exiting for accelerating bert inference . arXiv preprint arXiv:2004.12993 . Cited by: Appendix A , §1 , §1 , §5 .

Xu et al. (2023) G. Xu, J. Hao, L. Shen, H. Hu, Y. Luo, H. Lin, and J. Shen Lgvit: dynamic early exiting for accelerating vision transformer . In Proceedings of the 31st ACM International Conference on Multimedia , pp. 9103–9114 . Cited by: Appendix A .

Yang et al. (2023) L. Yang, K. Lee, R. Nowak, and D. Papailiopoulos Looped transformers are better at learning learning algorithms . arXiv preprint arXiv:2311.12424 . Cited by: Appendix A , §1 , §5 .

Yang et al. (2024) Y. Yang, Z. Cao, and H. Zhao Laco: large language model pruning via layer collapse . arXiv preprint arXiv:2402.11187 . Cited by: §4.1 , §5 .

Zhou et al. (2020) W. Zhou, C. Xu, T. Ge, J. McAuley, K. Xu, and F. Wei Bert loses patience: fast and robust inference with early exit . Advances in Neural Information Processing Systems 33 , pp. 18330–18341 . Cited by: Appendix A , §1 , §1 , §5 .

## Appendix A Related Work

#### Layer Pruning and Early-Exit Neural Networks

Many works aim to accelerate large Transformers by statically pruning weights or dynamically halting computation. Static pruning typically removes redundant neurons, heads, or layers after training. For example, Liu et al. (2021b) demonstrate that a significant fraction of BERT’s attention heads can be dropped with negligible performance loss, and Gordon et al. (2020) investigate fine-grained weight pruning in BERT. ( Fan et al., 2019 ) introduce LayerDrop, a structured dropout technique that effectively trains models so arbitrary subsets of layers can be skipped during inference without requiring fine-tuning. These methods produce smaller models that trade computation for a small accuracy loss.

By contrast, early-exit or input-adaptive methods add auxiliary classifiers at intermediate layers so that ”easy” inputs exit early. Notable examples include FastBERT ( Liu et al., 2020 ) and DeeBERT ( Xin et al., 2020 ) , which insert classifiers after each block and use confidence or entropy metrics to decide when to stop. PABEE ( Zhou et al., 2020 ) employs a patience criterion to halt when predictions stabilize. DACT-BERT ( Eyzaguirre et al., 2022 ) adopts a differentiable Adaptive Computation Time mechanism to learn how many Transformer layers to run for each example. Liu et al. (2021a) estimate input ”hardness” via mutual information or reconstruction error to pre-determine the number of Transformer layers to use.

These early-exit networks achieve significant speedups on NLP tasks by adaptively reducing depth per input. More recently, early-exit ideas have been extended to vision and multimodal Transformers. Xu et al. (2023) propose LGViT, which adds heterogeneous exit heads (local and global) to ViT so that vision transformers can terminate early with minimal feature loss. Tang et al. (2023) introduce MuE (“Multiple Exiting”), a strategy for unified vision-language models that dynamically skips layers in both encoder and decoder based on input similarity. These works demonstrate that later layers can be skipped to allow image and vision-language models to adapt computation per sample with minimal accuracy drop. Our work generalizes this approach by allowing skipping of arbitrary layers and enabling reuse of certain layers.

#### Looped Transformer and Recurrent Depth

Another line of research makes Transformer depth adaptive by looping or repeating layers. The Universal Transformer ( Dehghani et al., 2018 ) was an early example: it applies the same self-attention block recurrently and uses a halting mechanism to determine when each position is “done” (adapting depth per token). Building on these ideas, recent work explicitly introduces loops in model architectures. Fan et al. (2024) demonstrate that a Looped Transformer – a single Transformer block applied repeatedly – can achieve much better length generalization on algorithmic tasks by adjusting the number of loops during inference. Similarly, Yang et al. (2023) note that looped architectures excel at learning algorithms by explicitly incorporating iterative characteristics into the transformer architecture. More sophisticated variants like the Inner Thinking Transformer Chen et al. (2025) interleave adaptive loops with residual “thinking” connections and per-token routing, enabling the model to devote extra computation only to particularly difficult tokens. In summary, these approaches explore recurrent or elastic depth via explicit loops to tailor the number of applied layers to each input’s complexity. Unlike our approach, they require special architecture design and training from scratch, whereas our work focuses on pure test-time adaptation.

#### Dynamic Routing and Modular Inference

A third theme treats networks as collections of modules or experts with dynamically chosen pathways per sample. Mixture-of-Experts (MoE) Transformer layers are a well-known example: they maintain multiple sub-networks (“experts”) and route each token to a subset. Wu et al. (2024) introduce Routing Experts (RoE) for multimodal LLMs, retrofitting trained models into a mixture-of-experts style by learning input-dependent shortcut routes through layers, guided by sparsity regularizers. Jain et al. (2024) present Mixture of Nested Experts (MoNE): experts organized in a hierarchy of increasing capacity, where tokens are sent to smaller experts when sufficient. MoNE learns to prioritize easy tokens through low-cost experts and reserve full models for hard cases, halving inference compute on ImageNet/Video tasks.

These methods exemplify sample-wise routing: at inference time, the model conditionally activates different sub-modules or experts for each input. Similarly, neural module networks ( Andreas et al., 2016 ) assemble task-specific computation graphs from a library of modules. In modern LLMs/VLMs, these routing approaches – whether through gating experts, skipping layers, or assembling modules – form a spectrum of modular inference techniques that adapt the computation graph on a per-sample basis to balance cost and accuracy. Interestingly, our work suggests that transformer layers can function effectively as modules even without being specifically trained for that purpose.

## Appendix B Searching the Execution Program Space

This appendix provides full details of the execution-program search procedure used to test the conjecture in Section 2 . The search is used purely as a diagnostic tool to study the existence and structure of valid execution programs, rather than as a practical inference-time method.

### B.1 Execution Program Space

We follow the formalization in the main text and represent inference as the execution of a variable-length program that composes pretrained transformer layers. Consider a pretrained LLM with D D transformer layers, where each layer defines a fixed computation function f i : ℝ T × d → ℝ T × d , i ∈ { 0 , … , D − 1 } . f_{i}:\mathbb{R}^{T\times d}\rightarrow\mathbb{R}^{T\times d},\quad i\in\{0,\ldots,D-1\}. An execution program is defined as a finite sequence of layer indices π = ( i 1 , i 2 , … , i K ) , i k ∈ { 0 , … , D − 1 } , \pi=(i_{1},i_{2},\ldots,i_{K}),\quad i_{k}\in\{0,\ldots,D-1\}, which induces the composed computation F π = f i K ∘ ⋯ ∘ f i 1 . F_{\pi}=f_{i_{K}}\circ\cdots\circ f_{i_{1}}. Executing a program applies this composition to the input representation and produces a prediction. A program is considered valid for a given input if it yields a correct prediction.

Programs may be shorter than the standard forward pass through layer skipping, or longer through layer repetition. Increasing program length corresponds to increasing the number of latent reasoning steps.

### B.2 Search Space Constraints

The unconstrained space of programs grows exponentially with program length. To make search tractable while preserving expressiveness, we restrict the action space to structured operations on contiguous subsequences of layer indices. Specifically, we allow two classes of actions: • Skip : remove a contiguous block of k k indices from the program;

• Repeat : duplicate a contiguous block of k k indices for r r repetitions.

In all experiments, block size k k and repetition count r r are bounded by small constants ( k , r ≤ 4 k,r\leq 4 ). These constraints significantly reduce the branching factor while retaining the ability to realize layer skipping, recurrence, and emergent reordering patterns.

### B.3 Monte Carlo Tree Search Formulation

We formulate program discovery as a sequential decision process and employ Monte Carlo Tree Search (MCTS) to explore the constrained program space.

#### State and Actions.

Each MCTS node corresponds to a partial or complete execution program π \pi . Actions modify the current program by applying a valid skip or repeat operation, yielding a new program.

#### Reward.

For a completed program π \pi and input x x with ground-truth answer y y , we define a binary reward r ( π , x ) = 𝟏 { F π ( x ) = y } , r(\pi,x)=\mathbf{1}\{F_{\pi}(x)=y\}, where F π ​ ( x ) F_{\pi}(x) denotes executing the composed computation induced by π \pi .

#### Tree Policy.

Tree traversal is guided by a UCB-style objective that balances exploitation, exploration, and program length regularization: UCB ⁡ ( π ) = R ⁡ ( π ) v ⁡ ( π ) + c ​ ln ⁡ V v ⁡ ( π ) − λ ​ | π | D , \mathrm{UCB}(\pi)=\frac{R(\pi)}{v(\pi)}+c\sqrt{\frac{\ln V}{v(\pi)}}-\lambda\frac{|\pi|}{D}, where R ⁡ ( π ) R(\pi) is the cumulative reward, v ⁡ ( π ) v(\pi) is the visit count, V V is the total number of simulations, and λ \lambda penalizes long programs to encourage efficiency.

### B.4 Search Algorithm

Algorithm 1 summarizes the MCTS procedure. We initialize the root node with the standard forward execution π 0 = ( 0 , 1 , … , D − 1 ) \pi_{0}=(0,1,\ldots,D-1) and iteratively perform selection, expansion, simulation, and backpropagation. After a fixed number of simulations, we collect all explored programs with nonzero visit counts and analyze their validity and structural properties.

## Appendix C Experimental Results

This appendix provides additional experimental results that complement the main paper. We report full quantitative comparisons for both in-distribution and out-of-distribution evaluations across multiple pretrained LLMs. Unless otherwise stated, all models are evaluated in a fully frozen setting, and PoLar only predicts execution programs at inference time.

### C.1 In-Distribution Performance

We first report detailed in-distribution results on DART-Math, a structured mathematical reasoning benchmark with five difficulty levels (DM-1 to DM-5). Tables 5 , 6 , and 7 present pass@k accuracy under different inference strategies for Qwen1.5-MoE-A2.7B-Chat, Qwen2.5-3B-Instruct, and Qwen3-8B, respectively.

Across all models and difficulty levels, PoLar achieves strong in-distribution performance and generally outperforms standard inference and prior dynamic-depth baselines. In particular, increasing p ​ @ ​ k p@k leads to monotonic accuracy improvements for PoLar , demonstrating effective test-time computation scaling through execution-program exploration. At p ​ @ ​ 5 p@5 , PoLar achieves substantial absolute gains over Base (sampling), with improvements of +15.6 / +17.5 / +15.0 / +10.1 / +12.2 on Qwen1.5-MoE-A2.7B-Chat, +40.4 / +19.2 / +17.5 / +14.8 / +13.5 on Qwen2.5-3B-Instruct, and +14.1 / +23.4 / +15.5 / +10.6 / +9.9 on Qwen3-8B for DM-1 to DM-5, respectively.

Notably, methods that rely solely on layer skipping (e.g., ShortGPT, MindSkip, FlexiDepth) often suffer accuracy degradation, especially on harder difficulty levels. In contrast, PoLar jointly supports layer skipping and recurrence, allowing it to retain or improve accuracy while exploring diverse execution programs. Compared to DR.LLM, which performs layer-level routing, PoLar achieves stronger performance in most settings, particularly at larger p ​ @ ​ k p@k , indicating the benefit of structured, program-level execution prediction.

### C.2 Out-of-Distribution Generalization

We further evaluate the out-of-distribution (OOD) generalization of PoLar on benchmarks that differ substantially from DART-Math in both format and domain. Tables 8 , 9 , and 10 report pass@1 accuracy on ASDiv, MAWPS, and subject-wise subsets of MMLU-Pro using LLaMA-3.2-3B-Instruct, Qwen2.5-3B-Instruct, and Qwen3-8B, respectively.

Across all evaluated models, PoLar consistently improves over standard inference on arithmetic word problem benchmarks (ASDiv and MAWPS), indicating strong transfer from structured mathematical reasoning to natural language problem settings. On MMLU-Pro, which spans diverse domains including mathematics, natural sciences, social sciences, and humanities, PoLar achieves broad and consistent gains across most subject areas.

These results suggest that the execution programs learned by PoLar capture general, transferable computation control strategies rather than dataset-specific heuristics. Despite being trained on mathematical reasoning data, PoLar generalizes effectively to heterogeneous domains, highlighting the robustness of program-of-layers inference and its applicability beyond the original training distribution.

## Appendix D Empirical Details

### D.1 Dataset Details

All in-distribution experiments are conducted on DART-Math , a structured mathematical reasoning benchmark consisting of five difficulty levels, denoted as DM-1 to DM-5 .

We construct the in-distribution data from the DART-Math MATH pool. Since the released pool may contain multiple response records associated with the same underlying question, we deduplicate examples within each difficulty level by question text before splitting. We then adopt a difficulty-wise data split, where each difficulty level is split independently into training, validation, and test sets.

After deduplication, the five difficulty levels contain 565, 1,349, 1,579, 1,537, and 1,577 examples for DM-1 to DM-5, respectively. For each difficulty level, we use approximately 62.5% of the examples for training, 12.5% for validation, and 25% for testing.

Overall, this results in 4,130 training examples, 826 validation examples, and 1,651 test examples. All in-distribution results are reported on the held-out test sets corresponding to the same difficulty level used for training.

#### Revision note.

This arXiv version updates the DART-Math in-distribution evaluation protocol by removing duplicate questions prior to data splitting. We have rerun the affected in-distribution analyses, and the qualitative conclusions remain unchanged. The out-of-distribution (OOD) results are unaffected.

### D.2 Training Configuration

We train the PoLar prediction network using supervised learning on the training splits described above. All hyperparameters are selected via validation tuning.

#### Optimization.

We use the AdamW optimizer and tune the learning rate from {1e-4, 3e-4, 5e-4, 8e-4, 1e-3, 3e-3}, the batch size from {32, 128, 256}, and the number of training epochs from {3, 10} based on validation performance. We adopt a cosine learning rate schedule with linear warmup, and tune the number of warmup steps on the validation split together with the other hyperparameters.

### D.3 Predictor Size

The learned PoLar predictor is lightweight compared with the frozen base LLM. Across the evaluated models, the predictor contains approximately 2.1M parameters, corresponding to only 0.01%–0.06% of the base model size. This small footprint makes training and inference inexpensive relative to standard LLM fine-tuning or full-model execution.

### D.4 Direct Prompting

We adopt a direct prompting strategy throughout all experiments, without eliciting chain-of-thought or intermediate reasoning. The model is explicitly instructed to output only the final answer in a strictly formatted form.

Given a math problem instance question , the input prompt is constructed as follows: Solve the following math problem and output ONLY the final answer directly, formatted strictly as \boxed{ANSWER}. ### Problem Start {question} ### Problem End Answer:

This prompt design enforces concise answer generation and isolates the effect of latent execution programs from token-level reasoning strategies.

## Instructions for reporting errors

We are continuing to improve HTML versions of papers, and your feedback helps enhance accessibility and mobile support. To report errors in the HTML that will help us improve conversion and rendering, choose any of the methods listed below:

Click the "Report Issue" ( ) button, located in the page header.

Tip: You can select the relevant text first, to include it in your report.

Our team has already identified the following issues . We appreciate your time reviewing and reporting rendering errors we may not have found yet. Your efforts will help us improve the HTML versions for all readers, because disability should not be a barrier to accessing research. Thank you for your continued support in championing open access for all.

Have a free development cycle? Help support accessibility at arXiv! Our collaborators at LaTeXML maintain a list of packages that need conversion , and welcome developer contributions .
