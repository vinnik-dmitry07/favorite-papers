##### Report GitHub Issue

Content selection saved. Describe the issue below:

# Enabling Agents to Communicate Entirely in Latent Space

###### Abstract

While natural language is the de facto communication medium for LLM-based agents, it presents a fundamental constraint. The process of downsampling rich, internal latent states into discrete tokens inherently limits the depth and nuance of information that can be transmitted, thereby hindering collaborative problem-solving. Inspired by telepathy, which bypasses symbolic language in communication, we propose Interlat ( Inter -agent Lat ent Space Communication ), a paradigm that leverages the continuous last hidden states of an LLM as a representation of its thought for direct communication (termed “latent communication” ). An additional learned compression process further compresses latent communication via latent space reasoning. Experiments demonstrate that Interlat outperforms both fine-tuned chain-of-thought (CoT) prompting and single-agent baselines, even across heterogeneous models, promoting more exploratory behavior and enabling genuine utilization of latent information. Further compression not only substantially accelerates inference by up to 24 × \times but also maintains competitive performance through an efficient information-preserving mechanism. We position this work as a feasibility study of entirely latent space inter-agent communication, and our results highlight its potential, offering valuable insights for future research. Our code is available at https://github.com/XiaoDu-flying/Interlat .

“The limits of my language mean the limits of my world.” — Ludwig Wittgenstein, Tractatus Logico-Philosophicus , §5.6.

## 1 Introduction

Large language model (LLM)-based agentic systems have emerged as a promising paradigm for solving complex tasks by orchestrating multiple agents through natural language communication Wang et al. (2025) ; Wang et al. (2024) ; Zhang et al. (2024b) ; Tran et al. (2025) . Despite its human readability, natural language imposes fundamental constraints on inter-agent communication. To communicate, an agent must compress its rich, high-dimensional internal states into a sequence of discrete tokens, typically exposing only a single linear message ( i.e., a chain of thought (CoT) Wei et al. (2022) plan). This downsampling not only discards alternative reasoning paths, but also incurs substantial redundancy, as much of the generated text serves linguistic coherence rather than task-relevant information Zhang et al. (2024a) . As a result, language-based communication can be ambiguous and lossy, which has been identified as a major source of coordination failures in multi-agent systems Chen et al. (2025) ; Cemri et al. (2025) .

To move beyond language space, we explore the direct transmission of internal representations for more precise and information-preserving communication. In multi-agent settings, we refer to this as latent communication . While direct sharing is challenging for humans, which is often depicted in fictions Liu (2008) , i.e., telepathy , LLM-based agents naturally perform most of their computation in latent space and produce rich hidden states throughout generation, which can be extracted to support direct, expressive communication. Previous hidden-state-based communication methods either rely on one-shot activation grafting Ramesh and Li (2025) or remain coupled to language trajectories Tang et al. (2025) , and typically require ad-hoc layer selection, adding tuning overhead.

In this work, we propose Interlat, a novel framework that realizes this vision by enabling inter-agent communication entirely in latent space. Rather than transmitting discrete tokens decoded by the language head, Interlat directly transmits the temporally aligned last-layer hidden states corresponding to an agent’s generated message, treating them as a representation of its thoughts. Under this formulation, we design a supervised objective that explicitly encourages the interpretation and utilization of task-relevant latent information, with a simple but effective stochastic token–latent mixing curriculum to stabilize training. To overcome the rigidity of full-trajectory message communication while preserving information integrity, we further train a separate reasoning process that autoregressively generates compact latent messages with a controllable number of generation steps directly in latent space, without decoding to language space tokens. This allows Interlat to compress long reasoning trajectories into concise latent prefixes, substantially improving efficiency while retaining task-critical information for downstream execution.

Experimentally, we focus on a two-agent sender-receiver scenario, which is the building block of various multi-agent systems. To reduce confounding factors, we intentionally exclude components such as tool use, retrieval, or multi-round debate. Analysis reveals that agents utilizing latent communication exhibit more exploratory behavior patterns that lead to higher success rates by leveraging task-relevant latent information rather than superficial pattern matching. Moreover, we demonstrate that latent messages can be compressed to as few as 8 tokens while maintaining competitive performance, achieving up to a 24 × 24\times reduction in communication latency. Further analysis of the output probability distribution after compression reveals how task-critical information is effectively preserved.

## 2 Related Work

#### Latent Reasoning in LLMs.

Recent research has begun shifting reasoning processes from the discrete language space to continuous latent representations, bypassing the bandwidth and efficiency limits of text ( ≈ 15 \approx 15 bits/token vs. ≈ 40 \approx 40 k bits/hidden-state) Zhu et al. (2025b) . To expand computation during inference, Goyal et al. (2023) introduces pause tokens, while Pfau et al. (2024) employs filler tokens to scaffold intermediate reasoning. Beyond token scheduling, Liu et al. (2024) proposes a latent coprocessor that modifies the transformer KV cache. Other work Hao et al. (2024) ; Shen et al. (2025) ; Cheng and Van Durme (2024) enables multi-path parallel reasoning by feeding the last hidden state back as the next input embedding. Modular frameworks Bae et al. (2024) ; Gao et al. (2024) ; Geiping et al. (2025) decouple encoding, latent reasoning, and decoding. Building upon these insights, we shift focus from single-model latent reasoning to inter-agent communication entirely in latent space.

#### Multi-agent Communication.

LLM-based agent systems typically orchestrate in natural language Zhu et al. (2025a) ; Wang et al. (2024) , which can introduce ambiguity and computational overhead Zhang et al. (2024a) ; Yu et al. (2024) ; Cemri et al. (2025) ; Chen et al. (2025) . Emergent communication studies Lazaridou et al. (2016) ; Lazaridou et al. (2018) ; Tucker et al. (2021) ; Tucker et al. (2022) show that non-linguistic protocols can emerge, yet depend on channels learned from scratch and disconnected from internal reasoning. Recent work explores richer forms: Pham et al. (2023) transmits probability-weighted tokenizer embeddings; Ramesh and Li (2025) blends hidden activations between agents; and Tang et al. (2025) communicates per-token latent deltas tied to language trajectories. Zheng et al. (2025) infers latent “thoughts” from hidden states via an autoencoder and injects them as prefixes using recovered dependencies. Unlike these works, our method directly transmits temporally aligned sequences of last hidden states and further compresses them to enable efficient, language-free communication. Interlat preserves agent autonomy by requiring no parameter sharing Christianos et al. (2021) , memory coupling Salemi et al. (2025) , or cache synchronization Fu et al. (2025) ; Zou et al. (2025) , while expanding the effective communication bandwidth.

## 3 Interlat

In this section, we formalize how to extract an agent’s states as the representation of its “thought” for inter-agent latent space communication. Let x = ( x 1 , … , x T ) x=(x_{1},\dots,x_{T}) denote a sequence consisting of a prompt x 1 : m x_{1:m} and a completion sequence y = ( y 1 , … , y L ) y=(y_{1},\dots,y_{L}) such that y ℓ = x m + ℓ y_{\ell}=x_{m+\ell} and L = T − m L=T-m . For each decoding step ℓ = 1 , … , L \ell=1,\dots,L , define: h ℓ \displaystyle h_{\ell} = Transformer ​ ( x ≤ m + ℓ − 1 ) m + ℓ − 1 , \displaystyle=\mathrm{Transformer}\!\left(x_{\leq m+\ell-1}\right)_{m+\ell-1}, H \displaystyle H = [ h 1 , h 2 , … , h L ] , \displaystyle=[\,h_{1},\,h_{2},\,\dots,\,h_{L}\,], where h ℓ ∈ ℝ d h_{\ell}\in\mathbb{R}^{d} is the last-layer hidden state immediately before predicting y ℓ y_{\ell} ( i.e., at position m + ℓ − 1 m+\ell-1 in the full sequence). H ∈ ℝ L × d H\in\mathbb{R}^{L\times d} collects these last hidden states for the completion region.

### 3.1 Latent Communication

