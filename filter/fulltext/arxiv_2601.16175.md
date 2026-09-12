##### Report GitHub Issue

Content selection saved. Describe the issue below:

# Learning to Discover at Test Time

###### Abstract

How can we use AI to discover a new state of the art for a scientific problem? Prior work in test-time scaling, such as AlphaEvolve, performs search by prompting a frozen LLM. We perform reinforcement learning at test time, so the LLM can continue to train, but now with experience specific to the test problem. This form of continual learning is quite special, because its goal is to produce one great solution rather than many good ones on average, and to solve this very problem rather than generalize to other problems. Therefore, our learning objective and search subroutine are designed to prioritize the most promising solutions. We call this method Test-Time Training to Discover (TTT-Discover). Following prior work, we focus on problems with continuous rewards.

We report results for every problem we attempted, across mathematics, GPU kernel engineering, algorithm design, and biology. TTT-Discover sets the new state of the art in almost all of them: (i) Erdős’ minimum overlap problem and an autocorrelation inequality; (ii) a GPUMode kernel competition (up to 2 × 2\times faster than prior art); (iii) past AtCoder algorithm competitions; and (iv) denoising problem in single-cell analysis. Our solutions are reviewed by experts or the organizers.

All our results are achieved with an open model, OpenAI gpt-oss-120b, and can be reproduced with our publicly available code , in contrast to previous best results that required closed frontier models. Our test-time training runs are performed using Tinker, an API by Thinking Machines, with a cost of only a few hundred dollars per problem.

## 1 Introduction

To solve hard problems, humans often need to try, fail, stumble upon partial successes, and then learn from their experiences. Consider your first really hard programming assignment. You read the textbook and trained yourself on the book exercises, but this assignment just asked for so much beyond the basics in the book. You tried to guess the solution, but these attempts merely produced small signs of life. So you had to take a deep breath and learn from your failed attempts, which made your future attempts more intelligent. Finally, after hours of trying and learning, you understood the new ideas behind the assignment. And indeed, the next attempt worked!

In this example, the assignment was hard because it required new ideas beyond your training data (the text and exercises in the book). Now consider using AI to solve scientific discovery problems. This goal is even harder: By definition, discovery problems require ideas not only beyond the model’s training data but also all existing knowledge of humanity. And out-of-distribution generalization is no easier for AI than for humans Miller et al. (2020) ; Hendrycks et al. (2021) ; Ribeiro et al. (2020) ; Koh et al. (2021) .

To offset this hardness, prior work has focused on test-time search in the solution space by prompting a frozen LLM to make many attempts, similar to how we tried to guess the solution to the assignment. In particular, evolutionary search methods, such as AlphaEvolve, store past attempts in a buffer and use them to generate new prompts via hand-crafted and domain-specific heuristics Novikov et al. (2025) ; Lange et al. (2025) ; Sakana AI (2026) ; Yuksekgonul et al. (2025) . While these prompts can help the LLM improve previous solutions, the LLM itself cannot improve, similar to a student who can never internalize the new ideas behind the assignment.

The most direct way for the LLM to improve is through learning. And indeed, while both learning and search scale well with compute Sutton (2019) , learning has often superseded search in the history of AI for hard problems such as Go and protein folding Silver et al. (2017) ; Jumper et al. (2021) . We believe that this observation from history is still relevant today, as we scale compute at test time. So we continue to train the LLM, while it attempts to solve this very test problem. And these attempts, in turn, provide the most valuable training data: Recall that the test problem was hard because it was out-of-distribution. Now we have a data distribution specific to this problem.

At a high level, we simply perform Reinforcement Learning (RL) in an environment defined by the single test problem, so any technique in standard RL could be applied. However, our goal has two critical differences from that of standard RL. First, our policy only needs to solve this single problem rather than generalize to other problems. Second, we only need a single best solution, and the policy is merely a means towards this end. In contrast, the policy is the end in standard RL, whose goal is to maximize the average reward across all attempts. While the first difference is a recurring theme in the field of test-time training Sun et al. (2020) , the second is unique to discovery problems.

To take advantage of these differences, our learning objective and search subroutine strongly favor the most promising solutions. We call this method Test-Time Training to Discover (TTT-Discover). We focus on problems with continuous rewards, in mathematics (§ 4.1 ), GPU kernel engineering (§ 4.2 ), algorithm design (§ 4.3 ), and biology (§ 4.4 ). We report results for every problem we attempted, and TTT-Discover sets the new state of the art in almost all of them, using only an open model.

There are three pieces of concurrent work that share our high-level idea: EvoTune (Surina et al.) Surina et al. (2025) , MiGrATe (Phan et al.) Phan et al. (2025) , and recently ThetaEvolve (Wang et al.) Wang et al. (2025a) , which is especially relevant. Compared to ThetaEvolve, TTT-Discover using the same model and compute budget still produces significant improvements (Table 2 ), due to its special learning objective and search subroutine.

## 2 Preliminaries

All methods in this paper, including the baselines, share a common goal: Given a scientific problem at test time, the goal is to discover a new state-of-the-art solution with an LLM policy π θ \pi_{\theta} , whose weights θ \theta have already been trained (at training time). To formalize this goal, we first introduce how each scientific problem defines an environment, i.e., a Markov Decision Process (§ 2.1 ), which can then be used for search (§ 2.2 ) and learning (§ 3 ).

### 2.1 Discovery Problem

Our definition of the environment follows prior work in test-time scaling, such as AlphaEvolve Novikov et al. (2025) : A scientific problem comes in the form of a text description d d , which we always feed as context to the policy. We define a state s s as a candidate solution, such as a kernel implementation of the PyTorch code in d d . In our applications, the problem description also induces a continuous reward function R ⁡ ( s ) ∈ R R(s)\in\mathbb{R} , such as the inverse runtime of the kernel.

We denote s sota s_{\text{sota}} as the best-known solution among all existing candidates, and r sota = R ⁡ ( s sota ) r_{\text{sota}}=R(s_{\text{sota}}) as the best-known reward. And in case there is no existing solution, s sota s_{\text{sota}} can be the empty string <empty> . For example, s sota s_{\text{sota}} can be the kernel currently at the top of the leaderboard. These notations allow us to formalize the notion of a discovery:

###### Definition (Discovery) .

A discovery is an event where a state s s is found such that R ⁡ ( s ) > r sota R(s)>r_{\text{sota}} . The larger the difference, the more significant the discovery.

Under this formalism, we define a discovery problem as finding such a state s s with large R ⁡ ( s ) − r sota R(s)-r_{\text{sota}} within the environment defined by the scientific problem.

To produce a better solution, both search and learning methods use the LLM policy to generate an action a ∼ π θ ( ⋅ ∣ d , s ) a\sim\pi_{\theta}(\cdot\mid d,s) , where the choice of the initial solution s s (e.g., = s sota =s_{\text{sota}} ) is an important part of the method’s design. Similar to the reward function, the transition function ( s , a ) → s ′ (s,a)\rightarrow s^{\prime} of the environment is also induced by the problem description. Here, we consider only a single timestep since state reuse, which we will introduce soon, effectively subsumes multiple timesteps.

In all our applications, a valid action contains a piece of code and optionally some thinking tokens. For coding problems (e.g., kernel engineering), the environment produces s ′ s^{\prime} by simply parsing the code out of a a . For problems in mathematics, the environment also needs to execute the code in a a after it is parsed. Table 1 provides an overview of the environments for all our applications.

### 2.2 Search Methods

The simplest search method, known as Best-of- N N , samples i.i.d. rollouts from π θ \pi_{\theta} : Best-of- N : s = s sota or <empty> , a i ∼ π θ ( ⋅ ∣ d , s ) , \textbf{Best-of-$N$:}\quad s=s_{\text{sota}}\text{ or }\texttt{<empty>}{},\;\;a_{i}\sim\pi_{\theta}(\cdot\mid d,s), where the subscript, i = 1 , … , N i=1,\dots,N , denotes the index of the rollout. By using i i instead of t t for the index, we indicate that the rollouts here are independent. One reasonable choice of the initial state s s is s sota s_{\text{sota}} , assuming that a previous solution exists. But s sota s_{\text{sota}} might be too strong a prior towards exploitation. For example, conditioning on s sota s_{\text{sota}} might prevent the policy from exploring very different, but more promising directions that would ultimately produce better solutions under a large compute budget. To address this concern, we usually set s = <empty> s=\texttt{<empty>}{} , the empty (or trivial) solution.

On the other hand, the policy might also explore a promising direction using s = <empty> s=\texttt{<empty>}{} , but fail to fully exploit it. One technique to address this opposite concern is state reuse , which warm starts the policy with some of the previous solutions. Specifically, it maintains a buffer ℋ i \mathcal{H}_{i} of the previous solutions, and samples the initial solution s i s_{i} from ℋ i \mathcal{H}_{i} using a search heuristic, reuse , which favors high-reward solutions but still assigns nontrivial likelihood to low-reward ones: State reuse: s i ∼ reuse ( ℋ i ) , a i ∼ π θ ( ⋅ ∣ d , s i ) , ℋ i + 1 = ℋ i ∪ { ( s i ′ , r i ) } . \textbf{State reuse:}\quad s_{i}\sim\texttt{reuse}(\mathcal{H}_{i}),\;\;a_{i}\sim\pi_{\theta}(\cdot\mid d,s_{i}),\;\;\mathcal{H}_{i+1}=\mathcal{H}_{i}\cup\{(s^{\prime}_{i},r_{i})\}.\vskip-4.30554pt When we reuse a previous solution s i ′ s^{\prime}_{i} , we have effectively added an extra timestep to its trajectory.

Prior work, such as AlphaEvolve Novikov et al. (2025) , also reuses the actions, which can contain thinking tokens and intermediate results (e.g., code for math problems) that are not part of the states. As a consequence, the reuse heuristic also needs to convert the information from previous actions into natural language context c i c_{i} that can be ingested by the LLM policy: State-action reuse: s i , c i ∼ reuse ( ℋ i ) , a i ∼ π θ ( ⋅ ∣ d , s i , c i ) , ℋ i + 1 = ℋ i ∪ { ( s i , a i , s i ′ , r i ) } . \textbf{State-action reuse:}\quad s_{i},c_{i}\sim\texttt{reuse}(\mathcal{H}_{i}),\;\;a_{i}\sim\pi_{\theta}(\cdot\mid d,s_{i},c_{i}),\;\;\mathcal{H}_{i+1}=\mathcal{H}_{i}\cup\{(s_{i},a_{i},s^{\prime}_{i},r_{i})\}. Prior work Novikov et al. (2025) ; Lange et al. (2025) ; Yuksekgonul et al. (2025) ; Liu et al. (2024b) refers to state-action reuse as evolutionary search , because the reuse heuristic usually involves sophisticated designs motivated by evolution, including hand-crafted operations for mutation and cross-over, and domain-specific measurements of fitness and diversity.

## 3 Learning to Discover at Test Time

So far, the policy’s experience with the test problem can only improve the next prompt ( d , s i , c i ) (d,s_{i},c_{i}) , but not the policy π θ \pi_{\theta} itself, since θ \theta remains frozen. We use this experience to improve the policy in an online fashion, by training π θ \pi_{\theta} on its own search attempts accumulated in the buffer ℋ i \mathcal{H}_{i} .

Algorithm 1 outlines the general form of our method, where the two key subroutines to instantiate are reuse and train .

### 3.1 Naive RL at Test Time

Algorithm 1 falls under the formulation of reinforcement learning (RL). A natural baseline is to use a standard RL algorithm: train : θ i + 1 = θ i + η ∇ θ E a ∼ π θ i ( ⋅ ∣ s ) [ R ( s , a ) ] , reuse ( ℋ i ) = δ <empty> , \texttt{train}:\quad\theta_{i+1}=\theta_{i}+\eta\nabla_{\theta}\mathbb{E}_{a\sim\pi_{\theta_{i}}(\cdot\mid s)}\!\left[R(s,a)\right],\qquad\texttt{reuse}(\mathcal{H}_{i})=\delta_{\texttt{<empty>}{}}, i.e., optimize for expected reward with no reuse, where δ <empty> \delta_{\texttt{<empty>}{}} is a delta distribution with mass only on the initial state <empty> . We will use θ i \theta_{i} to denote the model weights for rollout i i . We can straightforwardly apply popular RL algorithms, such as PPO or GRPO Schulman et al. (2017) ; Guo et al. (2025) , only in the environment defined by the single problem.

