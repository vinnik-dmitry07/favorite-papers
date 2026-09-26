##### Report GitHub Issue

Content selection saved. Describe the issue below:

# Recirculation

###### Abstract

We describe an inference-time architectural enhancement for off-the-shelf foundation models that markedly reduces perplexity and boosts accuracy across generation and reasoning tasks. Our approach incurs essentially no additional latency during generation, though it requires serial processing in the prefill phase. Motivated by the fundamental limitation that state updates in feedforward transformers are bounded by model depth, our technique, recirculation , introduces a specific form of recurrence that allows the model to act as a dynamical system and track belief states. We distinguish this technique from chain-of-thought computation—which is better reserved for complex inferences rather than basic state tracking—as well as from popular depth-recurrence techniques (looping) and the costly training of recurrent transformers. We also propose and evaluate an adaptive variant of recirculation which requires only light tuning of hyperparameters while freezing the original model weights. Relative to the off-the-shelf baseline, adaptive recirculation achieves remarkable gains on the Gemma3 family, including a systematic reduction in perplexity on a suite of datasets, a 21% increase in accuracy on GSM8k, and reliable improvements in accuracy on other downstream tasks. Our training-free approach succeeds by leveraging the model itself to inform architectural modifications, suggesting a route to architectural evolution guided by a trained network’s properties rather than forced, arbitrary design choices.

## 1 State tracking

The ability to track a fluid, evolving state of affairs is essential for comprehending language, reasoning about situations, and modeling the world around us. Traditional approaches to state tracking, such as recurrent neural nets and Kalman filters, involve iterative, sequential updating of latent variables to capture dynamics. The parallel operation of transformers, during both training and prefill, precludes tracking state in the traditional manner ( Mozer et al., 2026 ) . Transformers learn a variety of clever solutions that can make them effective at state tracking for finite sequence lengths ( Li et al., 2025a ; Piotrowski et al., 2025 ; Prakash et al., 2026 ; Shai et al., 2024 ) . However, transformers can also fail to track state information needed to understand the structure of arguments and social interactions. State tracking failures in foundation models lead to loss of coherence in multi-turn conversations ( Laban et al., 2025 ) , inefficiency in information gathering ( Sawyer et al., 2025 ) , and breakdowns in communication and cooperation in multi-agent settings ( Davidson et al., 2025 ; Khatua et al., 2026 ) . Tracking deficits can lead to a range of reasoning failures arising from ineffective working memory, unstable theory-of-mind representations, and absence of a robust internal world model ( Song et al., 2026 ) .

Without proper state tracking, models can flip-flop in their interpretations and fail to detect their inconsistencies, e.g., the meaning of a polysemous word in Figure 1 ( Lepori et al., 2025 ) , known as a contextualization error. While it is perfectly sensible for a model to maintain a belief state that admits both interpretations of the word bank , after committing to the edge-of-a-river interpretation ( river bank ), a socially adept communicator should acknowledge the reversal of meaning.

In general, it becomes untenable for models—and people—to maintain and track belief states because the distributions explode in dimensionality. People adopt heuristics such as sampling ( Vul et al., 2014 , e.g.,) , collapsing distributions into prototypical cases ( Tversky and Kahneman, 1971 ) , or forming concrete mental models that are most consistent with premises ( Johnson-Laird, 1983 ) , kind of like a MAP estimate. All of these approaches nonetheless require state tracking, albeit without explicit representation of uncertainty.

Figure 2 a illustrates the challenge of state tracking in a transformer using the bank dialog of Figure 1 . Input steps are presented along the horizontal axis and blocks (or layers) of the transformer along the vertical axis. Each column represents the processing of an input token, where activation flows from bottom to top. The processing of the text day off work and fishing pole is depicted in columns on the left. Using a technique called Patchscopes ( Ghandeharioun et al., 2024 ) , Lepori et al. (2025) show that when the polysemous word bank is processed, shallow layers reflect the word’s ambiguity: the embedding is a mixture of its meanings—river edge and financial institution. In deeper layers of the stack (highlighted in yellow), the embedding is contextualized by the preceding text (depicted by the blue arrows), and the context-appropriate interpretation of the polysemous word is selected by nudging the embedding toward the river-edge representation. Because the architecture is feedforward, shallow layers of the transformer cannot access this interpretation. Thus, when the model is asked to formulate a response to the ATM question, the initial processing stages see only the ambiguous representation of bank . If the model commits to a response (highlighted yellow) using the ambiguous representation (blue arrows), it will choose the wrong response. Despite having previously interpreted bank as the river edge, it fails to access this state and responds yes based on a strong association between the ambiguous bank and ATM. Lepori et al. (2025) characterize this delayed disambiguation as a race in which the model’s response generation can outpace the model’s internal semantic convergence.

Lepori et al. (2025) obtained evidence in support of this account via an intervention experiment, illustrated in Figure 2 b. They processed the input sequence in the ordinary way up to the step at which the bank token is presented. At this step, they copied activation from a deep layer---after the ambiguity was resolved---down to a shallow layer and then continued processing the input sequence. This intervention, depicted in the Figure with an arrow, reduced contextualization errors by 60%. 1 1 1 The full experiment was based on a large set of generated questions containing a critical token that needs to be properly contextualized in order to answer correctly, with activation patching on only the critical token. Nikankin et al. (2025) have also shown that patching visual token activations back to a shallower layer in a vision-language model improves performances.

In this experiment, Lepori et al. (2025) replaced the embedding vector in a shallow layer with the corresponding vector from a deep layer, but only for one specific token pre-identified as critical in the given context. Suppose that instead of targeting this manipulation to a specific token, we did so in an undifferentiated fashion at every token position? Likely the outcome would be disastrous because the model was not trained to accommodate the resulting amplification of feedback. But what if instead of substituting one embedding vector for another, we merely leaked a small bit of activation from the deep layer to the shallow layer? The leakage might conceivably be sufficient to enrich the representation without pushing representations out of distribution. Consequently, we might observe benefits of this manipulation at inference without modifying the weights of a fully trained model .

This scheme might work even without fine tuning because a transformer’s residual stream acts like a shared blackboard onto which all layers can write, which encourages alignment of representations across layers ( Elhage et al., 2021 ) . By alignment, we mean that for a deep layer to communicate with a shallow layer, a 1:1 correspondence of features can be assumed and we do not require an arbitrary adapter such as a full-rank affine transformation or cross attention.

Why should there be alignment? Consider a particular feature of the embedding vector in the residual stream, and suppose that it is associated with a semantically meaningful concept such as moisture. Whether the feature is activated early or late in the stack, the direct effect on the output distribution is identical due to commutativity of addition. Some input tokens, e.g., pool or tears , may activate the moisture feature in the input embedding directly. An ambiguous token such as bank may not yield much intrinsic activation for moisture due to polysemy. However, if we feed back the disambiguated bank from a deep layer, the moisture feature will be amplified, providing useful information for subsequent processing. 2 2 2 This argument does not deny that the layer of origin of a feature may change the feature’s role, and in fact, the argument for leaking activation downwards is to leverage the changing roles. Layer normalization is one way that roles might depend on depth. However, while layer normalization may change a feature’s magnitude and even polarity, it does not reorient the feature. One might also be concerned about feature erasing: a feature may be ‘uncomputed’ once it is no longer needed. This concern is alleviated by recent work showing that transformers learn just as well, if not better, when each layer is forced to output orthogonal directions from the earlier layers, preventing feature erasing ( Oh et al., 2026 ; Zhang et al., 2026 ) .

## 2 Proposed method: Recirculation

We now formalize our method, which we refer to as recirculation , that involves running an LLM step-by-step and after each step, leaking a bit of the activation from a deep layer down to a shallow layer. Figure 3 a gives the general picture, where the recurrent arrow specifies one possible source- and destination-layer pair. Because this Figure does not specify how the recurrence is orchestrated with regard to input steps, the figure is ambiguous and could correspond to several distinct ideas ( Mozer et al., 2026 ) , one of which is recirculation and another of which is a very popular idea in the literature, the looped transformer ( Dehghani et al., 2019 ; Giannou et al., 2023 ) . For didactic purposes, we first discuss looped transformers and then characterize their relationship to recirculation.

A looped transformer is a parameter-efficient variant of the standard architecture. Whereas a standard transformer stacks a deep sequence of unique transformer blocks, a looped transformer applies a set of shared blocks multiple times. Figure 3 b depicts a looped transformer by unrolling the architecture of Figure 3 a vertically in depth and unrolled horizontally in input steps. At step 1, the first input token is presented, the activation stack is computed, and at layer 6 in the Figure (the loop source ), activation is passed to layer 3 (the loop destination ) of a second copy of the architecture, which then propagates activity to the output. The colored rectangles denote the current input token, the dark outlined rectangles are blocks whose activation is computed at a given step, the shaded blocks are frozen (or are replaced by KV cache), and the faint outlined rectangles are placeholders that are irrelevant at the current step. As each input step is processed, a single stack operates and the earlier stacks are frozen (or in KV cache). The Figure shows step-by-step operation of the model, as would be used with autoregressive decoding. However, when an input sequence is fixed—as during pretraining or in the prefill stage—the entire sequence can be computed in parallel.

Recurrence in a looped transformer is solely in depth: the arrows in Figure 3 b are directed within a stack. In contrast, recurrence in recirculation is in both depth and step , as depicted in Figure 3 c. Figure 3 c can be viewed as collapsing together the operation of Figure 3 b’s top stack at step i i and the bottom stack of step i + 1 i+1 . In recirculation, two input stacks are run in parallel at each recurrence step (except for the very first step, which serves as a warm up). The difference between Figures 3 b and 3 c looks to be a minor reorganization, but it fundamentally changes the nature of the computation when it comes to arbitrary state tracking. Figure 4 shows the same unrolled models but superimposes colored rectangles to indicate state propagation. To implement an arbitrary state updating function over time t t , z ⁡ ( t + 1 ) = f ⁡ ( z ⁡ ( t ) , x ⁡ ( t ) ) z(t+1)=f(z(t),x(t)) , where z z is state and x x is input, z ⁡ ( t + 1 ) z(t+1) must be one layer deeper in the looped transformer, which is just a deeper feedforward transformer with weight-sharing constraints. However, in recirculation, where there is projection in both depth and step, the same layer can hold both z ⁡ ( t ) z(t) and z ⁡ ( t + 1 ) z(t+1) . The cost of state tracking is that sequential passes must be made through the architecture, and because of this sequential updating, recirculation cannot be parallelized, even when an entire input sequence is provided, such as during prefill.

In Figures 3 and 4 , the model is unrolled to execute the transformer stack twice at each step, i.e., one more iteration than a standard transformer. This number of iterations can be increased, both for looping and recirculation. We depict two-iteration recirculation in Figure A.1 . However, all experiments reported in this article are with the one-additional-iteration variant. If the number of iterations is unbounded, recirculation behaves as a true recurrent neural net.

