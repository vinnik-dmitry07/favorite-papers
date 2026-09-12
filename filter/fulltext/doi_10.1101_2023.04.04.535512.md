Emergence of belief-like representations through
reinforcement learning
Jay A. Hennig1,2,∗, Sandra A. Romero Pinto2,3, Takahiro Yamaguchi3,4,
Scott W. Linderman5,6, Naoshige Uchida2,3, Samuel J. Gershman1,2
1 Department of Psychology, Harvard University, Cambridge, MA, USA
2 Center for Brain Science, Harvard University, Cambridge, MA, USA
3 Department of Molecular and Cellular Biology, Harvard University, Cambridge, MA, USA
4 Future Vehicle Research Department, Toyota Research Institute North America, Toyota Motor North
America Inc., Ann Arbor, MI, USA
5 Wu Tsai Neurosciences Institute, Stanford University, Stanford, CA, USA
6 Department of Statistics, Stanford University, Stanford, CA, USA
* Corresponding author
Email: jay.a.hennig@gmail.com (JAH)
1
.CC-BY 4.0 International licenseavailable under a 
was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made 
The copyright holder for this preprint (whichthis version posted April 7, 2023. ; https://doi.org/10.1101/2023.04.04.535512doi: bioRxiv preprint

Abstract
To behave adaptively, animals must learn to predict future reward, or value. To do this, animals are thought1
to learn reward predictions using reinforcement learning. However, in contrast to classical models, animals2
must learn to estimate value using only incomplete state information. Previous work suggests that animals3
estimate value in partially observable tasks by first forming “beliefs”—optimal Bayesian estimates of the4
hidden states in the task. Although this is one way to solve the problem of partial observability, it is not the5
only way, nor is it the most computationally scalable solution in complex, real-world environments. Here6
we show that a recurrent neural network (RNN) can learn to estimate value directly from observations, gen-7
erating reward prediction errors that resemble those observed experimentally, without any explicit objective8
of estimating beliefs. We integrate statistical, functional, and dynamical systems perspectives on beliefs to9
show that the RNN’s learned representation encodes belief information, but only when the RNN’s capac-10
ity is sufficiently large. These results illustrate how animals can estimate value in tasks without explicitly11
estimating beliefs, yielding a representation useful for systems with limited capacity.12
Author Summary13
Natural environments are full of uncertainty. For example, just because my fridge had food in it yester-14
day does not mean it will have food today. Despite such uncertainty, animals can estimate which states15
and actions are the most valuable. Previous work suggests that animals estimate value using a brain area16
called the basal ganglia, using a process resembling a reinforcement learning algorithm called TD learning.17
However, traditional reinforcement learning algorithms cannot accurately estimate value in environments18
with state uncertainty (e.g., when my fridge’s contents are unknown). One way around this problem is if19
agents form “beliefs,” a probabilistic estimate of how likely each state is, given any observations so far.20
However, estimating beliefs is a demanding process that may not be possible for animals in more complex21
environments. Here we show that an artificial recurrent neural network (RNN) trained with TD learning22
can estimate value from observations, without explicitly estimating beliefs. The trained RNN’s error signals23
resembled the neural activity of dopamine neurons measured during the same task. Importantly, the RNN’s24
2
.CC-BY 4.0 International licenseavailable under a 
was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made 
The copyright holder for this preprint (whichthis version posted April 7, 2023. ; https://doi.org/10.1101/2023.04.04.535512doi: bioRxiv preprint

activity resembled beliefs, but only when the RNN had enough capacity. This work illustrates how animals25
could estimate value in uncertain environments without needing to first form beliefs, which may be useful26
in environments where computing the true beliefs is too costly.27
Introduction28
One pervasive feature of animal behavior is the ability to predict future reward. For example, a dog may29
learn that when her owner picks up the leash, she is likely to be rewarded with a walk in the near future.30
In associative learning settings such as this one, animals learn to associate certain stimuli (e.g., her owner31
grabbing the leash) with future reward (e.g., a walk). The neural basis of associative learning has been32
interpreted through the lens of reinforcement learning (RL). In particular, one successful theoretical model33
posits that associative learning is driven by the activity of dopamine neurons in the midbrain, where spiking34
activity resembles the reward prediction error (RPE) signal in an RL algorithm called temporal difference35
(TD) learning [1, 2, 3, 4]. We will describe this algorithm in more detail below.36
In many real-world scenarios, effectively predicting reward may require a deeper understanding of the37
structure of the world that goes beyond associating observations and reward. To continue the example38
above, suppose the dog’s owner keeps his car keys under the leash. Now if he picks up the leash, this39
does not necessarily mean he is about to take his dog on a walk. In other words, his intention to take40
his dog on a walk is now “partially observable.” Standard RL approaches are insufficient for learning in41
partially observable environments, as these methods assume that all relevant states of the environment are42
fully observable. One way to solve this problem is by using observations to form a Bayesian posterior43
estimate of each hidden state, called a belief state [5]. Future reward can then be estimated by applying44
standard RL methods like TD learning to belief states rather than the raw observations.45
Do animals estimate future reward using belief states? Evidence for this idea is suggestive, although46
indirect. Previous experimental work has shown that the phasic activity of midbrain dopamine neurons47
resembles the RPEs of TD learning in partially observable environments, where TD learning is performed48
on belief states rather than observations [6, 7, 8, 9, 10, 11]. The brain may have dedicated machinery, perhaps49
in prefrontal cortex [12, 13], for computing belief states, which could then be provided to downstream areas,50
3
.CC-BY 4.0 International licenseavailable under a 
was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made 
The copyright holder for this preprint (whichthis version posted April 7, 2023. ; https://doi.org/10.1101/2023.04.04.535512doi: bioRxiv preprint

such as the basal ganglia, to perform standard RL algorithms such as TD learning [14]. This architectural51
division of labor resonates with the broader literature on probabilistic computation in cortex, which has52
identified several different ways in which belief states could be encoded by neural activity [15].53
There are a few difficulties in using a belief state to solve RL tasks. First, the belief state assumes54
knowledge of the environment’s transition and observation dynamics—something that may be challenging55
for animals to acquire via observations alone. Indeed, there are well-documented examples of animals56
failing to learn or use the correct environment model [16]. Second, the belief representation does not scale57
well to more realistic tasks with higher-dimensional state spaces, as beliefs live in a continuous space whose58
dimensionality grows with the number of discrete states in the environment. Finally, the belief state includes59
knowledge about all states in the environment, regardless of whether those states are relevant to the task at60
hand. Luckily, one can often use approximate representations of beliefs to find solutions that work well in61
practice [17]. This suggests that there may be other representations, more compact than the full belief state,62
that are sufficient for the particular task of estimating future reward [18, 19].63
To address these difficulties, here we take inspiration from deep reinforcement learning. In deep RL,64
rather than explicitly learning beliefs, an agent uses nonlinear function approximation to learn a hidden65
representation that is sufficient for performing the task [20]. Compared to the belief representation, this66
approach does not require explicit knowledge about the structure of the environment. It may also scale67
better to more complex tasks, by virtue of the agent not needing to represent any features of the environment68
that do not directly pertain to the task at hand. Because beliefs are a non-linear dynamical system, here69
we use recurrent neural networks (RNNs) as our nonlinear function approximator. This choice was also70
motivated by the observation from the machine learning literature that RNNs can perform well on complex71
partially observable tasks [21]. Previous work in computational neuroscience has explored whether RNNs72
can be used to directly compute beliefs [17]. Here, by contrast, we explore whether training RNNs in73
partially observable environments leads to their representations implicitly becoming more like beliefs.74
We show that RNNs can be trained to perform two previously studied associative learning tasks [7, 10],75
reproducing experimentally observed dopamine neuron activity. We probe the representations learned by the76
RNNs, and show that the representations resemble beliefs from statistical, functional, and dynamical systems77
perspectives. Finally, we show how an RNN’s capacity determines the degree to which its representation78
4
.CC-BY 4.0 International licenseavailable under a 
was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made 
The copyright holder for this preprint (whichthis version posted April 7, 2023. ; https://doi.org/10.1101/2023.04.04.535512doi: bioRxiv preprint

resembles beliefs, without a concurrent impact on its ability to perform the task. These results illustrate79
how animals might estimate reward in partially observable environments without requiring any explicit80
representation of beliefs.81
Results82
Reinforcement learning in partially observable environments using belief states83
The standard RL objective is to learn the expected discounted future return, or value, of each state:
V (st) = E
"∞X
k=0
γkrt+k
#
(1)
wherest∈S is the state of the environment at time t, 0≤γ <1 is a discount factor, andrt is the reward.84
Rewards are random variables that depend on the environment state, and E denotes an expectation over the85
potentially stochastic sequences of states and rewards. Because we are interested in modeling Pavlovian86
associative learning tasks, here we will assume there are no actions available to the agent. For notational87
simplicity, we will use the shorthandVt =V (st).88
TD learning estimates the value function by exploiting a set of Markovian assumptions about the en-
vironment: the probability of state st depends only on the last state st−1, and the probability of reward rt
depends only on the current statest. Under these assumptions, the value function can be decomposed into a
recursive form known as the Bellman equation [22]:
Vt = E[rt +γVt+1]. (2)
If an agent has access to an approximation of the value function, bVt, along with sample paths of states and
rewards, then it can compute an estimate of the discrepancy between the approximate and true value function
by taking the difference between the two sides of the Bellman equation:
δt =rt +γ bVt+1− bVt. (3)
5
.CC-BY 4.0 International licenseavailable under a 
was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made 
The copyright holder for this preprint (whichthis version posted April 7, 2023. ; https://doi.org/10.1101/2023.04.04.535512doi: bioRxiv preprint

This is the temporal difference error, the precise definition of the RPE used in TD learning. Under the
Bellman equation, E[δt] = 0 when bVt = Vt. If bVt is determined by a set of adaptable parameters θ, the
approximation can be improved by following the stochastic gradient of the squared TD error:
∆θ =ηδt∇θ bVt, (4)
where 0<η < 1 is a learning rate, and∇θ bVt is the gradient of bVt with respect toθ. One common example
is a linear function approximator:
bVt =
DX
d=1
w(d)zt(d), (5)
wherezt(d)∈ R is some feature (indexed by d) of the state, and θ =w∈ RD is a learned set of weights89
on all the features. Under this approximation,∇θ bVt =zt.90
In a partially observable Markov process, agents do not observe the statest directly, but instead observe91
only observations ot ∈O . Critically, observations are not in general Markovian, which means that TD92
learning methods cannot be naively applied to value function approximators defined over observations. One93
way of understanding this is to note that the value of an observation may depend on the long-term past [23].94
In the dog leash example from the Introduction, the value (to the dog) of her owner picking up the leash95
depends on the history of events leading up to that moment—for example, if her owner recently announced96
that his car keys were missing. Reward prediction requires a compression of this history into a “sufficient97
statistic”—in effect creating a transformed state space over which the Markov property holds. TD learning98
can then be applied to this transformed state space.99
One such transformed state is the posterior probability distribution over hidden states given the history
of observations, also known as the belief state [5]:
bt(st) =P (st|o1,...,o t)
∝P (ot|st)
Z
P (st|st−1)bt−1(st−1)∂st−1
(6)
where the recursion follows from the Chapman-Kolmogorov equation, which stipulates how to update the100
6
.CC-BY 4.0 International licenseavailable under a 
was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made 
The copyright holder for this preprint (whichthis version posted April 7, 2023. ; https://doi.org/10.1101/2023.04.04.535512doi: bioRxiv preprint

belief state fromt− 1 tot after observing observationot.101
For a partially observable Markov process with a finite state space,S ={1,...,K }, the value function
can be written as a weighted combination of beliefs:
Vt =
KX
k=1
V (k)bt(k) (7)
whereV (k) andbt(k) are the value and belief of state st = k, respectively. This means that linear value102
function approximation in Eqn. (5) is sufficiently expressive for the partially observable problems we con-103
sider in this paper: with enough training data, the value function approximator will perfectly estimate the104
true value function (i.e., given learned weightsw(k) =V (k) and featureszt(k) =bt(k) for eachk∈K).105
This motivates a straightforward model of how animals estimate value in partially observable environ-106
ments [6, 7], which we will refer to as the “Belief model”: First compute beliefs (Eqn. (6)), and then107
compute a linear transformation of those beliefs to a value estimate (Eqn. (7)), with weights obtained from108
TD learning.109
Learning state representations using recurrent neural networks110
The Belief model assumes animals use a particular feature representation (i.e., beliefs) for estimating value.
Here we ask what representations might emerge from solving the task of estimating value alone. It is useful
to note that the Belief model can be written as follows:
bVt =w⊤bt (8)
bt =P (st|o1,...,o t) (9)
=P (st|bt−1,ot)
=fϕ(bt−1,ot)
wheref is a function parameterized by a specific choice of (fixed) parameters ϕ, and only w is learned.
This latter equation has the same form as a generic recurrent neural network (RNN). This suggests a model
7
.CC-BY 4.0 International licenseavailable under a 
was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made 
The copyright holder for this preprint (whichthis version posted April 7, 2023. ; https://doi.org/10.1101/2023.04.04.535512doi: bioRxiv preprint

could learn its own representation by treatingϕ as a learnable parameter. Taken together, this results in the
following model for estimating value:
bVt =w⊤zt (10)
zt =fϕ(zt−1,ot) (11)
wherezt∈ RH is the activity of an RNN withH hidden units and parametersϕ. Importantly, bothϕ andw111
can be learned simultaneously, using backpropagation through time to calculate Eqn. (4) with θ = [ϕw ].112
This allows the network to learn the representations, zt, that are sufficient for estimating value. We will113
refer to this model as a “Value RNN” (see Materials and Methods).114
Importantly, this RNN-based approach resolves all three challenges for learning a belief representation115
that we raised in the Introduction: 1) The model can learn from observations alone, as no information is116
provided about the statistics of the underlying environment; 2) the model’s size (parameterized by H, the117
number of hidden units) can be controlled separately from the number of states in the environment; and 3)118
the model’s only objective is to estimate value.119
Though such a model has no explicit objective of learning beliefs, the network may discover a belief120
representation implicitly. We next asked what signatures, if any, would indicate the existence of a belief121
representation. In the sections that follow we develop an analytical approach for determining whether the122
Value RNN’s learned representations resemble beliefs.123
RNNs learn belief-like representations124
As a working example, we will consider the probabilistic associative learning paradigm where dopamine125
RPEs were shown to be consistent with a belief representation [7, 13]. This has the added benefit of ensuring126
that the RNN-based approach described above can recapitulate these previous results.127
This paradigm consisted of two tasks, which we will refer to as Task 1 and Task 2 (Fig 1). In both tasks,128
mice were trained to associate an odor cue with probabilistic delivery of a liquid reward 1.2-2.8s later. The129
tasks were each composed of two states: an intertrial interval (ITI), during which animals waited for an130
8
.CC-BY 4.0 International licenseavailable under a 
was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made 
The copyright holder for this preprint (whichthis version posted April 7, 2023. ; https://doi.org/10.1101/2023.04.04.535512doi: bioRxiv preprint

Fig 1. Associative learning tasks with probabilistic rewards and hidden states. a.
Trial structure in Starkweather et al. [7, 13]. Each trial consisted of a variable delay (the
intertrial interval, or ITI), followed by an odor, a second delay (the interstimulus interval,
or ISI), and a potential subsequent reward. Reward times were sampled from a discretized
Gaussian ranging from 1.2-2.8s (see Materials and Methods). b-c.. In both versions of
the task, there were two underlying states: the ITI and the ISI. In Task 1, every trial
was rewarded. As a result, an odor always indicated a transition from the ITI to the ISI,
while a reward always indicated a transition from the ISI to the ITI. In Task 2, rewards
were omitted on 10% of trials; as a result, an odor did not reveal whether or not the state
transitioned to the ISI.
odor; and an interstimulus interval (ISI), during which animals waited for a reward. In Task 1, every trial131
contained both an odor and a reward. As a result, the animal’s observations could fully disambiguate the132
underlying state: An odor signaled a transition to the ISI state, while a reward signaled a transition to the133
ITI state. In Task 2, by contrast, reward on a given trial was omitted with 10% probability. This meant the134
underlying states were now only partially observable; for example, in Task 2 an odor signaled a transition to135
the ISI state with 90% probability.136
To formalize these tasks, we largely followed previous work [7, 13]. Each task was modeled as a137
discrete-time Markov process with statesst∈{ 1,...,K }, where eacht denotes a 200ms time bin (Fig 2A).138
TheseK “micro” states can be partitioned into those belonging to one of two “macro” states (corresponding139
to the ITI and the ISI; see Materials and Methods). At each point in time, the agent’s observation is one of140
ot∈{odor,reward,null } (Fig 2B). For each task, we trained the Belief model, and a Value RNN (using141
a gated-recurrent unit cell [24], or GRU, with H = 50 hidden units), on a series of observations from that142
task to estimate value using TD learning (see Materials and Methods). Before training, the Value RNN’s143
representation consisted of transient responses to each observation (Fig S1). After training, we evaluated144
each model on a sequence of new trials from the same task (Fig 2C).145
To confirm that this approach could recapitulate previous results, we measured the RPEs generated by146
9
.CC-BY 4.0 International licenseavailable under a 
was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made 
The copyright holder for this preprint (whichthis version posted April 7, 2023. ; https://doi.org/10.1101/2023.04.04.535512doi: bioRxiv preprint

Fig 2. Observations, model representations, value estimates, and reward prediction
errors (RPEs) during Task 2. a. State transitions and observation probabilities in Task
2. Each macro-state (ISI or ITI) is composed of micro-states denoting elapsed time; this
allows for probabilistic reward times and minimum dwell times in the ISI and ITI, respec-
tively. b. Observations emitted by Task 2 during two example trials. Note that omission
trials are indicated only implicitly as the absence of a reward observation. c. Example
representations (bt,zt) and value estimates ( bVt) of two models (Belief model, left; Value
RNN, right) for estimating value in partially observable environments, after training. d.
After training, both models exhibit similar RPEs.
10
.CC-BY 4.0 International licenseavailable under a 
was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made 
The copyright holder for this preprint (whichthis version posted April 7, 2023. ; https://doi.org/10.1101/2023.04.04.535512doi: bioRxiv preprint

each trained model (Fig 2D). Previous work showed that dopamine RPEs depended on the reward time147
differently in the two tasks, with RPEs increasing as a function of reward time in Task 1, but decreasing148
as a function of reward time in Task 2 [7] (Fig 3A). As in previous work, we found that this pattern was149
also exhibited by the Belief model (Fig 3B). We found that the RPEs of the Value RNN exhibited the same150
pattern (Fig 3C). In particular, the Value RNN’s RPEs became nearly identical to those of the Belief model151
after training (Fig 3D). We emphasize that the Value RNN was not trained to match the value estimate from152
the Belief model; rather, it was trained via TD learning using only observations. This result shows that,153
through training on observations alone, Value RNNs discovered a representation that was sufficient for both154
learning the value function as well as explaining empirical dopamine activity.155
Fig 3. RPEs of the Value RNN resemble both mouse dopamine activity and the
Belief model. a. Average phasic dopamine activity in the ventral tegmental area (VTA)
recorded from mice trained in each task separately. Black traces indicate trial-averaged
RPEs relative to an odor observated at time 0, prior to reward; colored traces indicate the
RPEs following each of nine possible reward times. RPEs exhibit opposite dependence
on reward time across tasks. Reproduced from Starkweather et al. [7].b-c. Average RPEs
of the Belief model and an example Value RNN, respectively. Same conventions as panel
a. d. Mean squared error (MSE) between the RPEs of the Value RNN and Belief model,
before and after training each Value RNN. Small dots depict the MSE of each ofN = 12
Task 1 RNNs andN = 12 Task 2 RNNs, and circles depict the median across RNNs.
We next asked whether the Value RNN learned these tasks by forming representations that resembled156
beliefs. We considered three approaches to answering this question. First, we asked whether beliefs could157
11
.CC-BY 4.0 International licenseavailable under a 
was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made 
The copyright holder for this preprint (whichthis version posted April 7, 2023. ; https://doi.org/10.1101/2023.04.04.535512doi: bioRxiv preprint

be linearly decoded from the RNN’s activity. Next, because beliefs are the optimal estimate of the true state158
in the task, we asked whether RNN activity could similarly be used to decode the true state. Finally, we took159
a dynamical systems perspective, and asked whether the RNN and beliefs had similar dynamical structure.160
RNN activity readout was correlated with beliefs161
We first asked whether the Value RNN’s activity was correlated with beliefs. Because the belief and RNN
representations did not necessarily have the same dimensionality, we performed a multivariate linear regres-
sion to find the linear transformation of the RNN’s activity that came closest to matching the beliefs (see
Materials and Methods). In other words, we found the linear transformation, cW∈ RK×H, that could map
the RNN’s activity,zt∈ RH, to best match the belief vector,bt∈ RK:
cW = argminW
TX
t=1
∥Wzt−bt∥2
2
To quantify performance, we used held-out sessions to measure the total variance of the beliefs that were162
explained by the linear readout of RNN activity (R 2; see Materials and Methods). We found that the Value163
RNN’s activity explained most of the variance of beliefs (Fig 4B; Task 1 R2: 0.69 ± 0.01, mean± SE,164
N = 12; Task 2 R2: 0.76± 0.02, mean± SE,N = 12), substantially above the performance when using165
the RNN activity before training (Task 1 R2: 0.47 ± 0.00, mean ± SE, N = 12; Task 2 R2: 0.50 ±166
0.00, mean± SE, N = 12 ). This is not a trivial result of the network’s training objective, as the Value167
RNN’s target (i.e., value) is only a 1-dimensional signal, whereas beliefs are aK-dimensional signal (here,168
K = 25). Nevertheless, we found that training the Value RNN to estimate value resulted in its representation169
becoming more belief-like, in the sense of encoding more information about beliefs.170
RNN activity could be used to decode hidden states171
The previous analysis assessed how much information about beliefs was encoded by RNN activity. Given172
that beliefs are distributions over hidden states, we asked whether the ground truth state could be decoded173
from the RNN’s activity. To do this, we performed a multinomial logistic regression to find a linear trans-174
formation of the RNN’s activity that maximized the log-likelihood of the true states (see Materials and175
12
.CC-BY 4.0 International licenseavailable under a 
was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made 
The copyright holder for this preprint (whichthis version posted April 7, 2023. ; https://doi.org/10.1101/2023.04.04.535512doi: bioRxiv preprint

Fig 4. Value RNN activity readout was correlated with beliefs and could be used to
decode hidden states. a. Example states, beliefs, and Value RNN activity from the same
Task 2 trials shown in Fig 2. Note that the states following the second odor observation
remain in the ITI (black) because the second trial is an omission trial. Bottom traces depict
the linear transformation of the RNN activity that comes closest to matching the beliefs.
Total variance explained (R2) is calculated on held-out trials. b. Total variance of beliefs
explained (R2), on held-out trials, using different trained and untrained Value RNNs, in
both tasks. Same conventions as Fig 3D). c. In purple, the cross-validated log-likelihood
of linear decoders trained to estimate true states using RNN activity. Same conventions as
Fig 3D). Black circle indicates the log-likelihood when using the beliefs as the decoded
state estimate (i.e., no decoder is “trained”).
13
.CC-BY 4.0 International licenseavailable under a 
was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made 
The copyright holder for this preprint (whichthis version posted April 7, 2023. ; https://doi.org/10.1101/2023.04.04.535512doi: bioRxiv preprint

Methods). We quantified performance on held-out sessions by evaluating the log-likelihood of the decoded176
estimates. Because the beliefs capture the posterior distribution of the state given the observations under the177
true generative model, the log-likelihood of the beliefs serves as a ceiling on performance. We found that178
the log-likelihoods of the decoders trained on the RNN’s activity approached those of the beliefs, and easily179
outperformed the decoders that used the activity of untrained RNNs (Fig 4C). Thus, training the RNN to180
estimate value resulted in a representation that could be used to more accurately decode the true state.181
RNN activity exhibited belief-like dynamics182
One potential shortcoming of the above analyses is that we have not yet accounted for the dynamical nature183
of the belief representation: Belief updating can be thought of as a dynamical system describing how the184
posterior probability of each state evolves as a function of the observations. We therefore took a dynamical185
systems perspective [25, 26, 27] and asked whether the dynamics of RNN activity resembled the dynamics186
of the beliefs in each task.187
We first asked whether beliefs and RNNs had similar fixed point structure, a standard approach to188
characterizing the computations performed by dynamical systems [25, 26, 27]. Here, a “fixed point” is189
a belief state that remains unchanged in the absence of any new observations. Specifically, we considered190
the fixed points of beliefs in the absence of observations (Fig 5A). In both tasks, the duration of the ITI is191
sampled from a geometric distribution, which has a constant hazard function. Thus, if the agent believes192
it is in the ITI (i.e., waiting for an odor), it should maintain this belief for as long as it receives no new193
observations (∅). Thus, the ITI belief state is a fixed point of the belief updates in both tasks (Fig 5A).194
Now consider when the agent is in the ISI (e.g., following an odor observation). In Task 2 (Fig 5A, bottom195
panel), the agent should maintain a nonzero belief in the ISI only for as long as there are possible reward196
times remaining—i.e., the first 2.8s, or 14 time steps—but after that point it should return to the ITI state.197
Thus, the ITI state is the only fixed point of the Task 2 beliefs. In Task 1, by contrast, there are no omission198
trials, and so the beliefs are simply undefined when there are no observations for more than 14 time steps.199
Nevertheless, for the purposes of characterizing the fixed points of beliefs, we can ask what an agent with200
Task 1 beliefs could do when faced with an omission trial. In this sense, an agent could maintain a belief in201
14
.CC-BY 4.0 International licenseavailable under a 
was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made 
The copyright holder for this preprint (whichthis version posted April 7, 2023. ; https://doi.org/10.1101/2023.04.04.535512doi: bioRxiv preprint

Fig 5. Value RNN dynamics resembled belief dynamics in each task. a. Dynamics
of beliefs in Task 1 (top) and Task 2 (bottom). Black arrows indicate transitions between
states in the absence of observations (∅) as a function of elapsed time, t, following an
odor observation. ‘X’ indicates an unconstrained duration, and a dashed arrow indicates
a transition that happens only when ‘X’ is finite. b. RNN activity at each time step (small
black dots with connected lines) during an example trial in a 2D subspace identified using
PCA. Putative ITI fixed point indicated as purple circle. Vectors indicate the response to
odor (black) and reward (red). Activity during an omission trial is shown in cyan, though
note that omission trials were present in training data only for Task 2. c-d. Average
normalized distance of each model’s activity from its fixed point (identified numerically)
following an odor (panel c) or reward (panel d) observation, over time. To allow compar-
ing distances across models, each model’s distances were normalized by the maximum
distance following each observation.
the ISI for any number of time steps X > 14, resulting in two fixed points when X→∞, and one fixed202
point otherwise (Fig 5A, top panel). Thus, Task 1 beliefs can decay to the ITI fixed point at any point after203
14 time steps, and may potentially have two fixed points.204
We asked whether the Value RNNs in each task exhibited similar dynamics. To build intuition, for each205
task we visualized the activity of a Value RNN on example trials (Fig 5B). To visualize the activity of the206
RNN’s 50 units, we used principal components analysis (PCA) to project the RNN’s activity into the top207
two dimensions that captured the most variance of the activity across trials; these two dimensions explained208
83% and 79% of the total variance in the Task 1 and Task 2 Value RNN, respectively. We observed that209
each RNN’s activity was quite stable during the ITI (purple circle), suggestive of a fixed point. This activity210
15
.CC-BY 4.0 International licenseavailable under a 
was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made 
The copyright holder for this preprint (whichthis version posted April 7, 2023. ; https://doi.org/10.1101/2023.04.04.535512doi: bioRxiv preprint

was then perturbed by an odor observation (black vector), and continued to move through state space during211
the ISI. On rewarded trials, in response to a reward (red vector), RNN activity gradually returned to the212
same ITI location it started from (purple circle). We noted that the activity of both RNNs would also have213
converged to its original ITI location had the reward been omitted (cyan traces). Interestingly, this was true214
even for the Task 1 RNN, which did not experience omission trials during training. These visualizations215
suggested that these two example Value RNNs had a single fixed point (corresponding to the ITI), which216
we then confirmed numerically (see Materials and Methods). We next used the same numerical approach to217
identify the fixed points across all trained Value RNNs, and found similar results. In fact, only two Value218
RNNs had more than one fixed point; these were both Task 1 RNNs, which had a fixed point for both the ITI219
and the ISI. Overall, these analyses indicated that Value RNNs had a fixed point structure consistent with220
those of beliefs.221
Despite the fact that most Value RNNs had a single fixed point regardless of which task they were222
trained on, we noted that the temporal dynamics of RNN activity differed across the two tasks following223
odor observations. For example, in the Task 2 RNN, following an odor observation, the activity moved224
gradually closer to the ITI state throughout the ISI (Fig 5B, bottom subpanel). These dynamics allowed the225
Task 2 RNN’s activity to return to the ITI state at the appropriate time on trials without reward (cyan trace).226
By contrast, in the Task 1 RNN, which did not experience trials without rewards during training, activity227
took much longer to return to the ITI. To quantify these differences, we initialized each RNN to its fixed228
point, provided an odor observation, and then measured the RNN’s activity over time in the absence of any229
subsequent reward. We then measured the distance of each RNN’s activity over time from its ITI fixed point230
(Fig 5C, colored traces).231
We repeated this same analysis for beliefs (Fig 5C, black trace), allowing us to characterize the two232
models’ responses to an odor as a function of the distance of their representations from their ITI fixed point.233
We reasoned that, if the RNNs learned belief-like dynamics, the activity of Task 2 RNNs should return to234
the ITI as soon as possible after time step 14 (i.e., the largest reward time), which we found was largely235
the case (Fig 5C). By contrast, in Task 1, beliefs are undefined past time step 14 (because there are no236
omission trials), and so the activity of RNNs after this point was not constrained by the task. To quantify237
these differences across tasks, we calculated the time step at which each RNN’s activity returned within238
16
.CC-BY 4.0 International licenseavailable under a 
was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made 
The copyright holder for this preprint (whichthis version posted April 7, 2023. ; https://doi.org/10.1101/2023.04.04.535512doi: bioRxiv preprint

Fig 6. Value RNNs with larger capacity had more belief-like representations. a.
Error between the Value RNN’s RPEs and those of the Belief model (“RPE MSE”; see
Fig 3D) during Task 2, as a function of the number of units in the Value RNN. Each circle
indicates the median across the N = 12 Value RNNs with the same number of units. b.
Total variance explained (R 2) of beliefs (see Fig 4B). Same conventions as panel a. c.
Log-likelihood of the state decoder using Value RNN activity to estimate the true state
(see Fig 4C). Dashed line indicates maximum possible log-likelihood (i.e., from Belief
model). Same conventions as panel a.
some threshold distance of its ITI fixed point. We refer to this quantity—which essentially measures ‘X’ in239
the top panel of Fig 5A—as the network’s odor memory. In fact, we found that all Task 1 RNNs had longer240
odor memories (310±150, mean± SE,N = 12) than Task 2 RNNs (49±2, mean± SE,N = 12). Overall,241
these features were consistent with the beliefs in the two tasks following an odor observation: beliefs in Task242
2, but not Task 1, must quickly return to the ITI after the maximum possible reward time. We performed a243
similar analysis for reward observations, in which case the network activity in both tasks was expected to244
return to the ITI fixed point shortly after the minimum ITI duration (at time step 10). Here, we found that245
the activity of both Task 1 and Task 2 RNNs quickly returned to the ITI fixed point after this point (Fig 5D),246
again consistent with the beliefs in these tasks.247
RNNs with larger capacity had more belief-like representations248
Thus far, we have considered the representations of Value RNNs with the same number of hidden units249
(H = 50). To understand whether the network’s size influences the types of representations learned, we250
next trained Value RNNs with a variable number of hidden units. We found that Value RNNs with as few251
as 2 hidden units could learn the value function, as evidenced by their RPEs matching those of the Belief252
model (Fig 6A). In other words, despite there being 25 discrete states in our implementation of this task253
(and, as such, beliefs were 25-dimensional), an RNN with a 2-dimensional representation was sufficient for254
17
.CC-BY 4.0 International licenseavailable under a 
was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made 
The copyright holder for this preprint (whichthis version posted April 7, 2023. ; https://doi.org/10.1101/2023.04.04.535512doi: bioRxiv preprint

performing the task. On the other hand, RNNs with fewer units had representations that were notably less255
belief-like, in terms of how well they linearly encoded beliefs (Fig 6B) and allowed for decoding the true256
state (Fig 6C). Thus, Value RNNs with 2 or more hidden units could all estimate value equally well, but257
only those with a sufficient number of hidden units featured representations that resembled beliefs.258
Generalization to other tasks259
We showed that RNNs could be trained to estimate value in the tasks from Starkweather et al. [7], and that260
the representations of these RNNs became more belief-like as a result of training. We next assessed whether261
the same basic insights generalized to a different task, that of Babayan et al. [10]. In this task, similar to262
Task 1 of Starkweather et al. [7], each trial consisted of an odor followed by a deterministic reward. Unlike263
in the Starkweather task, in this task the reward quantity on each trial was varied in blocks. In Block 1, each264
trial consisted of a small (1µL) reward, while in Block 2 each trial consisted of a large (10µL) reward. As265
a result, we formalize the states in this task using pairs of ITI and ISI states, one for each block (Fig 7A).266
Importantly, the block identity was hidden to the animal, and was resampled uniformly every five trials. This267
meant that animals had to use the reward observations to infer which block they were currently in.268
Previous work showed that the dopamine activity of animals trained on this task depended on the num-269
ber of trials in the current block (Fig 7C), similar to what you would expect if animals used a belief rep-270
resentation (Fig 7D, dashed lines) [10]. To see if the Value RNN could reproduce these results, we trained271
N = 12 Value RNNs on this task. We found that Value RNNs exhibited nearly identical RPEs as the Belief272
model (Fig 7D). This was even true on probe sessions that included blocks with intermediate reward sizes,273
a setting in which both dopamine activity and belief RPEs exhibited a characteristic nonlinear relationship274
with reward size (Fig S2). These results indicate that the Value RNNs found a representation sufficient for275
estimating value despite the hidden states.276
We next asked whether, as in the Starkweather task, the Value RNN’s representations resembled beliefs.277
To do this, we repeated the analyses in Fig 4. We found that the Value RNN’s activity could be linearly278
transformed to match the beliefs (Fig 7D), and that its activity could also be used to decode the hidden279
states in the task (Fig 7E), as compared to RNNs not trained on the task. We next took a dynamical systems280
18
.CC-BY 4.0 International licenseavailable under a 
was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made 
The copyright holder for this preprint (whichthis version posted April 7, 2023. ; https://doi.org/10.1101/2023.04.04.535512doi: bioRxiv preprint

Fig 7. Value RNNs trained on Babayan et al. [10] reproduce Belief RPEs and learn
belief-like representations. a. Task environment of Babayan et al. [10]. Each trial con-
sists of an odor and a subsequent reward. The reward amount depends on the block iden-
tity, which is resampled uniformly every five trials (green). b. Average phasic dopamine
activity in the VTA of mice trained on the task at the time of odor (left) and reward (right)
delivery. Activity is shown separately as a function of the trial index within the block
(x-axis) and the current/previous block identity (colors). Reproduced from Babayan et al.
[10]. c. Average RPEs of the Belief model (dashed lines) and an example Value RNN
(solid lines). Same conventions as panel b. d. Total variance of beliefs explained (R 2)
using a linear transformation of model activity. Same conventions as Fig 4B. e. Cross-
validated log-likelihood of linear decoders trained to estimate true states using RNN ac-
tivity. Same conventions asFig 4C. f. Dynamics of beliefs in the absence of observations.
Same conventions as Fig 5A. g. Trajectories of an example Value RNN’s activity, in the
2D subspace identified using PCA, during an example trial from Block 1 (left) and Block
2 (right). These two dimensions explained 69% of the total variance in the Value RNN’s
activity across trials. Putative ITI states indicated as purple circles. Same conventions as
Fig 5B.
19
.CC-BY 4.0 International licenseavailable under a 
was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made 
The copyright holder for this preprint (whichthis version posted April 7, 2023. ; https://doi.org/10.1101/2023.04.04.535512doi: bioRxiv preprint

approach, characterizing the fixed points of beliefs in this task. Similar to Task 1 of Starkweather et al. [7]281
(Fig 5A), beliefs in the present task should have a fixed point at the ITIs for Block 1 and Block 2 (Fig 7F).282
To assess whether this was the case in the Value RNN, we visualized an example RNN’s activity on the last283
few trials of each block, when the network should be confident as to the current block’s identity (given the284
reward observations on previous trials). During these trials, we observed two non-overlapping trajectories of285
activity for each block (Fig 7G). Following a reward observation, the RNN’s activity converged to a distinct286
location in state space corresponding to that block’s ITI. This suggested the RNN had two fixed points, as287
in the belief representation. In reality, these were not both truly fixed points, as the RNN’s activity did288
eventually return to a single fixed point given enough time without an observation (Fig S3A). However, the289
RNN’s two putative ITI states remained distinct across the range of ITI durations present in the training290
data (Fig S3B), allowing the network to keep these trajectories (and thus the states corresponding to each291
block) separate. These analyses suggest that Value RNNs trained on this task also exhibited belief-like292
representations.293
Untrained RNNs could also be used to estimate value and encode beliefs294
In the sections above we analyzed Value RNNs whose representations had been trained through TD learning.295
Here we take an alternative approach, inspired by reservoir computing, and consider the representations of296
untrained RNNs. In reservoir computing, a static dynamical system, or “reservoir,” is combined with a297
learned linear readout. Given an appropriately initialized reservoir (e.g., an RNN), this approach can be298
used to approximate any nonlinear function [28]. Inspired by this approach, we explored whether we could299
choose a random initialization of our RNNs such that it was only necessary to learn a linear weighting of300
the RNN’s representation to form its value estimate (i.e., ϕ in Eqn. (11) was fixed throughout training).301
Because this model resembles an echo state network (“ESN”; a reservoir computer whose reservoir is an302
RNN [29]), we will refer to this model as a Value ESN.303
We initialized each RNN by sampling the matrix of recurrent weights as a random orthogonal matrix304
scaled by a single gain parameter [30], an approach commonly used to initialize RNNs (see Materials and305
Methods). The gain effectively modulated the duration of the network’s transient response to inputs (Fig306
20
.CC-BY 4.0 International licenseavailable under a 
was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made 
The copyright holder for this preprint (whichthis version posted April 7, 2023. ; https://doi.org/10.1101/2023.04.04.535512doi: bioRxiv preprint

Fig 8. Untrained RNNs can also be used to estimate value. a.Time-varying activations
of 20 example units in response to an odor input, in an untrained RNN (“ESN”) with 50
units, initialized with a gain of 0.1.b. Same as panela, but for an initialization gain of 1.9,
and a wider range shown on the x-axis.c. Number of time steps it took each ESN’s activity
to return to its fixed point following an odor observation (“odor memory”; see Materials
and Methods), as a function of ESN initialization gain. Points labeled “>200” indicate
those that did not fit within the plot. d. RPE MSE (see Fig 3D) as a function of ESN
initialization gain, after training each ESN’s value weights to estimate value during Task
2. Dashed line indicates average levels of a Task 2 Value RNN with the same number of
units. e. BeliefR2 (see Fig 4B) as a function of ESN initialization gain. Same conventions
as panel d.
21
.CC-BY 4.0 International licenseavailable under a 
was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made 
The copyright holder for this preprint (whichthis version posted April 7, 2023. ; https://doi.org/10.1101/2023.04.04.535512doi: bioRxiv preprint

8A-B), such that larger gains led to larger odor memories (Fig 8C). In agreement with previous work, we307
found that when the gain was above a critical value (“the edge of chaos” [30]), the network’s activity never308
decayed back to baseline (e.g., gain> 2 in Fig 8C).309
To see if Value ESNs could be trained to estimate value, we trained Value ESNs on Starkweather Task310
2, varying the gain for each network. During training, only the network’s value weights were modified to311
estimate the value function. We found that for a range of different gains, the resulting Value ESN could312
estimate value nearly as well as Value RNNs, and recapitulate the experimentally observed dopamine pat-313
terns (Fig 8D). Interestingly, the Value ESN’s representations could even be linearly transformed to match314
beliefs (Fig 8E). We emphasize that the Value ESN’s representation was determined solely by its initial-315
ization; given an appropriate initialization, the Value ESN’s representation could effectively act as a set of316
temporal basis functions, allowing the network to match any downstream target, including beliefs. However,317
in terms of dynamics, the Value ESN’s dynamics differed substantially from those of the beliefs: For the318
best performing Value ESN (with a gain of 1.9), following an odor observation, the RNN’s activity returned319
to its fixed point after around 200 time steps (Fig 8C), whereas Task 2 beliefs return to the ITI point in 15320
time steps. These results show that allowing the RNN to modify its representation during training led to its321
representation becoming even more belief-like than expected from a more carefully initialized RNN.322
Discussion323
We have shown that training RNNs to estimate value in partially observable environments yields representa-324
tions that resemble beliefs. Specifically, we showed that, after training, the RNN activity i) could be linearly325
transformed to approximate beliefs, ii) could be used to decode the true state in the environment, and iii)326
had a dynamical structure consistent with beliefs.327
From a theoretical perspective, using an RNN resolves the problem of how to compute belief states, by328
replacing the fine-tuned Bayesian machinery needed for beliefs with a more general learned function approx-329
imator (e.g., a recurrent neural network). Our results illustrate that, to perform tasks in partially observable330
environments, it is not necessary for an agent or animal to explicitly estimate states using a belief representa-331
tion; rather, agents can learn a sufficient representation for solving the task from observations alone. This is332
22
.CC-BY 4.0 International licenseavailable under a 
was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made 
The copyright holder for this preprint (whichthis version posted April 7, 2023. ; https://doi.org/10.1101/2023.04.04.535512doi: bioRxiv preprint

promising from a normative perspective, as it shows how neural circuits might come to compute theoretical333
features such as beliefs without that objective needing to be explicitly learned. Moreover, there is a growing334
toolkit for reverse engineering RNN solutions [26, 27, 31], which can shed light on learned mechanisms of335
value computation.336
One potential benefit of the Value RNN over the Belief model for estimating value is the ability to sepa-337
rate the capacity of the model (i.e., the number of hidden units in the RNN) from the size of the state space338
in the environment. As we showed in Fig 6, Value RNNs with fewer units discovered a representation that339
was more compressed than beliefs, but nevertheless sufficient for performing the task at hand. Value RNNs340
with more units had more belief-like representations. This suggests a potentially useful trade-off, in which341
agents could choose to allocate more capacity to a task in exchange for more belief-like representations.342
Such a trade-off may be a relevant feature for biological organisms, who must be able to perform tasks such343
as value estimation in complex environments where it may not always be feasible to learn the full belief344
representation.345
From a methodological perspective, this work can serve as a blueprint for how to bridge analyses of neu-346
ral computation across levels of abstraction. In future work, we hope to apply this framework to test neural347
models of how animals perform associative learning via reinforcement learning. For instance, previous work348
has suggested that prefrontal cortex may perform state estimation in tasks with hidden states [6, 12, 7, 13].349
The same tools we apply here to artificial neural networks can also be applied to neural activity recorded350
from animals performing the same task. For instance, if cortex implements something like a Value RNN,351
cortical activity may show a longer transient response to odors during Task 1 than in Task 2 (Fig 5). On the352
other hand, if activity is more like a Value ESN, cortical representations should be largely the same in both353
tasks.354
Traditional models of how animals perform trace conditioning tasks like the ones we consider here make355
a variety of implicit assumptions about how animals represent the passage of time [32, 33]. For example, the356
state space shown in Fig 2A, which forms the basis of the belief representation, conceptualizes the passage357
of time in the form of microstates. Many modeling efforts require even more assumptions to account for358
scalar variability in animals’ estimates of elapsed time, such as by incorporating a more complex set of359
temporal basis functions. In our model, by contrast, the Value RNN’s time-varying representation of inputs360
23
.CC-BY 4.0 International licenseavailable under a 
was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made 
The copyright holder for this preprint (whichthis version posted April 7, 2023. ; https://doi.org/10.1101/2023.04.04.535512doi: bioRxiv preprint

is learned through training. We observed that individual units in our RNNs were tuned to elapsed time361
relative to observations, and that the temporal precision of tuning decreased with elapsed time (Fig S1),362
both of which are standard assumptions of microstate representations [34]. Similarly tuned “time cells” have363
been observed in the striatum [35], hippocampus [36], and prefrontal cortex [37]. Our modeling suggests364
that at least some assumptions about microstate representations may be redundant in the sense that they may365
emerge naturally in recurrent networks that are trained to perform reinforcement learning. This viewpoint366
resonates with the idea (reviewed in [38]) that delay encoding can arise as an emergent property of neural367
network dynamics.368
Previous work has shown that, in animals, prefrontal cortex activity is a necessary component of ani-369
mals’ state representations [13]. This work found that inactivating prefrontal cortex in the Starkweather task370
led to animals’ RPEs in Task 2 resembling the RPEs of Task 1. This is what one would expect if prefrontal371
cortex was involved in estimating a belief in omission trials. In fact, both Tasks 1 and 2 include another form372
of uncertainty, which is the reward time on each trial. The fact that prefrontal inactivation did not interact373
with animals’ estimates of timing suggests that different neural circuits may form belief-like representations374
specific to particular types of state uncertainty (e.g., temporal uncertainty versus reward uncertainty). In the375
present work, our RNNs should be thought of as a generic computational model, and not a model of individ-376
ual brain regions. These networks had a generic architecture and only a single layer; as a result, our model377
would be unable to distinguish between different sources of uncertainty. Nevertheless, it is an interesting378
question how architectural considerations, such as layer connectivity and the dominance of feedforward379
versus recurrent connectivity, might contribute to where in the brain different belief-like representations are380
formed.381
Here we have shown that computing beliefs explicitly is not a necessary precursor for optimally per-382
forming a task in partially observable environments. Nor is it required to reproduce experimentally observed383
patterns of dopamine neuron activity. Nevertheless, beliefs are an efficient representation in that they are384
sufficient for solving any task in the same environment. Thus, beliefs may be a desirable representation385
for animals, who may need to achieve a range of different goals in the same environment (e.g., finding wa-386
ter when thirsty, but finding food when hungry) without having to learn a representation in each of these387
tasks separately. Future work should explore whether a dedicated belief mechanism is necessary in these388
24
.CC-BY 4.0 International licenseavailable under a 
was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made 
The copyright holder for this preprint (whichthis version posted April 7, 2023. ; https://doi.org/10.1101/2023.04.04.535512doi: bioRxiv preprint

multi-task settings, or if the RNN framework we present here can also yield representations that effectively389
generalize to new tasks in the same environment.390
Materials and Methods391
Task implementation392
In each experiment, at each time step t, agents received two observations: an odor cue, ct∈{0, 1}; and a393
reward,rt∈{0,r }, where r >0 depended on the task (see below). We will refer to the total observation394
vector asot = [ctrt]. We treated each time step as equal to 200ms.395
Each trial began with an intertrial interval (ITI), tITI ∈ N, during which there were no observations396
(ot = 0 fort < tITI ). The ITI (offset by a minimum delay of 10 time steps) was sampled as tITI − 10∼397
Geom(pITI = 1
8), where Geom(p) is a geometric distribution with parameterp.398
Following the ITI, a single odor cue was presented as ct = 1 fort = tITI . The cue was then followed399
by another interval with no observations, called the interstimulus interval (ISI), tISI ∈ N. A reward was400
then presented as rt > 0 fort = tITI +tISI , after which point the trial terminated. The details of the ISI401
and reward size depended on the specific task, as described below.402
Starkweather tasks403
There were two versions of this task. In both Tasks 1 and 2, every non-zero reward size had rt = 1. In404
Task 2, with probability pomission = 0.1, the reward on a given trial was omitted, such that rt = 0 for the405
duration of the trial. In both tasks, the ISIs on each trial were sampled from a discretized Gaussian with406
meanµ = 10, standard deviationσ = 2.5, and range 6≤tISI≤ 14, as in Starkweather et al. [7].407
Babayan task408
In this task, non-zero reward sizes were determined in blocks of trials. In block 1, the non-zero reward size409
wasrt = 1, while in block 2 the non-zero reward size was rt = 10. Each block consisted of 5 sequential410
trials. Block identities were sampled uniformly with equal probability. On all trials, the ISIs were uniformly411
25
.CC-BY 4.0 International licenseavailable under a 
was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made 
The copyright holder for this preprint (whichthis version posted April 7, 2023. ; https://doi.org/10.1101/2023.04.04.535512doi: bioRxiv preprint

sampled as tISI ∼ Unif({9, 10, 11}). For Fig S2, sessions also included blocks of intermediate rewards:412
rt∈{ 1, 2, 4, 6, 8, 10}, where block identities were sampled in similar proportions to those used in Babayan413
et al. [10] (i.e., blocks withrt = 1 orrt = 10 comprised∼90% of the total trials).414
Recurrent neural network implementation415
We trained recurrent network models, in PyTorch, on multiple tasks to estimate value. Each Value RNN416
consisted of a GRU cell [24] with H∈ N units, followed by a linear readout of value. At each time step t,417
the RNN received observations,ot∈ R2, from a given experiment. The RNN’s representation can be written418
aszt = fϕ(ot,zt−1) given parametersϕ. The RNN’s output was the value estimate bVt = w⊤zt +w0,419
forw∈ RH andw0∈ R. The full parameter vector θ = [ϕw w0] was learned using TD learning. This420
involved backpropagating the gradient of the squared error lossδ2
t = (rt +γ bVt+1− bVt)2 with respect to bVt421
on episodes composed of 20 (Starkweather task) or 50 (Babayan task) concatenated trials. Unless otherwise422
noted we usedγ = 0.93 as in Starkweather et al. [13].423
For each task, and for each H∈{ 2, 5, 10, 20, 50, 100} units, we trained N = 12 networks. Prior to424
training each network, the weights and biases of the GRU (i.e., ϕ) were initialized using PyTorch’s default425
ofU(−a,a) wherea = 1√
H . Training then proceeded for a maximum of 150 epochs on a session of 10,000426
trials, with a batch size of 12 episodes. Training was stopped early if the loss increased for 4 consecutive427
epochs. Gradient updates used Adam with an initial learning rate of 0.003. No hyperparameter search was428
performed to fine-tune these choices. In the text, we refer toValue RNNsas the result of this training process,429
while Untrained RNNs are those that have been similarly initialized but not trained.430
The Value ESN was similar to a Value RNN, except that it was initialized differently, andϕ was frozen431
during training (i.e., the only learned parameters were w and w0). For initialization, we did the follow-432
ing (“Tensorflow-style” initialization). All of the GRU’s biases were initialized to zero. The GRU’s re-433
current weights were sampled as a random orthogonal matrix using torch.nn.init.orthogonal_434
with a given gain [30]. The GRU’s input weights were sampled as U(−a,a) where a =
q
6
2+H , using435
torch.nn.init.xavier_uniform_ [39].436
26
.CC-BY 4.0 International licenseavailable under a 
was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made 
The copyright holder for this preprint (whichthis version posted April 7, 2023. ; https://doi.org/10.1101/2023.04.04.535512doi: bioRxiv preprint

State and belief representations437
Given a task with hidden states s∈{1,...,K }, the belief,bt∈ [0, 1]K, is the posterior probability distri-
bution over each possible state [17]. The tasks we analyze here are technically discrete-time semi-Markov
processes, and so we follow previous work in formulating them equivalently as Markov processes with
micro-states defined over each relevant discrete time step [6, 7]. In this setting, observations occur at the
transition between states. As a result, the belief in state can be written as:
bt(k)∝
KX
k′=1
Oot(k′,k )T (k′,k )bt−1(k′) (12)
whereT∈ [0, 1]K×K is the matrix of transition probabilities, and Oo(k′,k ) is the probability of observing438
o after making a transition fromk tok′.439
Starkweather tasks440
In both Tasks 1 and 2 there are three distinct observations, ot∈{[0 0], [1 0], [0x]}, which we refer to as441
the null, odor, and reward observations, respectively. Let the possible reward times betISIs ={6,..., 14}.442
The maximum reward time is max(tISIs ) = 14 , and so we let states 1− 14 be the ISI microstates. The443
ITI is a Geometric distribution plus a minimum ITI of tITI = 10, and so we let states 15− 25 be the ITI444
microstates. There areK = 25 total states.445
We first define the observation probabilities,Onull,Oodor,Oreward∈{ 0, 1}K×K, whereOo(k′,k ) indi-446
cates the probability of having transitioned from statek to statek′ upon observingo∈{null,odor,reward}.447
EachOo(k′,k ) = 0 except at the following:448
• Onull(t + 1,t) = 1 for allt̸= max(tISIs )449
• Onull(K,K ) = 1450
• Oodor(t,K ) = 1 fort = 1 (Task 1) ort∈{ 1, max(tISIs ) + 1} (Task 2)451
• Oreward(max(tISIs ) + 1,t) = 1 fort∈tISIs452
27
.CC-BY 4.0 International licenseavailable under a 
was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made 
The copyright holder for this preprint (whichthis version posted April 7, 2023. ; https://doi.org/10.1101/2023.04.04.535512doi: bioRxiv preprint

To define the transition probabilities, letpt∈ [0, 1] be the probability of receiving reward at timet∈tISIs ,453
Ft = P
t′≤tpt′ the cumulative probability, andht = pt/(1−Ft) the hazard. Recall that pITI = 1
8. Then454
T (k′,k ) = 0 except at the following:455
• T (t + 1,t) = 1 fort /∈ max(tISIs )456
• T (t + 1,t) = 1−ht andT (max(tISIs ) + 1,t) = ht fort∈tISIs457
• T (K,K ) = 1−pITI458
• T (max(tISIs ) + 1,K) =pITIpomission459
• T (1,K ) =pITI (1−pomission)460
Babayan task461
The states in this task can be thought of as two copies of the beliefs in the Starkweather tasks, with one copy
for each of the two blocks. (Note that tISIs ={9, 10, 11},K = 22, and the hazard probabilities must be
modified from the Starkweather task to account for the different reward timing distribution.) Each copy has
11 ISI microstates (because the maximum reward time is max(tISIs ) = 11) and 11 ITI microstates. Let
b(1)
t ∈ [0, 1]22 andb(2)
t ∈ [0, 1]22 be the beliefs for the substates of block 1 and block 2, respectively. Then
the full beliefbt∈ [0, 1]44 is as follows:
bt = [ptb(1)
t (1−pt)b(2)
t ]
pt =f(rt) ifrt> 0 otherwisept−1
(13)
wherept∈ [0, 1] is the estimated probability of being in block 1, and f is our likelihood function mapping462
nonzero rewards,rt, to the estimated probability of being in block 1 vs. block 2. In other words, we modeled463
the belief in the block identity as being a function only of the most recently observed reward. We definedf464
following the original paper: Let ϕ(rt;µ,σ ) be the pdf of a Normal distribution with mean µ and standard465
deviationσr > 0. Thenf(rt) = ϕ(rt;µ1,σr)
ϕ(rt;µ1,σr)+ϕ(rt;µ2,σr), whereµ1 = 1 andµ2 = 10 are the rewards amounts466
in block 1 and 2, respectively. Here we assumedσr was arbitrarily small, so we usedσr = 0.001.467
28
.CC-BY 4.0 International licenseavailable under a 
was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made 
The copyright holder for this preprint (whichthis version posted April 7, 2023. ; https://doi.org/10.1101/2023.04.04.535512doi: bioRxiv preprint

Model analyses468
We analyzed exemplars from each model class (Beliefs, Value RNNs, Untrained RNNs, Value ESNs) using469
two sessions of 1,000 concatenated trials each, using the same task parameters as those used when training470
the RNNs (see above). The first session was used for fitting any parameters relevant to the analysis (i.e.,471
value weights, regression weights, decoding weights), while the second session was used for evaluation.472
Because the RNN’s responses were deterministic functions of their inputs, prior to analysis we added noise473
to all RNN representations to prevent overfitting during regression and decoding as follows. Let σi > 0474
be the sample standard deviation of the activity of hidden unit i across trials. Then we added zero-mean475
Gaussian noise with a standard deviation of 0.01σi to this unit’s activity, so that each unit had the same476
SNR: 10 log10(σ2
i/(σ2
i 0.012)) = 40 dB.477
Value estimates478
Each model’s value estimate was given by bVt = z⊤
t bw +w0, where bw∈ RD andw0∈ R are the value479
weights, andzt∈ RD is the model’s representation at timet. (For the belief model,zt =bt.)480
We estimated the value weights, bw, using Least-Squares TD (LSTD) [22]: bw = bD−1bd, where bD =481
PT−1
t=1 zt(zt−γzt+1)⊤ and bd = PT−1
t=1 rtzt. To ensure each model’s value function was estimated using482
the same procedure, we used LSTD even for the models including RNNs, even though the Value RNNs and483
Value ESNs learned their own value weights during training.484
Reward prediction errors485
To assess how close each RNN’s RPEs came to the RPEs found using the belief model, we defined an RNN’s486
RPE error using the mean squared error: 1
T
PT
t=1(δt− bδt)2, where bδt is the RNN’s RPE, andδt is the RPE487
from the belief model. Because each trial had at most one reward delivery, for simplicity we considered the488
RPEs only at the time of reward delivery on each trial (i.e., the t in the above equation refers to a trial and489
not a time step); this simplification did not affect our results.490
29
.CC-BY 4.0 International licenseavailable under a 
was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made 
The copyright holder for this preprint (whichthis version posted April 7, 2023. ; https://doi.org/10.1101/2023.04.04.535512doi: bioRxiv preprint

Belief R2491
To assess how much variance of the beliefs could be explained by each model’s learned representation, we
used multivariate linear regression:
cW = (Z⊤Z)−1Z⊤B (14)
whereZ∈ RT×(H+1) is the matrix whose tth row is [zt 1],B∈ RT×K is the matrix whose tth row isbt,492
and cW∈ R(H+1)×K.493
To evaluate model fit, let Var(X) = 1
T
PT
t=1∥xt−x∥2
2, wherext is thetth row ofX, andx is the mean
of the rows ofX. Then we calculated the total variance explained:
R2 = 1− Var(B−Z cW )
Var(B) (15)
State decoding494
We asked where we could find a decoder that could infer the underlying state, st∈{1,...,K }, using an495
affine transformation of the RNN’s representation,zt∈ RH. To find such a decoder, we first standardized496
each model representation (considering each dimension ofzt in isolation) to have zero mean and unit vari-497
ance. We then performed a multinomial logistic regression using scikit-learn’s498
linear model.LogisticRegression with the parameters multi class="multinomial",499
C=1, and max iter=1e4.500
After training, the decoder’s estimated state probabilities overst are:
πt = softmax(˜z⊤
t cW )∈ [0, 1]K (16)
where cW ∈ R(H+1)×K contains the decoder parameters; ˜zt∈ RH+1 is the model representation at time501
t after standardization, plus an extra constant column of 1’s to fit the offset; and the softmax function502
normalizes the vector to be a valid probability over theK values ofst.503
To evaluate the resulting decoder, we calculated the model’s log-likelihood (ℓ) on the evaluation session
30
.CC-BY 4.0 International licenseavailable under a 
was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made 
The copyright holder for this preprint (whichthis version posted April 7, 2023. ; https://doi.org/10.1101/2023.04.04.535512doi: bioRxiv preprint

as follows:
ℓ(cW|s1,...,s T, ˜z1,..., ˜zT ) = 1
T
TX
t=1
log(πt(st)) (17)
whereπt(st) ∈ [0, 1] is the sth
t entry of the vector πt. We calculated the log-likelihood for the belief504
model similarly, except instead of training a decoder we used πt = bt. For the Babayan task (Fig 5E),505
we calculated the log-likelihood on all trials except the first trial in each block. This was necessary for the506
beliefs to act as an upper-bound on the log-likelihood, because we defined the beliefs in a way that did not507
assume knowledge of the number of trials in each block.508
Dynamics analysis509
An RNN with parametersϕ has a hidden state that evolves aszt =fϕ(ot,zt−1). Conditioned on a particular510
constant input,o, an RNN is at a fixed point when∥fϕ(o,z)−z∥2
2≈ 0. Numerically, we can simply look511
forz where∥fϕ(o,z)−z∥2
2<ϵ . For our analyses below we choseϵ = 1× 10−5.512
Identifying fixed points (Fig 5B, Fig 7G). During training, RNNs received three distinct types of inputs,513
ot∈{[0 0], [1 0], [0r]}, which we refer to as the null (∅), odor, and reward inputs, respectively. Under the514
beliefs of the Starkweather and Babayan tasks, the odor and reward inputs always result in a change in the515
beliefs. As a result, any fixed points of the beliefs must be conditional on the null input, ∅. We therefore516
sought to identify an RNN’s fixed points conditional on a null input. To do this, we took a numerical ap-517
proach: We initialized the RNN to a random state, applied the null input until the RNN’s activity converged,518
and then repeated this process across different random states to get a candidate set of fixed points. More pre-519
cisely, we consideredN = 20 randomly selected values ofz in the testing data following an odor or reward520
observation as a set of starting seeds. For each starting seed,z0, we computed the RNN’s representation,zt,521
over time, given no further odor or reward observations:zt =fϕ(∅,zt−1). We repeated this process until522
ηt =∥zt−zt−1∥2
2<ϵ. We then added zt to our list of candidate fixed points,F. For each pair of candidate523
fixed points within a distance 1× 10−3 of each other, we considered these to be the same fixed point.524
Odor and reward memory duration (Fig 5C, Fig 5D). For each Value RNN with a single fixed point,525
we measured the network’s odor (or reward) memory as follows. We initialized each RNN to its fixed526
31
.CC-BY 4.0 International licenseavailable under a 
was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made 
The copyright holder for this preprint (whichthis version posted April 7, 2023. ; https://doi.org/10.1101/2023.04.04.535512doi: bioRxiv preprint

point,z0, and then provided an odor (or reward) observation at time t = 1. We then measured the RNN’s527
representation,zt, over time, given no further odor or reward observations: zt = fϕ(∅,zt−1), for t >1.528
For each t, we calculated the distance of the activity from its fixed point: ηt =∥zt−z0∥2
2 (Fig 5C). We529
repeated this until ηt converged to zero, defining the odor memory (or reward memory) as the t at which530
ηt< 1× 10−3 (Fig 5D).531
Data Availability Statement532
All data and code used for analysis and plotting is available on a GitHub repository athttps://github.533
com/mobeets/value-rnn-beliefs/534
Author Contributions535
Conceptualization: Jay A. Hennig, Sandra A. Romero Pinto, Takahiro Yamaguchi, Naoshige Uchida,536
Samuel J. Gershman537
Formal analysis: Jay A. Hennig538
Investigation: Jay A. Hennig539
Funding acquisition: Samuel J. Gershman, Naoshige Uchida, Scott W. Linderman540
Methodology: Jay A. Hennig, Samuel J. Gershman541
Supervision: Scott W. Linderman, Naoshige Uchida, Samuel J. Gershman542
Visualization: Jay A. Hennig543
Writing - original draft: Jay A. Hennig544
Writing - review & editing: Jay A. Hennig, Sandra A. Romero Pinto, Takahiro Yamaguchi, Scott W.545
Linderman, Naoshige Uchida, Samuel J. Gershman546
32
.CC-BY 4.0 International licenseavailable under a 
was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made 
The copyright holder for this preprint (whichthis version posted April 7, 2023. ; https://doi.org/10.1101/2023.04.04.535512doi: bioRxiv preprint

Acknowledgments547
This work was funded by NIH U19 NS113201-01 and Air Force Office of Scientific Research grant FA9550-548
20-1-0413.549
References
[1] Wolfram Schultz, Peter Dayan, and P Read Montague. A neural substrate of prediction and reward.
Science, 275:1593–1599, 1997.
[2] Hannah M Bayer and Paul W Glimcher. Midbrain dopamine neurons encode a quantitative reward
prediction error signal. Neuron, 47(1):129–141, 2005.
[3] Jeremiah Y Cohen, Sebastian Haesler, Linh V ong, Bradford B Lowell, and Naoshige Uchida. Neuron-
type-specific signals for reward and punishment in the ventral tegmental area. nature, 482(7383):
85–88, 2012.
[4] Neir Eshel, Michael Bukwich, Vinod Rao, Vivian Hemmelder, Ju Tian, and Naoshige Uchida. Arith-
metic and local circuitry underlying dopamine prediction errors. Nature, 525(7568):243–246, 2015.
[5] Leslie Pack Kaelbling, Michael L Littman, and Anthony R Cassandra. Planning and acting in partially
observable stochastic domains. Artificial intelligence, 101(1-2):99–134, 1998.
[6] Nathaniel D Daw, Aaron C Courville, and David S Touretzky. Representation and timing in theories
of the dopamine system. Neural computation, 18(7):1637–1677, 2006.
[7] Clara Kwon Starkweather, Benedicte M Babayan, Naoshige Uchida, and Samuel J Gershman.
Dopamine reward prediction errors reflect hidden-state inference across time. Nature neuroscience,
20(4):581–589, 2017.
[8] Armin Lak, Kensaku Nomoto, Mehdi Keramati, Masamichi Sakagami, and Adam Kepecs. Midbrain
dopamine neurons signal belief in choice accuracy during a perceptual decision. Current Biology, 27:
821–832, 2017.
33
.CC-BY 4.0 International licenseavailable under a 
was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made 
The copyright holder for this preprint (whichthis version posted April 7, 2023. ; https://doi.org/10.1101/2023.04.04.535512doi: bioRxiv preprint

[9] Stefania Sarno, Victor de Lafuente, Ranulfo Romo, and N ´estor Parga. Dopamine reward prediction
error signal codes the temporal evaluation of a perceptual decision report.Proceedings of the National
Academy of Sciences, 114:E10494–E10503, 2017.
[10] Benedicte M Babayan, Naoshige Uchida, Samuel Gershman, et al. Belief state representation in the
dopamine system. Nature communications, 9(1):1–10, 2018.
[11] John G Mikhael, HyungGoo R Kim, Naoshige Uchida, and Samuel J Gershman. The role of state
uncertainty in the dynamics of dopamine. Current Biology, 32:1077–1087, 2022.
[12] Robert C Wilson, Yuji K Takahashi, Geoffrey Schoenbaum, and Yael Niv. Orbitofrontal cortex as a
cognitive map of task space. Neuron, 81(2):267–279, 2014.
[13] Clara Kwon Starkweather, Samuel J Gershman, and Naoshige Uchida. The medial prefrontal cortex
shapes dopamine reward prediction errors under state uncertainty. Neuron, 98(3):616–629, 2018.
[14] Samuel J Gershman and Naoshige Uchida. Believing in dopamine. Nature Reviews Neuroscience, 20:
703–714, 2019.
[15] Alexandre Pouget, Jeffrey M Beck, Wei Ji Ma, and Peter E Latham. Probabilistic brains: knowns and
unknowns. Nature Neuroscience, 16(9):1170–1178, 2013.
[16] Nathaniel D Daw, Yael Niv, and Peter Dayan. Uncertainty-based competition between prefrontal and
dorsolateral striatal systems for behavioral control. Nature Neuroscience, 8:1704–1711, 2005.
[17] Rajesh PN Rao. Decision making under uncertainty: a neural model based on partially observable
markov decision processes. Frontiers in computational neuroscience, 4:146, 2010.
[18] Pascal Poupart and Craig Boutilier. Value-directed compression of POMDPs. Advances in Neural
Information Processing Systems, 15, 2002.
[19] Nicholas Roy, Geoffrey Gordon, and Sebastian Thrun. Finding approximate POMDP solutions through
belief compression. Journal of Artificial Intelligence Research, 23:1–40, 2005.
34
.CC-BY 4.0 International licenseavailable under a 
was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made 
The copyright holder for this preprint (whichthis version posted April 7, 2023. ; https://doi.org/10.1101/2023.04.04.535512doi: bioRxiv preprint

[20] Matthew Botvinick, Jane X Wang, Will Dabney, Kevin J Miller, and Zeb Kurth-Nelson. Deep rein-
forcement learning and its neuroscientific implications. Neuron, 107(4):603–616, 2020.
[21] Tianwei Ni, Benjamin Eysenbach, and Ruslan Salakhutdinov. Recurrent model-free RL can be a strong
baseline for many POMDPs. In Kamalika Chaudhuri, Stefanie Jegelka, Le Song, Csaba Szepesvari,
Gang Niu, and Sivan Sabato, editors, Proceedings of the 39th International Conference on Machine
Learning, volume 162 of Proceedings of Machine Learning Research, pages 16691–16723. PMLR,
17–23 Jul 2022.
[22] Richard S Sutton and Andrew G Barto. Reinforcement learning: An introduction. MIT press, 2018.
[23] Samuel J Gershman and Nathaniel D Daw. Reinforcement learning and episodic memory in humans
and animals: an integrative framework. Annual Review of Psychology, 68:101–128, 2017.
[24] Kyunghyun Cho, Bart Van Merri ¨enboer, Caglar Gulcehre, Dzmitry Bahdanau, Fethi Bougares, Hol-
ger Schwenk, and Yoshua Bengio. Learning phrase representations using rnn encoder-decoder for
statistical machine translation. arXiv preprint arXiv:1406.1078, 2014.
[25] David Sussillo and Omri Barak. Opening the black box: low-dimensional dynamics in high-
dimensional recurrent neural networks. Neural computation, 25(3):626–649, 2013.
[26] Niru Maheswaranathan, Alex Williams, Matthew Golub, Surya Ganguli, and David Sussillo. Univer-
sality and individuality in neural dynamics across large populations of recurrent networks. Advances
in neural information processing systems, 32, 2019.
[27] Saurabh Vyas, Matthew D Golub, David Sussillo, and Krishna V Shenoy. Computation through neural
population dynamics. Annual review of neuroscience, 43:249–275, 2020.
[28] Mantas Luko ˇseviˇcius and Herbert Jaeger. Reservoir computing approaches to recurrent neural network
training. Computer science review, 3(3):127–149, 2009.
[29] Herbert Jaeger. Echo state network. scholarpedia, 2(9):2330, 2007.
35
.CC-BY 4.0 International licenseavailable under a 
was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made 
The copyright holder for this preprint (whichthis version posted April 7, 2023. ; https://doi.org/10.1101/2023.04.04.535512doi: bioRxiv preprint

[30] Andrew M Saxe, James L McClelland, and Surya Ganguli. Exact solutions to the nonlinear dynamics
of learning in deep linear neural networks. arXiv preprint arXiv:1312.6120, 2013.
[31] Jimmy Smith, Scott Linderman, and David Sussillo. Reverse engineering recurrent neural networks
with Jacobian switching linear dynamical systems. Advances in Neural Information Processing Sys-
tems, 34:16700–16713, 2021.
[32] Samuel J Gershman, Ahmed A Moustafa, and Elliot A Ludvig. Time representation in reinforcement
learning models of the basal ganglia. Frontiers in computational neuroscience, 7:194, 2014.
[33] Vijay Mohan K Namboodiri. How do real animals account for the passage of time during associative
learning? Behavioral Neuroscience, 2022.
[34] Elliot A Ludvig, Richard S Sutton, and E James Kehoe. Stimulus representation and the timing of
reward-prediction errors in models of the dopamine system. Neural Computation, 20:3034–3054,
2008.
[35] Gustavo BM Mello, Sofia Soares, and Joseph J Paton. A scalable population code for time in the
striatum. Current Biology, 25:1113–1122, 2015.
[36] Christopher J MacDonald, Kyle Q Lepage, Uri T Eden, and Howard Eichenbaum. Hippocampal “time
cells” bridge the gap in memory for discontiguous events. Neuron, 71:737–749, 2011.
[37] Zoran Tiganj, Min Whan Jung, Jieun Kim, and Marc W Howard. Sequential firing codes for time in
rodent medial prefrontal cortex. Cerebral Cortex, 27:5663–5671, 2017.
[38] Joseph J Paton and Dean V Buonomano. The neural basis of timing: distributed mechanisms for
diverse functions. Neuron, 98(4):687–705, 2018.
[39] Xavier Glorot and Yoshua Bengio. Understanding the difficulty of training deep feedforward neu-
ral networks. In Proceedings of the thirteenth international conference on artificial intelligence and
statistics, pages 249–256. JMLR Workshop and Conference Proceedings, 2010.
36
.CC-BY 4.0 International licenseavailable under a 
was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made 
The copyright holder for this preprint (whichthis version posted April 7, 2023. ; https://doi.org/10.1101/2023.04.04.535512doi: bioRxiv preprint

Supplemental Figures
Fig S1. RNN activity before and after training on Starkweather Task 2. a. Obser-
vations, states, beliefs, and RNN activations on two example trials from Task 2. b-c.
RNN unit activity (individually normalized to span between 0 and 1), with units sorted by
time of peak activation on held-out trials, on an RNN before (panel b) and after (panel c)
training. Both before and after after training, RNN units exhibited tuning to elapsed time
following observations, with variance that scaled with elapsed time.
S1
.CC-BY 4.0 International licenseavailable under a 
was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made 
The copyright holder for this preprint (whichthis version posted April 7, 2023. ; https://doi.org/10.1101/2023.04.04.535512doi: bioRxiv preprint

Fig S2. Value RNNs trained on the Babayan task recapitulate dopamine activity
and belief RPEs in response to intermediate reward sizes. a-b. Average dopamine
response on trial 1 (panel a) and trial 2 (panel b) during probe sessions including blocks
with intermediate reward sizes. Circles and lines depict mean ± SE across N = 11
animals. Reproduced from Babayan et al. [10]. c-d. Same as panels a-b, but for the
RPEs of the Belief model (black) and Value RNNs (purple). Value RNNs were trained
on sessions including only blocks with rewards rt∈{1, 10}, as in the main text. Value
weights for the Belief model and Value RNNs were fit using a test session including 39
blocks each withrt = 1 andrt = 10, and 3 blocks each with rt∈{2, 4, 6, 8}, similar to
the proportions used in Babayan et al. [10]. RPEs were then measured on a different test
session. Purple circles and lines depict mean± SE acrossN = 12 models.
S2
.CC-BY 4.0 International licenseavailable under a 
was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made 
The copyright holder for this preprint (whichthis version posted April 7, 2023. ; https://doi.org/10.1101/2023.04.04.535512doi: bioRxiv preprint

Fig S3. Value RNNs trained on the Babayan task exhibit one fixed point. a. RNN
activity during two example trials, one during Block 1 (left) and the other during Block
2 (right). Same as Fig 7D. Here we also include RNN activity trajectories if each reward
had been omitted. While activity for the Block 2 trial initially returns to the putative ITI 2
state, it eventually returns to the true fixed point at ITI 1 b. Distance of RNN activity
from the single fixed point (e.g., ITI 1 in panel a) following an odor observation (i.e., an
omission trial). While the maximum ITI duration is theoretically infinite, the maximum
ITI duration in the training data was at t = 65. RNN activity on Block 2 trials therefore
remained separate from the activity on Block 1 trials for the range of experienced ITI
durations.
S3
.CC-BY 4.0 International licenseavailable under a 
was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made 
The copyright holder for this preprint (whichthis version posted April 7, 2023. ; https://doi.org/10.1101/2023.04.04.535512doi: bioRxiv preprint
