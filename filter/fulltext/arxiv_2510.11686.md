##### Report GitHub Issue

Content selection saved. Describe the issue below:

\declaretheorem [name=Theorem,parent=section]theorem \declaretheorem [name=Lemma,parent=section]lemma \declaretheorem [name=Assumption, parent=section]assumption \declaretheorem [name=Definition, parent=section]definition \declaretheorem [name=Condition, parent=section]condition \declaretheorem [name=Corollary, parent=section]corollary \declaretheorem [name=Claim, parent=section]claim \declaretheorem [qed= ⊲ \triangleleft ,name=Example,style=definition, parent=section]example \declaretheorem [name=Remark, parent=section]remark \declaretheorem [name=Proposition, parent=section]proposition \declaretheorem [name=Fact, parent=section]fact

# Representation-Based Exploration for Language Models: From Test-Time to Post-Training

###### Abstract

Reinforcement learning (RL) promises to expand the capabilities of language models, but it is unclear if current RL techniques promote the discovery of novel behaviors, or simply sharpen those already present in the base model. In this paper, we investigate the value of deliberate exploration—explicitly incentivizing the model to discover novel and diverse behaviors—and aim to understand how the knowledge in pre-trained models can guide this search. Our main finding is that exploration with a simple, principled, representation-based bonus derived from the pre-trained language model’s hidden states significantly improves diversity and pass@k rates—both for post-training, and in a novel inference-time scaling setting we introduce.

1. For inference-time, exploration with representation-based diversity improves efficiency, consistently improving pass@k rates across a variety of models and reasoning tasks. For example, for Qwen-2.5-14b-Instruct we obtain over 50% improvement in verifier efficiency on almost all tasks.

2. For post-training, we show that integrating this exploration strategy into an RL pipeline improves reasoning performance over that of the initial model and over standard RL post-training. For example, on AIME 2024 , our post-trained Qwen-2.5-7b-Instruct ’s pass@80 matches the pass@256 of GRPO on the same model, demonstrating a 3x improvement in test-time sample efficiency.

Overall, our findings suggest that deliberate exploration---with the right notion of diversity---is a practical path toward discovery of new behaviors beyond sharpening. 1 1 1 Website and code: https://rep-exp.github.io

## 1 Introduction

Reinforcement learning (RL) promises to endow agents with the ability to discover valuable behaviors autonomously, via closed-loop trial and error. For language modeling tasks with verifiable rewards, such as mathematical reasoning and code generation, post-training with reinforcement learning has already enabled impressive breakthroughs ( DeepSeek-AI, 2025 ; OpenAI, 2024 ) . Still, it is unclear whether contemporary RL implementations for language models attain the full promise of reinforcement learning. Rather than unlocking capabilities not present in the pre-trained model, there is increasing evidence ( Yue et al., 2025 ; Gandhi et al., 2025 ) that existing RL recipes ( Schulman et al., 2017 ; Rafailov et al., 2023 ; DeepSeek-AI, 2025 ) may simply amplify or sharpen ( Huang et al., 2025 ) behaviors that the base model can already execute, albeit with modest probability. While this can be mitigated through deliberate data curation and some algorithmic interventions ( He et al., 2025 ; Liu et al., 2025 ; Setlur et al., 2025 ) , data scale and quality are rapidly becoming bottlenecks, particularly in complex, open-ended domains where existing interventions fall short of eliciting desired behavior.

We argue that deliberate exploration—incentivizing the model to discover truly novel and diverse behavior—is an essential ingredient in realizing the full potential of RL for language model reasoning. Exploration has a rich history in both the theory and practice of RL, and exploration techniques tailored to deep networks ( Tang et al., 2017 ; Pathak et al., 2017 ; Burda et al., 2018 ; Osband et al., 2019 ) have received extensive investigation in the context of embodied decision making, including game playing and robotic control. These algorithms proceed from scratch, without pre-training, yet rapidly learn complex behaviors, demonstrating that they enable learning beyond the sharpening regime. If we can equip language models with exploration in a similar fashion, we may be able to advance reasoning capabilities without incurring exorbitant data curation costs.

In spite of the potential benefits of exploration, it is unclear which, if any, exploration technique from deep RL can be scaled to modern language models. A central challenge involves the scalable quantification of novelty and behavior diversity—and acting on this information—when the decision space under consideration is the combinatorially large space of language. At the same time, pre-trained language models contain tremendous prior knowledge compared to policies found in traditional embodied settings, which may be the key to guiding efficient exploration. This leads us to ask:

### 1.1 Contributions

Toward answering these questions, we focus on understanding whether exploration with diversity bonuses div ​ ( x , y ) \texttt{div}(x,y) derived from a language model can effectively guide the search for diverse behaviors. We adopt a novel methodology ( Section 2 ) in which we first evaluate exploration in a simple, purely inference-time setting, then integrate our findings into post-training.

The inference-time selection problem ( Section 2 ). In this setting, we aim to select a small set of responses y 1 , … , y k y_{1},\ldots,y_{k} from a large set of candidates y 1 , … , y N y_{1},\ldots,y_{N} for a given prompt x x , such that the chosen set is as diverse as possible, and has high probability of including a positive response. This simple regime allows us to disentangle the role of diversity div ​ ( x , y ) \texttt{div}(x,y) from other complex RL mechanisms, such as optimization and generalization.

Representation-based exploration improves diversity and efficiency. Our main finding is that exploration with a representation-based bonus ( Section 3 ) derived from the pre-trained language model’s hidden states significantly improves diversity and pass@k rates—both for our inference-time setting and for post-training. Our specific findings are as follows: 1. Inference-time ( Section 4 ). Inference-time exploration with representation-based diversity improves verifier efficiency. For example, we obtain over 50% improvement in verifier efficiency over standard sampling for Qwen-2.5-14b-Instruct on GSM8K , MATH , MBPP+ and Game-of-24 . See Fig. 1 for an overview of our results for this setting.

2. Post-training ( Section 5 ). Representation-based exploration can be incorporated into RL post-training, where its pass@ k k performance is competitive with both GRPO and the base model uniformly for all k k ( Fig. 2 ). Notably, representation-based exploration completely eliminates the “diversity collapse” phenomenon where RL degrades pass@ k k with respect to the base model for large k k ( Dang et al., 2025 ; Yue et al., 2025 ; Wu et al., 2025 ) . In addition, representation-based exploration induces responses that look much more novel under the base model ( Fig. 9 ).

Our findings, particularly these last two points, suggest that deliberate exploration is a practical path toward discovery of new behaviors beyond sharpening. Although our experiments focus on arguably the simplest principled representation-based exploration scheme—for which we already see substantial performance improvements—we expect that our two-pronged evaluation approach will enable a deeper understanding of the benefits and tradeoffs of more sophisticated strategies, which may help realize the full potential of reinforcement learning for language model reasoning.

#### Diversity-guided generation ( Section 4.2 )

As a proof of concept, we also evaluate an inference-time exploration algorithm that uses representation-based diversity to encourage exploration during the autoregressive generation process itself . We find that this improves pass@k for large k over naive sampling for Qwen-2.5-7b-Instruct on MATH .

## 2 Problem Setup: From Inference-Time to Post-Training

In this section, we describe the two problem settings we consider for exploration: inference-time selection and RL post-training. In what follows, π \pi denotes a language model that maps a prompt x ∈ 𝒳 x\in\mathcal{X} to a distribution over responses y ∈ 𝒴 y\in\mathcal{Y} , and r ⋆ ​ ( x , y ) ∈ { 0 , 1 } r^{\star}(x,y)\in\{0,1\} denotes a verifiable reward function that measures correctness at a task of interest, such as whether the answer to a math question is correct, or whether a Python program passes unit tests.

#### Methodology and motivation

The goal of RL post-training is to find a policy π \pi that maximizes the expected reward 𝔼 y ∼ π ( ⋅ ∣ x ) [ r ⋆ ( x , y ) ] \En_{y\sim\pi(\cdot\mid{}x)}\left[r^{\star}(x,y)\right] . Given a budget k k of verifier queries per question at each data collection round, post-training algorithms such as GRPO ( Shao et al., 2024 ) update the model iteratively, where in each iteration they sample k k responses y 1 , … , y k ∼ i.i.d. π ( ⋅ ∣ x ) y_{1},\ldots,y_{k}\overset{\textrm{i.i.d.}}{\sim}\pi(\cdot\mid{}x) per prompt x x from the current model π \pi , query the verifier for a reward r ⋆ ​ ( x , y i ) r^{\star}(x,y_{i}) for each response, and use observed rewards to update the model for the next iteration.

If the initial model π \pi has poor support over rewarding behavior—i.e., if r ⋆ ​ ( x , y ) = 0 r^{\star}(x,y)=0 , with high probability under y ∼ π ( ⋅ ∣ x ) y\sim\pi(\cdot\mid{}x) —common RL algorithms such GRPO or PPO ( Schulman et al., 2017 ) will not make any progress. This motivates interventions for exploration such as bonuses ( Tang et al., 2017 ; Pathak et al., 2017 ; Burda et al., 2018 ; Osband et al., 2019 ) and alternative sampling strategies ( Holtzman et al., 2020 ; Minh et al., 2025 ) . However, understanding the benefits and tradeoffs of these interventions in RL post-training is challenging because exploration interacts with optimization and generalization. To isolate exploration from these other considerations, we center our investigation around a task we refer to as inference-time selection , validating interventions in this setting before integrating them into the RL post-training pipeline.

### 2.1 Inference-time selection

In the inference-time selection problem, we aim to use a fixed model π \pi to build a set of k k responses to a given prompt x x that are maximally diverse and have high probability of containing a positive response. As a simple baseline, we may independently sample k k responses from the model—potentially with high-temperature sampling, nucleus or min-p sampling, or other modified sampling schemes. However, the limitations of these baselines are (i) they may not effectively capture the model’s understanding of diversity, and (ii) by sampling independently, we may waste verifier queries on redundant responses.

Instead, we focus on selection-based approaches that initially sample a large set of candidate responses to the prompt, then use a diversity bonus div ​ ( x , y ) \texttt{div}(x,y) derived from the model to filter this set down to a smaller, more diverse “coreset” ( Clarkson, 2010 ; Feldman et al., 2020 ) that is passed to the verifier. Formally, we consider the following protocol: For each prompt x x , we (1) sample an initial batch of N N responses y 1 , … , y N ∼ π ( ⋅ ∣ x ) y_{1},\ldots,y_{N}\sim\pi(\cdot\mid{}x) , (2) use the inference-time selection algorithm 𝙰𝚕𝚐 \mathtt{Alg} to select k k of these responses (a subset S ⊂ [ N ] S\subset[N] of size | S | = k |S|=k ), and (3) query the verifier and record if any of the selected responses are rewarding. That is, we measure pass@ k k , 𝔼 y 1 , … , y N ∼ π ( ⋅ ∣ x ) [ 𝔼 S ∼ 𝙰𝚕𝚐 ⁡ ( x , y 1 , … , y N ) [ max i ∈ S [ r ⋆ ( x , y i ) ] ] ] . \displaystyle\En_{y_{1},\ldots,y_{N}\sim\pi(\cdot\mid{}x)}\big[\En_{S\sim\mathtt{Alg}(x,y_{1},\ldots,y_{N})}\big[\max_{i\in S}[r^{\star}(x,y_{i})]\big]\big]. (1) Importantly, the filtering algorithm operates without the verifier, and so successfully retaining high-quality responses translates to improved verifier efficiency (i.e., number of responses for which we query the verifier) over the initial set of responses. Thus, a useful diversity bonus div ​ ( x , y ) \texttt{div}(x,y) should yield a coreset that is maximally “exploratory,” in the sense that it is the most diverse set of responses that can be selected for a fixed budget of verifier queries. For example, in math reasoning settings, we would like to select the distinct-but-plausible proof strategies for a given problem, thus covering the space of potential proofs and maximizing the chance of selecting a correct one.