We note one other key difference between looping and recirculation. In looping, the activation that gets looped is the entire residual stream and it acts as the direct replacement for the input that would normally come from a preceding layer. In recirculation, activation is mixed from the source and destination layers. Initially, we formalize one-iteration recirculation as a mixture: 𝒛 t + 1 , t , d = α ​ f ​ ( 𝒛 t , t , s | d , t ) + β ​ 𝒛 t , t , d , {\boldsymbol{z}}_{t+1,t,d}=\alpha f({\boldsymbol{z}}_{t,t,s}|d,t)+\beta{\boldsymbol{z}}_{t,t,d}, (1) where t t is an index over the order of updates, s s and d d are the source and destination layer indices, respectively, α \alpha and β \beta are mixture coefficients, f ( . ) f(.) is a renormalization function, and 𝒛 𝒊 , 𝒋 , 𝒍 \boldsymbol{z_{i,j,l}} is the residual stream output after incorporating the computation of layer l l at unrolling step i i and input step j j . These three indices correspond to the three sequence dimensions depicted in Figure 3 c: l l and j j are the row and column indices of the transformer layer grid, respectively, and i i is an index over copies of architecture. The motivation for the renormalization function f f is to accommodate the possibility that embedding magnitudes grow as the layer outputs are combined. We always use a convex mixture with β ≡ 1 − α \beta\equiv 1-\alpha and rescale source to have the same L 2 L_{2} norm as the destination unless mentioned otherwise: f ⁡ ( 𝒛 | d , t ) = ‖ 𝒛 t , t , d ‖ 2 ‖ 𝒛 ‖ 2 ​ 𝒛 . f({\boldsymbol{z}}|d,t)=\frac{||{\boldsymbol{z}}_{t,t,d}||_{2}}{||{\boldsymbol{z}}||_{2}}~{\boldsymbol{z}}. (2)

## 3 Related research

Looped transformers. Looped transformers run single layers or a range of layers multiple times, obtaining a deeper architecture with no addition in free parameters ( Dehghani et al., 2019 ; Giannou et al., 2023 ) . Looping, which can be deterministic or adaptive, is a very popular and successful approach. Looping can increase the expressivity of a transformer ( Saunshi et al., 2025 ) , but it does not guarantee indefinite state tracking. Some methods are designed and trained to allow for inference time scaling ( Yang et al., 2024 ; Nowak et al., 2024 ; Raposo et al., 2024 ; Alabdulmohsin and Zhai, 2025 ; Bae et al., 2025 ; Chen et al., 2025a ; Geiping et al., 2025 ; Rodkin et al., 2025 ; Yu et al., 2025 ; Zhu et al., 2025 ; Zeng et al., 2026 ; Jeddi et al., 2026 , e.g.,) ; others incorporate recurrence via pretraining ( Sanyal, 2026 ) or fine tuning a pretrained model ( Koishekenov et al., 2025 ; McLeish et al., 2025 ) ; and surprisingly, several operate purely as an inference-time method to improve reasoning ( Li et al., 2025b ; Chen et al., 2026 ; Ng, 2026 ) . The inference-time methods have the greatest similarity to recirculation, although the notion of looping (greater depth) is conceptually distinct from the recurrence that occurs in recirculation (see Figures 3 and 4 ).

Training objectives. Training losses have been proposed that aim to make embeddings in a given layer of the transformer more stateful, i.e., interpretable in terms of state updating functions. Particular losses have been proposed to steer models toward such solutions, to the extent they exist exactly or approximately ( Hu et al., 2025 ; Teoh et al., 2025 ; Huang et al., 2026 ) .

State tracking. Liu et al. (2026) point to the weakness of modern massively parallel architectures on problems that are inherently sequential, problems where combinatorics make it impractical to parallelize, such as state tracking, multihop inference, and planning. Transformers are bounded in their serial capacity based on model depth ( Merrill and Sabharwal, 2023 ; Strobl et al., 2024 ; Merrill and Sabharwal, 2025 , e.g.,) and also by the fact that effectively utilizing the state representation becomes more challenging as it shifts upwards to deeper layers ( Biran et al., 2024 ; Lepori et al., 2025 ; Mozer et al., 2026 ; Sawyer et al., 2025 ; Venhoff et al., 2025 ) . Merrill and Sabharwal (2025) prove the necessity and sufficiency of log ⁡ n \log n layers to recognize regular language strings of up to length n n and graph-connectivity problems with n n vertices. However, this proof addresses only the constructability of solutions, not their learnability. In practice, many researchers have identified clever solutions obtained by training depth-limited models on specific finite sequence-length problems ( Li et al., 2025a ; Piotrowski et al., 2025 ; Prakash et al., 2026 ; Shai et al., 2024 ) .

Recurrent transformers. Models with sequential recurrent updates can express arbitrary state dynamics, z t = f ⁡ ( z t − 1 , x t ) z_{t}=f(z_{t-1},x_{t}) . Some of these models operate with token-by-token recurrence ( Fan et al., 2021 , e.g.,) , but most operate with blockwise recurrence ( Bulatov et al., 2022 ; Hutchins et al., 2022 ; Chevalier et al., 2023 ; Jabri et al., 2023 ; Chen et al., 2025b ; Borazjanizadeh and McClelland, 2026 ) . State-space models (SSMs) ( Katharopoulos et al., 2020 ; Schlag et al., 2021 ; Gu and Dao, 2024 ; Allen-Zhu, 2025 ; Yang et al., 2025 ; Peng et al., 2025 ; Sun et al., 2025 ; Siems et al., 2025 , e.g.,) are often touted as a means of state propagation, but many SSMs are no more expressive than an ordinary transformer ( Merrill et al., 2025 ) and none are as expressive as a generic recurrent net. Most closely related to our work is T 2 ​ MLR \text{T}^{2}\text{MLR} ( Cai et al., 2026 ) , which also recognizes the value of feeding intermediate representations from a deeper layer of the previous token position directly into a shallower layer of the current token position. However, the two approaches diverge substantially in their training paradigm and architectural mechanisms. While T 2 ​ MLR \text{T}^{2}\text{MLR} requires BPTT training or fine tuning, our formulation of recirculation is an inference-time, training-free intervention. Further, T 2 ​ MLR \text{T}^{2}\text{MLR} parameterizes the recurrence pathway with a dedicated, learnable gated fusion module, whereas recirculation relies directly on the intrinsic representation alignment of the Transformer’s residual stream.

Thinking models. One solution to the depth dilemma is chain-of-thought style “thinking” where a model can talk to itself by sequentially sending signals from deep in the transformer to shallow layers, thereby propagating state forward. This form of recurrence enhances model expressivity ( Li et al., 2024 ; Merrill and Sabharwal, 2024 ) . Thinking can be performed in natural language tokens or in latent space ( Hao et al., 2025 ; Jolicoeur-Martineau, 2025 , e.g.,) . As with other recurrent transformers, training thinking models can be costly because it restricts parallelism.

Activation steering. Recent work in activation steering demonstrates that a language model’s behavior can be predictably modulated by intervening on its latent representations ( Dathathri et al., 2020 ; Turner et al., 2023 ; Zou et al., 2023 ; Gao et al., 2025 ) . This representation space encodes complex behavioral directions, including those governing truthfulness and refusal ( Marks and Tegmark, 2023 ; Arditi et al., 2024 ) . In this context, recirculation can be viewed as an inference-time mechanism for self-steering. Rather than modifying the residual stream with a static, externally derived steering vector ( Rimsky et al., 2024 ) , recirculation leverages the model’s own contextualized deep-layer activations to guide representation trajectories in shallower layers.

## 4 Experiments

### 4.1 Hyperparameter sweeps

To explore the feasibility of recirculation, we begin by sweeping over the three hyperparameters of recirculation: the mixture coefficient α \alpha (with β = 1 − α \beta=1-\alpha unless mentioned otherwise), the source layer s s , and the destination layer d d . We incorporate recirculation into the Gemma3 1B PT (pretrained) model and compute perplexity for documents from the arXiv dataset. (Details of the simulation can be found in Appendix B.1 .) The four heatmaps of Figure 5 correspond to α ∈ { 0.04 , 0.07 , 0.10 , 0.16 } \alpha\in\{0.04,0.07,0.10,0.16\} ; the vertical and horizontal axes indicate the source and destination layers. We examine all source-destination pairs that are no more than 12 layers apart. The heatmap is coded blue-to-red to indicate perplexity lower-to-higher than a baseline no-recirculation Gemma3 1B model, which has perplexity 16.6 on this dataset. Notably, these heatmaps are fairly smooth and reveal systematic patterns. Increasing α \alpha amplifies the effect of recirculation but results in more source-destination pairs that harm perplexity. Layer 4 is desirable as a destination with a source 5-7 layers higher. For the moment, focus on the pattern of results and not on the magnitude of reduction in perplexity.

The top row of Figure 6 , shows perplexity for three datasets—arXiv, PG19, and C4—sweeping over source and destination layers and fixing α = 0.10 \alpha=0.10 . We transform absolute perplexity estimates into percentage change relative to the baseline model and average across the three datasets to get the boxed sweep showing percentage change. Blue indicates a reduction in perplexity, with the best source-destination pair obtaining an average reduction of 4.72%. Similarly to the 1B model, we identify the source and destination layers for the 4B and 12B models that yield the largest mean percentage perplexity reduction on the roughly 1.5M tokens in our tuning set. For the 1B, 4B, and 12B Gemma3 models, we found the optimal source and destination pairs based on our tuning set to be: {11, 4}, {18, 9}, and {35, 16}, respectively.

### 4.2 Perplexity evaluation

Having chosen source and destination layer based on our grid search results, we evaluate perplexity reduction on ten language modeling datasets with α = 0.15 \alpha=0.15 . Our evaluations include the three datasets used to select hyperparameters—arXiv, C4, and PG19—but the evaluation split is distinct from ‘training’ split used for hyperparameter tuning. Appendix B.2 presents details of the evaluation procedure, which included the Gemma3 1B, 4B, and 12B PT models.

Table 1 presents results for the three model sizes and ten data sets. For each model size, columns indicate perplexity of the baseline and recirculation models, and the percentage reduction in perplexity by incorporating recirculation. The 1B and 4B models obtain reductions up to 16% and the 12B model up to 35% 3 3 3 Note that the 12B model is relatively weak in terms of language modeling, but strong in downstream tasks post instruction-tuning as highlighted by its performance on standard benchmarks ( Gemma Team et al., 2024 ) . . For nine of the ten data sets, we see robust improvements across model scales. The lambada set is an anomaly due to the presence of very short sequences and tokenization artifacts. We show later that recirculation has greater benefits for longer sequences.

### 4.3 Normalization and ramping

Because the magnitude of residual-stream embeddings tends to grow over layers, we have found that renormalizing the source embedding before feeding it to the destination (Equations 1 and 2 ) better conditions the model to obtain a consistent and reliable pattern of perplexity reduction over the hyperparameter sweep (Figures 5 and 6 ). Appendix B.3 presents a range of normalization schemes we considered. The normalization scheme does not have much impact on the maximum perplexity reduction, only on the robustness of improvements over the source-destination landscape, which increases our confidence in being able to identify the optimal source-destination pair. The Appendix shows sweeps for multiple renormalization schemes, including an identity mapping (no renormalization). The Appendix also addresses the Gemma3 4B and 12B models, which turn out to critically require a non-convex mixture with β = 1 \beta=1 instead of β = 1 − α \beta=1-\alpha .

In Section 9 , we report results indicating that recirculating tokens at the beginning of the Gemma3 1B context window can be harmful. This finding does not seem surprising given there is little state information to propagate at the start of the window; and without a benefit from recirculation, the cost of potentially pushing the internal representations out of distribution may overwhelm. However, we find no harm of early-token recirculation in the 4B and 12B models. Nonetheless, we introduce ramping in the 1B model to attenuate α \alpha for the first tokens (see Appendix B.3 ), which yields a small reduction in perplexity.

### 4.4 Analysis of recirculation

#### 4.4.1 Robustness across model families

In Figure 7 , we observe that four other model families—Ministral3, Pythia, Qwen3, and Phi2—all show a robust region in the source-destination heatmap where reductions in perplexity are observed, analogous to what we observe with Gemma3 1B. The models are roughly the same size and all benefit most from recirculation in the middle region of the architecture.

