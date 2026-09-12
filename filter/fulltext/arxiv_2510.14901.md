##### Report GitHub Issue

Content selection saved. Describe the issue below:

# Reasoning with Sampling: Your Base Model is Smarter Than You Think

###### Abstract

Frontier reasoning models have exhibited incredible capabilities across a wide array of disciplines, driven by posttraining large language models (LLMs) with reinforcement learning (RL). However, despite the widespread success of this paradigm, much of the literature has been devoted to disentangling truly novel behaviors that emerge during RL but are not present in the base models. In our work, we approach this question from a different angle, instead asking whether comparable reasoning capabilites can be elicited from base models at inference time by pure sampling , without any additional training . Inspired by Markov chain Monte Carlo (MCMC) techniques for sampling from sharpened distributions, we propose a simple iterative sampling algorithm leveraging the base models’ own likelihoods. Over different base models, we show that our algorithm offers substantial boosts in reasoning that nearly match and even outperform those from RL on a wide variety of single-shot tasks, including MATH500, HumanEval, and GPQA. Moreover, our sampler avoids the collapse in diversity over multiple samples that is characteristic of RL-posttraining. Crucially, our method does not require training, curated datasets, or a verifier, suggesting broad applicability beyond easily verifiable domains.

## 1 Introduction

Reinforcement learning (RL) has become the dominant paradigm for enhancing the reasoning capabilities of large language models (LLMs) ( Guo et al., 2025 ; Hu et al., 2025 ) . Equipped with a reward signal that is typically automatically verifiable, popular RL techniques have been successfully applied to posttrain frontier models, leading to sizeable performance gains in domains like math, coding, and science ( Hendrycks et al., 2021 ; Li et al., 2022 ; Rein et al., 2024 ) .

Despite the widespread empirical success of RL for LLMs, a large body of literature has centered around the following question: are the capabilities that emerge during RL-posttraining fundamentally novel behaviors that are not present in the base models? This is the question of distribution sharpening ( He et al., 2025 ; Shao et al., 2025 ; Yue et al., 2025 ) : that is, whether the posttrained distribution is simply a “sharper” version of the base model distribution, instead of placing mass on reasoning traces the base model is unlikely to generate.

Several works point towards the difficulty in learning new capabilities with RL-posttraining. He et al. (2025) ; Song et al. (2025) compare the pass@ k k (multi-shot) scores of base models with posttrained models, finding that for large k k , base models actually outperform while the latter suffer from degraded generation diversity. In such cases, RL appears to redistribute pass@ k k performance to single-shot performance at the expense of multi-shot reasoning. Yue et al. (2025) also notes that the reasoning traces post-RL are tightly concentrated at high likelihoods/confidences under the base model, seemingly drawing from existing high-likelihood capabilities. We illustrate this point in our own experiments in Figure 4 . Regardless, the advantage of RL-posttraining for single-shot reasoning has remained, as of yet, undeniable.

In this paper, we present a surprising result: sampling directly from the base model can achieve single-shot reasoning capabilites on par with those from RL .

We propose a sampling algorithm for base models that leverages additional compute at inference time, achieving single-shot performance that nearly matches RL-posttraining on in-domain reasoning tasks and can even outperform on out-of-domain reasoning tasks. Furthermore, we observe that generation diversity does not degrade with our sampler; in fact, our pass@ k k (multi-shot) performance strongly outperforms RL. We benchmark specifically against Group Relative Policy Optimization (GRPO), which is the standard RL algorithm for enhancing LLM reasoning ( Shao et al., 2024 ) .

Crucially, our algorithm is training-free , dataset-free , and verifier-free , avoiding some of the inherent weaknesses of RL methods including extensive hyperparameter sweeps to avoid training instabilities, the need to curate a diverse and expansive posttraining dataset, and the lack of guaranteed access to a ground truth verifier/reward signal ( Prabhudesai et al., 2025 ) .

Our contributions can be summarized as follows: i) We introduce the power distribution as a useful sampling target for reasoning tasks. Since it can be explicitly specified with a base LLM, no additional training is required.

ii) We further introduce an approximate sampling algorithm for the power distribution using a Markov chain Monte Carlo (MCMC) algorithm that iteratively resamples token subsequences according to their base model likelihoods.

iii) We empirically demonstrate the effectiveness of our algorithm over a range of models (Qwen2.5-Math-7B, Qwen2.5-7B, Phi-3.5-mini-instruct) and reasoning tasks (MATH500, HumanEval, GPQA, AlpacaEval 2.0). Our results show that sampling directly from the base model can achieve results on par with GRPO. In fact, for some out-of-domain tasks, our algorithm consistently outperforms the RL baseline. Moreover, over multiple samples, we avoid the collapse in diversity afflicting RL-posttraining, achieving the best of both worlds in terms of single-to-few-shot reasoning capabilities as well as sample diversity.

Our results collectively illustrate that existing base models are much more capable at single-shot reasoning than current sampling methods reveal.

## 2 Related Works

#### Reinforcement learning for LLMs.

RL has been instrumental in posttraining LLMs. Early on, RL with human feedback (RLHF) ( Ouyang et al., 2022 ) was developed as a technique to align LLMs with human preferences using a trained reward model. Recently, RL with verifiable rewards (RLVR) has emerged as a powerful new posttraining technique, where many works ( Guo et al., 2025 ; Lambert et al., 2024 ; Hu et al., 2025 ; Zeng et al., 2025 ) discovered that a simple, end-of-generation reward given by an automated verifier could substantially enhance performance on difficult reasoning tasks in mathematics and coding. The Group Relative Policy Optimization (GRPO) algorithm was at the center of these advances ( Shao et al., 2024 ) . Building off of this success, many subsequent works have examined using reward signals derived from internal signals such as self-entropy ( Zhao et al., 2025 ) , confidence ( Prabhudesai et al., 2025 ) , and even random rewards ( Shao et al., 2025 ) . Similar to these works, our paper examines base model likelihoods as a mechanism for improving reasoning performance, but crucially, our technique is training-free .

#### Autoregressive MCMC sampling with LLMs.

Prior works have explored integrating classic MCMC techniques with autoregressive sampling. Many settings including red-teaming, prompt-engineering, and personalized generation can be framed as targeting sampling from the base LLM distribution but tilted towards an external reward function. Zhao et al. (2024) proposes learning intermediate value functions that are used in a Sequential Monte Carlo (SMC) framework ( Chopin, 2004 ) , where multiple candidate sequences are maintained and updated according to their expected future reward. Similarly, Faria et al. (2024) proposes a Metropolis-Hastings (MH) algorithm, which instead of maintaining multiple candidates performs iterative resampling, again updating according to expected reward. Methodologically, our sampling algorithm is most similar to this latter work, but the crucial difference is that our target sampling distribution is completely specified by the base LLM, avoiding the need for an external reward .

#### Annealed sampling for diffusion.

In the statistical physics and Monte Carlo literature, sampling from p α p^{\alpha} is known as sampling from an annealed , or tempered , distribution ( Neal, 1998 ) and has inspired a new wave of interest within the diffusion community. Indeed, in traditional MCMC sampling, annealing is used as a way to avoid mode-collapse during sampling and more accurately sample from complex multimodal distributions ( Łatuszyński et al., 2025 ) . This has re-emerged as inference-time sampling methods for diffusion that aim to steer a pretrained model towards “tilted distributions” ( Du et al., 2023 ; Kim et al., 2025 ; Karan et al., 2025 ; Wang et al., 2025 ; Kong et al., 2025 ; Zhang et al., 2025 ) . Where traditional RL techniques exhibit mode collapse, applications in the physical sciences ( Sambridge, 2014 ) require multimodal sampling. To this end, works such as Du et al. (2023) ; Wang et al. (2025) ; Kim et al. (2025) construct sequences of annealed distributions to ease the transition from base diffusion distribution to tilted distribution. Other works ( Skreta et al., 2025 ; Xu et al., 2025 ) intentionally target sampling from p α p^{\alpha} for α > 1 \alpha>1 as a means of generating higher quality samples from the base diffusion model, which is particularly popular for generating more designable proteins ( Geffner et al., 2025 ) .

