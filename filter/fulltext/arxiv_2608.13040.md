##### Report GitHub Issue

Content selection saved. Describe the issue below:

# Latent On-Policy Self-Distillation

###### Abstract

Enabling agents to learn from experience and internalize it into their policy has become a central problem in self-evolving AI. On-policy self-distillation (OPSD) offers an effective pathway by using a privileged self-teacher to provide dense supervision on the student’s own trajectories; however, existing methods still rely heavily on designer-specified privileged artifacts ( e.g. , answers, feedback, skills, or trajectories), limiting the end-to-end learnability and scalability required for continual self-improvement. In this work, we introduce Latent On-Policy Self-Distillation ( LOPD ), which, rather than proposing another hand-crafted OPSD variant with a newly prescribed form of privileged context, makes the teacher’s privileged context itself learnable end-to-end from experience. Technically, LOPD retrieves relevant experiences and composes them into continuous latent tokens that condition a self-teacher, while the student generates trajectories from the task and interaction history and receives dense token-level supervision at every visited prefix. We further introduce a privileged-margin objective to stabilize and regulate the learning of latent context. Empirically, LOPD demonstrates (I) strong performance , outperforming RLVR and representative OPSD methods including OPSD, SDPO, and Skill-SD across both agentic tool use and code generation; and (II) high learning efficiency , surpassing GRPO and Skill-SD with less than 30 % 30\% of their rollout budget. Ablation studies further provide direct evidence that making privileged context learnable is necessary for realizing these gains. Together, these results position LOPD as a step toward a more scalable and self-directed paradigm for agent evolution.

## 1 Introduction

How should an agent learn from experience? A natural answer is to expose the model to prior successful trajectories, corrective feedback, or expert demonstrations, and then train it to internalize the behaviors they reveal. This intuition has made on-policy distillation (OPD) a central paradigm for experience learning in large language models: the student first samples its own trajectory, and a teacher then provides dense token-level supervision on the states the student actually visits ( Song & Zheng, 2026 ; Li et al., 2026b ) . Compared with off-policy imitation, OPD reduces the mismatch between training and inference; compared with reinforcement learning with verifiable rewards (RLVR), it converts sparse outcome feedback into fine-grained distributional signals over the student’s own rollout ( Hübotter et al., 2026 ; Yang et al., 2026 ) . In this view, OPD is not merely a compression technique for a stronger model, but a mechanism for turning external experience into persistent policy improvement.

On-policy self-distillation (OPSD) has recently emerged as an especially appealing form of this paradigm because it removes the dependence on a separate, stronger teacher. Instead, the teacher and the student are instantiated from the same model under different contexts: the student acts from the task and interaction history, while the teacher additionally receives privileged information such as verified reasoning traces, final answers, environment feedback, or successful prior rollouts ( Zhao et al., 2026 ; Hübotter et al., 2026 ; Penaloza et al., 2026 ) . The privileged context makes the teacher distribution more informative than the student’s, enabling dense feedback without querying an external model. This design shifts the central question of OPSD from which teacher is strong enough? to what privileged context should be given to the self-teacher? The answer matters: the context must expose useful experience, make token-level supervision sharper, and yet remain compatible with a student that will not see that context at inference time.

Existing substrates for privileged experience remain imperfect in a more fundamental sense. Although prior work instantiates privileged context in many forms—verified answers, reasoning traces, environment feedback, contrastive evidence, or action-only trajectories ( Zhao et al., 2026 ; Hübotter et al., 2026 ; Yu et al., 2026c ; Penaloza et al., 2026 ; Yang et al., 2026 ) —these contexts are typically hand-designed or rule-extracted transformations of experience. They decide a priori what the teacher should see: an oracle answer, a textual reflection, a successful rollout, a retrieved document, or another discrete artifact. Such substrates can be useful, but they also constrain self-distillation to the information format chosen by the designer, rather than allowing the teacher to learn which aspects of prior experience are actually useful for supervising the student’s current trajectory. This motivates a substrate-level question for OPSD:

To address this challenge, we propose Latent On-Policy Self-Distillation ( LOPD ), a framework that realizes privileged context as a learnable latent substrate . Its training pipeline otherwise follows standard OPSD: the student first rolls out trajectories from the task and interaction history, and the teacher re-evaluates every visited prefix to provide dense token-level distributions, against which the student is optimized through reverse-KL distillation. The key difference is that the teacher is conditioned not on a pre-defined privileged artifact, but on learnable latent context instantiated by a composer that transforms retrieved experiences into compact continuous tokens. Because this context is differentiable, the same training process that improves the student also teaches the composer which aspects of experience to retain and how to organize them into effective teacher supervision. To ensure that this learning makes the teacher more informative rather than merely easier for the student to match, we introduce a privileged-margin constraint that requires the teacher to maintain a verifiable log-probability advantage over the student. After training, only the student is retained: inference requires no experience database, retrieval module, composer, or latent context. In this way, LOPD turns experience from a hand-crafted input artifact into an end-to-end learnable supervision substrate whose benefits are internalized by the student policy.

Our contributions are summarized as follows: • Context Re-formulation. We reformulate privileged context from pre-defined, hand-designed textual artifacts into an end-to-end learnable latent substrate, allowing the teacher to automatically extract task-relevant supervision signals from prior experience.

• Proposed Solution. We develop LOPD , which composes retrieved experiences into continuous latent context for the self-teacher and jointly optimizes the privileged context and student through on-policy distillation. A privileged-margin constraint keeps the learned context informative and prevents the teacher from collapsing toward the student.

• Experimental Validation. LOPD consistently surpasses RLVR and representative OPSD methods over three model backbones and seven benchmarks, and outperforms GRPO and Skill-SD with less than 30 % 30\% of their rollout budget. Further ablation studies directly establish the necessity of jointly learning the privileged context.

## 2 Related Work

#### On-Policy (Self-)Distillation.

On-policy distillation trains a student on trajectories sampled from its own policy while querying a teacher for dense token-level supervision on the visited states ( Song & Zheng, 2026 ; Li et al., 2026b ) . Recent work has applied this recipe broadly: reasoning and efficient post-training ( Wu et al., 2026a ; Jin et al., 2026 ; Fu et al., 2026 ) , long-context modeling ( Zhang et al., 2026a ) , context and knowledge distillation ( Ye et al., 2026 ; Lazaridis et al., 2026 ) , GUI grounding ( Zhang et al., 2026b ) , and multimodal domains such as video grounding ( Li et al., 2026a ) , speech alignment ( Cao et al., 2026 ) , and visual reasoning ( Yuan et al., 2026 ; Liu et al., 2026 ) . Within this landscape, on-policy self-distillation (OPSD) removes the external teacher by instantiating teacher and student from the same model under different contexts: the student acts under the deployable input, while the teacher receives privileged context ( Zhao et al., 2026 ; Hübotter et al., 2026 ; Penaloza et al., 2026 ; Yang et al., 2026 ; Yu et al., 2026c ) . This line is best understood by the form of privileged context it supplies: verified answers and reasoning traces ( Zhao et al., 2026 ; Yang et al., 2026 ) , rich environment feedback or self-revision signals ( Hübotter et al., 2026 ; He et al., 2026 ; Zhang et al., 2026c ) , contrastive or peer-rollout evidence ( Yu et al., 2026a ; Pan et al., 2026 ) , action-only frontier-agent trajectories ( Penaloza et al., 2026 ) , and retrieved or evidence-guided context ( Ye et al., 2026 ; Lazaridis et al., 2026 ) . These designs demonstrate that privileged context is the key interface through which OPSD converts experience into supervision, but the context itself is usually pre-defined as a textual or discrete artifact; in contrast, LOPD makes the privileged context a learnable latent substrate jointly optimized with distillation.

#### Latent Computation.

Latent computation uses continuous latent tokens/embeddings or hidden states as the carrier of LLM computation rather than natural language ( Yu et al., 2026b ; Zhu et al., 2025 ) . In reasoning , latent tokens can expand the model’s internal compute budget ( Deng et al., 2026 ; Hao et al., 2025 ; Amos et al., 2026 ) , letting the model perform deeper deliberation before producing an answer. In memory , latent states can serve as compact carriers of procedural ( Zhang et al., 2025 ; Yu et al., 2026d ) , factual ( Wang et al., 2024 ; Feng et al., 2026 ) , and experiential ( Hou et al., 2026 ; Wu et al., 2026b ) information, preserving reusable experience without exposing long textual traces in the prompt. In planning , latent computation can represent intermediate plans, subgoals, or world-state summaries that guide downstream actions while remaining flexible and differentiable. Our method is conceptually close to latent memory, but uses it in a different role: the latent state is not an inference-time augmentation, but a learnable privileged context through which an on-policy teacher supervises a student that does not observe this context.

## 3 Method

### 3.1 Problem Setup: Privileged Context in OPSD

