##### Report GitHub Issue

Content selection saved. Describe the issue below:

\LettrineTextFont

# Hyena Hierarchy: Towards Larger Convolutional Language Models

###### Abstract

Recent advances in deep learning have relied heavily on the use of large Transformers due to their ability to learn at scale. However, the core building block of Transformers, the attention operator, exhibits quadratic cost in sequence length, limiting the amount of context accessible. Existing subquadratic methods based on low-rank and sparse approximations need to be combined with dense attention layers to match Transformers, indicating a gap in capability. In this work, we propose Hyena , a subquadratic drop-in replacement for attention constructed by interleaving implicitly parametrized long convolutions and data-controlled gating . In recall and reasoning tasks on sequences of thousands to hundreds of thousands of tokens, Hyena improves accuracy by more than 50 50 points over operators relying on state-spaces and other implicit and explicit methods, matching attention-based models. We set a new state-of-the-art for dense-attention-free architectures on language modeling in standard datasets ( WikiText103 and The Pile ), reaching Transformer quality with a 20 % 20\% reduction in training compute required at sequence length 2 2 K. Hyena operators are twice as fast as highly optimized attention at sequence length 8 8 K, and 100 × 100\times faster at sequence length 64 64 K.

## 1 Introduction

Large Transformers have enabled a number of breakthrough advances in modeling language, vision, audio, biology and numerous other domains ( Vaswani et al., 2017 ) , ( Dosovitskiy et al., 2020 ) , ( Radford et al., 2022 ) , ( Cramer, 2021 ) . Much of the success of Transformers, powered by the attention operator ( Vaswani et al., 2017 ) , relies on their scaling properties ( Hoffmann et al., 2022 ) and the emergence of in-context learning ( Garg et al., 2022 ) , which allows them to generalize to unseen data and tasks given context as input. The Transformer block is a powerful tool for sequence modeling, but it is not without its limitations. One of the most notable is the computational cost, which grows rapidly as the length of the input sequence increases. Specifically, the cost scales quadratically with the length L L of the sequence, which places a strict limit on the amount of context that can be considered by the model. Breaking the quadratic barrier is a key step towards new possibilities for deep learning, such as using entire textbooks as context, generating long-form music or processing gigapixel scale images.

Efforts to reduce the computational cost of attention in models primarily involve the use of linearized, low-rank, and sparse approximations ( Child et al., 2019 ; Wang et al., 2020 ; Kitaev et al., 2020 ; Zhai et al., 2021 ; Roy et al., 2021 ; Schlag et al., 2021 ; Tu et al., 2022 ) . These approaches introduce a trade-off between expressivity and speed, requiring hybridization with standard attention layers to reach Transformer quality ( Mehta et al., 2022 ; Dao et al., 2022c ) .

A growing amount of evidence suggests that attention mechanisms only utilize a small portion of their quadratic capabilities for language processing ( Olsson et al., 2022 ; Dao et al., 2022c ) , leading us to question its role as the gold-standard operator for deep learning at scale. Specifically, we ask:

Are there subquadratic operators that can match the quality of attention at scale?

We obtain a positive answer based on a composition of efficient subquadratic primitives, such as element-wise multiplication (gating) and long convolutions i.e., convolutions with filter sizes as long as the input. We rely on a set of targeted reasoning tasks, grounded in recent work on mechanistic interpretability ( Elhage et al., 2021 ; Power et al., 2022 ; Olsson et al., 2022 ; Zhang et al., 2022 ) such as recall and induction, to distill three properties of attention correlated with its performance and the quality gap with existing subquadratic approaches: a . a. Data control: Attention implements an expressive data-controlled ( Massaroli et al., 2020 ) linear operator 1 1 1 Self-attention can be expressed as y = 𝖠 ⁡ ( k , q ) ​ v y=\mathsf{A}(k,q)v where 𝖠 \mathsf{A} is the attention matrix conditioned by linear projections k , q k,q of the input and multiplied by v v , another projection. , encoding an entire family of linear functions in a single block.

b . b. Sublinear parameter scaling: Parameter counts of attention layers are decoupled from sequence length, allowing Transformers to allocate more parameters elsewhere e.g., the feed-forward neural networks ( 𝖥𝖥𝖭 \sf FFN s) between attention layers.

c . c. Unrestricted context: For a given input, attention has an unrestricted context i.e., it can approximate dependencies between any two inputs, without arbitrary restrictions such as locality (except in cases using masking such as autoregressive models).

#### The 𝖧𝗒𝖾𝗇𝖺 {\sf Hyena} hierarchy

Guided by these findings, we introduce the 𝖧𝗒𝖾𝗇𝖺 {\sf Hyena} hierarchy, an operator defined by a recurrence of two efficient subquadratic primitives: a long convolution and element-wise multiplicative gating (see Figure 1.1 ). A specified depth (i.e., number of steps) of the recurrence controls the size of the operator. For short recurrences, existing models are recovered as special cases ( Mehta et al., 2022 ; Dao et al., 2022c ) . By mapping each step in the 𝖧𝗒𝖾𝗇𝖺 {\sf Hyena} recurrence to its corresponding matrix form, we reveal 𝖧𝗒𝖾𝗇𝖺 {\sf Hyena} operators to be equivalently defined as a decomposition of a data-controlled matrix i.e., a matrix whose entries are functions of the input. Furthermore, we show how 𝖧𝗒𝖾𝗇𝖺 {\sf Hyena} operators can be evaluated efficiently without materializing the full matrix, by leveraging fast convolution algorithms ( Selesnick and Burrus, 2017 ) . Empirically, 𝖧𝗒𝖾𝗇𝖺 {\sf Hyena} operators are able to significantly shrink the quality gap with attention at scale, reaching similar perplexity and downstream performance with a smaller computational budget (Section 4.2 ) and without hybridization of attention.

#### Narrowing the capabilities gap

The design of Hyena is motivated by a quality gap between standard dense attention and alternative subquadratic operators, which we identify by focusing on reasoning tasks correlated with language modeling performance at scale. We extend the suite of basic mechanistic interpretability benchmarks ( induction and recall ) with additional tasks that probe how quickly model performance degrades when task complexity increases (e.g. vocabulary size grows). In addition, we investigate the optimal parameterization of long convolutions in 𝖧𝗒𝖾𝗇𝖺 {\sf Hyena} . In the most challenging settings with hundreds of thousands of tokens, our implicit parameterization scheme improves over other operators leveraging state spaces ( Gu et al., 2021 ) , frequency-domain parametrizations ( Li et al., 2020 ) , or standard convolutions by over 50 % 50\% accuracy.

#### Scaling in language and vision

Next, we aim to verify whether rankings in our reasoning benchmark suite are predictive of quality at scale. We test 𝖧𝗒𝖾𝗇𝖺 {\sf Hyena} on autoregressive language modeling at the sub-billion parameter scale, setting a new state-of-the-art for dense-attention-free architectures in standard datasets ( WikiText103 and The Pile ) and matching Transformer quality. On the The Pile at the 335 335 M parameter scale, we match Transformer perplexity with a 20 % 20\% reduction in the total count of floating point operations (FLOPs). As an extension, we investigate the generality of 𝖧𝗒𝖾𝗇𝖺 {\sf Hyena} operators by testing on large-scale image recognition, replacing attention in the Vision Transformer (ViT) ( Dosovitskiy et al., 2020 ) . In image classification, 𝖧𝗒𝖾𝗇𝖺 {\sf Hyena} is able to match attention in accuracy when training on ImageNet-1k from scratch.

#### Toward much longer context

Finally, we benchmark the efficiency of 𝖧𝗒𝖾𝗇𝖺 {\sf Hyena} on long sequences. We measure 5 5 x speedups over dense self-attention at length 8192 8192 – 2 2 x over highly optimized FlashAttention 2 2 2 FlashAttention is already 2-4x faster than a standard attention implementation in PyTorch. ( Dao et al., 2022b ) – and 100 100 x speedup over FlashAttention at sequence lengths of 64 64 k, where standard attention implementation in PyTorch runs out of memory.

## 2 Preliminaries and Related Work

A discrete convolution is a function of two arguments: an input u u signal of length L L and a learnable filter h h . The linear (aperiodic) convolution of a (possibly infinitely long) measurable 3 3 3 In the L 1 ​ ( ℤ ) L^{1}(\mathbb{Z}) sense: ∑ t = − ∞ ∞ | h t | < ∞ \sum_{t=-\infty}^{\infty}|h_{t}|<\infty filter h h with a length- L L input signal u u is defined as y t = ( h ∗ u ) t = ∑ n = 0 L − 1 h t − n ​ u n . \displaystyle y_{t}=(h*u)_{t}=\sum_{n=0}^{L-1}h_{t-n}u_{n}. (1)

Generally, u t ∈ ℝ D u_{t}\in\mathbb{R}^{D} where D D is the width of the signal, or in deep learning parlance, the number of channels . Without loss of generality, we specialize our analysis to single input single output (SISO) layers, i.e. with D = 1 D=1 . The multiple input multiple output (MIMO) case, canonical in standard convolutional layers, follows directly.

In this case, the input signal can be represented as a vector u ∈ ℝ L u\in\mathbb{R}^{L} and the convolution as a matrix-vector product between the input and the Toeplitz kernel matrix 𝖲 h ∈ ℝ L × L \mathsf{S}_{h}\in\mathbb{R}^{L\times L} induced by the filter h h : ( h ∗ u ) = [ h 0 h − 1 ⋯ h − L + 1 h 1 h 0 ⋯ h − L + 2 ⋱ h L − 1 h L − 2 ⋯ h 0 ] ​ [ u 0 u 1 u L − 1 ] \displaystyle(h*u)=\begin{bmatrix}h_{0}&h_{-1}&\cdots&h_{-L+1}\\ h_{1}&h_{0}&\cdots&h_{-L+2}\\ \vdots&\vdots&\ddots&\vdots\\ h_{L-1}&h_{L-2}&\cdots&h_{0}\end{bmatrix}\begin{bmatrix}u_{0}\\ u_{1}\\ \vdots\\ u_{L-1}\end{bmatrix} (2)

### 2.1 Explicit and Implicit Convolutions

Parametrizing and optimizing convolution filters h t h_{t} is a standard procedure in deep learning and more broadly signal processing. The classical approach of convolutional neural networks (CNNs) ( Fukushima and Miyake, 1982 ; LeCun et al., 1998 ; Ronneberger et al., 2015 ; He et al., 2016 ) is to optimize directly the values h t h_{t} of the filter’s response at M M prescribed steps, a parametrization we call explicit . M M is referred to as the filter size and is typically much shorter than the input sequence length M ≪ L M\ll L . Such filters are denoted in signal processing as finite impulse response (FIR).

FIR filters are local and can capture dependencies between inputs separated at most by M M steps. Their main advantage is their speed, with complexity 𝒪 ⁡ ( M ​ L ) \mathcal{O}(ML) . However, the number of parameters of FIR filters scales linearly with filter size, which can be computationally prohibitive. To disentangle the parameter count from the filter size, we can instead represent the filter h t h_{t} as a parametric function of the time step t t , i.e. h t = γ θ ​ ( t ) h_{t}=\gamma_{\theta}(t) , where θ \theta are the parameters of the function γ θ \gamma_{\theta} . This parametrization is called implicit . The class of functions γ θ \gamma_{\theta} is a design choice with a significant impact on the expressivity and computational complexity of the layer.