Interlat removes natural language constraints by letting agents transmit their thoughts by directly passing the collected last hidden states, which we termed latent communication. As shown in Figure 1 , this transmission occurs at the end of an agent’s message generation process. Special tokens, x i = <bop> x_{i}=\texttt{<bop>} and x j = <eop> x_{j}=\texttt{<eop>} , are added to mark the beginning and the end of the latent communications. Consider an agent ℳ i \mathcal{M}_{i} solving a task 𝒯 = { x 1 , … , x m } \mathcal{T}=\{x_{1},\dots,x_{m}\} . Upon receiving a latent communication H = { h 1 , h 2 , … , h L } H=\{h_{1},h_{2},\dots,h_{L}\} from another agent, it forms its input embedding as: E = [ e ⁡ ( x 1 ) , … , e ⁡ ( x i ) , h 1 , h 2 , … , h L , e ⁡ ( x j ) ] , E\;=\;[\,e(x_{1}),\dots,e(x_{i}),h_{1},h_{2},\dots,h_{L},e(x_{j})\,], where e ⁡ ( ⋅ ) e(\cdot) is the token embedding. This inference process is analogous to language space multi-agent systems, except that it directly feeds hidden states between agents. The latent communications are processed by a trainable light-weight self-attention and a projection layer as a communication adapter for rescaling and interpretation. For brevity, we may refer to latent communication as latents where unambiguous.

### 3.2 Training Procedure

In this work, we consider two agents: a reasoning agent as a sender that produces a task-specific plan together with its last-layer hidden states, and an actor agent as a receiver that consumes this communication to generate actions to solve tasks. This two-agent setting can serve as a fundamental building block for more complex multi-agent systems.

Let Y t Y_{t} denote the next token at supervised position t ∈ S t\in S , where S S indexes the actor’s output tokens corresponding to the ground-truth response, and C t C_{t} the decoder prefix up to position t t . We encourage the actor to utilize H H by maximizing a supervised fine-tuning objective regularized by conditional distributional separation: ℒ total = ℒ task + λ S ​ ℒ sep + λ A ​ ℒ align , \mathcal{L}_{\mathrm{total}}\;=\;\mathcal{L}_{\mathrm{task}}\;+\;\lambda_{\mathrm{S}}\,\mathcal{L}_{\mathrm{sep}}\;+\;\lambda_{\mathrm{A}}\,\mathcal{L}_{\mathrm{align}}, where λ S , λ A > 0 \lambda_{\mathrm{S}},\lambda_{\mathrm{A}}>0 , and ℒ task \mathcal{L}_{\mathrm{task}} is the standard cross-entropy loss that ensures the model produces accurate and coherent responses for the given task.

#### Conditional thought separation.

We compare the conditional output distributions p θ p_{\theta} induced by matched latent communications H H and mismatched latents H ~ \tilde{H} ( i.e., latent communications sampled from a different task). Specifically, we minimize a weighted Jensen–Shannon divergence Lin (2002) : ℒ sep = − 1 | S | ∑ t ∈ S JS ( p θ ( ⋅ ∣ C t , H ) , p θ ( ⋅ ∣ C t , H ~ ) ) . \mathcal{L}_{\mathrm{sep}}=-\,\frac{1}{|S|}\sum_{t\in S}\mathrm{JS}\!\big(p_{\theta}(\cdot\!\mid\!C_{t},H),\,p_{\theta}(\cdot\!\mid\!C_{t},\tilde{H})\big). This objective separates matched from mismatched conditional distributions, providing a robust training signal that encourages the actor to attend to and leverage task-relevant latent information.

#### Plan-aligned regulation.

While maximizing separation encourages sensitivity to H H , it also introduces a failure mode where the model may exploit the objective by shifting probability mass toward idiosyncratic tokens that increase divergence while harming task utility. To mitigate this, we regularize predictions conditioned on H H using those conditioned on the corresponding language-space plan P P , generated by the same instruction-tuned model during the autoregressive generation of H H . Let p plan ( ⋅ ∣ C t , P ) p_{\mathrm{plan}}(\cdot\mid C_{t},P) denote the distribution when only the plan is provided. For brevity, we omit explicit conditioning on C t C_{t} in the following. ℒ align = β | S | ∑ t ∈ S KL ( p θ ( ⋅ ∣ H ) ∥ p plan ( ⋅ ∣ P ) ) \displaystyle\mathcal{L}_{\mathrm{align}}=\frac{\beta}{|S|}\sum_{t\in S}\mathrm{KL}\!\big(p_{\theta}(\cdot\mid H)\,\|\,p_{\mathrm{plan}}(\cdot\mid P)\big) + α | S | ∑ t ∈ S ( 1 − cos ( 𝐳 θ ( H ) , 𝐳 plan ( P ) ) ) , \displaystyle+\frac{\alpha}{|S|}\sum_{t\in S}\big(1-\cos\!\big(\mathbf{z}_{\theta}(H),\,\mathbf{z}_{\mathrm{plan}}(P)\big)\big), where 𝐳 θ \mathbf{z}_{\theta} and 𝐳 plan \mathbf{z}_{\mathrm{plan}} denote the corresponding normalized logit. All divergences and cosine similarities are computed at supervised positions, with probabilities obtained from the softmax of logits.

#### Curriculum Learning.

Learning to interpret latents from scratch is unstable. We thus adopt a token-to-latent curriculum that stochastically replaces early communication positions with their corresponding plan token embeddings. Concretely, we sample a replacement rate r ∈ { 0 , 0.1 , … , 1.0 } r\in\{0,0.1,\dots,1.0\} and form a mixed communication H ( r ) = e 1 , … , e ⌊ r ⋅ L ⌋ ⏟ token embeddings ⊕ h ⌊ r ⋅ L ⌋ + 1 , … , h L ⏟ latent states . H^{(r)}=\underbrace{e_{1},\dots,e_{\lfloor r\cdot L\rfloor}}_{\text{token embeddings}}\oplus\underbrace{h_{\lfloor r\cdot L\rfloor+1},\dots,h_{L}}_{\text{latent states}}. This method enhances training efficiency while achieving strong model performance.

## 4 Information Compression

While full-length latents H L ∈ ℝ L × d H_{L}\in\mathbb{R}^{L\times d} are highly expressive, their temporal length (often dozens to hundreds of steps) introduces substantial communication latency. Unlike natural-language tokens, whose semantics are discrete and inherently sequential, latent states are continuous and over-parameterized relative to task requirements, suggesting that much of the temporal structure is redundant. Our goal is therefore to learn an information-preserving bottleneck that compresses latents while retaining their utility for downstream agents.

#### Compression via Latent-Space Reasoning.

To this end, we train a separate reasoning model M ϕ M_{\phi} to generate compact latent messages H K ∈ ℝ K × d H_{K}\in\mathbb{R}^{K\times d} with K ≪ L K\ll L , while keeping the actor model and its communication adapter frozen. Rather than truncating or subsampling H L H_{L} , M ϕ M_{\phi} performs autoregressive reasoning entirely in latent space by feeding its last hidden state back as the next input embedding through a lightweight projection: ⟨ M ϕ ( E i ) → h i , E i + 1 = E i ⊕ Proj ( h i ) ⟩ . \langle M_{\phi}(E_{i})\rightarrow h_{i},\;E_{i+1}=E_{i}\oplus\mathrm{Proj}(h_{i})\rangle. This design enables an end-to-end differentiable latent generation loop without decoding to tokens, and isolates compression from changes in the actor’s behavior. During training, only the parameters of M ϕ M_{\phi} are updated, ensuring that compression is learned purely by adapting the latent message itself.

#### Training Objective.

We train the compression model using a composite objective: ℒ compress = λ task ​ ℒ task + λ pref ​ ℒ pref + λ geom ​ ℒ geom , \mathcal{L}_{\text{compress}}=\lambda_{\text{task}}\mathcal{L}_{\text{task}}+\lambda_{\text{pref}}\mathcal{L}_{\text{pref}}+\lambda_{\text{geom}}\mathcal{L}_{\text{geom}}, which jointly addresses the main failure modes of aggressive compression. The task loss ℒ task \mathcal{L}_{\text{task}} is a cross-entropy on the frozen actor’s predictions conditioned on H K H_{K} , ensuring downstream task utility.