The range of layers in this heatmap spans the full range of layers, which explains the difference in heatmap shape 4 4 4 Note that this Gemma3 1B heatmap is a full independent replication of Figure 5 with a different implementation, written in PyTorch and HuggingFace eco-system instead of JAX, but shares the data loader to ensure matched input. . The plot also includes recirculation to the output of layer 0 (leftmost column), whose representations apparently have not been contextualized to the point that deeper layers can interpret the recirculated signal.

The percentage reduction in perplexity is significantly larger for the Gemma model family than for the other families—about 5% versus less than 0.5%. As we explain in Appendix B.2 , the difference is due to an artifact specific to the Gemma family. When this artifact is eliminated, the Gemma family shows roughly the same sized perplexity reduction as other model families, which we will highlight in a revised version of this manuscript. Nonetheless, the basic purpose of the perplexity evaluation is to identify training-free routes to incorporating recurrence; the magnitude of the effect—averaged over all tokens—is not nearly as important as the qualitative pattern observed in the sweeps.

#### 4.4.2 Recirculation versus temperature tuning

Because perplexity is affected by the sharpness of a softmax distribution, we wanted to rule out the possibility that recirculation is merely sharpening or smoothing the distribution in an undifferentiated manner. We evaluated perplexity across a range of softmax temperatures and indeed found that with the base Gemma3 1B model, a temperature of 1.2 (versus the default of 1.0) reduced perplexity by 8.48% (see left panel of Figure C.2 ). Recirculation alone reduces perplexity by 14.21%, and therefore recirculation must not be reducible to temperature adjustment. When we combine recirculation with temperature tuning, we obtain a reduction in perplexity of 19.55%, also with temperature 1.2. The fact that the two effects are nearly additive allows us to rule out the artifactual explanation for recirculation in terms of token-independent temperature tuning.

#### 4.4.3 Recirculation versus looping

To verify that recirculation is influencing model dynamics in a structurally different manner than looped transformers ( Dehghani et al., 2019 ; Giannou et al., 2023 ; Alabdulmohsin and Zhai, 2025 ) , we compare recirculation and looped transformers. As we did with recirculation, we sweep over all ( ℓ 1 , ℓ 2 ) (\ell_{1},\ell_{2}) layer pairs with ℓ 2 > ℓ 1 \ell_{2}>\ell_{1} . To implement looping, we inserted into the transformer stack a copy of the layers from ℓ 1 + 1 \ell_{1}+1 up to and including ℓ 2 \ell_{2} immediately following the original ℓ 2 \ell_{2} in the stack. To be comparable to recirculation, we perform training-free evaluation. Although the literature indicates that models have been improved with training-free looping ( Li et al., 2025b ; Chen et al., 2026 ; Ng, 2026 ) , the heatmaps in Figure 8 indicate that, for the Gemma3 family at least, looping does not produce robust benefits. Furthermore, while recirculation shows benefits across model scales, looping a pretrained model shows benefits only at larger model scales, as suggested by our plots and observed by Ng (2026) . These qualitative differences in the heatmaps confirm that looping and recirculation are operating on different principles.

#### 4.4.4 Which tokens benefit from recirculation?

In all experiments reported to this point, tokens in every position of the context window are recirculated. Now we ask whether we can identify which tokens most contribute to recirculation performance improvements. Using a 1024-token context window and the Gemma3 1B PT model, we recirculate only the token in position t t and examine the benefit at lag k k , i.e., to the token in position t + k t+k . The increase in target log likelihood (equivalently, reduction in perplexity) relative to the no-recirculation model is a power function of k k , with large increases at short lags but a residual tail even at long lags. Figure 9 a shows the recirculation benefit averaged over token position t ∈ [ 0,767 ] t\in[0,767] for lag k ∈ [ 1,256 ] k\in[1,256] , relative to the baseline condition in which no recirculation occurs. Figure 9 b teases apart the effect of the recirculated token position, t t , shown along the horizontal axis of the Figure, and the heatmap indicates the benefit magnitude over lags k ∈ [ 1,256 ] k\in[1,256] . At the earliest positions, roughly t < 10 t<10 , recirculation reduces log likelihood, 5 5 5 In contrast to the Gemma3 1B model, we did not observe harmful effects of recirculating the early token positions with the larger Gemma3 4B and 12B models. but at all later position, recirculation yields increases, particularly at short lags. Roughly, positions 20 to 200 in the window appear to have the most persistent effects, with a measurable benefit even at lag 256.

The effectiveness of recirculation depends not only on token position, but also token content. We tag each token with a grammatical part-of-speech (PoS) and then determine the mean recirculation benefit for each PoS regardless of token position. Figure 9 c indicates that adverbs, adjectives, and verbs show the biggest effects, whereas fixed classes such as numerals, determiners, and pronouns show the smallest effects. We obtain supporting evidence in experiments where we recirculate all and only tokens of a given PoS (Appendix C.4 ) compared to a count matched random set. Interestingly, for nouns we find that plural forms yield robust benefits whereas singular forms do not. The distinction in how models process singular and plural nouns was also noted by Galashov et al. (2025) .

In contrast to the above experiment, in which we recirculated only a single token, we also conducted an experiment in which we recirculated all-but-one token. We obtain results complementary to Figures 9 a,b, hinting that the benefit of recirculating individual tokens is additive in log likelihood. In all, the position and content effects seem to further rule out artifactual explanations for the phenomenon, and to support the story that recirculation helps construct persistent state representations.

### 4.5 Generative tasks

We evaluated a range of downstream tasks that require models to generate responses, both single-token choices and thinking responses. Broadly, we observe modest to significant improvements in model accuracy.

#### 4.5.1 Instruction following

In a simple instruction-following task, we prompted models with text that included: ⬇

Exact prompts, which included two-shot examples, and additional details are presented in Appendix D.1 . This task is appealing as a test of executive function in children and neurological patients. The baseline Gemma3 1B IT (instruction tuned) model performs at chance, which is why we focus on the larger Gemma3 4B and 12B models. Larger models, despite being better, still have room for improvement as evident in Figure 10 . Using the hyperparameters we previously selected to minimize perplexity on a tuning set, recirculation reduces the error rate by about 25% for the 4B model and by 75% for the 12B model. To get an upper bound on recirculation’s potential, we overfit by performing a hyperparameter sweep specifically to maximize accuracy on this instruction-following task. Although this sweep constrains just two parameters (layer indices), recirculation improves significantly, as shown by the task-specific bars of Figure 10 .

#### 4.5.2 Contextualization

Lepori et al. (2025) curated a dataset to explore model contextualization failures of the sort that occur in the bank dialog (Figure 2 a). Each dataset instance consists of a context , a cue , and a question , includes zero or more embedded distractor sentences , and demands a yes/no answer, e.g., ⬇

Examples were counterbalanced to ensure that biases (e.g., to prefer one sense of the word bank) did not influence results. Specifically, for model responses to count as correct, the model must respond to two variants of the question, e.g., Is it a financial institution? and Is it a geographical feature? Thus, chance accuracy is 25%.

In addition to questions with polysemous words like the example above, there were factual and gender-related questions, e.g., ⬇

Figure 11 shows results for the Gemma3 1B, 4B, and 12B IT models. The abscissa of each graph is the number of distractor sentences; performance tends to drop with more distractors. Shown separately in each graph are the three question types and results for the baseline (solid) and recirculation (dashed) models. The chance rate of 25% is depicted as a dotted horizontal line.

For 1B, two of the three question types show a clear improvement with recirculation; the third is at chance for both baseline and recirculation. For 4B, two of the three question types again show a reliable improvement with recirculation; the third is about the same. For 12B, two of the three question types are at a disadvantage with recirculation; the third is at ceiling for both. On balance, recirculation is a win, though its failure on 12B is disappointing. We used source and destination hyperparameters based on perplexity evaluations in Section 4.2 for a pretrained not instruction tuned model; sweeping hyperparameters with the instruction tuned model did result in larger gains (see Appendix D.2 ).

#### 4.5.3 Multiple-choice and single-token response tasks

We turn now to standard benchmark datasets, including those from Open LLM Leaderboard (v1) ( Beeching et al., 2023 ) , tested using the eval-harness package ( Gao et al., 2024 ) . The tasks we evaluate are: ARC easy ( Clark et al., 2018 ) , ARC challenge ( Clark et al., 2018 ) , MMLU ( Hendrycks et al., 2021 ) , Winogrande ( Sakaguchi et al., 2021 ) , BoolQ ( Clark et al., 2019 ) , PiQA ( Bisk et al., 2020 ) , HellaSwag ( Zellers et al., 2019 ) , and Lambada ( Paperno et al., 2016 ) . Lambada is a fill-in-the-blank single token response task. All the rest are multiple-choice tasks. Accuracy is measured as the percent correct responses. We use the MMLU development set to search over hyperparameters, as detailed in Appendix D.3 . All results are based on zero-shot evaluation.

Table 2 shows accuracy for the eight datasets in the first column for the baseline (second column) and recirculation (third column) models. Recirculation improves performance on six of the eight datasets, although the accuracy differences—both positive and negative—are modest. Disregard the last four columns of Table 2 for the moment; we discuss them in Section 4.6 .

#### 4.5.4 GSM8k

In contrast to the single-token-response datasets examined in the previous section, we turn to problems that are solved with chain-of-thought reasoning ( Kojima et al., 2022 ; Wei et al., 2023 ) , specifically the grade-school math problems in GSM8k ( Cobbe et al., 2021 ) . With single-token responses, any benefit of recirculation must depend on inferences made in processing the problem statement; with chain of thought, recirculation has the additional opportunity to support extended reasoning.

GSM8k also contrasts with the previous datasets in that it allows for a large set of candidate responses. When the number of candidates is large, improvements in model performance can be characterized in terms of either capability sharpening or capability expansion ( Yue et al., 2025 ) . The distinction is made with pass@k metrics ( Yue et al., 2025 ) : improved model performance with pass@1 (greedy decoding) indicates sharpening—the correct response beating out other responses in the set of candidates; improved model performance with pass@128 (accepting any of 128 samples if they are correct) indicates expansion of the set of possibilities. We therefore examine model performance with pass@1 (greedy decoding) and pass@128 (using a higher temperature and nucleus sampling, as recommended by Gemma Team et al. , 2024 ). Presented results are based on zero-shot evaluation. Following Kojima et al. (2022) , we use the zero-shot chain-of-thought prompt, which is important without few-shot examples as we are only evaluating base models in our case.

Figure 12 compares baseline and recirculated Gemma3 4B models (brown and blue bars, respectively) for pass@1 and pass@128. We turn to the green bar in Section 4.6 . Recirculation improves both pass@1 and pass@128 performance, indicating its support for both capability sharpening and capability expansion. Recirculation appears to benefit extended generative responses more than single-token responses (Section 4.5.3 ), thus revealing its promise for advanced problem solving and complex reasoning.

### 4.6 Adaptive recirculation

Our strategy to this point has been to determine how far we could push recirculation as a pure inference-time technique for an off-the-shelf model. Recirculation is surprising and intriguing specifically because it works out-of-the-box. The blindingly obvious next step is to improve the robustness and gains from recirculation via model adaptation. Because training a recurrent architecture comes at a high cost and there is a risk of overfitting if the entire model is fine tuned, we begin by taking small steps away from the training-free setting, focusing on modulating the recirculation hyperparameters α \alpha and β \beta (Equation 1 ). Our goal is to make changes as minimal as possible that show benefits over the training-free recirculation setting.

For training experiments, we use 250 documents from each of arXiv, C4, and PG19. Experiments are conducted with Gemma3 1B PT. We fix the source and destination layer indices that produced earlier recirculation results (Table 1 ) and explore methods that learn representation-mixing terms α \alpha and β \beta to minimize prediction loss.