However, these algorithms are designed with the standard RL problem in mind. Discovery problems have important distinctions from standard RL problems.

In standard RL problems, the goal is to find a policy that maximizes the expected reward. This policy is to be deployed repeatedly in the same environment. The primary artifact is the policy.

In discovery problems, the goal is to find a single state that improves upon the state-of-the-art. We do not care about the average performance. There is no separate deployment phase and thus the policy need not maintain robust performance in many states it may encounter starting from the same initial state distribution. In fact, a policy can have very low expected reward, so long as it reaches a new state-of-the-art once.

Due to these differences, the naive RL instantiation has important shortcomings.

Objective function. Naive RL optimizes average performance, and is indifferent to the state of the art. In discovery, however, success is determined by the maximum, and whether it improves upon the state of the art. Consider a kernel engineering problem where the state-of-the-art runtime is 2000 ​ μ ​ s 2000\,\mu\text{s} . Achieving 1900 ​ μ ​ s 1900\,\mu\text{s} would require substantial optimization and perhaps a breakthrough. Yet, without complicated reward shaping, both would receive nearly the same reward.

Short effective horizon. Starting each attempt from scratch limits how far the policy can reach in an attempt. Reusing a previous solution effectively adds extra timesteps to an attempt, extending the horizon. As a result, more complex solutions can emerge during training. In standard RL, a fixed initial state distribution makes sense as the policy must perform robustly from states it will encounter at deployment. Discovery has no such deployment phase.

Exploration. Exploration requires care at two levels. Optimizing for expected reward, the policy can collapse to safe, high-reward actions rather than risky ones that might achieve discovery. At the reuse level, naive prioritization can over-exploit a few promising states at the expense of diversity.

### 3.2 TTT-Discover

To address these shortcomings, we introduce two simple components.

Entropic objective. We define the entropic objective that favors the maximum reward actions: J β ( θ ) = E s ∼ reuse ​ ( ℋ ) [ log E a ∼ π θ ( ⋅ ∣ s ) [ e β ​ ( s ) ​ R ​ ( s , a ) ] ] , J_{\beta}(\theta)=\mathbb{E}_{s\sim\texttt{reuse}(\mathcal{H})}\left[\log\mathbb{E}_{a\sim\pi_{\theta}(\cdot\mid s)}\left[e^{\beta(s)R(s,a)}\right]\right], ∇ θ J β ​ ( θ ) = E s ∼ reuse ​ ( ℋ ) a ∼ π θ ( ⋅ | s ) ​ [ w β ​ ( s ) ​ ( a ) ​ ∇ θ ​ log ⁡ π θ ​ ( a ∣ s ) ] , w β ​ ( s ) ​ ( a ) = e β ​ ( s ) ​ R ​ ( s , a ) E π θ ( ⋅ ∣ s ) [ e β ​ ( s ) ​ R ​ ( s , a ) ] , \nabla_{\theta}J_{\beta}(\theta)=\mathbb{E}_{\begin{subarray}{c}s\sim\texttt{reuse}(\mathcal{H})\\ a\sim\pi_{\theta}(\cdot|s)\end{subarray}}\left[w_{\beta(s)}(a)\nabla_{\theta}\log\pi_{\theta}(a\mid s)\right],\qquad w_{\beta(s)}(a)=\frac{e^{\beta(s)R(s,a)}}{\mathbb{E}_{\pi_{\theta}(\cdot\mid s)}[e^{\beta(s)R(s,a)}]}, where we also shape advantages with a KL penalty: A ⁡ ( a , s ) = w β ​ ( s ) ​ ( a ) − 1 − λ ​ log ⁡ π θ ​ ( a ∣ s ) π θ 0 ​ ( a ∣ s ) A(a;s)=w_{\beta(s)}(a)-1-\lambda\log\frac{\pi_{\theta}(a\mid s)}{\pi_{\theta_{0}}(a\mid s)} Schulman et al. (2017) ; Zhang et al. (2025b) ; Tang and Munos (2025) , and − 1 -1 is the baseline since E ⁡ [ w β ​ ( s ) ] = 1 \mathbb{E}[w_{\beta(s)}]=1 . Concurrent work Jiang et al. (2025) also explored the entropic objective J β J_{\beta} to maximize the pass@k performance for (training-time) RL with binary reward problems.

As β → ∞ \beta\to\infty , the entropic objective tends to the max \max , which is intuitively what we want. However, too large β \beta early in training causes instabilities, while too small later makes advantages vanish as even smaller improvements become harder. Empirically, we found that setting a constant β \beta that works well across different tasks is challenging. Therefore, different than Jiang et al. (2025) , we set β ​ ( s ) \beta(s) adaptively per initial state by constraining the KL divergence of the induced policy; see Appendix A.1 for details.

PUCT. We select initial states using a PUCT-inspired rule Rosin (2011) ; Silver et al. (2016) ; Silver et al. (2017) ; Silver et al. (2018) . Each state s s is scored by Q ⁡ ( s ) + c ⋅ P ⁡ ( s ) ⋅ 1 + T / ( 1 + n ⁡ ( s ) ) Q(s)+c\cdot P(s)\cdot\sqrt{1+T}/(1+n(s)) , where Q ⁡ ( s ) Q(s) is the maximum reward among states generated when the initial state was s s (or R ⁡ ( s ) R(s) if s s has not yet been selected). P ⁡ ( s ) P(s) is proportional to s s ’s rank in the buffer sorted by reward, n ⁡ ( s ) n(s) counts how many times s s or its descendants have been expanded, and T T is the total number of expansions, and c c is the exploration coefficient.

Rather than the mean (as in prior work), we use the maximum reward of children in Q ⁡ ( s ) Q(s) : we care about the best outcome starting from a state, not the average. The prior P ⁡ ( s ) P(s) captures the intuition that high-reward states are more likely to yield high-reward children—e.g., a fast kernel is more likely to seed a faster kernel than a slow one—while the exploration bonus prevents over-exploitation by keeping under-visited states as candidates. See Appendix A.2 for implementation details.

Test-time Training to Discover. With these building blocks, we can introduce our method, TTT-Discover. We combine J β ​ ( s ) J_{\beta(s)} as our (test-time) training objective and PUCT as our reuse routine:

train : θ i + 1 = θ i + η ​ ∇ θ J β ​ ( s i ) ​ ( θ i ) , reuse : s i ∼ PUCT ​ ( ℋ i ) . \texttt{train}:\quad\theta_{i+1}=\theta_{i}+\eta\nabla_{\theta}J_{\beta(s_{i})}(\theta_{i}),\qquad\texttt{reuse}:\quad s_{i}\sim\text{PUCT}(\mathcal{H}_{i}).

### 3.3 Implementation Details

We run TTT-Discover with gpt-oss-120b Agarwal et al. (2025) on Tinker Lab (2025) for 50 50 training steps. We use LoRA Hu et al. (2022) with rank 32 32 . At each step, we generate a batch of 512 512 rollouts, with 8 8 groups of 64 64 rollouts each. Each group of rollouts is generated using the same context and initial state selected from the reuse buffer. We use the entropic objective, and apply importance sampling ratio correction to the gradients due to the sampler/learner mismatch in the RL infrastructure Yao et al. () . We do not take any off-policy steps, i.e., take 1 1 gradient step on the entire batch.

We set the reasoning effort to high. The context window of gpt-oss-120b is limited to 32,768 32,768 tokens on Tinker. Thus, each rollout stops when the context window is exhausted or the LM produces the end of sequence token. In most domains, we limit the total length of the prompt and the thinking tokens to 26000 26000 tokens, so as to leave enough tokens to generate the final response, e.g., to allow generating longer algorithm code. We enforce this by token forcing the model to generate its final response. All hyperparameters reported in Table 9 , and are fixed unless otherwise stated. Assuming an average prompt length of 3000 3000 tokens and 16000 16000 sampling tokens on average, a training run with 50 50 steps and 512 512 rollouts costs around $ 500 \$500 on Tinker.

## 4 Applications

We evaluate TTT-Discover on problems in GPU kernel engineering, mathematics, algorithm design, and biology. We report our performance on every task we attempted. Besides potential impact, we pick domains with 2 criteria. First, we pick domains where we can compare our performance to human experts. This is possible, for example, by comparing to the best submissions in human engineering competitions, or to the best results reported in academic papers. We also want to compare to AI baselines. As we discuss below, mathematics and algorithm design are discovery domains where prior work recently made progress Novikov et al. (2025) ; Georgiev et al. (2025) ; Imajuku et al. (2025) ; Sakana AI (2026) ; Wang et al. (2025a) .

In every application, we report the best known human results and the best known AI results. Importantly, we always report the Best-of- N N baseline that matches the sampling budget and the model that TTT-Discover uses. That is, since we perform 50 50 steps with 512 512 rollouts per step, and compare to the Best-of- 25600 25600 baseline. For a closest evolutionary algorithm baseline, we also run OpenEvolve Sharma (2025) , an open-source version of AlphaEvolve Novikov et al. (2025) , with the same 25600 25600 sampling budget. We use the same context window budget and the Tinker client for gpt-oss-120b throughout the experiments. We caution that the context window limit led to a large number of rollouts in OpenEvolve to be truncated before the model completes its response, as OpenEvolve’s prompts grow very large in length. However, to stay faithful to their implementation, we did not modify their prompts or rollouts.

### 4.1 Mathematics

We explore multiple open problems in mathematics. These are often problems where even small numerical improvements carry real weight, since each result potentially rules out families of approaches and extends the frontier of what is mathematically known. Here, proofs are by construction: one can construct a concrete mathematical object – a step function or a sequence – that certifies, e.g., a bound for an inequality can be achieved. This property makes these problems amenable to search.

Environment: The state s s is a construction. Specifically, a construction is a step function represented as a numerical array, to certify a proof. The action a a consists of thinking tokens followed by Python code that either constructs a new step function or modifies an existing one. The dynamics execute the parsed code to produce the next state: s ′ = Python ​ ( Parse ​ ( a ) ) s^{\prime}=\texttt{Python}(\texttt{Parse}(a)) . The reward is the bound certified by s ′ s^{\prime} , or zero if s ′ s^{\prime} fails validity checks (e.g., the function must satisfy constraints on its support, sign, or integral). Most often, actions involve optimization algorithms to improve the constructions.

Throughout mathematics applications, we initialize the buffer with random states. Specifically, initial states are sampled uniformly at random within the problem’s valid range. For each action, we give a 10-minute limit to execute the code given by the action. In the case of a timeout, the action gets a reward of 0 0 . For minimization problems (certifying upper bounds), we set the reward proportional to 1 / bound 1/{\text{bound}} for the certified bound, and otherwise we set it proportional to bound . We report further details about the environment and the prompts we use in Appendix B .

Previous state-of-the-art. Such problems are recently explored in Georgiev et al. (2025) ; Novikov et al. (2025) . We report both the best known human results, and the recent progress by AI: AlphaEvolve Novikov et al. (2025) , AlphaEvolve V2 Georgiev et al. (2025) which was released around 6 months after AlphaEvolve, ShinkaEvolve Lange et al. (2025) , and ThetaEvolve Wang et al. (2025a) .

We select one representative problem from each area in AlphaEvolve Novikov et al. (2025) : Erdős’ minimum overlap problem (combinatorics), autocorrelation inequalities (analysis), circle packing (geometry).

#### 4.1.1 Erdős’ Minimum Overlap Problem