{remark} While we mainly introduce inference-time selection as a stepping stone to post-training (i.e., algorithms in this setting are not more compute-efficient than naive sampling, even if they are more verifier-efficient), we do expect inference-time exploration to be useful in its own right for domains where querying a verifier is costly or difficult (e.g., collecting feedback from expert-level annotators), allowing for more sample- and hence cost-efficient data curation. For preliminary results in one such domain, please refer to Section 4.3 .

### 2.2 Reinforcement learning post-training

As described earlier, RL post-training (e.g., with GRPO or PPO) proceeds by iteratively sampling batches of responses, querying the verifier, and using the feedback to update the current policy. After selecting a checkpoint π ^ \hat{\pi} , we evaluate performance via pass@ k k under standard generation, 𝔼 y 1 , … , y k ∼ π ^ ( ⋅ ∣ x ) [ max i ∈ [ k ] r ⋆ ( x , y i ) ] \En_{y_{1},\ldots,y_{k}\sim\hat{\pi}(\cdot\mid{}x)}\big[\max_{i\in[k]}r^{\star}(x,y_{i})\big] . There are two natural approaches to integrate exploration methods into this process. The first is to adjust the independent sampling process only (e.g., through nucleus sampling or min-p sampling), and the second is to augment the training objective with an exploration bonus div ​ ( x , y ) \texttt{div}(x,y) . Our experiments focus on the latter approach; however, based on our results for inference-time selection, we expect that incorporating representation-based exploration into the sampling process will also improve RL post-training performance. Indeed, our two-pronged evaluation is motivated by the hypothesis that diversity bonuses div ​ ( x , y ) \texttt{div}(x,y) that perform well at inference-time also perform well in post-training.

## 3 Representation-Based Exploration: Inference-Time and RL

Having motivated our setup, we now turn to the question of what diversity bonuses div ​ ( x , y ) \texttt{div}(x,y) are suitable for exploration with language models. While many metrics have been proposed in the literature ( Tang et al., 2017 ; Pathak et al., 2017 ; Burda et al., 2018 ; Osband et al., 2019 ) , the challenge in adapting these techniques to language models is to simultaneously (i) capture the model’s understanding and (ii) allow for efficient computation at scale. For example, count-based exploration ( Tang et al., 2017 ) is simple, but unsuited to large decision spaces. On the other hand, approaches based on intrinsic curiosity ( Pathak et al., 2017 ) , random network distillation ( Burda et al., 2018 ) , and posterior sampling ( Osband et al., 2019 ) are better suited to large or continuous spaces, but require additional learning machinery (i.e., auxiliary networks), which introduces significant complexity when scaling to language models.

We focus our experiments on an exploration strategy that avoids these shortcomings: An adaptation of elliptic bonuses and sampling—a de facto standard for linear bandits and active learning ( Abbasi-Yadkori et al., 2011 ; Chu et al., 2011 ; Ash et al., 2021 ; Henaff et al., 2022 ; Saran et al., 2023 ; Foster et al., 2025 ) 2 2 2 Indeed, elliptical bonuses are ubiquitous in linear bandits and reinforcement learning, the simplest non-tabular RL setting, where they have strong provable guarantees. Beyond this, elliptic bonuses and iterative schemes such as Algorithm 1 have a long history in the theory of optimal experimental design ( Kiefer and Wolfowitz, 1960 ; Pukelsheim, 2006 ; Allen-Zhu et al., 2021 ) and active learning ( Cesa-Bianchi et al., 2009 ; Agarwal, 2013 ; Gu et al., 2014 ; Chaudhuri et al., 2015 ) —with a representation derived from the language model’s hidden states. This approach is arguably the simplest principled strategy that is appropriate for language models, and already yields significant performance improvements in our experiments. Our use of elliptic bonuses is particularly inspired by Foster et al. (2025) , who prove that test-time exploration with such bonuses has provable computational benefits in a simplified language model setting with frozen features.

At a high level, elliptical bonus methods operate over a d d -dimensional feature space and adopt a linear-algebraic measure of novelty: given previously seen feature vectors h 1 , … , h i − 1 h_{1},\ldots,h_{i-1} the novelty (or bonus) of a new feature vector h h is defined as div ( h ∣ h 1 : i − 1 ) = h ⊤ Σ i − 1 h Σ i = λ I d + ∑ j < i h j h j ⊤ \displaystyle\texttt{div}(h\mid{}h_{1:i-1})=h^{\top}\Sigma_{i}^{-1}h\qquad\Sigma_{i}=\lambda I_{d}+\sum_{j<i}h_{j}h_{j}^{\top} (2)

These bonuses are grounded in the theory of linear regression: If we fit a linear model f θ ​ ( h ) = ⟨ θ , h ⟩ f_{\theta}(h)=\langle\theta,h\rangle on features h 1 , … , h i − 1 h_{1},\ldots,h_{i-1} (with associated regression targets), the prediction error on h h will be bounded by div ( h ∣ h 1 : i − 1 ) \texttt{div}(h\mid{}h_{1:i-1}) ( Lattimore and Szepesvári, 2020 ) . Thus, div ( h ∣ h 1 : i − 1 ) \texttt{div}(h\mid{}h_{1:i-1}) reflects novelty, as it will be large for features h h that are poorly represented by the training dataset.

To adapt elliptical bonuses to language models, we use representations extracted from the model itself as the feature vectors. Formally, given a prompt x x and a response y i = y i 1 , … , y i T y_{i}=y_{i}^{1},\ldots,y_{i}^{T} of T T tokens, we form the feature vector as h ¯ θ ( x , y i ) := 1 T ∑ t = 1 T h θ ( x , y i 1 : t ) \bar{h}_{\theta}(x,y_{i}):=\frac{1}{T}\sum_{t=1}^{T}h_{\theta}(x,y_{i}^{1:t}) where h θ ( x , y i 1 : t ) ∈ ℝ d h_{\theta}(x,y_{i}^{1:t})\in\mathbb{R}^{d} is the last-layer hidden state of the model on input ( x , y i 1 : t ) (x,y_{i}^{1:t}) (the activation prior to the unembedding matrix). In Fig. 4 , we ablate this choice by comparing it to the effectiveness of using representations at the last token h θ ( x , y i 1 : T ) h_{\theta}(x,y_{i}^{1:T}) or penultimate token h θ ( x , y i 1 : T − 1 ) h_{\theta}(x,y_{i}^{1:{T-1}}) instead. We reduce dimensionality to 512 using a sparse random projection ( Li et al., 2006 ) ; see Appendix B for details.

#### Representation-based exploration for inference-time selection

Fig. 3 presents RepExp , our main algorithm for inference-time selection using representation-based elliptical bonuses. Here, given a single prompt x x and a set of candidate generations 𝒴 = { y 1 , … , y N } \mathcal{Y}=\left\{y_{1},\ldots,y_{N}\right\} , we iteratively select the generation that maximizes the elliptical bonus via y t + 1 = arg ​ max y ∈ 𝒴 ⁡ h ¯ θ ​ ( x , y ) ​ Σ t − 1 ​ h ¯ θ ​ ( x , y ) y_{t+1}=\argmax_{y\in\mathcal{Y}}\bar{h}_{\theta}(x,y)\Sigma_{t}^{-1}\bar{h}_{\theta}(x,y) , leveraging the representations h ¯ θ ​ ( x , y ) \bar{h}_{\theta}(x,y) described above. We efficiently update the inverse covariance matrix Σ − 1 \Sigma^{-1} using the Woodbury identity for O ⁡ ( d 2 ) O(d^{2}) time per step ( Vetterling and Press, 1992 ) . We formally present our procedure in Algorithm 1 .

Algorithm 1 RepExp 1: input: Embeddings h ¯ θ \bar{h}_{\theta} (abbrv. h ¯ \bar{h} ) , generations 𝒴 \mathcal{Y} for prompt x x , budget k k , regularization param. λ \lambda . 2: Initialize L ← { y 1 } , y 1 ∼ Unif ​ ( 𝒴 ) L\leftarrow\{y_{1}\},y_{1}\sim\text{Unif}(\mathcal{Y}) . 3: Initialize inverse covariance Λ 0 = λ − 1 ​ I d \Lambda_{0}=\lambda^{-1}I_{d} . 4: for t = 1 t=1 to k − 1 k-1 do 5: Λ t ← Λ t − 1 − Λ t − 1 ​ h ¯ ​ ( x , y t ) ​ h ¯ ​ ( x , y t ) ⊤ ​ Λ t − 1 1 + h ¯ ​ ( x , y t ) ⊤ ​ Λ t − 1 ​ h ¯ ​ ( x , y t ) \Lambda_{t}\leftarrow\Lambda_{t-1}-\frac{\Lambda_{t-1}\bar{h}(x,y_{t})\bar{h}(x,y_{t})^{\top}\Lambda_{t-1}}{1+\bar{h}(x,y_{t})^{\top}\Lambda_{t-1}\bar{h}(x,y_{t})} . 6: y t + 1 = argmax y ∈ 𝒴 h ¯ ​ ( x , y ) ⊤ ​ Λ t ​ h ¯ ​ ( x , y ) y_{t+1}=\operatorname*{argmax}\limits_{y\in\mathcal{Y}}\bar{h}(x,y)^{\top}\,\Lambda_{t}\,\bar{h}(x,y) . 7: L ← L ∪ { y t + 1 } L\leftarrow L\cup\{y_{t+1}\} . 8: return: L L . Figure 4: Representation ablation. We compare averaging all token representations to using those from the penultimate or final token. Averaging is over 2x more sample efficient.

#### Representation-based exploration for RL post-training

For our post-training experiments, we use the same representations h ¯ θ ​ ( x , y ) \bar{h}_{\theta}(x,y) as above, but directly augment the rewards with elliptic bonuses instead of performing coreset selection. Concretely, given the current iterate π θ \pi_{\theta} in GRPO, we first sample a group of k k responses y 1 , … , y k ∼ i.i.d. π θ ( ⋅ ∣ x ) y_{1},\ldots,y_{k}\overset{\textrm{i.i.d.}}{\sim}\pi_{\theta}(\cdot\mid{}x) for each prompt x x . Letting Σ := λ ​ I d + ∑ i = 1 k h ¯ θ ​ ( x , y i ) ​ h ¯ θ ​ ( x , y i ) ⊤ \Sigma\vcentcolon=\lambda{}I_{d}+\sum_{i=1}^{k}\bar{h}_{\theta}(x,y_{i})\bar{h}_{\theta}(x,y_{i})^{\top} , we define the reward for response y i y_{i} as 3 3 3 The bonus here can be interpreted as a leverage score for y i y_{i} ( Drineas et al., 2006 ; Cohen et al., 2015 ) . r ⋆ ​ ( x , y i ) + β ⋅ h ¯ θ ​ ( x , y i ) ⊤ ​ Σ − 1 ​ h ¯ θ ​ ( x , y i ) r^{\star}(x,y_{i})+\beta\cdot\bar{h}_{\theta}(x,y_{i})^{\top}\Sigma^{-1}\bar{h}_{\theta}(x,y_{i}) , where β > 0 \beta>0 is a bonus parameter. While one could also imagine performing inference-time coreset selection in the loop with GRPO, this approach is more practical and efficient, and it achieves significant improvements in performance. We refer the reader to Section 5 and Appendix C for further details.