We score six different adaptation methods on nine datasets by the reduction in evaluation-set perplexity they achieve relative to the baseline (no recirculation) model. Experimental details are presented in Appendix D.5 . The six alternative methods, shown from left to right in Figure 13 , are as follows. • Fixed. We use the fixed, previously determined coefficients ( α = 0.15 \alpha=0.15 , β = 0.85 \beta=0.85 ), thereby replicating earlier results.

• Learned constant scalars . We perform gradient descent in the scalars α \alpha and β \beta to best fit the training data.

• Learned conditional scalars . We train an MLP that maps the token-specific source and destination embeddings to scalar α \alpha and β \beta values, allowing the model to self-determine the strength of recirculation for each token.

• Learned constant vectors. Instead of scaling the source and destination vectors by constants when recirculating, we scale by learned vector-valued 𝜶 \boldsymbol{\alpha} and 𝜷 \boldsymbol{\beta} : 𝒛 t + 1 , t , d = 𝜶 ∘ f ⁡ ( 𝒛 t , t , s ) + 𝜷 ∘ 𝒛 t , t , d , {\boldsymbol{z}}_{t+1,t,d}=\boldsymbol{\alpha}\circ f({\boldsymbol{z}}_{t,t,s})+\boldsymbol{\beta}\circ{\boldsymbol{z}}_{t,t,d}, (3) where ∘ \circ is the Hadamard product.

• Learned conditional vectors. We train an MLP that maps the token-specific source and destination embeddings to vector-valued 𝜶 \boldsymbol{\alpha} and 𝜷 \boldsymbol{\beta} .

• Model fine tuning. We fine tune the Gemma3 1B architecture augmented with the recurrent connections of recirculation. We fix the mixture coefficients at α = 0.15 \alpha=0.15 and β = 0.85 \beta=0.85 .

Of the methods that learn coefficients α \alpha and β \beta , the two that learn vector valued coefficients (fourth and fifth sets) perform better than those that learn scalar coefficients (second and third sets). And the two methods that learn token-conditional coefficients (third and fifth set) outperform the two methods that learn static coefficients (second and fourth set). Of the four methods, the best (fifth set: learned conditional vector 𝜶 , 𝜷 \boldsymbol{\alpha},\boldsymbol{\beta} ) trains an MLP to generate token-specific mixture vectors. The other methods (second, third, and fourth sets) can be considered ablations demonstrating that both vector-valued coefficients and conditioning on the current token is essential. Henceforth, we refer to the superior method as adaptive recirculation .

Adaptive recirculation obtains a mean 23.0% reduction in perplexity, relative to the 8.5% reduction for basic recirculation. Adaptive recirculation beats recirculation for each of the nine datasets (see Figure D.6 ). Adaptive recirculation performs at least as well as full Gemma3 1B fine tuning (23.0% versus 21.6%). The advantage of adaptive recirculation is that the Gemma3 model itself is untouched and therefore there is less risk of overfitting the model via fine tuning.

On downstream tasks, adaptive recirculation also shows promise, with the caveat that the dataset used for training the MLP is critical. Returning to the eight single-token-response datasets, the last four columns of Table 2 present accuracy for adaptive recirculation on these evaluation datasets for four different training datasets. Adapting to a small fraction of the MMLU test split (3600 of about 14000 examples) yields robust across-the-board improvements, and adapting to MMLU (auxiliary train split) yields on balance improvements. For comparability, we use the full test set of MMLU for evaluation even when training on the MMLU test split, which includes the examples used for training; performance on other datasets highlights generalization. Note that the auxiliary train set for MMLU is in general much lower quality than the well-curated MMLU test set, which may be the reason for its inferior performance. Finally, the MMLU train set is based on a combination of existing datasets, with potential contamination ( Hendrycks et al., 2021 ) . Training directly on other datasets such as ARC Easy or ARC Challenge produces significant drops in performance, although these datasets have a much smaller number of examples. Details of these experiments are provided in Appendix D.5 .

Although neither recirculation nor adaptive recirculation yield robust accuracy gains on single-token response tasks, the gains for GSM8k offer a promising signal for extended generative response tasks. The green bar in each panel of Figure 12 shows GSM8k performance with adaptive recirculation. Adaptive recirculation greatly benefits GSM8k, yielding 8.8% and 20.9% reductions in error rate with pass@1 and pass@128, respectively—a staggering result considering the model itself is untouched.

## 5 Discussion

Our work explores the consequences of recirculation, a training-free, inference-time architectural modification to incorporate recurrence into a transformer for improved state tracking. We have shown that for the Gemma3 pretrained and instruction-tuned architectures, recirculation yields notable reductions in model perplexity and enhances models’ ability to follow instructions, answer questions, and problem solve. When generating responses, recirculation incurs almost no additional computation cost; although recirculation requires running two transformer stacks in parallel instead of a single stack, modern AI hardware parallelizes efficiently in this case. However, there is an additional cost of processing the prefill context autoregressively, which for large-context problems, can be quite slow.

Although there is a robust literature on architectural improvements to the transformer, this literature focuses almost exclusively on training models from scratch or incorporating modifications mid-training. The notable exception is the notion of training-free looping ( Li et al., 2025b ; Chen et al., 2026 ; Ng, 2026 ) , a related but distinct architectural modification. Both looping and recirculation exploit a key property of the transformer’s residual pathway: the alignment of representations across layers ( Elhage et al., 2021 ) . Recirculation is complementary to and can be combined with other methods in common practice, including looping, variable computation time, and the coarser-grain recurrence that occurs with both latent thought and chain of thought.

### 5.1 Model-design affordances

We view recirculation not as a ‘shovel ready’ technique to be incorporated into state-of-the-art models, but rather as a methodological or philosophical contribution. By focusing on training-free architectural modifications, we are essentially asking the model to reveal to us its ingrained paths for improvement. Our search over where to place recurrence in the architecture and how to mix and normalize activations is informed by the model itself. The alternative—the typical course of research in machine learning—is to propose an arbitrary modification to an architecture and then evaluate the potential of this modification via costly training. Our key hypothesis is that if we identify how the pretrained model wants us to tweak it without modifying its weights, we also identify an inductive bias that will facilitate and simplify training, whether from scratch or with fine tuning. Our adaptive recirculation experiments support this hypothesis.

In product design, practitioners talk about design affordances ( Norman, 1999 ) , which are properties of an object that inform us about how it should be used. For example, a door handle affords grasping and pulling; a door plate affords pressing. Analogously, our research explores model-design affordances —the natural properties of a foundation model that we can exploit and amplify to improve the model’s basic operation. By improving this basic substrate, we improve all capabilities that build on it. Most approaches to incorporating recurrence within the internal layers of a foundation model do so via adapters or cross attention. Our observations suggest that the simpler strategy of mixing activation vectors may suffice.

### 5.2 Limitations and future directions

We close by discussing limitations of the present work and promising future directions that will address these limitations.

• Determination of optimal hyperparameters. The optimal model hyperparameters—the source and destination layers and the recirculation coefficients α \alpha and β \beta —appear to be domain or problem dependent. However, hyperparameters selected based on one dataset or one criterion often generalize to another. For example, hyperparameters based on perplexity evaluations were used for downstream tasks; hyperparameters based on one specific dataset (MMLU) were used for a range of other single-token-response tasks; and small sets of examples are often sufficient to select hyperparameters. However, unless we can identify task-universal hyperparameters or an automatic mapping from task to hyperparameters, the practical applicability of recirculation will be limited.

• Dependence on model family. While recirculation shows the same qualitative pattern across model families, it is possible that Gemma’s Peri-LN architecture and training optimization process yield larger benefits than other model families (Appendix C.1 ). Generalizability to other architectures requires further investigation.

• Normalization. We find that normalization of source activation vectors makes recirculation behave more robustly. For the Gemma3 family, we find that of the many candidate normalization schemes we investigated, one in particular seems to work well across model sizes (Section B.3 ). Nonetheless, further experiments are needed to determine whether normalization is necessary and how to normalize for other model families.

• Blockwise recurrence. Recirculation is computationally cheap during autoregressive generation because running two stacks in parallel is nearly as efficient with modern hardware as one stack. However, during prefill, token-by-token processing is also required. For state-of-the-art foundation models, which may include a large amount of contextually relevant information, sequential processing of the prefill may be infeasible. One way to alleviate the computational burden would be to perform blockwise recirculation, i.e., to process a set of K K tokens in parallel, and then recirculate those K K tokens simultaneously with the next K K as they are processed for the first pass. We have yet to explore the trade off between K K and recirculation performance.

• Multiple recirculation iterations. A true recurrent network would recirculate the activation in stacks 1 to t − 1 t-1 at step t t . In contrast, the variant of recirculation we explored recirculates only stack t − 1 t-1 , such that each stack is recirculated exactly one time. We have yet to study an intermediate approach in which each stack is recirculated exactly r r times. Figure A.1 shows an unrolled architecture with r = 2 r=2 iterations per stack. We wished to start with the simplest instantiation, but given the low cost of recirculating r r stacks in parallel, increasing the number of iterations is worthwhile.

• Multiple recirculation paths. We picked a single {source, destination} pair for recirculation, but one could recirculate along multiple paths simultaneously. Indeed, for some architectures (e.g., see Gemma3 4B and 12B recirculation sweeps in Figure 8 ), there appeared to be distinct, disjoint regions of the hyperparameter sweep where recirculation was effective. One hypothesis is that these distinct regions are complementary, e.g., they may convey state information at different levels of abstraction.

• Adaptation. The present work has only scratched the surface of possible approaches to adapting models to enhance recirculation effects. Our results with adaptive recirculation are extremely promising considering that the tuning set we used was quite small and that tuning of model weights was not required to obtain robust performance improvements. Before turning to model-weight fine tuning, many avenues for improvement still exist, e.g., token conditioned recirculation pathways and normalization methods.

By listening to the model’s own internal dynamics rather than forcing costly architectural overhauls, recirculation offers a powerful, computationally inexpensive path forward. Unlocking these intrinsic affordances may solidify the model’s basic contextual understanding, which in turn provides the vital scaffolding required for extended, multi-turn reasoning.

## 6 Acknowledgements

Our thanks to Lei Bao, Mukul Bhutani, and Lan Le who contributed to the shaping of this research. We are also grateful to Michael Riegler and Klas Pettersen (SimulaMet, Norway), Patrick Haller (Humbolt U., Berlin), and Jonathan Yanay for their independent replications and constructive discussions of our results.

## References

Alabdulmohsin and Zhai (2025) I. Alabdulmohsin and X. Zhai Recursive inference scaling: a winning path to scalable inference in language and multimodal systems . In The Thirty-ninth Annual Conference on Neural Information Processing Systems , External Links: Link Cited by: §3 , §4.4.3 .

Allen-Zhu (2025) Z. Allen-Zhu Physics of language models: part 4.1, architecture design and the magic of canon layers . Note: arXiv:2512.17351 [cs.CL] External Links: 2512.17351 , Link Cited by: §3 .

Arditi et al. (2024) A. Arditi, O. Obeso, A. Syed, D. Paleka, N. Panickssery, W. Gurnee, and N. Nanda Refusal in language models is mediated by a single direction . Advances in Neural Information Processing Systems 37 , pp. 136037–136083 . Cited by: §3 .

Bae et al. (2025) S. Bae, Y. Kim, R. Bayat, S. Kim, J. Ha, T. Schuster, A. Fisch, H. Harutyunyan, Z. Ji, A. Courville, and S. Yun Mixture-of-recursions: learning dynamic recursive depths for adaptive token-level computation . In The Thirty-ninth Annual Conference on Neural Information Processing Systems , External Links: Link Cited by: §3 .