## 3 Preliminaries

Let 𝒳 \mathcal{X} be a finite vocabulary of tokens, and let 𝒳 T \mathcal{X}^{T} denote the set of finite sequences of tokens x 0 : T = ( x 0 , x 1 , … , x T ) x_{0:T}=(x_{0},x_{1},\dots,x_{T}) , where x i ∈ 𝒳 x_{i}\in\mathcal{X} for all i i and T ∈ ℤ ≥ 0 T\in\mathbb{Z}_{\geq 0} is some nonnegative integer. For convenience, for a given t t , let x < t = ( x 0 , … , x t − 1 ) x_{<t}=(x_{0},\dots,x_{t-1}) and x > t = ( x t + 1 , … , x T ) x_{>t}=(x_{t+1},\dots,x_{T}) , with similar definitions for x ≤ t x_{\leq t} and x ≥ t x_{\geq t} . In general, 𝐱 \mathbf{x} refers to a token sequence x 0 : T x_{0:T} , where T T is implicitly given.

Then an LLM defines a distribution p p over token sequences 𝒳 T \mathcal{X}^{T} by autoregressively learning the conditional token distributions p ⁡ ( x t | x < t ) p(x_{t}|x_{<t}) for all t t , giving the joint distribution via the identity p ( x 0 : T ) = ∏ t = 0 T p ( x t | x < t ) . p(x_{0:T})=\prod_{t=0}^{T}p(x_{t}|x_{<t}). (1)

To sample a sequence from p p , we simply sample from the LLM token by token using the conditional distributions, which by ( 1 ) directly samples from the joint distribution.

## 4 MCMC Sampling for Power Distributions

In this section, we introduce our sampling algorithm for base models. Our core intuition is derived from the notion of distribution sharpening posed in Section 1 . Sharpening a reference distribution refers to reweighting the distribution so that high likelihood regions are further upweighted while low likelihood regions are downweighted, biasing samples heavily towards higher likelihoods under the reference. Then if RL posttrained models really are just sharpened versions of the base model, we should be able to explicitly specify a target sampling distribution that achieves the same effect.

We organize this section as follows. Section 4.1 presents this target sharpened distribution and provides some mathematical motivation for why its samples are amenable for reasoning tasks. Section 4.2 introduces a general class of Markov chain Monte Carlo (MCMC) algorithms aimed at actually sampling from this target distribution, and finally, Section 4.3 details our specific implementation for LLMs.

### 4.1 Reasoning with Power Distributions

One natural way to sharpen a distribution p p is to sample from the power distribution p α p^{\alpha} . Since p ⁡ ( 𝐱 ) > p ⁡ ( 𝐱 ′ ) ⟹ p ​ ( 𝐱 ) α p ​ ( 𝐱 ′ ) α > p ⁡ ( 𝐱 ) p ⁡ ( 𝐱 ′ ) ( α ∈ [ 1 , ∞ ] ) , p(\mathbf{x})>p(\mathbf{x^{\prime}})\implies\frac{p(\mathbf{x})^{\alpha}}{p(\mathbf{x^{\prime}})^{\alpha}}>\frac{p(\mathbf{x})}{p(\mathbf{x^{\prime}})}\qquad(\alpha\in[1,\infty]), (2) it follows that exponentiating p p increases the relative weight on higher likelihood sequences ( 𝐱 \mathbf{x} ) while decreasing the relative weight on lower likelihood ones ( 𝐱 ′ \mathbf{x^{\prime}} ) (see Figure 2 for a visualization).

A related but well-known sharpening strategy is low-temperature sampling ( Wang et al., 2020 ) , which exponentiates the conditional next-token distributions at each step: p temp ​ ( x t | x 0 ​ … ​ x t − 1 ) = p ​ ( x t | x t − 1 ​ … ​ x 0 ) α ∑ x t ′ ∈ 𝒳 p ​ ( x t ′ | x t − 1 ​ … ​ x 0 ) α , p_{\text{temp}}(x_{t}|x_{0}\dots x_{t-1})=\frac{p(x_{t}|x_{t-1}\dots x_{0})^{\alpha}}{\sum_{x_{t}^{\prime}\in\mathcal{X}}p(x_{t}^{\prime}|x_{t-1}\dots x_{0})^{\alpha}}, (3) where the temperature is τ = 1 / α \tau=1/\alpha . A common misconception is that sampling with ( 3 ) over T T tokens is equivalent to sampling from p α p^{\alpha} ; however, this is false in a subtle yet crucial way, as we illuminate in the following.

###### Proposition 1 .

Low-temperature sampling does not sample from the power distribution p α p^{\alpha} .

###### Proof.

We show that the associated conditional next-token distributions are distinct at each timestep t t . The conditional distribution on x t x_{t} for p α p^{\alpha} is given by p pow ​ ( x t | x 0 ​ … ​ x t − 1 ) = ∑ x > t p ​ ( x 0 , … , x t , … , x T ) α ∑ x ≥ t p ​ ( x 0 , … , x t , … , x T ) α . p_{\text{pow}}(x_{t}|x_{0}\dots x_{t-1})=\frac{\sum_{x_{>t}}p(x_{0},\dots,x_{t},\dots,x_{T})^{\alpha}}{\sum_{x_{\geq t}}p(x_{0},\dots,x_{t},\dots,x_{T})^{\alpha}}. (4)

Using Bayes rule p ⁡ ( x t | x t − 1 ​ … ​ x 0 ) = p ⁡ ( x 0 , … , x t ) p ⁡ ( x 0 , … , x t − 1 ) = ∑ x > t p ⁡ ( x 0 , … , x t , … , x T ) ∑ x ≥ t p ⁡ ( x 0 , … , x t , … , x T ) , p(x_{t}|x_{t-1}\dots x_{0})=\frac{p(x_{0},\dots,x_{t})}{p(x_{0},\dots,x_{t-1})}=\frac{\sum_{x_{>t}}p(x_{0},\dots,x_{t},\dots,x_{T})}{\sum_{x_{\geq t}}p(x_{0},\dots,x_{t},\dots,x_{T})}, (5) we can rewrite the low-temperature marginal ( 3 ) as p temp ​ ( x t | x 0 ​ … ​ x t − 1 ) = ( ∑ x > t p ⁡ ( x 0 , … , x t , … , x T ) ) α ∑ x t ′ ( ∑ x > t p ⁡ ( x 0 , … , x t , … , x T ) ) α . p_{\text{temp}}(x_{t}|x_{0}\dots x_{t-1})=\frac{\left(\sum_{x_{>t}}p(x_{0},\dots,x_{t},\dots,x_{T})\right)^{\alpha}}{\sum_{x_{t}^{\prime}}\left(\sum_{x_{>t}}p(x_{0},\dots,x_{t},\dots,x_{T})\right)^{\alpha}}. (6)