#### Why representation-based elliptical bonuses?

We summarize several desirable properties of these bonuses. First, by leveraging the hidden state of the model in featurization, the bonuses capture rich information about the generations, thereby incorporating the language model’s prior knowledge. Second, the method is history-aware 4 4 4 In the RL setting, we do not let the covariance matrix persist across multiple iterations of the same question, and hence there it is only group-aware . : the covariance matrix summarizes all previously selected generations, and redundancy with previous selection (in representation space) is penalized. Finally, the method is simple and scalable, involving no additional learning machinery and using rank-one updates to avoid costly matrix inversions.

## 4 Inference-Time Exploration: Experimental Results

In this section, we investigate the performance of representation-based exploration for the inference-time selection problem. We detail the experimental setup in Section 4 , present main findings in Section 4.1 , and present additional experiments with a “token-level” variant in Section 4.2 .

#### Datasets

We use the test splits of the following five datasets: MATH ( Hendrycks et al., 2021 ) , GSM8K ( Cobbe et al., 2021 ) , MBPP+ ( Liu et al., 2023 ) , Game-of-24 ( Yao et al., 2023 ) , and AIME 2025 . We chose these tasks as they cover easy ( GSM8K ), medium ( MATH ), and harder ( Game-of-24 , AIME ) difficulty levels in math. In addition, we include MBPP+ to verify that our findings transfer to the coding domain. For a more detailed overview of these datasets, please refer to Section B.1 .

#### Models

We consider a range of model families and sizes: Phi-3-Medium ( Abdin et al., 2024a ) and Phi-4 , Llama-3.2-3B-Instruct and Llama-3.1-8B-Instruct ( Dubey et al., 2024 ) , ( Abdin et al., 2024b ) , Qwen-2.5-X-Instruct ( Qwen et al., 2024 ) for X ∈ { 0.5B , 3B , 7B , 14B , 32B } \texttt{X}\in\left\{\texttt{0.5B},\texttt{3B},\texttt{7B},\texttt{14B},\texttt{32B}\right\} , and Mistral-7B ( Jiang et al., 2023 ) .

#### Algorithms

In our experiment protocol, we initially draw a pool of N N candidate generations from the base model, where unless otherwise specified we use temperature τ = 1.0 \tau=1.0 and top-p = 1.0 \text{top-p}=1.0 , which we refer to as vanilla settings (for MBPP+ , we set top-p = 0.95 \text{top-p}=0.95 ). Then we compare RepExp with budget k k with the baseline of random sampling (without replacement) of k k responses from this pool. We consider generating the pool using different samplers such as nucleus and min-p sampling in Fig. 6 , but always use random sampling without replacement as the baseline. See Section B.1 for further details.

### 4.1 Benefits of representation-based exploration

We present our results as a series of Research Findings (RF), expanding on the findings in Fig. 1 .

#### RF1 : RepExp improves verifier efficiency across models and tasks

In Fig. 1 , we plot the samples-to-correct , defined as the expected number of samples k k with which we query the verifier before finding a correct answer, for all model-task pairs. We compare RepExp , which picks responses to a fixed question according to Algorithm 1 , with the random sampling baseline. For both algorithms, we average the samples-to-correct across all questions in the dataset. Our results show the bulk of the data fall below the line y = x y=x , indicating exploration improves over random sampling in most cases. For example, we find RepExp obtains a 50% improvement in samples-to-correct for Qwen-2.5-14b-Instruct in MATH , GSM8K , MBPP+ , and Game-of-24 .

#### RF2 : The benefits of RepExp grow with model strength

Since RepExp relies on the model’s internal representations, it is natural to hypothesize that weaker models might have worse representations and thus benefit less from exploration. To validate this hypothesis, we expand the collection of models in Fig. 1 to include additional weaker models (e.g., Qwen-2.5-0.5B-Instruct and Mistral-7b ). For each task, we rank models according to their pass@1 performance, and plot the relative improvement of representation-based exploration over random sampling in Fig. 5 . We indeed observe a strong correlation between model strength and the benefit from representation-based exploration: weaker models (e.g., Qwen-2.5-0.5B ) experience no benefit or even degradation, while the strongest models (e.g., Qwen-2.5-32B ) almost uniformly benefit.

#### RF3 : RepExp provides more improvement for harder questions

Beyond RF2 —which provides insight into the benefits of RepExp across models —we also evaluate the benefits across question difficulty , for a fixed model and task. To this end, we sort all questions for a given task by their samples-to-correct under random sampling with a reference model ( GPT-4o-mini ). We then group the questions in bins, each containing 10% of the dataset, and plot the average samples-to-correct for each bin for both RepExp and random sampling. As displayed in Fig. 5 (right), RepExp matches or improves verifier efficiency across all bins, with the largest improvements on the hardest bins (e.g., the hardest 20% of questions on MATH ). Concretely, on the hardest Game-of-24 questions, we find that RepExp with Phi-4 provides a 3x improvement in verifier efficiency.

#### RF4 : RepExp improves verifier efficiency over standard generation modifications

We now investigate the effect of alternative base sampling strategies that might already induce diversity. Using Qwen-2.5-7B-Instruct on MATH , we change the underlying generation strategy to use one of five different generation settings: vanilla (no changes), low temperature ( τ = 0.6 \tau=0.6 ), high temperature ( τ = 1.5 \tau=1.5 ), min-p ( Minh et al., 2025 ) ( τ = 1.5 , p = 0.05 \tau=1.5,p=0.05 ), and nucleus sampling ( Holtzman et al., 2020 ) ( top-p = 0.9 \text{top-p}=0.9 ). In Fig. 6 , we find that RepExp improves verifier efficiency in all settings, except for when paired with high-temperature sampling. We suspect this is because high-temperature sampling tends to produce less coherent responses, which may look novel in representation space, yet do not necessarily contain correct answers.

### 4.2 Extension: Representation-based exploration at the token level

While useful in its own right as a testbed for benchmarking the viability of exploration methods, one drawback of the inference-time selection setting is that compute—as measured by N N , the size of the per-question data pool—may need to be rather large relative to k k for selection to yield improvements. As an extension, we conduct a preliminary investigation into algorithms that use elliptic bonuses to guide the autoregressive generation process itself, removing the need to generate such a pool at all.

#### Representation-based exploration for autoregressive generation

To guide sampling for improved diversity, given a budget k k , we use features from responses 1 , … , i − 1 1,\ldots,i-1 to guide the generation of the i ​ th i\text{th} response by modifying the logits at every generation step. Specifically, consider the i ​ th i\text{th} generation for a given prompt x x . At each position t t within the generation, we perturb the | V | |V| -dimensional token-level logit vector as: 𝐳 ~ ( i ) ​ ( x , y < t ) = 𝐳 ( i ) ​ ( x , y < t ) + β ⋅ 𝐛 ( i ) ​ ( x , y < t , V ) , 𝐳 ~ ( i ) ​ ( x ) ∈ ℝ | V | , \tilde{\mathbf{z}}^{(i)}(x,y_{<t})\;=\;\mathbf{z}^{(i)}(x,y_{<t})+\beta\cdot\mathbf{b}^{(i)}(x,y_{<t},V),\quad\tilde{\mathbf{z}}^{(i)}(x)\in\mathbb{R}^{|V|}, where the bonus 𝐛 ( i ) ​ ( x , y < t , V ) \mathbf{b}^{(i)}(x,y_{<t},V) is a token-level elliptic bonus, defined as: 𝐛 j ( i ) ​ ( x , y < t , V ) = h ~ θ ​ ( x , y < t , v j ) ⊤ ​ Σ ( i ) − 1 ​ h ~ θ ​ ( x , y < t , v j ) , \mathbf{b}_{j}^{(i)}(x,y_{<t},V)=\sqrt{\tilde{h}_{\theta}(x,y_{<t},v_{j})^{\top}\Sigma_{(i)}^{-1}\tilde{h}_{\theta}(x,y_{<t},v_{j})}, for v j ∈ V v_{j}\in V . Here h ~ θ ​ ( x , y < t , v j ) \tilde{h}_{\theta}(x,y_{<t},v_{j}) is a mean-centered Transformer representation for sequence ( y < t , v j ) (y_{<t},v_{j}) ; see Section B.2 for further details.

RF5 : RepExp for autoregressive generation improves solve rate . In Fig. 7 , we visualize the effect of token-level representation-based exploration for Qwen-2.5-7B-Instruct on the MATH task. We use two values for the bonus parameter β \beta (0.5, 1.0) and compare the pass@k to vanilla autoregressive generation for the 200 hardest (but solvable) questions in MATH , as judged by GPT-4o-mini . While token-level exploration tends to solve fewer problems compared to vanilla generation when given a small budget, this trend reverses when the budget exceeds 512 − 640 512-640 (depending on choice for β \beta ). Fig. 10 further shows that the improvement in solve rate is largest on the hardest questions. These results are encouraging, though further research is required (e.g., on more tasks and models) before one can draw a definitive conclusion. Further, our implementation is not optimized for efficiency and requires at least one additional forward pass per generation step compared to naive sampling.

### 4.3 Application: Protein sequence generation

As pointed out in Section 2.1 , we believe inference-time exploration can be useful in its own right for domains where verification is expensive. While an extensive study of this merits further study, we provide some preliminary experiments in the domain of protein sequence generation. In this domain, verification requires lab work, which is much more time consuming than sampling protein sequences from a generative protein model. Following prior work, we use two proxy metrics described below in lieu of expensive wet-lab verification.

For our experimental setup, we follow the unconditional generation setup in Hayes et al. (2025) and sample 2048 protein sequences for fully masked sequence prompts ranging in length from 64 to 916 with increments of size 4 (i.e. 64, 68, …, 916) using ESM3-open . Then, we perform structure prediction for all sampled sequences using ESMFold ( Lin et al., 2023 ) , which returns pLDDT and pTM scores per sequence. We count a sampled sequence as plausible when pLDDT > 0.8 and pTM > 0.8. To get representations for every sequence, we use esmc-600m , the 600M parameter version of ESM C ( Hayes et al., 2025 ; ESM Team, 2024 ) , and average the last-layer hidden representations. Finally, we perform inference-time selection for every prompt and its 2048 corresponding sampled sequences, using both random selection and RepExp . We find the average samples-to-correct for random to be 240.3 and for RepExp to be 6.7. This corresponds to a 35.9x verifier efficiency improvement. We also plot the corresponding pass@k curves in Fig. 8 , for which we find up to 56.9x improvements in verifier efficiency.

We find these results to be very promising and suggestive that our method can be practical in a domain where verification is genuinely expensive.

## 5 Exploration for RL Post-Training

Following the methodology in Section 2 , we now investigate the use of representation-based exploration to guide the RL post-training process.

#### Tasks and models

We use Qwen-2.5-7b-Instruct evaluated on MATH , GSM8K , and AIME 2024 . Because there are only 30 30 questions in AIME 2024 , we follow Yu et al. (2025) and use the DAPO-Math-17K dataset for training, leaving AIME 2024 for evaluation only. Please refer to Appendix C for exact details on train, validation, and test splits for all tasks.

#### Baselines

We compare our method with three baselines: (1) Unlikeliness ( He et al., 2025 ) modifies GRPO by scaling the extrinsic rewards by a value inversely related to the likelihood of a generation under the current policy. (2) GRPO is simply an unmodified version of the original GRPO algorithm. (3) Base Model is the original untrained model included as a reference point to see if methods can improve upon it, especially at high values of k k .

