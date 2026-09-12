##### Report GitHub Issue

Content selection saved. Describe the issue below:

# Why Can’t Transformers Learn Multiplication? Reverse-Engineering Reveals Long-Range Dependency Pitfalls

###### Abstract

Language models are increasingly capable, yet still fail at a seemingly simple task of multi-digit multiplication. In this work, we study why, by reverse-engineering a model that successfully learns multiplication via implicit chain-of-thought , and report three findings: (1) Evidence of long-range structure: Logit attributions and linear probes indicate that the model encodes the necessary long-range dependencies for multi-digit multiplication. (2) Mechanism: the model encodes long-range dependencies using attention to construct a directed acyclic graph to ‘‘cache’’ and ‘‘retrieve’’ pairwise partial products. (3) Geometry: the model implements partial products in attention heads by forming Minkowski sums between pairs of digits, and digits are represented using a Fourier basis, both of which are intuitive and efficient representations that the standard fine-tuning model lacks. With these insights, we revisit the learning dynamics of standard fine-tuning and find that the model converges to a local optimum that lacks the required long-range dependencies. We further validate this understanding by introducing an auxiliary loss that predicts the ‘‘running sum’’ via a linear regression probe, which provides an inductive bias that enables the model to successfully learn multi-digit multiplication. In summary, by reverse-engineering the mechanisms of an implicit chain-of-thought model we uncover a pitfall for learning long-range dependencies in Transformers and provide an example of how the correct inductive bias can address this issue. 0 0 footnotetext: Contact: andrewlee@g.harvard.edu, smallyan@uchicago.edu 0 0 footnotetext: Code: https://github.com/ajyl/icot

## 1 Introduction

Large language models demonstrate striking capabilities across reasoning, planning, and tool use. Yet, they also fail on surprisingly simple algorithmic tasks ( Nye et al., 2021 ; Lee et al., 2023 ) . Why do Transformers excel at some tasks, but fail to learn others? One such example is multi-digit multiplication. Despite having billions of parameters, models like Llama-3.2 90B or GPT4 still fail at 4x4-digit multiplication ( Gambardella et al., 2024 ) , 1 1 1 Note that some recent proprietary models that do solve multi-digit multiplication may rely on tool-use. even when explicitly fine-tuned on the task ( Yang et al., 2023 ) . Why do Transformers fail to learn multiplication?

We study these questions by contrasting a standard fine-tuned model (SFT), which fails at multiplication, with a model trained with implicit chain-of-thought (ICoT) ( Deng et al., 2024 ; Deng et al., 2023 ) , which succeeds. ICoT works by providing explicit chain-of-thought tokens during training, but gradually removes them and thus forces the model to internalize intermediate steps in its latent states.

We partially reverse-engineer the ICoT model and uncover several insights. First, unlike the SFT model, the ICoT model learns the correct long-range structure needed for multi-digit multiplication. We provide evidence of this using logit attributions and linear regression probes. Mechanistically , the ICoT model encodes long-range dependencies by organizing its attention into a sparse, binary-tree-like graph, which (i) selects the correct digit pairs to compute partial products and (ii) “caches” these intermediate computations into earlier tokens for later retrieval. Lastly, geometrically , attention heads realize partial products as Minkowski sums of digit embeddings, and represent digits with Fourier bases, yielding a pentagonal prism structure – both of which are intuitive and efficient representations that the SFT model lacks.

With these insights, we revisit the dynamics of standard fine-tuning: under gradient descent and an auto-regressive loss, the model never learns these long-range dependencies, and thus loss plateaus on the middle digits. To confirm our understanding, we introduce a simple fix by introducing an auxiliary loss that supervises the model to predict a “running partial sum” through a lightweight linear regression probe. This provides an inductive bias to learn the proper long-range dependencies, allowing it to achieve perfect accuracy, without any supervision from chain-of-thought.

In summary, by partially reverse-engineering a network that successfully implements multi-digit multiplication, we uncover how it implements long-range dependencies, a mechanism that the unsuccessful model lacks. Our work highlights a challenge for Transformers to learn long-range dependency using gradient descent and an auto-regressive loss. While we demonstrate a task-specific inductive bias to address this issue, we anticipate generic improvements to address this limitation.

## 2 Experiment Setup, Training ICoT, Notations

Task, Models. We are interested in understanding the difference in a model trained with standard fine-tuning and ICoT. From experiments, we find that the simplest multi-digit multiplication in which standard fine-tuning fails but ICoT works is 4 × \times 4 digit multiplications. Similarly, the smallest architecture in which ICoT works is a 2-layer model with 4 attention heads. Thus we carefully study a 2-layer 4-head ICoT model and a standard fine-tuned model trained on 4 × \times 4 multiplication.

Training Procedures. Our ICoT setup is the same as that Deng et al. (2024) . Here we provide an informal overview of ICoT, with details in Appendix A.1 . Namely, assume two operands a = ( a 3 , a 2 , a 1 , a 0 ) , b = ( b 3 , b 2 , b 1 , b 0 ) a=(a_{3},a_{2},a_{1},a_{0}),b=(b_{3},b_{2},b_{1},b_{0}) and their product c = ( c ​ 7 ​ … ​ c 0 ) c=(c7\dots c_{0}) . Operands are written least-significant digit first, similar to other algorithmic setups ( Deng et al., 2024 ; Deng et al., 2023 ; Lee et al., 2023 ) .

For ICoT, the training data includes intermediate chain-of-thought (CoT) tokens q i q_{i} that explicitly record the step-by-step calculations. As a simple illustration, consider 12 × 34 12\times 34 . The tokens appearing between the two equal signs follow the same CoT format used in our 4 × 4 4\times 4 -digit multiplication tasks:

12 ∗ 34 = 48 ⏟ 12 ∗ 4 + 360 ⏟ 12 ∗ 30 ​ ( 408 ) ⏟ running sum = 408 \displaystyle 12*34=\underbrace{48}_{12*4}+\underbrace{360}_{12*30}\ \underbrace{(408)}_{\text{running sum}}=408