Motivated by the non-uniform information density of token-level language communication Shannon (1951) ; Zhang et al. (2024a) , we introduce an uncertainty-weighted agreement loss that selectively aligns the actor’s behavior under compressed and full-length communications. Let p t ( A ) p_{t}^{(A)} , p t ( D ) p_{t}^{(D)} , and p t ( B ) p_{t}^{(B)} denote the actor’s output distributions at position t t when conditioned on H K H_{K} , H L H_{L} , and no latents, respectively. We define per-token weights w t ∝ max ⁡ ( ℋ ⁡ ( p t ( B ) ) − ℋ ⁡ ( p t ( D ) ) , 0 ) w_{t}\propto\max\!\big(\mathcal{H}(p_{t}^{(B)})-\mathcal{H}(p_{t}^{(D)}),\,0\big) . where ℋ ⁡ ( ⋅ ) \mathcal{H}(\cdot) denotes entropy, and compute ℒ pref = ∑ t ∈ S w t KL ( p t ( D ) ∥ p t ( A ) ) \mathcal{L}_{\text{pref}}=\sum_{t\in S}w_{t}\,\mathrm{KL}\!\left(p_{t}^{(D)}\,\|\,p_{t}^{(A)}\right) . This objective emphasizes positions where latents meaningfully reduces predictive uncertainty, while avoiding over-regularization where latents are uninformative.

Finally, to prevent representational drift under strong compression, we apply a latent geometry alignment loss. Let Z k ( A ) Z_{k}^{(A)} and Z k ( D ) Z_{k}^{(D)} denote the actor-side latent features induced by H K H_{K} and H L H_{L} after adapter processing and length alignment, and define their step-averaged directions z ¯ ( A ) \bar{z}^{(A)} and z ¯ ( D ) \bar{z}^{(D)} . We enforce ℒ geom = 1 − cos ⁡ ( z ¯ ( A ) , z ¯ ( D ) ) \mathcal{L}_{\text{geom}}=1-\cos\!\left(\bar{z}^{(A)},\,\bar{z}^{(D)}\right) , which preserves the global semantic orientation of the original communication in the compressed latent space. Together, these objectives encourage M ϕ M_{\phi} to learn an information-preserving bottleneck that discards redundant temporal structure while retaining task-critical functional and geometric properties. Full derivations are provided in Appendix B .

## 5 Experiments

#### Implementation Details.

We evaluate our approach on Alfworld ( Shridhar et al., 2020 ) , and MATH Hendrycks et al. (2021) . For Alfworld, training is conducted using data from Song et al. (2024) . Qwen2.5-7B/0.5B-Base Yang et al. (2024) and LLaMA3.1-8B-Base Dubey et al. (2024) are employed as actor agents to isolate benefits from instruction-tuning priors. CoT plans and compression-free latents are generated by their instruction-tuned counterparts. We use base models as reasoning models in the information compression experiments. Alfworld episodes are capped at 20 steps; unfinished episodes are failures. All models are trained using bfloat16, FlashAttention-2 Dao (2023) , and DeepSpeed Rajbhandari et al. (2020) . For the actor model, we optimize using AdamW Loshchilov and Hutter (2017) with a learning rate of 1 × 10 − 5 1\times 10^{-5} , a global batch size of 16, and a 3% linear warmup. We fix λ task = 1 \lambda_{\text{task}}=1 and dynamically anneal the regularization coefficients during training ( λ sep ∈ [ 0.1 , 1.0 ] \lambda_{\text{sep}}\in[0.1,1.0] , λ align ∈ [ 0.1 , 0.2 ] \lambda_{\text{align}}\in[0.1,0.2] ). Negative samples for ℒ sep \mathcal{L}_{\text{sep}} are constructed using latents from different tasks within the same batch. For information compression, we train the reasoning agent with a frozen actor, utilizing a learning rate of 5 × 10 − 5 5\times 10^{-5} and unit weights for all three compression objectives. We select the best models based on a 5% validation split. All reported results are averaged over three independent runs.

#### Baselines and variants in Interlat.

We study the feasibility of Interlat and compare against two baselines: CoT (full) uses complete CoT plans from instruction-tuned models for full-parameter supervised fine-tuning; No-CoT directly predicts final answers without any plan.

We further evaluate variants of our method: Text replaces latent messages with the corresponding CoT plan; No-Comm removes communication entirely; CrossTask replaces the current task’s latents with one sampled from a different task. Noised adds structured or unstructured perturbations to H H ; CovGauss and RandomRot preserve mean or covariance statistics while destroying higher-order structure. Qwen2LLaMA uses latents from Qwen2.5-7B to train LLaMA3.1-8B model. See Appendix B.1 for detailed implementation setups.

### 5.1 Main Results

Table 1 presents a comprehensive comparison of the Interlat framework against baselines. Latent communication improves agents’ task-solving performance, as evidenced by gains over both fine-tuned single-agent baselines and agents trained to communicate in natural language. We highlight several key observations below.

#### Latent Communication Prompts Exploration.

Beyond improvements in success rates, latent communication enables agents to execute longer yet more successful trajectories. By leveraging multiple plausible reasoning paths encoded in latents from other agents, the actor naturally exhibits more thorough exploratory behavior, even without explicit exploration training. Importantly, this increased trajectory length correlates with higher success rates rather than degraded efficiency, indicating informed exploration instead of random wandering. This behavior suggests a stronger environmental understanding enabled by latent communication, where parallel hypotheses are preserved and gradually resolved during action execution. This pattern is analyzed in detail in Appendix D .

#### Semantics and Learning Dynamics.

To assess whether the actor genuinely exploits latent information rather than superficial patterns, we conduct structured perturbation experiments. Replacing task-matched latents with cross-task latents leads to a substantial performance drop, indicating that the actor relies on task-specific reasoning content encoded in the latents. Performance degrades further under covariance-matched Gaussian surrogates or random orthogonal rotations, which preserve first- and second-order statistics while destroying higher-order structure, supporting the interpretation that the actor is sensitive to meaningful latent geometry rather than low-order moments alone. Additive and white noise perturbations similarly impair performance, further indicating reliance on structured internal information instead of noise-robust heuristics. Experiments involving cross-family latent inputs: feeding Qwen-derived latents to train an LLaMA actor, yield even stronger performance gains. Since these model families exhibit distinct latent manifolds, the improvement cannot be attributed to superficial architectural compatibility. Instead, it suggests latent-level inter-agent understanding that transfers across heterogeneous representations. This observation aligns with findings in language-space agentic systems, where heterogeneous LLM agents often outperform homogeneous ensembles due to complementary inductive biases and reduced error correlations Shinn et al. (2023) ; Wu et al. (2024) .To corroborate these findings qualitatively, Figure 4 and Appendix G visualize clear semantic clustering before and after processing by the communication adapter, confirming effective semantic alignment for downstream use.

Training dynamics further reveal how the actor learns to interpret latent communication. As shown in Figure 3 , the separation loss remains near ln ⁡ 2 \ln 2 for approximately the first 2k steps, indicating no effective distinction between matched and mismatched messages. It then drops sharply, marking an “aha” moment in which the actor begins to exploit and leverage task-relevant latents, consistent with the intended effect of the separation objective.

#### Generalization to Symbolic Reasoning.

To assess generalization beyond interactive settings, we evaluate Interlat on the MATH benchmark. While prior work on latent-space reasoning Hao et al. (2024) ; Shen et al. (2025) ; Ramesh and Li (2025) often reports degraded performance relative to CoT supervision, Table 2 reveals an intriguing inversion: although Interlat slightly underperforms on simpler problems, it surpasses the CoT baseline on the most challenging Level 5 tasks. We attribute this to the duality of linguistic constraints. For lower-complexity problems, the strict linearization of natural language acts as a beneficial regularizer, efficiently pruning the search space. However, for high-complexity tasks, this forced discretization causes a “premature collapse” of the reasoning distribution. In contrast, Interlat maintains a superposition of parallel hypotheses in its continuous representations. This capability allows the model to effectively conduct a broader search in latent space that is inaccessible to linear text decoding.

### 5.2 Compression Analysis

#### Compression Performance.

Theoretically, due to their substantially higher expressive capacity, latent communications can encode rich information in far fewer positions. To quantify this compression capacity, we consider two settings. i) Untrained: We directly use Qwen2.5-7B-Instruct to generate full-length latents for actor training, and then truncate them to shorter lengths. This setting evaluates the empirical compressibility of raw latents. ii) Trained: We use a compression-trained Qwen2.5-7B-Base reasoning model. Results on the LLaMA model are provided in Appendix E .

As shown in Table 3 , naive truncation performs best at moderate compression (50%) but degrades under more aggressive shortening, revealing the limits of untrained compression. In contrast, compression training enables consistently higher and more stable success rates across compressed latent ranging from 8 to 128 steps (around 1.8% to 28.8% of the full sequence), indicating that the reasoning model learns an information-preserving pattern that discards temporal redundancy while retaining task-relevant semantics. Furthermore, compression substantially improves efficiency, reducing end-to-end latency from 9.19 s to 0.39 s with 8-step latents (nearly 24 × 24\times speed-up), and further to 0.20 s with a lightweight bridge module by largely eliminating decode–re-encode overhead.