Beeching et al. (2023) E. Beeching, C. Fourrier, N. Habib, S. Han, N. Lambert, N. Rajani, O. Sanseviero, L. Tunstall, and T. Wolf Open llm leaderboard (2023-2024) . Hugging Face . Note: https://huggingface.co/spaces/open-llm-leaderboard-old/open_llm_leaderboard Cited by: §4.5.3 .

Biran et al. (2024) E. Biran, D. Gottesman, S. Yang, M. Geva, and A. Globerson Hopping too late: exploring the limitations of large language models on multi-hop queries . In Proceedings of the 2024 Conference on Empirical Methods in Natural Language Processing , Y. Al-Onaizan, M. Bansal, and Y. Chen (Eds.) , Miami, Florida, USA , pp. 14113–14130 . External Links: Link , Document Cited by: §3 .

Bisk et al. (2020) Y. Bisk, R. Zellers, R. L. Bras, J. Gao, and Y. Choi PIQA: reasoning about physical commonsense in natural language . In Thirty-Fourth AAAI Conference on Artificial Intelligence , Cited by: §4.5.3 .

Borazjanizadeh and McClelland (2026) N. Borazjanizadeh and J. McClelland Modeling language as a sequence of thoughts . Note: arXiv:2512.25026 [cs.CL] External Links: 2512.25026 , Link Cited by: §3 .

Bulatov et al. (2022) A. Bulatov, Y. Kuratov, and M. Burtsev Recurrent memory transformer . In Advances in Neural Information Processing Systems , S. Koyejo, S. Mohamed, A. Agarwal, D. Belgrave, K. Cho, and A. Oh (Eds.) , Vol. 35 , pp. 11079–11091 . External Links: Link Cited by: §3 .

Cai et al. (2026) Z. Cai, X. Zhu, Y. Dong, Y. He, and S. Arora T 2 {}^{2} MLR: Transformer with temporal middle-layer recurrence . Note: arXiv:2607.15178 [cs.CL] External Links: 2607.15178 , Link Cited by: §3 .

Chen et al. (2026) L. Chen, J. Li, C. Liang, N. Lao, and Q. Liu Training-free looped transformers . Note: arXiv:2605.23872 [cs.CL] External Links: 2605.23872 , Link Cited by: §3 , §4.4.3 , §5 .

Chen et al. (2025a) Y. Chen, J. Shang, Z. Zhang, Y. Xie, J. Sheng, T. Liu, S. Wang, Y. Sun, H. Wu, and H. Wang Inner thinking transformer: leveraging dynamic depth scaling to foster adaptive internal thinking . Note: arXiv:2502.13842 [cs.CL] External Links: 2502.13842 Cited by: §3 .

Chen et al. (2025b) Y. Chen, D. Hutchins, A. Jansen, A. Zhmoginov, D. Racz, and J. S. Andersen MELODI: exploring memory compression for long contexts . In The Thirteenth International Conference on Learning Representations , External Links: Link Cited by: §3 .

Chevalier et al. (2023) A. Chevalier, A. Wettig, A. Ajith, and D. Chen Adapting language models to compress contexts . Note: arXiv:2305.14788 [cs.CL] External Links: 2305.14788 , Link Cited by: §3 .

Clark et al. (2019) C. Clark, K. Lee, M. Chang, T. Kwiatkowski, M. Collins, and K. Toutanova BoolQ: exploring the surprising difficulty of natural yes/no questions . In NAACL , Cited by: §4.5.3 .

Clark et al. (2018) P. Clark, I. Cowhey, O. Etzioni, T. Khot, A. Sabharwal, C. Schoenick, and O. Tafjord Think you have solved question answering? Try ARC, the AI2 reasoning challenge . arXiv preprint arXiv:1803.05457 . Cited by: §4.5.3 .

Cobbe et al. (2021) K. Cobbe, V. Kosaraju, M. Bavarian, M. Chen, H. Jun, L. Kaiser, M. Plappert, J. Tworek, J. Hilton, R. Nakano, C. Hesse, and J. Schulman Training verifiers to solve math word problems . arXiv preprint arXiv:2110.14168 . Cited by: §4.5.4 .

Dathathri et al. (2020) S. Dathathri, A. Madotto, J. Lan, J. Hung, E. Frank, P. Molino, J. Yosinski, and R. Liu Plug and play language models: a simple approach to controlled text generation . In International Conference on Learning Representations , External Links: Link Cited by: §3 .

Davidson et al. (2025) T. R. Davidson, A. Fourney, S. Amershi, R. West, E. Horvitz, and E. Kamar The collaboration gap . Note: arXiv:2511.02687 [cs.AI] External Links: 2511.02687 , Link Cited by: §1 .

Dehghani et al. (2019) M. Dehghani, S. Gouws, O. Vinyals, J. Uszkoreit, and L. Kaiser Universal transformers . In International Conference on Learning Representations , External Links: Link Cited by: §2 , §3 , §4.4.3 .

Elhage et al. (2021) N. Elhage, N. Nanda, C. Olsson, T. Henighan, N. Joseph, B. Mann, A. Askell, Y. Bai, A. Chen, T. Conerly, N. DasSarma, D. Drain, D. Ganguli, Z. Hatfield-Dodds, D. Hernandez, A. Jones, J. Kernion, L. Lovitt, K. Ndousse, D. Amodei, T. Brown, J. Clark, J. Kaplan, S. McCandlish, and C. Olah A mathematical framework for transformer circuits . Transformer Circuits Thread . Note: https://transformer-circuits.pub/2021/framework/index.html Cited by: §1 , §5 .

Fan et al. (2021) A. Fan, T. Lavril, E. Grave, A. Joulin, and S. Sukhbaatar Addressing some limitations of transformers with feedback memory . Note: arXiv:2002.09402 [cs.CL] External Links: 2002.09402 , Link Cited by: §3 .

Galashov et al. (2025) A. Galashov, M. Jones, R. Ke, Y. Cao, V. Nagarajan, and M. C. Mozer Catch your breath: adaptive computation for self-paced sequence production . Note: arXiv:2510.13879 [cs.CL] External Links: 2510.13879 , Link Cited by: §4.4.4 .

Gao et al. (2025) L. Gao, T. Dupre la Tour, H. Tillman, G. Goh, R. Troll, A. Radford, I. Sutskever, J. Leike, and J. Wu Scaling and evaluating sparse autoencoders . In International Conference on Learning Representations , Vol. 2025 , pp. 26721–26754 . Cited by: §3 .

Gao et al. (2024) L. Gao, J. Tow, B. Abbasi, S. Biderman, S. Black, A. DiPofi, C. Foster, L. Golding, J. Hsu, A. Le Noac’h, H. Li, K. McDonell, N. Muennighoff, C. Ociepa, J. Phang, L. Reynolds, H. Schoelkopf, A. Skowron, L. Sutawika, E. Tang, A. Thite, B. Wang, K. Wang, and A. Zou The language model evaluation harness . Note: Zenodohttps://zenodo.org/records/12608602 External Links: Document Cited by: §4.5.3 .

Geiping et al. (2025) J. Geiping, S. M. McLeish, N. Jain, J. Kirchenbauer, S. Singh, B. R. Bartoldson, B. Kailkhura, A. Bhatele, and T. Goldstein Scaling up test-time compute with latent reasoning: a recurrent depth approach . In The Thirty-ninth Annual Conference on Neural Information Processing Systems , External Links: Link Cited by: §3 .

Gemma Team et al. (2024) Gemma Team, T. Mesnard, C. Hardin, R. Dadashi, S. Bhupatiraju, S. Pathak, L. Sifre, M. Rivière, M. S. Kale, J. Love, P. Tafti, L. Hussenot, P. G. Sessa, A. Chowdhery, A. Roberts, A. Barua, A. Botev, A. Castro-Ros, A. Slone, A. Héliou, A. Tacchetti, A. Bulanova, A. Paterson, B. Tsai, B. Shahriari, C. L. Lan, C. A. Choquette-Choo, C. Crepy, D. Cer, D. Ippolito, D. Reid, E. Buchatskaya, E. Ni, E. Noland, G. Yan, G. Tucker, G. Muraru, G. Rozhdestvenskiy, H. Michalewski, I. Tenney, I. Grishchenko, J. Austin, J. Keeling, J. Labanowski, J. Lespiau, J. Stanway, J. Brennan, J. Chen, J. Ferret, J. Chiu, J. Mao-Jones, K. Lee, K. Yu, K. Millican, L. L. Sjoesund, L. Lee, L. Dixon, M. Reid, M. Mikuła, M. Wirth, M. Sharman, N. Chinaev, N. Thain, O. Bachem, O. Chang, O. Wahltinez, P. Bailey, P. Michel, P. Yotov, R. Chaabouni, R. Comanescu, R. Jana, R. Anil, R. McIlroy, R. Liu, R. Mullins, S. L. Smith, S. Borgeaud, S. Girgin, S. Douglas, S. Pandya, S. Shakeri, S. De, T. Klimenko, T. Hennigan, V. Feinberg, W. Stokowiec, Y. Chen, Z. Ahmed, Z. Gong, T. Warkentin, L. Peran, M. Giang, C. Farabet, O. Vinyals, J. Dean, K. Kavukcuoglu, D. Hassabis, Z. Ghahramani, D. Eck, J. Barral, F. Pereira, E. Collins, A. Joulin, N. Fiedel, E. Senter, A. Andreev, and K. Kenealy Gemma: open models based on Gemini research and technology . Note: arXiv:2403.08295 [cs.CL] External Links: 2403.08295 , Link Cited by: §4.5.4 , footnote 3 .

Ghandeharioun et al. (2024) A. Ghandeharioun, A. Caciularu, A. Pearce, L. Dixon, and M. Geva Patchscopes: a unifying framework for inspecting hidden representations of language models . In Proceedings of the 41st International Conference on Machine Learning , ICML’24 . Cited by: §1 .

Giannou et al. (2023) A. Giannou, S. Rajput, J. Sohn, K. Lee, J. D. Lee, and D. Papailiopoulos Looped transformers as programmable computers . In International Conference on Machine Learning , pp. 11398–11442 . Cited by: §2 , §3 , §4.4.3 .

Gu and Dao (2024) A. Gu and T. Dao Mamba: linear-time sequence modeling with selective state spaces . In First Conference on Language Modeling , External Links: Link Cited by: §3 .

Hao et al. (2025) S. Hao, S. Sukhbaatar, D. Su, X. Li, Z. Hu, J. E. Weston, and Y. Tian Training large language models to reason in a continuous latent space . In Second Conference on Language Modeling , External Links: Link Cited by: §3 .

Hendrycks et al. (2021) D. Hendrycks, C. Burns, S. Basart, A. Zou, M. Mazeika, D. Song, and J. Steinhardt Measuring massive multitask language understanding . Proceedings of the International Conference on Learning Representations (ICLR) . Cited by: §4.5.3 , §4.6 .

Hu et al. (2025) E. S. Hu, K. Ahn, Q. Liu, H. Xu, M. Tomar, A. Langford, D. Jayaraman, A. Lamb, and J. Langford The belief state transformer . In The Thirteenth International Conference on Learning Representations , External Links: Link Cited by: §3 .

Huang et al. (2026) H. Huang, Y. LeCun, and R. Balestriero Semantic tube prediction: beating LLM data efficiency with JEPA . Note: arXiv:2602.22617 [cs.LG] External Links: 2602.22617 , Link Cited by: §3 .