Representation-based Exploration ( RepExp ). We augment the rewards in GRPO with representation-based bonuses as described in Section 3 . Concretely, we add sequence-level elliptic bonuses to the binary extrinsic rewards provided by the verifier: r i = R ⁡ ( x , y i ) + b ⁡ ( x , y i ) r_{i}=R(x,y_{i})+b(x,y_{i}) for the i th i^{\text{th}} rollout y i y_{i} of a given prompt x x . As mentioned in Section 3 , we specifically use leverage score-like elliptic bonuses, which allow easier control over their scale as they are bounded in [ 0 , 1 ] [0,1] . The covariance matrix Σ \Sigma used to compute bonuses is re-initialized for each batch of RL training. This way, the bonus b ⁡ ( x , y i ) b(x,y_{i}) measures the novelty of y i y_{i} only with respect to the other rollouts in the batch—previously generated sequences for x x are not considered. To better maximize the bonus along all relevant directions in representation space, we draw a new random projection of h ¯ θ ​ ( x , y i ) \bar{h}_{\theta}(x,y_{i}) at each optimization step. For further details, please refer to Appendix C .

RF6 : RepExp improves pass@k. Fig. 2 compares pass@ k k curves after training for all methods. In line with earlier work, we find that all instantiations of GRPO improve the pass@k for small values of k k , and that standard GRPO degrades performance relative to the base model for large values of k k ( Yue et al., 2025 ) . Exploration appears to be an essential part of mitigating the latter effect: policies fit using RepExp preserve or improve pass@ k k for large values of k k with limited reductions for small k k . This phenomenon is more pronounced for RepExp than for Unlikeliness.

#### RF7 : RepExp responses look novel

To provide further insight into whether RepExp is able to move beyond merely sharpening the base model, we run an additional experiment inspired by Figure 4 in Karan and Du (2025) . Specifically, we sample a single response from the base model, the GRPO post-trained model, and the RepExp post-trained model for each question in the full test set of MATH . We then score all responses under the base model in terms of log likelihood. We plot the resulting histogram in Fig. 9 . We find that responses from RepExp tend to be less likely under the base model, indicating that it generates more novel responses and is therefore not merely performing sharpening. In contrast, notice that standard GRPO exhibits sharpening behavior, as demonstrated by the movement of probability mass towards the right with respect to the base model. Taken together with RF6, these results suggest that with the right exploration strategy, we may be able to escape the sharpening regime and discover novel model behaviors.

## 6 Discussion

#### Related work

Several recent works aim to encourage exploration in language models, either by adapting exploration techniques from deep reinforcement learning, or by augmenting PPO or GRPO in ways that are more specialized to language models ( He et al., 2025 ; Cheng et al., 2025 ; Chen et al., 2025b ; Zhou et al., 2025 ; Setlur et al., 2025 ; Liu et al., 2025 ) . Examples of the former include count-based exploration via pseudo-counts ( Bai et al., 2025 ) and at the outcome level ( Song et al., 2025 ) , random network distillation ( Liu et al., 2024b ; Gao et al., 2025 ) , and posterior sampling ( Dwaracherla et al., 2024 ) . Examples of the latter include rewarding unlikely-but-correct responses ( He et al., 2025 ) , entropy bonuses ( Cheng et al., 2025 ) , adapting the number of rollouts based on question difficulty ( Yang et al., 2025 ) , training the model to explore in-context ( Setlur et al., 2024 ) , using a learned classifier to jointly optimize diversity and quality ( Li et al., 2025 ) , adding a diversity term based on determinantal point processes to the RL objective ( Chen et al., 2025a ) , and reformulating post-training to more-directly maximize the pass@ N N objective ( Balashankar et al., 2024 ; Chow et al., 2025 ; Chen et al., 2025b ; Walder and Karkhanis, 2025 ; Tang et al., 2025 ) . Among these, we experiment with the unlikeliness reward approach of He et al. (2025) as a baseline, due to its robust performance and clean implementation. More generally, our work is unique in (1) the specific representation-based objective, and (2) our focus on inference-time as a means to validate methods with minimal confounding factors. See Appendix A for a detailed overview.

#### Final remarks

Our work shows that deliberate exploration is a viable path toward expanding the reasoning capabilities of language models, offering the possibility of discovering novel behaviors that would be unlikely under naive sampling. While our results show that representation-based diversity is effective at incentivizing exploration, the algorithm design space for exploration techniques is vast, and there is still much to understand regarding how to best use the knowledge encoded in foundation models to guide exploration. Along these lines, natural directions for future work include: 1. Scaling up RL compute, and combining exploration with other techniques known to improve reasoning behavior in RL post-training, such as prolonged reinforcement learning ( Liu et al., 2025 ) .

2. Exploration for autoregressive generation. Our results in Section 4.2 show that incentivizing diversity during autoregressive generation is a promising approach to reducing the computational burden of exploration, but much remains to be done in terms of (1) understanding which diversity metrics are most helpful, and (2) optimizing the implementation to close the compute gap.

3. Beyond verifiable rewards. How can we deliberately incentivize exploration in domains without verifiable rewards, while simultaneously mitigating reward hacking?

## Acknowledgements

We thank Adam Block, Qinghua Liu, and Max Simchowitz for valuable feedback on this work. We thank Manan Tomar, Audrey Huang, Spencer Whitehead, Prabhat Nagarajan, and Karthik Narasimhan for support and encouragement throughout the project.

## Reproducibility Statement

To ensure reproducibility of our results, we have listed all relevant details (hyperparameters, experiment resources, etc.) for the inference-time experiments in Appendix B , and those for RL post-training in Appendix C . In addition, the code for all our experiments and plots can be found at https://rep-exp.github.io . We used Weights & Biases for experiment tracking and visualizations to develop insights for this paper.

## References

Abbasi-Yadkori et al. (2011) Yasin Abbasi-Yadkori, Dávid Pál, and Csaba Szepesvári. Improved algorithms for linear stochastic bandits. In Advances in Neural Information Processing Systems , 2011.

Abdin et al. (2024a) Marah Abdin, Jyoti Aneja, Harkirat Behl, Sébastien Bubeck, Ronen Eldan, Suriya Gunasekar, Michael Harrison, Russell J Hewett, Mojan Javaheripi, Piero Kauffmann, et al. Phi-4 technical report. arXiv preprint arXiv:2412.08905 , 2024a.

Abdin et al. (2024b) Marah Abdin, Jyoti Aneja, Harkirat Behl, Sébastien Bubeck, Ronen Eldan, Suriya Gunasekar, Michael Harrison, Russell J Hewett, Mojan Javaheripi, Piero Kauffmann, et al. Phi-4 technical report. arXiv preprint arXiv:2412.08905 , 2024b.

Agarwal (2013) Alekh Agarwal. Selective sampling algorithms for cost-sensitive multiclass prediction. In International Conference on Machine Learning , pages 1220–1228. PMLR, 2013.

Agarwal et al. (2020a) Alekh Agarwal, Mikael Henaff, Sham Kakade, and Wen Sun. Pc-pg: Policy cover directed exploration for provable policy gradient learning. Advances in neural information processing systems , 33:13399–13412, 2020a.

Agarwal et al. (2020b) Alekh Agarwal, Sham Kakade, Akshay Krishnamurthy, and Wen Sun. FLAMBE: Structural complexity and representation learning of low rank MDPs. Neural Information Processing Systems (NeurIPS) , 2020b.

Allen-Zhu et al. (2021) Zeyuan Allen-Zhu, Yuanzhi Li, Aarti Singh, and Yining Wang. Near-optimal discrete optimization for experimental design: A regret minimization approach. Mathematical Programming , 186(1):439–478, 2021.

Arumugam and Griffiths (2025) Dilip Arumugam and Thomas L Griffiths. Toward efficient exploration by large language model agents. arXiv preprint arXiv:2504.20997 , 2025.

Ash et al. (2021) Jordan T Ash, Cyril Zhang, Surbhi Goel, Akshay Krishnamurthy, and Sham Kakade. Anti-concentrated confidence bonuses for scalable exploration. arXiv preprint arXiv:2110.11202 , 2021.

Austin et al. (2021) Jacob Austin, Augustus Odena, Maxwell Nye, Maarten Bosma, Henryk Michalewski, David Dohan, Ellen Jiang, Carrie Cai, Michael Terry, Quoc Le, et al. Program synthesis with large language models. arXiv preprint arXiv:2108.07732 , 2021.

Bai et al. (2025) Chenjia Bai, Yang Zhang, Shuang Qiu, Qiaosheng Zhang, Kang Xu, and Xuelong Li. Online preference alignment for language models via count-based exploration. arXiv preprint arXiv:2501.12735 , 2025.

Balashankar et al. (2024) Ananth Balashankar, Ziteng Sun, Jonathan Berant, Jacob Eisenstein, Michael Collins, Adrian Hutter, Jong Lee, Chirag Nagpal, Flavien Prost, Aradhana Sinha, et al. Infalign: Inference-aware language model alignment. arXiv preprint arXiv:2412.19792 , 2024.

Burda et al. (2018) Yuri Burda, Harrison Edwards, Amos Storkey, and Oleg Klimov. Exploration by random network distillation. arXiv preprint arXiv:1810.12894 , 2018.

Cen et al. (2024) Shicong Cen, Jincheng Mei, Katayoon Goshvadi, Hanjun Dai, Tong Yang, Sherry Yang, Dale Schuurmans, Yuejie Chi, and Bo Dai. Value-incentivized preference optimization: A unified approach to online and offline rlhf, 2024.

Cesa-Bianchi et al. (2009) Nicolo Cesa-Bianchi, Claudio Gentile, and Francesco Orabona. Robust bounds for classification via selective sampling. In Proceedings of the 26th annual international conference on machine learning , pages 121–128, 2009.

Chaudhuri et al. (2015) Kamalika Chaudhuri, Sham M Kakade, Praneeth Netrapalli, and Sujay Sanghavi. Convergence rates of active learning for maximum likelihood estimation. Advances in Neural Information Processing Systems , 28, 2015.

Chen et al. (2021) Mark Chen, Jerry Tworek, Heewoo Jun, Qiming Yuan, Henrique Ponde De Oliveira Pinto, Jared Kaplan, Harri Edwards, Yuri Burda, Nicholas Joseph, Greg Brockman, et al. Evaluating large language models trained on code. arXiv preprint arXiv:2107.03374 , 2021.

Chen et al. (2024) Ruizhe Chen, Xiaotian Zhang, Meng Luo, Wenhao Chai, and Zuozhu Liu. Pad: Personalized alignment at decoding-time. arXiv:2410.04070 , 2024.

Chen et al. (2025a) Yilei Chen, Souradip Chakraborty, Lorenz Wolf, Ioannis Ch Paschalidis, and Aldo Pacchiano. Enhancing diversity in large language models via determinantal point processes. arXiv preprint arXiv:2509.04784 , 2025a.

Chen et al. (2025b) Zhipeng Chen, Xiaobo Qin, Youbin Wu, Yue Ling, Qinghao Ye, Wayne Xin Zhao, and Guang Shi. Pass@k training for adaptively balancing exploration and exploitation of large reasoning models, 2025b. URL https://arxiv.org/abs/2508.10751 .

Cheng et al. (2025) Daixuan Cheng, Shaohan Huang, Xuekai Zhu, Bo Dai, Wayne Xin Zhao, Zhenliang Zhang, and Furu Wei. Reasoning with exploration: An entropy perspective. arXiv preprint arXiv:2506.14758 , 2025.