#### Why compression is effective.

To understand why compression preserves performance, we analyze its effect on the actor’s predictive uncertainty. We sweep the communication rate R ∈ [ 0 , 1 ] R\in[0,1] and measure the task-averaged relative change in cross-entropy (CE), Δ ​ CE % ​ ( R ) = 100 × CE comp ​ ( R ) − CE full CE full \Delta\mathrm{CE}\%(R)=100\times\frac{\mathrm{CE}_{\mathrm{comp}}(R)-\mathrm{CE}_{\mathrm{full}}}{\mathrm{CE}_{\mathrm{full}}} . As shown in Figure 6 , Δ ​ CE % \Delta\mathrm{CE}\% decreases monotonically with increasing R R and plateaus between roughly 30% and 75%, aligning with the range of strongest empirical performance. Across all rates, learned compression consistently yields lower CE than training-free truncation, with a maximum gap of approximately 11 percentage points, indicating better preservation of predictive confidence under reduced communication.

We further examine how information is preserved under compression via the actor’s output distributions. Following Hao et al. (2024) , broader probability mass is interpreted as indicating that the model maintains more plausible alternatives. Figure 5 analyzes the latent steps of the reasoning agent by plotting the cumulative probability mass of the top- 6 6 tokens across communication percentiles, with probabilities normalized over the top-10 tokens for comparability. Latents produced by the trained reasoning agent exhibit stable gaps between successive top- 6 6 curves across steps, whereas untrained compression shows rapid concentration toward top-ranked tokens. We quantify this behavior using a head-coverage statistic, P50 ⁡ ( S 10 ) \mathrm{P50}(S_{10}) , defined as the median cumulative probability mass of the top-10 tokens, which is consistently lower for the trained model and indicates broader support over plausible alternatives.

Together, these observations suggest that learned compression preserves diverse hypotheses across multiple reasoning steps, avoiding collapse into a single trajectory and thereby retaining richer information for downstream decision making.

### 5.3 Ablation Studies

Table 4 presents a systematic ablation of the training components. For the actor model, removing curriculum learning forces the model to interpret latents from scratch, leading to extremely unstable training dynamics and severely degraded comprehension (Appendix, Figure 7 ). Removing the separation loss induces shortcut behavior; the model learns to ignore the latent communication and rely only on the textual task prompt, causing performance to regress toward the single agent baseline. Removing the communication adapter causes the largest drop; despite generating fluent and coherent responses, the model fails to complete tasks, underscoring the adapter’s role in bridging the agents’ latent spaces and enabling interpretation of latents.

For the reasoning model, which is trained to generate compressed latents, we ablated its three core loss functions with compressed target length K = 128 K=128 . The most critical component is the direction alignment loss ( ℒ geom \mathcal{L}_{\mathrm{geom}} ). This highlights the importance of maintaining geometric consistency between the compressed latents and the uncompressed ones. The agreement loss ( ℒ pref \mathcal{L}_{\mathrm{pref}} ) is also vital, as removing it significantly impairs the model’s ability to produce latents that elicit the correct behavior from the actor. Removing the cross-entropy loss ( ℒ task \mathcal{L}_{\mathrm{task}} ) degrades performance on seen tasks but slightly improves unseen performance, suggesting a minor trade-off between in-distribution optimization and generalization. We leave a deeper investigation into this trade-off to future work.

### 5.4 Generalization to Complex Topologies.

To directly verify that Interlat scales beyond simple pairwise communication, we evaluate it on 3-agent topologies using the Qwen2.5-0.5B-Base model on the ALFWorld benchmark. We ensure the entire multi-agent system can be jointly trained end-to-end by having all non-output sender agents generate fixed-length ( N = 32 N=32 ) messages entirely in latent space. Specifically, we investigate two distinct configurations:

Sequential Chain Topology. In this sequential structure (Agent 1 → \rightarrow Agent 2 → \rightarrow Actor), a Strategist agent first generates a high-level latent plan capturing the task goals. A Compiler agent then refines this received plan into a more actionable representation before passing it to the final Actor.

Parallel Tree Topology. This parallel structure ([Agent 1 + Agent 2] → \rightarrow Actor) utilizes an Explorer agent to generate diverse candidate reasoning paths and a Critic agent to produce verification constraints simultaneously. To dynamically fuse these parallel messages, we extend the communication adapter with an additional learned projector that maps the aggregated latents from multiple senders into a unified representation for the Actor.

As shown in Table 5 , both 3-agent latent configurations consistently outperform their natural language CoT counterparts with identical agent structures (e.g., 62.85% vs. 61.19% on seen tasks for the parallel tree). Moreover, both configurations yield solid improvements over the original 2-agent Interlat baseline (61.19%). These results demonstrate that the performance gains stem intrinsically from the rich expressive capacity and information preservation of the latent space, rather than a mere increase in the number of agents. Notably, the superior performance of the tree-3 configuration confirms that Interlat effectively supports parallel multi-agent reasoning, allowing downstream actors to synthesize heterogeneous latent perspectives without requiring pair-specific training.

## 6 Conclusion

In this work, we introduced Interlat, a paradigm that enables inter-agent communication entirely in latent space. Across experiments, our results show that directly transmitting and reasoning over latent states improves task performance and achieves substantially higher communication efficiency, even demonstrating compatibility across heterogeneous models. Beyond full-length latent exchange, we show that latent communication can be aggressively compressed through latent-space reasoning, forming a compact, task-preserving representation that retains parallel hypotheses while discarding redundant structure. Together, these findings suggest that communication need not be bound to language tokens, highlighting latent states as a viable, efficient, and generalizable medium for next-generation multi-agent systems.

## 7 Limitations

Our study has explored how inter-agent communication can be realized entirely in latent space and demonstrated its potential benefits in terms of performance and efficiency. However, several important limitations should be considered when interpreting our results and applying this paradigm more broadly.

First, our experiments mainly focus on a controlled two-agent setting, evaluated on one embodied interactive benchmark (ALFWorld) and one non-interactive symbolic reasoning benchmark (MATH). While these benchmarks jointly cover both interactive planning and single-turn reasoning scenarios, they do not yet fully capture the diversity of real-world multi-agent systems, such as settings with larger teams, dynamic role assignments, long-horizon collaboration, or richer environments involving tool use and external memory. Extending latent communication to larger-scale and more heterogeneous agent ecosystems is a natural and important direction for future work.

Second, our approach assumes access to internal model representations, specifically last-layer hidden states, in order to enable latent communication. This assumption may not hold for closed-source or API-only models, where hidden states are inaccessible. As a result, the current formulation of Interlat is primarily applicable to open or inspectable models, and extending latent communication to restricted-access settings is an open challenge.

Finally, latent communication trades human interpretability for efficiency and expressive capacity. Unlike language-based communication, latent messages are not directly human-readable, which complicates debugging, monitoring, and failure analysis in complex systems. While this work primarily focuses on task performance and efficiency and provides preliminary interpretability analysis via PCA (Figure 4 ), developing principled tools to improve both the interpretability and controllability of latent communication remains an important direction for broader deployment.

Despite these limitations, we view this work as an initial yet concrete step toward understanding and enabling inter-agent communication beyond language. Our results provide empirical evidence that latent space communication can support effective coordination and can be aggressively compressed while preserving task utility, highlighting its potential as a complementary paradigm to language-based interaction in LLM-powered agent systems.

## 8 Ethical Considerations

No human participants, crowdsourcing, or personally identifiable information (PII) were involved in this research. All experiments were conducted within a simulated environment using standard dataset splits.

Our study focuses on inter-agent communication in latent space, utilizing the last hidden states and their compressed variants. A potential theoretical risk is that such latent communication could be exploited to circumvent language-based safety mechanisms. To mitigate this concern to the greatest extent possible, we neither trained on nor evaluated any harmful instructions, and no harmful actions occurred during our experiments. Furthermore, to promote transparency, we provide PCA-based visualizations of latent communication in Figure 4 the analyze internal probability distribution of compressed latent communications in Figure 5 , offering a clearer understanding of the information being transmitted.

## 9 Acknowledgments

This research was partially supported by National Key R&D Program of China under Grant No. 2024YFF0907802, Zhejiang Provincial Natural Science Foundation of China under Grant No. LD24F020011, and Alibaba Group through Alibaba Research Intern Program.