Hutchins et al. (2022) D. Hutchins, I. Schlag, Y. Wu, E. Dyer, and B. Neyshabur Block-recurrent transformers . In Advances in Neural Information Processing Systems , S. Koyejo, S. Mohamed, A. Agarwal, D. Belgrave, K. Cho, and A. Oh (Eds.) , Vol. 35 , pp. 33248–33261 . External Links: Link Cited by: §3 .

Jabri et al. (2023) A. Jabri, D. Fleet, and T. Chen Scalable adaptive computation for iterative generation . Note: arXiv:2212.11972 [cs.LG] External Links: 2212.11972 , Link Cited by: §3 .

Jeddi et al. (2026) A. Jeddi, M. Ciccone, and B. Taati LoopFormer: elastic-depth looped transformers for latent reasoning via shortcut modulation . In The Fourteenth International Conference on Learning Representations , External Links: Link Cited by: §3 .

Johnson-Laird (1983) P.N. Johnson-Laird Mental models: towards a cognitive science of language, inference, and consciousness . Cognitive science series , Harvard University Press . External Links: ISBN 9780674568822 , LCCN 83004333 , Link Cited by: §1 .

Jolicoeur-Martineau (2025) A. Jolicoeur-Martineau Less is more: recursive reasoning with tiny networks . Note: arXiv:2510.04871 [cs.LG] External Links: 2510.04871 , Link Cited by: §3 .

Katharopoulos et al. (2020) A. Katharopoulos, A. Vyas, N. Pappas, and F. Fleuret Transformers are RNNs: fast autoregressive transformers with linear attention . In Proceedings of the 37th International Conference on Machine Learning , Proceedings of Machine Learning Research , Vol. 119 , pp. 5156–5165 . Cited by: §3 .

Khatua et al. (2026) A. Khatua, H. Zhu, P. Tran, A. Prabhudesai, F. Sadrieh, J. K. Lieberwirth, X. Yu, Y. Fu, M. J. Ryan, J. Pei, and D. Yang CooperBench: why coding agents cannot be your teammates yet . Note: arXiv:2601.13295 [cs.LG] External Links: 2601.13295 , Link Cited by: §1 .

Kim et al. (2025) J. Kim, B. Lee, C. Park, Y. Oh, B. Kim, T. Yoo, S. Shin, D. Han, J. Shin, and K. M. Yoo Peri-ln: revisiting normalization layer in the transformer architecture . arXiv preprint arXiv:2502.02732 . Cited by: 1st item .

Koishekenov et al. (2025) Y. Koishekenov, A. Lipani, and N. Cancedda Encode, think, decode: scaling test-time reasoning with recursive latent thoughts . Note: arXiv:2510.07358 [cs.LG] External Links: 2510.07358 , Link Cited by: §3 .

Kojima et al. (2022) T. Kojima, S. S. Gu, M. Reid, Y. Matsuo, and Y. Iwasawa Large language models are zero-shot reasoners . Advances in neural information processing systems 35 , pp. 22199–22213 . Cited by: §4.5.4 , §4.5.4 .

Laban et al. (2025) P. Laban, H. Hayashi, Y. Zhou, and J. Neville LLMs get lost in multi-turn conversation . Note: arXiv:2505.06120 [cs.CL] External Links: 2505.06120 , Link Cited by: §1 .

Lepori et al. (2025) M. A. Lepori, M. C. Mozer, and A. Ghandeharioun Racing thoughts: explaining contextualization errors in large language models . In Proceedings of the 2025 Conference of the Nations of the Americas Chapter of the Association for Computational Linguistics: Human Language Technologies (Volume 1: Long Papers) , L. Chiruzzo, A. Ritter, and L. Wang (Eds.) , Albuquerque, New Mexico , pp. 3020–3036 . External Links: Link , Document , ISBN 979-8-89176-189-6 Cited by: Figure D.2 , Figure D.2 , Figure D.3 , Figure D.3 , Figure D.4 , Figure D.4 , §D.2 , Figure 1 , Figure 1 , Figure 2 , Figure 2 , §1 , §1 , §1 , §1 , §3 , Figure 11 , Figure 11 , §4.5.2 .

Li et al. (2025a) B. Z. Li, Z. C. Guo, and J. Andreas (How) do language models track state? . In Forty-second International Conference on Machine Learning , External Links: Link Cited by: §1 , §3 .

Li et al. (2024) Z. Li, H. Liu, D. Zhou, and T. Ma Chain of thought empowers transformers to solve inherently serial problems . In The Twelfth International Conference on Learning Representations , External Links: Link Cited by: §3 .

Li et al. (2025b) Z. Li, Y. Li, and T. Zhou Skip a layer or loop it? Test-time depth adaptation of pretrained LLMs . Note: arXiv:2507.07996 [cs.LG] External Links: 2507.07996 , Link Cited by: §3 , §4.4.3 , §5 .

Liu et al. (2020) L. Liu, X. Liu, J. Gao, W. Chen, and J. Han Understanding the difficulty of training transformers . In Proceedings of the 2020 Conference on Empirical Methods in Natural Language Processing (EMNLP) , B. Webber, T. Cohn, Y. He, and Y. Liu (Eds.) , Online , pp. 5747–5763 . External Links: Link , Document Cited by: §B.3 .

Liu et al. (2026) Y. Liu, K. Preechakul, K. Kuwaranancharoen, and Y. Bai The serial scaling hypothesis . Note: arXiv:2507.12549 [cs.LG] External Links: 2507.12549 , Link Cited by: §3 .

Loshchilov and Hutter (2019) I. Loshchilov and F. Hutter Decoupled weight decay regularization . In International Conference on Learning Representations , External Links: Link Cited by: §D.5 .

Marks and Tegmark (2023) S. Marks and M. Tegmark The geometry of truth: emergent linear structure in large language model representations of true/false datasets . arXiv preprint arXiv:2310.06824 . Cited by: §3 .

McLeish et al. (2025) S. McLeish, A. Li, J. Kirchenbauer, D. S. Kalra, B. R. Bartoldson, B. Kailkhura, A. Schwarzschild, J. Geiping, T. Goldstein, and M. Goldblum Teaching pretrained language models to think deeper with retrofitted recurrence . Note: arXiv:2511.07384 [cs.CL] External Links: 2511.07384 , Link Cited by: §3 .

Merrill et al. (2025) W. Merrill, J. Petty, and A. Sabharwal The illusion of state in state-space models . Note: arXiv:2404.08819 [cs.LG] External Links: 2404.08819 , Link Cited by: §3 .

Merrill and Sabharwal (2023) W. Merrill and A. Sabharwal The parallelism tradeoff: limitations of log-precision transformers . Transactions of the Association for Computational Linguistics 11 , pp. 531–545 . External Links: Link , Document Cited by: §3 .

Merrill and Sabharwal (2024) W. Merrill and A. Sabharwal The expressive power of transformers with chain of thought . In The Twelfth International Conference on Learning Representations , External Links: Link Cited by: §3 .

Merrill and Sabharwal (2025) W. Merrill and A. Sabharwal A little depth goes a long way: the expressive power of log-depth transformers . Note: arXiv:2503.03961 [cs.LG] External Links: 2503.03961 , Link Cited by: §3 .

Mozer et al. (2026) M. C. Mozer, S. A. Siddiqui, and R. Liu The topological trouble with transformers . Note: arXiv:2604.17121 [cs.LG] External Links: 2604.17121 , Link Cited by: §1 , §2 , §3 .

Ng (2026) D. N. Ng LLM neuroanatomy: how I topped the LLM leaderboard without changing a single weight . Note: https://dnhkng.github.io/posts/rys/ Cited by: §3 , §4.4.3 , §5 .

Nikankin et al. (2025) Y. Nikankin, D. Arad, Y. Gandelsman, and Y. Belinkov Same task, different circuits: disentangling modality-specific mechanisms in vlms . Note: arXiv:2506.09047 [cs.LG] External Links: 2506.09047 , Link Cited by: footnote 1 .

Norman (1999) D. A. Norman Affordance, conventions, and design . Interactions 6 ( 3 ), pp. 38–43 . External Links: ISSN 1072-5520 , Link , Document Cited by: §5.1 .

Nowak et al. (2024) A. I. Nowak, O. Mercea, A. Arnab, J. Pfeiffer, Y. Dauphin, and U. Evci Towards optimal adapter placement for efficient transfer learning . Note: arXiv:2410.15858 [cs.LG] External Links: 2410.15858 , Link Cited by: §3 .

Oh et al. (2026) G. Oh, W. Cho, S. Kim, S. Choi, and Y. Yu Revisiting residual connections: orthogonal updates for stable and efficient deep networks . In The Thirty-ninth Annual Conference on Neural Information Processing Systems , External Links: Link Cited by: footnote 2 .

Paperno et al. (2016) D. Paperno, G. Kruszewski, A. Lazaridou, N. Pham, R. Bernardi, S. Pezzelle, M. Baroni, G. Boleda, and R. Fernández The LAMBADA dataset: word prediction requiring a broad discourse context . In Proceedings of the 54th Annual Meeting of the Association for Computational Linguistics (Volume 1: Long papers) , pp. 1525–1534 . Cited by: §4.5.3 .

Peng et al. (2025) B. Peng, R. Zhang, D. Goldstein, E. Alcaide, X. Du, H. Hou, J. Lin, J. Liu, J. Lu, W. Merrill, G. Song, K. Tan, S. Utpala, N. Wilce, J. S. Wind, T. Wu, D. Wuttke, and C. Zhou-Zheng RWKV-7 ”goose” with expressive dynamic state evolution . In Second Conference on Language Modeling , External Links: Link Cited by: §3 .

Piotrowski et al. (2025) M. Piotrowski, P. M. Riechers, D. Filan, and A. S. Shai Constrained belief updates explain geometric structures in transformer representations . Note: arXiv:2502.01954 [cs.LG] External Links: 2502.01954 , Link Cited by: §1 , §3 .

Prakash et al. (2026) N. Prakash, N. Shapira, A. S. Sharma, C. Riedl, Y. Belinkov, T. R. Shaham, D. Bau, and A. Geiger Language models use lookbacks to track beliefs . In The Fourteenth International Conference on Learning Representations , External Links: Link Cited by: §1 , §3 .

Raposo et al. (2024) D. Raposo, S. Ritter, B. Richards, T. Lillicrap, P. C. Humphreys, and A. Santoro Mixture-of-depths: dynamically allocating compute in transformer-based language models . Note: arXiv:2404.02258 [cs.LG] External Links: 2404.02258 , Link Cited by: §3 .

Rimsky et al. (2024) N. Rimsky, N. Gabrieli, J. Schulz, M. Tong, E. Hubinger, and A. Turner Steering llama 2 via contrastive activation addition . In Proceedings of the 62nd Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers) , pp. 15504–15522 . Cited by: §3 .

Rodkin et al. (2025) I. Rodkin, D. Orel, K. Smirnov, A. Bolatov, B. Elbouardi, B. Hassan, Y. Kuratov, A. Bulatov, P. Nakov, T. Baldwin, A. Shelmanov, and M. Burtsev Beyond memorization: extending reasoning depth with recurrence, memory and test-time compute scaling . Note: arXiv:2508.16745 [cs.LG] External Links: 2508.16745 , Link Cited by: §3 .

Sakaguchi et al. (2021) K. Sakaguchi, R. L. Bras, C. Bhagavatula, and Y. Choi Winogrande: an adversarial winograd schema challenge at scale . Communications of the ACM 64 ( 9 ), pp. 99–106 . Cited by: §4.5.3 .