Chow et al. (2025) Yinlam Chow, Guy Tennenholtz, Izzeddin Gur, Vincent Zhuang, Bo Dai, Aviral Kumar, Rishabh Agarwal, Sridhar Thiagarajan, Craig Boutilier, and Aleksandra Faust. Inference-aware fine-tuning for best-of-n sampling in large language models. In The Thirteenth International Conference on Learning Representations , 2025.

Chu et al. (2011) Wei Chu, Lihong Li, Lev Reyzin, and Robert E. Schapire. Contextual bandits with linear payoff functions. In International Conference on Artificial Intelligence and Statistics , 2011.

Clarkson (2010) Kenneth L Clarkson. Coresets, sparse greedy approximation, and the frank-wolfe algorithm. ACM Transactions on Algorithms (TALG) , 6(4):1–30, 2010.

Cobbe et al. (2021) Karl Cobbe, Vineet Kosaraju, Mohammad Bavarian, Mark Chen, Heewoo Jun, Lukasz Kaiser, Matthias Plappert, Jerry Tworek, Jacob Hilton, Reiichiro Nakano, et al. Training verifiers to solve math word problems. arXiv:2110.14168 , 2021.

Cohen et al. (2015) Michael B Cohen, Yin Tat Lee, Cameron Musco, Christopher Musco, Richard Peng, and Aaron Sidford. Uniform sampling for matrix approximation. In Proceedings of the 2015 conference on innovations in theoretical computer science , pages 181–190, 2015.

Dang et al. (2025) Xingyu Dang, Christina Baek, Kaiyue Wen, Zico Kolter, and Aditi Raghunathan. Weight ensembling improves reasoning in language models. arXiv:2504.10478 , 2025.

DeepSeek-AI (2025) DeepSeek-AI. DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning. 2025. URL https://github.com/deepseek-ai/DeepSeek-R1/blob/main/DeepSeek_R1.pdf .

Drineas et al. (2006) Petros Drineas, Michael W Mahoney, and S Muthukrishnan. Subspace sampling and relative-error matrix approximation: Column-row-based methods. In European Symposium on Algorithms , pages 304–314. Springer, 2006.

Dubey et al. (2024) Abhimanyu Dubey, Abhinav Jauhri, Abhinav Pandey, Abhishek Kadian, Ahmad Al-Dahle, Aiesha Letman, Akhil Mathur, Alan Schelten, Amy Yang, Angela Fan, et al. The llama 3 herd of models. arXiv:2407.21783 , 2024.

Dwaracherla et al. (2024) Vikranth Dwaracherla, Seyed Mohammad Asghari, Botao Hao, and Benjamin Van Roy. Efficient exploration for llms. In Forty-first International Conference on Machine Learning , 2024.

ESM Team (2024) ESM Team. Esm cambrian: Revealing the mysteries of proteins with unsupervised learning, 2024. URL https://evolutionaryscale.ai/blog/esm-cambrian .

Feldman et al. (2020) Dan Feldman, Melanie Schmidt, and Christian Sohler. Turning big data into tiny data: Constant-size coresets for k-means, pca, and projective clustering. SIAM Journal on Computing , 49(3):601–657, 2020.

Foster et al. (2025) Dylan J Foster, Zakaria Mhammedi, and Dhruv Rohatgi. Is a good foundation necessary for efficient reinforcement learning? the computational role of the base model in exploration. Conference on Learning Theory (COLT) , 2025.

Gandhi et al. (2025) Kanishk Gandhi, Ayush Chakravarthy, Anikait Singh, Nathan Lile, and Noah D Goodman. Cognitive behaviors that enable self-improving reasoners, or, four habits of highly effective stars. arXiv preprint arXiv:2503.01307 , 2025.

Gao et al. (2025) Jingtong Gao, Ling Pan, Yejing Wang, Rui Zhong, Chi Lu, Qingpeng Cai, Peng Jiang, and Xiangyu Zhao. Navigate the unknown: Enhancing llm reasoning with intrinsic motivation guided exploration. arXiv preprint arXiv:2505.17621 , 2025.

Gu et al. (2014) Quanquan Gu, Tong Zhang, and Jiawei Han. Batch-mode active learning via error bound minimization. In UAI , pages 300–309, 2014.

Hayes et al. (2025) Thomas Hayes, Roshan Rao, Halil Akin, Nicholas J. Sofroniew, Deniz Oktay, Zeming Lin, Robert Verkuil, Vincent Q. Tran, Jonathan Deaton, Marius Wiggert, Rohil Badkundri, Irhum Shafkat, Jun Gong, Alexander Derry, Raul S. Molina, Neil Thomas, Yousuf A. Khan, Chetan Mishra, Carolyn Kim, Liam J. Bartie, Matthew Nemeth, Patrick D. Hsu, Tom Sercu, Salvatore Candido, and Alexander Rives. Simulating 500 million years of evolution with a language model. Science , 387(6736):850–858, 2025. doi: 10.1126/science.ads0018 . URL https://www.science.org/doi/abs/10.1126/science.ads0018 .

He et al. (2025) Andre He, Daniel Fried, and Sean Welleck. Rewarding the unlikely: Lifting grpo beyond distribution sharpening. arXiv preprint arXiv:2506.02355 , 2025.

Henaff et al. (2022) Mikael Henaff, Roberta Raileanu, Minqi Jiang, and Tim Rocktäschel. Exploration via elliptical episodic bonuses. Advances in Neural Information Processing Systems , 35:37631–37646, 2022.

Hendrycks et al. (2021) Dan Hendrycks, Collin Burns, Saurav Kadavath, Akul Arora, Steven Basart, Eric Tang, Dawn Song, and Jacob Steinhardt. Measuring mathematical problem solving with the math dataset. In Thirty-fifth Conference on Neural Information Processing Systems Datasets and Benchmarks Track (Round 2) , 2021.

Holtzman et al. (2020) Ari Holtzman, Jan Buys, Li Du, Maxwell Forbes, and Yejin Choi. The curious case of neural text degeneration. In International Conference on Learning Representations , 2020.

Huang et al. (2025) Audrey Huang, Adam Block, Dylan J Foster, Dhruv Rohatgi, Cyril Zhang, Max Simchowitz, Jordan T Ash, and Akshay Krishnamurthy. Self-improvement in language models: The sharpening mechanism. International Conference on Learning Representations (ICLR) , 2025.

Ivison et al. (2025) Hamish Ivison, Muru Zhang, Faeze Brahman, Pang Wei Koh, and Pradeep Dasigi. Large-scale data selection for instruction tuning. arXiv preprint arXiv:2503.01807 , 2025.

Jiang et al. (2023) AQ Jiang, A Sablayrolles, A Mensch, C Bamford, DS Chaplot, D de Las Casas, F Bressand, G Lengyel, G Lample, L Saulnier, et al. Mistral 7b. corr, abs/2310.06825, 2023. doi: 10.48550. arXiv preprint ARXIV.2310.06825 , 10, 2023.

Jinnai et al. (2024) Yuu Jinnai, Tetsuro Morimura, Kaito Ariu, and Kenshi Abe. Regularized best-of-n sampling to mitigate reward hacking for language model alignment. arXiv:2404.01054 , 2024.

Karan and Du (2025) Aayush Karan and Yilun Du. Reasoning with sampling: Your base model is smarter than you think. arXiv preprint arXiv:2510.14901 , 2025.

Khanov et al. (2024) Maxim Khanov, Jirayu Burapacheep, and Yixuan Li. Args: Alignment as reward-guided search. arXiv:2402.01694 , 2024.

Kiefer and Wolfowitz (1960) Jack Kiefer and Jacob Wolfowitz. The equivalence of two extremum problems. Canadian Journal of Mathematics , 12:363–366, 1960.

Kwon et al. (2023) Woosuk Kwon, Zhuohan Li, Siyuan Zhuang, Ying Sheng, Lianmin Zheng, Cody Hao Yu, Joseph E. Gonzalez, Hao Zhang, and Ion Stoica. Efficient memory management for large language model serving with pagedattention. In Proceedings of the ACM SIGOPS 29th Symposium on Operating Systems Principles , 2023.

Lanchantin et al. (2025) Jack Lanchantin, Angelica Chen, Shehzaad Dhuliawala, Ping Yu, Jason Weston, Sainbayar Sukhbaatar, and Ilia Kulikov. Diverse preference optimization. arXiv preprint arXiv:2501.18101 , 2025.

Lattimore and Szepesvári (2020) Tor Lattimore and Csaba Szepesvári. Bandit algorithms . Cambridge University Press, 2020.

Li et al. (2006) Ping Li, Trevor J. Hastie, and Kenneth Ward Church. Very sparse random projections. In Knowledge Discovery and Data Mining , 2006. URL https://api.semanticscholar.org/CorpusID:7995734 .

Li et al. (2025) Tianjian Li, Yiming Zhang, Ping Yu, Swarnadeep Saha, Daniel Khashabi, Jason Weston, Jack Lanchantin, and Tianlu Wang. Jointly reinforcing diversity and quality in language model generations. arXiv preprint arXiv:2509.02534 , 2025.

Lightman et al. (2023) Hunter Lightman, Vineet Kosaraju, Yura Burda, Harri Edwards, Bowen Baker, Teddy Lee, Jan Leike, John Schulman, Ilya Sutskever, and Karl Cobbe. Let’s verify step by step. arXiv preprint arXiv:2305.20050 , 2023.

Lin et al. (2023) Zeming Lin, Halil Akin, Roshan Rao, Brian Hie, Zhongkai Zhu, Wenting Lu, Nikita Smetanin, Robert Verkuil, Ori Kabeli, Yaniv Shmueli, Allan dos Santos Costa, Maryam Fazel-Zarandi, Tom Sercu, Salvatore Candido, and Alexander Rives. Evolutionary-scale prediction of atomic-level protein structure with a language model. Science , 379(6637):1123–1130, 2023. doi: 10.1126/science.ade2574 . URL https://www.science.org/doi/abs/10.1126/science.ade2574 .

Liu et al. (2023) Jiawei Liu, Chunqiu Steven Xia, Yuyao Wang, and Lingming Zhang. Is your code generated by chatgpt really correct? rigorous evaluation of large language models for code generation. Advances in Neural Information Processing Systems , 36:21558–21572, 2023.

Liu et al. (2025) Mingjie Liu, Shizhe Diao, Ximing Lu, Jian Hu, Xin Dong, Yejin Choi, Jan Kautz, and Yi Dong. Prorl: Prolonged reinforcement learning expands reasoning boundaries in large language models. arXiv preprint arXiv:2505.24864 , 2025.

Liu et al. (2024a) Tianlin Liu, Shangmin Guo, Leonardo Bianco, Daniele Calandriello, Quentin Berthet, Felipe Llinares, Jessica Hoffmann, Lucas Dixon, Michal Valko, and Mathieu Blondel. Decoding-time realignment of language models. arXiv:2402.02992 , 2024a.

Liu et al. (2024b) Zichen Liu, Changyu Chen, Chao Du, Wee Sun Lee, and Min Lin. Sample-efficient alignment for llms. arXiv preprint arXiv:2411.01493 , 2024b.

Minh et al. (2025) Nguyen Nhat Minh, Andrew Baker, Clement Neo, Allen G Roush, Andreas Kirsch, and Ravid Shwartz-Ziv. Turning up the heat: Min-p sampling for creative and coherent llm outputs. In The Thirteenth International Conference on Learning Representations , 2025.