This is a classic problem in combinatorial number theory, posed by Erdős in 1955, with connections to the distribution of sequences and difference sets. Partition { 1 , 2 , … , 2 ​ n } \{1,2,\ldots,2n\} into two sets A A and B B of equal cardinality n n . Define M k M_{k} as the number of solutions to a i − b j = k a_{i}-b_{j}=k for a i ∈ A , b j ∈ B a_{i}\in A,b_{j}\in B , and let M ⁡ ( n ) = min A , B ⁡ max k ​ M k M(n)=\min_{A,B}\max_{k}M_{k} over all partitions. The problem is to bound c = lim n → ∞ M ⁡ ( n ) / n c=\lim_{n\to\infty}M(n)/n . Bounds before AlphaEvolve were 0.379005 < c < 0.380927 0.379005<c<0.380927 , with the upper bound due to Haugland Haugland (2016) and the lower bound due to White (2023) . AlphaEvolve Novikov et al. (2025) ; Georgiev et al. (2025) improved the upper bound to 0.380924 0.380924 .

Following Novikov et al. (2025) , we optimize step functions f f describing the density of A A throughout [ 1 , 2 ​ n ] [1,2n] . Due to a result of Swinnerton-Dyer Haugland (2016) , density functions yield valid upper bounds on lim M ⁡ ( n ) / n \lim M(n)/n without constructing explicit partitions for large n n . Validity checks require f ⁡ ( x ) ∈ [ 0 , 1 ] f(x)\in[0,1] and ∫ f = 1 \intop\nolimits f=1 .

Results. We improve the upper bound on Erdős’ Minimum Overlap Problem to 0.380876 0.380876 , surpassing AlphaEvolve’s recent construction with 0.380924 0.380924 Novikov et al. (2025) . Our improvement over AlphaEvolve is 16 times larger than AlphaEvolve’s improvement over the previous state-of-the-art. Unlike AlphaEvolve’s symmetric construction, our method discovered a 600-piece asymmetric step function. Surprisingly, the Best-of- 25600 25600 baseline also improved upon the AlphaEvolve construction.

The discovered algorithm minimizes the correlation bound using FFT-accelerated gradient descent combined with random hill climbing and simulated annealing. The code maintains feasibility by projecting onto the constraint set where f ⁡ ( x ) ∈ [ 0 , 1 ] f(x)\in[0,1] with with ∫ f = 1 \intop\nolimits f=1 . Interestingly, the solution found by TTT-Discover is asymmetric.

#### 4.1.2 Autocorrelation Inequalities

Autocorrelation inequalities are motivated by additive combinatorics Barnard and Steinerberger (2020) . Improving these inequalities tightens a constant that propagates into sharper limits on how large a set can be while still avoiding repeated additive patterns (a central theme in additive combinatorics). Similar to the Erdős’ minimum overlap problem, we will construct a step function f f to certify bounds.

First autocorrelation inequality. For nonnegative f f supported on [ − 1 / 4 , 1 / 4 ] [-1/4,1/4] , define C 1 C_{1} as the largest constant such that max | t | ≤ 1 / 2 ⁡ ( f ∗ f ) ​ ( t ) ≥ C 1 ​ ( ∫ f ) 2 \max_{|t|\leq 1/2}(f*f)(t)\;\geq\;C_{1}\Bigl(\intop\nolimits f\Bigr)^{2} holds for all such f f . The goal is to certify the tightest upper bound on C 1 C_{1} ; any valid construction f f certifies C 1 ≤ ‖ f ∗ f ‖ ∞ ‖ f ‖ 1 2 . C_{1}\leq\frac{\|f*f\|_{\infty}}{\|f\|_{1}^{2}}. Until early 2025, the best known upper bound was C 1 ≤ 1.50973 C_{1}\leq 1.50973 Matolcsi and Vinuesa (2010) . AlphaEvolve improved this to C 1 ≤ 1.5053 C_{1}\leq 1.5053 , and AlphaEvolve V2 further improved it to C 1 ≤ 1.50317 C_{1}\leq 1.50317 , and ThetaEvolve refined AlphaEvolve’s construction to get C 1 ≤ 1.50314 C_{1}\leq 1.50314 .

Second autocorrelation inequality. For nonnegative f f , define C 2 = sup f ≥ 0 ‖ f ∗ f ‖ 2 2 ‖ f ∗ f ‖ 1 ​ ‖ f ∗ f ‖ ∞ . C_{2}\;=\;\sup_{f\geq 0}\;\frac{\|f*f\|_{2}^{2}}{\|f*f\|_{1}\,\|f*f\|_{\infty}}. The problem is to certify the tightest known lower bound on C 2 C_{2} ; any valid construction f f with ratio r r certifies C 2 ≥ r C_{2}\geq r . The best human bound was C 2 ≥ 0.8892 C_{2}\geq 0.8892 Matolcsi and Vinuesa (2010) . AlphaEvolve first improved this to C 2 ≥ 0.8962 C_{2}\geq 0.8962 , Boyer and Li (2025) improved this to 0.9015 0.9015 , and AlphaEvolve V2 further improved it to C 2 ≥ 0.9610 C_{2}\geq 0.9610 using a 50,000-piece step function.

Results. We improved the best known upper bound to prove C 1 ≤ 1.50286 C_{1}\leq 1.50286 , with a 30000-piece step function. The comparisons are reported in Table 2 . The previous state-of-the-art, ThetaEvolve, achieved their result by refining the AlphaEvolve V2 construction. In contrast, TTT-Discover found a new construction by starting from scratch. We visualize our and prior works’ step functions in Figure 3 . In the second autocorrelation inequality, we have not made a discovery. Our best construction certified a bound of 0.959 0.959 , where the AlphaEvolve construction had certified a tighter lower bound of 0.961 0.961 .

For the first inequality, early improvements down to 1.510 1.510 came from trying and improving gradient-based optimization (e.g., using Adam with softmax parameterization). To reduce the bound from around 1.510 1.510 to 1.504 1.504 , the policy mostly used linear programming (LP), following the insights in Matolcsi and Vinuesa (2010) . The key insight for the later steps, that gradually achieved the state-of-the-art, was using heuristics to focus optimization only on the constraints that are close to being tight—where each constraint in the LP bounds one position of the convolution. Heuristics included picking the top K positions where the convolution was largest and only including those in the LP, as well as computing gradients from all near-maximum positions rather than just the single largest for gradient-based methods. Unlike AlphaEvolve Georgiev et al. (2025) , which mentions the authors suggested ideas such as using Newton type methods, we never intervened on the optimization process.

For a better comparison to the concurrent work, ThetaEvolve, we also report TTT-Discover with Qwen3-8B Yang et al. (2025) . The Qwen3-8B variant they used, DeepSeek-R1-0528-Qwen3-8B that was released by DeepSeek, is not available on Tinker. Thus, we used the original Qwen model ( Qwen/Qwen3-8B ) that was reportedly worse than the DeepSeek variant. ThetaEvolve reports using 65 65 steps with 512 512 rollouts ( 32 32 groups of 16 16 rollouts) each, however we do not modify our hyperparameters otherwise and keep 50 50 steps of 512 512 rollouts each. For both inequalities, TTT-Discover with Qwen3-8B certified tighter bounds than ThetaEvolve, using a worse model and a smaller sampling budget.

#### 4.1.3 Circle Packing

In Circle packing, the goal is to maximize the sum of radii of n n non-overlapping circles packed inside a unit square. We follow the setup from prior work Novikov et al. (2025) ; Georgiev et al. (2025) . The state s s is a list of circle centers and radii. The action a a consists of thinking tokens followed by Python code that optimizes circle positions and radii. The reward is the sum of radii achieved for valid packings, and 0 0 otherwise. We present the results below mostly for comparison purposes, as several recent works on evolutionary algorithms reported their performance using this task.

Table 3 shows results. TTT-Discover with Qwen3-8B matches the best known constructions for both n = 26 n=26 and n = 32 n=32 . We make no improvements here, but include these results for completeness. The algorithms found by TTT-Discover are presented in Appendix B.1 . Algorithms initialize circles in staggered or hexagonal grid arrangements, then refine positions and radii using sequential least squares programming with boundary and pairwise non-overlap constraints. This solution is a lot simpler than recent work, such as ShinkaEvolve Lange et al. (2025) , especially in terms of initialization, where their solution uses an initialization based on simulated annealing algorithm, while TTT-Discover initializes only with a simple geometric arrangement.

#### 4.1.4 Expert Review

### 4.2 Kernel Engineering

GPU kernels are the computational foundation of modern AI, every forward pass and backward pass ultimately executes as kernel code on hardware. We apply our method to GPU kernel optimization, where a new state-of-the-art kernel is a faster implementation than existing ones.

GPUMODE is an open community for kernel development that also hosts competitions for domain experts. We test our method on two competitions: TriMul (triangular matrix multiplication), a core primitive in AlphaFold’s architecture Jumper et al. (2021) , and DeepSeek MLA (Multi-head Latent Attention), a key component in DeepSeek’s inference stack Liu et al. (2024a) . Each GPU type for the TriMul competition (NVIDIA H100, A100, B200, AMD MI300X) has a separate leaderboard, as performant implementations differ across architectures. For The MLA competition there is only an MI300X leaderboard.

As these competitions were conducted earlier, we retrospectively evaluate our performance while respecting competition standards. We prefer GPUMODE because their leaderboards are well-tested through human competitions with a robust evaluation harness Zhang et al. (2025a) , and their benchmarks avoid signal-to-noise issues where simple operations or small inputs cause overheads to dominate runtime.

Environment: The state s s is a GPU kernel code. The action a a consists of thinking tokens followed by kernel code written in Triton Tillet et al. (2019) . The dynamics parse the code from the action: s ′ = Parse ​ ( a ) s^{\prime}=\texttt{Parse}(a) . For the initial state, we provide unoptimized kernels, detailed in Appendix C . The reward is proportional to the inverse of the geometric mean of runtimes on a fixed set of input shapes (following the leaderboard), or zero if the kernel fails correctness checks or times out. We evaluate runtime remotely on Modal to scale and ensure consistent hardware conditions. For TriMul, we evaluate the runtime only on H100s during training, even though we still evaluate the generated kernels for A100, B200, and MI300X for final report. Since MI300X is not available on Modal, for MLA-Decode we use H200s, and hope the kernels generalize to MI300X. Further details about the prompts and environments are in Appendix C .

Results. We report the runtime of the best kernels and the baselines in Table 4 . Our TriMul kernels achieve state-of-the-art across the board in all GPU types. For A100s, our best kernel is 50 % 50\% faster than the top human kernel, even though our reward function did not time the kernels on A100s. We uniformly achieve > 15 % >15\% improvement over the best human submissions for all GPU types. Finally, we submit to the official TriMul A100/H100 leaderboard 1 1 1 See leaderboards . For TriMul B200/MI300X and MLA-Decode MI300X tasks, due to an infra problem on GPU Mode’s server, we could not submit to the official leaderboard. .

The discovered kernels for Trimul identify heavy memory I/O incurred by frequent elementwise operations as a major bottleneck to optimize. Specifically, the kernels fuse: (i) operations in the input LayerNorm, (ii) sigmoid and elementwise multiplication in input gating, and (iii) operations in the output LayerNorm and gating. As for the most compute-heavy operation, which is the matmul with O ⁡ ( N 3 ) O(N^{3}) complexity, the kernels convert the inputs to FP16 and delegate the computation to cuBLAS/rocBLAS to effectively leverage TensorCores/MatrixCores of the hardwares.

Discovered MLA-Decode kernels. The kernels shown in table 5 mainly rely on torch.compile() for optimization. Specifically, they adopt a specific configuration of torch.compile . However, these kernels do not leverage Triton for fine-grained optimization, which may limit further improvements and more flexible use case. We additionally filter and evaluate generated kernels that explicitly use Triton despite their slightly slower runtime, and report in Appendix C .

#### 4.2.1 Expert Review

Below, we provide verbatim reviews from the GPUMode organizers for our TriMul competition kernels.

### 4.3 Algorithm Engineering

Hard optimization problems like package-delivery routing, crew scheduling, factory production planning, power-grid balancing—appear throughout industries and must be solved repeatedly at scale. We apply our method to these algorithm engineering problems, where a new state-of-the-art would be writing a higher-scoring algorithm than existing ones written by human experts.

