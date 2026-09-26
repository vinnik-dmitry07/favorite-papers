##### Report GitHub Issue

Content selection saved. Describe the issue below:

# Universal Reasoning Model

###### Abstract

Universal transformers (UTs) have been widely used for complex reasoning tasks such as ARC-AGI and Sudoku, yet the specific sources of their performance gains remain underexplored. In this work, we systematically analyze UTs variants and show that improvements on ARC-AGI primarily arise from the recurrent inductive bias and strong nonlinear components of Transformer, rather than from elaborate architectural designs. Motivated by this finding, we propose the Universal Reasoning Model (URM), which enhances the UT with short convolution and truncated backpropagation. Our approach substantially improves reasoning performance, achieving state-of-the-art ∗ 53.8% pass@1 on ARC-AGI 1 and 16.0% pass@1 on ARC-AGI 2. 0 0 footnotetext: ∗ This comparison focuses on pass@1 score of single small models trained from scratch under the same data setting as HRM and TRM, excluding test-time scaling, ensembling, and visual methods such as VARC [ 10 ] . Our code is avaliable at https://github.com/UbiquantAI/URM .

## 1 Introduction

Recent advances in recurrent models [ 20 , 7 , 11 ] have demonstrated the effectiveness of Universal Transformers (UTs) [ 5 ] in addressing complex reasoning tasks, such as ARC-AGI and Sudoku [ 3 , 2 ] . UT-based small models, despite being trained from scratch on these tasks without internet-scale pre-training, consistently outperform most standard Transformer-based Large Language models (LLMs) by a significant margin [ 20 ] .

While this contrast highlights the potential of UTs for depth-intensive iterative reasoning, the function and impact of gating mechanisms remain insufficiently explored beyond their initial intuition

Prior studies often attribute improvements to high-level architectural innovations [ 20 , 7 , 11 ] , yet our analysis reveals that the core performance gain actually arises from the often-overlooked recurrent inductive bias intrinsic to the Universal Transformer. In particular, nonlinear depth-wise computation plays a much larger role than previously acknowledged, suggesting that architectural modifications that enhance recurrent processing can yield substantial downstream improvements. Motivated by this insight, we further investigate and strengthen this inductive bias via a simplified yet effective enhancement to the UT framework, enabling stronger abstraction capabilities while preserving parameter efficiency.

Our main contributions are as follows: • Through extensive ablation studies, we show that the performance of models on ARC-AGI–style complex reasoning tasks primarily stems from their nonlinearity. Moreover, we reveal that the true source of reasoning capability beyond standard Transformers comes from the recurrent mechanism of Universal Transformers rather than overly elaborate design in prior work.

• By introducing short convolutions and truncated backpropagation into the Universal Transformer, we achieve a state-of-the-art 53.8% pass@1 accuracy on ARC-AGI 1 and 16.0% on ARC-AGI 2.

## 2 Preliminaries

### 2.1 Standard Transformer

Let 𝒱 \mathcal{V} denote the vocabulary of size V V , and let 𝐱 = ( x 1 , … , x N ) ∈ 𝒱 N \mathbf{x}=(x_{1},\dots,x_{N})\in\mathcal{V}^{N} be an input sequence of length N N . We define the token embedding function as ϕ : 𝒱 N → ℝ N × d \phi:\mathcal{V}^{N}\to\mathbb{R}^{N\times d} , mapping discrete tokens to a d d -dimensional continuous representation. Conversely, the unembedding function (or language modeling head) is denoted by ψ : ℝ N × d → ℝ N × V \psi:\mathbb{R}^{N\times d}\to\mathbb{R}^{N\times V} , which projects hidden states back to the vocabulary logit space.

A single Transformer layer, parameterized by θ \theta , is defined as a function 𝒯 θ : ℝ N × d → ℝ N × d \mathcal{T}_{\theta}:\mathbb{R}^{N\times d}\to\mathbb{R}^{N\times d} . This function typically composes a Multi-Head Self-Attention (MHSA) module and a Position-wise Feed-Forward Network (FFN), each wrapped with residual connections and layer normalization:

𝒯 θ ​ ( H ) = FFN ​ ( LN ​ ( H ′ + H ) ) , where ​ H ′ = MHSA ​ ( LN ​ ( H ) ) \begin{split}\mathcal{T}_{\theta}(H)&=\text{FFN}(\text{LN}(H^{\prime}+H)),\\ \text{where }H^{\prime}&=\text{MHSA}(\text{LN}(H))\end{split}

A standard, non-recursive Transformer model ℳ std \mathcal{M}_{\text{std}} of depth L L is constructed by stacking L L layers with distinct parameters Θ = { θ 1 , … , θ L } \Theta=\{\theta_{1},\dots,\theta_{L}\} . The forward pass is the composition of these layers:

ℳ std ​ ( 𝐱 ) = ψ ∘ 𝒯 θ L ∘ ⋯ ∘ 𝒯 θ 1 ∘ ϕ ⁡ ( 𝐱 ) \mathcal{M}_{\text{std}}(\mathbf{x})=\psi\circ\mathcal{T}_{\theta_{L}}\circ\dots\circ\mathcal{T}_{\theta_{1}}\circ\phi(\mathbf{x})

Here, the operator ∘ \circ denotes function composition. The computational cost and parameter count both scale linearly with L L , creating a rigid coupling between model capacity and inference compute.

### 2.2 Universal Transformer

The Universal Transformer (UT) [ 5 ] extends the standard Transformer [ 18 ] by introducing recurrent computation over depth . Instead of stacking L L distinct layers, the UT applies a single transition block repeatedly to refine token representations. For an input sequence 𝐱 \mathbf{x} with embedding matrix 𝐇 0 ∈ ℝ n × d \mathbf{H}^{0}\in\mathbb{R}^{n\times d} , the UT updates states as

𝐇 t + 1 = LayerNorm ⁡ ( 𝐇 t + MHA ⁡ ( 𝐇 t ) ) , \mathbf{H}^{t+1}=\mathrm{LayerNorm}\!\left(\mathbf{H}^{t}+\mathrm{MHA}\!\left(\mathbf{H}^{t}\right)\right),

followed by a shared position-wise transition function

𝐇 t + 1 ← LayerNorm ( 𝐇 t + 1 + Transition ( 𝐇 t + 1 ) ) , t = 0 , … , T − 1 , \mathbf{H}^{t+1}\leftarrow\mathrm{LayerNorm}\!\left(\mathbf{H}^{t+1}+\mathrm{Transition}\!\left(\mathbf{H}^{t+1}\right)\right),\qquad t=0,\dots,T-1,

where Transition \mathrm{Transition} is either a feed-forward network or separable convolution. To encode both position and refinement depth, UT adds 2-D sinusoidal embeddings at each step.

#### 2.2.1 Parameter Sharing

A key design of UT is weight tying across depth. The attention and transition parameters

Θ UT = { 𝐖 h Q , 𝐖 h K , 𝐖 h V , 𝐖 O , Θ Transition } \Theta_{\mathrm{UT}}=\{\mathbf{W}_{h}^{Q},\mathbf{W}_{h}^{K},\mathbf{W}_{h}^{V},\mathbf{W}^{O},\Theta_{\mathrm{Transition}}\}

are reused for all t t . Thus, the model performs iterative representation refinement with a flexible number of steps T T , enabling (i) depth adaptation at inference and (ii) higher theoretical expressivity than fixed-depth Transformers.

#### 2.2.2 Adaptive Computation Time (ACT)

With ACT [ 9 ] , different tokens may halt at different recurrent steps. At step t t , each position predicts a halting probability

p t , i = σ ⁡ ( 𝐰 ⊤ ​ 𝐡 t , i + b ) , p_{t,i}=\sigma(\mathbf{w}^{\top}\mathbf{h}_{t,i}+b),

accumulated until reaching threshold 1 − ϵ 1-\epsilon . The final token representation is a weighted mixture