Ignoring normalizations for clarity, the relative weight on token x t x_{t} for sampling from p α p^{\alpha} is given by a sum of exponents p pow ​ ( x t | x < t ) ∝ ∑ x > t p ​ ( x 0 , … , x t , … , x T ) α . p_{\text{pow}}(x_{t}|x_{<t})\propto\sum_{x_{>t}}p(x_{0},\dots,x_{t},\dots,x_{T})^{\alpha}. (7) Meanwhile, the relative weight for low-temperature sampling is given by an exponent of sums p temp ​ ( x t | x < t ) ∝ ( ∑ x > t p ⁡ ( x 0 , … , x t , … , x T ) ) α . p_{\text{temp}}(x_{t}|x_{<t})\propto\left(\sum_{x_{>t}}p(x_{0},\dots,x_{t},\dots,x_{T})\right)^{\alpha}. (8) Since the relative weights of next-token prediction are distinct for each sampling strategy, it follows that the joint distribution over seqeunces must also be distinct for each sampler. Hence, the distribution on sequences given by low-temperature sampling is not the same as the one given by p α p^{\alpha} . ∎

One intuitive way to understand this difference is that low-temperature sampling does not account for how exponentiation sharpens the likelihoods of “future paths” at time step t t , instead “greedily” averaging all these future likelihoods ( exponent of sums ( 8 )). On the other hand, sampling from p α p^{\alpha} inherently accounts for future completions as it exponentiates all future paths ( sum of exponents ( 7 )) before computing the weights for next-token prediction. This has the following consequence:

###### Observation 1 .

The power distribution upweights tokens with few but high likelihood future paths, while low-temperature sampling upweights tokens with several but low likelihood completions.

###### Example 1 .

We can observe this phenomenon with a simple example. Let us consider the token vocabulary 𝒳 = { a , b } \mathcal{X}=\{a,b\} and restrict our attention to two-token sequences ( x 0 , x 1 ) (x_{0},x_{1}) : a ​ a , a ​ b , b ​ a , b ​ b aa,ab,ba,bb . Let p ⁡ ( a ​ a ) = 0.00 , p ⁡ ( a ​ b ) = 0.40 , p ⁡ ( b ​ a ) = 0.25 , p ⁡ ( b ​ b ) = 0.25 , p(aa)=0.00,\qquad p(ab)=0.40,\qquad p(ba)=0.25,\qquad p(bb)=0.25, so that p ⁡ ( x 0 = a ) = 0.40 , p ⁡ ( x 0 = b ) = 0.50 . p(x_{0}=a)=0.40,\qquad p(x_{0}=b)=0.50.\qquad Let α = 2.0 \alpha=2.0 . Under p α p^{\alpha} , we have p pow ​ ( x 0 = a ) ∝ 0.00 2 + 0.40 2 = 0.160 , p pow ​ ( x 0 = b ) ∝ 0.25 2 + 0.25 2 = 0.125 , p_{\text{pow}}(x_{0}=a)\propto 0.00^{2}+0.40^{2}=0.160,\qquad p_{\text{pow}}(x_{0}=b)\propto 0.25^{2}+0.25^{2}=0.125, so p α p^{\alpha} prefers sampling a a over b b . Under low-temperature sampling, p temp ​ ( x 0 = a ) ∝ ( 0.00 + 0.40 ) 2 = 0.160 , p temp ​ ( x 0 = b ) ∝ ( 0.25 + 0.25 ) 2 = 0.250 , p_{\text{temp}}(x_{0}=a)\propto(0.00+0.40)^{2}=0.160,\qquad p_{\text{temp}}(x_{0}=b)\propto(0.25+0.25)^{2}=0.250, preferring sampling b b over a a . If p α p^{\alpha} samples x 0 = a x_{0}=a , there is only one future path with likelihood 0.40 0.40 . If p temp p_{\text{temp}} samples x 0 = b x_{0}=b , there are two future paths b ​ a , b ​ b ba,bb , but either choice has likelihood 0.25 0.25 .

In other words, even though a a has lower conditional likelihood under both p p and p temp p_{\text{temp}} , p α p^{\alpha} upweights a a and samples the highest likelihood two-token sequence. b b has many future paths contributing to a higher likelihood under p p and p temp p_{\text{temp}} , but leads to low likelihood sequences. We provide a stronger formalization of this phenomenon in Appendix A.1 .

Thus, sampling from p α p^{\alpha} encourages sampling tokens which have fewer but higher likelihood “future paths”, as opposed to tokens with several lower likelihood completions. This type of behavior is immensely valuable for reasoning tasks. For example, choosing “wrong” tokens that have high average likelihoods but trap outputs in low likelihood individual futures are examples of critical windows or pivotal tokens ( Li et al., 2025 ; Abdin et al., 2024 ) , a phenomenon where a few tokens are highly influential in the correctness of language model outputs. In fact, sharp critical windows have been shown to correlate strongly with reasoning failures ( Li et al., 2025 ) . Instead, embedded in sampling from the power distribution is an implicit bias towards planning for future high likelihood tokens.

### 4.2 The Metropolis-Hastings Algorithm

Now that we have seen how sampling from p α p^{\alpha} can in theory assist the underlying LLM’s ability to reason, our aim now turns towards proposing an algorithm to accurately sample from it. Given an LLM p p , we have access to the values p α p^{\alpha} over any sequence length; however, these values are unnormalized . Direct sampling from the true probabilities requires normalizing over all sequences ( x 0 , … , x T ) ∈ 𝒳 T (x_{0},\dots,x_{T})\in\mathcal{X}^{T} , which is computationally intractable.

To get around this, we invoke a Markov Chain Monte Carlo (MCMC) algorithm known as Metropolis-Hastings (MH) ( Metropolis et al., 1953 ) , which targets exactly what we want: approximate sampling from an unnormalized probability distribution. The MH algorithm constructs a Markov chain of sample sequences ( 𝐱 0 , 𝐱 1 , … , 𝐱 n ) (\mathbf{x}^{0},\mathbf{x}^{1},\dots,\mathbf{x}^{n}) using an arbitrary proposal distribution q ⁡ ( 𝐱 | 𝐱 i ) q(\mathbf{x}|\mathbf{x}^{i}) to select the next candidate 𝐱 i + 1 \mathbf{x}^{i+1} . With probability A ⁡ ( 𝐱 , 𝐱 i ) = min ​ { 1 , p α ​ ( 𝐱 ) ⋅ q ⁡ ( 𝐱 i | 𝐱 ) p α ​ ( 𝐱 i ) ⋅ q ⁡ ( 𝐱 | 𝐱 i ) } , A(\mathbf{x},\mathbf{x}^{i})=\text{min}\left\{1,\frac{p^{\alpha}(\mathbf{x})\cdot q(\mathbf{x}^{i}|\mathbf{x})}{p^{\alpha}(\mathbf{x}^{i})\cdot q(\mathbf{x}|\mathbf{x}^{i})}\right\}, (9)

candidate 𝐱 \mathbf{x} is accepted as 𝐱 i + 1 \mathbf{x}^{i+1} ; otherwise, MH sets 𝐱 i + 1 = 𝐱 i \mathbf{x}^{i+1}=\mathbf{x}^{i} . This algorithm is especially convenient as it only requires the relative weights given by p α p^{\alpha} (as the normalization weights in A A cancel) and works with any generic but tractable sampler q q with minimal restrictions. Remarkably, for large enough n n , this process converges to sampling from the target distribution p α p^{\alpha} under the following (quite minimal) conditions on the proposal distribution ( Neal, 1993 ) :

###### Definition 1 .

The proposal distribution q q is irreducible if for any set X X with nonzero mass under the target distribution p α p^{\alpha} , q q has nonzero probability of eventually sampling from X X . The proposal is aperiodic if the induced chain of samples does not return to the same sample after a fixed interval number of steps.

Thus, we must simply ensure that our proposal distribution satisfies irreducibility and aperiodicity, and Metropolis-Hastings takes care of the rest. On a practical level, we would also like both q ⁡ ( 𝐱 | 𝐱 i ) q(\mathbf{x}|\mathbf{x}^{i}) and its reverse q ⁡ ( 𝐱 i | 𝐱 ) q(\mathbf{x}^{i}|\mathbf{x}) to be easily computable.