At each training epoch, a fixed number of CoT tokens are removed from the left of the chain. Concretely, the training examples at each epoch may have the following form: ( Epoch 1 ) \displaystyle(\text{Epoch 1}) a 0 ​ a 1 ​ a 2 ​ a 3 ∗ b 0 ​ b 1 ​ b 2 ​ b 3 % % % ​ q 0 ​ … ​ q i ​ … ​ q j ​ … ​ q k ​ … ​ q τ ​ # ​ # ​ # ​ # ​ c 0 ​ … ​ c 7 \displaystyle\quad a_{0}a_{1}a_{2}a_{3}*b_{0}b_{1}b_{2}b_{3}\%\%\%\ q_{0}\ldots q_{i}\ldots q_{j}\ldots q_{k}\ldots q_{\tau}\ \#\#\#\#\ c_{0}\ldots c_{7} ( Epoch 2 ) \displaystyle(\text{Epoch 2}) a 0 ​ a 1 ​ a 2 ​ a 3 ∗ b 0 ​ b 1 ​ b 2 ​ b 3 % % % ​ q i ​ … ​ q j ​ … ​ q k ​ … ​ q τ ​ # ​ # ​ # ​ # ​ c 0 ​ … ​ c 7 \displaystyle\quad a_{0}a_{1}a_{2}a_{3}*b_{0}b_{1}b_{2}b_{3}\%\%\%\ q_{i}\ldots q_{j}\ldots q_{k}\ldots q_{\tau}\ \#\#\#\#\ c_{0}\ldots c_{7} ( Epoch 3 ) \displaystyle(\text{Epoch 3}) a 0 ​ a 1 ​ a 2 ​ a 3 ∗ b 0 ​ b 1 ​ b 2 ​ b 3 % % % ​ q j ​ … ​ q k ​ … ​ q τ ​ # ​ # ​ # ​ # ​ c 0 ​ … ​ c 7 \displaystyle\quad a_{0}a_{1}a_{2}a_{3}*b_{0}b_{1}b_{2}b_{3}\%\%\%\ q_{j}\ldots q_{k}\ldots q_{\tau}\ \#\#\#\#\ c_{0}\ldots c_{7} … \displaystyle\ldots ( Epoch N ) \displaystyle(\text{Epoch N}) a 0 ​ a 1 ​ a 2 ​ a 3 ∗ b 0 ​ b 1 ​ b 2 ​ b 3 % % % ​ # ​ # ​ # ​ # ​ c 0 ​ … ​ c 7 \displaystyle\quad a_{0}a_{1}a_{2}a_{3}*b_{0}b_{1}b_{2}b_{3}\%\%\%\ \#\#\#\#\ c_{0}\ldots c_{7} where q i q_{i} are CoT tokens and % , # \%,\# are special delimiters. 2 2 2 These delimiters have no special meaning beyond matching the setup of Deng et al. (2024) . Note that after each epoch, the model sees a shorter chain by truncating some tokens, and that by the end, only the operands and final answer remain. For comparison, standard fine-tuning only trains on the operands: a 0 ​ a 1 ​ a 2 ​ a 3 ∗ b 0 ​ b 1 ​ b 2 ​ b 3 % % % ​ # ​ # ​ # ​ # ​ c 0 ​ … ​ c 7 a_{0}a_{1}a_{2}a_{3}*b_{0}b_{1}b_{2}b_{3}\%\%\%\#\#\#\#\ c_{0}\ldots c_{7} .

Interestingly, the ICoT model is able to achieve 100% accuracy on 4 × \times 4 digit multiplication, while standard fine-tuning only achieves less than 1% accuracy. Note that scaling does not help – scaling to a 12 layer 8 head model achieves the same < 1 % <1\% accuracy, and Yang et al. (2023) show that fine-tuning a 2B model still plateaus at 95% accuracy.

For more details regarding training (data format, sample size, hyperparameters), see Appendix A .

##### Notations.

𝐡 t ℓ \mathbf{h}^{\ell}_{t} indicates the hidden states at layer ℓ \ell timestep t t . Timesteps for solution tokens c k , k = [ 0 , … , 7 ] c_{k},k=[0,\ldots,7] are notated t c k t_{c_{k}} . Att h ℓ \textsc{Att}^{\ell}_{h} ( ⋅ ) (\cdot) , MLP ℓ \textsc{MLP}^{\ell} ( ⋅ ) (\cdot) indicate the output of the attention heads or MLP blocks at layer ℓ \ell , head index h h . E , U ∈ ℝ V × d E,U\in\mathbb{R}^{V\times d} indicate (un)embedding weights.

## 3 Comparing the Mechanisms of ICoT versus SFT

### 3.1 Long-range dependencies in multi-digit multiplication

Here we discuss how one might solve multi-digit multiplication, and the required long-range dependencies needed to solve multiplication.

One approach to compute each digit, c k c_{k} , is as follows:

s k ≜ ∑ i + j = k a i ​ b j , ⏟ sum of partial products c k = ( s k + r k − 1 ) ​ mod ​ 10 , r k = ⌊ s k + r k − 1 10 ⌋ ⏟ carry , r − 1 = 0 \displaystyle s_{k}\triangleq\underbrace{\sum_{i+j=k}a_{i}b_{j},}_{\text{sum of partial products}}\quad c_{k}=(s_{k}+r_{k-1})\ \text{mod}\ 10,\quad r_{k}=\underbrace{\big\lfloor\frac{s_{k}+r_{k-1}}{10}\big\rfloor}_{\text{carry}},\quad r_{-1}=0 (1)

Note that both c k c_{k} and r k r_{k} can be expressed with an intermediary term c ^ k \hat{c}_{k} , which encapsulates both the relevant information from the partial products and the carry:

c ^ k ≜ s k + r k − 1 , c k = c ^ k ​ ( mod ​ 10 ) , r k = ⌊ c ^ k 10 ⌋ \displaystyle\hat{c}_{k}\triangleq s_{k}+r_{k-1},\qquad c_{k}=\hat{c}_{k}\;(\mathrm{mod}\;10),\qquad r_{k}=\big\lfloor\frac{\hat{c}_{k}}{10}\big\rfloor (2)

Importantly, note the long-range dependencies needed for multi-digit multiplication. Specifically, we highlight two observations: (i) To determine c k c_{k} , one must use all the partial products { a i ​ b j | i + j ≤ k } \{a_{i}b_{j}|i+j\leq k\} , since all of these terms contribute to c k c_{k} . (ii) Knowing the intermediary term c ^ k \hat{c}_{k} suffices to compute c k c_{k} and to propagate necessary information for later digits. Thus we use c ^ k \hat{c}_{k} as a probing signature (Section 3.2 ) at each timestep t c k t_{c_{k}} to check if the model is utilizing all the necessary long-range information to predict the correct tokens c k c_{k} .

In the following sections, we demonstrate how the ICoT model satisfies such long-range dependency while the standard fine-tuning model does not.

### 3.2 Evidence of Long-Range Dependencies in ICoT

We first demonstrate two lines of evidence that the ICoT model satisfies long-range dependencies in multi-digit multiplication, while the standard fine-tuning model does not.

Logit Attributions. Note from Figure 1 that digits a i , b i a_{i},b_{i} can only affect c k c_{k} terms where k ≥ i k\geq i . Also note that at timestep t c k t_{c_{k}} , the pairwise products { a i ​ b j | i + j = k } \{a_{i}b_{j}|i+j=k\} affect the final prediction c k c_{k} the most. “Earlier” pairwise products { a i ​ b j | i + j ≤ k } \{a_{i}b_{j}|i+j\leq k\} can still affect c k c_{k} , but with diminishing effects as i + j i+j gets smaller.