## References

Bae et al. (2024) S. Bae, A. Fisch, H. Harutyunyan, Z. Ji, S. Kim, and T. Schuster Relaxed recursive transformers: effective parameter sharing with layer-wise lora . arXiv preprint arXiv:2410.20672 . Cited by: §2 .

Cemri et al. (2025) M. Cemri, M. Z. Pan, S. Yang, L. A. Agrawal, B. Chopra, R. Tiwari, K. Keutzer, A. Parameswaran, D. Klein, K. Ramchandran, et al. Why do multi-agent llm systems fail? . arXiv preprint arXiv:2503.13657 . Cited by: §1 , §2 .

Chen et al. (2025) Y. Chen, J. Benton, A. Radhakrishnan, J. Uesato, C. Denison, J. Schulman, A. Somani, P. Hase, M. Wagner, F. Roger, et al. Reasoning models don’t always say what they think . arXiv preprint arXiv:2505.05410 . Cited by: §1 , §2 .

Cheng and Van Durme (2024) J. Cheng and B. Van Durme Compressed chain of thought: efficient reasoning through dense representations . arXiv preprint arXiv:2412.13171 . Cited by: §2 .

Christianos et al. (2021) F. Christianos, G. Papoudakis, M. A. Rahman, and S. V. Albrecht Scaling multi-agent reinforcement learning with selective parameter sharing . In International Conference on Machine Learning , pp. 1989–1998 . Cited by: §2 .

Dao (2023) T. Dao Flashattention-2: faster attention with better parallelism and work partitioning . arXiv preprint arXiv:2307.08691 . Cited by: §5 .

Dubey et al. (2024) A. Dubey, A. Jauhri, A. Pandey, A. Kadian, A. Al-Dahle, A. Letman, A. Mathur, A. Schelten, A. Yang, A. Fan, et al. The llama 3 herd of models . arXiv e-prints , pp. arXiv–2407 . Cited by: §5 .

Fu et al. (2025) T. Fu, Z. Min, H. Zhang, J. Yan, G. Dai, W. Ouyang, and Y. Wang Cache-to-cache: direct semantic communication between large language models . arXiv preprint arXiv:2510.03215 . Cited by: §2 .

Gao et al. (2024) Y. Gao, C. Zheng, E. Xie, H. Shi, T. Hu, Y. Li, M. K. Ng, Z. Li, and Z. Liu Algoformer: an efficient transformer framework with algorithmic structures . arXiv preprint arXiv:2402.13572 . Cited by: §2 .

Geiping et al. (2025) J. Geiping, S. McLeish, N. Jain, J. Kirchenbauer, S. Singh, B. R. Bartoldson, B. Kailkhura, A. Bhatele, and T. Goldstein Scaling up test-time compute with latent reasoning: a recurrent depth approach . arXiv preprint arXiv:2502.05171 . Cited by: §2 .

Goyal et al. (2023) S. Goyal, Z. Ji, A. S. Rawat, A. K. Menon, S. Kumar, and V. Nagarajan Think before you speak: training language models with pause tokens . arXiv preprint arXiv:2310.02226 . Cited by: §2 .

Hao et al. (2024) S. Hao, S. Sukhbaatar, D. Su, X. Li, Z. Hu, J. Weston, and Y. Tian Training large language models to reason in a continuous latent space . arXiv preprint arXiv:2412.06769 . Cited by: §2 , §5.1 , §5.2 .

Hendrycks et al. (2021) D. Hendrycks, C. Burns, S. Kadavath, A. Arora, S. Basart, E. Tang, D. Song, and J. Steinhardt Measuring mathematical problem solving with the math dataset . arXiv preprint arXiv:2103.03874 . Cited by: §5 .

Lazaridou et al. (2018) A. Lazaridou, K. M. Hermann, K. Tuyls, and S. Clark Emergence of linguistic communication from referential games with symbolic and pixel input . arXiv preprint arXiv:1804.03984 . Cited by: §2 .

Lazaridou et al. (2016) A. Lazaridou, A. Peysakhovich, and M. Baroni Multi-agent cooperation and the emergence of (natural) language . arXiv preprint arXiv:1612.07182 . Cited by: §2 .

Lin (2002) J. Lin Divergence measures based on the shannon entropy . IEEE Transactions on Information theory 37 ( 1 ), pp. 145–151 . Cited by: §3.2 .

Liu (2008) C. Liu The dark forest . Chongqing Publishing House , Chongqing, China . Note: English translation published by Tor Books, 2015 Cited by: §1 .

Liu et al. (2024) L. Liu, J. Pfeiffer, J. Wu, J. Xie, and A. Szlam Deliberation in latent space via differentiable cache augmentation . arXiv preprint arXiv:2412.17747 . Cited by: §2 .

Loshchilov and Hutter (2017) I. Loshchilov and F. Hutter Decoupled weight decay regularization . arXiv preprint arXiv:1711.05101 . Cited by: §5 .

Mezzadri (2006) F. Mezzadri How to generate random matrices from the classical compact groups . arXiv preprint math-ph/0609050 . Cited by: item 6 .

Pfau et al. (2024) J. Pfau, W. Merrill, and S. R. Bowman Let’s think dot by dot: hidden computation in transformer language models . arXiv preprint arXiv:2404.15758 . Cited by: §2 .

Pham et al. (2023) C. Pham, B. Liu, Y. Yang, Z. Chen, T. Liu, J. Yuan, B. A. Plummer, Z. Wang, and H. Yang Let models speak ciphers: multiagent debate through embeddings . arXiv preprint arXiv:2310.06272 . Cited by: §2 .

Rajbhandari et al. (2020) S. Rajbhandari, J. Rasley, O. Ruwase, and Y. He Zero: memory optimizations toward training trillion parameter models . In SC20: International Conference for High Performance Computing, Networking, Storage and Analysis , pp. 1–16 . Cited by: §5 .

Ramesh and Li (2025) V. Ramesh and K. Li Communicating activations between language model agents . arXiv preprint arXiv:2501.14082 . Cited by: §1 , §2 , §5.1 .

Salemi et al. (2025) A. Salemi, M. Parmar, P. Goyal, Y. Song, J. Yoon, H. Zamani, H. Palangi, and T. Pfister Llm-based multi-agent blackboard system for information discovery in data science . arXiv preprint arXiv:2510.01285 . Cited by: §2 .

Shannon (1951) C. E. Shannon Prediction and entropy of printed english . Bell system technical journal 30 ( 1 ), pp. 50–64 . Cited by: §4 .

Shen et al. (2025) Z. Shen, H. Yan, L. Zhang, Z. Hu, Y. Du, and Y. He Codi: compressing chain-of-thought into continuous space via self-distillation . arXiv preprint arXiv:2502.21074 . Cited by: §2 , §5.1 .

Shinn et al. (2023) N. Shinn, F. Cassano, A. Gopinath, K. Narasimhan, and S. Yao Reflexion: language agents with verbal reinforcement learning . Advances in Neural Information Processing Systems 36 , pp. 8634–8652 . Cited by: §5.1 .

Shridhar et al. (2020) M. Shridhar, X. Yuan, M. Côté, Y. Bisk, A. Trischler, and M. Hausknecht Alfworld: aligning text and embodied environments for interactive learning . arXiv preprint arXiv:2010.03768 . Cited by: §C.1 , §5 .

Song et al. (2024) Y. Song, D. Yin, X. Yue, J. Huang, S. Li, and B. Y. Lin Trial and error: exploration-based trajectory optimization for llm agents . arXiv preprint arXiv:2403.02502 . Cited by: §5 .

Tang et al. (2025) Y. Tang, W. Su, Y. Zhou, Y. Liu, M. Zhang, S. Ma, and Q. Ai Augmenting multi-agent communication with state delta trajectory . arXiv preprint arXiv:2506.19209 . Cited by: §1 , §2 .

Tran et al. (2025) K. Tran, D. Dao, M. Nguyen, Q. Pham, B. O’Sullivan, and H. D. Nguyen Multi-agent collaboration mechanisms: a survey of llms . arXiv preprint arXiv:2501.06322 . Cited by: §1 .

Tucker et al. (2022) M. Tucker, R. Levy, J. A. Shah, and N. Zaslavsky Trading off utility, informativeness, and complexity in emergent communication . Advances in neural information processing systems 35 , pp. 22214–22228 . Cited by: §2 .