Consider the following family of random resampling proposal distributions (see Figure 3 ). Let p prop p_{\text{prop}} be a proposal LLM. With uniform probability 1 T \frac{1}{T} , select a random t ∈ [ 1 , T ] t\in[1,T] and resample the sequence starting at index t t using p prop p_{\text{prop}} . Then the transition likelihood q ⁡ ( 𝐱 | 𝐱 i ) q(\mathbf{x}|\mathbf{x}^{i}) is simply the likelihood of the resampling. Note that at each candidate selection step, we have a nonzero probability of transitioning between any two sequences 𝐱 , 𝐱 ′ ∈ 𝒳 \mathbf{x},\mathbf{x^{\prime}}\in\mathcal{X} , since with some probability we can always resample as early as the beginning of 𝐱 \mathbf{x} . This ensures our proposal distribution is both irreducible and aperiodic. Moreover, q ⁡ ( 𝐱 i | 𝐱 ) q(\mathbf{x}^{i}|\mathbf{x}) is easy to calculate by symmetry, since we can treat 𝐱 i \mathbf{x}^{i} as a resampled version of 𝐱 \mathbf{x} .

With the flexibility endowed by Metropolis-Hastings, we can choose the proposal LLM p prop p_{\text{prop}} to be any LLM with any sampling strategy (e.g., low-temperature sampling).

### 4.3 Power Sampling with Autoregressive MCMC

A direct implementation of Metropolis-Hastings for LLMs would involve initializing with a sampled token sequence of length T T , subsequently generating new candidates of length T T with ( 9 ) over many, many iterations. This process is computationally expensive, however, due to the repeated, full sequence inference calls to the LLM.

In fact, the main downside to MCMC algorithms in practice is the potential for an exponential mixing time ( Gheissari et al., 2017 ) , where a poor choice of initialization or proposal distribution can result in an exponentially large number of samples required before convergence to the target distribution. This problem is exacerbated if the sample space has high dimensionality ( Bandeira et al., 2022 ; Schmidler and Woodard, 2013 ) , which is precisely exhibited by the sequence space of tokens 𝒳 T \mathcal{X}^{T} , especially for long sequences/large values of T T .

To remedy this, we propose an algorithm that leverages the sequential structure of autoregressive sampling. We define a series of intermediate distributions which we progressively sample from, until converging to the target distribution p α p^{\alpha} . In particular, samples from one intermediate distribution initiate a Metropolis-Hastings process for the next, helping avoid pathological initializations.

Fix block size B B and proposal LLM p prop p_{\text{prop}} , and consider the sequence of (unnormalized) distributions ∅ ⟶ p ​ ( x 0 , … , x B ) α ⟶ p ​ ( x 0 , … , x 2 ​ B ) α ⟶ … ⟶ p ​ ( x 0 , … , x T ) α , \emptyset\longrightarrow p(x_{0},\dots,x_{B})^{\alpha}\longrightarrow p(x_{0},\dots,x_{2B})^{\alpha}\longrightarrow\dots\longrightarrow p(x_{0},\dots,x_{T})^{\alpha}, (10) where p ⁡ ( x 0 , … , x k ​ B ) p(x_{0},\dots,x_{kB}) denotes the joint distribution over token sequences of length k ​ B kB , for any k k . For convenience, let π k \pi_{k} denote the distribution given by π k ( x 0 : k ​ B ) ∝ p ( x 0 : k ​ B ) α . \pi_{k}(x_{0:kB})\propto p(x_{0:kB})^{\alpha}. (11) Suppose we have a sample from π k \pi_{k} . To obtain a sample from π k + 1 \pi_{k+1} , we initialize a Metropolis-Hastings process by sampling the next B B tokens x k ​ B + 1 : ( k + 1 ) ​ B x_{kB+1:(k+1)B} with p prop p_{\text{prop}} . We subsequently run the MCMC sampling procedure for N MCMC N_{\text{MCMC}} steps, using the random resampling proposal distribution q q from the previous section. The full details are presented in Algorithm 1 .

Note that Algorithm 1 is single-shot : even though multiple inference calls are made, the decision to accept vs. reject new tokens is made purely by base model likelihoods to simulate sampling a single sequence from p α p^{\alpha} . We can interpret this as a new axis for inference-time scaling , as we expend additional compute during sampling to obtain a higher quality/likelihood sample.