Sanyal (2026) S. Sanyal Looped-gpt: looping during pre-training improves generalization . Note: Blog https://sanyalsunny111.github.io/posts/2026-01-15-post1-looped-gpt/ Cited by: §3 .

Saunshi et al. (2025) N. Saunshi, N. Dikkala, Z. Li, S. Kumar, and S. J. Reddi Reasoning with latent thoughts: on the power of looped transformers . In The Thirteenth International Conference on Learning Representations , External Links: Link Cited by: §3 .

Sawyer et al. (2025) D. P. Sawyer, N. R. Ke, H. Soyer, M. Engelcke, J. Reid, D. P. Reichert, D. A. Hudson, A. Lerchner, D. J. Rezende, T. P. Lillicrap, M. C. Mozer, and J. X. Wang Exploring exploration with foundation agents in interactive environments . In NeurIPS 2025 Workshop on Embodied World Models for Decision Making , External Links: Link Cited by: §1 , §3 .

Schlag et al. (2021) I. Schlag, K. Irie, and J. Schmidhuber Linear transformers are secretly fast weight programmers . arXiv preprint arXiv:2102.11174 . Cited by: §3 .

Shai et al. (2024) A. Shai, P. M. Riechers, L. Teixeira, A. G. Oldenziel, and S. Marzen Transformers represent belief state geometry in their residual stream . In The Thirty-eighth Annual Conference on Neural Information Processing Systems , External Links: Link Cited by: §1 , §3 .

Siems et al. (2025) J. Siems, T. Carstensen, A. Zela, F. Hutter, M. Pontil, and R. Grazzi DeltaProduct: improving state-tracking in linear RNNs via householder products . In The Thirty-ninth Annual Conference on Neural Information Processing Systems , External Links: Link Cited by: §3 .

Song et al. (2026) P. Song, P. Han, and N. Goodman Large language model reasoning failures . Transactions on Machine Learning Research . Note: Survey Certification External Links: ISSN 2835-8856 , Link Cited by: §1 .

Strobl et al. (2024) L. Strobl, W. Merrill, G. Weiss, D. Chiang, and D. Angluin What formal languages can transformers express? a survey . Transactions of the Association for Computational Linguistics 12 , pp. 543–561 . External Links: ISSN 2307-387X , Document , Link , https://direct.mit.edu/tacl/article-pdf/doi/10.1162/tacl_a_00663/2370911/tacl_a_00663.pdf Cited by: §3 .

Sun et al. (2026) W. Sun, X. Song, P. Li, L. Yin, Y. Zheng, and S. Liu The curse of depth in large language models . Advances in Neural Information Processing Systems 38 , pp. 163104–163136 . Cited by: 1st item .

Sun et al. (2025) Y. Sun, X. Li, K. Dalal, J. Xu, A. Vikram, G. Zhang, Y. Dubois, X. Chen, X. Wang, S. Koyejo, T. Hashimoto, and C. Guestrin Learning to (learn at test time): RNNs with expressive hidden states . In Forty-second International Conference on Machine Learning , External Links: Link Cited by: §3 .

Team et al. (2026) G. Team, S. E. Abd, V. Aggarwal, R. Algayres, A. Andreev, O. Bachem, I. Ballantyne, C. Brick, V. Cărbune, M. Casbon, et al. Gemma 4 technical report . arXiv preprint arXiv:2607.02770 . Cited by: §C.1 .

Teoh et al. (2025) J. Teoh, M. Tomar, K. Ahn, E. S. Hu, P. Sharma, R. Islam, A. Lamb, and J. Langford Next-latent prediction transformers learn compact world models . Note: arXiv:2511.05963 [cs.LG] External Links: 2511.05963 , Link Cited by: §D.5 , §3 .

Turner et al. (2023) A. M. Turner, L. Thiergart, G. Leech, D. Udell, J. J. Vazquez, U. Mini, and M. MacDiarmid Steering language models with activation engineering . arXiv preprint arXiv:2308.10248 . Cited by: §3 .

Tversky and Kahneman (1971) A. Tversky and D. Kahneman Belief in the law of small numbers . Psychological Bulletin 76 ( 2 ), pp. 105–110 . External Links: Document Cited by: §1 .

Venhoff et al. (2025) C. Venhoff, A. Khakzar, S. Joseph, P. Torr, and N. Nanda Too late to recall: explaining the two-hop problem in multimodal knowledge retrieval . In The Thirty-ninth Annual Conference on Neural Information Processing Systems , External Links: Link Cited by: §3 .

Vul et al. (2014) E. Vul, N. Goodman, T. L. Griffiths, and J. B. Tenenbaum One and done? Optimal decisions from very few samples . Cognitive Science 38 ( 4 ), pp. 599–637 . External Links: Document Cited by: §1 .

Wei et al. (2023) J. Wei, X. Wang, D. Schuurmans, M. Bosma, B. Ichter, F. Xia, E. Chi, Q. Le, and D. Zhou Chain-of-thought prompting elicits reasoning in large language models . Note: arXiv:2201.11903 [cs.CL] External Links: 2201.11903 Cited by: §4.5.4 .

Xiao et al. (2024) G. Xiao, Y. Tian, B. Chen, S. Han, and M. Lewis Efficient streaming language models with attention sinks . In International Conference on Learning Representations , Vol. 2024 , pp. 21875–21895 . Cited by: §B.2 .

Xiong et al. (2020) R. Xiong, Y. Yang, D. He, K. Zheng, S. Zheng, C. Xing, H. Zhang, Y. Lan, L. Wang, and T. Liu On layer normalization in the transformer architecture . In Proceedings of the 37th International Conference on Machine Learning , ICML’20 . Cited by: §B.3 , 1st item .

Yang et al. (2024) L. Yang, K. Lee, R. D. Nowak, and D. Papailiopoulos Looped transformers are better at learning learning algorithms . In The Twelfth International Conference on Learning Representations , External Links: Link Cited by: §3 .

Yang et al. (2025) S. Yang, Y. Shen, K. Wen, S. Tan, M. Mishra, L. Ren, R. Panda, and Y. Kim PaTH attention: position encoding via accumulating householder transformations . In The Thirty-ninth Annual Conference on Neural Information Processing Systems , External Links: Link Cited by: §3 .

Yu et al. (2025) Z. Yu, Y. Belinkov, and S. Ananiadou Back attention: understanding and enhancing multi-hop reasoning in large language models . In Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing , C. Christodoulopoulos, T. Chakraborty, C. Rose, and V. Peng (Eds.) , Suzhou, China , pp. 11257–11272 . External Links: Link , Document , ISBN 979-8-89176-332-6 Cited by: §3 .

Yue et al. (2025) Y. Yue, Z. Chen, R. Lu, A. Zhao, Z. Wang, Y. Yue, S. Song, and G. Huang Does reinforcement learning really incentivize reasoning capacity in LLMs beyond the base model? . In The Thirty-ninth Annual Conference on Neural Information Processing Systems , Vol. 38 , pp. 57654–57689 . External Links: Link Cited by: §4.5.4 .

Zellers et al. (2019) R. Zellers, A. Holtzman, Y. Bisk, A. Farhadi, and Y. Choi HellaSwag: can a machine really finish your sentence? . In Proceedings of the 57th Annual Meeting of the Association for Computational Linguistics , Cited by: §4.5.3 .

Zeng et al. (2026) B. Zeng, S. Song, S. Huang, Y. Wang, H. Li, Z. He, X. Wang, Z. li, and Z. Lin PonderLM: pretraining language models to ponder in continuous space . In The Fourteenth International Conference on Learning Representations , External Links: Link Cited by: §3 .

Zhang et al. (2026) M. Zhang, A. Khalifa, S. Bhardwaj, M. C. Mozer, and Y. Dauphin Amplification-free residual networks . Note: arXiv:26xx.xxxxx [cs.LG] External Links: 26xx.xxxxx , Link Cited by: footnote 2 .

Zhu et al. (2025) R. Zhu, Z. Wang, K. Hua, T. Zhang, Z. Li, H. Que, B. Wei, Z. Wen, F. Yin, H. Xing, L. Li, J. Shi, K. Ma, S. Li, T. Kergan, A. Smith, X. Qu, M. Hui, B. Wu, Q. Min, H. Huang, X. Zhou, W. Ye, J. Liu, J. Yang, Y. Shi, C. Lin, E. Zhao, T. Cai, G. Zhang, W. Huang, Y. Bengio, and J. Eshraghian Scaling latent reasoning via looped language models . Note: arXiv:2510.25741 [cs.LG] External Links: 2510.25741 , Link Cited by: §3 .

Zou et al. (2023) A. Zou, L. Phan, S. Chen, J. Campbell, P. Guo, R. Ren, A. Pan, X. Yin, M. Mazeika, A. Dombrowski, et al. Representation engineering: a top-down approach to ai transparency . arXiv preprint arXiv:2310.01405 . Cited by: §3 .

## Appendix A Unrolled recirculation architecture

Figure A.1 shows an unrolled transformer with two iterations of recirculation. In general, with k k iterations of recirculation, it will be necessary to run k + 1 k+1 stacks for each input step.

## Appendix B Recirculation implementation details

### B.1 Hyperparameter sweeps

For the hyperparameter sweeps (Figures 5 and 6 ), we used a context window of 1024 tokens and pulled roughly 500 windows from training documents in three datasets: arXiv, C4, and PG19. We used at most two windows from each document, requiring that the windows had no filler tokens (i.e., the document extended at least to the end of the window). This requirement yielded 484 windows for arXiv (495132 predicted tokens), 488 windows for C4 (499224 tokens), and 500 windows for PG19 (511000 tokens).

### B.2 Perplexity evaluation

For our perplexity evaluation (Table 1 ), we used the entire evaluation set from nine data sets (arXiv, billsum, booksum/books, C4/webtextlike, gov report, lambada, newsroom, PG19, and pubmed) and the first 10000 documents from a tenth data set (big patent). The evaluation split was labeled ‘validation’ for C4 and ‘test’ for all other datasets. We partitioned each document into chunks of 1024 tokens and excluded partially filled windows (i.e., less than 1024 tokens), except for three data sets whose documents were typically too short (c4/webtextlike, lambada, and newsroom). This procedure resulted in the evaluation of the number of tokens listed in the second column of Table 1 .

Based on hyperparameter sweeps for the 1B, 4B, and 12B models, we used the source and destination pairs shown in Table B.1 . These hyperparameters were used for all results presented in the article unless otherwise mentioned.

### B.3 Normalization and ramping

Figures B.1 - B.3 show hyperparameter sweeps for multiple renormalization techniques, i.e., scaling of the source vector when recirculating to the destination layer. Scaling helps to ensure that the source activations do not overwhelm the destination activations, due to the fact that embedding norms increase over transformer layers ( Liu et al., 2020 ; Xiong et al., 2020 ) . The heatmaps depict percentage reduction (negative) or increase (red) in perplexity over our three tuning datasets (arXiv, C4, PG-19).

The normalization schemes are summarized in the Figures and in Table B.2 . We simplify the notation used in the main paper, where 𝒛 i , j , l \boldsymbol{z}_{i,j,l} referred to the embedding at unrolling step i i for input step j j and layer l l . Instead, we denote: d ≡ \displaystyle d\equiv~ 𝒛 t , t , d , \displaystyle\boldsymbol{z}_{t,t,d}, s ≡ \displaystyle s\equiv~ 𝒛 t , t , s ​ , and \displaystyle\boldsymbol{z}_{t,t,s}\text{, and} d ′ ≡ \displaystyle d^{\prime}\equiv~ 𝒛 t + 1 , t , d . \displaystyle\boldsymbol{z}_{t+1,t,d}. The normalization schemes in Table B.2 include the simple scheme in which no normalization is applied. The no-normalization heatmaps (top row, middle panel in Figures B.1 - B.3 ) attain reasonable outcomes but clearly the schemes with L 2 L_{2} normalization (top row, right panel and second row, left panel) are better behaved in the sense that there are fewer hyperparameters that result in poorer performance. Oddly, a convex combination of source and destination vectors (top row, right panel) is superior to a nonconvex combination (second row, left panel) for the Gemma3 1B model, but the nonconvex combination is superior for Gemma3 4B and 12B. Other candidate schemes either had pathologies (non-smooth heatmaps, large red regions) or mimicked the simple norm-ratio schemes. Based on the Gemma family, we recommend evaluating at least the convex and non-convex mixtures with norm-ratio adjustment of the source.