OpenAI (2024) OpenAI. Introducing openai o1. Blog , 2024. URL https://openai.com/o1/ .

Osband et al. (2019) Ian Osband, Benjamin Van Roy, Daniel J Russo, and Zheng Wen. Deep exploration via randomized value functions. Journal of Machine Learning Research , 20(124):1–62, 2019.

Pathak et al. (2017) Deepak Pathak, Pulkit Agrawal, Alexei A Efros, and Trevor Darrell. Curiosity-driven exploration by self-supervised prediction. In International conference on machine learning , pages 2778–2787. PMLR, 2017.

Pukelsheim (2006) Friedrich Pukelsheim. Optimal design of experiments . SIAM, 2006.

Qwen et al. (2024) A Yang Qwen, Baosong Yang, B Zhang, B Hui, B Zheng, B Yu, Chengpeng Li, D Liu, F Huang, H Wei, et al. Qwen2.5 technical report. arXiv preprint , 2024.

Rafailov et al. (2023) Rafael Rafailov, Archit Sharma, Eric Mitchell, Christopher D Manning, Stefano Ermon, and Chelsea Finn. Direct preference optimization: Your language model is secretly a reward model. Advances in Neural Information Processing Systems , 2023.

Rohatgi and Saleh (2015) V. K. Rohatgi and A. K. Md. Ehsanes Saleh. An Introduction to Probability and Statistics . John Wiley & Sons, Inc., 3rd edition, 2015.

Saran et al. (2023) Akanksha Saran, Safoora Yousefi, Akshay Krishnamurthy, John Langford, and Jordan T Ash. Streaming active learning with deep neural networks. In International Conference on Machine Learning , pages 30005–30021. PMLR, 2023.

Schulman et al. (2017) John Schulman, Filip Wolski, Prafulla Dhariwal, Alec Radford, and Oleg Klimov. Proximal policy optimization algorithms. arXiv:1707.06347 , 2017.

Setlur et al. (2024) Amrith Setlur, Chirag Nagpal, Adam Fisch, Xinyang Geng, Jacob Eisenstein, Rishabh Agarwal, Alekh Agarwal, Jonathan Berant, and Aviral Kumar. Rewarding progress: Scaling automated process verifiers for llm reasoning. arXiv preprint arXiv:2410.08146 , 2024.

Setlur et al. (2025) Amrith Setlur, Matthew YR Yang, Charlie Snell, Jeremy Greer, Ian Wu, Virginia Smith, Max Simchowitz, and Aviral Kumar. e3: Learning to explore enables extrapolation of test-time compute for llms. arXiv preprint arXiv:2506.09026 , 2025.

Shao et al. (2024) Zhihong Shao, Peiyi Wang, Qihao Zhu, Runxin Xu, Junxiao Song, Xiao Bi, Haowei Zhang, Mingchuan Zhang, YK Li, Yang Wu, et al. Deepseekmath: Pushing the limits of mathematical reasoning in open language models. arXiv preprint arXiv:2402.03300 , 2024.

Sheng et al. (2024) Guangming Sheng, Chi Zhang, Zilingfeng Ye, Xibin Wu, Wang Zhang, Ru Zhang, Yanghua Peng, Haibin Lin, and Chuan Wu. Hybridflow: A flexible and efficient rlhf framework. arXiv preprint arXiv: 2409.19256 , 2024.

Shi et al. (2024a) Ruizhe Shi, Yifang Chen, Yushi Hu, ALisa Liu, Noah Smith, Hannaneh Hajishirzi, and Simon Du. Decoding-time language model alignment with multiple objectives. arXiv:2406.18853 , 2024a.

Shi et al. (2024b) Ruizhe Shi, Runlong Zhou, and Simon S Du. The crucial role of samplers in online direct preference optimization. arXiv preprint arXiv:2409.19605 , 2024b.

Song et al. (2025) Yuda Song, Julia Kempe, and Remi Munos. Outcome-based exploration for llm reasoning. arXiv preprint arXiv:2509.06941 , 2025.

Tang et al. (2017) Haoran Tang, Rein Houthooft, Davis Foote, Adam Stooke, OpenAI Xi Chen, Yan Duan, John Schulman, Filip DeTurck, and Pieter Abbeel. # exploration: A study of count-based exploration for deep reinforcement learning. Advances in neural information processing systems , 30, 2017.

Tang et al. (2025) Yunhao Tang, Kunhao Zheng, Gabriel Synnaeve, and Remi Munos. Optimizing language models for inference time objectives using reinforcement learning. In Forty-second International Conference on Machine Learning , 2025.

Vetterling and Press (1992) William T Vetterling and William H Press. Numerical recipes: example book C . Cambridge University Press, 1992.

Walder and Karkhanis (2025) Christian Walder and Deep Karkhanis. Pass@ k policy optimization: Solving harder reinforcement learning problems. arXiv preprint arXiv:2505.15201 , 2025.

Wu et al. (2025) Fang Wu, Weihao Xuan, Ximing Lu, Zaid Harchaoui, and Yejin Choi. The invisible leash: Why rlvr may not escape its origin. arXiv preprint arXiv:2507.14843 , 2025.

Xie et al. (2024) Tengyang Xie, Dylan J Foster, Akshay Krishnamurthy, Corby Rosset, Ahmed Awadallah, and Alexander Rakhlin. Exploratory preference optimization: Harnessing implicit Q*-approximation for sample-efficient RLHF. arXiv:2405.21046 , 2024.

Xu et al. (2025) Wanqiao Xu, Allen Nie, Ruijie Zheng, Aditya Modi, Adith Swaminathan, and Ching-An Cheng. Provably learning from language feedback. arXiv preprint arXiv:2506.10341 , 2025.

Yang et al. (2025) Zhicheng Yang, Zhijiang Guo, Yinya Huang, Yongxin Wang, Dongchun Xie, Yiwei Wang, Xiaodan Liang, and Jing Tang. Depth-breadth synergy in rlvr: Unlocking llm reasoning gains with adaptive exploration. arXiv preprint arXiv:2508.13755 , 2025.

Yao et al. (2023) Shunyu Yao, Dian Yu, Jeffrey Zhao, Izhak Shafran, Tom Griffiths, Yuan Cao, and Karthik Narasimhan. Tree of thoughts: Deliberate problem solving with large language models. Advances in neural information processing systems , 36:11809–11822, 2023.

Yu et al. (2025) Qiying Yu, Zheng Zhang, Ruofei Zhu, Yufeng Yuan, Xiaochen Zuo, Yu Yue, Weinan Dai, Tiantian Fan, Gaohong Liu, Lingjun Liu, et al. Dapo: An open-source llm reinforcement learning system at scale. arXiv preprint arXiv:2503.14476 , 2025.

Yue et al. (2025) Yang Yue, Zhiqi Chen, Rui Lu, Andrew Zhao, Zhaokai Wang, Shiji Song, and Gao Huang. Does reinforcement learning really incentivize reasoning capacity in llms beyond the base model? arXiv preprint arXiv:2504.13837 , 2025.

Zhang et al. (2024) Shenao Zhang, Donghan Yu, Hiteshi Sharma, Ziyi Yang, Shuohang Wang, Hany Hassan, and Zhaoran Wang. Self-exploring language models: Active preference elicitation for online alignment, 2024.

Zhou et al. (2025) Ruiyang Zhou, Shuozhe Li, Amy Zhang, and Liu Leqi. Expo: Unlocking hard reasoning with self-explanation-guided reinforcement learning. arXiv preprint arXiv:2507.02834 , 2025.

## Appendix A Additional Related Work

#### Exploration at test time

Test-time alignment techniques for language models are an active area of research with many complementary threads ( Khanov et al., 2024 ; Chen et al., 2024 ; Shi et al., 2024a ; Liu et al., 2024a ; Jinnai et al., 2024 ; Shi et al., 2024b ) , but exploration has not typically been the focus of this line of work.

Most closely related to our work, Setlur et al. (2025) , propose a test-time exploration approach based on the idea of learning to explore in-context . They propose to encourage exploration within a long chain of thought by training the LLM to chain operations such as generation, verification, and refinement together in search of a solution. This is somewhat complementary to our inference-time exploration framework, which aims to improve diversity across parallel generations once the model is fixed; these techniques could potentially be combined.

Also related, Xu et al. (2025) consider the problem of learning from language (non-verifiable) feedback, and propose an iterative prompting approach to enable exploration at test time; their work focuses on simpler exploration domains, but with more difficult, implicit feedback.

#### Exploration in RL post-training

Exploration in RL post-training for reasoning is a growing area of research, motivated by the observation that standard techniques tend to simply sharpen responses already covered by the base model ( Yue et al., 2025 ; Gandhi et al., 2025 ; Wu et al., 2025 ) . A number of recent works, discussed below, aim to improve diversity and expand the reasoning frontier by incorporating bonuses into the GRPO objective or by otherwise augmenting it. Briefly, our work is unique in terms of (1) the specific representation-based diversity objective we focus on, and (2) our focus on inference-time exploration as a means to validate diversity metrics before applying them to post-training.

He et al. (2025) introduce an unlikeliness reward to GRPO, which reweights the reward by ranking generations according to their unlikeliness under the sampling policy. Unlikeliness reward is a form of diversity metric, similar to our representation-based diversity metrics. Cheng et al. (2025) observe that high-entropy (high uncertainty) tokens in the model’s output often correspond to critical reasoning steps, and augment the GRPO objective with entropy bonuses to encourage exploration at these high-entropy steps. Entropy can be seen as another form of diversity metric in our setup. Another option is to learn the diversity metric as in Li et al. (2025) , who use a learned classifier to determine whether a pair of responses is semantically equivalent. They then use the classifier score to scale the reward in GRPO to joinly optimize quality and diversity. Our work, in contrast, does not require training any auxiliary models for computing diversity.

Various works ( Balashankar et al., 2024 ; Chow et al., 2025 ; Chen et al., 2025b ; Walder and Karkhanis, 2025 ; Tang et al., 2025 ) formulate the problem of directly post-training to maximize the pass@ N N objective, deriving approximate gradient estimators and using them for policy optimization. As discussed in Chow et al. (2025) ; Chen et al. (2025b) , these gradient estimators implicitly encourage exploration, since they allow the model to distribute probability mass across a more diverse range of responses when it is uncertain about the correct answer. Our work instead focuses on using the language model representations to deliberately incentivize novel behaviors, including in a novel inference-time setting.

Zhou et al. (2025) consider a setting where ground truth answers are available (as opposed to just rewards), and propose to encourage exploration by prompting the model to generate self-explanations for the ground truth answers and incorporating this as an SFT term in the GRPO loss. Unlike our method, their approach does not directly optimize for diversity, and cannot be used in settings where ground truth answers are unavailable (e.g. coding).

Yang et al. (2025) investigate the role of “breadth" (batch size) and “depth” (number of rollouts) in RLVR. They show that increasing breadth through full batch updates and increasing depth through more rollouts for harder questions has complementary benefits and overall improves pass@1 and pass@k performance. We view this as orthogonal and potentially complementary to our work.

Lanchantin et al. (2025) introduce diverse preference optimization (DivPO), an alignment method to optimize for both quality and diversity. In contrast to our work, their method is designed for the RLHF setting and applied to non-reasoning tasks (e.g. creative writing).