AtCoder Heuristic Contest (AHC) is a series of programming competitions focused on optimization problems drawn from real-world industrial challenges AtCoder Inc. (2025) , attracting hundreds of participants including industry experts. We attempted to evaluate on two past contests, ahc039 and ahc058. ahc039 ("Purse Seine Fishing") is a computational geometry problem where you design a simple closed net on a 2D map, restricted to horizontal/vertical edges, to capture many target points while avoiding penalty points under a budget. ahc058 ("Apple Incremental Game") is a production planning problem where upgrades trade off immediate output versus growing future production capacity, and the goal is to schedule upgrades to maximize final output.

We select ahc039 because ShinkaEvolve Lange et al. (2025) reported a solution that would have placed 2nd, and ahc058 because Sakana AI’s ALE-Agent achieved the first-ever AI victory in an AHC Sakana AI (2026) . We use the evaluation harness from ALE-Bench Imajuku et al. (2025) . We use the public test case generator to create local tests, select our best-performing algorithm, and submit it to be scored on the official platform.

Environment: The state s s is an algorithm implementation in C++. The action a a consists of thinking tokens followed by C++ code. The dynamics parse the code from the action: s ′ = Parse ​ ( a ) s^{\prime}=\texttt{Parse}(a) . The reward is the score on locally generated test cases, or zero if the algorithm fails correctness checks or exceeds the time limit of 2 seconds and memory limit of 1024MB. We select the best-performing algorithm and submit it to be scored on the official private tests. We use the evaluation harness released by Imajuku et al. (2025) . For initial states, for the ahc039 competition we use the same initial program as Lange et al. (2025) , which is based on ALE-Agent Imajuku et al. (2025) best program, that would have placed 5th in the competition leaderboard. For ahc058 we start from scratch, similar to ALE-Agent Sakana AI (2026) .

Previous state-of-the-art. We report the top human submissions on each contest leaderboard. For AI baselines, we compare to ALE-Agent Imajuku et al. (2025) and ShinkaEvolve Lange et al. (2025) , which use ensembles of models including the gpt, Gemini, and Claude families of models. ALE-Agent Imajuku et al. (2025) starts from scratch for both problems. ShinkaEvolve Lange et al. (2025) reports results in ahc039 where they start from ALE-Agent solution, and improve it from 5th place to 2nd place.

Results. We report results in Table 6 . For both competitions, if we had submitted during competition time, our algorithms would have gotten the 1st place. For ahc039, we marginally improve upon the best human, while there is a significant gap between next best AI and human scores. For ahc039, we follow ShinkaEvolve by starting from the ALE-Agent solution and improve it from 5th place to 1st place, while ShinkaEvolve reaches the 2nd place using significantly more capable frontier models such as Gemini 2.5 Pro. For ahc058, we start from scratch and outscore all submissions in the competition.

For AHC039, the solution builds a large pool of promising axis-aligned rectangles using prefix sum scoring, then greedily seeds a connected union and uses simulated annealing with add, remove, replace, expand, shrink, and slide moves to optimize the rectangle union score under perimeter and vertex constraints, followed by cleanup and final greedy refinement.

For AHC058, the solution first builds several reasonable plans using greedy rules, different biases, and a short beam search to explore promising early decisions. Then, the program improves the best plan with simulated annealing that makes random edits, swaps, and partial rebuilds before finishing with a small local cleanup pass. It estimates the value of actions using a simple formula for how much future production an upgrade is likely to create, which guides both greedy choices and pruning. For performance, it caches intermediate states so it only recomputes parts of the plan that change. Overall, the program balances broad exploration early with focused local improvement later.

### 4.4 Single Cell Analysis

Single-cell RNA-sequencing (RNA-seq) aims to help us understand how organisms work and get sick by resolving biology at the level of individual cells; measuring which genes each cell is using to reveal cell types, states, and how they change. Practically, it isolates single cells, tags their mRNA with a Unique Molecular Identifier (UMI), sequences it, and outputs a per-cell gene-by-count table. RNA-seq protocols suffer from measurement noise in the observed UMI counts. Thus, denoising algorithms significantly increases the realized value of expensive experiments. Each sequencing run costs thousands of dollars, and better denoising methods reduce the need for deeper sequencing.

We apply our method to one of the recent benchmarks OpenProblems Luecken et al. (2025) , an important set of open problems for single-cell analysis. We use the denoising task therein. Batson et al. (2019) demonstrated that partitioning the observed molecules of a single dataset into training and test sets via binomial sampling and evaluating the denoised training set against the held-out test counts provides a proxy for accuracy against true expression values, providing an evaluation framework without requiring external ground truth data.

Environment. The state s s is an algorithm implementation. The action a a consists of thinking tokens followed by code. The dynamics parse the code from the action: s ′ = Parse ​ ( a ) s^{\prime}=\text{Parse}(a) . The benchmark evaluates denoising quality using two complementary metrics: mean squared error (MSE) in log-normalized space, which measures overall reconstruction accuracy, and Poisson negative log-likelihood, which assesses how well the denoised counts match the statistical properties expected of count data. In our context, the reward is the MSE score, or zero if it violates constraints we add for the Poisson score or the algorithm exceeds the time limit of 400 400 seconds. The Denoising benchmark offers 3 datasets: PBMC, Pancreas, and Tabula Muris Senis Lung, in order of size. We train our policy by using Pancreas in our environment, and ultimately performance is reported by running the algorithm on the held out PBMC and Tabula datasets.

Previous state-of-the-art. We report the state of the art as described by the OpenProblems Luecken et al. (2025) benchmark. The best result was provided by MAGIC Van Dijk et al. (2018) using an approximate solver and reversed normalization. MAGIC is a well known technique, frequently used in the literature Youssef et al. (2024) ; Venkat et al. (2025) , the only method different from MAGIC that provides good performance is ALRA Linderman et al. (2022) , ranked third. We also compare with OpenEvolve and Best-of-25600.

Results. The improved function obtained via TTT-Discover shows consistent improvements on both datasets (see Table 7 ). TTT-Discover is initialized with MAGIC code. TTT-Discover adds gene-adaptive transform ensembling, low-rank SVD refinement, and log-space polishing steps that directly optimize the benchmark metric.

#### 4.4.1 Expert Review

Below, we provide a verbatim review from Prof. Eric Sun.

### 4.5 Ablations

We have three sets of ablations. First, we ablate the design choices for the train method, while keeping our reuse method, PUCT, fixed. We test (i) TTT with entropic objective using constant β = 2 \beta=2 ( Jiang et al. (2025) ), (ii) TTT with no entropic objective (expected reward), (iii) No TTT (only reuse). Second, we ablate the choice of the Reuse method , while keeping our train method, TTT with entropic objective using adaptive β \beta , fixed. We replace PUCT with (i) ϵ − \epsilon- greedy reuse with ϵ = 0.1 \epsilon=0.1 as this is perhaps the most naive reuse method, and (ii) no reuse. Finally, we report the naive RL baseline, where we use the expected reward objective with no reuse, and the Best-of- 25600 25600 baseline.

For each ablation, we report the runtime of the best kernel found in Table 8 , and the reward distribution in Figure 4 . The rewards distributions and best kernel runtimes are computed with our evaluator, not the leaderboard.

Only the full TTT-Discover algorithm achieves the best performance in the TriMul competition. When using a constant β \beta , the improvements diminish later in the training. Using the expected reward objective, improvements are slower overall. Without any test-time training, both the mean reward and the max reward stagnates. ϵ \epsilon -greedy reuse works reasonably well, especially with an early lucky kernel. In early experiments with other applications, the lack of exploration was also a bigger problem than it is in kernel engineering tasks. Naive RL and no reuse make minimal improvements.

It is entirely possible that additional tuning (e.g., a task-specific β \beta schedule) or hyperparameter interactions (e.g., batch size and reuse) can provide improvements in the ablation configurations. For each component, many additional knobs could be ablated (e.g., PUCT exploration bonus, learning rate, batch size). However, our focus was on identifying design choices that works reliably across diverse applications within our budget with minimal task-specific tuning. In practice, the key hyperparameters such as learning rate, batch size, and LoRA rank were fixed after the initial iterations of the project.

## 5 Related Works

In this section, we first provide a broad overview of continual learning and test-time training, using some of the exposition in Tandon et al. (2025) . Then towards the end of § 5.2 , we discuss the most relevant work on test-time training: MiGrATe Phan et al. (2025) and ThetaEvolve Wang et al. (2025a) . Finally, we discuss two pieces of work with tangential formulations: RL on a single training problem that is not the test problem Wang et al. (2025b) (§ 5.3 ), and RL on the entire test set Zuo et al. (2025) (§ 5.4 ).

### 5.1 Continual Learning

Most of today’s AI systems remain static after deployment, even though the world keeps changing. The high-level goal of continual learning is to enable AI systems to keep changing with the world, similar to how humans improve throughout their lives Hassabis et al. (2017) ; De Lange et al. (2021) .

Conventionally, continual learning as a research field has focused on learning from a distribution that gradually changes over time Lopez-Paz and Ranzato (2017) ; Van de Ven and Tolias (2019) ; Hadsell et al. (2020) . For example, one could update a chatbot model every hour using new knowledge from the Internet, while typical use cases of the model may require knowledge from both the past and the present Scialom et al. (2022) ; Ke et al. (2023) ; Wang et al. (2024) . More formally, at each timestep, we sample new training and test data from the current distribution, update our model using the new training data, and then evaluate it on all the test data up to the current timestep. Under this setting, most algorithms focus on not forgetting the past when learning from the present Santoro et al. (2016) ; Li and Hoiem (2017) ; Kirkpatrick et al. (2017) ; Gidaris and Komodakis (2018) .

### 5.2 Test-Time Training

The algorithmic framework of test-time training has the same high-level goal as continual learning, but it focuses on two aspects where human learning stands out from the forms of continual learning in the conventional literature.

First, each person has a unique brain that learns within the context of their individual life. This personalized form of continual learning is quite different from, for example, the chatbot model that is fine-tuned hourly using the latest information available worldwide. While such a model does change over time, it is still the same at any given moment for every user and every problem instance.

Second, most human learning happens without a boundary between training and testing. Consider your commute to work this morning. It is both "testing" because you did care about getting to work this very morning, and "training" because you were also gaining experience for future commutes. But in machine learning, the train-test split has always been a fundamental concept.

The concept of test-time training is introduced to realize these two special aspects of human learning. Training typically involves formulating a learning problem (such as empirical risk minimization) and then solving it. Following Sun et al. (2023) , test-time training is defined as any kind of training that formulates a potentially different learning problem based on each individual test instance.

This concept has a rich history in AI. A well-known example in NLP is dynamic evaluation, pioneered by Mikolov et al. Mikolov et al. (2013) and extended by Krause et al. Krause et al. (2018) . In computer vision, early examples have also emerged in applications such as face detection Jain and Learned-Miller (2011) , video segmentation Mullapudi et al. (2018) , super-resolution Shocher et al. (2018) , and 3D reconstruction Luo et al. (2020) . Next, we discuss three popular forms of test-time training today, with an emphasis on their connections to each other and to historical examples.

#### 5.2.1 TTT on Nearest Neighbors: Larger Effective Capacity

One simple form of test-time training was called locally weighted regression in the 1970s Stone (1977) ; Cleveland (1979) , local learning in the 1990s Bottou and Vapnik (1992) , and KNN-SVM in the 2000s Zhang et al. (2006) : Given a test instance, find its nearest neighbors in the training set, and then train (or fine-tune) the model on these neighbors before making a prediction. This procedure can significantly increase the effective capacity of the model; for example, it allows a linear model to fit a highly nonlinear ground truth Stone (1977) .

This simple form captures one of the key intuitions of test-time training. In the conventional view of machine learning, a model, once trained, no longer changes at test time. As a consequence, it must prepare to be good at all possible inputs in the future. This task can be very hard, because being good at all possible futures limits the model’s capacity to be good at any particular one. But only one future is actually going to happen. So why not train our model once this future happens?

Recently, Hardt and Sun (2023) extended this idea to modern language models and observed a similar benefit of larger effective model capacity after test-time training, and Hübotter et al. (2024) further improved these results through better strategies for neighbor selection. In addition, Hübotter et al. (2025) showed that test-time training on neighbors from the training set is also effective with RL for reasoning tasks, and Bagatella et al. (2025) developed the same idea for visual-motor tasks.