Tucker et al. (2021) M. Tucker, H. Li, S. Agrawal, D. Hughes, K. Sycara, M. Lewis, and J. A. Shah Emergent discrete communication in semantic spaces . Advances in neural information processing systems 34 , pp. 10574–10586 . Cited by: §2 .

Wang et al. (2024) L. Wang, C. Ma, X. Feng, Z. Zhang, H. Yang, J. Zhang, Z. Chen, J. Tang, X. Chen, Y. Lin, et al. A survey on large language model based autonomous agents . Frontiers of Computer Science 18 ( 6 ), pp. 186345 . Cited by: §1 , §2 .

Wang et al. (2025) Y. Wang, S. Liu, J. Fang, and Z. Meng EvoAgentX: an automated framework for evolving agentic workflows . arXiv preprint arXiv:2507.03616 . Cited by: §1 .

Wei et al. (2022) J. Wei, X. Wang, D. Schuurmans, M. Bosma, F. Xia, E. Chi, Q. V. Le, D. Zhou, et al. Chain-of-thought prompting elicits reasoning in large language models . Advances in neural information processing systems 35 , pp. 24824–24837 . Cited by: §1 .

Wu et al. (2024) Q. Wu, G. Bansal, J. Zhang, Y. Wu, B. Li, E. Zhu, L. Jiang, X. Zhang, S. Zhang, J. Liu, et al. Autogen: enabling next-gen llm applications via multi-agent conversations . In First Conference on Language Modeling , Cited by: §5.1 .

Yang et al. (2024) A. Yang, B. Yang, B. Zhang, B. Hui, B. Zheng, B. Yu, C. Li, D. Liu, F. Huang, H. Wei, H. Lin, J. Yang, J. Tu, J. Zhang, J. Yang, J. Yang, J. Zhou, J. Lin, K. Dang, K. Lu, K. Bao, K. Yang, L. Yu, M. Li, M. Xue, P. Zhang, Q. Zhu, R. Men, R. Lin, T. Li, T. Xia, X. Ren, X. Ren, Y. Fan, Y. Su, Y. Zhang, Y. Wan, Y. Liu, Z. Cui, Z. Zhang, and Z. Qiu Qwen2.5 technical report . arXiv preprint arXiv:2412.15115 . Cited by: §5 .

Yu et al. (2024) F. Yu, H. Zhang, P. Tiwari, and B. Wang Natural language reasoning, a survey . ACM Computing Surveys 56 ( 12 ), pp. 1–39 . Cited by: §2 .

Zhang et al. (2024a) G. Zhang, Y. Yue, Z. Li, S. Yun, G. Wan, K. Wang, D. Cheng, J. X. Yu, and T. Chen Cut the crap: an economical communication pipeline for llm-based multi-agent systems . arXiv preprint arXiv:2410.02506 . Cited by: §1 , §2 , §4 .

Zhang et al. (2024b) J. Zhang, J. Xiang, Z. Yu, F. Teng, X. Chen, J. Chen, M. Zhuge, X. Cheng, S. Hong, J. Wang, et al. Aflow: automating agentic workflow generation . arXiv preprint arXiv:2410.10762 . Cited by: §1 .

Zheng et al. (2025) Y. Zheng, Z. Zhao, Z. Li, Y. Xie, M. Gao, L. Zhang, and K. Zhang Thought communication in multiagent collaboration . arXiv preprint arXiv:2510.20733 . Cited by: §2 .

Zhu et al. (2025a) K. Zhu, H. Du, Z. Hong, X. Yang, S. Guo, Z. Wang, Z. Wang, C. Qian, X. Tang, H. Ji, et al. Multiagentbench: evaluating the collaboration and competition of llm agents . arXiv preprint arXiv:2503.01935 . Cited by: §2 .

Zhu et al. (2025b) R. Zhu, T. Peng, T. Cheng, X. Qu, J. Huang, D. Zhu, H. Wang, K. Xue, X. Zhang, Y. Shan, et al. A survey on latent reasoning . arXiv preprint arXiv:2507.06203 . Cited by: §2 .

Zou et al. (2025) J. Zou, X. Yang, R. Qiu, G. Li, K. Tieu, P. Lu, K. Shen, H. Tong, Y. Choi, J. He, et al. Latent collaboration in multi-agent systems . arXiv preprint arXiv:2511.20639 . Cited by: §2 .

Appendix

The supplementary information accompanying the main paper provides additional data, explanations, and details.

## Appendix A LLM usage

ChatGPT 1 1 1 https://chat.openai.com/ was used purely with the language of the paper during the writing process, including spell-checking and paraphrasing the authors’ original content, without suggesting new content. Any content generated with the assistant underwent meticulous manual review and subsequently received final approval from the authors.

## Appendix B Compression Loss

#### Setup.

After training an actor M θ M_{\theta} to consume latent communications, we freeze M θ M_{\theta} and train a reasoning model M ϕ M_{\phi} to produce compact, information-dense latent communications of length K K that the frozen actor can still exploit. For an input instance with supervised token indices S S (the teacher-forced window after the first user turn), let H 1 : K gen = M ϕ ( x ) and H 1 : L full = M ins ( x ) , H^{\mathrm{gen}}_{1:K}\;=\;M_{\phi}(x)\quad\text{and}\quad H^{\mathrm{full}}_{1:L}\;=\;M_{\text{ins}}(x), (1) denote respectively the generated latent communication from the trainable reasoning model and the full-length latent communication extracted from a fixed instruction-tuned model M ins M_{\text{ins}} . A lightweight communication adapter g ⁡ ( ⋅ ) g(\cdot) (kept frozen) preprocesses the latent communication before concatenation with boundary tokens <bop> / <eop> . For brevity, we use H K ≡ H gen 1 : K H_{K}\equiv H^{\mathrm{gen}}_{1:K} and H L ≡ H full 1 : L H_{L}\equiv H^{\mathrm{full}}_{1:L} .

We define three actor-scored forward paths through the frozen actor M θ M_{\theta} given a prompt x x : (i) Path A (generated latents) : E ( A ) = [ e ⁡ ( x ) , e ⁡ ( <bop> ) , g ⁡ ( H K ) , e ⁡ ( <eop> ) ] E^{(A)}=[\,e(x),\,e(\texttt{<bop>}),\,g(H_{K}),\,e(\texttt{<eop>})\,] ; (ii) Path D (full-length latents) : E ( D ) = [ e ⁡ ( x ) , e ⁡ ( <bop> ) , g ⁡ ( H L ) , e ⁡ ( <eop> ) ] E^{(D)}=[\,e(x),\,e(\texttt{<bop>}),\,g(H_{L}),\,e(\texttt{<eop>})\,] ; (iii) Path B (no latents) : E ( B ) = [ e ⁡ ( x ) ] E^{(B)}=[\,e(x)\,] . Let 𝐳 t ( q ) \mathbf{z}^{(q)}_{t} be the frozen-actor logits at position t ∈ S t\!\in\!S under path q ∈ { A , D , B } q\!\in\!\{A,D,B\} , and p t ( q ) = softmax ⁡ ( 𝐳 t ( q ) / T ) p^{(q)}_{t}\;=\;\mathrm{softmax}\!\big(\mathbf{z}^{(q)}_{t}/T\big) (2) be the corresponding token distributions with temperature T ≥ 1 T\!\geq\!1 used for distillation. Unless stated otherwise, gradients do not flow into M θ M_{\theta} or g ⁡ ( ⋅ ) g(\cdot) .

#### (1) Actor cross-entropy utility.

We require the generated message to be useful for the frozen actor: ℒ task = 1 | S | ​ ∑ t ∈ S ( − log ⁡ p θ ​ ( y t ∣ C t , H K ) ) ⏟ (computed under Path A). \underbrace{\mathcal{L}_{\mathrm{task}}\;=\;\frac{1}{|S|}\sum_{t\in S}\big(-\log p_{\theta}(y_{t}\mid C_{t},H_{K})\big)}_{\text{(computed under Path A).}} (3) This term enforces that the compressed latents H K H_{K} still drive correct next-token predictions, directly penalizing information loss due to shortening ( K ≪ L K\!\ll\!L ). It prevents degenerate “over-compression” that would be efficient but useless to the actor. Practically, it anchors training on task utility, encouraging compression gain does not come at the cost of downstream performance.

#### (2) Uncertainty-weighted agreement.