Concurrent work of Song et al. (2025) adapts tabular UCB-style bonuses to language model post-training with GRPO, but their approach—unlike representation-based exploration—is only suitable for domains with a small, discrete set of possible outcomes. Other concurrent work of Chen et al. (2025a) optimizes a diversity term along with the rewards, where the diversity term captures the volume of the responses in representation space by computing the determinant of the gram matrix. While related, our method instead adds a leverage-based score to the reward of each individual response.

Lastly, Liu et al. (2025) take a complementary approach and aim to incentivize reasoning beyond the base model through (1) prolonged RL training (increasing the overall amount of training steps), and (2) periodically resetting the reference model; they show that this can increase pass@ N N performance beyond the base model in a variety of reasoning tasks. This approach is complementary, and could likely be combined with our techniques.

#### Representation-based diversity

Our findings regarding benefits of inference-time exploration with representation-based diversity parallel the findings of Ivison et al. (2025) , who evaluated the effectiveness of various data selection schemes for instruction tuning, and found a similar representation-based scheme to be the most effective when normalized for compute. In addition, there is a long line of work relying on representation-based exploration for RL through elliptic bonuses in non-LLM settings ( Agarwal et al., 2020a ; Agarwal et al., 2020b ; Henaff et al., 2022 ; Ash et al., 2021 ) .

#### Adapting exploration techniques from deep reinforcement learning

Various papers have adapted exploration techniques from deep learning to language models, including Bai et al. (2025) (count-based exploration), Gao et al. (2025) (random network distillation), and Liu et al. (2024b) ; Dwaracherla et al. (2024) (posterior sampling). 5 5 5 See also Arumugam and Griffiths (2025) , which uses a pre-trained model to simulate posterior sampling in-context for multi-turn sequential decision making tasks. These works show initial promise in terms of sample complexity benefits, but their potential to explore beyond the base model in reasoning domains has not been evaluated to our knowledge. In addition, these methods require additional learning machinery (e.g., auxiliary networks), which introduces significant complexity when scaling to language models.

#### Theoretical analysis of language model exploration

On the theoretical side, our work draws on Foster et al. (2025) , who prove that test-time exploration with representation-based diversity has provable computational benefits in a simplified linear setting. Our RepExp algorithm for test-time exploration can be viewed as a simplified, practical adaptation of their theoretical algorithm.

Other theoretical works on exploration with language models include the XPO algorithm of Xie et al. (2024) and related algorithms by Cen et al. (2024) ; Zhang et al. (2024) , 6 6 6 Cen et al. (2024) ; Zhang et al. (2024) concurrently proposed similar algorithms to XPO , but did not provide non-trivial theoretical guarantees (e.g., guarantees that indicate benefits over purely passive exploration). which augment the Online DPO objective with exploration bonuses inspired by the optimism principle. To our knowledge, these techniques have only been evaluated on RLHF tasks, and Foster et al. (2025) show that there may be computational barriers to implementing them in a way that is faithful to the theoretical guarantees.

## Appendix B Details for Inference-Time Experiments ( Section 4 )

### B.1 Details from Section 4.1

#### Hyperparameters

In Algorithm 1 , we set λ = 1.0 \lambda=1.0 . For all models and tasks, we perform a sparse projection from the respective model hidden dimension to d = 512 d=512 .

#### Preprocessing

In Algorithm 1 , after obtaining the representations h ¯ θ \bar{h}_{\theta} for every generation y y for a fixed prompt x x , we sparse project all representations down and then mean-center where the mean is taken across the response-level representations.

#### Datasets

Below we provide a brief overview of all datasets along with relevant numerical details. Note that "vanilla" sampling settings refer to τ = 1.0 \tau=1.0 , top-p = 1.0 \text{top-p}=1.0 , and min-p = 0.0 \text{min-p}=0.0 . We also do not use top-k sampling in any of the coreset experiments. Finally, we only use the test split of every dataset for all our inference-time experiments, unless specified otherwise. • MATH . This dataset contains 12.5k problems from high school math competitions, split into 7.5k training examples and 5k test examples. For each question in the test split, we generate 6400 6400 responses using vanilla settings and set the maximum response length per generation to 512 512 tokens.

• GSM8K . This dataset contains 8.79k grade school math word problems, split into 7.47k training examples and 1.32k test examples. For each question in the test split, we generate 6400 6400 responses using vanilla settings and set the maximum response length per generation to 512 512 tokens.

• MBPP+ . This dataset contains 378 basic Python programming problems that are a curated subset of the full MBPP ( Austin et al., 2021 ) dataset with more test cases. Since the dataset does not come with any train or test splits, we use the full set of questions for our experiments. For each problem, we generate 6400 6400 responses using vanilla settings, except that we set top-p = 0.95 \text{top-p}=0.95 . We set the maximum response length per generation to 768 768 tokens.

• Game of 24 . This dataset contains 1.36k questions that specify four integers that need to be combined using basic arithmetic operations ( + , − , x , / ) (+,-,x,/) to equal 24 24 . For each question, we generate 6400 6400 responses using vanilla settings and set the maximum response length per generation to 512 512 tokens. We use the version available at https://huggingface.co/datasets/nlile/24-game .

• AIME 2025 . This dataset contains the 30 30 problems taken directly from the 2025 edition of the American Invitational Mathematics Examination (AIME). For each question, we generate 8192 8192 responses using vanilla settings and set the maximum response length per generation to 8192 8192 tokens.

#### Experiment resources

We used vLLM ( Kwon et al., 2023 ) on 1 − 2 1-2 (depending on the size of the model) NVIDIA A100 40GB GPUs per model-task pair to generate the data pools for all questions in the dataset.

#### Estimating samples-to-correct

For random sampling, we estimate the average number of samples to take (without replacement) from the data pool to find the first correct one as: samples-to-correct = N + 1 c + 1 , \text{samples-to-correct}=\frac{N+1}{c+1},

where N N indicates the size of the data pool and c c indicates the number of correct samples in the pool. Please refer to Rohatgi and Saleh (2015) for a proof. For the representation-based exploration algorithm described in Algorithm 1 , we perform 5 5 trials per question where we record the samples-to-correct for each and take their average.

#### Estimating pass@k

To compute the pass@k values plotted in Figure 6 , we follow Chen et al. (2021) and use the following unbiased estimator: pass@k = 𝔼 𝒟 ​ [ 1 − ( n − c k ) ( n k ) ] = 1 | 𝒟 | ​ ∑ i = 1 | 𝒟 | [ 1 − ( n − c k ) ( n k ) ] , \text{pass@k}=\mathbb{E}_{\mathcal{D}}\left[1-\frac{\binom{n-c}{k}}{\binom{n}{k}}\right]=\frac{1}{|\mathcal{D}|}\sum_{i=1}^{|\mathcal{D}|}\left[1-\frac{\binom{n-c}{k}}{\binom{n}{k}}\right],

where 𝒟 \mathcal{D} indicates the dataset and | 𝒟 | |\mathcal{D}| indicates its size.

### B.2 Details from Section 4.2

#### Hyperparameters

Similarly to Section 4.1 , we initialize Σ ( 0 ) − 1 = λ − 1 ​ I d \Sigma_{(0)}^{-1}=\lambda^{-1}I_{d} . We set λ = 0.1 \lambda=0.1 . For all values of β \beta , we use top-p = 0.95 \text{top-p}=0.95 and top-k = 128 \text{top-k}=128 . At every time step t t , we use a batch size of 64 to compute h θ ​ ( x , y < t , v j ) h_{\theta}(x,y_{<t},v_{j}) for all v j ∈ V v_{j}\in V where v j > − ∞ v_{j}>-\infty (note that a logit v j v_{j} is set to − ∞ -\infty if it gets filtered out by either the top-p or top-k filters mentioned earlier).

#### Computational expense

Note that computing the bonus 𝐛 ⁡ ( x , y < t , V ) \mathbf{b}(x,y_{<t},V) requires one forward pass through the model per token in the vocabulary at every time step t t . While these can be batched together since all tokens share the same prefix, this is still prohibitively time and memory intensive. To mitigate this, we combine this method with nucleus and top-k sampling such that the bonus will only need to be computed for at most k ≪ V k\ll V tokens.

#### Dataset construction

Due to the large computational cost of experiments, we only focus on MATH using Qwen-2.5-7b-Instruct . In addition, we do not evaluate on the full test split of MATH , but instead use a subset consisting of the 200 200 hardest questions as ranked by GPT-4o mini . Specifically, we sampled 1024 1024 responses for each question in the MATH test split using GPT-4o mini to estimate the per-question pass@1. We threw out all questions for which the pass@1 was 0 0 (indicating not a single response was correct among all 1024 1024 ), sorted the remaining questions, and kept the 200 200 questions with the lowest pass@1.

#### Estimating samples-to-correct

We collected up to 1024 1024 generations per question (stopping early once the correct answer was found). Since the resulting samples-to-correct value found can have high variance due to the inherent randomness in the generation process, we repeat this process 5 5 times with a different seed every time. This then results in a total of 200 × 5 = 1000 200\times 5=1000 data points, minus a few data points that didn’t finish running in time, for an effective total of 985 985 data points used in Fig. 7 .

#### Experiment resources

Experiments were run on a combination of NVIDIA A100 40GB, NVIDIA A100 80GB, and NVIDIA H100 80GB GPUs. Every run indicates one seed for a fixed question and performs up to 1024 1024 generations. We used one GPU (one of the several mentioned earlier) per run, adjusting the forward batch size to compute the elliptical bonus down from 64 64 to 32 32 when using the 40GB GPUs.

#### Computing the inverse covariance

The inverse covariance matrix Σ ( i ) − 1 \Sigma^{-1}_{(i)} includes all mean-centered hidden representations for all generated tokens in all i − 1 i-1 complete sequences generated so far for a fixed prompt x x . Note that the mean μ ( i ) \mu^{(i)} of the raw hidden representations h θ h_{\theta} is computed as: μ ( i ) = 1 H ​ ∑ j = 0 i − 1 ∑ t = 1 T j h θ ​ ( x , y < t ( j ) ) , H = ∑ j = 0 i − 1 T j , \ \mu^{(i)}=\frac{1}{H}\sum_{j=0}^{i-1}\sum_{t=1}^{T_{j}}h_{\theta}(x,y_{<t}^{(j)}),\quad H=\sum_{j=0}^{i-1}T_{j}, where T j T_{j} indicates the length (in number of tokens) of response j j . Because of this, the mean changes after every generation i i . This means some care is required when computing the inverse covariance matrix Σ ( i ) − 1 \Sigma^{-1}_{(i)} with mean-centered hidden representations. To account for this, we will separately keep track of the inverse covariance matrix Σ ~ ( i ) − 1 \tilde{\Sigma}^{-1}_{(i)} with non -mean-centered hidden representations as well as the mean μ ( i ) \mu^{(i)} . Then, we compute the mean-centered inverse covariance matrix Σ ( i ) − 1 \Sigma^{-1}_{(i)} as

Σ ( i ) − 1 = Σ ~ ( i ) − 1 − ( Σ ~ ( i ) − 1 ​ μ ( i ) ​ μ ( i ) T ​ Σ ~ ( i ) − 1 − 1 / H + μ ( i ) T Σ ~ ( i ) − 1 μ ( i ) ) . \Sigma^{-1}_{(i)}=\tilde{\Sigma}_{(i)}^{-1}-\left(\frac{\tilde{\Sigma}_{(i)}^{-1}\mu^{(i)}\mu_{(i)}^{T}\tilde{\Sigma}_{(i)}^{-1}}{-1/H+\mu_{(i)}^{T}\tilde{\Sigma}_{(i)}^{-1}\mu^{(i)}}\right).