We consider a multi-turn agent that receives a task x x and interacts with an environment through observations and actions. We call the acting policy the student . At turn t t , the student observes 𝒔 t = ( x , 𝒐 ≤ t , 𝒂 < t ) \bm{s}_{t}=(x,\bm{o}_{\leq t},\bm{a}_{<t}) , where 𝒐 ≤ t \bm{o}_{\leq t} denotes observations so far and 𝒂 < t \bm{a}_{<t} denotes previous actions, and samples actions to form a trajectory: 𝒂 t ∼ π θ S ( ⋅ ∣ 𝒔 t ) , 𝝉 = ( 𝒔 1 , 𝒂 1 , … , 𝒔 | 𝝉 | , 𝒂 | 𝝉 | ) ∼ π θ S ( ⋅ ∣ x ) , \bm{a}_{t}\sim\pi_{\theta}^{S}(\cdot\mid\bm{s}_{t}),\qquad\bm{\tau}=(\bm{s}_{1},\bm{a}_{1},\ldots,\bm{s}_{|\bm{\tau}|},\bm{a}_{|\bm{\tau}|})\sim\pi_{\theta}^{S}(\cdot\mid x), (1) where 𝒂 t = ( a t , 1 , … , a t , L t ) \bm{a}_{t}=(a_{t,1},\ldots,a_{t,L_{t}}) is the tokenized action at turn t t , L t L_{t} is its length, and | 𝝉 | |\bm{\tau}| is the number of turns. OPSD constructs a teacher by giving the same model additional privileged context. Abstractly, this context is obtained from some experience source ℰ \mathcal{E} by a fixed transformation: 𝒄 fix = Φ fix ( x , ℰ ) , π θ T ( ⋅ ∣ 𝒔 t , 𝒄 fix ) = π θ ( ⋅ ∣ [ 𝒔 t ; 𝒄 fix ] ) , \bm{c}_{\mathrm{fix}}=\Phi_{\mathrm{fix}}(x,\mathcal{E}),\qquad\pi_{\theta}^{T}(\cdot\mid\bm{s}_{t},\bm{c}_{\mathrm{fix}})=\pi_{\theta}(\cdot\mid[\bm{s}_{t};\bm{c}_{\mathrm{fix}}]), (2) where ℰ \mathcal{E} may contain answers, traces, feedback, demonstrations, or retrieved trajectories, and Φ fix \Phi_{\mathrm{fix}} is a designer-specified rule that decides what artifact the teacher sees. Given a student trajectory, OPSD matches teacher and student distributions on the same visited prefixes: ℒ OPSD ( θ ) = 𝔼 𝝉 ∼ π θ S [ ∑ t = 1 | 𝝉 | ∑ n = 1 L t D ( sg [ π θ T ( ⋅ ∣ 𝒔 t , 𝒄 fix , a t , < n ) ] ∥ π θ S ( ⋅ ∣ 𝒔 t , a t , < n ) ) ] , \displaystyle\mathcal{L}_{\mathrm{OPSD}}(\theta)=\mathbb{E}_{\bm{\tau}\sim\pi_{\theta}^{S}}\left[\sum_{t=1}^{|\bm{\tau}|}\sum_{n=1}^{L_{t}}D\!\left(\operatorname{sg}\!\left[\pi_{\theta}^{T}(\cdot\mid\bm{s}_{t},\bm{c}_{\mathrm{fix}},a_{t,<n})\right]\middle\|\pi_{\theta}^{S}(\cdot\mid\bm{s}_{t},a_{t,<n})\right)\right], (3) where a t , < n a_{t,<n} is the action prefix before token n n , D D is a token-level divergence, and sg ⁡ [ ⋅ ] \operatorname{sg}[\cdot] denotes stop-gradient. This setup makes the limitation explicit: the supervision quality is bounded by a pre-defined context constructor. We instead parameterize the constructor: 𝒄 ϕ = Φ ϕ ​ ( x , ℰ ) = ⟨ e 1 ⟩ ⊕ ⟨ e 2 ⟩ ⊕ ⋯ ⊕ ⟨ e K ⟩ , \bm{c}_{\phi}=\Phi_{\phi}(x,\mathcal{E})=\langle e_{1}\rangle\oplus\langle e_{2}\rangle\oplus\cdots\oplus\langle e_{K}\rangle, (4) where Φ ϕ \Phi_{\phi} is a learnable composer, ⟨ e i ⟩ \langle e_{i}\rangle is a continuous latent token, K K is the number of latent tokens per retrieved experience, and ⊕ \oplus denotes context concatenation. The goal of LOPD is to make privileged context itself learnable while preserving the defining asymmetry of OPSD: the teacher additionally observes 𝒄 ϕ \bm{c}_{\phi} , whereas the student continues to condition only on 𝒔 t \bm{s}_{t} .

### 3.2 Learnable Latent Privileged Context

LOPD instantiates Φ ϕ \Phi_{\phi} as a latent-context composer. We deliberately begin with a minimal experience pipeline. Offline, we retain successful rollouts in an experience bank, with each entry storing its task description and a compact action–result trace that omits verbose observations. For a current task x x , a dense retriever embeds the query and each stored task–trajectory pair, then returns the top- J J entries under cosine similarity; these entries form ℰ = { m j } j = 1 J \mathcal{E}=\{m_{j}\}_{j=1}^{J} . Full construction and retrieval details are provided in Section A.3 .

Given x x and the retrieved set ℰ \mathcal{E} , the composer first encodes each item into hidden states: 𝐇 j = Enc ψ ⁡ ( x , m j ) ∈ ℝ T j × d , \mathbf{H}_{j}=\operatorname{Enc}_{\psi}(x,m_{j})\in\mathbb{R}^{T_{j}\times d}, (5) where m j m_{j} is the j j -th retrieved trajectory, Enc ψ \operatorname{Enc}_{\psi} is the encoder that maps the task–experience pair into hidden states, T j T_{j} is the encoded sequence length, and d d is the hidden dimension. The variable-length states are compressed into a fixed number of latent tokens by a lightweight latent compressor. In our implementation, this compressor is QFormer-style cross-attention with learned queries, although other latent-token generators can be used under the same abstraction: 𝐄 j = Comp χ ⁡ ( 𝐇 j ; 𝐐 χ ) = [ ⟨ e j , 1 ⟩ , … , ⟨ e j , K ⟩ ] ∈ ℝ K × d , \mathbf{E}_{j}=\operatorname{Comp}_{\chi}(\mathbf{H}_{j};\mathbf{Q}_{\chi})=[\langle e_{j,1}\rangle,\ldots,\langle e_{j,K}\rangle]\in\mathbb{R}^{K\times d}, (6) where Comp χ \operatorname{Comp}_{\chi} is the compressor, 𝐐 χ ∈ ℝ K × d \mathbf{Q}_{\chi}\in\mathbb{R}^{K\times d} is a learned query bank, and 𝐄 j \mathbf{E}_{j} is the latent representation of experience item m j m_{j} . We use ϕ ≔ ( ψ , χ ) \phi\coloneqq(\psi,\chi) to denote all trainable composer parameters, comprising the encoder LoRA parameters ψ \psi and compressor parameters χ \chi ; the encoder backbone itself remains frozen. Note that we do not treat the particular attention block as a contribution; its role is simply to produce a compact, differentiable context (details in Section A.1 ). The teacher receives the latent tokens as ordinary context positions: 𝒄 ϕ ( x , ℰ ) = ⨁ j = 1 J ( ⟨ e j , 1 ⟩ ⊕ ⋯ ⊕ ⟨ e j , K ⟩ ) , π θ ¯ , ϕ T ( ⋅ ∣ 𝒔 , 𝒄 ϕ ) = π θ ¯ ( ⋅ ∣ [ 𝒔 ; 𝒄 ϕ ] ) , \bm{c}_{\phi}(x,\mathcal{E})=\bigoplus_{j=1}^{J}(\langle e_{j,1}\rangle\oplus\cdots\oplus\langle e_{j,K}\rangle),\qquad\pi_{\bar{\theta},\phi}^{T}(\cdot\mid\bm{s},\bm{c}_{\phi})=\pi_{\bar{\theta}}(\cdot\mid[\bm{s};\bm{c}_{\phi}]), (7) where 𝒔 \bm{s} is an interaction state defined above and 𝒄 ϕ \bm{c}_{\phi} is the learned privileged context. Each ⟨ e j , k ⟩ \langle e_{j,k}\rangle is implemented as a continuous embedding and behaves like a special token in the teacher’s context window. The composer is cold-started on successful trajectories with the backbone frozen, yielding ϕ 0 \phi_{0} . During subsequent joint optimization, both the encoder LoRA parameters ψ \psi and compressor parameters χ \chi remain trainable as part of ϕ \phi , while the teacher backbone θ ¯ \bar{\theta} stays fixed (details in Section A.2 ).

### 3.3 Latent On-Policy Self-Distillation