We further encourage behavioral agreement between using full-length latent communication (Path D) and generated compressed latent communication (Path A), with per-token weights that reflect how much any latent reduces uncertainty relative to the no-latent baseline (Path B). Let the entropies be H ( q ) ( t ) = − ∑ v p ( q ) t ( v ) log p ( q ) t ( v ) ⏟ q ∈ { A , D , B } , . \underbrace{H^{(q)}(t)\;=\;-\sum_{v}p^{(q)}_{t}(v)\,\log p^{(q)}_{t}(v)}_{q\!\in\!\{A,D,B\}},. (4) Define raw weights w t ⋆ = max ⁡ ( H ( B ) ​ ( t ) − H ( D ) ​ ( t ) , 0 ) w_{t}^{\star}=\max\!\big(H^{(B)}(t)-H^{(D)}(t),\,0\big) and optionally clip w t ⋆ w_{t}^{\star} to [ 0 , τ ] [0,\tau] to suppress outliers. Normalize to unit mean: w t = w t ⋆ 1 | S | ​ ∑ u ∈ S w u ⋆ + ε . w_{t}\;=\;\frac{w_{t}^{\star}}{\frac{1}{|S|}\sum_{u\in S}w_{u}^{\star}+\varepsilon}. (5) The agreement term is a temperature-scaled KL: ℒ pref = 1 ∑ t ∈ S w t ∑ t ∈ S w t T 2 KL ( p ( D ) t ∥ p ( A ) t ) = T 2 ∑ t ∈ S w t ​ ∑ t ∈ S w t ​ ∑ v p t ( D ) ​ ( v ) ​ log ⁡ p t ( D ) ​ ( v ) p t ( A ) ​ ( v ) . \begin{split}\mathcal{L}_{\mathrm{pref}}&=\frac{1}{\sum_{t\in S}w_{t}}\sum_{t\in S}w_{t}\;T^{2}\,\mathrm{KL}\!\Big(p^{(D)}_{t}\,\big\|\,p^{(A)}_{t}\Big)\\ &=\frac{T^{2}}{\sum_{t\in S}w_{t}}\sum_{t\in S}w_{t}\sum_{v}p^{(D)}_{t}(v)\log\frac{p^{(D)}_{t}(v)}{p^{(A)}_{t}(v)}.\end{split} (6) By matching p ( A ) p^{(A)} to p ( D ) p^{(D)} where full latents actually reduce uncertainty (weights w t w_{t} ), this term teaches H K H_{K} to reproduce the informative behavioral effects of H L H_{L} while ignoring positions where latents are unhelpful. Unlike reconstruction-based or contrastive objectives, this formulation aligns compressed latents directly through the actor’s induced behavior, avoiding assumptions about latent invertibility or instance-level correspondence. This allows compressed communication to focus on functional equivalence rather than representational similarity. This is particularly important for reasoning latents, which are over-parameterized, temporally misaligned under compression, and lack a natural one-to-one mapping across steps. By aligning compressed and full communications through induced behavior, our formulation supports variable-length latent messages, enables abstraction across multiple reasoning steps, and yields more stable and transferable training signals.

#### (3) Latent direction alignment.

To stabilize compression, we align the global direction of actor-side latent features induced by generated vs. data latents. Let Z k ( q ) ∈ ℝ d z Z^{(q)}_{k}\in\mathbb{R}^{d_{z}} be the actor-side features (after g ⁡ ( ⋅ ) g(\cdot) and the actor’s input stack) at latent step k k under path q ∈ { A , D } q\in\{A,D\} . When H L H_{L} has length L ≠ K L\!\neq\!K , apply a fixed resampling operator ρ K \rho_{K} ( e.g., uniform down/up-sampling) and write Z 1 : K ( D ) = ρ K ( Z 1 : L ( D ) ) Z^{(D)}_{1:K}=\rho_{K}\!\big(Z^{(D)}_{1:L}\big) . Define step-averaged directions z ¯ ( q ) = 1 K ​ ∑ k = 1 K Z k ( q ) \bar{z}^{(q)}=\frac{1}{K}\sum_{k=1}^{K}Z^{(q)}_{k} and the cosine penalty ℒ geom = 1 − cos ⁡ ( z ¯ ( A ) , z ¯ ( D ) ) = 1 − ⟨ z ¯ ( A ) , z ¯ ( D ) ⟩ ‖ z ¯ ( A ) ‖ 2 ​ ‖ z ¯ ( D ) ‖ 2 . \begin{split}\mathcal{L}_{\mathrm{geom}}&=1-\cos\!\big(\bar{z}^{(A)},\,\bar{z}^{(D)}\big)\\ &=1-\frac{\langle\bar{z}^{(A)},\,\bar{z}^{(D)}\rangle}{\|\bar{z}^{(A)}\|_{2}\,\|\bar{z}^{(D)}\|_{2}}.\end{split} (7) This term preserves the geometry of the actor-side representations, preventing the compressed latents from drifting to directions that the actor interprets differently. Empirically, it improves stability and mitigates mode collapse when K K is small by retaining the global semantic orientation of H L H_{L} .

#### Overall objective.

The compression objective for M ϕ M_{\phi} (with M θ M_{\theta} frozen) is

ℒ compress = λ task ​ ℒ task + λ pref ​ ℒ pref + λ geom ​ ℒ geom . \begin{split}\mathcal{L}_{\mathrm{compress}}&=\lambda_{\mathrm{task}}\;\mathcal{L}_{\mathrm{task}}\\ &\quad+\lambda_{\mathrm{pref}}\;\mathcal{L}_{\mathrm{pref}}\\ &\quad+\lambda_{\mathrm{geom}}\;\mathcal{L}_{\mathrm{geom}}.\end{split} (8) In practice, all terms are computed over t ∈ S t\!\in\!S with teacher forcing; gradients propagate only to ϕ \phi .

### B.1 Baselines and settings in Interlat.

We consider two external baselines, which do not rely on latent communication at all. All baselines are trained using the same base models (Qwen2.5-7B/0.5B-Base, LLaMA3.1-8B-Base) as Interlat, differing only in whether and how inter-agent communication is provided.

1. CoT (full). We use complete Chain-of-Thought (CoT) traces produced by a related instruction-tuned model (Qwen2.5-7B-Instruct, Qwen2.5-0.5B-Instruct, and LLaMA3.1-8B-Instruct) to perform full-parameter supervised fine-tuning. In inference, the model receives a complete CoT plan before generating answers.

Rationale. This baseline serves as a strong upper bound for language-based communication: it evaluates whether latent communication can surpass explicit human-readable planning, and controls for the supervision quality provided by an instruction-tuned teacher.

2. No-CoT. The language model is trained to produce the final answer directly, without receiving any plan from other agents. Rationale. This baseline isolates the contribution of any communication signal. It tests whether inter-agent exchange, latent or linguistic, is necessary for solving multi-step tasks.

In addition, we evaluate controlled variants of Interlat to diagnose what information is encoded in the latents.

1. Text. Instead of latent communication, we feed the corresponding CoT plan (in language space) to the actor.

Rationale. This variant keeps the interaction protocol unchanged while varying only the communication channel. It enables a direct comparison between language-space and latent-space communication under matched training conditions, disentangling architectural factors from representational ones.

2. No-Comm. We remove any communication from the actor’s input. This variant quantifies the intrinsic benefit of communication in our framework and verifies that performance improvements do not arise solely from modifications to the underlying model parameters.

3. CrossTask. We replace the current task’s latent communication with one sampled from a different task. Rationale. This variant examines whether the actor is genuinely interpreting task-specific latent content. A substantial degradation indicates reliance on meaningful information encoded in the latents, rather than superficial distributional shortcuts.

4. Noised. We add perturbations to the latent communication H H : (a) CovNoise-0.5 × \times /1.0 × \times : covariance-shaped noise ε t ∼ 𝒩 ⁡ ( 0 , Σ ^ ) \varepsilon_{t}\sim\mathcal{N}(0,\hat{\Sigma}) with optional strength λ ∈ { 0.5 , 1.0 } \lambda\in\{0.5,1.0\} , where Σ ^ \hat{\Sigma} is the sample covariance of the original H H ; (b) WhiteNoise : a control drawn from 𝒩 ⁡ ( 0 , I ) \mathcal{N}(0,I) with the same length. Rationale. Noise-based perturbations interrogate the robustness and locality of latent-space semantics. Covariance-shaped noise preserves global second-order structure, whereas white noise does not, allowing us to assess whether the actor relies on fine-grained geometric relations within true latent trajectories.