#### 5.2.2 TTT for Novel Instances: Better Generalization

As models become larger today, their competence is often limited not by their capacity, but by the amount of available training data, especially when they need to generalize to novel test instances that are “out-of-distribution”. In this case, it is even harder to prepare for all possible test instances in the future, especially the novel ones, with a static model. But once a specific test instance is given, we can use it to generate relevant data, which we can then use for training Sun et al. (2020) . In other words, the “neighbors” for TTT do not have to come from the training set; they can also be generated on-the-fly.

Since the test instance is unlabeled, one way to make it useful for training is through self-supervision, which generates new pairs of inputs and labels for an auxiliary task such as masked reconstruction (e.g., BERT Devlin et al. (2018) and MAE He et al. (2021) ). While the auxiliary task is different from the main prediction task, improving performance in one can help the other through their shared representations. This form of TTT can significantly improve generalization under distribution shifts Sun et al. (2020) ; Gandelsman et al. (2022) .

Recently, TTT has been an important part of AlphaProof Hubert et al. (2025) , which achieved IMO silver-medal standard in 2024. Given each test problem, their system first generates a targeted curriculum of easier problems by prompting a language model, and then performs reinforcement learning on the generated data. Another recent work, Akyurek et al. Akyürek et al. (2024) , found TTT effective for few-shot reasoning tasks such as ARC-AGI. Their system generates augmentations of the few-shot demonstrations in the test problem then performs supervised learning. In Li et al. (2025) , authors perform policy gradients at test time using the policy itself as an evaluator of solutions, similar to using LMs as a judge. Further, they optimize token representations with policy gradients, as opposed to optimizing the policy.

Three closest and concurrent works perform test-time training: MiGrATe Phan et al. (2025) , ThetaEvolve Wang et al. (2025a) , and EvoTune Surina et al. (2025) . All three combine per-instance RL updates with various replay/reuse mechanisms, and typically use PPO/GRPO/DPO-style updates for LMs Schulman et al. (2017) ; Guo et al. (2025) ; Rafailov et al. (2023) . Relative to Phan et al. (2025) ; Surina et al. (2025) , our contribution is to tailor both the learning objective and the reuse rule to the discovery goal, rather than largely standard RL or evolutionary baselines; also test in more realistic discovery tasks with human expert baselines. Compared to ThetaEvolve, TTT-Discover using the same model and compute budget still produces significant improvements (Table 2 ), which we attribute to our entropic objective and PUCT-based reuse instead of more complicated and brittle heuristics in evolutionary algorithms.

In an earlier work Bello et al. (2016) , the authors train a neural policy with policy gradients to directly output solutions to combinatorial problems like TSP, using (negative) tour length as reward, and they study both training across many instances and per-instance learning at test time.

### 5.3 RL on One Example

One Example RL Wang et al. (2025b) is relevant as they also train on a single problem. To be specific, they train on one example from a dataset, such as the MATH training set. They show that a policy trained with on one such problem with RL generalizes to other problems in the same dataset. In contrast, TTT-Discover trains on the test problem itself, where the goal is not to generalize but to solve this specific problem.

### 5.4 RL on the Test Set

TTRL Zuo et al. (2025) trains on an entire test set of problems using majority voting as pseudo-labels for reward estimation. In contrast, TTT-Discover trains on a single test problem with a continuous verifiable reward, where the goal is not to improve average performance across a set of problems but to find one exceptional solution.

## 6 Future Work

The current form of our method can only be applied to problems with continuous rewards, and the most important direction for future work is test-time training for problems with sparse or binary rewards, or problems in non-verifiable domains.

## Acknowledgments

We thank Matej Sirovatka, Davide Torlo, Eric Sun, Alex Zhang, Mark Saroufim, for reviewing our results and letting us cite their reviews in this paper. We would like to thank Amanda Moran and Nvidia for their support with the compute infrastructure; Charles Frye and Modal team, Clare Birch, John Schulman, Tianyi Zhang, Yangjun Ruan, and Thinking Machines Lab team for compute credits supporting this project; Anika Gupta, Zacharie Bugaud, and the broader Astera Institute for their support in various phases of the project; Matej Sirovatka, Alex Zhang, Mark Saroufim and the broader GPUMode community, and Simon Guo for their support in various phases of this project. We thank Mehmet Hamza Erol and Vipul Sharma for their short-term contributions. We thank Luke Bailey for feedback on this draft. Mert would like to thank Begum Ergun, Fatih Dinc, Omer Faruk Akgun, Ramiz Colak, Yigit Korkmaz for their support at every phase of this project.

## References

[1] S. Agarwal, L. Ahmad, J. Ai, S. Altman, A. Applebaum, E. Arbus, R. K. Arora, Y. Bai, B. Baker, H. Bao, et al. (2025) Gpt-oss-120b & gpt-oss-20b model card . arXiv preprint arXiv:2508.10925 . Cited by: Table 9 , §3.3 .

[2] E. Akyürek, M. Damani, A. Zweiger, L. Qiu, H. Guo, J. Pari, Y. Kim, and J. Andreas (2024) The surprising effectiveness of test-time training for few-shot learning . arXiv preprint arXiv:2411.07279 . Cited by: §5.2.2 .

[3] AtCoder Inc. (2025) AtCoder . Note: https://atcoder.jp Cited by: §4.3 .

[4] M. Bagatella, M. Albaba, J. Hübotter, G. Martius, and A. Krause (2025) Test-time offline reinforcement learning on goal-related experience . arXiv preprint arXiv:2507.18809 . Cited by: §5.2.1 .

[5] R. C. Barnard and S. Steinerberger (2020) Three convolution inequalities on the real line with connections to additive combinatorics . Journal of Number Theory 207 , pp. 42–55 . Cited by: §4.1.2 .

[6] J. Batson, L. Royer, and J. Webber (2019) Molecular cross-validation for single-cell rna-seq . BioRxiv , pp. 786269 . Cited by: §4.4 .

[7] I. Bello, H. Pham, Q. V. Le, M. Norouzi, and S. Bengio (2016) Neural combinatorial optimization with reinforcement learning . arXiv preprint arXiv:1611.09940 . Cited by: §5.2.2 .

[8] L. Bottou and V. Vapnik (1992) Local learning algorithms . Neural computation 4 ( 6 ), pp. 888–900 . Cited by: §5.2.1 .

[9] C. Boyer and Z. K. Li (2025) An improved example for an autoconvolution inequality . arXiv preprint arXiv:2506.16750 . Cited by: §4.1.2 .

[10] W. S. Cleveland (1979) Robust locally weighted regression and smoothing scatterplots . Journal of the American statistical association 74 ( 368 ), pp. 829–836 . Cited by: §5.2.1 .

[11] M. De Lange, R. Aljundi, M. Masana, S. Parisot, X. Jia, A. Leonardis, G. Slabaugh, and T. Tuytelaars (2021) A continual learning survey: defying forgetting in classification tasks . IEEE transactions on pattern analysis and machine intelligence 44 ( 7 ), pp. 3366–3385 . Cited by: §5.1 .

[12] J. Devlin, M. Chang, K. Lee, and K. Toutanova (2018) Bert: pre-training of deep bidirectional transformers for language understanding . arXiv preprint arXiv:1810.04805 . Cited by: §5.2.2 .

[13] Y. Gandelsman, Y. Sun, X. Chen, and A. A. Efros (2022) Test-time training with masked autoencoders . Advances in Neural Information Processing Systems . Cited by: §5.2.2 .

[14] B. Georgiev, J. Gómez-Serrano, T. Tao, and A. Z. Wagner (2025) Mathematical exploration and discovery at scale . arXiv preprint arXiv:2511.02864 . Cited by: §4.1.1 , §4.1.2 , §4.1.3 , §4.1 , Table 2 , Table 3 , §4 .

[15] S. Gidaris and N. Komodakis (2018) Dynamic few-shot visual learning without forgetting . In Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition , pp. 4367–4375 . Cited by: §5.1 .

[16] D. Guo, D. Yang, H. Zhang, J. Song, P. Wang, Q. Zhu, R. Xu, R. Zhang, S. Ma, X. Bi, et al. (2025) Deepseek-r1 incentivizes reasoning in llms through reinforcement learning . Nature 645 ( 8081 ), pp. 633–638 . Cited by: §3.1 , §5.2.2 .

[17] R. Hadsell, D. Rao, A. A. Rusu, and R. Pascanu (2020) Embracing change: continual learning in deep neural networks . Trends in cognitive sciences 24 ( 12 ), pp. 1028–1040 . Cited by: §5.1 .

[18] M. Hardt and Y. Sun (2023) Test-time training on nearest neighbors for large language models . arXiv preprint arXiv:2305.18466 . Cited by: §5.2.1 .

[19] D. Hassabis, D. Kumaran, C. Summerfield, and M. Botvinick (2017) Neuroscience-inspired artificial intelligence . Neuron 95 ( 2 ), pp. 245–258 . Cited by: §5.1 .

[20] J. K. Haugland (2016) The minimum overlap problem revisited . arXiv preprint arXiv:1609.08000 . Cited by: Figure 1 , Figure 2 , Figure 2 , §4.1.1 , §4.1.1 .

[21] K. He, X. Chen, S. Xie, Y. Li, P. Dollár, and R. B. Girshick (2021) Masked autoencoders are scalable vision learners . CoRR abs/2111.06377 . External Links: 2111.06377 Cited by: §5.2.2 .

[22] D. Hendrycks, S. Basart, N. Mu, S. Kadavath, F. Wang, E. Dorundo, R. Desai, T. Zhu, S. Parajuli, M. Guo, D. Song, J. Steinhardt, and J. Gilmer (2021) The many faces of robustness: a critical analysis of out-of-distribution generalization . ICCV . Cited by: §1 .

[23] E. J. Hu, Y. Shen, P. Wallis, Z. Allen-Zhu, Y. Li, S. Wang, L. Wang, W. Chen, et al. (2022) Lora: low-rank adaptation of large language models. . ICLR 1 ( 2 ), pp. 3 . Cited by: Table 9 , §3.3 .

[24] T. Hubert, R. Mehta, L. Sartran, and et al. (2025) Olympiad-level formal mathematical reasoning with reinforcement learning . Nature . Cited by: §5.2.2 .

[25] J. Hübotter, S. Bongni, I. Hakimi, and A. Krause (2024) Efficiently learning at test-time: active fine-tuning of llms . arXiv preprint arXiv:2410.08020 . Cited by: §5.2.1 .

[26] J. Hübotter, L. Diaz-Bone, I. Hakimi, A. Krause, and M. Hardt (2025) Learning on the job: test-time curricula for targeted reinforcement learning . arXiv preprint arXiv:2510.04786 . Cited by: §5.2.1 .

[27] Y. Imajuku, K. Horie, Y. Iwata, K. Aoki, N. Takahashi, and T. Akiba (2025) ALE-bench: a benchmark for long-horizon objective-driven algorithm engineering . arXiv preprint arXiv:2506.09050 . Cited by: §4.3 , §4.3 , §4.3 , Table 6 , §4 .

[28] V. Jain and E. Learned-Miller (2011) Online domain adaptation of a pre-trained cascade of classifiers . In CVPR 2011 , pp. 577–584 . Cited by: §5.2 .

[29] Y. Jiang, J. Huang, Y. Yuan, X. Mao, Y. Yue, Q. Zhao, and L. Yan (2025) Risk-sensitive rl for alleviating exploration dilemmas in large language models . arXiv preprint arXiv:2509.24261 . Cited by: §A.1 , §A.1 , §3.2 , §3.2 , §4.5 .

[30] J. Jumper, R. Evans, A. Pritzel, T. Green, M. Figurnov, O. Ronneberger, K. Tunyasuvunakool, R. Bates, A. Žídek, A. Potapenko, et al. (2021) Highly accurate protein structure prediction with alphafold . nature 596 ( 7873 ), pp. 583–589 . Cited by: §1 , §4.2 .