𝐡 i final = ∑ t Δ t , i ​ 𝐡 t , i , \mathbf{h}^{\mathrm{final}}_{i}=\sum_{t}\Delta_{t,i}\,\mathbf{h}_{t,i},

where Δ t , i \Delta_{t,i} is the truncated allocation. ACT allows UT to allocate more computation to complex tokens and less to simpler ones.

## 3 Universal Reasoning Model

The base architecture of our Universal Reasoning Model (URM) closely follows that of the Universal Transformer [ 5 ] , with the difference being its decoder-only design. This aspect is consistent with previous works such as HRM [ 20 ] and TRM [ 11 ] . Our work differs from previous models [ 20 , 11 ] by introducing the following ConvSwiGLU module and a Truncated Backpropagation Through Loops mechanism.

### 3.1 ConvSwiGLU

To strengthen the non-linearity of Universal Transformer, we introduce a ConvSwiGLU (motivation see Section 4.6 ), which augments the standard SwiGLU feed-forward block with a depthwise short convolution. Unlike the conventional point-wise SwiGLU [ 16 ] , which treats each token independently, our design explicitly injects local contextual interactions into the gating mechanism, introducing lightweight channel mixing in token space without increasing sequence-level complexity [ 1 , 22 ] .

Given an input sequence X ∈ ℝ T × d X\in\mathbb{R}^{T\times d} , we first project it into an expanded intermediate representation:

[ 𝐆 , 𝐔 ] = X ​ W up ∈ ℝ T × 2 ​ m . [\mathbf{G},\mathbf{U}]=XW_{\text{up}}\in\mathbb{R}^{T\times 2m}.

The SwiGLU activation produces a gated representation:

𝐇 ffn = SiLU ​ ( 𝐆 ) ⊙ 𝐔 . \mathbf{H}_{\text{ffn}}=\text{SiLU}(\mathbf{G})\odot\mathbf{U}.

To integrate short-range token interactions, we apply a depthwise 1D convolution over the gated features:

𝐇 conv = σ ⁡ ( 𝐖 dwconv ∗ 𝐇 ffn ) , \mathbf{H}_{\text{conv}}=\sigma\bigl(\mathbf{W}_{\text{dwconv}}*\mathbf{H}_{\text{ffn}}\bigr),

where 𝐖 dwconv ∈ ℝ m × 1 × k \mathbf{W}_{\text{dwconv}}\in\mathbb{R}^{m\times 1\times k} is a depthwise convolution kernel of size k = 2 k=2 .

Finally, the output is projected back to the hidden dimension:

𝐘 = [ σ ⁡ ( 𝐖 dwconv ∗ ( SiLU ​ ( 𝐆 ) ⊙ 𝐔 ) ) ] ​ W down . \boxed{\mathbf{Y}=\bigl[\sigma(\mathbf{W}_{\text{dwconv}}*(\text{SiLU}(\mathbf{G})\odot\mathbf{U}))\bigr]W_{\text{down}}.}

### 3.2 Truncated Backpropagation Through Loops

When the number of recurrent reasoning loops becomes large, the gradients propagated from early loops may hinder optimization due to noise accumulation and instability (see empirical evidence in Section 4.5 ). To alleviate this issue, we employ Truncated Backpropagation Through Loops (TBPTL) and only compute gradients for the later loops.

Consider a D D -layer Universal Reasoning Model unrolled for M M iterative loops during training. Let 𝐡 t ( d ) \mathbf{h}_{t}^{(d)} denote the hidden representation of layer d ∈ { 1 , … , D } d\in\{1,\ldots,D\} at iteration t ∈ { 1 , … , M } t\in\{1,\ldots,M\} . The recurrent transition is defined as:

𝐡 t ( d ) = F θ ( d ) ​ ( 𝐡 t ( d − 1 ) , 𝐡 t − 1 ( d ) ) , \mathbf{h}_{t}^{(d)}=F_{\theta}^{(d)}\big(\mathbf{h}_{t}^{(d-1)},\mathbf{h}_{t-1}^{(d)}\big),