One choice of implicit parametrization is to select h h as the response function of a linear state-space model (SSM) ( Chen, 1984 ) , described by the first-order difference equation: x t + 1 \displaystyle x_{t+1} = 𝖠 ​ x t + 𝖡 ​ u t \displaystyle=\mathsf{A}x_{t}+\mathsf{B}u_{t} state equation \displaystyle\text{state equation} y t \displaystyle y_{t} = 𝖢 ​ x t + 𝖣 ​ u t \displaystyle=\mathsf{C}x_{t}+\mathsf{D}u_{t} output equation \displaystyle\text{output equation} Here, the convenient choice of x 0 = 0 x_{0}=0 renders the input-output map to a simple convolution y t \displaystyle y_{t} = ∑ n = 0 t ( 𝖢𝖠 t − n ​ 𝖡 + 𝖣 ​ δ t − n ) ​ u n \displaystyle=\sum_{n=0}^{t}\left(\mathsf{C}\mathsf{A}^{t-n}\mathsf{B}+\mathsf{D}\delta_{t-n}\right)u_{n} where δ t \delta_{t} denotes the Kronecker delta. We can then identify the filter h h as t ↦ h t = { 0 t < 0 𝖢𝖠 t ​ 𝖡 + 𝖣 ​ δ t t ≥ 0 t\mapsto h_{t}=\begin{cases}0&t<0\\ \mathsf{C}\mathsf{A}^{t}\mathsf{B}+\mathsf{D}\delta_{t}&t\geq 0\end{cases} where the entries of 𝖠 , 𝖡 , 𝖢 \mathsf{A},\mathsf{B},\mathsf{C} and 𝖣 \mathsf{D} are the learned parameters of the filter. In terms of layer design, the degrees of freedom of SSMs are the dimension of the state and the structure of the matrices. SSMs are a canonical example of how long convolutions with sub-linear parameter counts can improve deep learning models for long sequences ( Gu et al., 2020 ; Gu et al., 2021 ) . Other implicit approaches include parametrizing filters as maps from (a positional encoding of) t t to the filter response i.e. γ θ : t ↦ h t = γ θ ​ ( t ) \gamma_{\theta}:t\mapsto h_{t}=\gamma_{\theta}(t) , for example with feed-forward neural networks ( Romero et al., 2021b ; Romero et al., 2021a ) .

#### Fast Methods for Convolutions

One of the first applications of the Cooley-Tukey fast Fourier transform (FFT) algorithm was to implement convolution faster than the direct evaluation of ( 1 ). At first glance ( 1 ) comes with O ⁡ ( L 2 ) O(L^{2}) an asymptotic time complexity. A common approach to achieve fast long convolutions in subquadratic time is through the FFT algorithm. The method first converts the aperiodic convolution into a circular convolution Selesnick and Burrus (2017) by appropriate zero-padding of input and filter sequences. The resulting kernel 𝖲 ^ h \hat{\mathsf{S}}_{h} is a circulant matrix and is diagonalized by the discrete Fourier basis 𝖲 ^ h = 𝖶 − 1 ​ 𝖣 H ​ 𝖶 \hat{\mathsf{S}}_{h}=\mathsf{W}^{-1}\mathsf{D}_{H}\mathsf{W} where 𝖶 \mathsf{W} is the DFT matrix, 𝖶 t ​ t ′ = z − t , z = e i ​ 2 ​ π ​ t ′ / L \mathsf{W}_{tt^{\prime}}=z^{-t},z=e^{i2\pi t^{\prime}/L} and H H is the DFT of the padded filter h h , H = 𝖶𝗉𝖺𝖽 ⁡ ( h ) H=\mathsf{W}{\sf pad}(h) . Thus, the calculation of such convolutions is performed as 𝗉𝖺𝖽 ⁡ ( y ) \displaystyle{\sf pad}(y) = 𝖲 ^ h ​ 𝗉𝖺𝖽 ​ ( u ) \displaystyle=\hat{\mathsf{S}}_{h}{\sf pad}(u) = 𝖶 − 1 ​ 𝖣 H ​ 𝖶 ​ 𝗉𝖺𝖽 ​ ( u ) \displaystyle=\mathsf{W}^{-1}\mathsf{D}_{H}\mathsf{W}~{\sf pad}(u) = 𝗂𝖥𝖥𝖳 ⁡ ( 𝖣 H ​ 𝖥𝖥𝖳 ​ ( 𝗉𝖺𝖽 ⁡ ( u ) ) ) \displaystyle={\sf iFFT}(\mathsf{D}_{H}{\sf FFT}({\sf pad}(u))) where 𝖣 H \mathsf{D}_{H} is the matrix with 𝖶 ​ h \mathsf{W}h on its diagonal. The above is known as the convolution theorem of DFT ( Oppenheim et al., 1997 ) . In this 𝖥𝖥𝖳𝖢𝗈𝗇𝗏 {\sf FFTConv} form the convolution can be performed without materializing the operator 𝖲 h \mathsf{S}_{h} with the same asymptotic cost O ⁡ ( L ​ log 2 ​ L ) O(L\log_{2}L) of FFT.

### 2.2 The Self-Attention Operator

At the heart of Transformers is the multi-head attention (MHA) mechanism. Given a length- L L sequence u ∈ ℝ L × D u\in\mathbb{R}^{L\times D} , each head of scaled self-attention ( Vaswani et al., 2017 ) is a map from ℝ L × D \mathbb{R}^{L\times D} to ℝ L × D \mathbb{R}^{L\times D} which performs the following operations 𝖠 ⁡ ( u ) \displaystyle\mathsf{A}(u) = 𝖲𝗈𝖿𝗍𝖬𝖺𝗑 ⁡ ( 1 D ​ u ​ 𝖬 q ​ 𝖬 k ⊤ ​ u ⊤ ) \displaystyle={\sf SoftMax}\left(\tfrac{1}{\sqrt{D}}u\mathsf{M}_{q}\mathsf{M}^{\top}_{k}u^{\top}\right) (3) y \displaystyle y = 𝖲𝖾𝗅𝖿𝖠𝗍𝗍𝖾𝗇𝗍𝗂𝗈𝗇 ⁡ ( u ) \displaystyle={\sf SelfAttention}(u) = 𝖠 ⁡ ( u ) ​ u ​ 𝖬 v , \displaystyle=\mathsf{A}(u)u\mathsf{M}_{v},

where 𝖬 q , 𝖬 k , 𝖬 v ∈ ℝ D × D \mathsf{M}_{q},\mathsf{M}_{k},\mathsf{M}_{v}\in\mathbb{R}^{D\times D} are learnable linear projections and 𝖲𝗈𝖿𝗍𝖬𝖺𝗑 {\sf SoftMax} is intended to be applied row-wise. Attention parametrizes a family of dense linear operators and for an input u u , indexes through it via projections of u u i.e., 𝖠 ⁡ ( u ) \mathsf{A}(u) . We refer to operators of this type as data-controlled , as they encode a linear transformation u ↦ y u\mapsto y , that is, however, nonlinearly defined by u u . This approach yields expressive nonlinear operators in u u , and we hypothesize contributes, together with other mechanisms ( Olsson et al., 2022 ) , to the ability of certain operators to learn in-context i.e., to adapt to unseen tasks by leveraging context. In deep learning, the projections take on specific names: query q = u ​ 𝖬 q q=u\mathsf{M}_{q} , key k = u ​ 𝖬 k k=u\mathsf{M}_{k} and value v = u ​ 𝖬 v v=u\mathsf{M}_{v} . We often rewrite the attention operator as y = 𝖠 ⁡ ( q , k ) ​ v y=\mathsf{A}(q,k)v .

###### Remark 2.1 .

Similarly to implicit convolutions, 𝖲𝖾𝗅𝖿𝖠𝗍𝗍𝖾𝗇𝗍𝗂𝗈𝗇 \sf SelfAttention does not entangle its ability to access distant information with the number of parameters: it looks at the whole sequence at the price of 𝒪 ⁡ ( L 2 ) \mathcal{O}(L^{2}) operations.

#### Subquadratic Operators

Existing approaches to subquadratic alternatives to attention can be summarized by altering the way the data control is implemented i.e., how the operator is nonlinearly defined by u u , and then applied to v v . For example, a layer of Attention-Free Transformers (AFTs) ( Zhai et al., 2021 ) constructs the operator through a combination of gating and 𝖲𝗈𝖿𝗍𝖬𝖺𝗑 \sf SoftMax (AFT full) or gating and a single explicit convolution (AFT conv). Gated State Spaces (GSS) instead compose the operator via gating and a long convolution parametrized via SSMs. Taking this idea further, Hungry Hungry Hippo (H3) ( Dao et al., 2022c ) , motivated by gaps of GSS on associative recall, extend the mechanism to include an additional gate and a short convolution obtained via a shift SSM. 𝖧𝗒𝖾𝗇𝖺 {\sf Hyena} generalizes this body of work by introducing a recurrence of gates and implicit long convolutions, evaluated efficiently.

## 3 Hyena: Definition and Properties

In this section, we define Hyena, a class of data-controlled operators consisting of a recurrence of multiplicative gating interactions and long convolutions. Instead of seeking an approximation to attention, we guide our design by intentionally incorporating key computational properties of attention, including the decoupling of sequence length and parameter counts.

### 3.1 𝖧𝗒𝖾𝗇𝖺 {\sf Hyena} Recurrences

At a high level, 𝖧𝗒𝖾𝗇𝖺 {\sf Hyena} consists of the following steps (setting D = 1 D=1 for clarity): i . i. Compute a set of N + 1 N+1 linear projections of the input, similarly to attention. The number of projections ( v t , x t 1 , … , x t N ) (v_{t},x^{1}_{t},\dots,x^{N}_{t}) need not be three. One projection takes the role of value, such that a linear input-output function can be defined as y = 𝖧 ⁡ ( u ) ​ v y=\mathsf{H}(u)v for some 𝖧 ⁡ ( u ) \mathsf{H}(u) .

i ​ i . ii. The matrix 𝖧 ⁡ ( u ) \mathsf{H}(u) is defined by interleaving implicit long convolutions and element-wise multiplication with one projection x i x^{i} at a time, until all projections are exhausted. Evaluation of 𝖧 ⁡ ( u ) ​ v \mathsf{H}(u)v is done efficiently without materializing 𝖧 ⁡ ( u ) \mathsf{H}(u) . By doing so, we implicitly define a data-controlled operator as a factorization of a matrix. The long convolutions forming 𝖧 ⁡ ( u ) \mathsf{H}(u) are parametrized implicitly to retain sublinear parameter scaling in sequence length.

Next, we formally define 𝖧𝗒𝖾𝗇𝖺 {\sf Hyena} , starting with its computational model. We leave the analysis of its data-controlled matrix form for the latter part of the section.

###### Remark 3.1 .

The time complexity of a 𝖧𝗒𝖾𝗇𝖺 \sf Hyena recurrence is 𝒪 ⁡ ( N ​ L ​ log 2 ⁡ L ) \mathcal{O}(NL\log_{2}L) . The input-output map can be rewritten as y = x N ⋅ ( h N ∗ ( x N − 1 ⋅ ( h N − 1 ∗ ( ⋯ ) ) ) ) y=x^{N}\cdot(h^{N}*(x^{N-1}\cdot(h^{N-1}*(\cdots)))) where each convolution is performed through the Fourier domain in 𝒪 ⁡ ( L ​ log 2 ​ L ) \mathcal{O}(L\log_{2}L) .

Interestingly, the element-wise product in time domain corresponds to convolution in frequency domain, i.e. x t ​ u t = ( x ^ ∗ u ^ ) t , x_{t}u_{t}=(\hat{x}*\hat{u})_{t}, where x ^ , u ^ \hat{x},\hat{u} denote the DFT of x x and u u , respectively. Thus, 𝖧𝗒𝖾𝗇𝖺 \sf Hyena is alternatively applying convolutions in the time and then the frequency domain (or alternatively applying element-wise products in the time and frequency domain). One potential explanation for the effectiveness of this procedure is that the convolution in the time domain (element-wise multiplication in the frequency domain) increases the memory length, allowing for a broader context to be taken into account. On the other hand, the element-wise multiplication in the time domain (convolution in the frequency domain) allows for more fine-grained selection of specific frequency components of the signal.

### 3.2 𝖧𝗒𝖾𝗇𝖺 {\sf Hyena} Matrices

𝖧𝗒𝖾𝗇𝖺 {\sf Hyena} operators build on the 𝖧𝟥 {\sf H3} mechanism developed by ( Dao et al., 2022c ) . For clarity of exposition, we once again consider the SISO case ( D = 1 D=1 ). Let 𝖣 q \mathsf{D}_{q} and 𝖣 k \mathsf{D}_{k} be the L L -by- L L diagonal matrices whose respective main diagonal entries are the respective entries of q q and k k . 𝖧𝟥 {\sf H3} realizes a surrogate attention matrix with a data-controlled, parametrized decomposition in four terms: 𝖠 ⁡ ( q , k ) \displaystyle\mathsf{A}(q,k) = 𝖣 q ​ 𝖲 ψ ​ 𝖣 k ​ 𝖲 φ \displaystyle=\mathsf{D}_{q}\mathsf{S}_{\psi}\mathsf{D}_{k}\mathsf{S}_{\varphi} (5) 𝖧𝟥 ⁡ ( q , k , v ) \displaystyle{\sf H3}(q,k,v) = 𝖠 ⁡ ( q , k ) ​ v \displaystyle=\mathsf{A}(q,k)v where 𝖲 φ , 𝖲 ψ \mathsf{S}_{\varphi},\mathsf{S}_{\psi} are the Toeplitz matrices of learnable causal filters φ , ψ \varphi,\psi parametrized via SSMs 5 5 5 For consistency with our discussion, we have swapped k k and v v compared to the notation in ( Dao et al., 2022c ) . . Alongside the q ​ k ​ v qkv -projections the filters constitute our degrees of freedom in the layer design. This decomposition allows evaluation of ( 8 ) in just 𝒪 ⁡ ( L ​ log 2 ​ L ) \mathcal{O}(L\log_{2}L) time (two FFT convolutions and two element-wise products), i.e. z t \displaystyle z_{t} = k t ​ ( φ ∗ v ) t \displaystyle=k_{t}(\varphi*v)_{t} (6) y t \displaystyle y_{t} = q t ​ ( ψ ∗ z ) t \displaystyle=q_{t}(\psi*z)_{t} 𝖧𝗒𝖾𝗇𝖺 \small\sf Hyena represents a generalization of ( 8 ) for an arbitrary number of projections – not limited to three – and with implicit free-form long filters for the convolutions. The resulting recurrence ( 4 ) can be also represented in matrix form y = 𝖧 ⁡ ( u ) ​ v y=\mathsf{H}(u)v . Let 𝖣 x n = diag ⁡ ( x n ) ∈ ℝ L × L \mathsf{D}_{x}^{n}=\diag(x^{n})\in\mathbb{R}^{L\times L} and let 𝖲 h n \mathsf{S}_{h}^{n} be the Toeplitz matrix corresponding to filter h n h^{n} . The resulting 𝖧𝗒𝖾𝗇𝖺 \sf Hyena recurrence is linear in v v and can be rewritten in matrix form: y = 𝖧 ( u ) v = 𝖣 x N 𝖲 h N ⋯ 𝖣 x 2 𝖲 h 2 𝖣 x 1 𝖲 h 1 v y=\mathsf{H}(u)v=\mathsf{D}_{x}^{N}\mathsf{S}_{h}^{N}\cdots\mathsf{D}_{x}^{2}\mathsf{S}_{h}^{2}\mathsf{D}_{x}^{1}\mathsf{S}_{h}^{1}v Figure 2.1 visualizes an example decomposition.

###### Remark 3.2 ( 𝖧𝗒𝖾𝗇𝖺 \sf Hyena generalizes 𝖧𝟥 \sf H3 and 𝖦𝖲𝖲 \sf GSS .) .

The 𝖧𝟥 \sf H3 mechanism ( Dao et al., 2022c ) corresponds to 𝖧𝗒𝖾𝗇𝖺 2 {\sf Hyena}_{2} and 𝖦𝖲𝖲 \sf GSS ( Mehta et al., 2022 ) is 𝖧𝗒𝖾𝗇𝖺 1 {\sf Hyena}_{1} , with a particular choice of parametrization for the long convolutions (SSMs).

Analysis of the 𝖧𝟥 \sf H3 mechanism as a decomposition 𝖣 q ​ 𝖲 ψ ​ 𝖣 k ​ 𝖲 φ \mathsf{D}_{q}\mathsf{S}_{\psi}\mathsf{D}_{k}\mathsf{S}_{\varphi} of its surrogate attention matrix 6 6 6 Some of this analysis is reported in the Appendix. clarifies a connection to fast evaluation algorithms for matrix-vector multiplications. In particular, the generalization of ( 8 ) to an arbitrary order is inspired by fast evaluation algorithms for structured dense matrices based on butterfly decompositions ( Li et al., 2015 ; Dao et al., 2019 ; Dao et al., 2022a ) , with length of the decomposition closely tied to its expressivity (in the classes of matrices it can represent). The 𝖧𝗒𝖾𝗇𝖺 {\sf Hyena} operator blends data control with a special case of butterfly decomposition.

###### Remark 3.3 .

𝖧𝗒𝖾𝗇𝖺 {\sf Hyena} operators have unbounded context. Namely, they are not artificially restricted by e.g., locality, and can learn long-range dependencies between any of the elements of v v via long convolutions, which we discuss next.

### 3.3 𝖧𝗒𝖾𝗇𝖺 {\sf Hyena} Filters

Here we provide details on the convolution parametrization. We represent the filters of each 𝖧𝗒𝖾𝗇𝖺 {\sf Hyena} operator as a map from the time (or space) domain t t to values h t h_{t} , and learn it with a shallow feed-forward neural network ( 𝖥𝖥𝖭 \sf FFN ): h t = 𝖶𝗂𝗇𝖽𝗈𝗐 ⁡ ( t ) ⋅ ( 𝖥𝖥𝖭 ∘ 𝖯𝗈𝗌𝗂𝗍𝗂𝗈𝗇𝖺𝗅𝖤𝗇𝖼𝗈𝖽𝗂𝗇𝗀 ) ​ ( t ) h_{t}={\sf Window}(t)\cdot({\sf FFN}\circ{\sf PositionalEncoding})(t) (7) This approach builds on the neural implicit representation literature ( Mildenhall et al., 2021 ; Sitzmann et al., 2020 ) , which has found application in long convolution layers ( Romero et al., 2021b ; Romero et al., 2021a ) . One advantage of ( 7 ) is given by the decoupling of filter length and parameter cost.

#### Specializing filters in Hyena

The window and positional encoding functions are used to specialize filters in 𝖧𝗒𝖾𝗇𝖺 {\sf Hyena} operators, biasing them towards a specific type. Figure 3.1 provides an important example: we choose at least one of the convolutions in 𝖧𝗒𝖾𝗇𝖺 {\sf Hyena} to be shaped towards exponential decay, mirroring the findings of ( Li et al., 2022 ) in other applications.

Interestingly, we find that long exponentially decaying filters display synergy with high-frequency filters, as they enable the operator to select specific inputs at specific steps 7 7 7 This observation finds mirrors in the parametrization of the convolutions in H3 ( Dao et al., 2022c ) as a shift SSM and a diagonal SSM. . Similarly to ( Romero et al., 2021b ) , we use high-frequency periodic activations (sine) in the 𝖥𝖥𝖭 \sf FFN . This allows ( 7 ) to learn filters with high-frequency content, addressing the low-frequency bias of neural networks ( Basri et al., 2020 ) . Owing to the 𝖥𝖥𝖭 \sf FFN , the parametrization in ( 7 ) can approximate filters obtained through other means, such as S4 ( Gu et al., 2020 ; Gu et al., 2021 ) , CKConv ( Romero et al., 2021b ) , SGConv ( Li et al., 2022 ) and Fourier Neural Operator (FNO) ( Li et al., 2020 ) .

#### Preserving causality

Causality is necessary to train autoregressive language models, in order for the output at a given position to depend only on the past. For example, Transformers mask the attention matrix to be lower triangular. In the case of 𝖧𝗒𝖾𝗇𝖺 {\sf Hyena} , causality can be guaranteed by parametrizing causal convolutions:

###### Proposition 3.1 (Causal Hyenas) .

If each filter h n , n = 1 , … , N h^{n},~n=1,\dots,N is causal, then the corresponding 𝖧𝗒𝖾𝗇𝖺 N {\sf Hyena}_{N} operator is causal.

In practice, we need not constrain the learning of the filter ( 7 ) to ensure its numerical causality. If we use FFT-based convolution algorithms, all we need is to evaluate the filter at t = 0 , … , L − 1 t=0,\dots,L-1 and zero-pad the input and filter sequences to 2 ​ L − 1 2L-1 before taking FFT.

#### Efficiency

One bottleneck of long convolution models can be their low utilization of hardware accelerators, especially when they involve iterative numerical methods to materialize the filter 8 8 8 In contrast, deep learning primitives are designed for high GPU utilization, with FFNs and attention usually reaching 50 − 70 % 50-70\% or higher, if optimized. . Evaluation of 7 is fast, since it involves a single forward pass of an 𝖥𝖥𝖭 \sf FFN , and can be performed in parallel across sequence length and all orders of an 𝖧𝗒𝖾𝗇𝖺 {\sf Hyena} operator as displayed in Algorithm 3 , increasing hardware utilization. An additional source of low utilization is the FFT, which is also shared by other long other convolutional layers. This bottleneck can be partially addressed by blocking ( Selesnick and Burrus, 2017 ) , and optimization of the underlying routines ( Dao et al., 2022c ) . We benchmark runtime in Section 4.5 .

### 3.4 Hyena Algorithm

A forward pass of Hyena is summarized below.

###### Proposition 3.2 (Computational Complexity) .

The computational cost of processing an input u ∈ ℝ L × D u\in\mathbb{R}^{L\times D} with an order- N N 𝖧𝗒𝖾𝗇𝖺 \sf Hyena operator is 𝒪 ⁡ ( N ​ D ​ L ​ ( log 2 ​ L + D ) ) \mathcal{O}(NDL(\log_{2}L+D))

## 4 Experiments

### 4.1 Shrinking the gap on in-context learning

We begin by empirically motivating the 𝖧𝗒𝖾𝗇𝖺 {\sf Hyena} design, including the choice of long convolution parametrization. We consider the suite of tasks described in Table 4.1 .

Our evaluation is grounded in recent work on mechanistic interpretability of Transformers ( Elhage et al., 2021 ; Power et al., 2022 ; Olsson et al., 2022 ; Zhang et al., 2022 ) . Recently, associative recall, in particular, has been successfully used to guide the design of H3 ( Dao et al., 2022c ) . We extend the suite of tasks from these works and include benchmarking more challenging versions of each task . For example, solving associative recall with a vocabulary size of only 10 10 reveals whether a model is structurally capable of performing recall. Testing on much longer sequences and larger vocabularies reveals additional gaps in performance that are otherwise hidden.

#### How to parametrize long convolutions

We compare the performance of the following long convolution parametrizations for S 1 S^{1} and S 2 S^{2} in an order 2 2 Hyena: • Conv1d: Explicit convolutions (regular convolution layers with fixed filter size).

• FNO: Filters parametrized explicitly in the frequency-domain ( Li et al., 2020 ) .

• H3: Implicit parametrization using state-space models (SSMs), in particular the standard S4 ( Gu et al., 2021 ) .

• TransferFunc: Implicit parametrization via transfer functions, a classical system-theoretic generalization of SSMs 9 9 9 Transfer functions roughly correspond to a frequency-domain representation of SSMs.

• CKConv: Implicit parametrization using 𝖥𝖥𝖭 \sf FFN s ( Romero et al., 2021b ) .

• 𝖧𝗒𝖾𝗇𝖺 {\sf Hyena} : Combination of implicit parametrizations via 𝖥𝖥𝖭 \sf FFN s (with exponential decay modulation as shown in Figure 3.1 ), and short explicit filters.

All models have the same width and 2 2 layers. Figure 4.1 shows implicit approaches based on FFNs outperform other long convolutions, with the gap widening on longer sequences and larger vocabulary sizes. We train a different model on each setting of sequence length and vocabulary size. The ranking is correlated with the ability to decouple sequence length from parameter count ( 𝖧𝗒𝖾𝗇𝖺 {\sf Hyena} , CKConv, TransferFunc, H3) and expressivity (Hyena, CKConv). We observe similar trends on the other tasks.

#### Pushing sequence length to the limit

Next, we evaluate associative recall performance on extremely long sequences of length 131 131 k. To the best of our knowledge, these represent the first empirical display of attention-free in-context learning on sequences of this length. The gap between parametrization schemes widens as shown in Appendix A, with 𝖧𝗒𝖾𝗇𝖺 {\sf Hyena} outperforming CKConv by 80 80 points.

#### Comparing operators

We repeat our associative recall experiment, this time benchmarking different 2 2 layer models rather than changing the convolution parametrization: an order 2 2 Hyena, GSS ( Mehta et al., 2022 ) , H3 ( Dao et al., 2022c ) , AFT-conv ( Zhai et al., 2021 ) , RWKV ( Peng, 2021 ) , and a standard GPT ( Brown et al., 2020 ) using FlashAttention ( Dao et al., 2022b ) . As shown in Table 4.2 , 𝖧𝗒𝖾𝗇𝖺 {\sf Hyena} is the only operator able to solve the task. Our results challenge the observation that only Transformers are capable of challenging in-context learning.

Surprisingly, rankings of model performance at a fixed sequence length on The Pile are consistent with rankings on aggregate scores on our synthetics (Appendix C ).

#### Generality of 𝖧𝗒𝖾𝗇𝖺 {\sf Hyena} operators and filters

𝖧𝗒𝖾𝗇𝖺 {\sf Hyena} operators and filters can also applied successfully beyond language tasks. We experiment on sequential CIFAR, where pixels are flattened as a sequence, and use the same operator defined for language. We reach the accuracy of standard S4 ( Gu et al., 2021 ) with same model size ( 91 % 91\% ). In Section 4.5 and Appendix A , we discuss larger-scale image classification experiments with Hyena.

### 4.2 Language Modeling

Next, we verify the scaling of 𝖧𝗒𝖾𝗇𝖺 {\sf Hyena} on autoregressive language modeling. We evaluate the perplexity on WikiText103 (Table 4.4 ) and The Pile (Table 4.4 ). On the The Pile , we train different models for 5 , 10 , 15 5,10,15 billion tokens (different runs), adjusting the learning rate scheduler. 𝖧𝗒𝖾𝗇𝖺 {\sf Hyena} is the first attention-free, convolution architecture to match GPT quality with a 20 % ~20\% 10 10 10 The FLOP reduction consists in the non-parametric FLOPs of 𝖲𝖾𝗅𝖿𝖠𝗍𝗍𝖾𝗇𝗍𝗂𝗈𝗇 \sf SelfAttention devoted to attention matrix computation. The ratio of parametric to non-parametric FLOPs (and hence the gains) depend on the ratio of model width D D and sequence length L L used in training. reduction in total FLOPs. Preliminary scaling laws are shown in Figure 4.2 , collecting the training runs at 5 , 10 , 15 5,10,15 billion tokens. Each curve represents a different training run. In Appendix A , we provide results on the PG-19 long-range benchmark ( Rae et al., 2019 ) .

### 4.3 Downstream Evaluation

We perform a downstream evaluation on SuperGLUE ( Wang et al., 2019 ) tasks. We compare 𝖧𝗒𝖾𝗇𝖺 {\sf Hyena} (trained for 137 137 billion tokens) with the best available pre-trained attention-free model, RWKV ( Peng, 2021 ) (trained for 332 332 billion tokens), and a reference GPTNeo ( Black et al., 2021 ) (trained for 300 300 billion tokens) of the same size. Tables 4.5 and 4.6 summarize the results. 𝖧𝗒𝖾𝗇𝖺 {\sf Hyena} performs similarly to other models despite having been trained on less than half the number of total tokens. We observe 𝖧𝗒𝖾𝗇𝖺 {\sf Hyena} to display characteristic few-shot capabilities of standard Transformers, with some tasks e.g., MultiRC seeing a lift of more than 20 % 20\% accuracy over zero-shot when the model is provided additional prompts as context. The improvements are more noticeable in generation tasks, where the additional prompts can instruct the model on how it should be responding to the questions. We report an additional downstream evaluation on the LAMBADA task ( Paperno et al., 2016 ) in Appendix A .

### 4.4 Benchmarking

We benchmark runtime of an order 2 2 𝖧𝗒𝖾𝗇𝖺 {\sf Hyena} operator compared to attention and FlashAttention layers ( Dao et al., 2022b ) . 𝖧𝗒𝖾𝗇𝖺 {\sf Hyena} uses a fused CUDA kernel to perform 𝖥𝖥𝖳𝖢𝗈𝗇𝗏 {\sf FFTConv} ( Dao et al., 2022c ) . We set batch size to 64 64 and measure runtime (in milliseconds). Results are provided in Figure 4.3 . 𝖧𝗒𝖾𝗇𝖺 {\sf Hyena} speedups reach 100 × 100\times at sequence length 64 64 K. Crossover points for 𝖧𝗒𝖾𝗇𝖺 {\sf Hyena} and attention is at length 2048 2048 , and for 𝖧𝗒𝖾𝗇𝖺 {\sf Hyena} and FlashAttention is between 4096 4096 and 8196 8196 . Despite the absolute reduction in FLOPs, speedups are achieved only on longer sequences when the gap grows sufficiently large. This occurs because hardware utilization of 𝖧𝗒𝖾𝗇𝖺 {\sf Hyena} is lower than FlashAttention. We expect the gap between theoretical maximum speedup to shrink with improved implementations of 𝖥𝖥𝖳𝖢𝗈𝗇𝗏 {\sf FFTConv} and specialized hardware.

### 4.5 Large-Scale Image Classification

Finally, we demonstrate the potential of 𝖧𝗒𝖾𝗇𝖺 {\sf Hyena} as a general deep learning operator by applying it to image classification. On ImageNet , we drop-in replace attention layers in the Vision Transformer (ViT) ( Dosovitskiy et al., 2020 ) with the 𝖧𝗒𝖾𝗇𝖺 {\sf Hyena} operator (without changes from its language counterpart) and match performance with ViT. We also show that using smaller image patches boosts performance in both attention and 𝖧𝗒𝖾𝗇𝖺 {\sf Hyena} . Since this results in longer sequence lengths, we expect 𝖧𝗒𝖾𝗇𝖺 {\sf Hyena} to outperform in speed as patches get more fine-grained approaching pixel-level. On CIFAR-2D, we test a 2D version of 𝖧𝗒𝖾𝗇𝖺 {\sf Hyena} long convolution filters in a standard convolutional architecture, which improves on the 2D long convolutional model S4ND ( Nguyen et al., 2022 ) in accuracy with a 8 % 8\% speedup and 25% fewer parameters. See Appendix A.4 for additional vision architectures and training procedure details.

## 5 Discussion and Conclusion

In this work, we introduced an attention-free drop-in replacement to the core building block of many large-scale language models. 𝖧𝗒𝖾𝗇𝖺 {\sf Hyena} operators are a recurrence of gating and implicitly parametrized long convolutions, can be evaluated efficiently in subquadratic time, and can learn in-context on very long sequences. On The Pile , deep stacks of 𝖧𝗒𝖾𝗇𝖺 {\sf Hyena} operators constitute one of the first attention-free, convolutional architectures to match perplexity and downstream performance of Transformers with a significant reduction in training compute. Our promising results at the sub-billion parameter scale suggest that attention may not be all we need, and that simpler subquadratic designs such as 𝖧𝗒𝖾𝗇𝖺 {\sf Hyena} , informed by a set of simple guiding principles and evaluation on mechanistic interpretability benchmarks, may form the basis for efficient large models. We are excited about what new capabilities Hyena opens up as we scale and optimize the inference speed of these models.

## Acknowledgments

We would like to thank Karan Goel, Albert Gu, Avanika Narayan, Khaled Saab, Michael Zhang, Elliot Epstein and Sabri Eyuboglu for helpful discussion and feedback on earlier drafts, and Together Computer and Crusoe for providing the compute used to train models in this paper. We gratefully acknowledge the support of NIH under No. U54EB020405 (Mobilize), NSF under Nos. CCF1763315 (Beyond Sparsity), CCF1563078 (Volume to Velocity), and 1937301 (RTML); US DEVCOM ARL under No. W911NF-21-2-0251 (Interactive Human-AI Teaming); ONR under No. N000141712266 (Unifying Weak Supervision); ONR N00014-20-1-2480: Understanding and Applying Non-Euclidean Geometry in Machine Learning; N000142012275 (NEPTUNE); NXP, Xilinx, LETI-CEA, Intel, IBM, Microsoft, NEC, Toshiba, TSMC, ARM, Hitachi, BASF, Accenture, Ericsson, Qualcomm, Analog Devices, Google Cloud, Salesforce, Total, the HAI-GCP Cloud Credits for Research program, the Stanford Data Science Initiative (SDSI), Department of Defense (DoD) through the National Defense Science and Engineering Graduate Fellowship (NDSEG) Program, and members of the Stanford DAWN project: Facebook, Google, and VMWare. This work is supported by NSF (1651565), AFOSR (FA95501910024), ARO (W911NF-21-1-0125), ONR, DOE (DE-SC0022222), CZ Biohub, and Sloan Fellowship. The U.S. Government is authorized to reproduce and distribute reprints for Governmental purposes notwithstanding any copyright notation thereon. Any opinions, findings, and conclusions or recommendations expressed in this material are those of the authors and do not necessarily reflect the views, policies, or endorsements, either expressed or implied, of NIH, ONR, or the U.S. Government.

## References

Arora et al. (2022) S. Arora, A. Narayan, M. F. Chen, L. J. Orr, N. Guha, K. Bhatia, I. Chami, F. Sala, and C. Ré. Ask me anything: A simple strategy for prompting language models. arXiv preprint arXiv:2210.02441 , 2022.

Basri et al. (2020) R. Basri, M. Galun, A. Geifman, D. Jacobs, Y. Kasten, and S. Kritchman. Frequency bias in neural networks for input of non-uniform density. In International Conference on Machine Learning , pages 685–694. PMLR, 2020.

Black et al. (2021) S. Black, L. Gao, P. Wang, C. Leahy, and S. Biderman. GPT-Neo: Large Scale Autoregressive Language Modeling with Mesh-Tensorflow, Mar. 2021. URL https://doi.org/10.5281/zenodo.5297715 . If you use this software, please cite it using these metadata.

Brown et al. (2020) T. Brown, B. Mann, N. Ryder, M. Subbiah, J. D. Kaplan, P. Dhariwal, A. Neelakantan, P. Shyam, G. Sastry, A. Askell, et al. Language models are few-shot learners. Advances in neural information processing systems , 33:1877–1901, 2020.

Chen (1984) C.-T. Chen. Linear system theory and design . Saunders college publishing, 1984.

Child et al. (2019) R. Child, S. Gray, A. Radford, and I. Sutskever. Generating long sequences with sparse transformers. arXiv preprint arXiv:1904.10509 , 2019.

Cramer (2021) P. Cramer. Alphafold2 and the future of structural biology. Nature structural & molecular biology , 28(9):704–705, 2021.

Cubuk et al. (2020) E. D. Cubuk, B. Zoph, J. Shlens, and Q. V. Le. Randaugment: Practical automated data augmentation with a reduced search space. In Proceedings of the IEEE/CVF conference on computer vision and pattern recognition workshops , pages 702–703, 2020.

Dao et al. (2019) T. Dao, A. Gu, M. Eichhorn, A. Rudra, and C. Ré. Learning fast algorithms for linear transforms using butterfly factorizations. In International conference on machine learning , pages 1517–1527. PMLR, 2019.

Dao et al. (2022a) T. Dao, B. Chen, N. S. Sohoni, A. Desai, M. Poli, J. Grogan, A. Liu, A. Rao, A. Rudra, and C. Ré. Monarch: Expressive structured matrices for efficient and accurate training. In International Conference on Machine Learning , pages 4690–4721. PMLR, 2022a.

Dao et al. (2022b) T. Dao, D. Y. Fu, S. Ermon, A. Rudra, and C. Ré. Flashattention: Fast and memory-efficient exact attention with io-awareness. arXiv preprint arXiv:2205.14135 , 2022b.

Dao et al. (2022c) T. Dao, D. Y. Fu, K. K. Saab, A. W. Thomas, A. Rudra, and C. Ré. Hungry hungry hippos: Towards language modeling with state space models. arXiv preprint arXiv:2212.14052 , 2022c.

Dosovitskiy et al. (2020) A. Dosovitskiy, L. Beyer, A. Kolesnikov, D. Weissenborn, X. Zhai, T. Unterthiner, M. Dehghani, M. Minderer, G. Heigold, S. Gelly, et al. An image is worth 16x16 words: Transformers for image recognition at scale. arXiv preprint arXiv:2010.11929 , 2020.

Elhage et al. (2021) N. Elhage, N. Nanda, C. Olsson, T. Henighan, N. Joseph, B. Mann, A. Askell, Y. Bai, A. Chen, T. Conerly, et al. A mathematical framework for transformer circuits. Transformer Circuits Thread , 2021.

Fukushima and Miyake (1982) K. Fukushima and S. Miyake. Neocognitron: A self-organizing neural network model for a mechanism of visual pattern recognition. In Competition and cooperation in neural nets , pages 267–285. Springer, 1982.

Gao et al. (2020) L. Gao, S. Biderman, S. Black, L. Golding, T. Hoppe, C. Foster, J. Phang, H. He, A. Thite, N. Nabeshima, et al. The pile: An 800gb dataset of diverse text for language modeling. arXiv preprint arXiv:2101.00027 , 2020.

Garg et al. (2022) S. Garg, D. Tsipras, P. Liang, and G. Valiant. What can transformers learn in-context? a case study of simple function classes. arXiv preprint arXiv:2208.01066 , 2022.

Gu et al. (2020) A. Gu, T. Dao, S. Ermon, A. Rudra, and C. Ré. Hippo: Recurrent memory with optimal polynomial projections. Advances in Neural Information Processing Systems , 33:1474–1487, 2020.

Gu et al. (2021) A. Gu, K. Goel, and C. Ré. Efficiently modeling long sequences with structured state spaces. arXiv preprint arXiv:2111.00396 , 2021.

He et al. (2016) K. He, X. Zhang, S. Ren, and J. Sun. Deep residual learning for image recognition. In Proceedings of the IEEE conference on computer vision and pattern recognition , pages 770–778, 2016.

Hendrycks et al. (2019) D. Hendrycks, N. Mu, E. D. Cubuk, B. Zoph, J. Gilmer, and B. Lakshminarayanan. Augmix: A simple data processing method to improve robustness and uncertainty. arXiv preprint arXiv:1912.02781 , 2019.

Hoffmann et al. (2022) J. Hoffmann, S. Borgeaud, A. Mensch, E. Buchatskaya, T. Cai, E. Rutherford, D. d. L. Casas, L. A. Hendricks, J. Welbl, A. Clark, et al. Training compute-optimal large language models. arXiv preprint arXiv:2203.15556 , 2022.

Huang et al. (2016) G. Huang, Y. Sun, Z. Liu, D. Sedra, and K. Q. Weinberger. Deep networks with stochastic depth. In European conference on computer vision , pages 646–661. Springer, 2016.

Kitaev et al. (2020) N. Kitaev, Ł. Kaiser, and A. Levskaya. Reformer: The efficient transformer. arXiv preprint arXiv:2001.04451 , 2020.

LeCun et al. (1998) Y. LeCun, L. Bottou, Y. Bengio, and P. Haffner. Gradient-based learning applied to document recognition. Proceedings of the IEEE , 86(11):2278–2324, 1998.

Li et al. (2015) Y. Li, H. Yang, E. R. Martin, K. L. Ho, and L. Ying. Butterfly factorization. Multiscale Modeling & Simulation , 13(2):714–732, 2015.

Li et al. (2022) Y. Li, T. Cai, Y. Zhang, D. Chen, and D. Dey. What makes convolutional models great on long sequence modeling? arXiv preprint arXiv:2210.09298 , 2022.

Li et al. (2020) Z. Li, N. Kovachki, K. Azizzadenesheli, B. Liu, K. Bhattacharya, A. Stuart, and A. Anandkumar. Fourier neural operator for parametric partial differential equations. arXiv preprint arXiv:2010.08895 , 2020.

Liang et al. (2022) P. Liang, R. Bommasani, T. Lee, D. Tsipras, D. Soylu, M. Yasunaga, Y. Zhang, D. Narayanan, Y. Wu, A. Kumar, et al. Holistic evaluation of language models. arXiv preprint arXiv:2211.09110 , 2022.

Massaroli et al. (2020) S. Massaroli, M. Poli, J. Park, A. Yamashita, and H. Asama. Dissecting neural odes. Advances in Neural Information Processing Systems , 33:3952–3963, 2020.

Mehta et al. (2022) H. Mehta, A. Gupta, A. Cutkosky, and B. Neyshabur. Long range language modeling via gated state spaces. arXiv preprint arXiv:2206.13947 , 2022.

Mildenhall et al. (2021) B. Mildenhall, P. P. Srinivasan, M. Tancik, J. T. Barron, R. Ramamoorthi, and R. Ng. Nerf: Representing scenes as neural radiance fields for view synthesis. Communications of the ACM , 65(1):99–106, 2021.

Nguyen et al. (2022) E. Nguyen, K. Goel, A. Gu, G. W. Downs, P. Shah, T. Dao, S. A. Baccus, and C. Ré. S4nd: Modeling images and videos as multidimensional signals using state spaces. arXiv preprint arXiv:2210.06583 , 2022.

Olsson et al. (2022) C. Olsson, N. Elhage, N. Nanda, N. Joseph, N. DasSarma, T. Henighan, B. Mann, A. Askell, Y. Bai, A. Chen, et al. In-context learning and induction heads. arXiv preprint arXiv:2209.11895 , 2022.

Oppenheim et al. (1997) A. V. Oppenheim, A. S. Willsky, S. H. Nawab, and J.-J. Ding. Signals and systems , volume 2. Prentice hall Upper Saddle River, NJ, 1997.

Paperno et al. (2016) D. Paperno, G. Kruszewski, A. Lazaridou, Q. N. Pham, R. Bernardi, S. Pezzelle, M. Baroni, G. Boleda, and R. Fernández. The lambada dataset: Word prediction requiring a broad discourse context. arXiv preprint arXiv:1606.06031 , 2016.

Peng (2021) B. Peng. RWKV-LM, 8 2021. URL https://github.com/BlinkDL/RWKV-LM .

Polyak and Juditsky (1992) B. T. Polyak and A. B. Juditsky. Acceleration of stochastic approximation by averaging. SIAM journal on control and optimization , 30(4):838–855, 1992.

Power et al. (2022) A. Power, Y. Burda, H. Edwards, I. Babuschkin, and V. Misra. Grokking: Generalization beyond overfitting on small algorithmic datasets. arXiv preprint arXiv:2201.02177 , 2022.

Radford et al. (2022) A. Radford, J. W. Kim, T. Xu, G. Brockman, C. McLeavey, and I. Sutskever. Robust speech recognition via large-scale weak supervision. arXiv preprint arXiv:2212.04356 , 2022.

Rae et al. (2019) J. W. Rae, A. Potapenko, S. M. Jayakumar, C. Hillier, and T. P. Lillicrap. Compressive transformers for long-range sequence modelling. arXiv preprint , 2019. URL https://arxiv.org/abs/1911.05507 .

Romero et al. (2021a) D. W. Romero, R.-J. Bruintjes, J. M. Tomczak, E. J. Bekkers, M. Hoogendoorn, and J. C. van Gemert. Flexconv: Continuous kernel convolutions with differentiable kernel sizes. arXiv preprint arXiv:2110.08059 , 2021a.

Romero et al. (2021b) D. W. Romero, A. Kuzina, E. J. Bekkers, J. M. Tomczak, and M. Hoogendoorn. Ckconv: Continuous kernel convolution for sequential data. arXiv preprint arXiv:2102.02611 , 2021b.

Ronneberger et al. (2015) O. Ronneberger, P. Fischer, and T. Brox. U-net: Convolutional networks for biomedical image segmentation. In International Conference on Medical image computing and computer-assisted intervention , pages 234–241. Springer, 2015.

Roy et al. (2021) A. Roy, M. Saffar, A. Vaswani, and D. Grangier. Efficient content-based sparse attention with routing transformers. Transactions of the Association for Computational Linguistics , 9:53–68, 2021.

Schlag et al. (2021) I. Schlag, K. Irie, and J. Schmidhuber. Linear transformers are secretly fast weight programmers. In International Conference on Machine Learning , pages 9355–9366. PMLR, 2021.

Selesnick and Burrus (2017) I. W. Selesnick and C. S. Burrus. Fast convolution and filtering. In The Digital Signal Processing Handbook , pages 8–1. CRC Press, 2017.

Sitzmann et al. (2020) V. Sitzmann, J. N. Martel, A. W. Bergman, D. B. Lindell, and G. Wetzstein. Implicit neural representations with periodic activation functions. arXiv preprint arXiv:2006.09661 , 2020.

Szegedy et al. (2016) C. Szegedy, V. Vanhoucke, S. Ioffe, J. Shlens, and Z. Wojna. Rethinking the inception architecture for computer vision. In Proceedings of the IEEE conference on computer vision and pattern recognition , pages 2818–2826, 2016.

Tu et al. (2022) Z. Tu, H. Talebi, H. Zhang, F. Yang, P. Milanfar, A. Bovik, and Y. Li. Maxvit: Multi-axis vision transformer. arXiv preprint arXiv:2204.01697 , 2022.

Vaswani et al. (2017) A. Vaswani, N. Shazeer, N. Parmar, J. Uszkoreit, L. Jones, A. N. Gomez, Ł. Kaiser, and I. Polosukhin. Attention is all you need. In Advances in neural information processing systems , pages 5998–6008, 2017.

Wang et al. (2019) A. Wang, Y. Pruksachatkun, N. Nangia, A. Singh, J. Michael, F. Hill, O. Levy, and S. Bowman. Superglue: A stickier benchmark for general-purpose language understanding systems. Advances in neural information processing systems , 32, 2019.

Wang et al. (2020) S. Wang, B. Z. Li, M. Khabsa, H. Fang, and H. Ma. Linformer: Self-attention with linear complexity. arXiv preprint arXiv:2006.04768 , 2020.

Yuan et al. (2021) L. Yuan, Y. Chen, T. Wang, W. Yu, Y. Shi, Z.-H. Jiang, F. E. Tay, J. Feng, and S. Yan. Tokens-to-token vit: Training vision transformers from scratch on imagenet. In Proceedings of the IEEE/CVF international conference on computer vision , pages 558–567, 2021.

Yun et al. (2019) S. Yun, D. Han, S. J. Oh, S. Chun, J. Choe, and Y. Yoo. Cutmix: Regularization strategy to train strong classifiers with localizable features. In Proceedings of the IEEE/CVF international conference on computer vision , pages 6023–6032, 2019.

Zhai et al. (2021) S. Zhai, W. Talbott, N. Srivastava, C. Huang, H. Goh, R. Zhang, and J. Susskind. An attention free transformer. arXiv preprint arXiv:2105.14103 , 2021.

Zhang et al. (2017) H. Zhang, M. Cisse, Y. N. Dauphin, and D. Lopez-Paz. mixup: Beyond empirical risk minimization. arXiv preprint arXiv:1710.09412 , 2017.

Zhang et al. (2022) Y. Zhang, A. Backurs, S. Bubeck, R. Eldan, S. Gunasekar, and T. Wagner. Unveiling transformers with lego: a synthetic reasoning task. arXiv preprint arXiv:2206.04301 , 2022.

Zhong et al. (2020) Z. Zhong, L. Zheng, G. Kang, S. Li, and Y. Yang. Random erasing data augmentation. In Proceedings of the AAAI conference on artificial intelligence , volume 34, pages 13001–13008, 2020.

Hyena Hierarchy Supplementary Material

## Appendix A Experimental Details

An implementation of 𝖧𝗒𝖾𝗇𝖺 {\sf Hyena} can be found at this link .

### A.1 Mechanistic Design Synthetic Benchmarks

Our synthetic reasoning are inspired by mechanistic interpretability ( Elhage et al., 2021 ) , in-context learning (ICL) ( Garg et al., 2022 ) and language model benchmarking ( Liang et al., 2022 ) research. The evaluation revolves around 4 4 main tasks: • Associative recall: Each string is produced by concatenating key-value tuples from a different random dictionary. This test verifies whether a model is able to extract right value given a key as prompt, effectively applying a data-controlled shift (delay).

• Majority voting and counting: Testing if a model can densely activate its data-controlled matrix i.e., through many non-zero entries (consider the string ’ a a a a a a a a a a b → \rightarrow a ’).

• ICL of linear functions: Verifying whether a model can perform ICL on real-valued inputs. Prompts are generated as x 1 , w k ​ x 1 , … , x n → w k ​ x n x_{1},w^{k}x_{1},\dots,x_{n}\rightarrow w^{k}x_{n} , where both x k x_{k} and w k ∈ R n o w^{k}\in R^{n_{o}} are sampled from a normal distribution.

• Arithmetic: Basic capability check.

For each task, we train models using the hyperparameters shown in Table A.1 . We consider increasing settings of difficulty controlled by sequence length, spanning values 1024 , 2048 , 4098 , 8196 , 16392 , 32784 , 65568 , 131136 1024,2048,4098,8196,16392,32784,65568,131136 and vocabulary sizes 10 , 20 , 30 , 40 10,20,30,40 . For ICL of functions, we vary instead the dimension n o n_{o} .

Note that for associative recall on longer sequences, multiple copies of key-value tuples appear in the prompt. To see this, consider how likely it is to sample multiple copies of a particular key-value pair with a vocabulary size of 40 40 , in order to form a sequence of 100 100 k characters. Models capable of looking further back in the sequence effectively see more data, and can solve challenging versions of the in-context learning task. Increasing the vocabulary size has the increasing the average distance between instances of the same key-value pair in each prompt, highlighting performance gaps between different approaches.

#### Long convolution comparisons:

We compare different convolution parametrizations, embedding them in an order 2 2 𝖧𝗒𝖾𝗇𝖺 {\sf Hyena} operator. All convolutions are applied separately to input channels (referred to as single-input single-output (SISO) in signal processing, or depthwise in other machine learning contexts).

• Conv1d: Explicit convolutions (regular convolution layers with fixed filter size). We use a fixed filter size of 64 64 , to match parameters of the other approaches.

• FNO: Filters parametrized explicitly in the frequency-domain ( Li et al., 2020 ) . We set the number of modes to 64 64 .

• H3: Implicit parametrization using state-space models (SSMs), and in particular the standard S4 ( Gu et al., 2021 ) . We set the state dimension to 64 64 .

• TransferFunc: Implicit parametrization via transfer functions, a classical system-theoretic generalization of SSMs. Transfer functions are defined by a ratio of polynomials (we parametrize the coefficients, and evaluate the polynomials efficiently via FFTs). We set the order to 64 64 .

• CKConv: Implicit parametrization using 𝖥𝖥𝖭 \sf FFN s ( Romero et al., 2021b ) .

• item 𝖧𝗒𝖾𝗇𝖺 {\sf Hyena} : Combination of implicit parametrizations via 𝖥𝖥𝖭 \sf FFN s (with exponential decay modulation as shown in Figure 3.1 ), and short explicit filters.

CKConv and 𝖧𝗒𝖾𝗇𝖺 {\sf Hyena} use the same size of 𝖥𝖥𝖭𝗌 {\sf FFNs} (width 32 32 to match in parameters).

In Table A.2 , we report additional results on the challenging setting of sequence length 131072 131072 and vocabulary size 30 30 . Implicit parametrizations of convolutions outperform explicit parametrizations on associative recall, with CKConv and 𝖧𝗒𝖾𝗇𝖺 {\sf Hyena} greatly improving on the ability to extract the right key, value relations from different inputs. In Appendix C , we discuss how results on our synthetic tasks can be indicative of performance at a larger scale.

#### Operator comparisons:

We compare different models on the same associative recall task, using hyperparameters in Table A.1 . 𝖧𝗒𝖾𝗇𝖺 {\sf Hyena} uses our filter parametrization with decay windowing for long convolutions, and short explicit convolutions of size 3 3 after the dense input projections. All other models use defaults from their largest scale experiment, while keeping the size to 2 2 layers and width 64 64 .

#### A note on Transformer performance

Transformers can solve associative recall tasks with longer sequences, provided the length does not prevent them from fitting in memory, and enough examples are present in the training data. In all our experiments, we keep the number of samples fixed ( 2000 2000 ), a regime where Transformers struggle to find the generalizing solution (see Table A.2 ).

For shorter sequences (see Appendix C ), Transformers solve the task easily even with limited data, comparably to Hyena .

More broadly, these different properties of attention and attention-free token-mixing layers may explain improved performance when they are combined in hybrid architectures ( Dao et al., 2022c ) . The focus on this work has been identifying an architecture capable of performing without attention, which is necessary to tackle domains where long sequences are common. However, when training with shorter sequences (up to 8 8 k), if final downstream performance is the only metric of interest, improved results can be obtained by hybridizing our models similarly to H3 ( Dao et al., 2022c ) .

### A.2 Language Modeling

#### WikiText103:

We train 125 125 M parameter models on WikiText103 and compare perplexity to Transformers, hybrid models such as H3 ( Dao et al., 2022c ) , and other variants of subquadratic attention. All models use the same GPT2 tokenizer with vocabulary size 50257 50257 . We test order 3 3 𝖧𝗒𝖾𝗇𝖺 {\sf Hyena} with our proposed filter parametrization for two long convolutions, and a shorter explicit convolution on the third. We also consider 𝖧𝗒𝖾𝗇𝖺 {\sf Hyena} (slim) that are 1.5 1.5 x deeper than Transformers ( 12 12 versus 18 18 layers), with width multiplier of the FFNs set to 2 2 . We find trading-off width for depth to be generally favourable. These modifications are made possible by the reduction in overall FLOPs of Hyena operators compared to self-attention, in particular non-parametric FLOPs which include materialization of the attention matrix, application of softmax, and matrix-value reduction.

#### The Pile:

We follow a same procedure and train 125 125 M and 355 355 M-sized models on The Pile ( Gao et al., 2020 ) . Hyperparameters are reported in Table A.3 . Hyperparameters for 355 355 M are the same beyond a reduction in peak learning rate to 4 ⋅ 10 − 4 4\cdot 10^{-4} . For larger models ( 1.3 1.3 B), we set a learning rate of 2.2 ⋅ 10 − 4 2.2\cdot 10^{-4} .

We perform three experiments for each model type and size, and train for 5 , 10 , 15 5,10,15 billion tokens at a sequence length 2024 2024 and global batch size 256 256 . All models are trained on a single node of 8 8 A ​ 100 A100 80 80 GB GPUs. We use order 2 2 𝖧𝗒𝖾𝗇𝖺 {\sf Hyena} s, with the same architectural considerations described above for WikiText103 . In addition to our data scaling experiments at 5 5 , 10 10 and 15 15 billion tokens, we provide preliminary results for models at the 1.3 1.3 B parameter scale ( 10.8 10.8 perplexity after 5 5 billion tokens), and train a 153 153 M model ( 130 130 billion tokens), reaching a perplexity of 9.8 9.8 . The 153 153 M is the same used in our downstream evaluation on SuperGLUE.

Training hyperparameters match those of standard GPT training pipelines, and are thus likely suboptimal for new attention-free architectures such as Hyena . We run some preliminary experiments and find that e.g., some modifications to the learning rate schedule, currently involving linear warmup and cosine decay, to improve perplexity at convergence of Hyena models (we recommend slightly lower learning rates for Hyena models compared to GPT of a similar size). Despite these findings, we use standard GPT hyperparameters for both GPT and Hyena .

#### PG-19

We also report results of additional training runs on other datasets. We train a 𝖧𝗒𝖾𝗇𝖺 {\sf Hyena} 153 153 M model on the standard PG-19 long-range corpus ( Rae et al., 2019 ) , with a context length of 16 16 k tokens, reaching a test perplexity of 14.6 14.6 (using the standard GPT2 tokenizer) in 8 8 epochs.

#### Architectures

Architectural hyperparameters for Hyena are shown in Table A.4 . We use sine as an activation function for the FFN of Hyena filters.

#### FLOP computation

The number of floating point operations (FLOPs) reported in the main text are computed using the same strategy as in ( Hoffmann et al., 2022 ) . For GPT, we do not use the approximation, opting instead for the more accurate formula based on FLOP counts of individual layers. In the case of Hyena , FLOPs are computed using the same method, except attention layers are replaced by: i. Projections: order × \times d_model × \times d_model × \times seq_len.

ii. Short conv on projections: order × \times d_model × \times seq_len × \times filter_len (usually 3 3 ).

iii. FFTConv: 5 5 × \times (order - 1) × \times d_model × \times log ⁡ ( seq_len ) \log(\text{seq\_len}) × \times seq_len.

iv. Output: d_model × \times d_model × \times seq_len.

with a leading factor 2 2 to account for both additions and multiplications.

### A.3 Downstream Evaluation

#### SuperGLUE:

We evaluate models on the SuperGLUE ( Wang et al., 2019 ) with the parsing pipeline of ( Arora et al., 2022 ) . For all tasks except WIC, CB and BoolQ, we generate a response using greedy decoding, then check for the gold label. WIC, CB and BoolQ use logit scoring instead of generation.

#### Models

The models considered are the open-source checkpoint of GPTNeo 125 125 M trained for 300 300 B tokens The Pile , and the RWKV-v4 169 169 M checkpoint trained for 332 332 B tokens on The Pile . Hyena is a 153 153 M model trained for 137 137 B tokens on The Pile .

#### LAMBADA:

We evaluate 𝖧𝗒𝖾𝗇𝖺 {\sf Hyena} on the LAMBADA ( Paperno et al., 2016 ) task. We apply a stop word filter and check whether predictions for all tokens corresponding to the last word agree with the ground truth. The small 𝖧𝗒𝖾𝗇𝖺 {\sf Hyena} model trained on 137 137 B tokens reaches 44.64 % 44.64\% accuracy.

### A.4 Image Classification

#### a

ImageNet: We use ImageNet-1k which consists of 1000 classes and 1.3M images and train from scratch with no outside data on 8 Nvidia A100 GPUs. In our ViT benchmark, we swap the attention layers with the Hyena operator defined in our language experiments, and remove the class token and positional embeddings, similar to S4ND ( Nguyen et al., 2022 ) . The parameter count is kept similar at 87M ViT-B (base) vs 88M Hyena-ViT. The training procedure from T2T-ViT ( Yuan et al., 2021 ) is used, including augmentations such as RandAugment ( Cubuk et al., 2020 ) , Mixup ( Zhang et al., 2017 ) , and AugMix ( Hendrycks et al., 2019 ) . See table A.5 for hyperparameter settings used.

#### CIFAR-10:

We use CIFAR-10 in sequential and 2D experiments. For sequential, we use the Hyena operator defined in our language tasks and compare with an S4 model ( Gu et al., 2021 ) of the same size by swapping layers in the residual blocks. In 2D, we learn Hyena filters (in both x x and y y dimensions) that are equal to the size of the input shape, and forgo the gating mechanism from our language experiments. We window (i.e., apply a soft mask spatially to) the Hyena filters with a decay term. The rate of decay varies across channels, ensuring different sizes of the filters at initialization. We compare with another implicit 2D convolution, S4ND ( Nguyen et al., 2022 ) , by swapping the model layers with the 2D Hyena filters. The "isometric" model consists of 4 residual blocks of model dimension 128. We use basic image augmentations, 0.1 dropout, 0.03 weight decay and train for 100 epochs using a Nvidia T4 GPU.

## Appendix B Theoretical Results and Details

### B.1 Proofs

#### Proof of Proposition 3.1

###### Proof.

A discrete L L -by- L L operator is causal if it is lower triangular, i.e., when there is no leakage of future input information to the output. The 𝖧𝗒𝖾𝗇𝖺 {\sf Hyena} operator 𝖧 \mathsf{H} is the product of alternating diagonal and Toeplitz matrices. Thus, if all the Toeplitz matrices 𝖲 h n \mathsf{S}_{h}^{n} are lower triangular then 𝖧 \mathsf{H} is lower triangular. In turn, each 𝖲 h n \mathsf{S}_{h}^{n} is lower triangular if and only if the filter h h is causal, concluding the proof. ∎

### B.2 Analysis of Data-Controlled Mechanisms

We discuss the surrogate attention mechanism of Hyena - 2 2 : q , k , v ↦ y q,k,v\mapsto y : z t \displaystyle z_{t} = k t ​ ( φ ∗ v ) t \displaystyle=k_{t}(\varphi*v)_{t} (8) y t \displaystyle y_{t} = q t ​ ( ψ ∗ z ) t \displaystyle=q_{t}(\psi*z)_{t} If φ \varphi and ψ \psi are convolutions parametrized via state-space models (SSMs), the above resembles the H3 mechanism ( Dao et al., 2022c ) . We investigate the effect of the convolutional kernels φ \varphi and ψ \psi on the attention layer. We start by introducing a matrix representation of the layer, and we isolate the attention matrix 𝖠 φ ψ ​ ( q , k ) \mathsf{A}_{\varphi}^{\psi}(q,k) such that y \displaystyle y = 𝖠 φ ψ ​ ( q , k ) ​ v . \displaystyle=\mathsf{A}_{\varphi}^{\psi}(q,k)v. (9)

#### Isolating the surrogate attention matrix

In the case of length- L L discrete sequences z t \displaystyle z_{t} = k t ​ ∑ m = 0 L − 1 φ t − m ​ v m \displaystyle=k_{t}\sum_{m=0}^{L-1}\varphi_{t-m}v_{m} (10) y t \displaystyle y_{t} = q t ​ ∑ m = 0 L − 1 ψ t − m ​ z m \displaystyle=q_{t}\sum_{m=0}^{L-1}\psi_{t-m}z_{m} Therefore we can rewrite ( 8 ) as y t \displaystyle y_{t} = q t ​ ∑ m = 0 L − 1 ψ t − m ​ k m ​ ∑ n = 0 L − 1 φ m − n ​ v n \displaystyle=q_{t}\sum_{m=0}^{L-1}\psi_{t-m}k_{m}\sum_{n=0}^{L-1}\varphi_{m-n}v_{n} (11) = q t ​ ∑ m = 0 L − 1 ∑ n = 0 L − 1 ψ t − m ​ k m ​ φ m − n ​ v n \displaystyle=q_{t}\sum_{m=0}^{L-1}\sum_{n=0}^{L-1}\psi_{t-m}k_{m}\varphi_{m-n}v_{n} Move ψ , k inside inner sum \displaystyle\text{Move $\psi$, $k$ inside inner sum} = q t ​ ∑ n = 0 L − 1 ∑ m = 0 L − 1 ψ t − m ​ k m ​ φ m − n ​ v n \displaystyle=q_{t}\sum_{n=0}^{L-1}\sum_{m=0}^{L-1}\psi_{t-m}k_{m}\varphi_{m-n}v_{n} Index shift \displaystyle\text{Index shift} = ∑ n = 0 L − 1 q t ​ ∑ m = 0 L − 1 ψ t − m ​ k m ​ φ m − n ​ v n \displaystyle=\sum_{n=0}^{L-1}q_{t}\sum_{m=0}^{L-1}\psi_{t-m}k_{m}\varphi_{m-n}v_{n} And we can define the surrogate attention matrix 𝖠 φ ψ ​ ( q , k ) \mathsf{A}_{\varphi}^{\psi}(q,k) t , t ′ \displaystyle{}_{t,t^{\prime}} = q t ​ ∑ m = 0 L − 1 ψ t − m ​ k m ​ φ m − t ′ . \displaystyle=q_{t}\sum_{m=0}^{L-1}\psi_{t-m}k_{m}\varphi_{m-t^{\prime}}. (12)

#### Operator decomposition of the surrogate attention matrix

We can decompose the linear map v ↦ y ; y = 𝖠 φ ψ ​ ( q , k ) ​ v v\mapsto y;~y=\mathsf{A}_{\varphi}^{\psi}(q,k)v into a sequence of factors, each dependent on a projection of the input 𝖠 φ ψ ​ ( q , k ) = 𝖠 ψ ​ ( q ) ​ 𝖠 φ ​ ( k ) \mathsf{A}_{\varphi}^{\psi}(q,k)=\mathsf{A}^{\psi}(q)\mathsf{A}_{\varphi}(k) . Let 𝖣 q \mathsf{D}_{q} and 𝖣 k \mathsf{D}_{k} be the L L -by- L L diagonal matrices whose respective main diagonal entries are the respective entries of q q and k k . Then, we have that 𝖠 ψ ​ ( q ) \displaystyle\mathsf{A}^{\psi}(q) = 𝖣 q 𝖲 ψ , 𝖣 q = diag ( q ) , \displaystyle=\mathsf{D}_{q}\mathsf{S}_{\psi},\qquad\mathsf{D}_{q}=\diag(q), (16) 𝖠 φ ​ ( k ) \displaystyle\mathsf{A}_{\varphi}(k) = 𝖣 k 𝖲 φ , 𝖣 k = diag ( k ) . \displaystyle=\mathsf{D}_{k}\mathsf{S}_{\varphi},\qquad\mathsf{D}_{k}=\diag(k). The matrix has been decomposed into two terms 𝖠 ψ ​ ( q ) \mathsf{A}^{\psi}(q) and 𝖠 φ ​ ( k ) \mathsf{A}_{\varphi}(k) constructed by multiplying the diagonal matrices 𝖣 q \mathsf{D}_{q} and 𝖣 k \mathsf{D}_{k} with the Toeplitz matrices 𝖲 ψ \mathsf{S}_{\psi} and 𝖲 φ \mathsf{S}_{\varphi} . 𝖲 ψ \mathsf{S}_{\psi} and 𝖲 φ \mathsf{S}_{\varphi} are the kernels of the convolution operators with filter’s impulse responses ψ \psi and φ \varphi respectively. In the current applications of interest, ψ \psi and φ \varphi are chosen to be causal, i.e. ψ ⁡ [ t ] = 0 ​ for ​ t < 0 \psi[t]=0\text{ for }t<0 and φ ⁡ [ t ] = 0 ​ for ​ t < 0 \varphi[t]=0\text{ for }t<0 . This results in 𝖲 ψ \mathsf{S}_{\psi} and 𝖲 φ \mathsf{S}_{\varphi} to be lower triangular matrices 𝖲 ψ = [ ψ 0 0 ⋯ 0 ψ 1 ψ 0 ⋯ 0 ⋱ ⋱ ψ L − 1 ψ L − 2 ⋯ ψ 0 ] , 𝖲 φ = [ φ 0 0 ⋯ 0 φ 1 φ 0 ⋯ 0 ⋱ ⋱ φ L − 1 φ L − 2 ⋯ φ 0 ] . \mathsf{S}_{\psi}=\begin{bmatrix}\psi_{0}&0&\cdots&0\\ \psi_{1}&\psi_{0}&\cdots&0\\ \vdots&\ddots&\ddots&\vdots\\ \psi_{L-1}&\psi_{L-2}&\cdots&\psi_{0}\end{bmatrix},\qquad\mathsf{S}_{\varphi}=\begin{bmatrix}\varphi_{0}&0&\cdots&0\\ \varphi_{1}&\varphi_{0}&\cdots&0\\ \vdots&\ddots&\ddots&\vdots\\ \varphi_{L-1}&\varphi_{L-2}&\cdots&\varphi_{0}\end{bmatrix}. (17) The surrogate attention matrix is then given by 𝖠 φ ψ ​ ( q , k ) = 𝖣 q ​ 𝖲 ψ ​ 𝖣 k ​ 𝖲 φ \mathsf{A}_{\varphi}^{\psi}(q,k)=\mathsf{D}_{q}\mathsf{S}_{\psi}\mathsf{D}_{k}\mathsf{S}_{\varphi} (18) We can expand the matrix multiplications in ( 16 ) in the case of causal filters φ \varphi and ψ \psi as 𝖣 q [ q 0 q 1 ⋱ q L − 1 ] ​ 𝖲 ψ [ ψ 0 ψ 1 ψ 0 ⋱ ⋱ ψ L − 1 ψ L − 2 ⋯ ψ 0 ] ​ 𝖣 k [ k 0 k 1 ⋱ k L − 1 ] ​ 𝖲 φ [ φ 0 φ 1 φ 0 ⋱ ⋱ φ L − 1 φ L − 2 ⋯ φ 0 ] \displaystyle\underset{\begin{bmatrix}q_{0}&&&\\ &q_{1}&&\\ &&\ddots&\\ &&&q_{L-1}\end{bmatrix}}{\displaystyle\mathsf{D}_{q}}\underset{\begin{bmatrix}\psi_{0}&&&\\ \psi_{1}&\psi_{0}&&\\ \vdots&\ddots&\ddots&\\ \psi_{L-1}&\psi_{L-2}&\cdots&\psi_{0}\end{bmatrix}}{\displaystyle\mathsf{S}_{\psi}}\underset{\begin{bmatrix}k_{0}&&&\\ &k_{1}&&\\ &&\ddots&\\ &&&k_{L-1}\end{bmatrix}}{\displaystyle\mathsf{D}_{k}}\underset{\begin{bmatrix}\varphi_{0}&&&\\ \varphi_{1}&\varphi_{0}&&\\ \vdots&\ddots&\ddots&\\ \varphi_{L-1}&\varphi_{L-2}&\cdots&\varphi_{0}\end{bmatrix}}{\displaystyle\mathsf{S}_{\varphi}} (19) = [ q 0 ​ ψ 0 q 1 ​ ψ 1 q 1 ​ ψ 0 ⋱ ⋱ q L − 1 ​ ψ L − 1 q L − 1 ​ ψ L − 2 ⋯ q L − 1 ​ ψ 0 ] 𝖠 ψ ​ ( q ) ​ [ k 0 ​ φ 0 k 1 ​ φ 1 k 1 ​ φ 0 ⋱ ⋱ k L − 1 ​ φ L − 1 k L − 1 ​ φ L − 2 ⋯ k L − 1 ​ φ 0 ] 𝖠 φ ​ ( k ) \displaystyle\underset{\displaystyle\mathsf{A}_{\psi}(q)}{=\begin{bmatrix}q_{0}\psi_{0}&&&\\ q_{1}\psi_{1}&q_{1}\psi_{0}&&\\ \vdots&\ddots&\ddots&\\ q_{L-1}\psi_{L-1}&q_{L-1}\psi_{L-2}&\cdots&q_{L-1}\psi_{0}\end{bmatrix}}\underset{\displaystyle\mathsf{A}_{\varphi}(k)}{\begin{bmatrix}k_{0}\varphi_{0}&&&\\ k_{1}\varphi_{1}&k_{1}\varphi_{0}&&\\ \vdots&\ddots&\ddots&\\ k_{L-1}\varphi_{L-1}&k_{L-1}\varphi_{L-2}&\cdots&k_{L-1}\varphi_{0}\end{bmatrix}}

## Appendix C Discussion and Additional Results

#### Vocabulary size scaling

Table C.1 showcases interesting correlation between associative recall performance for varying vocabulary sizes and loss on the The Pile . In this case, we fix sequence length for associative recall to be 2048 2048 , the same sequence length used to train all models on the The Pile .

We observe a similar phenomenon on other slices of tasks from our mechanistic design benchmarks, indicating that it may be possible to derive predictive laws for performance at scale, based on fast experimentation on synthetic tasks with models of 1 1 or 2 2 layers. Surprisingly, performance on our language synthetics appears to be further linked to performance as attention replacement in other domains (Appendix A.4 for results on image classification).

#### Single layer recall

All experiments on our synthetic tasks default to 2 2 layer models. We choose 2 2 as it is the canonical number for mechanistic analysis of Transformers ( Elhage et al., 2021 ) based on circuits . Interestingly, a single layer of Hyena (width 64 64 ) is capable of performing associative recall, solving the task completely even in the challenging setting with vocabulary size 40 40 . Reverse engineering exactly how the single Hyena operator is able to perform recall is left for future work.

### C.1 Learning Arithmetic

We showcase an additional task in our mechanistic design benchmark: learning arithmetic. We train Hyena models of increasing depth ( 1 1 , 2 2 and 3 3 layers) on a dataset of D n D_{n} -digit addition. As an example, a 3 3 -digit addition input sample is given by the sequence 𝟷 , 𝟸 , 𝟹 , 𝟿 , 𝟻 , 𝟺 , 𝟷 , 𝟶 , 𝟽 , 𝟽 {\tt 1,2,3,9,5,4,1,0,7,7} where the first 6 6 digits contain the two 3 3 digits numbers to add, and the last 4 4 the result. Our models are optimized using standard autoregressive training i.e., predicting the next token, since they are causal. In particular, we optimize models to learn a map x ↦ y x\mapsto y where x x is the original prompt without the last element, and y y equal to x x shifted right by one position. We mask the first 2 ​ D n − 1 2D_{n}-1 elements of the loss for each sequence since they contain predictions for addends and not results.

We report results in Figure C.1 . A single layer of Hyena is able to learn to perform addition with up to 4 4 digits. Longer numbers require deeper models. In our experiments, alternative architectures such as AFT-conv struggle to learn arithmetic, signaling a cap in capability.

## Appendix D Samples and Visualizations

### D.1 Hyena Matrices

We provide visualizations of attention and 𝖧𝗒𝖾𝗇𝖺 {\sf Hyena} matrices activated by test strings. In D.1 , D.2 , we compare GPTNeo ( Black et al., 2021 ) attention matrices with Hyena matrices extracted by our pre-trained small Hyena model. In D.3 and D.4 , we provide additional Hyena matrices for the 355 355 M model, activated by test strings of different length.

For attention, we visualize the raw post-softmax matrix. For 𝖧𝗒𝖾𝗇𝖺 {\sf Hyena} matrices, we plot the (element-wise) absolute value of 𝖧 ⁡ ( u ) \mathsf{H}(u) : 𝖧 ⁡ ( u ) \displaystyle\mathsf{H}(u) = 𝖣 x N 𝖲 h N ⋯ 𝖣 x 2 𝖲 h 2 𝖣 x 1 𝖲 h 1 \displaystyle=\mathsf{D}_{x}^{N}\mathsf{S}_{h}^{N}\cdots\mathsf{D}_{x}^{2}\mathsf{S}_{h}^{2}\mathsf{D}_{x}^{1}\mathsf{S}_{h}^{1} 𝖧 ^ ​ ( u ) i ​ j \displaystyle\hat{\mathsf{H}}(u)_{ij} = | 𝖧 ​ ( u ) i ​ j | \displaystyle=\left|\mathsf{H}(u)_{ij}\right| Since Hyena does not normalize the entries of its matrices with e.g., softmax, there are notable differences with attention: (1) the entries of 𝖧 ⁡ ( u ) \mathsf{H}(u) can be either positive and negative, and (2) the magnitude is unconstrained. We observe the magnitude of matrices in pre-trained Hyena models to be around 10 − 3 10^{-3} .

### D.2 Hyena Filters

Figure D.5 provides a visualization of Hyena long convolution filters at initialization and after training to completion on The Pile .

We find a substantial performance difference (up to 5 % 5\% perplexity) between initialization schemes. If the filters at initialization are excessively smooth (see Appendix D.3 for a discussion of positional encoding and activation), the model finds a worse solution and takes longer to converge. Further, we observe initialization schemes that regularize filters towards typical filters learned at convergence to decrease performance. These observations are in line with performance gaps between convolution parametrization schemes discussed in main text and Appendix A.1 . In particular, the performance improvements obtained via Hyena filters could be due to easier optimization in the space of convolutional filters.

At convergence, Hyena learns a collection of lower-order filters with a similar structure, which can be exploited to further speed up inference after training.

### D.3 Positional Encoding and Filters Initialization

The positional encoding chosen for the 𝖧𝗒𝖾𝗇𝖺 \sf Hyena filters is a truncated complex exponential basis. Specifically, with ρ k ​ ( t ) = e i ​ 2 ​ π ​ k ​ t / L \rho_{k}(t)=e^{i2\pi kt/L} for k = 0 , … ​ K − 1 k=0,\dots K-1 , the positional encoding is defined as a map from ℝ \mathbb{R} to ℝ 2 ​ K + 1 \mathbb{R}^{2K+1} such that 𝖯𝗈𝗌𝗂𝗍𝗂𝗈𝗇𝖺𝗅𝖤𝗇𝖼𝗈𝖽𝗂𝗇𝗀 ⁡ ( t ) = [ t ℜ ​ [ ρ 0 ] ​ ( t ) ⋯ ℜ ​ [ ρ K − 1 ] ​ ( t ) ℑ ​ [ ρ 0 ] ​ ( t ) ⋯ ℑ ​ [ ρ K − 1 ] ​ ( t ) ] {\sf PositionalEncoding}(t)=\begin{bmatrix}t&\mathfrak{R}[\rho_{0}](t)&\cdots&\mathfrak{R}[\rho_{K-1}](t)&\mathfrak{I}[\rho_{0}](t)&\cdots&\mathfrak{I}[\rho_{K-1}](t)\end{bmatrix} where ℜ ⁡ [ ⋅ ] \mathfrak{R}[\cdot] , ℑ ⁡ [ ⋅ ] \mathfrak{I}[\cdot] denote the real and imaginary part of their argument, respectively. In the main text, we use D e = 2 ​ K + 1 D_{e}=2K+1 to denote the size of a positional encoding with K K features. The number of features of the positional encoding has an impact on the filter initialization and training performances. In particular, we show how K K leads to a preconditioning of the spectrum of the filter at initialization. Figures D.6 , D.7 , D.8 display the initialized filters (with no 𝖶𝗂𝗇𝖽𝗈𝗐 \sf Window function) for different values of K K ( { 8 , 32 , 64 } \{8,32,64\} ) for L = 128 L=128 and frequency ω a \omega_{a} of sinusoidal activation σ ⁡ ( ⋅ ) = sin ( ω a ⋅ ) \sigma(\cdot)=\sin(\omega_a \cdot) set to 1. We notice how the choice of K K induces a bias in the modeled frequencies at initialization. Specifically the filters resemble low-pass filters with a cut-off frequency of approximatively 2 ​ K + 1 2K+1 .

This cut-off frequency is strongly related to the smoothness of the filter; as previously mentioned, we empirically observe better training dynamics of filters initialized to be non-smooth, i.e. with a rich high-frequency content. While we can achieve good initializations by increasing K K , this results in larger 𝖥𝖥𝖭 \sf FFN s (its input dimension is 2 ​ K + 1 2K+1 , i.e. the number of positional encoding features) which come with a higher parameter count. A more efficient solution is to increase the frequency ω a \omega_{a} of the sinusoidal activation. Figure D.9 show how with K = 8 K=8 we can cover the full spectrum simply by setting ω a = 10 \omega_{a}=10 .

### D.4 Downstream Examples

#### MultiRC

We report examples of downstream evaluation of small models on the MultiRC question-answering task. We report answers of small Hyena (153M, trained for 130 130 B tokens on The Pile ) and the public checkpoint RWKV-v4 ( Peng, 2021 ) ( 169 169 M, trained for 332 332 B tokens on The Pile ). We select randomized examples with indices being powers of 2 2 . Alignment of Hyena ’s responses to the task format is greatly improved by providing few-shot examples in the prompt, which may be a promising sign for larger models based on the proposed attention-free architecture. Each example shows responses for specific examples in the validation set (example indices are listed at the beginning of each example).

## Instructions for reporting errors

We are continuing to improve HTML versions of papers, and your feedback helps enhance accessibility and mobile support. To report errors in the HTML that will help us improve conversion and rendering, choose any of the methods listed below:

Click the "Report Issue" ( ) button, located in the page header.

Tip: You can select the relevant text first, to include it in your report.

Our team has already identified the following issues . We appreciate your time reviewing and reporting rendering errors we may not have found yet. Your efforts will help us improve the HTML versions for all readers, because disability should not be a barrier to accessing research. Thank you for your continued support in championing open access for all.

Have a free development cycle? Help support accessibility at arXiv! Our collaborators at LaTeXML maintain a list of packages that need conversion , and welcome developer contributions .