[31] Z. Ke, Y. Shao, H. Lin, T. Konishi, G. Kim, and B. Liu (2023) Continual pre-training of language models . arXiv preprint arXiv:2302.03241 . Cited by: §5.1 .

[32] D. P. Kingma and J. Ba (2014) Adam: a method for stochastic optimization . arXiv preprint arXiv:1412.6980 . Cited by: Table 9 .

[33] J. Kirkpatrick, R. Pascanu, N. Rabinowitz, J. Veness, G. Desjardins, A. A. Rusu, K. Milan, J. Quan, T. Ramalho, A. Grabska-Barwinska, et al. (2017) Overcoming catastrophic forgetting in neural networks . Proceedings of the national academy of sciences 114 ( 13 ), pp. 3521–3526 . Cited by: §5.1 .

[34] P. W. Koh, S. Sagawa, H. Marklund, S. M. Xie, M. Zhang, A. Balsubramani, W. Hu, M. Yasunaga, R. L. Phillips, I. Gao, et al. (2021) Wilds: a benchmark of in-the-wild distribution shifts . In International conference on machine learning , pp. 5637–5664 . Cited by: §1 .

[35] B. Krause, E. Kahembwe, I. Murray, and S. Renals (2018) Dynamic evaluation of neural sequence models . In International Conference on Machine Learning , pp. 2766–2775 . Cited by: §5.2 .

[36] T. M. Lab (2025) Tinker . External Links: Link Cited by: §3.3 .

[37] R. T. Lange, Y. Imajuku, and E. Cetin (2025) Shinkaevolve: towards open-ended and sample-efficient program evolution . arXiv preprint arXiv:2509.19349 . Cited by: Figure 1 , §1 , §2.2 , §4.1.3 , §4.1 , §4.3 , §4.3 , §4.3 , Table 3 , Table 6 .

[38] H. Li, C. Li, T. Wu, X. Zhu, Y. Wang, Z. Yu, E. H. Jiang, S. Zhu, Z. Jia, Y. N. Wu, et al. (2025) Seek in the dark: reasoning via test-time instance-level policy gradient in latent space . arXiv preprint arXiv:2505.13308 . Cited by: §5.2.2 .

[39] Z. Li and D. Hoiem (2017) Learning without forgetting . IEEE transactions on pattern analysis and machine intelligence 40 ( 12 ), pp. 2935–2947 . Cited by: §5.1 .

[40] G. C. Linderman, J. Zhao, M. Roulis, P. Bielecki, R. A. Flavell, B. Nadler, and Y. Kluger (2022) Zero-preserving imputation of single-cell rna-seq data . Nature communications 13 ( 1 ), pp. 192 . Cited by: §4.4 , Table 7 .

[41] A. Liu, B. Feng, B. Xue, B. Wang, B. Wu, C. Lu, C. Zhao, C. Deng, C. Zhang, C. Ruan, et al. (2024) Deepseek-v3 technical report . arXiv preprint arXiv:2412.19437 . Cited by: §4.2 .

[42] F. Liu, R. Zhang, Z. Xie, R. Sun, K. Li, X. Lin, Z. Wang, Z. Lu, and Q. Zhang (2024) Llm4ad: a platform for algorithm design with large language model . arXiv preprint arXiv:2412.17287 . Cited by: §2.2 .

[43] D. Lopez-Paz and M. Ranzato (2017) Gradient episodic memory for continual learning . In Advances in Neural Information Processing Systems , pp. 6467–6476 . Cited by: §5.1 .

[44] M. D. Luecken, S. Gigante, D. B. Burkhardt, R. Cannoodt, D. C. Strobl, N. S. Markov, L. Zappia, G. Palla, W. Lewis, D. Dimitrov, et al. (2025) Defining and benchmarking open problems in single-cell analysis . Nature Biotechnology , pp. 1–6 . Cited by: Appendix E , §4.4 , §4.4 .

[45] X. Luo, J. Huang, R. Szeliski, K. Matzen, and J. Kopf (2020) Consistent video depth estimation . ACM Transactions on Graphics (ToG) 39 ( 4 ), pp. 71–1 . Cited by: §5.2 .

[46] M. Matolcsi and C. Vinuesa (2010) Improved bounds on the supremum of autoconvolutions . Journal of Mathematical Analysis and Applications 372 ( 2 ), pp. 439–447 . Cited by: §4.1.2 , §4.1.2 , §4.1.2 .

[47] T. Mikolov, K. Chen, G. Corrado, and J. Dean (2013) Efficient estimation of word representations in vector space . arXiv preprint arXiv:1301.3781 . Cited by: §5.2 .

[48] J. Miller, K. Krauth, B. Recht, and L. Schmidt (2020) The effect of natural distribution shift on question answering models . In International conference on machine learning , pp. 6905–6916 . Cited by: §1 .

[49] R. T. Mullapudi, S. Chen, K. Zhang, D. Ramanan, and K. Fatahalian (2018) Online model distillation for efficient video inference . arXiv preprint arXiv:1812.02699 . Cited by: §5.2 .

[50] A. Novikov, N. Vũ, M. Eisenberger, E. Dupont, P. Huang, A. Z. Wagner, S. Shirobokov, B. Kozlovskii, F. J. Ruiz, A. Mehrabian, et al. (2025) AlphaEvolve: a coding agent for scientific and algorithmic discovery . arXiv preprint arXiv:2506.13131 . Cited by: Figure 1 , §1 , §2.1 , §2.2 , §2.2 , §4.1.1 , §4.1.1 , §4.1.1 , §4.1.3 , §4.1 , §4.1 , Table 2 , Table 3 , §4 , §4 .

[51] J. Peters, K. Muelling, and Y. Altun (2010) Relative entropy policy search . In Proceedings of 24th AAAI Conference on Artificial Intelligence (AAAI ’10) , pp. 1607–1612 . Cited by: §A.1 .

[52] P. Phan, D. Agarwal, K. Srinivas, H. Samulowitz, P. Kapanipathi, and A. McCallum (2025) MiGrATe: mixed-policy grpo for adaptation at test-time . arXiv preprint arXiv:2508.08641 . Cited by: §1 , §5.2.2 , §5 .

[53] R. Rafailov, A. Sharma, E. Mitchell, C. D. Manning, S. Ermon, and C. Finn (2023) Direct preference optimization: your language model is secretly a reward model . Advances in neural information processing systems 36 , pp. 53728–53741 . Cited by: §5.2.2 .

[54] M. T. Ribeiro, T. Wu, C. Guestrin, and S. Singh (2020) Beyond accuracy: behavioral testing of nlp models with checklist . arXiv preprint arXiv:2005.04118 . Cited by: §1 .

[55] C. D. Rosin (2011) Multi-armed bandits with episode context . Annals of Mathematics and Artificial Intelligence 61 ( 3 ), pp. 203–230 . Cited by: §A.2 , §3.2 .

[56] Sakana AI (2026) Sakana ai agent wins atcoder heuristic contest (first ai to place 1st) . Note: https://sakana.ai/ahc058/ Cited by: §1 , §4.3 , §4.3 , §4 .

[57] Sakana (2024) Submission #59660035 — third programming contest 2024 (atcoder heuristic contest 039) . AtCoder . Note: https://atcoder.jp/contests/ahc039/submissions/59660035 AtCoder Heuristic Contest 039 submission page Cited by: Figure 1 .

[58] A. Santoro, S. Bartunov, M. Botvinick, D. Wierstra, and T. Lillicrap (2016) Meta-learning with memory-augmented neural networks . In International conference on machine learning , pp. 1842–1850 . Cited by: §5.1 .

[59] J. Schulman, F. Wolski, P. Dhariwal, A. Radford, and O. Klimov (2017) Proximal policy optimization algorithms . arXiv preprint arXiv:1707.06347 . Cited by: §3.1 , §3.2 , §5.2.2 .

[60] T. Scialom, T. Chakrabarty, and S. Muresan (2022) Fine-tuned language models are continual learners . arXiv preprint arXiv:2205.12393 . Cited by: §5.1 .

[61] A. Sharma (2025) OpenEvolve: an open-source evolutionary coding agent . GitHub . External Links: Link Cited by: Table 2 , §4 .

[62] A. Shocher, N. Cohen, and M. Irani (2018) “Zero-shot” super-resolution using deep internal learning . In Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition , pp. 3118–3126 . Cited by: §5.2 .

[63] D. Silver, A. Huang, C. J. Maddison, A. Guez, L. Sifre, G. van den Driessche, J. Schrittwieser, I. Antonoglou, V. Panneershelvam, M. Lanctot, S. Dieleman, D. Grewe, J. Nham, N. Kalchbrenner, I. Sutskever, T. Lillicrap, M. Leach, K. Kavukcuoglu, T. Graepel, and D. Hassabis (2016) Mastering the game of Go with deep neural networks and tree search . Nature 529 ( 7587 ), pp. 484–489 . External Links: Document Cited by: §A.2 , §3.2 .

[64] D. Silver, T. Hubert, J. Schrittwieser, I. Antonoglou, M. Lai, A. Guez, M. Lanctot, L. Sifre, D. Kumaran, T. Graepel, et al. (2018) A general reinforcement learning algorithm that masters chess, shogi, and go through self-play . Science 362 ( 6419 ), pp. 1140–1144 . Cited by: §A.2 , §A.2 , §3.2 .

[65] D. Silver, J. Schrittwieser, K. Simonyan, I. Antonoglou, A. Huang, A. Guez, T. Hubert, L. Baker, M. Lai, A. Bolton, Y. Chen, T. Lillicrap, F. Hui, L. Sifre, G. van den Driessche, T. Graepel, and D. Hassabis (2017) Mastering the game of Go without human knowledge . Nature 550 ( 7676 ), pp. 354–359 . External Links: Document Cited by: §A.2 , §A.2 , §1 , §3.2 .

[66] C. J. Stone (1977) Consistent nonparametric regression . The annals of statistics , pp. 595–620 . Cited by: §5.2.1 .

[67] Y. Sun, X. Li, K. Dalal, C. Hsu, S. Koyejo, C. Guestrin, X. Wang, T. Hashimoto, and X. Chen (2023) Learning to (learn at test time) . arXiv preprint arXiv:2310.13807 . Cited by: §5.2 .

[68] Y. Sun, X. Wang, Z. Liu, J. Miller, A. Efros, and M. Hardt (2020) Test-time training with self-supervision for generalization under distribution shifts . In International Conference on Machine Learning , pp. 9229–9248 . Cited by: §1 , §5.2.2 , §5.2.2 .

[69] A. Surina, A. Mansouri, L. Quaedvlieg, A. Seddas, M. Viazovska, E. Abbe, and C. Gulcehre (2025) Algorithm discovery with llms: evolutionary search meets reinforcement learning . arXiv preprint arXiv:2504.05108 . Cited by: §1 , §5.2.2 .

[70] R. Sutton (2019) The bitter lesson . Incomplete Ideas (blog) 13 ( 1 ), pp. 38 . Cited by: §1 .

[71] A. Tandon, K. Dalal, X. Li, D. Koceja, M. Rød, S. Buchanan, X. Wang, J. Leskovec, S. Koyejo, T. Hashimoto, et al. (2025) End-to-end test-time training for long context . arXiv preprint arXiv:2512.23675 . Cited by: §5 .

[72] Y. Tang and R. Munos (2025) On a few pitfalls in kl divergence gradient estimation for rl . arXiv preprint arXiv:2506.09477 . Cited by: §3.2 .

[73] P. Tillet, H. Kung, and D. Cox (2019) Triton: an intermediate language and compiler for tiled neural network computations . In Proceedings of the 3rd ACM SIGPLAN International Workshop on Machine Learning and Programming Languages , pp. 10–19 . Cited by: §4.2 .

[74] G. M. Van de Ven and A. S. Tolias (2019) Three scenarios for continual learning . arXiv preprint arXiv:1904.07734 . Cited by: §5.1 .

[75] D. Van Dijk, R. Sharma, J. Nainys, K. Yim, P. Kathail, A. J. Carr, C. Burdziak, K. R. Moon, C. L. Chaffer, D. Pattabiraman, et al. (2018) Recovering gene interactions from single-cell data using data diffusion . Cell 174 ( 3 ), pp. 716–729 . Cited by: §4.4 , Table 7 .