where F θ ( d ) F_{\theta}^{(d)} denotes the parameterized transformation at layer d d with trainable parameters θ \theta .

Instead of backpropagating through all M M loops, we partition the rollout into forward-only and trainable segments. Specifically, for a truncation index N < M N<M : { 1 , 2 , … , N } ⏟ no backward pass , { N + 1 , … , M } ⏟ forward + backward . \underbrace{\{1,2,\ldots,N\}}_{\text{no backward pass}},\qquad\underbrace{\{N+1,\ldots,M\}}_{\text{forward + backward}}. During training, we compute gradients only on the loss accumulated in the latter ( M − N ) (M-N) loops: ℒ TBPTL ​ ( θ ) = ∑ t = N + 1 M ℒ ⁡ ( 𝐡 t ( D ) , y ) , \mathcal{L}_{\text{TBPTL}}(\theta)=\sum_{t=N+1}^{M}\mathcal{L}\big(\mathbf{h}_{t}^{(D)},y\big), where ℒ ⁡ ( ⋅ ) \mathcal{L}(\cdot) is cross-entropy loss function. The gradients with respect to θ \theta are thus: ∇ θ ℒ TBPTL = ∑ t = N + 1 M ∂ ℒ ∂ 𝐡 t ( D ) ​ ∂ 𝐡 t ( D ) ∂ θ . \nabla_{\theta}\mathcal{L}_{\text{TBPTL}}=\sum_{t=N+1}^{M}\frac{\partial\mathcal{L}}{\partial\mathbf{h}_{t}^{(D)}}\frac{\partial\mathbf{h}_{t}^{(D)}}{\partial\theta}.

## 4 Experiment

### 4.1 Experiment Settings

Our experimental setup largely follows HRM and TRM [ 20 , 11 ] . We use the same datasets and augmented data as in prior work, and apply an exponential moving average (EMA) to model parameters to improve training stability, following [ 11 ] . All models are trained with the AdamAtan2 optimizer [ 6 ] . For ARC-AGI 1 and ARC-AGI 2, the main model learning rates are set to 1 × 10 − 4 1\times 10^{-4} and 3 × 10 − 4 3\times 10^{-4} , respectively, while the puzzle embedding uses a learning rate of 1 × 10 − 2 1\times 10^{-2} ; for Sudoku, the puzzle embedding learning rate is 1 × 10 − 4 1\times 10^{-4} . Weight decay is set to 0.1 for both the main model and puzzle embedding on ARC-AGI 1 and ARC-AGI 2, and to 1.0 for Sudoku, consistent with prior work. The model has 4 layers with hidden size 512 and 8 attention heads. The inner loop runs for 8 steps, with the first two steps being forward-only, while the outer loop employs Adaptive Computation Time (ACT) [ 9 ] with a maximum of 16 steps.

### 4.2 Main Results

As shown in Table 1, the Universal Reasoning Model (URM) achieves substantial improvements over prior UT-based approaches across all benchmarks. On ARC-AGI 1, URM reaches 53.8% pass@1, outperforming TRM (40.0%) and HRM (34.4%) by large margins. On ARC-AGI 2, URM obtains 16.0% pass@1, nearly tripling HRM and more than doubling TRM. A similar advantage appears on Sudoku, where URM achieves 77.6% accuracy, surpassing both TRM and HRM.

Notably, URM’s gains further widen under larger sampling budgets (e.g., pass@1000), indicating that iterative refinement enables richer candidate generation rather than brittle one-step predictions.

### 4.3 Why Universal Transformer?

Table 2 demonstrates that the performance gains of Universal Transformers (UTs) on ARC-AGI 1 arise from substantially higher parameter efficiency rather than increased model scale or computational budget. With only 4× parameters, a UT achieves a pass@1 score of 40.0, dramatically outperforming vanilla Transformers that employ up to 32× more parameters yet remain markedly weaker. Simply scaling depth or width in vanilla Transformers yields diminishing returns and can even lead to performance degradation, highlighting a fundamental inefficiency in how parameters are used to support multi-step reasoning.