Having specified how the teacher is constructed, we now describe the self-distillation process. The student first produces a multi-turn trajectory conditioned only on 𝒔 t \bm{s}_{t} . The composer then constructs 𝒄 ϕ \bm{c}_{\phi} from retrieved experience, and the teacher re-evaluates the same student prefixes with this additional context. We instantiate the teacher as a frozen reference copy θ ¯ \bar{\theta} initialized from the same backbone as the student; the two share architecture and initialization, but not weights after the student begins updating. For every turn t t and token position n n , we define: 𝒑 S t , n = π θ S ( ⋅ ∣ 𝒔 t , a t , < n ) , 𝒑 T t , n = π θ ¯ , ϕ T ( ⋅ ∣ 𝒔 t , 𝒄 ϕ ( x , ℰ ) , a t , < n ) , \displaystyle\bm{p}^{S}_{t,n}=\pi_{\theta}^{S}\big(\cdot\mid\bm{s}_{t},a_{t,<n}\big),\;\bm{p}^{T}_{t,n}=\pi_{\bar{\theta},\phi}^{T}\big(\cdot\mid\bm{s}_{t},\bm{c}_{\phi}(x,\mathcal{E}),a_{t,<n}\big), (8) where 𝒑 t , n S \bm{p}^{S}_{t,n} and 𝒑 t , n T \bm{p}^{T}_{t,n} are next-token distributions over the vocabulary 𝒱 \mathcal{V} , and θ ¯ \bar{\theta} denotes a fixed base-model checkpoint whose parameters receive no gradient updates; however, the teacher’s forward activations remain in the computation graph, so 𝒑 t , n T \bm{p}^{T}_{t,n} is differentiable with respect to 𝒄 ϕ \bm{c}_{\phi} and hence to ϕ \phi . To keep logit-level distillation efficient, we follow ( Zhao et al., 2026 ) and use the teacher top- M M vocabulary entries plus a tail bucket. This preserves the teacher’s high-probability modes while accounting for the remaining probability mass: 𝒑 ~ t , n T ​ ( v ) = { 𝒑 t , n T ​ ( v ) , v ∈ 𝒱 t , n M , 1 − ∑ u ∈ 𝒱 t , n M 𝒑 t , n T ​ ( u ) , v = ⊥ , ​ 𝒑 ~ t , n S ​ ( v ) = { 𝒑 t , n S ​ ( v ) , v ∈ 𝒱 t , n M , 1 − ∑ u ∈ 𝒱 t , n M 𝒑 t , n S ​ ( u ) , v = ⊥ , , \tilde{\bm{p}}^{T}_{t,n}(v)=\begin{cases}\bm{p}^{T}_{t,n}(v),&v\in\mathcal{V}_{t,n}^{M},\\ 1-\sum_{u\in\mathcal{V}_{t,n}^{M}}\bm{p}^{T}_{t,n}(u),&v=\bot,\end{cases}\;\tilde{\bm{p}}^{S}_{t,n}(v)=\begin{cases}\bm{p}^{S}_{t,n}(v),&v\in\mathcal{V}_{t,n}^{M},\\ 1-\sum_{u\in\mathcal{V}_{t,n}^{M}}\bm{p}^{S}_{t,n}(u),&v=\bot,\end{cases}, (9) where 𝒱 t , n M \mathcal{V}_{t,n}^{M} is the teacher top- M M support at prefix ( t , n ) (t,n) and ⊥ \bot denotes the aggregated tail event. The distillation objective matches teacher and student on the student’s own multi-turn trajectory: ℒ distill ( θ , ϕ ) = 𝔼 x ∼ 𝒟 𝔼 𝝉 ∼ π θ S ( ⋅ ∣ x ) [ ∑ t = 1 | 𝝉 | ∑ n = 1 L t ω t , n ​ D KL ​ ( 𝒑 ~ t , n S ∥ 𝒑 ~ t , n T ) ∑ t = 1 | 𝝉 | ∑ n = 1 L t ω t , n ] , \displaystyle\mathcal{L}_{\mathrm{distill}}(\theta,\phi)=\mathbb{E}_{x\sim\mathcal{D}}\mathbb{E}_{\bm{\tau}\sim\pi_{\theta}^{S}(\cdot\mid x)}\left[\frac{\sum_{t=1}^{|\bm{\tau}|}\sum_{n=1}^{L_{t}}\omega_{t,n}\,D_{\mathrm{KL}}\!\left(\tilde{\bm{p}}^{S}_{t,n}\middle\|\tilde{\bm{p}}^{T}_{t,n}\right)}{\sum_{t=1}^{|\bm{\tau}|}\sum_{n=1}^{L_{t}}\omega_{t,n}}\right], (10) where 𝒟 \mathcal{D} is the task distribution and ω t , n ∈ { 0 , 1 } \omega_{t,n}\in\{0,1\} masks supervised action tokens. We use reverse KL so that the student concentrates on teacher-supported behavior. Because θ ¯ \bar{\theta} denotes a fixed checkpoint while ϕ \phi remains trainable, the distillation gradient flows through the frozen network back to the latent input (injection mechanism in Section A.4 ). This allows the composer to learn which experience features produce effective teacher supervision for the current student trajectory.

#### Privileged-Margin Constraint.

The distillation loss alone does not ensure that the teacher provides more effective supervision: an unconstrained composer can instead minimize Equation 10 by moving 𝒑 T \bm{p}^{T} toward 𝒑 S \bm{p}^{S} , yielding uninformative latent context without improving the student. We therefore prevent this collapse in two ways. ❶ First, the cold start in Section 3.2 initializes the composer to transform experience into informative latent context. ❷Second, we introduce outcome reward into the supervision signal, and more concretely, impose a privileged-margin constraint that ties the teacher’s token-level advantage to the verified outcome of the complete trajectory. For each supervised token, we define the per-token privilege: δ t , n ​ ( ϕ ) = log ⁡ π θ ¯ , ϕ T ​ ( a t , n ∣ 𝒔 t , 𝒄 ϕ , a t , < n ) − sg ⁡ [ log ⁡ π θ S ​ ( a t , n ∣ 𝒔 t , a t , < n ) ] , \delta_{t,n}(\phi)=\log\pi^{T}_{\bar{\theta},\phi}\!\left(a_{t,n}\mid\bm{s}_{t},\bm{c}_{\phi},a_{t,<n}\right)-\operatorname{sg}\!\left[\log\pi^{S}_{\theta}\!\left(a_{t,n}\mid\bm{s}_{t},a_{t,<n}\right)\right], (11) where a t , n a_{t,n} is the student’s sampled token and sg \operatorname{sg} blocks gradients to θ \theta through this path. Both log-probabilities are already computed during the teacher and student forward passes; δ t , n \delta_{t,n} requires only a gather, not an additional forward. We then use the trajectory-level verification signal A ⁡ ( 𝝉 ) = 2 ​ r ​ ( 𝝉 ) − 1 ∈ [ − 1 , 1 ] A(\bm{\tau})=2r(\bm{\tau})-1\in[-1,1] , where r ⁡ ( 𝝉 ) r(\bm{\tau}) is the outcome reward, to favor teacher advantages on successful trajectories and suppress them on unsuccessful ones: Δ ⁡ ( ϕ ) = 𝔼 𝝉 ​ [ ∑ t , n ω t , n ​ A ​ ( 𝝉 ) ​ δ t , n ​ ( ϕ ) ∑ t , n ω t , n ] . \Delta(\phi)=\mathbb{E}_{\bm{\tau}}\!\left[\frac{\sum_{t,n}\omega_{t,n}\,A(\bm{\tau})\,\delta_{t,n}(\phi)}{\sum_{t,n}\omega_{t,n}}\right]. (12) The full LOPD objective constrains ϕ \phi to maintain a minimum privilege level m > 0 m>0 : min θ , ϕ ⁡ max β ≥ 0 ​ ℒ distill ​ ( θ , ϕ ) + β ⁡ ( m − Δ ⁡ ( ϕ ) ) + λ ​ ‖ 𝒄 ϕ − sg ⁡ [ 𝒄 ϕ 0 ] ‖ 2 2 , \min_{\theta,\phi}\;\max_{\beta\geq 0}\;\;\mathcal{L}_{\mathrm{distill}}(\theta,\phi)\;+\;\beta\!\left(m-\Delta(\phi)\right)+\;\lambda\left\|\bm{c}_{\phi}-\operatorname{sg}\!\left[\bm{c}_{\phi_{0}}\right]\right\|_{2}^{2}, (13) where β \beta is a dual variable updated by β ← [ β + η β ​ ( m − Δ ⁡ ( ϕ ) ) ] + \beta\leftarrow[\beta+\eta_{\beta}(m-\Delta(\phi))]_{+} , and the anchor term penalizes drift from the initialization ϕ 0 \phi_{0} in latent space, requiring no additional forward pass. If the composer degenerates to uninformative context, π T → π S \pi^{T}\to\pi^{S} , δ t , n → 0 \delta_{t,n}\to 0 , Δ → 0 < m \Delta\to 0<m , and the dual penalty activates—structurally excluding the trivial solution. Within the feasible region, outcome-weighted privilege steers the composer toward evidence that supports successful behavior, while the distillation gradient determines how that evidence is selected and encoded.

#### Algorithm Summary.

Algorithm 1 summarizes the overall workflow of LOPD . The loop collects on-policy trajectories from the student, constructs learnable latent privileged context from retrieved experience, evaluates the same visited prefixes with the teacher, and jointly updates the student and composer while adjusting the dual variable to maintain the privilege margin. At inference, only the student policy π θ S \pi_{\theta}^{S} is deployed and used.

## 4 Experiments

### 4.1 Experiment Setup

#### Training.

We evaluate LOPD under two post-training settings: ❶ agentic tool-use and ❷ coding . For tool-use training, we use the EnvScaler-derived tool-interactive corpus ( Song et al., 2026 ) , comprising 2,349 2{,}349 tasks. For coding, we use the TACO subset of DeepCoder ( TogetherAI, 2025 ) , comprising 7 7 K verified Python problems (see Section B.2 for training details). The used model backbones include Qwen3-4B , Qwen3-8B ( Yang et al., 2025 ) , Olmo3-7B ( Olmo et al., 2026 ) .

#### Evaluation.

Our evaluation mirrors the two training regimes while keeping all test sets disjoint from training data. For tool-use, we report the EnvScaler task success metric on a held-out test split of 200 200 tasks disjoint from the training pool, BFCL-v3 scores across base, missing-function, missing-parameter, and long-context subsets ( Patil et al., 2025 ) , and ACEBench multi-step and multi-turn scores ( Chen et al., 2025 ) . For coding, we report pass@1 on LiveCodeBench v5/v6 ( Jain et al., 2024 ) , HumanEval+ and MBPP+ ( Liu et al., 2023 ) (evaluation protocols in Section B.3 ).

#### Baselines.

We compare against the baselines reported in Tables 1 and 2 . Vanilla denotes the unadapted backbone. GRPO is the outcome-reward RL baseline ( Shao et al., 2024 ) . SDFT ( Shenfeld et al., 2026 ) is a demonstration-conditioned distillation baseline. The OPSD-style baselines include OPSD ( Zhao et al., 2026 ) , SDPO ( Hübotter et al., 2026 ) , and Skill-SD ( Wang et al., 2026 ) , whose privileged contexts respectively instantiate answer/trace, feedback-conditioned self-teacher, and skill-conditioned supervision. Detailed baseline configurations are provided in Section B.1 .

#### Configurations.

All trainable methods share the same backbone, training split and evaluation protocol within each setting. For LOPD , the teacher receives latent context composed from J = 3 J{=}3 retrieved experiences, each compressed into K = 32 K{=}32 latent tokens ( 96 96 total); the distillation loss uses reverse KL with SDPO-style top- M M logits plus a tail bucket, with M = 20 M{=}20 by default. The privileged-margin threshold is m = 0.05 m{=}0.05 ; the verification signal is A ⁡ ( 𝝉 ) = 2 ​ r ​ ( 𝝉 ) − 1 A(\bm{\tau})=2r(\bm{\tau})-1 where r r is the environment reward. Tool-use rollouts are capped at 30 30 environment steps. Coding distillation uses a 16,384 16{,}384 -token response budget. We keep decoding temperature/top- p p fixed across methods within each benchmark, each baseline retains its original KL direction and loss formulation ( Section B.1 ), and within the on-policy training loop the methods differ only in privileged context construction and distillation loss. Prompt templates are provided in Section A.5 .

### 4.2 Main Results

We evaluate whether latent privileged context improves self-distillation learning across tool use and code generation domains in Tables 1 and 2 .

#### Performance.

LOPD obtains the best aggregate result in all ten backbone–benchmark comparisons. On tool use with Qwen3-4B , it improves over the strongest competing method from 61.8 61.8 to 63.7 63.7 on EnvScaler, from 25.25 25.25 to 27.38 27.38 on BFCL-v3, and from 56.0 56.0 to 60.6 60.6 on ACEBench. The advantage becomes larger with Qwen3-8B : LOPD reaches 66.4 / 29.88 / 62.7 66.4/29.88/62.7 on EnvScaler, BFCL-v3, and ACEBench, compared with the strongest baseline results of 60.2 / 29.00 / 58.0 60.2/29.00/58.0 , respectively. The same trend extends beyond interactive agents. With Qwen3-4B , LOPD improves the LiveCodeBench and EvalPlus aggregates to 48.78 48.78 and 81.36 81.36 ; with Olmo3-7B , it reaches 50.98 50.98 and 78.41 78.41 , outperforming the strongest alternatives by 2.69 2.69 and 0.55 0.55 points. These results indicate that LOPD ’s improvement transfers across task formats and model families.

#### No Hand-Crafted Context Is Universally Optimal.

A careful reader may notice that adding privileged information does not always improve upon the vanilla model in Tables 1 and 2 . For example, with Qwen3-4B , SDPO falls from 22.88 22.88 to 15.75 15.75 on BFCL-v3, from 50.6 50.6 to 38.0 38.0 on ACEBench, and from 45.61 45.61 to 38.78 38.78 on LiveCodeBench; OPSD likewise reduces the LiveCodeBench aggregate to 40.24 40.24 . More revealingly, the utility of the same context can reverse across settings: OPSD raises the BFCL-v3 long-context score from 22.00 22.00 to 29.00 29.00 , yet remains below vanilla on the overall BFCL-v3 score with Qwen3-8B ( 25.75 25.75 vs. 28.38 28.38 ) and on LiveCodeBench with both backbones ( 40.24 40.24 vs. 45.61 45.61 and 44.39 44.39 vs. 46.34 46.34 ). This behavior is consistent with how these contexts are constructed. SDPO can condition only on successful siblings produced by the current rollout group, making its privileged signal dependent on the current policy’s success coverage; OPSD instead injects a fixed oracle trace, which can be highly informative when its procedure matches the current task but need not align with the particular prefix or valid solution path visited by the student. A context format that helps in one regime can therefore become sparse, mismatched, or overly prescriptive in another. The issue is not simply whether privileged information is available, but whether its representation remains appropriate across tasks and learning states.

#### Learnable Context Matters.

LOPD avoids committing the teacher to a fixed answer, demonstration, sibling rollout, or discrete skill. Instead, it learns a compact continuous representation directly from retrieved trajectories, allowing the privileged signal to adapt to the task and the student’s visited prefixes. Unlike the reversals above, LOPD remains above the vanilla model in all ten aggregate backbone–benchmark settings, with gains ranging from 1.50 1.50 points on BFCL-v3 with Qwen3-8B to 17.2 17.2 points on EnvScaler with the same backbone. It also consistently improves over prescribed-context baselines: with Qwen3-8B , LOPD exceeds OPSD, SDFT, and Skill-SD by 14.4 / 10.2 / 6.2 14.4/10.2/6.2 points on EnvScaler and 10.0 / 8.0 / 6.7 10.0/8.0/6.7 points on ACEBench, respectively. Together, the results favor optimizing the representation of experience for supervision over searching for an increasingly elaborate hand-crafted artifact.

### 4.3 Framework Analysis

#### Effect of Joint Optimization.

Does joint optimization actually produce a better privileged context, or merely introduce additional trainable parameters? This is the central ablation behind our claim. Figure 3 compares a frozen composer with jointly optimized variants and evaluates each resulting student without retrieved experience or latent context, so the difference reflects what context learning transfers into the policy. Training with a frozen composer ( ϕ 0 \phi_{0} ) achieves 0.573 0.573 . Without the margin constraint ( m = 0 m{=}0 ), the student drops to 0.551 0.551 , indicating that unconstrained distillation gradients degrade the latent context. Weak margins ( m ≤ 0.01 m{\leq}0.01 ) do not prevent this decline. With m ≥ 0.02 m{\geq}0.02 , the student surpasses the frozen-composer baseline, reaching 0.637 0.637 at m = 0.05 m{=}0.05 and 0.626 0.626 at m = 0.10 m{=}0.10 . The improvement suggests that the distillation process exposes the composer to a signal unavailable during initialization: what evidence the current student’s trajectory distribution requires from the privileged context. The margin constraint is necessary to realize this benefit—without it, collapsing the teacher toward the student is a lower-resistance path than learning a more informative representation.

#### Training Dynamics and Sample Efficiency.

Beyond final performance, a practical question is whether LOPD reaches strong performance with fewer on-policy generations. To test this, Figure 4 tracks the strongest baselines over the same 1,600 1{,}600 -generation budget. LOPD exceeds 0.61 0.61 mean reward after 320 320 generations and reaches 0.637 0.637 by generation 576 576 . Its reward then remains in a narrow 0.63 0.63 – 0.64 0.64 range through generation 1,600 1{,}600 , showing that the early gain is sustained rather than caused by a shorter training horizon. GRPO and Skill-SD improve more gradually and finish at 0.611 0.611 and 0.588 0.588 , respectively. The persistent early separation suggests that the latent teacher extracts a denser learning signal from each visited trajectory.

#### Sensitivity Analysis.

How much latent capacity and retrieved experience does the learnable substrate actually need? We vary the number of latent tokens produced by the composer and the number of experiences retrieved during training, then evaluate the resulting student alone. Figure 5 (a) shows a capacity threshold in the latent bottleneck. EnvScaler reward remains near 0.56 0.56 with 8 8 or 16 16 tokens per experience, rises sharply to 0.637 0.637 with 32 32 , and then fluctuates without a consistent gain at 64 64 and 128 128 . We therefore use K = 32 K{=}32 tokens per experience as the smallest setting that escapes the low-capacity regime. Retrieval sensitivity is shown in Figure 5 (b–e), where n ret n_{\mathrm{ret}} varies from 1 1 to 10 10 . EnvScaler reward improves from 0.605 0.605 with one retrieval to 0.637 0.637 with three, but additional retrievals yield no monotonic benefit. At the default n ret = 3 n_{\mathrm{ret}}{=}3 , ACEBench reaches 56.6 56.6 on M-Step, 63.3 63.3 on M-Turn, and 60.6 60.6 overall, matching the main result in Table 1 . Larger retrieval counts can improve one ACEBench regime without producing the same trajectory in the other, and the aggregate remains on a broad plateau rather than varying monotonically. We therefore retain n ret = 3 n_{\mathrm{ret}}{=}3 as the earliest setting that attains the strongest EnvScaler reward while already reaching competitive ACEBench performance.

#### Behavioral Internalization.

Finally, higher reward alone does not reveal what the student has internalized. We therefore ask whether LOPD changes how the student interacts with the environment. Table 3 shows that the distilled student inherits the interaction pattern induced by latent context. Relative to the vanilla model, LOPD uses more environment steps ( 17.04 17.04 vs. 11.12 11.12 ) but makes far fewer tool calls per step ( 1.11 1.11 vs. 3.50 3.50 ), indicating a shift from issuing many speculative calls at once to executing a more sequential plan. Its first-step response is 37.5 % 37.5\% shorter, repeated calls fall from 8.89 8.89 to 5.25 5.25 , and reward per tool call rises from 0.038 0.038 to 0.050 0.050 . The latent-context-conditioned base model and the final student exhibit the same qualitative pattern, providing behavioral evidence that LOPD internalizes the teacher’s procedural guidance rather than merely fitting the aggregate reward. Per-experiment configurations are detailed in Section B.4 .

### 4.4 Case Study

Having established that the latent context improves learning, a natural question is what these continuous tokens actually encode. To obtain a qualitative view, we apply the frozen language-model head to each of the 32 32 latent tokens and inspect ten tool-use and ten coding examples, with and without task conditioning. Figure 6 shows two representative cases. In the agentic example, the current task and retrieved trajectory share the same add–update–change–withdraw operation schema despite using different entities. In the coding example, the retrieved Josephus recurrence matches the circular-elimination structure of the target problem. Nevertheless, both projections remain fragmented mixtures of multilingual and code-like tokens, and task conditioning changes the surface projection without yielding a readable procedure or copying the retrieved solution. This is consistent with a distributed latent representation, although direct decodability alone does not establish which information the teacher functionally uses.

## 5 Conclusion

The question behind this work is not which new artifact should be appended to an OPSD teacher, but whether the teacher’s privileged context can itself be learned from experience. LOPD answers this question by transforming retrieved raw trajectories into differentiable latent privileged context, using the resulting self-teacher to supervise the student’s own visited prefixes, and constraining the learned context to preserve a verifiable teacher advantage. Across agentic tool use and code generation, this formulation achieves the best aggregate result in all ten backbone–benchmark comparisons and surpasses GRPO and Skill-SD with less than 30 % 30\% of their rollout budget. The analyses sharpen this interpretation: retrieval alone is insufficient, unconstrained joint optimization can collapse the teacher toward the student, and the privileged margin turns context learning into productive supervision. The induced behavioral shift remains in the trained student, which acts without privileged context. More broadly, scalable self-evolution should not depend on a succession of increasingly elaborate, human-authored experience formats. Raw trajectories provide a minimal substrate, and richer repositories or retrievers may broaden what is available, but learning should decide what becomes useful guidance. In this sense, LOPD is less another privileged-context recipe than evidence for a different design principle: experience representations should be optimized end-to-end for the policies they are meant to improve.

## References

Amos et al. (2026) Ido Amos, Avi Caciularu, Mor Geva, Amir Globerson, Jonathan Herzig, Lior Shani, and Idan Szpektor. Latent reasoning with supervised thinking states, 2026. URL https://arxiv.org/abs/2602.08332 .

Cao et al. (2026) Di Cao, Dongjie Fu, Hai Yu, Siqi Zheng, Xu Tan, and Tao Jin. X-OPD: Cross-Modal On-Policy Distillation for Capability Alignment in Speech LLMs. arXiv preprint arXiv:2603.24596 , 2026. URL https://arxiv.org/abs/2603.24596 .

Chen et al. (2025) Chen Chen, Xinlong Hao, Weiwen Liu, Xu Huang, Xingshan Zeng, Shuai Yu, Dexun Li, Shuai Wang, Weinan Gan, Yuefeng Huang, Wulong Liu, Xinzhi Wang, Defu Lian, Baoqun Yin, Yasheng Wang, and Wu Liu. Acebench: Who wins the match point in tool usage?, 2025. URL https://arxiv.org/abs/2501.12851 .

Deng et al. (2026) Jingcheng Deng, Liang Pang, Zihao Wei, Shicheng Xu, Zenghao Duan, Kun Xu, Yang Song, Huawei Shen, and Xueqi Cheng. Llm latent reasoning as chain of superposition, 2026. URL https://arxiv.org/abs/2510.15522 .

Feng et al. (2026) Tao Feng, Chongrui Ye, Tianyang Luo, Jingjun Xu, Xueqiang Xu, Haozhen Zhang, Ge Liu, and Jiaxuan You. Elasticmem: Latent memory as a learnable resource for llm agents, 2026. URL https://arxiv.org/abs/2605.30690 .

Fu et al. (2026) Yuqian Fu, Haohuan Huang, Kaiwen Jiang, Jiacai Liu, Zhuo Jiang, Yuanheng Zhu, and Dongbin Zhao. Revisiting On-Policy Distillation: Empirical Failure Modes and Simple Fixes. arXiv preprint arXiv:2603.25562 , 2026. URL https://arxiv.org/abs/2603.25562 .

Hao et al. (2025) Shibo Hao, Sainbayar Sukhbaatar, DiJia Su, Xian Li, Zhiting Hu, Jason Weston, and Yuandong Tian. Training large language models to reason in a continuous latent space, 2025. URL https://arxiv.org/abs/2412.06769 .

He et al. (2026) Yinghui He, Simran Kaur, Adithya Bhaskar, Yongjin Yang, Jiarui Liu, Narutatsu Ri, Liam Fowl, Abhishek Panigrahi, Danqi Chen, and Sanjeev Arora. Self-Distillation Zero: Self-Revision Turns Binary Rewards into Dense Supervision. arXiv preprint arXiv:2604.12002 , 2026. URL https://arxiv.org/abs/2604.12002 .

Hou et al. (2026) Yubo Hou, Zhisheng Chen, Tao Wan, and Zengchang Qin. Flashmem: Distilling intrinsic latent memory via computation reuse, 2026. URL https://arxiv.org/abs/2601.05505 .

Hübotter et al. (2026) Jonas Hübotter, Frederike Lübeck, Lejs Behric, Anton Baumann, Marco Bagatella, Daniel Marta, Ido Hakimi, Idan Shenfeld, Thomas Kleine Buening, Carlos Guestrin, and Andreas Krause. Reinforcement learning via self-distillation, 2026. URL https://arxiv.org/abs/2601.20802 .

Jain et al. (2024) Naman Jain, King Han, Alex Gu, Wen-Ding Li, Fanjia Yan, Tianjun Zhang, Sida Wang, Armando Solar-Lezama, Koushik Sen, and Ion Stoica. LiveCodeBench: Holistic and contamination free evaluation of large language models for code. arXiv preprint arXiv:2403.07974 , 2024.

Jin et al. (2026) Woogyeol Jin, Taywon Min, Yongjin Yang, Swanand Ravindra Kadhe, Yi Zhou, Dennis Wei, Nathalie Baracaldo, and Kimin Lee. Entropy-Aware On-Policy Distillation of Language Models. arXiv preprint arXiv:2603.07079 , 2026. URL https://arxiv.org/abs/2603.07079 .

Lazaridis et al. (2026) Aristotelis Lazaridis, Dylan Bates, Aman Sharma, Brian King, Vincent Lu, and Jack FitzGerald. Edge-opd: Internalizing privileged context with evidence guided on-policy distillation, 2026. URL https://arxiv.org/abs/2605.23493 .

Li et al. (2026a) Jiaze Li, Hao Yin, Haoran Xu, Boshen Xu, Wenhui Tan, Zewen He, Jianzhong Ju, Zhenbo Luo, and Jian Luan. Video-OPD: Efficient Post-Training of Multimodal Large Language Models for Temporal Video Grounding via On-Policy Distillation. arXiv preprint arXiv:2602.02994 , 2026a. URL https://arxiv.org/abs/2602.02994 .

Li et al. (2026b) Yaxuan Li, Yuxin Zuo, Bingxiang He, Jinqian Zhang, Chaojun Xiao, Cheng Qian, Tianyu Yu, Huan ang Gao, Wenkai Yang, Zhiyuan Liu, and Ning Ding. Rethinking on-policy distillation of large language models: Phenomenology, mechanism, and recipe, 2026b. URL https://arxiv.org/abs/2604.13016 .

Liu et al. (2023) Jiawei Liu, Chunqiu Steven Xia, Yuyao Wang, and Lingming Zhang. Is your code generated by chatgpt really correct? rigorous evaluation of large language models for code generation, 2023. URL https://arxiv.org/abs/2305.01210 .

Liu et al. (2026) Ruiqi Liu, Xiaolei Lv, Gengsheng Li, Ximo Zhu, Zhiheng Wang, Zhengbo Zhang, Junkai Chen, Zhiheng Li, Bo Li, Jun Gao, and Shu Wu. Visual-Advantage On-Policy Distillation for Vision-Language Models. arXiv preprint arXiv:2605.21924 , 2026. URL https://arxiv.org/abs/2605.21924 .

Olmo et al. (2026) Team Olmo, :, Allyson Ettinger, Amanda Bertsch, Bailey Kuehl, David Graham, David Heineman, Dirk Groeneveld, Faeze Brahman, Finbarr Timbers, Hamish Ivison, Jacob Morrison, Jake Poznanski, Kyle Lo, Luca Soldaini, Matt Jordan, Mayee Chen, Michael Noukhovitch, Nathan Lambert, Pete Walsh, Pradeep Dasigi, Robert Berry, Saumya Malik, Saurabh Shah, Scott Geng, Shane Arora, Shashank Gupta, Taira Anderson, Teng Xiao, Tyler Murray, Tyler Romero, Victoria Graf, Akari Asai, Akshita Bhagia, Alexander Wettig, Alisa Liu, Aman Rangapur, Chloe Anastasiades, Costa Huang, Dustin Schwenk, Harsh Trivedi, Ian Magnusson, Jaron Lochner, Jiacheng Liu, Lester James V. Miranda, Maarten Sap, Malia Morgan, Michael Schmitz, Michal Guerquin, Michael Wilson, Regan Huff, Ronan Le Bras, Rui Xin, Rulin Shao, Sam Skjonsberg, Shannon Zejiang Shen, Shuyue Stella Li, Tucker Wilde, Valentina Pyatkin, Will Merrill, Yapei Chang, Yuling Gu, Zhiyuan Zeng, Ashish Sabharwal, Luke Zettlemoyer, Pang Wei Koh, Ali Farhadi, Noah A. Smith, and Hannaneh Hajishirzi. Olmo 3, 2026. URL https://arxiv.org/abs/2512.13961 .

Pan et al. (2026) Leyi Pan, Shuchang Tao, Yunpeng Zhai, Lingzhe Zhang, Zhaoyang Liu, Bolin Ding, Aiwei Liu, and Lijie Wen. RLCSD: Reinforcement Learning with Contrastive On-Policy Self-Distillation. arXiv preprint arXiv:2606.11709 , 2026. URL https://arxiv.org/abs/2606.11709 .

Patil et al. (2025) Shishir G Patil, Huanzhi Mao, Fanjia Yan, Charlie Cheng-Jie Ji, Vishnu Suresh, Ion Stoica, and Joseph E. Gonzalez. The berkeley function calling leaderboard (BFCL): From tool use to agentic evaluation of large language models. In Forty-second International Conference on Machine Learning , 2025. URL https://openreview.net/forum?id=2GmDdhBdDk .

Penaloza et al. (2026) Emiliano Penaloza, Dheeraj Vattikonda, Nicolas Gontier, Alexandre Lacoste, Laurent Charlin, and Massimo Caccia. Privileged information distillation for language models, 2026. URL https://arxiv.org/abs/2602.04942 .

Shao et al. (2024) Zhihong Shao, Peiyi Wang, Qihao Zhu, Runxin Xu, Junxiao Song, Xiao Bi, Haowei Zhang, Mingchuan Zhang, YK Li, Yang Wu, et al. Deepseekmath: Pushing the limits of mathematical reasoning in open language models. arXiv preprint arXiv:2402.03300 , 2024.

Shenfeld et al. (2026) Idan Shenfeld, Mehul Damani, Jonas Hübotter, and Pulkit Agrawal. Self-distillation enables continual learning, 2026. URL https://arxiv.org/abs/2601.19897 .

Song & Zheng (2026) Mingyang Song and Mao Zheng. A survey of on-policy distillation for large language models, 2026. URL https://arxiv.org/abs/2604.00626 .

Song et al. (2026) Xiaoshuai Song, Haofei Chang, Guanting Dong, Yutao Zhu, Ji-Rong Wen, and Zhicheng Dou. Envscaler: Scaling tool-interactive environments for llm agent via programmatic synthesis, 2026. URL https://arxiv.org/abs/2601.05808 .

TogetherAI (2025) TogetherAI. DeepCoder: A Fully Open-Source 14B Coder at O3-mini Level — together.ai. https://www.together.ai/blog/deepcoder , 2025.

Wang et al. (2026) Hao Wang, Guozhi Wang, Han Xiao, Yufeng Zhou, Yue Pan, Jichao Wang, Ke Xu, Yafei Wen, Xiaohu Ruan, Xiaoxin Chen, and Honggang Qi. Skill-sd: Skill-conditioned self-distillation for multi-turn llm agents, 2026. URL https://arxiv.org/abs/2604.10674 .

Wang et al. (2024) Yu Wang, Yifan Gao, Xiusi Chen, Haoming Jiang, Shiyang Li, Jingfeng Yang, Qingyu Yin, Zheng Li, Xian Li, Bing Yin, Jingbo Shang, and Julian McAuley. Memoryllm: Towards self-updatable large language models, 2024. URL https://arxiv.org/abs/2402.04624 .

Wu et al. (2026a) Yecheng Wu, Song Han, and Han Cai. Lightning OPD: Efficient Post-Training for Large Reasoning Models with Offline On-Policy Distillation. arXiv preprint arXiv:2604.13010 , 2026a. URL https://arxiv.org/abs/2604.13010 .

Wu et al. (2026b) Zijun Wu, Yongchang Hao, and Lili Mou. Tokmem: One-token procedural memory for large language models, 2026b. URL https://arxiv.org/abs/2510.00444 .

Yang et al. (2025) An Yang, Anfeng Li, Baosong Yang, Beichen Zhang, Binyuan Hui, Bo Zheng, Bowen Yu, Chang Gao, Chengen Huang, Chenxu Lv, et al. Qwen3 technical report. arXiv preprint arXiv:2505.09388 , 2025.

Yang et al. (2026) Chenxu Yang, Chuanyu Qin, Qingyi Si, Minghui Chen, Naibin Gu, Dingyu Yao, Zheng Lin, Weiping Wang, Jiaqi Wang, and Nan Duan. Self-distilled rlvr, 2026. URL https://arxiv.org/abs/2604.03128 .

Ye et al. (2026) Tianzhu Ye, Li Dong, Xun Wu, Shaohan Huang, and Furu Wei. On-policy context distillation for language models, 2026. URL https://arxiv.org/abs/2602.12275 .

Yu et al. (2026a) Weichen Yu, Xiaomin Li, Yizhou Zhao, Xiaoze Liu, Ruowang Zhang, Haixin Wang, Yinyi Luo, Chen Henry Wu, Gaurav Mittal, Matt Fredrikson, and Yu Hu. Multi-Rollout On-Policy Distillation via Peer Successes and Failures. arXiv preprint arXiv:2605.12652 , 2026a. URL https://arxiv.org/abs/2605.12652 .

Yu et al. (2026b) Xinlei Yu, Zhangquan Chen, Yongbo He, Tianyu Fu, Guanting Dong, Cheng Yang, Chengming Xu, Yue Ma, Xiaobin Hu, Zhe Cao, Jie Xu, Guibin Zhang, Jiale Tao, Jiayi Zhang, Siyuan Ma, Kaituo Feng, Haojie Huang, Youxing Li, Ronghao Chen, Huacan Wang, Chenglin Wu, Zikun Su, Xiaogang Xu, Kelu Yao, Kun Wang, Chen Gao, Yue Liao, Ruqi Huang, Tao Jin, Zhucun Xue, Cheng Tan, Jiangning Zhang, Wenqi Ren, Yanwei Fu, Yong Liu, Yu Wang, Xiangyu Yue, Yu-Gang Jiang, and Shuicheng Yan. The latent space: Foundation, evolution, mechanism, ability, and outlook, 2026b. URL https://arxiv.org/abs/2604.02029 .

Yu et al. (2026c) Xinlei Yu, Gen Li, Qingyi Si, Guibin Zhang, Yuqi Xu, Congcong Wang, Shuai Dong, Kaiwen Tuo, Xiangyu Zeng, Kaituo Feng, et al. Dopd: Dual on-policy distillation. arXiv preprint arXiv:2606.30626 , 2026c.

Yu et al. (2026d) Xinlei Yu, Chengming Xu, Guibin Zhang, Zhangquan Chen, Yudong Zhang, Yongbo He, Peng-Tao Jiang, Jiangning Zhang, Xiaobin Hu, and Shuicheng Yan. Vismem: Latent vision memory unlocks potential of vision-language models, 2026d. URL https://arxiv.org/abs/2511.11007 .

Yuan et al. (2026) Qianhao Yuan, Jie Lou, Xing Yu, Hongyu Lin, Le Sun, Xianpei Han, and Yaojie Lu. Vision-OPD: Learning to See Fine Details for Multimodal LLMs via On-Policy Self-Distillation. arXiv preprint arXiv:2605.18740 , 2026. URL https://arxiv.org/abs/2605.18740 .

Zhang et al. (2025) Guibin Zhang, Muxin Fu, and Shuicheng Yan. Memgen: Weaving generative latent memory for self-evolving agents, 2025. URL https://arxiv.org/abs/2509.24704 .

Zhang et al. (2026a) Xinsen Zhang, Zhenkai Ding, Tianjun Pan, Run Yang, Chun Kang, Xue Xiong, and Jingnan Gu. OPSDL: On-Policy Self-Distillation for Long-Context Language Models. arXiv preprint arXiv:2604.17535 , 2026a. URL https://arxiv.org/abs/2604.17535 .

Zhang et al. (2026b) Yan Zhang, Daiqing Wu, Huawen Shen, Yu Zhou, and Can Ma. Learn where to Click from Yourself: On-Policy Self-Distillation for GUI Grounding. arXiv preprint arXiv:2605.00642 , 2026b. URL https://arxiv.org/abs/2605.00642 .

Zhang et al. (2026c) Yuwei Zhang, Sha Li, Changlong Yu, Qin Lu, Shuowei Jin, Chengyu Dong, Haoran Liu, Ilgee Hong, Xintong Li, Zhenyu Shi, Bing Yin, and Jingbo Shang. Learning with Rare Success but Rich Feedback via Reflection-Enhanced Self-Distillation. arXiv preprint arXiv:2605.12741 , 2026c. URL https://arxiv.org/abs/2605.12741 .

Zhao et al. (2026) Siyan Zhao, Zhihui Xie, Mengchen Liu, Jing Huang, Guan Pang, Feiyu Chen, and Aditya Grover. Self-distilled reasoner: On-policy self-distillation for large language models, 2026. URL https://arxiv.org/abs/2601.18734 .

Zhu et al. (2025) Rui-Jie Zhu, Tianhao Peng, Tianhao Cheng, Xingwei Qu, Jinfa Huang, Dawei Zhu, Hao Wang, Kaiwen Xue, Xuanliang Zhang, Yong Shan, Tianle Cai, Taylor Kergan, Assel Kembay, Andrew Smith, Chenghua Lin, Binh Nguyen, Yuqi Pan, Yuhong Chou, Zefan Cai, Zhenhe Wu, Yongchi Zhao, Tianyu Liu, Jian Yang, Wangchunshu Zhou, Chujie Zheng, Chongxuan Li, Yuyin Zhou, Zhoujun Li, Zhaoxiang Zhang, Jiaheng Liu, Ge Zhang, Wenhao Huang, and Jason Eshraghian. A survey on latent reasoning, 2025. URL https://arxiv.org/abs/2507.06203 .

## Appendix A Implementation Details

### A.1 Composer Architecture

The latent composer Φ ϕ \Phi_{\phi} consists of an encoder Enc ψ \operatorname{Enc}_{\psi} and a compressor Comp χ \operatorname{Comp}_{\chi} , with ϕ ≔ ( ψ , χ ) \phi\coloneqq(\psi,\chi) . The encoder uses the frozen backbone augmented with a trainable LoRA adapter (rank 8 8 , α = 16 \alpha{=}16 , dropout 0 0 , applied to all seven linear projections per transformer block: 𝐖 q \mathbf{W}_{q} , 𝐖 k \mathbf{W}_{k} , 𝐖 v \mathbf{W}_{v} , 𝐖 o \mathbf{W}_{o} , gate, up, and down projections). During encoding, the task description is prepended to each retrieved experience to enable task-conditional compression, so that the QFormer’s cross-attention can condition on the current task when compressing the experience (see Section A.5 for the exact format).

The compressor is a QFormer-style perceiver where learned queries cross-attend to the encoder’s hidden states. It has 8 8 cross-attention layers with shared parameters (i.e., all layers reuse the same weights), attention heads and hidden dimension inherited from the backbone model, and a feed-forward multiplier of 4 4 . Learned queries 𝐐 χ ∈ ℝ K × d \mathbf{Q}_{\chi}\in\mathbb{R}^{K\times d} are initialized from 𝒩 ⁡ ( 0 , 1 / d ) \mathcal{N}(0,1/\sqrt{d}) . The compressor operates independently on each retrieved experience, producing K K latent tokens per item; the outputs are concatenated to form the full latent context 𝒄 ϕ \bm{c}_{\phi} . Based on the sensitivity analysis in Section 4.3 , we set K = 32 K{=}32 tokens per retrieved experience for the final LOPD training runs. The encoder LoRA and QFormer are updated during both cold-start and joint optimization; the backbone weights remain frozen throughout.

### A.2 Cold-Start Initialization

The composer is cold-started by supervised finetuning on retrieved-experience–trajectory pairs with frozen backbone. The training objective is next-token NLL on assistant tokens with latent-augmented input: ℒ init ​ ( ϕ ) = − 𝔼 ( x , 𝒚 ⋆ ) ∼ 𝒟 exp , ℰ = Ret ⁡ ( x ) ​ [ log ⁡ π θ ¯ ​ ( 𝒚 ⋆ ∣ 𝒔 , 𝒄 ϕ ​ ( x , ℰ ) ) ] , \mathcal{L}_{\mathrm{init}}(\phi)=-\mathbb{E}_{(x,\bm{y}^{\star})\sim\mathcal{D}_{\mathrm{exp}},\;\mathcal{E}=\operatorname{Ret}(x)}\!\left[\log\pi_{\bar{\theta}}\!\left(\bm{y}^{\star}\mid\bm{s},\bm{c}_{\phi}(x,\mathcal{E})\right)\right], (14) where 𝒚 ⋆ \bm{y}^{\star} is a successful trajectory and θ ¯ \bar{\theta} denotes the frozen backbone. Concretely, the composer first produces latent tokens 𝒄 ϕ \bm{c}_{\phi} from retrieved experiences and inserts them into the input embedding sequence at designated placeholder positions. The frozen backbone then performs a standard forward pass over this latent-augmented input. Although the backbone parameters receive no gradient updates, the loss gradient flows backward through the frozen layers’ activations to the latent token positions, and from there to the QFormer and LoRA parameters—the same mechanism as prefix-tuning.

The training data is synthesized from the base model’s own rollouts—no external expert or stronger model is required—and filtered by task success. The data volume and number of training steps are adjusted per domain. Training uses AdamW with learning rate 10 − 5 10^{-5} , batch size 8 8 , gradient clipping 3.0 3.0 , task-conditional compression, and n ret = 3 n_{\mathrm{ret}}{=}3 retrieved experiences per task. The LoRA adapter and QFormer are updated during cold-start and remain trainable during subsequent joint optimization; the backbone remains frozen.

### A.3 Retrieval Configuration

Let ℬ = { ( x i , 𝝉 i ) } i = 1 | ℬ | \mathcal{B}=\{(x_{i},\bm{\tau}_{i})\}_{i=1}^{|\mathcal{B}|} denote the experience bank, where each entry pairs a task description x i x_{i} with a successful trajectory 𝝉 i \bm{\tau}_{i} . A dense encoder f ret f_{\mathrm{ret}} maps text to a unit-norm embedding. We adopt asymmetric encoding: document-side embeddings encode the concatenation of task description and trajectory, while query-side embeddings encode only the task description with an instruction-aware query prompt: 𝒛 i doc = f ret ​ ( [ x i ; 𝝉 i ] ) ‖ f ret ​ ( [ x i ; 𝝉 i ] ) ‖ 2 , 𝒛 q = f ret query ​ ( x ) ‖ f ret query ​ ( x ) ‖ 2 , 𝒛 i doc , 𝒛 q ∈ ℝ d ret . \bm{z}_{i}^{\mathrm{doc}}=\frac{f_{\mathrm{ret}}([x_{i};\bm{\tau}_{i}])}{\|f_{\mathrm{ret}}([x_{i};\bm{\tau}_{i}])\|_{2}},\qquad\bm{z}_{q}=\frac{f_{\mathrm{ret}}^{\mathrm{query}}(x)}{\|f_{\mathrm{ret}}^{\mathrm{query}}(x)\|_{2}},\qquad\bm{z}_{i}^{\mathrm{doc}},\,\bm{z}_{q}\in\mathbb{R}^{d_{\mathrm{ret}}}. (15) Given a query task x x , retrieval returns the n ret n_{\mathrm{ret}} entries with the highest cosine similarity: Ret ⁡ ( x ) = top ​ - ​ n ret ⁡ { ( x i , 𝝉 i ) ∈ ℬ | 𝒛 q ⊤ ​ 𝒛 i doc } . \operatorname{Ret}(x)=\operatorname{top\text{-}n_{\mathrm{ret}}}\left\{(x_{i},\bm{\tau}_{i})\in\mathcal{B}\;\middle|\;{\bm{z}_{q}}^{\top}\bm{z}_{i}^{\mathrm{doc}}\right\}. (16) We use Qwen3-Embedding-8B as f ret f_{\mathrm{ret}} , producing d ret = 4,096 d_{\mathrm{ret}}{=}4{,}096 -dimensional embeddings. The index is implemented as a FAISS IndexFlatIP for exact inner-product search over the precomputed document embeddings. The bank ℬ \mathcal{B} is constructed offline exclusively from successful rollouts generated on the training split: agentic trajectories must exceed a task-reward threshold, while coding trajectories must pass all test cases. No evaluation task, trajectory, or outcome is ever inserted into the bank, and the bank is frozen before evaluation. Consequently, LOPD receives neither evaluation-set information nor an additional task corpus; it uses only experience produced from the same training-task split available to the baselines. Trajectories are stored in an observation-lite format that omits verbose environment observations to reduce storage and encoding length. All query embeddings 𝒛 q \bm{z}_{q} are precomputed and cached per task, so the retriever does not need to be loaded during training or evaluation.

Each bank entry stores the task description followed by a linearized action–result trace in observation-lite format, as illustrated below:

### A.4 Latent Injection Mechanism

The latent tokens produced by the composer must be injected into the backbone’s input in a way compatible with the inference engine’s pipeline. Unlike prior latent-state injection work that typically relies on HuggingFace Transformers or TRL for direct inputs_embeds manipulation, our implementation operates on top of production inference engines (SGLang and vLLM).

#### Placeholder strategy.

A text-level sentinel string <|LATENT_PH|> is inserted into the first user message of the chat template, sandwiched between natural-language framing text (e.g., “ The following is a reference example… ” before and “ Now complete your task… ” after). The full prompt is then rendered via the tokenizer’s chat template and split on the sentinel. Each half is tokenized independently, and J ⋅ K J\cdot K dummy token IDs (using the tokenizer’s pad token) are inserted between them: input ​ _ ​ ids = [ t 1 , … , t a ⏟ before , t pad , … , t pad ⏟ J ⋅ K ​ placeholders , t a + 1 , … , t L ⏟ after ] . \mathrm{input\_ids}=[\,\underbrace{t_{1},\ldots,t_{a}}_{\text{before}},\;\underbrace{t_{\mathrm{pad}},\ldots,t_{\mathrm{pad}}}_{J\cdot K\text{ placeholders}},\;\underbrace{t_{a+1},\ldots,t_{L}}_{\text{after}}\,]. (17) This produces a contiguous span of placeholder positions at known absolute indices, without any tokenizer modification.

#### Embedding replacement.

The engine embeds the full input_ids as usual, producing 𝐗 ∈ ℝ L × d \mathbf{X}\in\mathbb{R}^{L\times d} . Before the first transformer layer, the placeholder embeddings are replaced with the latent tokens from the composer: 𝐗 [ p k ] ← ⟨ e k ⟩ , k = 1 , … , J ⋅ K . \mathbf{X}[p_{k}]\leftarrow\langle e_{k}\rangle,\quad k=1,\ldots,J\cdot K. (18) The replacement uses torch.cat over slices (rather than in-place assignment) so that autograd can track gradients through ⟨ e k ⟩ \langle e_{k}\rangle back to the composer parameters during training. The modified embedding tensor is then passed through the backbone’s transformer layers without any architectural change; the operation is transparent to the engine’s KV-cache, attention mask, and batching logic.

#### Engine-specific implementations.

SGLang provides a positional_embed_overrides interface that accepts embeddings at specified absolute positions and performs the replacement in-GPU. vLLM provides a prompt_embeds interface: the full sequence is first embedded on CPU via a frozen copy of the embedding table, the latent positions are overwritten with the composer’s output, and the complete embedding tensor is submitted to the engine. In both cases, the backbone model is unmodified.

#### Equivalence verification.

To confirm that the placeholder-based injection introduces no numerical artifacts, we replaced the latent span with known token embeddings from the vocabulary and compared the token-ID input path against the embedding-tensor input path. The two paths produce identical greedy-decoded sequences with negligible log-probability differences, verifying that latent injection is numerically equivalent to standard token-ID forwarding.

#### Encoder LoRA isolation.

The encoder Enc ψ \operatorname{Enc}_{\psi} uses a LoRA adapter to specialize hidden-state extraction for experience compression. This adapter is explicitly disabled during the main forward pass (both at inference and during teacher evaluation in training), so that the model behaves as a pure base actor conditioned on the injected latent context. This dual-use pattern—LoRA active for encoding, inactive for generation—avoids interference between the two roles.

### A.5 Prompt and Interaction Format

#### Agentic system prompt.

For tool-use tasks (EnvScaler, ACEBench), the agent receives a system prompt instructing it to complete tasks via step-by-step tool invocation:

#### Coding system prompt.

For TACO and LiveCodeBench, the model receives a minimal system instruction:

HumanEval+ and MBPP+ use no system prompt, following the official EvalPlus evaluation protocol. All coding benchmarks use Python as the target language.

#### Latent-context framing text.

The latent privileged context is injected into the first user message, wrapped by domain-specific framing text. The framing instructs the model to treat the injected content as a reference from a different task, not as instructions to follow verbatim.

The latent tokens produced by the composer replace the framing’s interior (as described in Section A.4 ).

#### Encoder input format.

When the encoder Enc ψ \operatorname{Enc}_{\psi} processes a retrieved experience for compression, the input is formatted as “ Task to solve: \n x x \n\nReference past trajectory: \n m j m_{j} ”, where x x is the current task description and m j m_{j} is the retrieved trajectory. This task-conditional formatting allows the QFormer to attend to task-relevant features when producing the latent tokens.

## Appendix B Experiment Details

### B.1 Baseline Setup

All trainable methods share the same base model, training task distribution, on-policy rollout budget ( 32 32 rollouts per step), optimizer (AdamW, learning rate 10 − 5 10^{-5} , gradient clipping 1.0 1.0 ), and evaluation protocol. Each distillation-based method uses the KL direction prescribed by its original paper: OPSD and SDFT use forward KL over the full vocabulary, SDPO uses reverse KL with top- K K truncation and a tail bucket, and Skill-SD uses sampled-token reverse KL with importance weighting. SDFT and OPSD require ground-truth demonstrations as privileged context for the teacher. These are drawn from a shared pool of verified-successful trajectories: for agentic tasks, trajectories must exceed a reward threshold; for coding tasks, solutions must pass all test cases. The pool is first populated from the base model’s own rollouts; when its coverage is insufficient, we synthesize additional ground-truth trajectories by querying stronger models (DeepSeek-V4-Pro and Qwen3.7-Max in our experiments). Below we describe the method-specific configurations.

#### Vanilla.

The unadapted backbone model, evaluated without any post-training.

#### GRPO.

Standard group relative policy optimization ( Shao et al., 2024 ) . Each step samples G = 4 G{=}4 rollouts per task with stochastic decoding; group-normalized advantages weight a PPO-clip objective with ϵ lo = ϵ hi = 0.2 \epsilon_{\mathrm{lo}}{=}\epsilon_{\mathrm{hi}}{=}0.2 . No teacher or privileged context is used; the training signal comes entirely from environment rewards.

#### SDFT.

Demonstration-conditioned distillation ( Shenfeld et al., 2026 ) . The teacher receives oracle trajectories from the shared pool as textual in-context demonstrations appended to the first user message. The teacher is an EMA shadow of the student ( α EMA = 0.01 \alpha_{\mathrm{EMA}}{=}0.01 , synced every step). The distillation loss is forward KL over the full vocabulary, following the official implementation.

#### OPSD.

On-policy self-distillation ( Zhao et al., 2026 ) . The teacher receives oracle trajectories from the shared pool directly as privileged context in the system message. The teacher is frozen throughout training. The distillation loss is forward KL over the full vocabulary, as prescribed by the original paper.

#### SDPO.

Self-distillation policy optimization ( Hübotter et al., 2026 ) . The teacher is an EMA shadow of the student (update rate 0.05 0.05 ), conditioned on successful sibling trajectories sampled within the same training step ( G = 4 G{=}4 rollouts per task). Unlike SDFT and OPSD, SDPO does not use an external trajectory pool; it filters from its own rollouts using the same domain-specific success criterion (reward threshold for agentic tasks, full test-case pass for coding tasks).

#### Skill-SD.

Skill-conditioned self-distillation ( Wang et al., 2026 ) . Each task selects one skill from a skill bank via UCB1 ( c = 2 c{=}\sqrt{2} ). Skills are distilled from rollout trajectories into structured summaries and injected into the teacher’s first user message:

The loss combines PPO-clip ( ϵ lo = 0.2 \epsilon_{\mathrm{lo}}{=}0.2 , ϵ hi = 0.28 \epsilon_{\mathrm{hi}}{=}0.28 ) with importance-weighted sampled-token reverse KL ( λ sdl = 0.001 \lambda_{\mathrm{sdl}}{=}0.001 ), following the original paper.

### B.2 Training Data and Domain Setup

All methods are trained exclusively on the two datasets listed in Table 4 ; no additional task dataset is used. In particular, the LOPD experience bank contains only rollouts from the corresponding training split and excludes every evaluation task and trajectory. The agentic training corpus (EnvScaler) covers diverse tool-interactive scenarios including insurance, logistics, e-commerce, and healthcare, with each task requiring multi-turn API interactions to complete. The coding training corpus (TACO subset of DeepCoder) consists of competitive programming problems with verified test cases, spanning algorithmic topics such as dynamic programming, graph traversal, and string manipulation. The environment reward differs by domain: EnvScaler returns a continuous reward in [ 0 , 1 ] [0,1] reflecting the fraction of subtasks completed, while TACO returns a binary reward ( 1 1 if all test cases pass, 0 0 otherwise).

### B.3 Evaluation Protocols

Table 5 summarizes the inference configuration for each benchmark. All benchmarks use thinking mode enabled.

#### EnvScaler.

We evaluate on a held-out set of 200 200 tasks, randomly sampled from the full task pool and fully disjoint from the training split.

#### BFCL-v3.

We use the official Berkeley Function Calling Leaderboard V3 codebase with four multi-turn subsets: base, missing-function, missing-parameter, and long-context. Models are served in function-calling (FC) mode. We report per-subset and average scores.

#### ACEBench.

ACEBench evaluates 50 50 tasks split into multi-step ( 20 20 ) and multi-turn ( 30 30 ) categories. A user simulator ( deepseek-v4-flash via API) drives the multi-turn dialogues.

#### LiveCodeBench.

We use the official code_generation_lite evaluation harness and report pass@1 on release v5 ( 279 279 tasks, Aug 2024–Feb 2025) and release v6 ( 131 131 tasks, Feb–May 2025).

#### EvalPlus.

We use HumanEval+ v0.1.10 ( 164 164 tasks) and MBPP+ v0.2.0 ( 378 378 tasks) from the official EvalPlus codebase.

### B.4 Ablation and Analysis Setup

This section details the configuration of each analysis experiment in Section 4.3 .

#### Effect of Joint Optimization ( Figure 3 ).

Each row trains LOPD with a different margin m m and evaluates the resulting student on the EnvScaler test set without retrieval, the composer, or latent privileged context at inference, isolating the effect of joint optimization on the resulting policy. The “Frozen ϕ 0 \phi_{0} ” row trains with a frozen composer (no joint optimization). All jointly-optimized rows share the same training configuration except for m m .

#### Training Dynamics ( Figure 4 ).

Mean reward is periodically evaluated on the EnvScaler test set throughout training using Qwen3-4B .

#### Sensitivity Analysis ( Figure 5 ).

(a) Latent-token capacity : we train separate LOPD variants with K ∈ { 8 , 16 , 32 , 64 , 128 } K\in\{8,16,32,64,128\} and evaluate each resulting student alone on the EnvScaler test set ( n ret = 3 n_{\mathrm{ret}}{=}3 during training). (b–e) Retrieval count : we train separate LOPD variants with K = 32 K{=}32 , m = 0.05 m{=}0.05 , and n ret ∈ { 1 , … , 10 } n_{\mathrm{ret}}\in\{1,\ldots,10\} , then evaluate the resulting students on the EnvScaler test set and ACEBench without retrieval, the composer, or latent privileged context.

#### Behavioral Internalization ( Table 3 ).

Vanilla : the unadapted Qwen3-4B backbone. Base + Composer : the jointly optimized composer ( m = 0.05 m{=}0.05 ) paired with the unadapted backbone and latent privileged context ( n ret = 3 n_{\mathrm{ret}}{=}3 , K = 32 K{=}32 ). LOPD : the distilled student policy evaluated without retrieval, the composer, or latent privileged context. All three are evaluated on the EnvScaler test set with otherwise identical inference settings.

## Instructions for reporting errors

We are continuing to improve HTML versions of papers, and your feedback helps enhance accessibility and mobile support. To report errors in the HTML that will help us improve conversion and rendering, choose any of the methods listed below:

Click the "Report Issue" ( ) button, located in the page header.

Tip: You can select the relevant text first, to include it in your report.

Our team has already identified the following issues . We appreciate your time reviewing and reporting rendering errors we may not have found yet. Your efforts will help us improve the HTML versions for all readers, because disability should not be a barrier to accessing research. Thank you for your continued support in championing open access for all.

Have a free development cycle? Help support accessibility at arXiv! Our collaborators at LaTeXML maintain a list of packages that need conversion , and welcome developer contributions .