This result is immediate from Proposition B.2 .

.

{proposition} Given the current generation step i i , the non-mean-centered inverse data covariance matrix Σ ~ ( i ) − 1 \tilde{\Sigma}^{-1}_{(i)} and the current mean μ ( i ) \mu^{(i)} , the mean-centered inverse data covariance matrix Σ ( i ) − 1 \Sigma^{-1}_{(i)} is given as Σ ( i ) − 1 = Σ ~ ( i ) − 1 − ( Σ ~ ( i ) − 1 ​ μ ( i ) ​ μ ( i ) T ​ Σ ~ ( i ) − 1 − 1 / H + μ ( i ) T Σ ~ ( i ) − 1 μ ( i ) ) , H = ∑ j = 0 i − 1 T j . \Sigma^{-1}_{(i)}=\tilde{\Sigma}_{(i)}^{-1}-\left(\frac{\tilde{\Sigma}_{(i)}^{-1}\mu^{(i)}\mu_{(i)}^{T}\tilde{\Sigma}_{(i)}^{-1}}{-1/H+\mu_{(i)}^{T}\tilde{\Sigma}_{(i)}^{-1}\mu^{(i)}}\right),\quad H=\sum_{j=0}^{i-1}T_{j}. Here, T j T_{j} indicates the length (in number of tokens) of response j j .

Proof of Section B.2 . We can write Σ ( i ) \displaystyle\Sigma^{(i)} = ∑ j = 0 i − 1 ∑ t = 1 T j ( h t ( j ) − μ t ( i ) ) ​ ( h t ( j ) − μ t ( i ) ) T \displaystyle=\sum_{j=0}^{i-1}\sum_{t=1}^{T_{j}}(h^{(j)}_{t}-\mu^{(i)}_{t})(h_{t}^{(j)}-\mu^{(i)}_{t})^{T} = ∑ j = 0 i − 1 ∑ t = 1 T j h t ( j ) ​ ( h t ( j ) ) T − ∑ j = 0 i − 1 ∑ t = 1 T j h t ( j ) ​ ( μ ( i ) ) T − ∑ j = 0 i − 1 ∑ t = 1 T j μ ( i ) ​ ( h t ( j ) ) T + ∑ j = 0 i − 1 ∑ t = 1 T j μ ( i ) ​ ( μ ( i ) ) T \displaystyle=\sum_{j=0}^{i-1}\sum_{t=1}^{T_{j}}h^{(j)}_{t}(h^{(j)}_{t})^{T}-\sum_{j=0}^{i-1}\sum_{t=1}^{T_{j}}h^{(j)}_{t}(\mu^{(i)})^{T}-\sum_{j=0}^{i-1}\sum_{t=1}^{T_{j}}\mu^{(i)}(h_{t}^{(j)})^{T}+\sum_{j=0}^{i-1}\sum_{t=1}^{T_{j}}\mu^{(i)}(\mu^{(i)})^{T} = Σ ~ ( i ) − ( ∑ j = 0 i − 1 ∑ t = 1 T j h t ( j ) ) ​ ( μ ( i ) ) T − μ ( i ) ​ ( ∑ j = 0 i − 1 ∑ t = 1 T j ( h t ( j ) ) T ) + ∑ j = 0 i − 1 ∑ t = 1 T j μ ( i ) ​ ( μ ( i ) ) T \displaystyle=\tilde{\Sigma}^{(i)}-\left(\sum_{j=0}^{i-1}\sum_{t=1}^{T_{j}}h_{t}^{(j)}\right)(\mu^{(i)})^{T}-\mu^{(i)}\left(\sum_{j=0}^{i-1}\sum_{t=1}^{T_{j}}(h_{t}^{(j)})^{T}\right)+\sum_{j=0}^{i-1}\sum_{t=1}^{T_{j}}\mu^{(i)}(\mu^{(i)})^{T} = Σ ~ ( i ) − H ​ μ ( i ) ​ ( μ ( i ) ) T − μ ( i ) ​ H ​ ( μ ( i ) ) T + H ​ μ ( i ) ​ ( μ ( i ) ) T \displaystyle=\tilde{\Sigma}^{(i)}-H\mu^{(i)}(\mu^{(i)})^{T}-\mu^{(i)}H(\mu^{(i)})^{T}+H\mu^{(i)}(\mu^{(i)})^{T} = Σ ~ ( i ) − 2 ​ H ​ μ ( i ) ​ ( μ ( i ) ) T + H ​ μ ( i ) ​ ( μ ( i ) ) T \displaystyle=\tilde{\Sigma}^{(i)}-2H\mu^{(i)}(\mu^{(i)})^{T}+H\mu^{(i)}(\mu^{(i)})^{T} = Σ ~ ( i ) − H ​ μ ( i ) ​ ( μ ( i ) ) T . \displaystyle=\tilde{\Sigma}^{(i)}-H\mu^{(i)}(\mu^{(i)})^{T}. Inverting Σ ( i ) \Sigma^{(i)} , we conclude that Σ ( i ) − 1 \displaystyle\Sigma_{(i)}^{-1} = ( Σ ~ ( i ) − H ​ μ ( i ) ​ μ ( i ) T ) − 1 \displaystyle=\left(\tilde{\Sigma}^{(i)}-H\mu^{(i)}\mu_{(i)}^{T}\right)^{-1} = Σ ~ ( i ) − 1 − ( Σ ~ ( i ) − 1 ​ μ ( i ) ​ μ ( i ) T ​ Σ ~ ( i ) − 1 − 1 / H + μ ( i ) T Σ ~ ( i ) − 1 μ ( i ) ) , \displaystyle=\tilde{\Sigma}_{(i)}^{-1}-\left(\frac{\tilde{\Sigma}_{(i)}^{-1}\mu_{(i)}\mu_{(i)}^{T}\tilde{\Sigma}_{(i)}^{-1}}{-1/H+\mu_{(i)}^{T}\tilde{\Sigma}_{(i)}^{-1}\mu^{(i)}}\right), where we used the Woodbury matrix identity lemma 7 7 7 https://en.wikipedia.org/wiki/Woodbury_matrix_identity in the last step with U = μ ( i ) U=\mu^{(i)} , C = − H C=-H , and V = μ ( i ) T V=\mu_{(i)}^{T} . ∎

We exclude representations from the current sequence i i in Σ ( i ) \Sigma^{(i)} to keep the generation from veering off topic, and update Σ ( i ) − 1 \Sigma^{-1}_{(i)} after each generation i i using T i T_{i} consecutive applications of the Sherman-Morrison update in Algorithm 1 , one for each hidden representation of the output tokens. Finally, we found it necessary for numerical stability to perform all covariance related computations in double precision.

#### Additional plots

In Fig. 10 , we provide a revised version of Fig. 7 where we add shaded areas indicating one standard error to the left plot, and we additionally add β = 0.5 \beta=0.5 to the right plot.

## Appendix C Details for RL Post-Training Experiments ( Section 5 )

#### Hyperparameters

We use verl for training ( Sheng et al., 2024 ) , and provide a full overview of all common hyperparameters in Table 3 , all hyperparameters specific to unlikeliness in Table 3 , and all hyperpameters specific to RepExp in Table 3 . Note that for AIME 2024 , we adjusted the maximum prompt length to 2048, the maximum response length to 8192, the train batch size to 512, the ppo mini batch size to 128, and the ppo micro batch size per gpu to 8. Also, for RepExp on AIME 2024 , we increased the sparse projection dimension from 32 to 128.

#### Algorithm details

We note that we mean-center the representations h ¯ θ \bar{h}_{\theta} that are used to compute the elliptic bonuses as described in Section 3 , where the mean is taken over all the response-level representations of the current group of rollouts for a fixed prompt x x . In addition, we do not add a bonus for questions where all rollouts in the batch are incorrect, as we found this to empirically hurt performance.

#### Dataset splits

For MATH , we use the original 7.5k train split for training, MATH-500 ( Lightman et al., 2023 ) for validation, and the 4.5k (originally 5k minus the problems in MATH-500 )) test split for testing. For GSM8K, we use the original 8.79k train split for training, the first 512 512 examples from the test split for validation, and the remaining 807 807 examples from the test split for testing. Finally for AIME 2024 , we use 4096 4096 examples randomly chosen from the full DAPO-Math-17K dataset for training and use the full AIME 2024 dataset both for validation and testing.

#### Modifications to unlikeliness baseline

The original unlikeliness method from He et al. (2025) combines the reward modification described in Section 5 along with several other modifications to the underlying GRPO mechanics: • They only include samples for which the resulting rollouts have nonzero advantages in the batch sent for training. Specifically, questions where either none of the rollouts are correct or all of the rollouts are correct are thrown out. To ensure batch sizes stay roughly equal, the authors implement a buffer mechanism that collects samples until the buffer reaches a target batch size.

• They increase the number of ppo epochs from 1 1 to 2 2 as they find this helps further increase the pass@k.

• They use a high KL penalty coefficient of 0.1 as they find this helps prevent the pass@k from decreasing.

Since our primary aim in this section is to isolate and compare the exploration mechanisms of our method with others, we leave out the additional changes described above when running the unlikeliness baseline. Furthermore, this allows us to use the exact same underlying GRPO hyperparameters for all methods, making the comparison much more clean.

#### Checkpoint picking

For each seed per method, we pick the checkpoint during training that achieves the highest pass@1 on the respective task’s validation set and use the resulting checkpoint for evaluation.

#### Evaluation

We evaluate each final checkpoint (picked in the way described earlier) on the test split of each respective task by sampling 256 responses per question using vanilla sampling parameters ( τ = 1.0 \tau=1.0 , top-p = 1.0 \text{top-p}=1.0 ). We then estimate the pass@k exactly as described in Section B.1 . We run 3 3 seeds for all methods on all tasks and average the resulting pass@k curves. In addition, we provide an alternative view of Fig. 2 in Fig. 11 .

#### Experiment resources

We run all methods on all tasks using 8 NVIDIA H100 80GB GPUs per seed per method for 1 1 day.

#### Computational overhead

On MATH , we estimated RepExp to reach about 0.73 0.73 x the steps/hour throughput of GRPO. In other words, RepExp requires about 1.37 1.37 x higher wall-clock time per step. Note that this overhead comes from an extra forward pass that’s required to compute the hidden representations of the sampled responses at each iteration of the algorithm. However, if either (1) one were to use a KL constraint (which we do not in our experiments) or (2) one were to use the hidden representations from π t \pi_{t} (the current policy iterate) instead of π ref \pi_{\mathrm{ref}} (the base model), then the extra forward pass would not be needed and RepExp would have the same throughput as GRPO.

## Appendix D Beyond Sharpening: Full Results

In Fig. 12 , we provide results for both MATH and GSM8K . We find that on GSM8K the shift toward lower likelihood responses from RepExp as evaluated under the base model is even more dramatic.

## Instructions for reporting errors

We are continuing to improve HTML versions of papers, and your feedback helps enhance accessibility and mobile support. To report errors in the HTML that will help us improve conversion and rendering, choose any of the methods listed below:

Click the "Report Issue" ( ) button, located in the page header.

Tip: You can select the relevant text first, to include it in your report.

Our team has already identified the following issues . We appreciate your time reviewing and reporting rendering errors we may not have found yet. Your efforts will help us improve the HTML versions for all readers, because disability should not be a barrier to accessing research. Thank you for your continued support in championing open access for all.

Have a free development cycle? Help support accessibility at arXiv! Our collaborators at LaTeXML maintain a list of packages that need conversion , and welcome developer contributions .