Crucially, this advantage persists even when computation is held constant. At 32× FLOPs, reallocating computation from deep, non-shared layers to recurrent refinement improves pass@1 from 23.75 for vanilla Transformers to 40.0 for UTs. This behavior is consistent with analyses of previous works [ 15 ] , which argue that many reasoning tasks benefit more from iterative computation than from increasing the number of independent layers. In standard Transformers, additional FLOPs are often spent on redundant refinement in higher layers, whereas recurrent computation converts the same budget into increased effective depth [ 23 , 15 ] .

This superior efficiency is driven by the recurrent inductive bias introduced by parameter sharing across depth. Through repeated application of a shared transformation, UTs realize iterative refinement that better aligns with the structure of algorithmic reasoning, while avoiding any increase in parameter count. Consequently, under both fixed parameter and fixed FLOPs budgets, UTs consistently outperform vanilla Transformers on reasoning tasks, making them particularly well suited for reasoning-intensive settings such as ARC-AGI, where multi-step abstraction is more critical than sheer scale.

### 4.4 Short Convolution

To strengthen the nonlinear inductive bias of the Universal Transformer, we introduce a depthwise short convolution module parameterized by W dwconv W_{\mathrm{dwconv}} (see Section 3.1 for details), which provides token-local mixing while preserving the per-step computational budget. Since ARC-AGI performance correlates strongly with nonlinear capacity (Section 4.6 ), we evaluate how inserting this module at different locations affects the recurrent transition.

We examine six insertion points: (a) after the SDPA output; (b) after the value projection; (c) after the key projection; (d) after the query projection; (e) between multi-head concatenation and the output projection; and (f) after the MLP expansion.

As shown in Figure 3 , inserting the W dwconv W_{\mathrm{dwconv}} module inside the attention pathway, positions (a)–(d), does not yield improvements and often degrades performance, suggesting that local perturbations interfere with the geometric structure of attention’s linear projections. A mild gain appears at position (e), where the perturbation acts only on aggregated multi-head features.

The dominant effect arises at position (f), after the MLP expansion, indicating that short-range mixing is most beneficial when applied within an already nonlinear subspace. This supports a functional interpretation in which the MLP—not attention—constitutes the model’s primary source of expressive nonlinearity; augmenting it with W dwconv W_{\mathrm{dwconv}} substantially enhances the model’s nonlinear representational capacity.

As shown in Fig. 4 , the incorporation of short convolution into the MLP significantly enhances channel mixing. While the standard Universal Transformer exhibits relatively sparse and homogeneous attention patterns, the model with ConvSwiGLU produces attention matrices with more diverse and structured distributions. This suggests that short convolution facilitates more effective inter-channel information flow, thereby improving the expressiveness of the attention mechanism.

### 4.5 Truncated Backpropagation Through Loops

As shown in Table 5 , when the total number of inner loops is fixed to 8, truncating gradients for the first two loops—i.e., running the initial two inner-loop iterations in forward-only mode—achieves the best performance. Both pass@1 and pass@1000 peak at this truncation setting, while shorter or longer truncation horizons result in inferior outcomes.

This trend closely resembles truncated backpropagation through time (TBPTT) in recurrent neural networks, where the underlying motivation is largely the same. In full backpropagation through time, gradients are propagated through the entire sequence, which incurs high computational and memory costs and often yields ineffective long-range gradients due to vanishing or exploding behaviors. As a result, practical implementations typically restrict gradient propagation to a fixed recent window, e.g., by backpropagating errors only through the last L L time steps and updating the network parameters accordingly [ 14 , 17 ] .

Similarly, in universal transformers, propagating gradients across all inner-loop iterations can lead to unstable optimization, while overly aggressive truncation limits the model’s ability to coordinate multi-step refinement. Moderately truncating gradient propagation therefore provides a favorable balance between optimization stability and effective long-horizon learning.