5. CovGauss. We replace the entire H H with i.i.d. samples H t ∼ 𝒩 ⁡ ( 0 , Σ ^ ) H_{t}\sim\mathcal{N}(0,\hat{\Sigma}) (0 μ \mu ) and report a robustness check with 𝒩 ⁡ ( μ ^ , Σ ^ ) \mathcal{N}(\hat{\mu},\hat{\Sigma}) ( μ \mu ). These preserve first-second order moments while removing higher-order structure and temporal alignment. Rationale. This variant preserves the mean and covariance of the original latent distribution while discarding all higher-order statistics and temporal correlations. It tests whether latent communication conveys information beyond global moments (first-order and second-order moments), e.g., structured reasoning paths or non-Gaussian manifold geometry.

6. RandomRot. We apply a structure-preserving but information-scrambling transform H ′ = μ ^ + ( H − μ ^ ) Σ ^ − 1 / 2 Q Σ ^ 1 / 2 H^{\prime}=\hat{\mu}+(H-\hat{\mu})\,\hat{\Sigma}^{-1/2}\,Q\,\hat{\Sigma}^{1/2} , where Q Q is a Haar-random orthogonal matrix ( Mezzadri, 2006 ) . Rationale. This preserves the mean/covariance exactly while disrupting higher-order structure. Random rotation strictly preserves the first two moments of the latent distribution while scrambling its geometric orientation and higher-order structure. This constitutes a strong diagnostic of whether the actor depends on directional semantics or sequential organization within the latent manifold, rather than mere distributional similarity.

7. Cross-Family. We evaluate Interlat under a cross-model-family setting, where the sender and actor belong to different pretrained model families. Specifically, latent communications are generated by a sender model from one family (In this work, we use Qwen2.5-7B-Instruct) and consumed by an actor model from another family (LLaMA3.1-8B-Base), without sharing parameters or tokenizer vocabularies. Rationale. This setting tests whether latent communication encodes task-relevant information in a model-agnostic manner, rather than exploiting family-specific activation conventions or implicit alignment.

## Appendix C Benchmark

### C.1 Alfworld

Alfworld Shridhar et al. (2020) is a text-only benchmark that simulates embodied household tasks while keeping interaction purely in natural language. Agents observe textual descriptions of the scene and issue high-level commands from a constrained action set ( e.g., go to, open, close, take, put, toggle on/off, heat, cool, examine). Tasks are long-horizon and compositional, requiring perception, planning, and execution over multiple steps under partial observability. The benchmark provides official train/seen/unseen splits and a standard success metric under a fixed step budget ( e.g., 20 steps in our setup), enabling systematic and reproducible evaluation of sequential decision-making.

## Appendix D Ablations and Step Analysis

We present ablation studies for both the actor and reasoning models, reporting the average number of steps for successful trials versus all trials (success/all).

#### Effect of curriculum learning.

For the actor model, removing curriculum learning forces the agent to interpret latent communications from scratch. As shown in Figure 7 , this leads to highly unstable training dynamics and substantially degraded latent comprehension, preventing the model from consistently leveraging the communicated information.

#### Step count versus performance.

Table 6 reveals a nuanced but systematic relationship between step count and task performance. On seen tasks, ablating key components results in a lower overall success rate. Although these ablated models often take fewer steps on the trials they complete, their high failure rate indicates an inability to reliably interpret latent communication and solve tasks. In contrast, the full model achieves both higher success rates and longer trajectories, suggesting that additional steps correspond to productive exploration rather than inefficiency.

On unseen tasks, several ablations ( e.g., removing curriculum learning or the communication adapter) exhibit the opposite pattern: the agent takes more steps while achieving a lower success rate. This demonstrates that longer trajectories alone do not imply effective exploration. Without these critical components, the policy exhibits unstructured search behavior that fails to form coherent task-solving strategies. Together, these observations underscore the importance of evaluating step count jointly with success rate, and support our central claim that information-rich latent communication enables structured and effective exploration rather than random wandering.

## Appendix E Compression Result

In this section, we provide more detailed results on compression with average steps as success/all across tasks in Table 7 (LLaMA3.1-8B-Base) and Table 8 (Qwen2.5-7B-Base) and corresponding performance trend in Figure 8 . Latency is measured on the same machine and decoding policy (if needed) across rows 2 2 2 For the untrained reasoning model, we use the standard generate API from Hugging Face transformers ; see https://github.com/huggingface/transformers . .

## Appendix F Latent Parallelism Analysis

We first compared the latent communications produced by our trained reasoning model with those from an off-the-shelf Qwen2.5-7B-Instruct model in the compression-effectiveness analysis (see the Experiments section). Because our reasoning model is initialized from Qwen2.5-7B-Base, we additionally compare it with this base model, which has not been trained for generating compressed latent communication, in Figure 9 . The findings are consistent with the earlier comparison: the trained model maintains stable vertical gaps between successive Top- k k curves across steps and exhibits a substantially lower P 50 ​ ( S 10 ) P_{50}(S_{10}) , whereas the base model shows a clear convergence toward Top-1.

We further extend the parallelism analysis to a deeper horizon of 32 steps. As shown in Figure 10 , the trained model exhibits stable vertical gaps between successive Top- k k curves throughout these steps. This extended analysis further verifies that the trained latent representations preserve a broader set of plausible reasoning paths by sustaining a more balanced probability distribution rather than prematurely collapsing to a Top-1 hypothesis.

## Appendix G Qualitative Analysis of Latent Communication via PCA

To qualitatively examine the semantic structure encoded in latent communications, we perform Principal Component Analysis (PCA) on 3,119 samples from the ALFWorld training set. Each sample corresponds to the mean-pooled last-layer hidden state generated by the reasoning agent for a specific task instance. Tasks are grouped according to the official ALFWorld task templates, which define six core reasoning patterns: pick_and_place , pick_clean_then_place , pick_heat_then_place , pick_cool_then_place , look_in_recep , and look_at_obj . Figure 11 visualizes the projection of latent communications onto the first two principal components, which capture the dominant axes of variance across task instances.

The resulting PCA visualization reveals clear task-dependent organization in the latent space. Action-centric templates such as pick_and_place form a dense central cluster, while templates involving additional procedural constraints—such as thermal manipulation in pick_heat_then_place and pick_cool_then_place —occupy adjacent yet separable regions. Perception-oriented tasks ( look_in_recep and look_at_obj ), although less frequent, also exhibit localized concentrations distinct from execution-heavy templates. As PCA preserves global variance structure rather than emphasizing local neighborhoods, this separation indicates that task-specific semantics are encoded in the dominant latent dimensions, rather than arising from projection artifacts. Moreover, intra-cluster dispersion (e.g., within pick_and_place ) suggests that latent representations retain fine-grained variations across task instances, rather than collapsing to a single prototype per template.

Beyond static clustering, we further analyze how these task-level structures are affected by the latent communication adapter. As shown in Figure 12 and quantified in Table 9 , different task templates exhibit consistent but template-dependent centroid shifts before and after transformation. While the absolute magnitudes of these shifts are moderate relative to within-template dispersion, their directions are highly structured, indicating selective reorganization rather than global rescaling of the latent space. Execution-heavy templates such as pick_and_place and pick_heat_then_place undergo larger relative shifts, whereas observation-oriented templates remain more stable. Together, these results suggest that Interlat preserves the overall geometry of latent communications while inducing task-aware semantic alignment, enabling the actor agent to differentiate diverse reasoning paradigms without relying on explicit natural language communication.

## Appendix H Training Template

We present an example in Figure H to illustrate how agents explore and solve tasks in Alfworld. After perceiving the environment, the agent executes an action, receives feedback from the environment, and then proceeds to the next step until the goal is accomplished. Figure H shows an example of how training data is structured for the actor agent. We append either the latent communication or the natural-language plan after the instruction to facilitate inter-agent communication.

## Instructions for reporting errors

We are continuing to improve HTML versions of papers, and your feedback helps enhance accessibility and mobile support. To report errors in the HTML that will help us improve conversion and rendering, choose any of the methods listed below:

Click the "Report Issue" ( ) button, located in the page header.

Tip: You can select the relevant text first, to include it in your report.

Our team has already identified the following issues . We appreciate your time reviewing and reporting rendering errors we may not have found yet. Your efforts will help us improve the HTML versions for all readers, because disability should not be a barrier to accessing research. Thank you for your continued support in championing open access for all.

Have a free development cycle? Help support accessibility at arXiv! Our collaborators at LaTeXML maintain a list of packages that need conversion , and welcome developer contributions .