To quantify the scaling, we can estimate the average number of tokens generated by Algorithm 1 . Note that each candidate generation step when sampling from π k ( x 0 : k ​ B \pi_{k}(x_{0:kB} resamples an average of k ​ B 2 \frac{kB}{2} tokens, N MCMC N_{\text{MCMC}} times. Summing over all k k , the expected number of tokens generated is 𝔼 tokens = N MCMC ​ ∑ k = 1 ⌈ T / B ⌉ k ​ B 2 ≈ N MCMC ​ T 2 4 ​ B . \mathbb{E}_{\text{tokens}}=N_{\text{MCMC}}\sum_{k=1}^{\lceil T/B\rceil}\frac{kB}{2}\approx\frac{N_{\text{MCMC}}T^{2}}{4B}. (12) The key tradeoff here is between the block size B B and number of MCMC steps N MCMC N_{\text{MCMC}} . A larger B B requires larger “jumps” between intermediate distributions, requiring a larger N MCMC N_{\text{MCMC}} to adequately transition. In Section 5 , we empirically find a value for B B that makes Algorithm 1 performant for relatively small values of N MCMC N_{\text{MCMC}} .

## 5 Experiments

### 5.1 Experimental Setup

#### Evaluation.

We use a standard suite of reasoning benchmarks ranging across mathematics, coding, and STEM (MATH500, HumanEval, GPQA), along with a non-verifiable benchmark (AlpacaEval 2.0) evaluating general helpfulness. We evaluate all of our methods and baselines single-shot ; i.e., on one final response string.

• MATH500 : The MATH dataset ( Lightman et al., 2024 ) consists of competition math problems spanning seven categories including geometry, number theory, and precalculus. There are 12500 problems total, with 7500 training problems and 5000 test problems. MATH500 is a specific randomly chosen subset of the test set standardized by OpenAI.

• HumanEval : HumanEval is a set of 164 handwritten programming problems covering algorihtms, reasoning, mathematics, and language comprehension ( Chen et al., 2021 ) . Each problem has an average of 7.7 associated unit tests, where solving the problem corresponds to passing all unit tests.

• GPQA : GPQA ( Rein et al., 2024 ) is a dataset of multiple-choice science questions (physics, chemistry, and biology) which require advanced reasoning skills to solve. We use subset GPQA Diamond for evaluation, which consists of 198 questions which represent the highest quality subset of the GPQA dataset.

• AlpacaEval 2.0 : The AlpacaEval dataset is a collection of 805 prompts ( Dubois et al., 2024 ) that gauge general helpfulness with questions asking e.g., for movie reviews, recommendations, and reading emails. The model responses are graded by an automated LLM judge (GPT-4-turbo), which determines a preference for the model responses over those from a baseline (also GPT-4-turbo). The resulting score is a win rate of model responses normalized for the length of the model response.

#### Models.

To demonstrate the efficacy of our sampling algorithm, we use the base models Qwen2.5-Math-7B, Qwen2.5-7B, and Phi-3.5-mini-instruct. For our RL baselines, we use the implementation of GRPO in Shao et al. (2025) , which posttrains these models on the MATH training split. For both the Qwen2.5 models, we use the default hyperparameters used to benchmark their performance in Shao et al. (2025) . For the Phi-3.5 model, we use a set of hyperparameters selected from Abdin et al. (2024) that avoids training instabilities and converges to improvement over the base model over a large number of epochs.

#### Sampling Algorithm.

For our implementation of power sampling (Algorithm 1 ), we set the maximum T T to be T max = 3072 T_{\text{max}}=3072 (termination can happen earlier with an EOS token) and block size B = 3072 / 16 = 192 B=3072/16=192 . Empirically, we find α = 4.0 \alpha=4.0 coupled with a proposal LLM p prop p_{\text{prop}} chosen as the base model with sampling temperature 1 / α 1/\alpha to be most performant for reasoning tasks. For AlpacaEval 2.0, we find that having a proposal distribution of higher temperature ( τ = 0.5 \tau=0.5 ) improves performance.

### 5.2 Results

#### Main results.

We display our main results in Table 1 . Across base models of different families, our sampling algorithm achieves massive, near-universal boosts in single-shot accuracies and scores over different reasoning and evaluation tasks that reach, e.g., up to +51.9% on HumanEval with Phi-3.5-mini and +25.2% on MATH500 with Qwen2.5-Math. In particular, on MATH500, which is in-domain for RL-posttraining, power sampling achieves accuracies that are on par with those obtained by GRPO. Furthermore, on out-of-domain reasoning, our algorithm again matches GRPO on GPQA and actually outperforms on HumanEval by up to +59.8% . Similarly, power sampling consistently outperforms on the non-verifiable AlpacaEval 2.0, suggesting a generalizability of our boosts to domains beyond verifiability.

The surprising success of this fundamentally simple yet training-free sampling algorithm underscores the latent reasoning capabilities of existing base models.

### 5.3 Analysis

We analyze how the reasoning characteristics of power sampling relate to those of GRPO. We present an example in Table 2 , with further examples in Appendix A.3 .

#### Reasoning trace likelihoods and confidences.

By design, power sampling targets sampling higher likelihood sequences from the base model. In Figure 4 , the left graph plots a histogram of the output sequence log-likelihoods (averaged by length) of the base model, power sampling, and GRPO responses on MATH500, where likelihoods are taken relative to the Qwen2.5-Math-7B base model. Our method samples from higher likelihood regions of the base model, as intended, but still maintains noticeable spread. Meanwhile, GRPO samples are heavily concentrated at the highest likelihood peak.

We also plot the base model confidence of MATH500 responses, defined to be the average negative entropy ( uncertainty ) of the next-token distributions ( Prabhudesai et al., 2025 ) : Conf ( x 0 : T ) = 1 T + 1 ∑ t = 0 T ∑ x ∈ 𝒳 p ( x | x < t ) log p ( x | x < t ) . \text{Conf}(x_{0:T})=\frac{1}{T+1}\sum_{t=0}^{T}\sum_{x\in\mathcal{X}}p(x|x_{<t})\log{p(x|x_{<t}}). (13) The right plot of Figure 4 demonstrates that our method’s and GRPO responses sample from similarly high confidence regions from the base model, which again correspond to regions of higher likelihood and correct reasoning.

#### Reasoning trace lengths.

Another defining characteristic of RL-posttraining is long-form reasoning ( Guo et al., 2025 ) , where samples tend to exhibit longer responses. On MATH500, Qwen2.5-Math-7B averages a response length of 600 tokens, while GRPO averages 671 tokens. Surprisingly, power sampling achieves a similar average length of 679 tokens, without explicitly being encouraged to favor longer generations. This emerges naturally from the sampling procedure.

#### Diversity and pass@ k k performance.

Again, notice the peaked and highly concentrated likelihoods/confidences of GRPO relative to the distributional spread of power sampling in Figure 4 . This suggests GRPO exhibits a collapse in diversity while our sampler does not, aligning with the observation that RL-posttraining strongly sharpens the base model distribution at the expense of diversity ( Song et al., 2025 ) . To quantify the comparative diversity of power sampling relative to GRPO, we can plot the pass@ k k accuracy rate, where a question is solved if at least one of k k samples is accurate. Figure 5 shows exactly this: unlike GRPO, whose pass@ k k performance tapers off for large k k , power sampling strongly outperforms for k > 1 k>1 . Moreover, our performance curve supersedes that of the base model until finally converging in performance. In particular, we are able to achieve GRPO-level single-shot performance without compromising multi-shot performance (see Appendix A.2 for other domains), addressing a long-standing downside to RL-posttraining.

#### The effect of power distributions.

The two most important hyperparameters for power sampling are the choice of α \alpha and the number of MCMC (resampling) steps during sequence generation N MCMC N_{\text{MCMC}} . At the extremes, choosing α = 1.0 \alpha=1.0 samples from the base model directly, while taking α → ∞ \alpha\to\infty has the effect of deterministically accepting any resampled sequence that strictly increases the likelihood. Of course, even though higher base model likelihoods correlate with better reasoning (Figure 4 ), directly optimizing for likelihood is not necessarily optimal for reasoning, suggesting an ideal intermediate value of α \alpha .

In Figure 6 , we display MATH500 accuracies across various values of α \alpha and find that an intermediate α = 4.0 \alpha=4.0 outperforms other values, as expected. Noticeably, the accuracies of power sampling remain relatively stable beyond α ≥ 2.0 \alpha\geq 2.0 , suggesting that power sampling in practice is relatively robust to the choice of α \alpha .

#### Test-time scaling with MCMC steps.

On the other hand, N MCMC N_{\text{MCMC}} toggles the inference-time compute expended by our algorithm, providing a natural axis for test-time scaling. In Section 4.3 we raised the notion of a mixing time , or the number of MCMC steps required before adequately sampling from the target distribution. In our case, we expect that the fewer MCMC steps we take, the further our algorithm samples from the target p α p^{\alpha} .

We plot performance dependence on N MCMC N_{\text{MCMC}} in Figure 6 and notice a steady increase in accuracy until N MCMC = 10 N_{\text{MCMC}}=10 , beyond which accuracy remains roughly stable (not plotted). The accuracy difference from using fewer MCMC steps is noticeable but no more than 3 3 - 4 % 4\% between N MCMC = 2 N_{\text{MCMC}}=2 and N MCMC = 10 N_{\text{MCMC}}=10 . However, the jump in accuracy by using at least two steps as opposed to none is substantial ( 3 3 - 4 4 %).

We can even compute the total amount of tokens generated by our method relative to running GRPO. From ( 12 ), our sampler generates 1 4 ​ B ⋅ N MCMC ​ T \frac{1}{4B}\cdot{N_{\text{MCMC}}T} times as many tokens as standard inference to generate a sequence of length T T . Plugging in our experimental parameters N MCMC = 10 N_{\text{MCMC}}=10 , T = 679 T=679 (our average output length for MATH500) and B = 192 B=192 , running inference with power sampling incurs a multiplier of 8.84 × \textbf{8.84}\times the number of tokens as running standard inference. Since GRPO generates multiple rollouts per example during training, our method incurs roughly the same inference cost as one epoch of GRPO training , assuming 8 rollouts per sample with identical dataset sizes. Typically though, one GRPO epoch is still more expensive as it uses 16 rollouts and a training set that is larger than MATH500.

## 6 Conclusion

In this work, we present an algorithm that samples directly from a base model without any additional training or access to an external signal, achieving a single-shot reasoning performance that is on par with, and sometimes even better than, that of a state-of-the-art RL-posttraining algorithm. We use the discussion of RL distribution sharpening to motivate defining the power distribution as a valuable target distribution for reasoning. Although exact power distribution sampling is intractable, we employ classic MCMC techniques alongside the sequential structure of autoregressive generation to define our power sampling algorithm, which demonstrates strong empirical performance.

Our results suggest that base model capabilities are underutilized at sampling time and point towards a close relationship between high likelihood regions of the base model and strong reasoning capabilities. Employing additional compute at sampling-time with a stronger understanding of base model capabilites offers a promising direction for expanding the scope of reasoning beyond verifiability.

## 7 Acknowledgments

A.K. would like to thank the Paul and Daisy Soros Foundation, NDSEG Fellowship, and Kempner Institute for their support.

## References

Guo et al. [2025] Daya Guo, Dejian Yang, Haowei Zhang, Junxiao Song, Ruoyu Zhang, Runxin Xu, Qihao Zhu, Shirong Ma, Peiyi Wang, Xiao Bi, et al. Deepseek-r1: Incentivizing reasoning capability in LLMs via reinforcement learning. arXiv preprint arXiv:2501.12948 , 2025.

Hu et al. [2025] Jingcheng Hu, Yinmin Zhang, Qi Han, Daxin Jiang, Xiangyu Zhang, and Heung-Yeung Shum. Open-reasoner-zero: An open source approach to scaling up reinforcement learning on the base model. arXiv preprint arXiv:2503.24290 , 2025.

Hendrycks et al. [2021] Dan Hendrycks, Collin Burns, Saurav Kadavath, Akul Arora, Steven Basart, Eric Tang, Dawn Song, and Jacob Steinhardt. Measuring mathematical problem solving with the MATH dataset. arXiv preprint arXiv:2103.03874 , 2021.

Li et al. [2022] Yujia Li, David Choi, Junyoung Chung, Nate Kushman, Julian Schrittwieser, Rémi Leblond, Tom Eccles, James Keeling, Felix Gimeno, Agustin Dal Lago, Thomas Hubert, Peter Choy, Cyprien de Masson d’Autume, Igor Babuschkin, Xinyun Chen, Po-Sen Huang, Johannes Welbl, Sven Gowal, Alexey Cherepanov, James Molloy, Daniel Mankowitz, Esme Sutherland Robson, Pushmeet Kohli, Nando de Freitas, Koray Kavukcuoglu, and Oriol Vinyals. Competition-level code generation with AlphaCode. arXiv preprint arXiv:2203.07814 , 2022.

Rein et al. [2024] David Rein, Betty Li Hou, Asa Cooper Stickland, Jackson Petty, Richard Yuanzhe Pang, Julien Dirani, Julian Michael, and Samuel R Bowman. GPQA: A graduate-level google-proof q&a benchmark. In First Conference on Language Modeling , 2024.

He et al. [2025] Andre He, Daniel Fried, and Sean Welleck. Rewarding the unlikely: Lifting GRPO beyond distribution sharpening. arXiv preprint arXiv:2506.02355 , 2025.

Shao et al. [2025] Rulin Shao, Shuyue Stella Li, Rui Xin, Scott Geng, Yiping Wang, Sewoong Oh, Simon Shaolei Du, Nathan Lambert, Sewon Min, Ranjay Krishna, Yulia Tsvetkov, Hannaneh Hajishirzi, Pang Wei Koh, and Luke Zettlemoyer. Spurious rewards: Rethinking training signals in RLVR. arXiv preprint arXiv:2506.10947 , 2025.

Yue et al. [2025] Yang Yue, Zhiqi Chen, Rui Lu, Andrew Zhao, Zhaokai Wang, Shiji Song, and Gao Huang. Does reinforcement learning really incentivize reasoning capacity in llms beyond the base model? arXiv preprint arXiv:2504.13837 , 2025. URL https://arxiv.org/abs/2504.13837 .

Song et al. [2025] Yuda Song, Julia Kempe, and Rémi Munos. Outcome-based exploration for LLM reasoning. arXiv preprint arXiv:2509.06941 , 2025. URL https://arxiv.org/abs/2509.06941 .

Shao et al. [2024] Zhihong Shao, Peiyi Wang, Qihao Zhu, Runxin Xu, Junxiao Song, Xiao Bi, Haowei Zhang, Mingchuan Zhang, Y. K. Li, Y. Wu, and Daya Guo. Deepseek-math: Advancing mathematical reasoning through step-by-step exploration. arXiv preprint arXiv:2404.01140 , 2024.

Prabhudesai et al. [2025] Mihir Prabhudesai, Lili Chen, Alex Ippoliti, Katerina Fragkiadaki, Hao Liu, and Deepak Pathak. Maximizing confidence alone improves reasoning. arXiv preprint arXiv:2505.22660 , 2025. URL https://arxiv.org/abs/2505.22660 .

Ouyang et al. [2022] Long Ouyang, Jeffrey Wu, Xu Jiang, Diogo Almeida, Carroll L. Wainwright, Pamela Mishkin, Chong Zhang, Sandhini Agarwal, Katarina Slama, Alex Ray, et al. Training language models to follow instructions with human feedback. In NeurIPS , volume 35, pages 27730–27744, 2022.

Lambert et al. [2024] Nathan Lambert, Jacob Morrison, Valentina Pyatkin, Shengyi Huang, Hamish Ivison, Faeze Brahman, Lester James V Miranda, Alisa Liu, Nouha Dziri, Shane Lyu, et al. Tülu 3: Pushing frontiers in open language model post-training. arXiv preprint arXiv:2411.15124 , 2024.

Zeng et al. [2025] Weihao Zeng, Yuzhen Huang, Qian Liu, Wei Liu, Keqing He, Zejun Ma, and Junxian He. Simplerlzoo: Investigating and taming zero reinforcement learning for open base models in the wild. arXiv preprint arXiv:2503.18892 , 2025. URL https://arxiv.org/abs/2503.18892 .

Zhao et al. [2025] Xuandong Zhao, Zhewei Kang, Aosong Feng, Sergey Levine, and Dawn Song. Learning to reason without external rewards. arXiv preprint arXiv:2505.19590 , 2025. URL https://arxiv.org/abs/2505.19590 .

Zhao et al. [2024] Stephen Zhao, Rob Brekelmans, Alireza Makhzani, and Roger Grosse. Probabilistic inference in language models via twisted sequential monte carlo. arXiv preprint arXiv:2404.17546 , 2024. URL https://arxiv.org/abs/2404.17546 .

Chopin [2004] Nicolas Chopin. Central limit theorem for sequential monte carlo methods and its application to bayesian inference. The Annals of Statistics , 32(6):2385–2411, 2004. doi: 10.1214/009053604000000615 . URL https://projecteuclid.org/journals/annals-of-statistics/volume-32/issue-6/Central-limit-theorem-for-sequential-Monte-Carlo-methods-and-its/10.1214/009053604000000698.full .

Faria et al. [2024] Gonçalo R. A. Faria, Sweta Agrawal, António Farinhas, Ricardo Rei, José G. C. de Souza, and André F. T. Martins. Quest: Quality-aware metropolis-hastings sampling for machine translation. In NeurIPS , 2024. URL https://proceedings.neurips.cc/paper_files/paper/2024/file/a221d22ff6a33599142c8299c7ed06bb-Paper-Conference.pdf .

Neal [1998] Radford M. Neal. Annealed importance sampling. arXiv preprint physics/9803008 , 1998. URL https://arxiv.org/abs/physics/9803008 .

Łatuszyński et al. [2025] Krzysztof Łatuszyński, Matthew T. Moores, and Timothée Stumpf-Fétizon. Mcmc for multi-modal distributions. arXiv preprint arXiv:2501.05908 , 2025. URL https://arxiv.org/abs/2501.05908v1 .

Du et al. [2023] Yilun Du, Conor Durkan, Robin Strudel, Joshua B Tenenbaum, Sander Dieleman, Rob Fergus, Jascha Sohl-Dickstein, Arnaud Doucet, and Will Sussman Grathwohl. Reduce, reuse, recycle: Compositional generation with energy-based diffusion models and mcmc. In International conference on machine learning , pages 8489–8510. PMLR, 2023.

Kim et al. [2025] Sunwoo Kim, Minkyu Kim, and Dongmin Park. Test-time alignment of diffusion models without reward over-optimization. arXiv preprint arXiv:2501.05803 , 2025. URL https://arxiv.org/abs/2501.05803 .

Karan et al. [2025] Aayush Karan, Kulin Shah, and Sitan Chen. Reguidance: A simple diffusion wrapper for boosting sample quality on hard inverse problems. arXiv preprint arXiv:2506.10955 , 2025. URL https://arxiv.org/abs/2506.10955 .

Wang et al. [2025] Yanwei Wang, Lirui Wang, Yilun Du, Balakumar Sundaralingam, Xuning Yang, Yu-Wei Chao, Claudia Pérez-D’Arpino, Dieter Fox, and Julie Shah. Inference-time policy steering through human interactions. In 2025 IEEE International Conference on Robotics and Automation (ICRA) , pages 15626–15633. IEEE, 2025.

Kong et al. [2025] Lingkai Kong, Yuanqi Du, Wenhao Mu, Kirill Neklyudov, Valentin De Bortoli, Dongxia Wu, Haorui Wang, Aaron M. Ferber, Yian Ma, Carla P. Gomes, and Chao Zhang. Diffusion models as constrained samplers for optimization with unknown constraints. In Yingzhen Li, Stephan Mandt, Shipra Agrawal, and Emtiyaz Khan, editors, Proceedings of The 28th International Conference on Artificial Intelligence and Statistics , volume 258 of Proceedings of Machine Learning Research , pages 4582–4590. PMLR, 2025. URL https://proceedings.mlr.press/v258/kong25b.html .

Zhang et al. [2025] Xiangcheng Zhang, Haowei Lin, Haotian Ye, James Zou, Jianzhu Ma, Yitao Liang, and Yilun Du. Inference-time scaling of diffusion models through classical search. arXiv preprint arXiv:2505.23614 , 2025.

Sambridge [2014] Malcolm Sambridge. A parallel tempering algorithm for probabilistic sampling and optimization. Geophysical Journal International , 196(1):357–374, 2014. doi: 10.1093/gji/ggt374 . URL https://academic.oup.com/gji/article/196/1/357/585739 .

Skreta et al. [2025] Marta Skreta, Tara Akhound-Sadegh, Viktor Ohanesian, Roberto Bondesan, Alán Aspuru-Guzik, Arnaud Doucet, Rob Brekelmans, Alexander Tong, and Kirill Neklyudov. Feynman-kac correctors in diffusion: Annealing, guidance, and product of experts. arXiv preprint arXiv:2503.02819 , 2025. URL https://arxiv.org/abs/2503.02819 .

Xu et al. [2025] Yanbo Xu, Yu Wu, Sungjae Park, Zhizhuo Zhou, and Shubham Tulsiani. Temporal score rescaling for temperature sampling in diffusion and flow models. arXiv preprint arXiv:2510.01184 , 2025. URL https://arxiv.org/abs/2510.01184 .

Geffner et al. [2025] Tomas Geffner, Kieran Didi, Zuobai Zhang, Danny Reidenbach, Zhonglin Cao, Jason Yim, Mario Geiger, Christian Dallago, Emine Kucukbenli, and Arash Vahdat. Proteina: Scaling flow-based protein structure generative models. arXiv preprint arXiv:2503.00710 , 2025. URL https://arxiv.org/abs/2503.00710 .

Wang et al. [2020] Pei-Hsin Wang, Sheng-Iou Hsieh, Shih-Chieh Chang, Yu-Ting Chen, Jia-Yu Pan, Wei Wei, and Da-Chang Juan. Contextual temperature for language modeling. arXiv preprint arXiv:2012.13575 , 2020. URL https://arxiv.org/abs/2012.13575 .

Li et al. [2025] Marvin Li, Aayush Karan, and Sitan Chen. Blink of an eye: A simple theory for feature localization in generative models. arXiv preprint arXiv:2502.00921 , 2025. URL https://arxiv.org/abs/2502.00921 .

Abdin et al. [2024] Marah Abdin, Jyoti Aneja, Harkirat Behl, Sébastien Bubeck, Ronen Eldan, Suriya Gunasekar, Michael Harrison, Russell J. Hewett, Mojan Javaheripi, Piero Kauffmann, James R. Lee, Yin Tat Lee, Yuanzhi Li, Weishung Liu, Caio C. T. Mendes, Anh Nguyen, Eric Price, Gustavo de Rosa, Olli Saarikivi, Adil Salim, Shital Shah, Xin Wang, Rachel Ward, Yue Wu, Dingli Yu, Cyril Zhang, and Yi Zhang. Phi-4 technical report. arXiv preprint arXiv:2412.08905 , 2024. URL https://arxiv.org/abs/2412.08905 .

Metropolis et al. [1953] Nicholas Metropolis, Arianna W. Rosenbluth, Marshall N. Rosenbluth, Augusta H. Teller, and Edward Teller. Equation of state calculations by fast computing machines. Journal of Chemical Physics , 21(6):1087–1092, 1953. doi: 10.1063/1.1699114 .

Neal [1993] Radford M Neal. Probabilistic inference using markov chain monte carlo methods. Department of Computer Science, University of Toronto (review paper / technical report) , 1993.

Gheissari et al. [2017] Reza Gheissari, Eyal Lubetzky, and Yuval Peres. Exponentially slow mixing in the mean-field swendsen–wang dynamics. arXiv preprint arXiv:1702.05797 , 2017.

Bandeira et al. [2022] Afonso S. Bandeira, Antoine Maillard, Richard Nickl, and Sven Wang. On free energy barriers in gaussian priors and failure of cold start mcmc for high-dimensional unimodal distributions. arXiv preprint arXiv:2209.02001 , 2022. URL https://arxiv.org/abs/2209.02001 .

Schmidler and Woodard [2013] Scott C. Schmidler and Dawn B. Woodard. Lower bounds on the convergence rates of adaptive mcmc methods. Technical report, Duke University / Cornell University, 2013. URL https://www2.stat.duke.edu/~scs/Papers/AdaptiveLowerBounds_AS.pdf .

Lightman et al. [2024] Hunter Lightman, Vineet Kosaraju, Yura Burda, Harri Edwards, Bowen Baker, Teddy Lee, Jan Leike, John Schulman, Ilya Sutskever, and Karl Cobbe. Let’s verify step by step. In The Twelfth International Conference on Learning Representations , 2024. URL https://openreview.net/forum?id=v8L0pN6EOi .

Chen et al. [2021] M. Chen, J. Tworek, H. Jun, Q. Yuan, H. P. de Oliveira Pinto, J. Kaplan, H. Edwards, Y. Burda, N. Joseph, G. Brockman, A. Ray, R. Puri, G. Krueger, M. Petrov, H. Khlaaf, G. Sastry, P. Mishkin, B. Chan, S. Gray, N. Ryder, M. Pavlov, A. Power, L. Kaiser, M. Bavarian, C. Winter, P. Tillet, F. P. Such, D. Cummings, M. Plappert, F. Chantzis, E. Barnes, A. Herbert-Voss, W. H. Guss, A. Nichol, A. Paino, N. Tezak, J. Tang, I. Babuschkin, S. Balaji, S. Jain, W. Saunders, C. Hesse, A. N. Carr, J. Leike, J. Achiam, V. Misra, E. Morikawa, A. Radford, M. Knight, M. Brundage, M. Murati, K. Mayer, P. Welinder, B. McGrew, D. Amodei, S. McCandlish, I. Sutskever, and W. Zaremba. Evaluating large language models trained on code. CoRR , abs/2107.03374, 2021. URL https://arxiv.org/abs/2107.03374 .

Dubois et al. [2024] Yann Dubois, Balázs Galambosi, Percy Liang, and Tatsunori B. Hashimoto. Length-controlled alpacaeval: A simple way to debias automatic evaluators. arXiv preprint arXiv:2404.04475 , 2024. URL https://arxiv.org/abs/2404.04475 .

## Appendix A Appendix

### A.1 Additional Theoretical Discussion

In this section, we provide a stronger formalization of the phenomenon that power sampling downweights tokens that trap outputs in low-likelihood futures while low-temperature sampling does not.

###### Proposition 2 ( Informal ) .

Power sampling upweights tokens with small support but high likelihood completions, while low-temperature sampling upweights tokens with large support but low likelihood completions.

###### Definition 2 .

For the rest of this section, fix a prefix x 0 : t − 1 x_{0:t-1} . We say that x t x_{t} has marginal weight ε \varepsilon under the conditional next-token distribution if ∑ x > t p ⁡ ( x 0 , … , x t , … ​ x T ) = ε \sum_{x>t}p(x_{0},\dots,x_{t},\dots x_{T})=\varepsilon .

We consider a simplified model of the “critical window” or “pivotal token” phenomenon ( Li et al., 2025 ; Abdin et al., 2024 ) , which refers to intermediate tokens that strongly influence the quality of the final generation. We differentiate between pivotal tokens that lead to high-likelihood futures vs. low-likelihood ones.

###### Definition 3 .

At one extreme, a pivotal token maximally induces a high-likelihood completion if it places its entire marginal weight ε \varepsilon on one future (singular support); i.e., for only one choice of x > t x>t is p ⁡ ( x 0 , … , x t , … , x T ) p(x_{0},\dots,x_{t},\dots,x_{T}) nonzero. We call such a token a positive pivotal token.

###### Definition 4 .

At the other extreme, a pivotal token minimizes the likelihood of any future if its entire marginal weight ε \varepsilon is uniformly distributed across N N future completions. In other words, there exist N N completions x > t x>t such that p ⁡ ( x 0 , … , x t , … , x T ) p(x_{0},\dots,x_{t},\dots,x_{T}) are all nonzero with likelihood ε N \frac{\varepsilon}{N} . We call such a token a negative pivotal token.

Our simplified model of high and low-likelihood futures examines when positive pivotal tokens are favored over negative pivotal tokens under a given sampling distribution. In particular, we show that power sampling can upweight a positive pivotal token over a negative one even if the latter has a higher marginal weight, whereas low-temperature sampling always upweights the negative pivotal token in such a scenario.

Of course, whenever a positive pivotal token has higher marginal weight, both power sampling and low-temperature sampling will upweight it.

###### Proposition 3 .

Let x t x_{t} be a positive pivotal token with marginal weight ε \varepsilon , and let x t ′ x_{t}^{\prime} be a negative pivotal token with marginal weight ε ′ \varepsilon^{\prime} and support N N . Then if ε ′ N 1 − 1 / α < ε < ε ′ , \frac{\varepsilon^{\prime}}{N^{1-1/\alpha}}<\varepsilon<\varepsilon^{\prime}, (14) the future likelihood of x t x_{t} is higher than any future likelihood of x t ′ x_{t}^{\prime} . Moreover, power sampling upweights x t x_{t} over x t ′ x_{t}^{\prime} while low-temperature sampling upweights x t ′ x_{t}^{\prime} over x t x_{t} .

###### Proof.

Since α ≥ 1 \alpha\geq 1 , it follows that ε ′ N 1 − 1 / α > ε ′ N \frac{\varepsilon^{\prime}}{N^{1-1/\alpha}}>\frac{\varepsilon^{\prime}}{N} (15) and thus ε > ε ′ N \varepsilon>\frac{\varepsilon^{\prime}}{N} , establishing that the future completion likelihood of x t x_{t} is greater than that of x t ′ x_{t}^{\prime} (i.e. the assignment of positive and negative pivotal tokens is consistent).

Now, if ε < ε ′ \varepsilon<\varepsilon^{\prime} , then under the low-temperature distribution, the relative marginal weights on x t x_{t} and x t ′ x_{t}^{\prime} are ε α \varepsilon^{\alpha} and ε ′ α \varepsilon^{\prime\alpha} , so the probability of choosing x t x_{t} is downweighted relative to x t ′ x_{t}^{\prime} . However, for the power distribution, the relative marginal weights are p pow ​ ( x t | x < t ) = ε α p_{\text{pow}}(x_{t}|x_{<t})=\varepsilon^{\alpha} and p pow ​ ( x t ′ | x < t ) = ε ′ α N α − 1 p_{\text{pow}}(x_{t}^{\prime}|x_{<t})=\frac{\varepsilon^{\prime\alpha}}{N^{\alpha-1}} . Then, as long as ε α > ε ′ α N α − 1 ⇔ ε > ε ′ N 1 − 1 / α \varepsilon^{\alpha}>\frac{\varepsilon^{\prime\alpha}}{N^{\alpha-1}}\iff\varepsilon>\frac{\varepsilon^{\prime}}{N^{1-1/{\alpha}}} , token x t x_{t} will be upweighted relative to token x t ′ x_{t}^{\prime} .

In other words, the marginal weight on x t x_{t} can be less than the mass on x t ′ x_{t}^{\prime} under p p , but if the completion for x t x_{t} has higher likelihood than any individual completion for x t ′ x_{t}^{\prime} , power sampling favors x t x_{t} over x t ′ x_{t}^{\prime} .∎

### A.2 Pass@k Accuracies over Multiple Domains

In this section, we plot the pass@ k k performance of power sampling, GRPO, and the base model (Qwen2.5-Math-7B) over MATH500, GPQA, and HumanEval to demonstrate that our sampling algorithm is highly performant at both single-shot and multi-shot reasoning while maintaining response diversity. Power sampling is plotted with α = 4.0 \alpha=4.0 for MATH500 and GPQA and α = 1.67 \alpha=1.67 for HumanEval (this temperature exhibits slightly better results at earlier k k ). In all cases, both in-domain and out-of-domain for GRPO, power sampling has near universally better performance than both GRPO and the base model in pass@ k k for k > 1 k>1 and matches, if not exceeds, the base model upper bound at large k k .

One thing to note about these plots is that the loss in diversity varies noticeably from benchmark to benchmark. MATH500 and GPQA clearly show that GRPO has a significantly lower pass@ k k performance and diversity even for smaller k k , while on HumanEval GRPO exhibits better pass@ k k than the base model until k = 16 k=16 . We speculate this might be due to the fact that while MATH500 and GPQA are graded on a “singular” answer, HumanEval is based on completing code where multiple solutions might be accepted, indicating a reduction in diversity may emerge but at much higher k k .

### A.3 More Qualitative Examples

## Instructions for reporting errors

We are continuing to improve HTML versions of papers, and your feedback helps enhance accessibility and mobile support. To report errors in the HTML that will help us improve conversion and rendering, choose any of the methods listed below:

Click the "Report Issue" ( ) button, located in the page header.

Tip: You can select the relevant text first, to include it in your report.

Our team has already identified the following issues . We appreciate your time reviewing and reporting rendering errors we may not have found yet. Your efforts will help us improve the HTML versions for all readers, because disability should not be a barrier to accessing research. Thank you for your continued support in championing open access for all.

Have a free development cycle? Help support accessibility at arXiv! Our collaborators at LaTeXML maintain a list of packages that need conversion , and welcome developer contributions .