We note that all results in this experiment are obtained using a two-layer URM without the short convolution module, which differs from the full URM model reported earlier.

### 4.6 Nonlinearity of Transformers

As shown in Table 4 , the performance on ARC-AGI 1 decreases monotonically as nonlinear components are progressively removed from the model. Among these components, the activation function in the MLP plays a particularly critical role: replacing SwiGLU with simpler nonlinearities such as SiLU or ReLU leads to substantial degradation, while completely removing the attention softmax results in a dramatic collapse in performance. This clear monotonic trend highlights the importance of strong nonlinear transformations for solving complex abstract reasoning tasks.

These results suggest that the expressive power required for ARC-AGI primarily arises from rich nonlinear mappings. Weakening the nonlinearity may systematically limits the model’s ability to represent complex reasoning skills.

We note that the model still retains certain forms of nonlinearity that are not ablated in this study, such as the RMSNorm applied after each layer and the dot-product interaction between queries and keys in attention. However, these components are either difficult to remove without causing training instability or represent relatively weak nonlinear effects compared to explicit activation functions. As ablating them typically leads to training failure, they fall outside the scope of the present analysis.

### 4.7 Muon Optimizer

To evaluate the training efficiency of the Universal Reasoning Model (URM), we compare the Muon (Momentum Updated Orthogonal Newton) optimizer [ 12 ] with a standard adaptive baseline, Adamatan2 [ 6 ] . Muon approximates second-order curvature to apply orthogonal updates to better handle the complex loss landscapes [ 8 ] induced by deep recurrent structures. Both models are trained from scratch under identical experimental settings, including batch size, learning rate schedules, and data augmentation, ensuring that any observed differences arise solely from the choice of optimizer.

Across the ARC-AGI 1 and ARC-AGI 2 benchmarks, Muon demonstrates substantially faster convergence. On ARC-AGI 2, the Muon-optimized model reaches a pass@1 accuracy of 11.5% in approximately 600,000 training steps, whereas the Adamatan2 baseline requires over 1,300,000 steps to achieve the same performance, corresponding to nearly a twofold speedup in optimization. Despite this advantage in early training, both methods converge to similar final accuracies (approximately 53.8% on ARC-AGI 1 and 16.0% on ARC-AGI 2), indicating comparable asymptotic performance.

These results suggest a separation between optimization efficiency and architectural capacity in the URM. While Muon preconditions the challenging spectral properties of recurrent weight matrices [ 13 ] and reduces training cost, it does not lead to improved final generalization.

## 5 Related Work

### 5.1 ARC-AGI

Prior work on the ARC-AGI benchmark [ 3 , 2 ] spans vision-based formulations, large language model (LLM) adaptation, and recurrent reasoning architectures. Vision-centric approaches such as Vision ARC [ 10 ] reformulate ARC as an image-to-image transformation problem and show that standard visual inductive biases can achieve competitive performance, particularly with ensembling and test-time scaling. LLM-based methods explore fine-tuning and test-time training, demonstrating that transient parameter updates outperform static in-context learning on ARC-like tasks. Beyond language and vision models, recurrent architectures emphasize iterative computation as a core mechanism for abstraction. The Hierarchical Reasoning Model (HRM) [ 20 , 7 ] introduces multi-timescale recurrence and achieves strong ARC-AGI results, while subsequent analyses suggest that its gains may largely stem from recurrence rather than explicit hierarchy. The Tiny Recursive Model (TRM) [ 11 ] further simplifies this paradigm, showing that a single lightweight network applied recursively can match or exceed more complex hierarchical designs.

### 5.2 Universal Transformers (Looped Transformers)

The Universal Transformer (UT), also known as the Looped Transformer, was introduced by Dehghani et al. [ 5 ] as an extension of the standard Transformer with recurrent computation and adaptive computation time. Subsequent work has shown that UTs exhibit significantly stronger multi-step reasoning abilities than vanilla Transformers, as the recurrent refinement mechanism helps overcome architectural limitations in multi-hop reasoning tasks [ 4 , 19 ] . In addition, UTs demonstrate improved algorithmic learning capabilities, enabling more effective modeling of iterative and rule-based computations [ 21 ] . By reusing parameters across refinement steps, UTs also achieve higher parameter efficiency, allowing more expressive computation without increasing model size [ 15 ] .