We directly test for these relationships in our ICoT and SFT models using logit attributions. Namely, given an input sample orig := a 0 ​ a 1 ​ a 2 ​ a 3 ∗ b 0 ​ b 1 ​ b 2 ​ b 3 \textsc{orig}:=a_{0}a_{1}a_{2}a_{3}*b_{0}b_{1}b_{2}b_{3} , we measure the logits of the model’s predictions for c 0 − 7 : logit c k ​ ( orig ) c_{0-7}:\text{logit}_{c_{k}}(\textsc{orig}) . We then randomly swap out one of the operand digits at timestep t t (e.g., a ~ 2 \tilde{a}_{2} ) to construct a counterfactual input counter t = a 0 ​ a 1 ​ a ~ 2 ​ a 3 ∗ b 0 ​ b 1 ​ b 2 ​ b 3 \textsc{counter}_{t}=a_{0}a_{1}\tilde{a}_{2}a_{3}*b_{0}b_{1}b_{2}b_{3} and measure the change in logits: Δ t , k = logit c k ​ ( orig ) − logit c k ​ ( counter t ) \Delta_{t,k}=\text{logit}_{c_{k}}(\textsc{orig})-\text{logit}_{c_{k}}(\textsc{counter}_{t}) Thus Δ t , k \Delta_{t,k} measures the effect that digit at timestep t t has on the prediction of token c k c_{k} .

We use 1,000 samples for each ( t , k ) (t,k) pair and show the results in Figure 2 . Note that for SFT, the model does not see the correct dependencies between earlier tokens to middle tokens, while the ICoT model does, suggesting that the model has indeed learned the correct long-range dependencies.

Probing for 𝐜 ^ k \mathbf{\hat{c}}_{k} . Note from Figure 1 and Equation 2 that the long-range dependencies can be captured by an intermediate term, c ^ k \hat{c}_{k} . We test for whether c ^ k \hat{c}_{k} information can be decoded from the hidden states of the models using linear regression probes. Namely, at each timestep t c k t_{c_{k}} we predict for c ^ k \hat{c}_{k} by training a single vector 𝐰 k ∈ ℝ d \mathbf{w}_{k}\in\mathbb{R}{}^{d} such that 𝐰 k ​ 𝐡 t c ​ k 2 . mid = c ^ k \mathbf{w}_{k}\mathbf{h}_{t_{ck}}^{2.\text{mid}}=\hat{c}_{k} using a MSE loss, where 𝐡 2 . mid \mathbf{h}^{2.\text{mid}} is the hidden state at layer 2 after attention heads, before MLPs.

Figure 3 reports the mean absolute error from probing for c ^ k \hat{c}_{k} for middle and late digits, k = 2 , … , 6 k=2,\ldots,6 . Note that the accuracy from the ICoT model is much higher than that of SFT, further suggesting that the ICoT model has learned the correct long-range dependencies while SFT has not.

### 3.3 Encoding Long-Range Dependencies via Attention Trees

How does the ICoT model compute long-range dependencies? Here we describe how the model’s attention patterns induce a shallow directed acyclic graph, akin to a binary expression tree, in order to encode long-range dependencies.

Namely, in the first layer, across all timesteps t > 5 t>5 , 3 3 3 Note that only after timestep 5, both a a and b b tokens appear in the context. each attention head only attends to a pair of digit tokens, { a i , b j } \{a_{i},b_{j}\} (Figure 4 , left). This allows the model to produce the pairwise product a i ​ b j a_{i}b_{j} (see Section 4.1 for how attention heads represent pairwise products), but also allows the model to cache the product a i ​ b j a_{i}b_{j} in the hidden state of layer 1 at timestep t t (i.e., 𝐡 t 1 \mathbf{h}^{1}_{t} ). Put differently, product pairs { a i ​ b j } i , j ∈ { 0 , … ​ 4 } \{a_{i}b_{j}\}_{i,j\in\{0,\ldots 4\}} are “cached” in the first layer across different timesteps ( 𝐡 t 1 , t < t c k \mathbf{h}^{1}_{t},t<t_{c_{k}} ).

At later timesteps t ≥ t c k t\geq t_{c_{k}} , when the model predicts solution tokens c k c_{k} , this allows the second layer attention heads to attend to a small set of previous cache sites , i.e., where the appropriate pairs of products a i ​ b j , i + j = k a_{i}b_{j},i+j=k are stored from earlier timesteps.

Example: Figure 4 depicts the attention patterns when the model predicts c 2 c_{2} , given input “ a 0 ​ … ​ 3 ∗ b 0 ​ … ​ 3 = c 0 ​ c 1 a_{0\ldots 3}*b_{0\ldots 3}=c_{0}c_{1} ”. These attention maps are averaged from 1,000 samples from a held out test set. The necessary terms to compute c 2 c_{2} are a 2 ​ b 0 , a 1 ​ b 1 , a 0 ​ b 2 a_{2}b_{0},a_{1}b_{1},a_{0}b_{2} , and c ^ 1 \hat{c}_{1} (which in turn requires a 1 ​ b 0 , a 0 ​ b 1 , a 0 ​ b 0 a_{1}b_{0},a_{0}b_{1},a_{0}b_{0} ).