[76] A. Venkat, S. E. Youlten, B. P. San Juan, C. A. Purcell, S. Gupta, M. Amodio, D. P. Neumann, J. G. Lock, A. E. Westacott, C. S. McCool, et al. (2025) AAnet resolves a continuum of spatially-localized cell states to unveil intratumoral heterogeneity . Cancer Discovery . Cited by: §4.4 .

[77] L. Wang, X. Zhang, H. Su, and J. Zhu (2024) A comprehensive survey of continual learning: theory, method and application . IEEE transactions on pattern analysis and machine intelligence 46 ( 8 ), pp. 5362–5383 . Cited by: §5.1 .

[78] Y. Wang, S. Su, Z. Zeng, E. Xu, L. Ren, X. Yang, Z. Huang, X. He, L. Ma, B. Peng, et al. (2025) ThetaEvolve: test-time learning on open problems . arXiv preprint arXiv:2511.23473 . Cited by: §1 , §4.1 , Table 2 , Table 3 , §4 , §5.2.2 , §5 .

[79] Y. Wang, Q. Yang, Z. Zeng, L. Ren, L. Liu, B. Peng, H. Cheng, X. He, K. Wang, J. Gao, et al. (2025) Reinforcement learning for reasoning in large language models with one training example . arXiv preprint arXiv:2504.20571 . Cited by: §5.3 , §5 .

[80] E. P. White (2023) A new bound for Erdős’ minimum overlap problem . Acta Arithmetica 208 , pp. 235–255 . Cited by: §4.1.1 .

[81] A. Yang, A. Li, B. Yang, B. Zhang, B. Hui, B. Zheng, B. Yu, C. Gao, C. Huang, C. Lv, et al. (2025) Qwen3 technical report . arXiv preprint arXiv:2505.09388 . Cited by: §4.1.2 .

[82] F. Yao, L. Liu, D. Zhang, C. Dong, J. Shang, and J. Gao Your efficient rl framework secretly brings you off-policy rl training, august 2025 . URL https://fengyao. notion. site/off-policy-rl . Cited by: §3.3 .

[83] K. K. Youssef, N. Narwade, A. Arcas, A. Marquez-Galera, R. Jiménez-Castaño, C. Lopez-Blau, H. Fazilaty, D. García-Gutierrez, A. Cano, J. Galcerán, et al. (2024) Two distinct epithelial-to-mesenchymal transition programs control invasion and inflammation in segregated tumor cell populations . Nature Cancer 5 ( 11 ), pp. 1660–1680 . Cited by: §4.4 .

[84] M. Yuksekgonul, F. Bianchi, J. Boen, S. Liu, P. Lu, Z. Huang, C. Guestrin, and J. Zou (2025) Optimizing generative ai by backpropagating language model feedback . Nature 639 ( 8055 ), pp. 609–616 . Cited by: §1 , §2.2 .

[85] A. L. Zhang, M. Sirovatka, E. Schultheis, B. Horowitz, and M. Saroufim (2025) KernelBot: a competition platform for writing heterogeneous GPU code . In Championing Open-source DEvelopment in ML Workshop @ ICML25 , External Links: Link Cited by: §4.2 .

[86] H. Zhang, A. C. Berg, M. Maire, and J. Malik (2006) SVM-knn: discriminative nearest neighbor classification for visual category recognition . In 2006 IEEE Computer Society Conference on Computer Vision and Pattern Recognition (CVPR’06) , Vol. 2 , pp. 2126–2136 . Cited by: §5.2.1 .

[87] Y. Zhang, Y. Liu, H. Yuan, Y. Yuan, Q. Gu, and A. C. Yao (2025) On the design of kl-regularized policy gradient algorithms for llm reasoning . arXiv preprint arXiv:2505.17508 . Cited by: §3.2 .

[88] Y. Zuo, K. Zhang, L. Sheng, S. Qu, G. Cui, X. Zhu, H. Li, Y. Zhang, X. Long, E. Hua, et al. (2025) Ttrl: test-time reinforcement learning . arXiv preprint arXiv:2504.16084 . Cited by: §5.4 , §5 .

## Appendix A Training details

Our hyperparameters are fixed throughout almost all experiment. For almost all applications we used a KL penalty coefficient of 0.1 0.1 . For algorithm engineering, we used a KL coefficient of 0.01 0.01 . We present details on our objective function and the reuse algorithm below.

### A.1 Entropic utility objective

We define the entropic utility objective explored also in the concurrent work [ 29 ] : J β ( θ ; s ) 𝐵 log E τ ∼ π θ ( ⋅ ∣ s ) [ e β ​ r ​ ( τ , s ) ] . J_{\beta}(\theta;s)\;\coloneqq\;\log\mathbb{E}_{\tau\sim\pi_{\theta}(\cdot\mid s)}\!\left[e^{\beta r(\tau;s)}\right].

The gradient of this objective yields ∇ θ J β ( θ ; s ) = E τ ∼ π θ ( ⋅ ∣ s ) [ ∇ θ log π θ ( τ ∣ s ) w β ( τ ∣ s ) ] , w β ( τ ∣ s ) = e β ​ r ​ ( τ , s ) E π θ ​ [ e β ​ r ​ ( τ , s ) ] , A β ( τ ∣ s ) = w β ( τ ∣ s ) − 1 , \nabla_{\theta}J_{\beta}(\theta;s)=\mathbb{E}_{\tau\sim\pi_{\theta}(\cdot\mid s)}\!\left[\nabla_{\theta}\log\pi_{\theta}(\tau\mid s)\;w_{\beta}(\tau\mid s)\right],\quad w_{\beta}(\tau\mid s)\;=\;\frac{e^{\beta r(\tau;s)}}{\mathbb{E}_{\pi_{\theta}}[e^{\beta r(\tau;s)}]},\quad A_{\beta}(\tau\mid s)\;=\;w_{\beta}(\tau\mid s)-1, since E π θ ​ [ w β ​ ( τ ∣ s ) ] = 1 \mathbb{E}_{\pi_{\theta}}[w_{\beta}(\tau\mid s)]=1 , we get A β A_{\beta} as the mean baselined advantage. The remaining question is how to set β \beta . [ 29 ] recommends value β = 2 \beta=2 , yet we found it tricky to set it. Later in the training, improvements become harder, and unless β \beta is adjusted carefully advantages can become very small. Early in the training, a large β \beta can cause instabilities.

Adaptive β \beta . Define the auxiliary tilted distribution induced by the entropic weights, q β ​ ( τ ∣ s ) = π θ ​ ( τ ∣ s ) ​ exp ⁡ ( β ​ r ​ ( τ , s ) ) E π θ ​ [ exp ⁡ ( β ​ r ​ ( τ , s ) ) ] , w β ​ ( τ ∣ s ) = q β ​ ( τ ∣ s ) π θ ​ ( τ ∣ s ) . q_{\beta}(\tau\mid s)\;=\;\frac{\pi_{\theta}(\tau\mid s)\exp(\beta r(\tau;s))}{\mathbb{E}_{\pi_{\theta}}[\exp(\beta r(\tau;s))]},\qquad w_{\beta}(\tau\mid s)\;=\;\frac{q_{\beta}(\tau\mid s)}{\pi_{\theta}(\tau\mid s)}. Then w β w_{\beta} is exactly the density ratio that appears in the entropic policy-gradient update, so β \beta controls the effective step size induced by this reweighting. We choose β ​ ( s ) \beta(s) by enforcing a KL budget on the auxiliary distribution, KL ( q β ​ ( s ) ( ⋅ ∣ s ) ∥ π θ ( ⋅ ∣ s ) ) = γ , \mathrm{KL}\!\big(q_{\beta(s)}(\cdot\mid s)\,\|\,\pi_{\theta}(\cdot\mid s)\big)\;=\;\gamma, analogous to Relative Entropy Policy Search, where the temperature is set by an exponential tilt under a relative-entropy constraint [ 51 ] . In words, β ​ ( s ) \beta(s) is increased only until the KL budget is exhausted, ensuring the induced reweighting, and hence the update, does not move too far from π θ ( ⋅ ∣ s ) \pi_{\theta}(\cdot\mid s) . We fix γ = ln ⁡ 2 \gamma=\ln 2 throughout our experiments.

Batch estimator. Given N N rollouts from the same s s with rewards { r n } n = 1 N \{r_{n}\}_{n=1}^{N} , the empirical sampling distribution is uniform on the batch, u ⁡ ( n ) = 1 / N u(n)=1/N . The induced reweighting on the batch is q β ​ ( n ) = e β ​ r n ∑ m = 1 N e β ​ r m , q_{\beta}(n)=\frac{e^{\beta r_{n}}}{\sumop\displaylimits_{m=1}^{N}e^{\beta r_{m}}}, and we set β ​ ( s ) \beta(s) by solving the weight-concentration constraint KL ( q β ∥ u ) = ∑ n = 1 N q β ( n ) log ( N q β ( n ) ) = γ \mathrm{KL}(q_{\beta}\|u)=\sumop\displaylimits_{n=1}^{N}q_{\beta}(n)\log\!\big(Nq_{\beta}(n)\big)=\gamma via simple bisection search over β ≥ 0 \beta\geq 0 . With β ^ ​ ( s ) \hat{\beta}(s) , we compute LOO entropic advantages using r max = max n ⁡ r n r_{\max}=\max_{n}r_{n} , and an ϵ \epsilon in the denominator for numerical stability: Z ^ − n = 1 N − 1 ​ ∑ m , n exp ⁡ ( β ^ ​ ( s ) ​ ( r m − r max ) ) , A n = exp ⁡ ( β ^ ​ ( s ) ​ ( r n − r max ) ) Z ^ − n + ε − 1 . \qquad\hat{Z}_{-n}=\frac{1}{N-1}\sumop\displaylimits_{m\neq n}\exp(\hat{\beta}(s)(r_{m}-r_{\max})),\qquad A_{n}=\frac{\exp(\hat{\beta}(s)(r_{n}-r_{\max}))}{\hat{Z}_{-n}+\varepsilon}-1.

##### Discussion.

States where improvements are consistently small (e.g. high-value / near-goal states) tend to make the batch weights q β ​ ( n ) q_{\beta}(n) less peaky for a given β \beta , so the constraint typically permits a larger β ​ ( s ) \beta(s) . In contrast, states that occasionally yield a few very large improvements (often earlier in training or low-value states with large headroom) make q β q_{\beta} concentrate quickly as β \beta grows; the same KL budget then forces a smaller β ​ ( s ) \beta(s) , preventing the update from being dominated by a handful of outlier trajectories while still preferring better-than-average rollouts. Finally, this estimator is invariant to shifting or scaling the reward by a constant, i.e., r ⁡ ( τ ) r(\tau) and r ′ ​ ( τ ) = w ​ r ​ ( τ ) + b r^{\prime}(\tau)=wr(\tau)+b yield the same advantage for w ∈ R + w\in\mathbb{R}^{+} and b ∈ R b\in\mathbb{R} .

### A.2 PUCT Prioritization