## 6 Conclusion

We systematically investigate the sources of performance gains in Universal Transformer models on complex reasoning tasks. Extensive ablation studies reveal that these gains stem primarily from the recurrent inductive bias and strong nonlinear components of Transformer, rather than from overly complex architectural designs. Motivated by this insight, we propose the Universal Reasoning Model (URM), which enhances nonlinear depth-wise computation via short convolutional gating and improves optimization stability through truncated backpropagation through loops. URM achieves state-of-the-art performance on ARC-AGI 1 and 2.

## 7 Acknowledgement

We thank Benhao Huang for pointing out the typo in the previous version, and we also thank Zhengmao Ye from the Ubiquant AI team for providing infrastructure support.

## References

[1] Z. Allen-Zhu (2025) Physics of language models: part 4.1, architecture design and the magic of canon layers . In The Thirty-ninth Annual Conference on Neural Information Processing Systems , External Links: Link Cited by: §3.1 .

[2] F. Chollet, M. Knoop, G. Kamradt, B. Landers, and H. Pinkard (2025) ARC-agi-2: a new challenge for frontier ai reasoning systems . External Links: 2505.11831 , Link Cited by: §1 , §5.1 .

[3] F. Chollet, M. Knoop, G. Kamradt, and B. Landers (2025) ARC prize 2024: technical report . External Links: 2412.04604 , Link Cited by: §1 , §5.1 .

[4] R. Csordás, K. Irie, and J. Schmidhuber (2021) The devil is in the detail: simple tricks improve systematic generalization of transformers . In Proc. Conf. on Empirical Methods in Natural Language Processing (EMNLP) , Punta Cana, Dominican Republic . Cited by: §5.2 .

[5] M. Dehghani, S. Gouws, O. Vinyals, J. Uszkoreit, and Ł. Kaiser (2019) Universal transformers . External Links: 1807.03819 , Link Cited by: §1 , §2.2 , §3 , §5.2 .

[6] K. Everett, L. Xiao, M. Wortsman, A. A. Alemi, R. Novak, P. J. Liu, I. Gur, J. Sohl-Dickstein, L. P. Kaelbling, J. Lee, and J. Pennington (2024) Scaling exponents across parameterizations and optimizers . In Proceedings of the 41st International Conference on Machine Learning , ICML’24 . Cited by: §4.1 , §4.7 .

[7] R. Ge, Q. Liao, and T. Poggio (2025) Hierarchical reasoning models: perspectives and misconceptions . External Links: 2510.00355 , Link Cited by: §1 , §1 , §5.1 .

[8] Z. Gong, J. Teng, and Y. Liu (2025) What makes looped transformers perform better than non-recursive ones (provably) . External Links: 2510.10089 , Link Cited by: §4.7 .

[9] A. Graves (2017) Adaptive computation time for recurrent neural networks . External Links: 1603.08983 , Link Cited by: §2.2.2 , §4.1 .

[10] K. Hu, A. Cy, L. Qiu, X. D. Ding, R. Wang, Y. E. Zhu, J. Andreas, and K. He (2025) ARC is a vision problem! . External Links: 2511.14761 , Link Cited by: §5.1 , Abstract .

[11] A. Jolicoeur-Martineau (2025) Less is more: recursive reasoning with tiny networks . External Links: 2510.04871 , Link Cited by: §1 , §1 , §3 , §4.1 , §5.1 .

[12] K. Jordan, Y. Jin, V. Boza, J. You, F. Cesista, L. Newhouse, and J. Bernstein (2024) Muon: an optimizer for hidden layers in neural networks . External Links: Link Cited by: §4.7 .