Attention heads Att 3 2 \textsc{Att}^{2}_{3} , Att 4 2 \textsc{Att}^{2}_{4} each attend to positions ( b 0 , b 2 , c 1 ) (b_{0},b_{2},c_{1}) and ( b 3 , “ ​ # ​ ” , c 0 ) (b_{3},\text{``}\#\text{''},c_{0}) . Inspecting what was “cached” in the first layer at those timesteps reveals the necessary partial products to compute c 2 c_{2} . For example, at timestep b 0 b_{0} , Att 1 1 \textsc{Att}^{1}_{1} , Att 2 1 \textsc{Att}^{1}_{2} attend to a 2 , b 0 a_{2},b_{0} ; at timestep b 2 b_{2} Att 1 1 \textsc{Att}^{1}_{1} attends to a 1 , b 1 a_{1},b_{1} while Att 2 1 \textsc{Att}^{1}_{2} attends to a 0 , b 2 a_{0},b_{2} ; at timestep c 0 c_{0} Att 1 1 \textsc{Att}^{1}_{1} attends to a 1 , b 0 a_{1},b_{0} , Att 2 1 \textsc{Att}^{1}_{2} attends to a 0 ​ b 1 a_{0}b_{1} . Thus the model can derive partial products, a 2 ​ b 0 , a 1 ​ b 1 , a 0 ​ b 2 , a 1 ​ b 0 , a 0 ​ b 1 a_{2}b_{0},a_{1}b_{1},a_{0}b_{2},a_{1}b_{0},a_{0}b_{1} with its attention tree. 4 4 4 Note that there may be a couple of different ways that a 0 ​ b 0 a_{0}b_{0} is derived. One possibility is to re-use a 0 , b 0 a_{0},b_{0} information that was fetched at various timesteps. Another possibility is when a 0 a_{0} is slightly attended to at Att 3 2 \textsc{Att}^{2}_{3} (difficult to see in our visuals). Note that a 0 ​ b 0 a_{0}b_{0} plays a relatively minor role in computing c 2 c_{2} compared to all other partial products.

While Figure 4 shows an example of the “attention tree” for predicting c 2 c_{2} , one can similarly reconstruct the correct trees for all digits c 0 , … , c 7 c_{0},\ldots,c_{7} using the attention patterns for all digits in Figure 10 .

In summary, for each output step c k c_{k} , the ICoT model constructs a binary-tree-like graph, spread out across timesteps, to attend to the correct pairs of tokens, allowing it to compute partial products.

## 4 Feature Geometry of ICoT

In addition to the mechanisms seen in Section 3 , we also study the geometry of features in ICoT.

### 4.1 Digit-wise Multiplications as Minkowski Sums

Note from Section 3.3 that the attention patterns are sparse, often only attending to the two digits a i , b j a_{i},b_{j} being multiplied. In such a case, the outputs of the attention head form a Minkowski sum.

Namely, consider a single head Att 1 \textsc{Att}^{1} ( i , j i,j ) at the first layer, attending to two digits a i a_{i} , b j b_{j} . Let W O ∈ ℝ d × d h ​ e ​ a ​ d , W V ∈ ℝ d h ​ e ​ a ​ d × d W_{O}\in\mathbb{R}{}^{d\times d_{head}},W_{V}\in\mathbb{R}{}^{d_{head}\times d} be the output and value weights of the attention head, E [ a i ] ∈ ℝ d E[a_{i}]\in\mathbb{R}{}^{d} the token embedding for token a i a_{i} , and A i := W O W V E [ a i ] , B j := W O W V E [ b j ] , A i , B j ∈ ℝ d A_{i}:=W_{O}W_{V}E[a_{i}],B_{j}:=W_{O}W_{V}E[b_{j}],A_{i},B_{j}\in\mathbb{R}{}^{d} .

In such a case, when the model spends α % \alpha\% of its attention on digit a i a_{i} , and thus attends to digit b j b_{j} by ( 1 − α ) % (1-\alpha)\% , the set of all possible values for the output of the attention head forms a Minkowski sum:

Att 1 ​ ( i , j ) \displaystyle\textsc{Att}^{1}(i,j) = α ​ A i + ( 1 − α ) ​ B j + ϵ \displaystyle=\alpha A_{i}+(1-\alpha)B_{j}+\epsilon (3) { Att 1 ​ ( i , j ) } i , j \displaystyle\{\textsc{Att}^{1}(i,j)\}_{i,j} ⊆ ( α ​ A ) ⊕ ( ( 1 − α ) ​ B ) ⊕ ϵ \displaystyle\subseteq(\alpha A)\oplus((1-\alpha)B)\oplus\epsilon (4) (ignoring position embeddings). See Figure 5 (a) for a visualization.

Visually, 3D PCAs can reveal nested representations. Namely, we can observe clusters, each cluster corresponding to a feature (i.e., a i a_{i} ). These clusters form a “global” geometry. When zoomed in to each cluster, we observe additional clusters for a second feature (i.e., b j b_{j} ) that form a “local” geometry of the same shape as its global counterpart. See Figure 5 (b-d) for examples.

This observation can be explained by deconstructing the covariance of the attention output:

Σ Att = α 2 ​ Σ A + ( 1 − α ) 2 ​ Σ B , \displaystyle\Sigma_{\textsc{Att}}=\alpha^{2}\Sigma_{A}+(1-\alpha)^{2}\Sigma_{B}, (5) where Σ A = Cov ​ ( A i ) , Σ B = Cov ​ ( B j ) \Sigma_{A}=\text{Cov}(A_{i}),\Sigma_{B}=\text{Cov}(B_{j}) . First, note that if we ignore positional encodings, Σ A \Sigma_{A} and Σ B \Sigma_{B} share the same eigenvectors, as they each depend on the same terms ( E ⁡ [ ⋅ ] , W O , W V E[\cdot],W_{O},W_{V} ), which are picked by PCA. Further note that fixing a value for a i a_{i} leaves a local covariance, Σ l ​ o ​ c ​ a ​ l | a i = ( 1 − α ) 2 ​ Σ B \Sigma_{local|a_{i}}=(1-\alpha)^{2}\Sigma_{B} , which again share the same eigenvectors with the global Σ Att \Sigma_{\textsc{Att}} term, leading to the same local geometry when projected onto.

### 4.2 Embedding Digits on a Pentagonal Prism via Fourier Bases

Similar to Kantamneni & Tegmark (2025) , we find that our model encodes digits in Fourier space. Specifically, the model’s embeddings E E , the final hidden layer 𝐡 L \mathbf{h}^{L} , and even the weights of the last MLP can be well reconstructed from a small set of Fourier basis functions.

Figure 6 shows a 3D PCA visualization of the final hidden layer at timestep t c 2 t_{c_{2}} , for both the SFT and ICoT models. While the SFT hidden states do not reveal any obvious patterns, the ICoT hidden states reveal a striking pattern: the ten digits form vertices of a pentagonal prism .

This structure is naturally explained by Fourier modes. Consider the Fourier expansion ∑ C n ∗ e − 2 ​ π ​ i ​ k ​ n 10 , n = 0 , … , 9 . \sum C_{n}*e^{-2\pi i\tfrac{kn}{10}},\quad n=0,\ldots,9.

where C n ( ≠ c k ) C_{n}(\neq c_{k}) is some constant per digit n n . Following Kantamneni & Tegmark (2025) , we take frequencies k ∈ { 0 , 1 , 2 , 5 } k\in\{0,1,2,5\} , yielding the real Fourier basis Φ ⁡ ( n ) = [ 𝟏 ​ ( n ) cos ⁡ ( 2 ​ π ​ n 10 ) sin ⁡ ( 2 ​ π ​ n 10 ) cos ⁡ ( 2 ​ π ​ n 5 ) sin ⁡ ( 2 ​ π ​ n 5 ) 𝒑 ⁡ ( n ) ( k = 0 ) ( k = 1 ) ( k = 1 ) ( k = 2 ) ( k = 2 ) ( k = 5 ) ] , \Phi(n)=\left[\begin{array}[]{c@{\quad}c@{\quad}c@{\quad}c@{\quad}c@{\quad}c}\mathbf{1}(n)&\cos\!\left(2\pi\tfrac{n}{10}\right)&\sin\!\left(2\pi\tfrac{n}{10}\right)&\cos\!\left(2\pi\tfrac{n}{5}\right)&\sin\!\left(2\pi\tfrac{n}{5}\right)&\bm{p}(n)\\[-2.0pt] \scriptstyle(k=0)\hfil\hskip 8.19447pt&\scriptstyle(k=1)\hfil\hskip 8.19447pt&\scriptstyle(k=1)\hfil\hskip 8.19447pt&\scriptstyle(k=2)\hfil\hskip 8.19447pt&\scriptstyle(k=2)\hfil\hskip 8.19447pt&\scriptstyle(k=5)\end{array}\right], where 𝟏 ​ ( n ) ≡ 1 \mathbf{1}(n)\equiv 1 (the DC component) and 𝒑 ⁡ ( n ) ≡ ( − 1 ) n \bm{p}(n)\equiv(-1)^{n} (the Nyquist/parity vector). The sine terms for k = 0 k=0 and k = 5 k=5 vanish over n = 0 , … , 9 n=0,\dots,9 and are omitted.

The final hidden layer 𝐡 L \mathbf{h}^{L} can be reconstructed via these six terms (see Appendix B ), indicating that the final hidden state is encoded using Fourier bases.

Revisiting Figure 6 , the first principal component (PC1) aligns with the parity vector 𝒑 ⁡ ( n ) \bm{p}(n) , separating even from odd digits. Second and third principal components span the k = 2 k=2 Fourier pair ( cos , sin ⁡ ( 2 ​ π ​ n 5 ) \cos,\sin(\tfrac{2\pi n}{5}) ), so the digits lie on two regular pentagons: one each for even and odd digits. The digits within each pentagon advance by n + 4 ( mod 10 ) n+4\pmod{10} (e.g., n = → → 8 ​ … n=0\!\to\!4\!\to\!8\ldots , same for odd digits), allowing a walk around the pentagon while staying within the even/odd set. Interestingly, taking ( mod 5 ) \pmod{5} on such a sequence yields decreasing steps of 1 ( n ( mod 5 ) = → → 3 ​ … n\pmod{5}=0\!\to\!4\!\to\!3\ldots ). Lastly, the two pentagons are parallel and stacked along PC1, with corresponding vertices differing by ± 5 \pm 5 (same phase, opposite parity). Together, these yield the pentagonal-prism geometry in Figure 6 .

## 5 Pitfalls of Learning: Lack of Long-Range Dependency

Given our insights, we revisit why Transformers fail at multiplication under standard fine-tuning.

In particular, in Figure 7 (a), we inspect the gradient norms (top row) and losses (bottom row) per token c k c_{k} over the course of training. There are a few observations to make.

First, note from the loss curves that the first two digits, c 0 , c 1 c_{0},c_{1} , followed by the last digit, c 7 c_{7} , are learned first, as indicated by their immediate drop in loss to near zero. This aligns with the gradient norms observed for these tokens: within the first few steps, these tokens receive gradients, but their norms quickly drop to near zero once the loss for these tokens reach zero. Also note that the order in which tokens are learned according to gradient norms and losses is consistent.

The model then eventually learns to predict c 2 c_{2} . However, middle digits, c 3 c_{3} to c 6 c_{6} are never learned. Despite only the middle digits receiving gradients (as they are the only sources of loss remaining), their losses plateau, suggesting that the model is stuck in a local optimum that lacks the long-range dependencies to properly learn the middle digits.

Note that scaling to a larger model does not address this issue, as the same pattern can be found in a 12 layer 8 head model: see Appendix C .

## 6 Learning Multiplication Without ICoT

To further validate our understanding of why Transformers fail to learn multiplication, we demonstrate an example of a simple fix to teach Transformers multiplications without needing ICoT.

In particular, we leverage the observation from Section 3.1 in that ( i i ) multi-digit multiplication requires long-range dependencies between digit c k c_{k} and pairwise products { a i ​ b j | i + j ≤ k } \{a_{i}b_{j}|i+j\leq k\} , and ( i ​ i ii ) such dependency can be summarized by an intermediate value c ^ k \hat{c}_{k} to produce c k c_{k} .

Thus in order to guide the Transformer to learn long-range dependencies, we simply add an auxiliary loss term to predict c ^ k \hat{c}_{k} at each timestep t c k t_{c_{k}} . We attach an additional linear regression head 𝐰 h ∈ ℝ d \mathbf{w}_{h}\in\mathbb{R}^{d} to the output of H ( = 2 ) H(=2) attention heads in the second layer. These regression heads are trained to predict the correct accumulated sum c ^ k \hat{c}_{k} at each timestep t c k , c k ∈ [ 0 , … ​ 7 ] t_{c_{k}},c_{k}\in[0,\ldots 7] with a MSE loss: z i h \displaystyle z_{i}^{h} = 𝐰 h ⊤ ​ Att h 2 ​ ( ⋅ ) \displaystyle=\mathbf{w}^{\top}_{h}\textsc{Att}^{2}_{h}(\cdot) (6) ℒ a ​ u ​ x \displaystyle\mathcal{L}_{aux} = 1 H ​ ∑ h ∈ H 1 8 ​ ∑ i = 0 7 ( z i h − c ^ i ) 2 \displaystyle=\frac{1}{H}\sum_{h\in H}\frac{1}{8}\sum_{i=0}^{7}(z_{i}^{h}-\hat{c}_{i})^{2} (7) ℒ \displaystyle\mathcal{L} = ℒ L ​ M + λ ​ ℒ a ​ u ​ x \displaystyle=\mathcal{L}_{LM}+\lambda\mathcal{L}_{aux} (8)

where ℒ L ​ M \mathcal{L}_{LM} is the standard language modeling loss.

This introduces an inductive bias for the task, and allows our 2-layer model to correctly learn 4x4 multiplication with 99% accuracy. Again, note that a larger 12-layer model still fails at multiplication under standard fine-tuning.

Revisiting Figure 7 (b) demonstrates a very different learning dynamic. We observe the model learn early and last digits ( c 0 , c 1 , c 7 c_{0},c_{1},c_{7} ) and work inwards ( c 2 , c 3 , c 4 , c 6 c_{2},c_{3},c_{4},c_{6} , and finally c 5 c_{5} ).

Limitation. Obviously the suggested inductive bias pertains specifically to our task. However, our experiments demonstrate the pitfall of Transformers that require long-range dependencies, and that it is possible to overcome such a pitfall with the correct inductive biases. We speculate that there are other generalizing inductive biases that can improve performance on tasks with long-range dependencies ( Tay et al., 2020 ) , and leave this for future work.

### 6.1 Does the model with auxiliary loss learn the same mechanism as ICoT?

A natural question that arises is whether ICoT and our inductive bias leads to the same mechanisms.

Inspecting the attention patterns suggests that a similar (but not necessarily exact) mechanism is learned: see Figure 8 . Namely, the model similarly forms an “attention tree” to sparsely attend to the correct pairs of digits for each c i c_{i} in the first layer (red boxes). Interestingly, in the auxiliary-loss model we also observe an attention head (Layer 2 Head 2) that simultaneously attends to all the necessary digits, { a i ≤ k , b i ≤ k } \{a_{i\leq k},b_{i\leq k}\} , at each timestep t c k t_{c_{k}} , forming a parallelogram-like attention pattern (black box) akin to the shape seen in Figure 2 .

## 7 Related Work

##### Studying Transformers with Arithmetic Tasks.

A growing line of work study Transformers under controlled settings to better characterize their behavior ( Allen-Zhu & Li, 2023a ; Allen-Zhu & Li, 2023b ; Li et al., 2023 ; Nanda et al., 2023b ; Park et al., 2024b ; Park et al., 2024a ) . Often, arithmetics is a natural and popular domain ( Lee et al., 2023 ; Ye et al., 2024 ; Nikankin et al., 2024 ) , which has led to numerous insights. For instance, Nanda et al. (2023a) study how Transformers perform modular addition to explain grokking. Kantamneni & Tegmark (2025) find that large language models use trigonometry to do addition, encoding digits using Fourier bases, while Nikankin et al. (2024) suggest that they also rely on heuristics. Cai et al. (2025) study length generalization in Transformers using arithmetic tasks. Similarly, we study the limitations of Transformers by studying why it fails to learn multi-digit multiplication.

Process Supervision. Recent work trains models with process supervision , in which feedback is given not just on final correctness but on each intermediate reasoning step. For example, Uesato et al. (2022) demonstrate that process-supervision can yield less reasoning errors on GSM8K compared to outcome-only supervision. Similarly, Lightman et al. (2023) show that step-level human feedback on MATH leads to stronger reward models. More recently, Zhong et al. (2023) ’s Math-Shepherd automates step-wise rewards via continuation-based verification, improving performance on both GSM8K and MATH. ICoT similarly plays the role of process supervision in latent space, by slowly removing chain-of-thought tokens during training such that the model internalizes the reasoning procedure. We thus use ICoT’s success on multiplication to study why Transformers fail.

## 8 Conclusion

In this work, we study why Transformers fail on a seemingly simple task of multi-digit multiplication. We answer this question by reverse-engineering a model trained with implicit chain-of-thought, and uncover that it has learned to compute the correct long-range dependencies needed for multi-digit multiplication. Our findings point to a pitfall of the standard recipe for training language models: using gradient descent with an auto-regressive loss on Transformers does not encourage the model to learn the right long-range dependencies. While we provide a simple example of how the right inductive bias can address such a limitation, we anticipate future work to provide a generic solution to improve on tasks with long-range dependencies.

#### Acknowledgments

XB, CT acknowledge the support of NSF grants IIS-2126602. YD is supported by an NSERC Discovery Grant (RGPIN-2024-05178) and a Starter Grant from the University of Waterloo. AL, MW, and FV acknowledge support from the Superalignment Fast Grant from OpenAI, Effective Ventures Foundation, Effektiv Spenden Schweiz, and the Open Philanthropy Project. IP thanks Keya Hu for constructive feedback and AL thanks Thomas Fel for fruitful discussions regarding feature geometry.

### Reproducibility Statement

Our code to reproduce all of our experiments can be found in https://github.com/ajyl/icot . Appendix A provides details of our training setup, including data formats, sample size, and hyperparameters.

## References

Allen-Zhu & Li (2023a) Zeyuan Allen-Zhu and Yuanzhi Li. Physics of language models: Part 1, context-free grammar. arXiv e-prints , pp. arXiv–2305, 2023a.

Allen-Zhu & Li (2023b) Zeyuan Allen-Zhu and Yuanzhi Li. Physics of language models: Part 3.1, knowledge storage and extraction. arXiv preprint arXiv:2309.14316 , 2023b.

Cai et al. (2025) Ziyang Cai, Nayoung Lee, Avi Schwarzschild, Samet Oymak, and Dimitris Papailiopoulos. Extrapolation by association: Length generalization transfer in transformers. arXiv preprint arXiv:2506.09251 , 2025.

Deng et al. (2023) Yuntian Deng, Kiran Prasad, Roland Fernandez, Paul Smolensky, Vishrav Chaudhary, and Stuart Shieber. Implicit chain of thought reasoning via knowledge distillation. arXiv preprint arXiv:2311.01460 , 2023.

Deng et al. (2024) Yuntian Deng, Yejin Choi, and Stuart Shieber. From explicit cot to implicit cot: Learning to internalize cot step by step, 2024. URL https://arxiv.org/abs/2405.14838 .

Gambardella et al. (2024) Andrew Gambardella, Yusuke Iwasawa, and Yutaka Matsuo. Language models do hard arithmetic tasks easily and hardly do easy arithmetic tasks. In Lun-Wei Ku, Andre Martins, and Vivek Srikumar (eds.), Proceedings of the 62nd Annual Meeting of the Association for Computational Linguistics (Volume 2: Short Papers) , pp. 85–91, Bangkok, Thailand, August 2024. Association for Computational Linguistics. doi: 10.18653/v1/2024.acl-short.8 . URL https://aclanthology.org/2024.acl-short.8/ .

Kantamneni & Tegmark (2025) Subhash Kantamneni and Max Tegmark. Language models use trigonometry to do addition. arXiv preprint arXiv:2502.00873 , 2025.

Lee et al. (2023) Nayoung Lee, Kartik Sreenivasan, Jason D Lee, Kangwook Lee, and Dimitris Papailiopoulos. Teaching arithmetic to small transformers. arXiv preprint arXiv:2307.03381 , 2023.

Li et al. (2023) Kenneth Li, Aspen K Hopkins, David Bau, Fernanda Viégas, Hanspeter Pfister, and Martin Wattenberg. Emergent world representations: Exploring a sequence model trained on a synthetic task. ICLR , 2023.

Lightman et al. (2023) Alex Lightman, Yuntao Bai, Saurav Kadavath, Tamera Lanham, Nicholas Schiefer, et al. Let’s verify step by step, 2023. URL https://arxiv.org/abs/2305.20050 .

Nanda et al. (2023a) Neel Nanda, Lawrence Chan, Tom Lieberum, Jess Smith, and Jacob Steinhardt. Progress measures for grokking via mechanistic interpretability. arXiv preprint arXiv:2301.05217 , 2023a.

Nanda et al. (2023b) Neel Nanda, Andrew Lee, and Martin Wattenberg. Emergent linear representations in world models of self-supervised sequence models. arXiv preprint arXiv:2309.00941 , 2023b.

Nikankin et al. (2024) Yaniv Nikankin, Anja Reusch, Aaron Mueller, and Yonatan Belinkov. Arithmetic without algorithms: Language models solve math with a bag of heuristics. arXiv preprint arXiv:2410.21272 , 2024.

Nye et al. (2021) Maxwell Nye, Anders Johan Andreassen, Guy Gur-Ari, Henryk Michalewski, Jacob Austin, David Bieber, David Dohan, Aitor Lewkowycz, Maarten Bosma, David Luan, et al. Show your work: Scratchpads for intermediate computation with language models. 2021.

Park et al. (2024a) Core Francisco Park, Andrew Lee, Ekdeep Singh Lubana, Yongyi Yang, Maya Okawa, Kento Nishi, Martin Wattenberg, and Hidenori Tanaka. Iclr: In-context learning of representations. arXiv preprint arXiv:2501.00070 , 2024a.

Park et al. (2024b) Core Francisco Park, Ekdeep Singh Lubana, Itamar Pres, and Hidenori Tanaka. Competition dynamics shape algorithmic phases of in-context learning. arXiv preprint arXiv:2412.01003 , 2024b.

Tay et al. (2020) Yi Tay, Mostafa Dehghani, Samira Abnar, Yikang Shen, Dara Bahri, Philip Pham, Jinfeng Rao, Liu Yang, Sebastian Ruder, and Donald Metzler. Long range arena: A benchmark for efficient transformers. arXiv preprint arXiv:2011.04006 , 2020.

Uesato et al. (2022) Jonathan Uesato, Po-Sen Huang, Tim Rocktäschel, Pushmeet Kohli, et al. Solving math word problems with process- and outcome-based feedback, 2022. URL https://arxiv.org/abs/2211.14275 .

Yang et al. (2023) Zhen Yang, Ming Ding, Qingsong Lv, Zhihuan Jiang, Zehai He, Yuyi Guo, Jinfeng Bai, and Jie Tang. Gpt can solve mathematical problems without a calculator. arXiv preprint arXiv:2309.03241 , 2023.

Ye et al. (2024) Tian Ye, Zicheng Xu, Yuanzhi Li, and Zeyuan Allen-Zhu. Physics of language models: Part 2.1, grade-school math and the hidden reasoning process. arXiv preprint arXiv:2407.20311 , 2024.

Zhong et al. (2023) Zexue Zhong, Zihan Zhao, Yutao Sun, et al. Math-shepherd: Process supervision for large language models, 2023. URL https://arxiv.org/abs/2312.08935 .

## Appendix A Training Details

Here we provide additional details regarding the training procedures of each of our models.

### A.1 ICoT Training

Our ICoT training setup follows the practice outlined in the original ICoT paper ( Deng et al., 2024 ) .

ICoT works by initially presenting explicit chain-of-thought tokens during training, but gradually removing them across numerous “stages” (e.g., epochs). Concretely, the training examples at each epoch may have the following form: ( Epoch 1 ) \displaystyle(\text{Epoch 1}) a 0 ​ a 1 ​ a 2 ​ a 3 ∗ b 0 ​ b 1 ​ b 2 ​ b 3 % % % ​ q 0 ​ … ​ q i ​ … ​ q j ​ … ​ q k ​ … ​ q τ ​ # ​ # ​ # ​ # ​ c 0 ​ … ​ c 7 \displaystyle\quad a_{0}a_{1}a_{2}a_{3}*b_{0}b_{1}b_{2}b_{3}\%\%\%\ q_{0}\ldots q_{i}\ldots q_{j}\ldots q_{k}\ldots q_{\tau}\ \#\#\#\#\ c_{0}\ldots c_{7} ( Epoch 2 ) \displaystyle(\text{Epoch 2}) a 0 ​ a 1 ​ a 2 ​ a 3 ∗ b 0 ​ b 1 ​ b 2 ​ b 3 % % % ​ q i ​ … ​ q j ​ … ​ q k ​ … ​ q τ ​ # ​ # ​ # ​ # ​ c 0 ​ … ​ c 7 \displaystyle\quad a_{0}a_{1}a_{2}a_{3}*b_{0}b_{1}b_{2}b_{3}\%\%\%\ q_{i}\ldots q_{j}\ldots q_{k}\ldots q_{\tau}\ \#\#\#\#\ c_{0}\ldots c_{7} ( Epoch 3 ) \displaystyle(\text{Epoch 3}) a 0 ​ a 1 ​ a 2 ​ a 3 ∗ b 0 ​ b 1 ​ b 2 ​ b 3 % % % ​ q j ​ … ​ q k ​ … ​ q τ ​ # ​ # ​ # ​ # ​ c 0 ​ … ​ c 7 \displaystyle\quad a_{0}a_{1}a_{2}a_{3}*b_{0}b_{1}b_{2}b_{3}\%\%\%\ q_{j}\ldots q_{k}\ldots q_{\tau}\ \#\#\#\#\ c_{0}\ldots c_{7} … \displaystyle\ldots ( Epoch N ) \displaystyle(\text{Epoch N}) a 0 ​ a 1 ​ a 2 ​ a 3 ∗ b 0 ​ b 1 ​ b 2 ​ b 3 % % % ​ # ​ # ​ # ​ # ​ c 0 ​ … ​ c 7 \displaystyle\quad a_{0}a_{1}a_{2}a_{3}*b_{0}b_{1}b_{2}b_{3}\%\%\%\ \#\#\#\#\ c_{0}\ldots c_{7} where q i q_{i} are CoT tokens and % , # \%,\# are special delimiters. These delimiters have no special meaning beyond matching the setup of Deng et al. (2024) . Note that after each epoch, the model sees a shorter chain by truncating some tokens, and that by the end, only the operands and final answer remain.

The actual format of our ICoT data is as follows. Using an example input of 8331 × 5015 8331\times 5015 , digits are presented in least-significant digits first, resulting in the following format: 1338 ∗ 5105 | | 5614 + 013380 ( 569421 ) + 0000000 ( 5694210 ) + 0005561 % % # # # # 56997714 1338*5105||5614+013380(569421)+0000000(5694210)+0005561\%\%\#\#\#\#56997714

Unlike Deng et al. (2024) , instead of using a pre-trained 12-layer GPT model, we train a smaller 2-layer, 4-head GPT-based model from scratch, not only to remove any confounding factors from pre-trained knowledge, but also because the 2-layer 4-head architecture is the simplest form in which ICoT succeeds but standard fine-tuning fails. The training data consists of 80,800 samples, while the validation and test sets each contain 1,000 held out samples. We train with a learning rate of 5e-5 , and remove 8 chain-of-thought tokens at every “stage” (which in our case is an epoch). Both training and validation loss converge after 13 epochs, and achieves 100% accuracy on the test set.

### A.2 Standard Fine-Tuning

Similar to ICoT, for our standard fine-tuning model, we train a 2-layer, 4-head GPT-based model from scratch, on the same data as ICoT. We use a learning rate of 5e-5 , and the input format is a 0 ​ a 1 ​ a 2 ​ a 3 ∗ b 0 ​ b 1 ​ b 2 ​ b 3 % % ​ # ​ # ​ # ​ # ​ c 0 ​ … ​ c 7 a_{0}a_{1}a_{2}a_{3}*b_{0}b_{1}b_{2}b_{3}\%\%\#\#\#\#c_{0}\ldots c_{7} . All other hyperparameters match those in our ICoT setup. The model’s loss and accuracy plateaus after 13 epochs, it achieves only about 1% train and validation accuracy, while digit-level accuracy converges at approximately 81%, and remains the same even after 60 epochs.

Note that scaling the model larger to a 12-layer, 8-head model achieves the same low accuracy at 1% and digit-level accuracy of 80%.

## Appendix B Fourier structure in model’s weights, activations

Here we provide a deeper dive into the Fourier structure found in the ICoT model’s weights and hidden states. Namely, we analyze the model’s embedding weights, final MLP’s weights, and last hidden layer:

1. Embeddings ℰ ∈ ℝ 10 × d \mathcal{E}\in\mathbb{R}{}^{10\times d}

2. Final layer MLP output weights W o ​ u ​ t ∈ ℝ d m ​ l ​ p × d W_{out}\in\mathbb{R}{}^{d_{mlp}\times d} , given MLP ​ ( 𝐱 ) = σ ⁡ ( W i ​ n ​ 𝐱 ) ​ W o ​ u ​ t \text{MLP}(\mathbf{x})=\sigma(W_{in}\mathbf{x})W_{out}

3. Final hidden layer 𝐡 L t ∈ ℝ N × d \mathbf{h}^{L}_{t}\in\mathbb{R}{}^{N\times d}

where N ( = 1,000 ) N(=1,000) is the size of our validation set. For the latter two, we first project them onto the model’s embedding space: W o ​ u ​ t ^ = ( ℰ W o ​ u ​ t ) ⊤ ∈ ℝ d m ​ l ​ p × 10 \widehat{W_{out}}=(\mathcal{E}W_{out})^{\top}\in\mathbb{R}{}^{d_{mlp}\times 10} 𝐡 L ^ = ( ℰ 𝐡 L ) ⊤ ∈ ℝ N × 10 \widehat{\mathbf{h}^{L}}=(\mathcal{E}\mathbf{h}^{L})^{\top}\in\mathbb{R}{}^{N\times 10}

Each item X ∈ { ℰ , W o ​ u ​ t ^ , 𝐡 L ^ } X\in\{\mathcal{E},\widehat{W_{out}},\widehat{\mathbf{h}^{L}}\} is a collection of row vectors 𝐱 ∈ ℝ 10 \mathbf{x}\in\mathbb{R}{}^{10} whose ten entries correspond to digits n = 0 , … , 9 n=0,\ldots,9 .

We find that vectors 𝐱 \mathbf{x} are encoded in a low-dimensional trigonometric subspace.

Namely, consider the Fourier expansion ∑ C n ∗ e − 2 ​ π ​ i ​ k ​ n 10 , n = 0 , … , 9 . \sum C_{n}*e^{-2\pi i\tfrac{kn}{10}},\quad n=0,\ldots,9.

where C n ( ≠ c k ) C_{n}(\neq c_{k}) is some constant per n n . Following Kantamneni & Tegmark (2025) , we take frequencies k ∈ { 0 , 1 , 2 , 5 } k\in\{0,1,2,5\} , yielding the real Fourier basis Φ ⁡ ( n ) = [ 𝟏 ​ ( n ) cos ⁡ ( 2 ​ π ​ n 10 ) sin ⁡ ( 2 ​ π ​ n 10 ) cos ⁡ ( 2 ​ π ​ n 5 ) sin ⁡ ( 2 ​ π ​ n 5 ) 𝒑 ⁡ ( n ) ( k = 0 ) ( k = 1 ) ( k = 1 ) ( k = 2 ) ( k = 2 ) ( k = 5 ) ] , \Phi(n)=\left[\begin{array}[]{c@{\quad}c@{\quad}c@{\quad}c@{\quad}c@{\quad}c}\mathbf{1}(n)&\cos\!\left(2\pi\tfrac{n}{10}\right)&\sin\!\left(2\pi\tfrac{n}{10}\right)&\cos\!\left(2\pi\tfrac{n}{5}\right)&\sin\!\left(2\pi\tfrac{n}{5}\right)&\bm{p}(n)\\[-2.0pt] \scriptstyle(k=0)\hfil\hskip 8.19447pt&\scriptstyle(k=1)\hfil\hskip 8.19447pt&\scriptstyle(k=1)\hfil\hskip 8.19447pt&\scriptstyle(k=2)\hfil\hskip 8.19447pt&\scriptstyle(k=2)\hfil\hskip 8.19447pt&\scriptstyle(k=5)\end{array}\right], where 𝟏 ​ ( n ) ≡ 1 \mathbf{1}(n)\equiv 1 (the DC component) and 𝒑 ⁡ ( n ) ≡ ( − 1 ) n \bm{p}(n)\equiv(-1)^{n} (the Nyquist/parity vector). The sine terms for k = 0 k=0 and k = 5 k=5 vanish over n = 0 , … , 9 n=0,\dots,9 and are omitted.

Let F ∈ 10 × 6 F\in 10\times 6 be a Fourier matrix with rows indexed by n ∈ { 0 , … , 9 } n\in\{0,\ldots,9\} and columns as defined above.

For each row 𝐱 ∈ ℝ 10 \mathbf{x}\in\mathbb{R}{}^{10} we fit least squares coefficients C = arg min C ∈ ℝ 6 ∥ x − F C ∥ 2 2 C\;=\;\arg\min_{C\in\mathbb{R}{}^{6}}\;\|x-FC\|_{2}^{2} and quantify goodness-of-fit using coefficient of determination R 2 ​ ( x ) = 1 − ‖ x − F ​ C ‖ 2 2 ‖ x − x ¯ ‖ 2 2 , R^{2}(x)\;=\;1-\frac{\|x-FC\|_{2}^{2}}{\|x-\bar{x}\|_{2}^{2}}, We report the median R 2 R^{2} over the set of rows in each X X (i.e., over d mlp d_{\text{mlp}} rows for W o ​ u ​ t ^ \widehat{W_{out}} , d d rows for ℰ \mathcal{E} , and over batch examples for 𝐡 L \mathbf{h}^{L} .

In Table 1 we observe strong fits: the per-row medians lie between 0.85 0.85 and 0.99 0.99 , indicating that a six-dimensional trigonometric basis over digits captures the vast majority of variance:

We can extend the Fourier bases to include additional terms, for k = 3 , 4 k=3,4 , which forms a 8 dimensional basis (excluding sine terms for k = 0 , 5 k=0,5 ), which leads to perfect R 2 R^{2} fits.

## Appendix C Per Token Gradients and Losses: 12-Layer Model

Even with a larger 12 layer model, the model fails to learn the right long-range dependencies. Figure 9 displays the results – we see the similar patterns as the 2-layer model, in which middle digits never receive the right gradients and loss does not drop.

## Appendix D Attention Patterns of All Models

ICoT

SFT

Auxiliary Loss Model

In Section 3.3 , we illustrate how a binary tree is constructed for c 2 c_{2} in the ICoT model. In Figure 10 , we present the attention patterns for all digits across the three models, from with attention trees can be derived for the ICoT model for each solution token c i c_{i} .

## Appendix E LLM Usage

We used LLMs to proof read our draft and polish our notations.

## Instructions for reporting errors

We are continuing to improve HTML versions of papers, and your feedback helps enhance accessibility and mobile support. To report errors in the HTML that will help us improve conversion and rendering, choose any of the methods listed below:

Click the "Report Issue" ( ) button, located in the page header.

Tip: You can select the relevant text first, to include it in your report.

Our team has already identified the following issues . We appreciate your time reviewing and reporting rendering errors we may not have found yet. Your efforts will help us improve the HTML versions for all readers, because disability should not be a barrier to accessing research. Thank you for your continued support in championing open access for all.

Have a free development cycle? Help support accessibility at arXiv! Our collaborators at LaTeXML maintain a list of packages that need conversion , and welcome developer contributions .