Ramping. As we mentioned in the main article, for the Gemma3 1B model, we found a small additional reduction in perplexity if we ramped up the recirculation coefficient over the first 10 steps. Specifically, we defined the α \alpha coefficient at step t ≥ 0 t\geq 0 to be α t ≡ min ⁡ ( t / 10 , 1 ) ​ α \alpha_{t}\equiv\min(t/10,1)\alpha .

## Appendix C Basic results

### C.1 Robustness across architectures

In Figure 7 , we contrasted recirculation hyperparameter sweeps for Gemma3 1B to four other model families: Ministral3, Qwen3, Pythia, and Phi2. The Figure compares architectures using only the arXiv training set. Due to the fact that all of these models were relatively small, we utilized the same hyperparameters as we did for Gemma3 1B PT: scaling of the source layer norm to match the target layer norm, α = .07 \alpha=.07 and β = 1 − α \beta=1-\alpha . Using β = 1 \beta=1 —the choice for Gemma3 4B and 12B—produced qualitatively similar results.

In addition to the comparison across different model families, we also compared results from Gemma3 with those from other generations of the Gemma model family, including the older Gemma2 and the newer Gemma4 (Figure C.1 ). The arXiv train set is again used in this Figure. The gains for Gemma2 and Gemma4 are as pronounced as those for Gemma3 in the main text, despite the fact that there are regions of the hyperparameter space where recirculation is quite harmful. Note that smaller variants of Gemma4 (i.e., E2B and E4B) uses cross-layer KV cache sharing as well as per-layer embedding, which can explain the instability in these plots ( Team et al., 2026 ) .

We hypothesize that this favorability of Gemma architectures can be attributed to two distinct explanations: • Gemma architectures use a Peri-LN architecture ( Kim et al., 2025 ) which adds layer-norm to both the input of the layer (i.e., self-attention or MLP), as well as the output of the layer. In contrast, other architectures only use input normalization ( Xiong et al., 2020 ) . The use of output normalization might improve the model’s compatibility with recirculation by avoiding diminishing contribution from later layers ( Sun et al., 2026 ) .

• The compatibility with recirculation is strongly dependent on the optimization process used for training the model. Hence, the scheme used to train Gemma models is particularly favorable for recirculation.

### C.2 Recirculation versus temperature tuning

Gemma3 1B with the PG-19 evaluation (‘test’) set was used for temperature tuning experiments. The documents were split into 1024 token chunks per context window; partially filled sequences were excluded. We swept over a wide enough range of softmax temperatures to identify the range in which adjusting model temperature improved perplexity. Figure C.2 shows the sweep without recirculation in the left panel and with recirculation in the right panel. Whether with or without recirculation, the optimal temperature was about 1.2. Although we performed a more granular sweep for the combined experiment, we report in the main paper the optimum over only the range of temperatures used for the temperature-alone experiment.

### C.3 Recirculation versus looping

The dataset is comprised of 250 documents from the arxiv train set, with 2 subsequences taken from each document starting from the beginning of the document, each of size 1024 tokens. This is identical to our setting for the grid search results in Figure 5 . Results for recirculation are shown with α = 0.07 \alpha=0.07 , with convex combination ( β = 0.93 \beta=0.93 ) for the 1B model and a non-convex combination ( β = 1.0 \beta=1.0 ) for the 4B and 12B models, as discussed in the main text.

### C.4 Which tokens benefit from recirculation?

Experiments in the main paper are based on Gemma3 1B PT with the arXiv data set, training split, with a context window of 1024 tokens extracted from a randomly selected position within each document. Part-of-speech tags are extracted with nltk.pos_tag . We processed 24960 documents and for each, we recirculated tokens 0-767 individually and examined downstream effects at lags 1-256.

We also ran an experiment in which we recirculated all and only tokens tagged with a given part of speech (Figure C.3 ). For this experiment, 3120 documents from the arXiv train set were used, and from each, a sequence of 1024 tokens was taken from a random starting position within the document. Each of these sequences was tested with recirculation of only PoS-selected tokens.

## Appendix D Downstream evaluations

### D.1 Instruction following

We generated 800 queries of the following form: ⬇

On half the trials, the model was asked instead to identify the position of the animal (“If the first word is an animal, you say first…”). We formed 400 trials by combining twenty different fruit names with twenty different animal names. With the respond-to-fruit and respond-to-animal variants, this yields 800 trials total. The fruits are: apple, avocado, banana, blueberry, cantaloupe, cherry, grape, honeydew, kiwi, lemon, lime, mango, orange, peach, pear, pineapple, plum, raspberry, strawberry, watermelon. The animals are: bear, bird, cat, deer, dog, dolphin, elephant, fox, giraffe, lion, lizard, monkey, penguin, shark, snake, spider, tiger, whale, wolf, zebra.

We selected the most likely response among eight candidate tokens, which consisted of the words first and second, both in upper- and lower-case form and with and without a leading space.

For the Gemma3 4B and 12B IT, we used the source and destination layers determined by our previous perplexity hyperparameter sweep, and α = 0.07 \alpha=0.07 . For the task-specific result, we conducted a sweep using the instruction-following dataset to determine an upper bound on performance. These sweeps are shown in Figure D.1 . The 1B sweep is included as well, revealing that the model is essentially performing at chance. For the 4B model, source layer 18, destination layer 8 was best; for the 12B model, source layer 29, destination layer 16 was best.

### D.2 Contextualization

For Figure 11 of the main paper, we used hyperparameters chosen based on minimizing perplexity of the pretrained model. We also swept hyperparameters of the Gemma3 1B IT model using a particular condition of the Lepori et al. (2025) dataset: both the 5-distractor condition of the gender questions and the polysemy questions. These sweeps appear in the upper right of Figures D.2 - D.4 , corresponding to the 1B, 4B, and 12B models. In the lower row of the Figure, left to right we show recirculation accuracy with hyperparameters chosen based on pretrained model perplexity, instruction tuned model perplexity, accuracy for gender 5-distractor condition, and accuracy for polysemy 5-distractor condition. Note that the 1B model is not much above chance except for no-distractor polysemy questions.

### D.3 Multiple-choice and single-token response tasks

We tested the Gemma3 4B PT model. To determine the optimal hyperparameters we conducted a (source, destination) sweep using the 1531 MMLU development-set problems. These problems are distinct from the examples used for evaluation. Figure D.5 a shows the sweep, fixing α = 0.07 \alpha=0.07 . Figure D.5 b shows a scan over α \alpha , fixing source and destination layers to be the pair that yields the lowest perplexity in the sweep of Figure D.5 a. The resulting hyperparameters that were used in the various single-token response datasets were source 16, destination 5, α = 0.09 \alpha=0.09 .

### D.4 Standard benchmark datasets: GSM8k

We trained Gemma3 4B model with identical hyperparameters as the perplexity experiments (see Section 4.6 ), except that we masked the prompt part of the question, and only trained the model to predict the ground-truth response present in the dataset. We only report results using our best-performing conditional 𝜶 , 𝜷 \boldsymbol{\alpha},\boldsymbol{\beta} scheme as highlighted in Figure 13 .

### D.5 Adaptive recirculation

For all training experiments, we use 250 documents from each of the PG19, C4, and arXiv training sets. Documents are partitioned into windows of 1024 tokens and only completely full windows were included in the training set. The transformer with recirculation and the MLP module is trained with Back Propagation Through Time (BPTT). For the perplexity studies of Figure 13 , we use the Gemma3 1B PT model with the previously selected source and destination layers (Table B.1 ).

Our architecture is adapted from the next-latent prediction MLP in Teoh et al. (2025) , where we use a 2 hidden layer GELU-based MLP with the same hidden size as the model dimension, with layer-norm at the input of the MLP. The input is twice the model hidden dimension as we concatenate the source and the destination embeddings to be fed to the MLP. Output size is dependent on the formulation used; e.g., it would be twice the model hidden dimension for learned conditional vectors scheme, which predicts two scalars ( α \alpha , β \beta ) per dimension.

We use sigmoid activation at the output to ensure that these coefficients lie in [0,1]. Further, we initialize the parameters of the network such that it starts with α = 0.1 \alpha=0.1 and β = 0.9 \beta=0.9 at initialization, based on the range of values we found to be suitable from our grid-search results.

We train the model for 100 steps with a batch size of 32 using AdamW ( Loshchilov and Hutter, 2019 ) , a learning rate of 3e-4, and a weight decay of 1e-4. For all simulations other than LLM fine-tuning, we freeze the parameters of Gemma3. For LLM fine-tuning, we disable weight decay and use a small learning rate of 1e-5. Similarly, for the unconditional prediction schemes (same for all inputs), we disable weight decay and increase the learning rate to 1e-1.

Evaluation was performed with the validation or test set of nine datasets: ArXiv, PubMed, PG19, BookSum, Lambada, Gov Report, BillSum, OpenWebText, and Big Patent. Note that nonoverlapping subsets of ArXiv and PG19 were used for training and evaluation.

Figure D.6 b compares recirculation with fixed coefficients ( α = 0.15 , β = 0.85 \alpha=0.15,\beta=0.85 ) and the scheme in which an MLP is trained to produce vector-valued 𝜶 \boldsymbol{\alpha} and 𝜷 \boldsymbol{\beta} coefficients for each token (Figure D.6 a). We refer to this scheme as adaptive recirculation for short, as well as conditional 𝛂 , 𝛃 \boldsymbol{\alpha},\boldsymbol{\beta} in the text. The comparison indicates that adaptive recirculation increases the percentage reduction in perplexity for every dataset, and by a factor of three or more for many of the datasets.

When training our conditional vector 𝜶 , 𝜷 \boldsymbol{\alpha},\boldsymbol{\beta} scheme on downstream tasks with Gemma3 4B (Table 2 and Figure 12 ), we use the same hyperparameters as our perplexity experiments. However, we mask the prompt and only train on the response, which refers to only a single token in the single-token benchmarks (Table 2 ). Because the ARC datasets have fewer examples than the MMLU datasets (MMLU train set: 99842, MMLU test set: 14042, ARC easy: 2251, ARC challenge: 1119), we used multi-epoch training for the ARC datasets as we train on a total of 3200 examples (100 steps with a batch-size of 32).

## Instructions for reporting errors

We are continuing to improve HTML versions of papers, and your feedback helps enhance accessibility and mobile support. To report errors in the HTML that will help us improve conversion and rendering, choose any of the methods listed below:

Click the "Report Issue" ( ) button, located in the page header.

Tip: You can select the relevant text first, to include it in your report.

Our team has already identified the following issues . We appreciate your time reviewing and reporting rendering errors we may not have found yet. Your efforts will help us improve the HTML versions for all readers, because disability should not be a barrier to accessing research. Thank you for your continued support in championing open access for all.

Have a free development cycle? Help support accessibility at arXiv! Our collaborators at LaTeXML maintain a list of packages that need conversion , and welcome developer contributions .