[13] J. Liu, J. Su, X. Yao, Z. Jiang, G. Lai, Y. Du, Y. Qin, W. Xu, E. Lu, J. Yan, Y. Chen, H. Zheng, Y. Liu, S. Liu, B. Yin, W. He, H. Zhu, Y. Wang, J. Wang, M. Dong, Z. Zhang, Y. Kang, H. Zhang, X. Xu, Y. Zhang, Y. Wu, X. Zhou, and Z. Yang (2025) Muon is scalable for llm training . External Links: 2502.16982 , Link Cited by: §4.7 .

[14] R. Pascanu, T. Mikolov, and Y. Bengio (2013) On the difficulty of training recurrent neural networks . In Proceedings of the 30th International Conference on Machine Learning , S. Dasgupta and D. McAllester (Eds.) , Proceedings of Machine Learning Research , Vol. 28 , Atlanta, Georgia, USA , pp. 1310–1318 . External Links: Link Cited by: §4.5 .

[15] N. Saunshi, N. Dikkala, Z. Li, S. Kumar, and S. J. Reddi (2025) Reasoning with latent thoughts: on the power of looped transformers . In The Thirteenth International Conference on Learning Representations , External Links: Link Cited by: §4.3 , §5.2 .

[16] N. Shazeer (2020) GLU variants improve transformer . External Links: 2002.05202 , Link Cited by: §3.1 .

[17] C. Tallec and Y. Ollivier (2017) Unbiasing truncated backpropagation through time . External Links: 1705.08209 , Link Cited by: §4.5 .

[18] A. Vaswani, N. Shazeer, N. Parmar, J. Uszkoreit, L. Jones, A. N. Gomez, Ł. Kaiser, and I. Polosukhin (2017) Attention is all you need . In Advances in Neural Information Processing Systems , I. Guyon, U. V. Luxburg, S. Bengio, H. Wallach, R. Fergus, S. Vishwanathan, and R. Garnett (Eds.) , Vol. 30 , pp. . External Links: Link Cited by: §2.2 .

[19] B. Wang, X. Yue, Y. Su, and H. Sun (2024) Grokked transformers are implicit reasoners: a mechanistic journey to the edge of generalization . In The Thirty-eighth Annual Conference on Neural Information Processing Systems , External Links: Link Cited by: §5.2 .

[20] G. Wang, J. Li, Y. Sun, X. Chen, C. Liu, Y. Wu, M. Lu, S. Song, and Y. A. Yadkori (2025) Hierarchical reasoning model . External Links: 2506.21734 , Link Cited by: §1 , §1 , §3 , §4.1 , §5.1 .

[21] L. Yang, K. Lee, R. D. Nowak, and D. Papailiopoulos (2024) Looped transformers are better at learning learning algorithms . In The Twelfth International Conference on Learning Representations , External Links: Link Cited by: §5.2 .

[22] W. Yu, M. Luo, P. Zhou, C. Si, Y. Zhou, X. Wang, J. Feng, and S. Yan (2022) MetaFormer is actually what you need for vision . In Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR) , pp. 10819–10829 . Cited by: §3.1 .

[23] Y. Zhang, Y. Dong, and K. Kawaguchi (2024) Investigating layer importance in large language models . In The 7th BlackboxNLP Workshop , External Links: Link Cited by: §4.3 .

## Instructions for reporting errors

We are continuing to improve HTML versions of papers, and your feedback helps enhance accessibility and mobile support. To report errors in the HTML that will help us improve conversion and rendering, choose any of the methods listed below:

Click the "Report Issue" ( ) button, located in the page header.

Tip: You can select the relevant text first, to include it in your report.

Our team has already identified the following issues . We appreciate your time reviewing and reporting rendering errors we may not have found yet. Your efforts will help us improve the HTML versions for all readers, because disability should not be a barrier to accessing research. Thank you for your continued support in championing open access for all.

Have a free development cycle? Help support accessibility at arXiv! Our collaborators at LaTeXML maintain a list of packages that need conversion , and welcome developer contributions .