We maintain an archive ℋ t \mathcal{H}_{t} of previously discovered states s s with reward R ⁡ ( s ) ∈ R R(s)\in\mathbb{R} . To choose the next start state, we score each s ∈ ℋ t s\in\mathcal{H}_{t} by a PUCT-inspired rule, analogous to applying PUCT at a virtual root whose actions correspond to selecting a start state from the archive [ 55 , 63 , 65 , 64 ] : score ​ ( s ) = Q ⁡ ( s ) + c ⋅ scale ⋅ P ⁡ ( s ) ​ 1 + T 1 + n ⁡ ( s ) , \text{score}(s)=Q(s)+c\cdot\text{scale}\cdot P(s)\frac{\sqrt{1+T}}{1+n(s)}, where n ⁡ ( s ) n(s) is a visitation count, T T is the number of expanded parents so far, c > 0 c>0 is an exploration coefficient, and scale = R max − R min \text{scale}=R_{\max}-R_{\min} is the reward range over the archive. The prior P ⁡ ( s ) P(s) is a linear rank distribution: P ⁡ ( s ) = | ℋ t | − rank ​ ( s ) ∑ s ′ ∈ ℋ t ( | ℋ t | − rank ​ ( s ′ ) ) , P(s)=\frac{|\mathcal{H}_{t}|-\text{rank}(s)}{\sumop\displaylimits_{s^{\prime}\in\mathcal{H}_{t}}(|\mathcal{H}_{t}|-\text{rank}(s^{\prime}))}, where rank ​ ( s ) ∈ { 0 , … , | ℋ t | − 1 } \text{rank}(s)\in\{0,\ldots,|\mathcal{H}_{t}|-1\} orders states by descending reward (rank 0 0 is the best state). The term Q ⁡ ( s ) Q(s) uses the best one-step reachable reward m ⁡ ( s ) m(s) : Q ⁡ ( s ) = { m ⁡ ( s ) n ⁡ ( s ) > 0 R ⁡ ( s ) n ⁡ ( s ) = 0 . Q(s)=\begin{cases}m(s)&n(s)>0\\ R(s)&n(s)=0\end{cases}. After expanding parent p p and observing its best child reward y = max s ′ ∈ Child ⁡ ( p ) ⁡ R ⁡ ( s ′ ) y=\max_{s^{\prime}\in\mathrm{Child}(p)}R(s^{\prime}) , we update: m ⁡ ( p ) \displaystyle m(p) ← max ⁡ ( m ⁡ ( p ) , y ) \displaystyle\leftarrow\max(m(p),\,y) (direct parent only) n ⁡ ( a ) \displaystyle n(a) ← n ⁡ ( a ) + 1 ∀ a ∈ { p } ∪ Anc ⁡ ( p ) \displaystyle\leftarrow n(a)+1\quad\forall a\in\{p\}\cup\mathrm{Anc}(p) (backprop visitation) T \displaystyle T ← T + 1 . \displaystyle\leftarrow T+1. For the archive update, we keep the top- 2 2 children per expanded parent (largest R R ) before inserting, then enforce a global size constraint by retaining the top- 1000 1000 states in ℋ t \mathcal{H}_{t} by R R , while always keeping the initial seed states.

##### Comparison to AlphaZero PUCT.

AlphaZero’s PUCT operates over a tree of state-action edges, selecting actions via a = arg ⁡ max a ⁡ [ Q ⁡ ( s , a ) + c ⋅ P ⁡ ( s , a ) ⋅ ∑ b N ⁡ ( s , b ) / ( 1 + N ⁡ ( s , a ) ) ] a=\arg\max_{a}[Q(s,a)+c\cdot P(s,a)\cdot\sqrt{\sumop\displaylimits_{b}N(s,b)}/(1+N(s,a))] , where Q ⁡ ( s , a ) Q(s,a) is the mean value of simulations through edge ( s , a ) (s,a) , P ⁡ ( s , a ) P(s,a) is a learned policy prior, and N ⁡ ( s , a ) N(s,a) counts visits to that edge [ 65 , 64 ] . Our formulation differs in four ways: (i) Q ⁡ ( s ) Q(s) tracks the maximum child reward rather than the mean, favoring optimistic expansion; (ii) P ⁡ ( s ) P(s) is a rank-based prior over archived states rather than a learned action distribution; (iii) visitation counts backpropagate to all ancestors, so expanding any descendant reduces the exploration bonus for the entire lineage; and (iv) we block the full lineage (ancestors and descendants) from the current batch to encourage diversity, whereas AlphaZero uses virtual loss as a temporary penalty.

## Appendix B Mathematics

### B.1 Circle Packing

⬇

### B.2 Autocorrelation Inequalities

For autocorrelation inequalities, initial sequences are created by sampling a random value in [ 0 , 1 ] [0,1] and repeating it between 1,000 and 8,000 times (or loading a state-of-the-art construction when available). For the first inequality, the verifier computes the upper bound 2 ​ n ⋅ max ⁡ ( f ∗ f ) / ( ∑ f ) 2 2n\cdot\max(f*f)/(\sumop\displaylimits f)^{2} where f ∗ f f*f denotes discrete autocorrelation; it validates that inputs are non-empty lists of non-negative floats clamped to [ 0 , 1000 ] [0,1000] with sum ≥ 0.01 \geq 0.01 , and returns ∞ \infty for invalid constructions. For the second inequality, verifier computes the lower bound C 2 = ‖ f ∗ f ‖ 2 2 / ( ‖ f ∗ f ‖ 1 ⋅ ‖ f ∗ f ‖ ∞ ) C_{2}=\|f*f\|_{2}^{2}/(\|f*f\|_{1}\cdot\|f*f\|_{\infty}) using piecewise-linear integration for the L 2 L^{2} norm (Simpson-like rule with endpoint zeros) over the normalized interval [ − 1 / 2 , 1 / 2 ] [-1/2,1/2] . Each algorithm is run with 1 GB with 2 CPUs each and a timeout of up to 1100 seconds.

### B.3 Erdős’

We initialize TTT-Discover with random constructions of 40-100 samples around 0.5 with random perturbations. We filter out sequences with more than 1000 values in the verifier. Each algorithm is run with 1 GB with 2 CPUs each and a timeout of up to 1100 seconds.

## Appendix C Kernel engineering

For trimul, we provide the a matrix multiplication kernel that triton provides in README , mostly for syntax purposes For MLA-Decode, we first put a softmax kernel in a preliminary prompt to let the base model generate a correct but unoptimized MLA-Decode kernel, and then use that as the initial state with the earlier softmax example removed.

### C.1 Kernel evaluation details

Setup of verifier for training. We follow the exact same practice for evaluating kernel correctness and runtime as the original GPUMode competitions. Specifically, the verifier used in our training jobs uses the same code as the official GPU Mode Competition Github repository, with minor adjustment to integrate into our training codebase. The verification process includes a correctness check that compare output values between the custom kernel and a pytorch reference program under a designated precision, followed by runtime benchmarking of the custom kernel across multiple iterations. All the details in our verification procedure follow the official competition exactly, including the test cases used for correctness check and benchmarking, hyper-parameters such as matching precision and iterations used for timing, etc. We run our verifier on H100s for TriMul, and H200s for MLA-Decode, both from the Modal cloud platform.

Setup of environments for final report. For final report, we submit to the official TriMul A100/H100 leaderboard and report the runtime shown. For TriMul B200/MI300X and MLA-Decode MI300X tasks, due to an infra problem on GPU Mode’s server, we could not submit to the official leaderboard. For these tasks, we work with the GPU Mode team closely to set up our local environment, which replicates the official environment and gets GPU Mode team’s review and confirmation.

Selection protocol for best kernels. For TriMul H100 task, we select 20 kernels with the best verifier score throughout training. For other tasks, since our verifier hardware in training is different from the target hardware, we select 20 kernels with the best training scores plus 20 random correct kernels every 10 steps of training. Finally, we used our verifier with the target hardware to verify each selected kernels for three times, and submit the kernel with the smallest average runtime for final report.

### C.2 Analysis of best generated kernels

TriMul H100 kernels. The below code shows the best TriMul kernels discovered by TTT for H100 GPU. At the high level, the kernel correctly identifies a major bottleneck of the problem, which is the heavy memory I/O incurred by a series of elementwise operations, and then focuses on fusing them with Triton. Specifically, the kernel fuses: (i) operations in the input LayerNorm, (ii) elementwise activation and multiplication for input gating, and (iii) operations in the output Layernorm and output gating. As for the compute-heavy operation, which is an O ⁡ ( N 3 ) O(N^{3}) matmul, the kernel converts its inputs to fp16 and delegate the computation to cuBLAS to effectively leverage the TensorCores on H100 GPU.

Compared with kernels generated early in training, the final kernel achieves a big improvement by (i) fusing more operations together, and (ii) deeper optimization of the memory access pattern inside fused kernels. For example, a kernel generated early fuses LayerNorm operations, but does not fuse the input gating process. A kernel generated in the middle of training fuses the same operations as the final kernel, but has less efficient memory access pattern in the fused kernel for output LayerNorm, gating, and output projection.

Compared with the best human leaderboard kernel, the TTT discovered kernel adopts a similar fusion strategy for the input LayerNorm and input gating. Different from human kernel, the TTT kernel does not perform as much auto-tuning of block size, which could be a limitation. However, the TTT kernel fuses the output LayerNorm and gating with output projection whereas the human kernel does not, which could explain the moderate advantage of the former.

⬇

### C.3 TTT MLA-Decode kernels filtered with Triton kernels

## Appendix D Algorithm Engineering

During the contest, AtCoder provides an official input generator, tester to evaluate program correctness, and a scoring function used for the final ranking. For training, we generate 150 test cases using seeds 0 through 149 from the input generator and run our program on each of these cases with an ALE-Bench provided C++20 container (yimjk/ale-bench:cpp20-202301) . A program receives a non-zero reward only if it passes all correctness checks and executes within the problem time limit (2 seconds) across all 150 test cases. The per-test case score is problem-specific and matches the scoring used in the AtCoder contest. For ahc039, we use ShinkaEvolve’s performance metric, which is determined by the score’s relative placement among the final contest’s scores, and for ahc058, we directly use the contest score.

For the final evaluation, we select the top three highest-scoring programs from our local training runs and submit them to the official AtCoder submission website. For our language, we specify C++23 (GCC 15.2.0). The submission is evaluated using the same scoring and validation process as the original contest, including checks for incorrect output, time limit violations, and compilation or runtime errors on AtCoder’s hidden test cases. The resulting score is used as the final evaluation.

For AHC training runs, we make a slight modification from our standard hyperparameters. For AHC039, we decrease the prompt length + thinking token limit to 22000 due to the large initial program. For AHC058, we similarly decrease the prompt length + thinking token limit to 25000 and found that a learning rate of 2 × 10 − 5 2\times 10^{-5} performed slightly better. For both AHC problems, we use a KL coefficient of 1 × 10 − 2 1\times 10^{-2} . Other hyperparameters are set to our standard values.

## Appendix E Single cell analysis

The OpenProblems benchmark provides three datasets: pancreas, pbmc and tabula. We select the Pancreas dataset to compute MSE and Poisson loss scores and use the other two datasets to assess generalization. MSE and Poisson loss scores are normalized with respect to the scores that no denoising and perfect denoising would get on this task. The main score metric in the OpenProblems denoising benchmark is the mean between the normalized MSE and the normalized Poisson. During verification, we reject all the solutions that obtain a normalized Poisson lower than 0.97 or larger than 1 so that we can focus only on improving a single metric, MSE.

In the prompt we also include instructions regarding what makes a solution taking inspiration from the Supplementary Materials of the OpenProblems paper [ 44 ] . For this specific applications, considering the size of the datasets, the memory limit is increased to 3GB. To force generalization, we reduce the time limits for the execution to 400 seconds.

We ran the OpenEvolve baseline with 25,600 samples. After sample 17,000, we observed the OpenEvolve database filling up with programs that timed out. Consequently, we selected the best program found up to that point.

Both TTT-Discover and the Best-of-25600 baselines are run with max tokens equal to 20,000.

Both MAGIC and the solution found by TTT-Discover are run with default parameters.

⬇

## Appendix F Prompts

Below we show example prompts from a sample step.

⬇

⬇

⬇

⬇

⬇

⬇

⬇

⬇

## Instructions for reporting errors

We are continuing to improve HTML versions of papers, and your feedback helps enhance accessibility and mobile support. To report errors in the HTML that will help us improve conversion and rendering, choose any of the methods listed below:

Click the "Report Issue" ( ) button, located in the page header.

Tip: You can select the relevant text first, to include it in your report.

Our team has already identified the following issues . We appreciate your time reviewing and reporting rendering errors we may not have found yet. Your efforts will help us improve the HTML versions for all readers, because disability should not be a barrier to accessing research. Thank you for your continued support in championing open access for all.

Have a free development cycle? Help support accessibility at arXiv! Our collaborators at LaTeXML maintain a list of packages that need conversion , and welcome developer contributions .
