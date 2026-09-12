##### Report GitHub Issue

Content selection saved. Describe the issue below:

# Continual Learning and Catastrophic Forgetting

###### Abstract

This book chapter delves into the dynamics of continual learning, which is the process of incrementally learning from a non-stationary stream of data. Although continual learning is a natural skill for the human brain, it is very challenging for artificial neural networks. An important reason is that, when learning something new, these networks tend to quickly and drastically forget what they had learned before, a phenomenon known as catastrophic forgetting. Especially in the last decade, continual learning has become an extensively studied topic in deep learning. This book chapter reviews the insights that this field has generated.

## Key Points

• Incrementally learning from a non-stationary stream of data, referred to as continual learning, is a key aspect of intelligence.

• Artificial neural networks tend to rapidly and drastically forget previously learned information when learning something new, a phenomenon referred to as catastrophic forgetting.

• Catastrophic forgetting is an important reason why continual learning is so challenging for deep neural networks, but solving the continual learning problem requires more than preventing catastrophic forgetting.

• Two distinctions often made in the deep learning literature on continual learning are between task-based and task-free continual learning, and between task-, domain- and class-incremental learning. These two distinctions are orthogonal to each other, and can be captured in a single framework.

• Deep learning methods for continual learning are evaluated using metrics covering performance, diagnostic analysis and resource efficiency.

• Six main computational approaches for continual learning with deep neural networks are (i) replay, (ii) parameter regularization, (iii) functional regularization, (iv) optimization-based approaches, (v) context-dependent processing and (vi) template-based classification.

• Establishing further connections between deep learning and cognitive science in the context of continual learning could benefit both fields.

## 1 Introduction

Continual learning is a key aspect of intelligence. The ability to accumulate knowledge by incrementally learning from one’s experiences is an important skill for any agent, natural or artificial, that operates in a non-stationary world. Humans are excellent continual learners. The human brain can incrementally learn new skills without compromising those that were learned before, and it is able to integrate and contrast new information with previously acquired knowledge ( Flesch et al., 2018 ; Kudithipudi et al., 2022 ) . Intriguingly, artificial deep neural networks, although rivaling human intelligence in other ways, almost completely lack this ability to learn continually. Most strikingly, when these networks are trained on something new, they tend to “catastrophically” forget what they had learned before ( McCloskey and Cohen, 1989 ; Ratcliff, 1990 ) .

The inability of deep neural networks to continually learn has important practical implications. Due to its powerful representation learning capabilities, deep learning has become a major driving force behind many recent advances in artificial intelligence. However, to achieve their strong performance, deep neural networks must be trained for extended periods of time on large amounts of data (e.g., Radford et al., 2021 ). This resource-intensive training makes the lack of continual learning abilities of these networks particularly costly. For example, if after an expensive training process has finished, relevant new data become available, rapidly updating the network by training only on the new data does not work. To avoid adapting too strongly to the new data, the network must be trained on both old and new data together. However, even such continued joint training often does not yield satisfactory results. Instead, practitioners in industry tend to periodically retrain the entire network from scratch on all data, despite the large computational costs ( Huyen, 2022 ) . Therefore, developing successful continual learning methods for deep learning could result in significant efficiency gains and a substantial reduction in the required resources. Another important potential application for continual learning is correcting errors or biases. After being trained, deep neural networks are often found to make mistakes or have certain biases (e.g., a subset of demographics is underrepresented in the training set), but updating a network to correct for these is difficult ( Mitchell et al., 2022 ) . Another practical use case of continual learning is in edge applications ( Deng et al., 2020 ) . These applications require the ability to learn in real-time on-device to reduce their reliance on pre-deployed solutions. For these and other reasons (e.g., see Verwimp et al., 2023 ), continual learning has become an intensively studied topic in deep learning, and is seen as one of the main open challenges in the field ( Hadsell et al., 2020 ; Bubeck et al., 2023 ) .

In addition to the practical arguments above, another motivation for studying continual learning in deep neural networks is to gain insight into the computational principles that might underlie the cognitive processes supporting continual learning in the brain. Artificial deep neural networks are a popular class of computational models that can account for many aspects of information processing in the brain (e.g., van Gerven and Bohte, 2017 ; Perconti and Plebe, 2020 ; Doerig et al., 2023 ). Yet, in terms of continual learning, this class of models has clear insufficiencies. If we can understand the reasons for this failure and how to fix it, this might give clues as to which computational processes underlie the cognitive skill of continual learning. At the same time, but in the reverse direction, the brain’s exceptional ability to continually learn can serve as a source of inspiration for the development of novel continual learning algorithms for deep learning.

The structure of this book chapter is as follows. Section 2 introduces the problem of continual learning, illustrates why it is so challenging for deep neural networks, and discusses different variants of the continual learning problem. Section 3 covers various computational strategies that have been proposed to improve the continual learning capabilities of neural networks. Section 4 compares how continual learning is studied in cognitive science versus in deep learning, and section 5 concludes.

## 2 The Continual Learning Problem

Continual learning is the skill of incrementally learning from a non-stationary stream of data. In this definition, the term “non-stationary” indicates that the distribution of the data from which is learned changes over time. The term “incrementally” signals that new learning should not overwrite what was learned before, but that knowledge should be accumulated. In this section, we discuss why continual learning is so challenging for artificial deep neural networks (subsections 2.1 and 2.2 ), we review different types of continual learning (subsections 2.3 and 2.4 ), and we briefly discuss how continual learning is evaluated (subsection 2.5 ).

### 2.1 Catastrophic Forgetting

Central to continual learning is the concept of catastrophic forgetting, also referred to as catastrophic interference. Catastrophic forgetting is the phenomenon that artificial neural networks tend to rapidly and drastically forget previously learned information when learning new information (see Fig. 1 ).

When a neural network is sequentially trained on multiple tasks, forgetting of earlier tasks can be expected because the network parameters are adjusted to optimize the loss on the new task, which likely pushes these parameters away from their optimum value that was found for the earlier tasks. It was appreciated early on that such forgetting would occur when incrementally training a neural network on multiple tasks, but initially it was speculated that this forgetting might be relatively mild: Hinton et al. (1986) hypothesized that the many small parameter updates that work together to optimize the new task, might mostly cancel each other out in terms of their effect on previous tasks. This however turned out not to be the case. McCloskey and Cohen (1989) and Ratcliff (1990) were the first to demonstrate that the sequential training of simple neural networks on disjoint sets of data results in drastic forgetting, even with only small amounts of training on the new data distribution. McCloskey and Cohen also noted that this forgetting is substantially worse than that observed in humans, which prompted them to describe it as “catastrophic”.

Inspired by the observations from McCloskey and Cohen and Ratcliff , in the 1990s several research groups began exploring the problem of catastrophic forgetting in early connectionist models. The proposed solutions incorporated concepts such as reducing network overlap (e.g., sparse or orthogonal representations) and the rehearsal of prior data (see Robins, 1995 and French, 1999 for reviews). Following these works, the early concepts of continual learning began to emerge ( Thrun and Mitchell, 1995 ) . More recently, Srivastava et al. (2013) and Goodfellow et al. (2013) demonstrated that catastrophic forgetting remains a problem in modern deep learning architectures, which had just begun gaining popularity. Since then there has been a rapid rise in the number of deep learning studies addressing the problem of continual learning.

### 2.2 Other Features Important for Continual Learning

While catastrophic forgetting is the root cause for why continual learning is so challenging for neural networks, it is not the case that preventing catastrophic forgetting is enough to solve the continual learning problem. One reason for this is that approaches that lower forgetting often introduce or exacerbate other issues. For example, reduced forgetting often comes at the cost of an impaired ability to learn new information, a trade-off known as the stability-plasticity dilemma ( Grossberg, 1982 ) . Another example is that catastrophic forgetting could be avoided by always training on all data seen so far, but this approach presents significant challenges in terms of memory and computation usage. Among others, Díaz-Rodríguez et al. (2018) , Mundt et al. (2022) , Prabhu et al. (2023) and Verwimp et al. (2023) have stressed that continual learning should focus on more than just preventing forgetting.

In a recent perspective article, Kudithipudi et al. (2022) argued that, in addition to avoiding catastrophic forgetting, successful continual learning methods should exhibit the following features for full-scale operation:

1. Adaptation - Continual learning models must be able to quickly adapt to new situations or surroundings, without requiring extensive offline (re)training. Such rapid adaptation is essential when models are deployed in the real world, where conditions may vary considerably and change quickly. It was recently shown that incremental training of deep neural networks on a sequence of tasks can lead to a substantial loss of plasticity ( Dohare et al., 2023 ) , highlighting that rapid adaptation is still an open problem in continual learning.

2. Exploiting task similarity - When the different tasks (or contexts) that must be learned are related, it should be possible to exploit their similarity to achieve ‘positive transfer’ between tasks. Positive transfer means that due to learning one task, the network also becomes better at another task – either directly in terms of performance improvement, or indirectly by making (re)learning of that task easier. For example, once a human has learned to play a first musical instrument (e.g., the piano), it is typically easier for them to master a second one (e.g., the violin). In continual learning, there are two types of transfer: forward transfer , whereby learning a new task facilitates future tasks; and backward transfer , whereby learning a new task benefits previously learned tasks. Especially positive backward transfer has proven to be a challenging feature to achieve with artificial deep neural networks ( Lopez-Paz and Ranzato, 2017 ) . A promising route to enabling improved knowledge transfer between tasks is learning compositional representations ( Mendez and Eaton, 2023 ) .

3. Task agnostic - In many real world problem settings, continual learning models cannot rely on an oracle to tell them for each encountered example to which task (or domain / context) it belongs. It is often a desirable property for continual learning models to be task agnostic . The term task agnostic can refer to multiple different things: not knowing task identity during testing, not knowing task identity during training, not being informed about task switches, or even that there is no discrete set of underlying tasks at all. Various forms of being task agnostic are covered in subsections 2.3 and 2.4 .

4. Noise tolerance - Deep learning models are usually trained on datasets that are curated, cleaned, and annotated to optimize training (e.g., ImageNet; Deng et al., 2009 ). Training instead on non-curated datasets can lead to substantially lower performance and generalization capabilities ( Tian et al., 2021 ) . For practical applications of continual learning, it is important that models are able to deal with data in the form they arrive – raw, noisy and uncleaned; as well as with situations in which the noise level or distribution changes over time, for example due to variability in the environment or in the sensors.

5. Resource efficiency and sustainability - When deep neural networks are expected to continue learning for extended periods of time, it is critical that they do so in a sustainable and resource efficient manner. Existing continual learning methods often violate this desideratum ( Vogelstein et al., 2020 ; Prabhu et al., 2023 ) . For example, storing all data points that are encountered (e.g., in a memory buffer) can be problematic in terms of required storage space, while constantly retraining on all previous tasks can quickly become infeasible in terms of computational costs. Verwimp et al. (2023) argued that he goal of continual learning can be interpreted as finding the best approach in terms of some trade-off between performance and resource efficiency (e.g., memory and compute), whereby the relative importances in the trade-off differ depending on the problem.

### 2.3 Task-based versus Task-free Continual Learning

A common assumption in continual learning research is that there is a discrete set of tasks that are presented to the network one after the other, often with marked boundaries between tasks. This task-based continual learning setting is illustrated in Fig. 2 a. A popular way to set up a task set for continual learning is to take an existing dataset (e.g., MNIST, LeCun et al., 1998 ; CIFAR-100, Krizhevsky, 2009 ; MiniImageNet, Vinyals et al., 2016 ) and split it into tasks based on the class labels (e.g., Split MNIST; see Fig. 2 ). Another common way to create multiple tasks from a single dataset is to use task-specific transformations, for example rotations, permutations or the addition of noise. An alternative approach is to interweave multiple datasets (e.g., one task contains the ten MNIST-digits, another task contains the ten digits from the SVHN dataset; Netzer et al., 2011 ). Task-based continual learning is an important and frequently used setting in the literature because it provides a convenient way to study various aspects of continual learning in a controlled and isolated manner.

However, not all aspects of the rich pattern of non-stationarity in the real world are well captured by the task-based continual learning setting. For example, continual learning methods developed in the task-based setting can be reliant on the presence of hard boundaries between tasks (to perform certain consolidation operations, such as updating the memory buffer or replacing a stored copy of the model) ( Aljundi et al., 2019b ; Zeno et al., 2019 ) , and for many methods it is unclear how they could benefit if a previously seen task is encountered again ( Stojanov et al., 2019 ; Hemati et al., 2023 ) . This has motivated the emergence of task-free continual learning (Fig. 2 b), which allows for gradual transitions between tasks and repetition of tasks. With task-free continual learning, there is usually still an underlying set of discrete tasks (e.g., Lee et al., 2020 ; Jin et al., 2021 ; Shanahan et al., 2021 ), but the transitions between those tasks are continuous, in the sense that the probabilities of observing each task gradually change over time. A description of how the probabilities of observing each task change over time has been referred to as a schedule ( Shanahan et al., 2021 ; Wang et al., 2022a ) .

Following van de Ven et al. (2022) , the above descriptions of task-based and task-free continual learning can be formalized by letting 𝒯 \mathcal{T} be the set of underlying tasks and defining the data stream as a sequence of experiences: { e 1 , e 2 , … , e N } \{e_{1},e_{2},...,e_{N}\} . These experiences e n e_{n} are the ‘incremental steps’ of a continual learning problem, in the sense that they are presented one after the other and the network has free access to the data of the current experience but not to the data from other experiences (except possibly to data stored in a memory buffer). In the standard task-based continual learning setting, each experience contains all training data for its corresponding task: e t = 𝒟 t train e_{t}=\mathcal{D}^{\text{train}}_{t} for all t ∈ 𝒯 t\in\mathcal{T} . In the task-free continual learning setting, each data point within every experience can be sampled from any combination of underlying tasks: e n ​ [ i ] ∼ ∑ t ∈ 𝒯 π t n , i ​ 𝒟 t e_{n}[i]\sim\sum_{t\in\mathcal{T}}\pi^{n,i}_{t}\mathcal{D}_{t} (1) whereby e n ​ [ i ] e_{n}[i] is data point i i of experience n n and π t n , i \pi^{n,i}_{t} is the probability that this data point is sampled from 𝒟 t \mathcal{D}_{t} , the data distribution of task t t . In this notation, the schedule is given by { π t n , i } n ∈ ℕ ≤ N , i ∈ ℕ ≤ I n , t ∈ 𝒯 \{\pi^{n,i}_{t}\}_{n\in\mathbb{N}_{\leq N},i\in\mathbb{N}_{\leq I_{n}},t\in\mathcal{T}} , where I n I_{n} denotes the number of data points in experience n n . In this framework for continual learning, the task set 𝒯 \mathcal{T} describes what part of the data change over time (i.e., the non-stationary aspect of the data) and the schedule π \pi describes how it changes over time (i.e., the temporal correlation structure). Finally, we note that this framework can be generalized to allow for a continuous task set (this requires changing the summation in equation 1 to an integral), but as far as we are aware this option has not yet been systematically explored in the literature.

In addition to ‘task-based’ and ‘task-free’, other labels that have been used to describe variants of continual learning are ‘streaming’ and ‘online’. Although the precise definitions of these terms vary, streaming continual learning generally means that only a single training example is presented to the network at a time (i.e., in the above framework, each experience e n e_{n} contains only one data point) ( Hayes et al., 2020 ; Banerjee et al., 2021 ) , and online continual learning typically refers to that the network encounters each training sample only once, also referred to as the ‘single-pass-through-data’ setting ( Aljundi et al., 2019a ; Chen et al., 2020 ) .

### 2.4 Three Continual Learning Scenarios

Another important way in which continual learning problems can differ from each other is described by van de Ven and Tolias (2018) . They distinguished three scenarios that have been widely used in the literature: task-incremental learning (sometimes abbreviated as Task-IL or TIL), domain-incremental learning (Domain-IL or DIL) and class-incremental learning (Class-IL or CIL). Formally, these three scenarios can be distinguished based on whether, at test time, task identity is provided and, if not, whether task identity must be inferred. This means that, in theory, any sequence of tasks could be performed according to all three scenarios. Fig. 3 illustrates what it means for the Split MNIST toy problem to be performed according to each scenario. These three scenarios were initially described for task sequences with clear boundaries (i.e., task-based continual learning), but it has since been pointed out that they also generalize to task-free continual learning ( van de Ven et al., 2022 ) . The key to generalizing these three scenarios is defining them based on how the non-stationary aspect of the data (i.e., the aspect of the data that changes over time, or the ‘task set’) relates to the function or mapping that must be learned by the network.

Informally, with task-incremental learning a network must incrementally learn a set of distinct tasks. The use of ‘distinct tasks’ here indicates that the network is always aware of which task it is presented with. Task identity might, for example, be known because it is explicitly provided, because it is clear from context which task must be performed, or because the inputs from different tasks are easily distinguishable from each other. Thanks to the availability of task identity information, with task-incremental learning it is possible to use networks with task-specific components (e.g., a separate output layer per task), or even to have a completely separate network per task – in which case there is no forgetting at all. Thus, simply preventing catastrophic forgetting is not difficult in this scenario. Instead, the challenge with task-incremental learning is to do better (in terms of a trade-off between performance and resource efficiency) than the naive solution in which there is a separate network per task. To realize this, it is necessary to achieve a positive transfer between tasks by sharing learned representations across tasks. An illustrative example of task-incremental learning is learning to play different musical instruments (e.g., first the piano, then the violin), since it should typically be clear which instrument must be played.

Domain-incremental learning can be described as the structure of the problem to be learned being always the same, but the context or input-distribution changes (e.g., there are domain shifts). In contrast to task-incremental learning, where the network always knows from which task an example is, with domain-incremental learning it is not necessarily clear to which domain a presented example belongs. As a result, in this scenario it is not possible to use networks with ‘domain’-specific components, unless the network also infers to which domain an example belongs (e.g., as done by Heald et al., 2021 ; Verma et al., 2021 ). However, inferring domain identity can be challenging and is not necessarily the most effective way to solve a domain-incremental learning problem. Illustrative examples of domain-incremental learning are learning to drive in various weather conditions or learning to classify objects under different lighting conditions (e.g., indoors versus outdoors).

Finally, class-incremental learning is the problem of incrementally learning to distinguish between an increasing number of objects or classes. In the literature, this scenario is often implemented in a ‘task-based manner’, meaning that there is a sequence of classification-based ‘tasks’, with each task containing a distinct set of classes, and the goal is to learn to discriminate between the classes of all tasks. Let us illustrate this with an example. Imagine that a network is first presented with a task consisting of pianos and guitars, and later with one containing saxophones and violins. In the class-incremental learning scenario, after seeing both tasks, the network is expected to be able to discriminate between all four musical instruments (i.e., it should have learned a four-way classifier). On the other hand, if this same task sequence were performed according to the task-incremental learning scenario, the network would only be expected to be able to distinguish between instruments in the same task, but not between those from different tasks. In this task-based setting, class-incremental learning can be decomposed into solving each individual task (or prediction within the task) and inference of task identity (or prediction across tasks) ( Soutif-Cormerais et al., 2021 ; Guo et al., 2023 ) . Especially inferring task identity, which has links to out-of-distribution detection ( Henning et al., 2021 ; Kim et al., 2022 ) , is often found to be particularly difficult. Beyond the task-based setting, this can be generalized by saying that a challenging aspect of class-incremental learning is learning to discriminate between classes that are not observed together.

#### Clarifying note.

It is useful to point out that the distinction between task-, domain- and class-incremental learning is orthogonal to the distinction between task-based and task-free continual learning, in the sense that each of the three scenarios can occur in both a task-based and a task-free continual learning setting. In the literature, there is sometimes confusion about the difference between ‘task-based continual learning’ and ‘task-incremental learning’. We therefore clarify that task-based continual learning refers to that training data change over time in a task-by-task manner (and with clear boundaries between tasks), while task-incremental learning signals that task identity is known to the network at test time.

### 2.5 Evaluation

With the rapid increase in interest in continual learning, numerous approaches have been proposed for evaluating and comparing different continual learning methods (e.g., Lopez-Paz and Ranzato, 2017 ; Díaz-Rodríguez et al., 2018 ; New et al., 2022 ; De Lange et al., 2023 ; Kudithipudi et al., 2023 ). Typically, metrics for continual learning cover one of three areas: i) performance, ii) diagnostic analysis, and iii) resource efficiency.

With regards to evaluating performance in a continual learning setting, two important questions are: (a) how to evaluate it, and (b) when to evaluate it. Regarding the first question, continual learning performance is typically evaluated using the average of a certain performance metric (e.g., test accuracy in case of classification) over a family of tasks. Usually this family of tasks consists of all tasks trained on so far, or sometimes all tasks that will be trained on, and o the performance on all evaluated tasks is weighted equally. Regarding the question when to evaluate performance, one approach is to only do so at the end of training on all tasks. Another common approach is to evaluate performance periodically throughout training by interleaving training and evaluation blocks. Performance can for example be evaluated after finishing training on each task, or after a fixed number of training steps.

A disadvantage of comparing continual learning methods only based on their average performance is that this does not provide much insight into how each method addresses continual learning. For example, a plastic model that achieves 0% accuracy on the first task and 100% accuracy on the second task, has the same average performance as a completely rigid model with 100% accuracy on the first task and 0% accuracy on the second. To provide greater insight into the dynamics of continual learning, there are several diagnostic metrics. One such diagnostic metric is learning accuracy. This measures well a model can learn from the current task, which, when compared to a baseline model, can provide a measure of plasticity. Another popular diagnostic metric is backward transfer, which measures how the performance on previous tasks changes when training on new ones. This metric provides insight into the degree of catastrophic forgetting that occurs and the stability of the model. Another diagnostic metric is forward transfer, which quantifies how much training on previous tasks improves the performance of a model on, or its ability to learn, future tasks.

A third set of metrics evaluates the resource efficiency of continual learning methods. One way to quantify resource efficiency is through the computational overhead and energy consumption of a method. The number of operations and the complexity are important factors when deploying continual learning methods to real-world problems, especially when targeting edge applications. It is important to note that although computational complexity is often only computed for the training phase, a portion of continual learning methods introduce additional complexity during inference, which can be measured as well and is not always identical to the training costs. Another key aspect of resource efficiency is sustainability, which refers to how quickly a model grows in terms of parameters, or in terms of memory for storing information about prior experiences (e.g., data samples, model copies).

## 3 Continual Learning Approaches

In this section we focus on approaches that have been proposed to address the continual learning problem. We do not provide an extensive review of individual continual learning methods (for this, we refer to Belouadah et al., 2021 ; De Lange et al., 2022 ; Masana et al., 2023 ; Wang et al., 2023b ), but rather we discuss the main computational strategies that underlie these methods. Individual continual learning methods often combine multiple of these strategies.

### 3.1 Replay

Perhaps the most widely used approach for continual learning is replay. The idea behind replay, which is also referred to as rehearsal, is to approximate interleaved learning by complementing the training data of the current task or experience with data that are representative of previous ones (Fig. 4 a). Replay has close links to neuroscience. In the brain, the re-occurence of neuronal activity patterns that represent previous experiences is believed to be important for the stabilization and consolidation of new memories ( Wilson and McNaughton, 1994 ; Rasch and Born, 2007 ) .

In the deep learning literature, a common way to add replay to a neural network is to store previously seen data in a memory buffer and revisit them later on. Such ‘experience replay’ can substantially speed up training in reinforcement learning ( Lin, 1992 ; Mnih et al., 2015 ) , and it has proven to be an effective way to reduce catastrophic forgetting in continual learning ( Robins, 1995 ; Rolnick et al., 2019 ; Chaudhry et al., 2019b ; Buzzega et al., 2020 ) . A common assumption in benchmarks for continual learning is that only a limited amount of data can be stored (but see Prabhu et al., 2023 ; Verwimp et al., 2023 for recent perspectives on this assumption), and a research question that has received a lot of attention is how to best pick the samples to store in the memory buffer ( Rebuffi et al., 2017 ; Chaudhry et al., 2019b ; Aljundi et al., 2019c ; Mundt et al., 2023 ) .

Instead of explicitly storing past observations, it is also possible to learn a generative model, which can then be used to generate the data to be replayed ( Mocanu et al., 2016 ; Shin et al., 2017 ; Wu et al., 2018 ; Rao et al., 2019 ; Cong et al., 2020 ; Khan et al., 2023 ) . An issue with such ‘generative replay’ is that it can be difficult to train generative models of decent quality, especially in an incremental setting or when data are complex ( Aljundi et al., 2019a ; Lesort et al., 2019a ) . This issue can sometimes be alleviated by replaying latent features instead of raw inputs ( Liu et al., 2020 ; Pellegrini et al., 2020 ; Ostapenko et al., 2022 ) , but this ‘internal replay’ approach needs some form of pretraining to work well.

When replay is used to train a deep neural network, the loss on the replayed data ( ℓ replay \ell_{\text{replay}} ) is usually added to the loss on the current data ( ℓ current \ell_{\text{current}} ), possibly with some weighting applied, and the objective is to optimize the combined loss: ℓ total ​ ( 𝜽 ) = ℓ current ​ ( 𝜽 ) + ℓ replay ​ ( 𝜽 ) \ell_{\text{total}}(\boldsymbol{\theta})=\ell_{\text{current}}(\boldsymbol{\theta})+\ell_{\text{replay}}(\boldsymbol{\theta}) (2) with 𝜽 \boldsymbol{\theta} the parameters of the network that can be updated during training.

An alternative way to use the loss on the replayed data is to construct one or more inequality constraints that should be respected when optimizing the loss on the current data ( Lopez-Paz and Ranzato, 2017 ; Chaudhry et al., 2019a ) . Although this strategy, which is referred to as ‘gradient episodic memory’, is sometimes categorized in the literature under replay, we consider it an optimization-based approach and discuss it in subsection 3.4 .

Especially for large and complex continual learning problems, replay seems to play an important and perhaps necessary role. However, as replay involves constantly retraining on past data, an important concern with this approach is the potentially high computational cost. Luckily, there is evidence that it is not necessary to fully (re)train on all past tasks whenever a new task is learned. One reason is that learning something new is typically more demanding than preventing its forgetting once it has been learned, which explains why it can be sufficient to replay only relatively small amounts of data ( van de Ven et al., 2020 ) . In the cognitive science literature, it has further been suggested that it might only be needed to replay old data that are similar to the new data ( McClelland et al., 2020 ) . The intuition for this is that interference between unrelated items should be small anyway (for example because such items are stored in separate parts of the network). This idea has inspired a series of continual learning studies asking how to adaptively select which data to replay given the currently observed data ( Riemer et al., 2019 ; Aljundi et al., 2019a ; Klasson et al., 2023 ; Krawczyk and Gepperth, 2023 ) . Other open questions with regards to replay are how to store and compress data, in what format to replay data (e.g., raw data or intermediate features), and how to best integrate replay with other methods.

### 3.2 Parameter Regularization

Another popular approach for continual learning is parameter regularization. When a new task is learned, parameter regularization discourages large changes to parameters of the network that are thought to be important for previous tasks (Fig. 4 b). From a neuroscience perspective, this approach can be linked to metaplasticity ( Abraham, 2008 ) , as it can be interpreted as equipping the network parameters with an internal state that modulates their level of plasticity ( Zenke et al., 2017 ) . Another motivation for parameter regularization comes from a Bayesian perspective, as instances of this approach can often be expressed or interpreted as performing sequential approximate Bayesian inference on the parameters of a neural network ( Kirkpatrick et al., 2017 ; Nguyen et al., 2018 ; Farquhar and Gal, 2019 ) .

We define parameter regularization as adding a regularization term to the loss function to penalize changes to the network’s parameters 𝜽 \boldsymbol{\theta} , whereby the applied penalty is usually weighted by an estimate of how important parameters are for previously learned tasks (e.g., Kirkpatrick et al., 2017 ; Zenke et al., 2017 ; Aljundi et al., 2018 ; Schwarz et al., 2018 ; Ritter et al., 2018 ): ℓ total ​ ( 𝜽 ) = ℓ current ​ ( 𝜽 ) + ‖ 𝜽 − 𝜽 ∗ ‖ Σ \ell_{\text{total}}(\boldsymbol{\theta})=\ell_{\text{current}}(\boldsymbol{\theta})+\left\lVert\boldsymbol{\theta}-\boldsymbol{\theta}^{*}\right\rVert_{\Sigma} (3) with 𝜽 ∗ \boldsymbol{\theta}^{*} the value of the parameters relative to which changes are penalized (often this is the value of 𝜽 \boldsymbol{\theta} at the end of the previous task), Σ \Sigma an estimate of how important the parameters are for past tasks and ‖ . ‖ Σ \left\lVert.\right\rVert_{\Sigma} a weighted norm. The most common choice is a weighted L 2 L^{2} -norm, in which case the regularization term becomes 1 2 ​ ( 𝜽 − 𝜽 ∗ ) T ​ Σ ​ ( 𝜽 − 𝜽 ∗ ) \frac{1}{2}\left(\boldsymbol{\theta}-\boldsymbol{\theta}^{*}\right)^{T}\Sigma\left(\boldsymbol{\theta}-\boldsymbol{\theta}^{*}\right) . We note that it is also possible to use estimates of the importance of parameters for past tasks in other ways, for example to reduce the learning rate for relatively important parameters (e.g., Özgün et al., 2020 ) or to perform gradient projection during optimization (e.g., Kao et al., 2021 ). Although in the literature these approaches are sometimes categorized under parameter regularization, we consider them optimization-based approaches and discuss them in subsection 3.4 .

A pivotal aspect of parameter regularization is estimating the importance of the network’s parameters for past tasks. An often-used method is to leverage the Fisher Information matrix ( Kirkpatrick et al., 2017 ) , which, under certain assumptions, indicates how a small change to the parameters would impact the loss. The Fisher Information is typically approximated with a diagonal matrix, thus assuming independence among all parameters. However, this assumption can be relaxed, for example by instead using a Kronecker-factored approximation ( Martens and Grosse, 2015 ; Ritter et al., 2018 ; Kao et al., 2021 ) . An important disadvantage of the Fisher Information is that it can be costly to compute. Several other parameter regularization methods instead estimate parameter importance online throughout training, which often incurs substantially lower computational costs ( Zenke et al., 2017 ; Aljundi et al., 2018 ) .

Although parameter regularization methods have shown success in task- and domain-incremental learning problems, they often struggle to learn inter-task boundaries in class-incremental learning scenarios ( Lesort et al., 2019b ; van de Ven et al., 2022 ; Kessler et al., 2023 ) .

### 3.3 Functional Regularization

An inherent difficulty with parameter regularization is that correctly estimating the importance of parameters for past tasks is very hard, which is due to the complex relation between the behaviour of a deep neural network and its parameters. Instead of operating in the parameter space, a more effective approach might be applying regularization in the function space of a neural network ( Benjamin et al., 2019 ; Pan et al., 2020 ; Titsias et al., 2020 ) . The goal of such functional regularization is to prevent large changes to a network’s input-output mapping f 𝜽 f_{\boldsymbol{\theta}} at a set of specific inputs, which are termed ‘anchor points’ (Fig. 4 c). Similar to parameter regularization, functional regularization can be expressed as adding a penalty term to the loss function: ℓ total ​ ( 𝜽 ) = ℓ current ​ ( 𝜽 ) + ⟨ f 𝜽 , f 𝜽 ∗ ⟩ 𝒜 \ell_{\text{total}}(\boldsymbol{\theta})=\ell_{\text{current}}(\boldsymbol{\theta})+\left<f_{\boldsymbol{\theta}},f_{\boldsymbol{\theta}^{*}}\right>_{\mathcal{A}} (4) with f 𝜽 ∗ f_{\boldsymbol{\theta}^{*}} the input-output mapping relative to which changes are penalized (often this is the input-output mapping of the network at the end of the previous task) and 𝒜 \mathcal{A} the set of anchor points where the divergence between f 𝜽 f_{\boldsymbol{\theta}} and f 𝜽 ∗ f_{\boldsymbol{\theta}^{*}} is evaluated.

There are different ways in which the divergence between f 𝜽 f_{\boldsymbol{\theta}} and f 𝜽 ∗ f_{\boldsymbol{\theta}^{*}} can be measured. For classification-based problems, following Li and Hoiem (2017) , a popular choice is to use the knowledge distillation loss proposed by Hinton et al. (2015) , which involves the cross entropy between temperature-scaled logits of both networks. However, the divergence between f 𝜽 f_{\boldsymbol{\theta}} and f 𝜽 ∗ f_{\boldsymbol{\theta}^{*}} does not need to be measured at the output level. In recent years, functional regularization is increasingly applied at various levels of the representation of neural networks, in which case it is also called feature distillation ( Heo et al., 2019 ; Douillard et al., 2020 ; Gomez-Villa et al., 2022 ; Roy et al., 2023 ) .

Another important aspect of functional regularization is the selection of anchor points. For relatively simple problems, Robins (1995) demonstrated that functional regularization with random patterns as anchor points, which he called ‘pseudorehearsal’, can already work reasonably well. However, for more complex problems, it is important that the set of anchor points is representative of the inputs from previous tasks. A naive solution would be to use all inputs that have been seen so far as anchor points, but this requires storing those inputs and functional regularization with a large number of anchor points can incur high computational costs. An option that does not involve storing past samples is using the currently observed inputs as anchor points ( Li and Hoiem, 2017 ) . This approach, which is known as ‘learning without forgetting’, tends to work well when the inputs from different tasks have similar structure (e.g., as is the case with tasks that all consist of natural images), but in general there is no guarantee that the current inputs are suitable anchor points for previous tasks. Another option is to use as anchor points a small number of strategically selected inputs from previous tasks that represent those tasks well. One way to select such representative inputs is by formulating neural networks as Gaussian Processes ( Khan et al., 2019 ) , as this allows for summarizing the input distributions of previous tasks with inducing points ( Titsias et al., 2020 ) or memorable inputs ( Pan et al., 2020 ) . How to optimally select the anchor points for functional regularization is still largely an open question.

Functional regularization is closely related to replay. In fact, functional regularization can be interpreted as a form of replay, whereby the replayed data consist of the anchor points labelled with the predictions for those points made by (a previous version of) the network itself. The key difference between both approaches is that with replay inputs and targets of past tasks are stored externally to the network (e.g., in a memory buffer or in the form of a separate generative model), while with functional regularization only inputs of past tasks are stored externally. With functional regularization, the input-output mapping of past tasks is therefore only stored internally in the network itself (or in its copies), while with replay at least part of this mapping is stored externally. However, in the continual learning literature, the distinction between replay and functional regularization is sometimes blurred. For example, with generative replay there is often only a generative model for the input distribution, and the generated inputs that are replayed are labelled based on predictions made for them by a previous version of the network (e.g., Shin et al., 2017 ). Consequently, despite its name, such generative replay is actually a form of functional regularization. Moreover, the replay of stored data from a memory buffer has also been combined with distillation (e.g., Buzzega et al., 2020 ; Boschini et al., 2023 ), making those instances a form of functional regularization as well.

### 3.4 Optimization-based Approaches

The three approaches discussed so far – replay, parameter regularization and functional regularization – operate by making changes to the loss function that is optimized (as shown by equations 2 - 4 ). An alternative approach to continual learning is to change how the loss function is optimized (Fig. 4 d). The standard optimization routines that are used in deep learning, such as stochastic gradient descent (SGD) and its variants (e.g., AdaGrad, Duchi et al., 2011 ; Adam, Kingma and Ba, 2014 ), have been developed for stationary settings. In non-stationary settings, there are typically no guarantees for their behavior, yet these standard optimization routines are the default choice in most work on continual learning. However, in the last few years there has been an increasing attention in the continual learning literature for the role of optimization, and there have been several attempts to develop novel optimization routines specific for continual learning. It has even been argued that an wholistic solution for continual learning must consist of both changes to the loss function and changes to how that loss function is optimized ( Hess et al., 2023 ) .

Already about six years ago it was empirically found that the type of optimizer (e.g., plain SGD, AdaGrad or Adam) can have a large effect on continual learning performance ( Hsu et al., 2018 ) . Later work explored a wider range of factors that influence optimization (e.g., learning rate, batch size) and concluded that the best optimization routines for continual learning are the ones that tend to find wider or flatter minima ( Mirzadeh et al., 2020 ) . This can be explained because with a wider minimum, larger changes to the parameters are needed to ‘get out of the minimum’. This insight has motivated several continual learning works to modify optimization routines to encourage finding such wider minima ( Deng et al., 2021 ; Yang et al., 2023 ; Tran Tung et al., 2023 ) .

A popular way to control how a given loss function is optimized is by using adaptive learning rates. For example, one strategy might be to reduce the learning rate for either parameters or units that are estimated to be important for past tasks ( Ahn et al., 2019 ; Jung et al., 2020 ; Özgün et al., 2020 ; Paik et al., 2020 ; Laborieux et al., 2021 ; Soures et al., 2021 ; Malviya et al., 2022 ) . This approach is related to parameter regularization, but it is different because the use of adaptive learning rates does not change the loss function, while parameter regularization does. Similar to parameter regularization, the use of adaptive learning rates can be related to the neuroscience concept of metaplasticity ( Abraham, 2008 ) . A different metaplasticity-inspired way to control the optimization trajectory is through probabilistic parameter updates ( Zohora et al., 2020 ; Schug et al., 2021 ) rather than adjusting the learning rate.

Another optimization-based tool that has been explored in continual learning is gradient projection. With gradient projection, rather than basing parameter updates on the original gradient g = ∇ 𝜽 ℓ ​ ( 𝜽 ) g=\nabla_{\boldsymbol{\theta}}\ell\left(\boldsymbol{\theta}\right) , they are based on a projected version g ¯ \bar{g} of that gradient. A first popular approach is ‘orthogonal gradient projection’ ( Zeng et al., 2019 ; Farajtabar et al., 2020 ; Saha et al., 2021 ) . To restrict parameter updates to directions that do not interfere with the performance on old tasks, this approach projects gradients to the subspace orthogonal to the gradients of old tasks. A less restrictive version of this approach instead projects gradients using the inverse of the Fisher Information as projector matrix ( Kao et al., 2021 ) . Another gradient projection-based approach is ‘gradient episodic memory’ ( Lopez-Paz and Ranzato, 2017 ; Chaudhry et al., 2019a ) . The projection mechanism of this approach is derived from a constrained optimization problem which aims to optimize the loss on a new task without increasing the loss on old tasks.

Another method that falls into the category of optimization-based techniques is based on the biological process of synaptic consolidation, which consolidates information within an individual synapse over multiple timescales ( Sossin, 2008 ; Morris, 2003 ) . Such synaptic consolidation can be modelled with a complex synaptic model consisting of a rapidly adapting weight 𝜽 f \boldsymbol{\theta}_{f} and a slowly evolving weight 𝜽 s \boldsymbol{\theta}_{s} . The rapidly adapting weight, 𝜽 f \boldsymbol{\theta}_{f} , is driven by a combination of the loss function and a regularization-like function that attempts to prevent divergence from 𝜽 s \boldsymbol{\theta}_{s} . The main distinction between parameter regularization and this approach lies in the dynamic nature of 𝜽 s \boldsymbol{\theta}_{s} , which slowly evolves to consolidate the information learned by 𝜽 f \boldsymbol{\theta}_{f} . Several studies have used this approach to reduce catastrophic forgetting in continual learning ( Zenke et al., 2015 ; Leimer et al., 2019 ; Soures et al., 2021 ) .

### 3.5 Context-dependent Processing

Another popular approach for continual learning is context-dependent processing. The idea behind this approach is to use certain parts of the network only for specific tasks or contexts, in order to reduce the interference that can occur between them (Fig. 4 e). It is worth noting that when taken to the extreme, this approach corresponds to having a completely separate network per task or context. In this case, there would be no interference or forgetting at all, but there would also no longer be any possibility of positive transfer between tasks or contexts. It could therefore be argued that continual learning methods should aim to only segregate information that is unrelated to each other (as there is likely no positive transfer to be gained between them anyway), while storing related information in the same part of the network.

A widespread example of context-dependent processing in continual learning is the use of a separate linear output layer for each task to be learned. The use of such a ‘multi-headed output layer’ has become the default setup for task-incremental learning experiments. But there are other ways in which context-dependent processing is used as well.

One other way to induce context-dependent processing in a neural network is by gating either its units or its parameters in a different way for each task that must be learned. It is possible to specify such task-specific gates a priori and randomly ( Masse et al., 2018 ) , but it is also possible to learn them, for example using gradient descent ( Serra et al., 2018 ) , Hebbian plasticity ( Flesch et al., 2023 ) or evolutionary algorithms ( Ellefsen et al., 2015 ; Fernando et al., 2017 ) . The use of task- or context-specific gates has been linked to the concept of neuromodulation in the brain, which refers to chemical signals that locally modify the way inputs are processed ( Marder and Thirumalai, 2002 ) .

Another way to realize context-dependent processing is by periodically adding new components, and thus dynamically expanding the network ( Zhou et al., 2012 ; Terekhov et al., 2015 ; Draelos et al., 2017 ) . Expanding the network can be based on when extra capacity is needed ( Hung et al., 2019 ; Mitchell et al., 2023 ) , but in many cases new components are simply added whenever a new task must be learned ( Rusu et al., 2016 ; Yoon et al., 2018 ) . Often, this approach is combined with freezing parts of the network after a task has been learned. To control the growth of the network, many model expansion methods make use of sparse training (e.g., prompt learning or the use of adaptors; Wang et al., 2022b ; Gao et al., 2023 ) or pruning techniques ( Golkar et al., 2019 ; Pandit and Kudithipudi, 2020 ; Yan et al., 2021 ) . The approach of dynamically expanding the network can be linked to the process of neurogenesis, which refers to the addition of neurons to certain brain regions throughout life ( Aimone et al., 2014 ) . It has indeed been hypothesized that neurogenesis plays a role in the brain’s ability to mitigate catastrophic forgetting ( Wiskott et al., 2006 ) .

An important assumption that often underlies the use of context-dependent processing in continual learning is that the context (or task) is always clear to the network. As a result of this, when used by itself, this approach is limited to task-incremental learning type of problems. To be applicable to domain- or class-incremental learning problems, context-dependent processing must be combined with an algorithm for context identification (e.g., as done by Aljundi et al., 2017 ; von Oswald et al., 2020 ; Wortsman et al., 2020 ; Henning et al., 2021 ; Verma et al., 2021 ; Heald et al., 2021 ). In this regard it is important to realize that context identification itself is a class-incremental learning problem as well, as it consists of distinguishing categories (in this case ‘contexts’) that are not observed together. Inferring context information has indeed proven to be a difficult problem, and presents a promising avenue for future research.

### 3.6 Template-based Classification

An approach to class-incremental learning that is often used in continual learning is template-based classification. With this approach, a ‘class template’ is learned for every class, and classification is performed based on which class template is closest or most suitable for the sample to be classified (Fig. 4 f). In this description, a class template can be thought of as a representation or a model of that particular class. In the context of class-incremental learning, an important advantage of template-based classification is that it avoids the need to make comparisons between classes during training . Standard softmax-based classifiers have to learn decision boundaries between all classes during their training, but this is challenging with class-incremental learning because not all classes are observed together. Template-based classifiers instead only have to learn a template per class during their training, and the comparison between classes is deferred to test time. Importantly, while the original problem is a class-incremental learning problem, learning these class templates is a task-incremental learning problem, whereby each ‘task’ is to learn a template for a specific class. This means that with this approach it is possible to use ‘template-specific components’, or other context-dependent processing approaches.

A popular way to implement template-based classification is to use ‘prototypes’ as class templates. The use of such prototypes has roots in cognitive science, where it is an influential model for how humans make categorization decisions ( Nosofsky, 1986 ) . In deep learning, a prototype is often taken to be the mean vector of examples from a class in an embedding space defined by a neural network ( Snell et al., 2017 ; Yang et al., 2018 ) . Classification is then done by putting samples through the embedding network and assigning them to the class of the prototype they are closest to. When a suitable pretrained embedding network is available and it is kept frozen throughout training, storing raw data is not needed and prototype-based classification only requires storing a single prototype per class (e.g., Hayes and Kanan, 2020 ). If the embedding network requires updates, for example to better distinguish new classes, one option is to store a few well-chosen examples per class to update the prototypes following changes to the embedding network ( Rebuffi et al., 2017 ; De Lange and Tuytelaars, 2021 ) . Alternatively, prototype drift can be addressed without storing past examples by estimating and correcting drift based on the observed drift for data from the current task ( Yu et al., 2020 ; Wei et al., 2021 ) .

Another example of template-based classification that has shown promise for class-incremental learning is generative classification ( van de Ven et al., 2021 ; Banayeeanzade et al., 2021 ) . With generative classification, the class templates that are learned are generative models, and their suitability for a sample to be classified is computed as the sample’s likelihood under each of the generative models. An advantage of generative classification is that it does not require storing samples, but a drawback is that learning decent generative models can be challenging, especially in the case of limited training data or complex distributions. Moreover, inference (i.e., making classification decisions) can be computationally costly as it requires computing likelihoods under the generative model of each class. Several more lightweight and efficient alternatives for generative classification have been proposed. One option is to train an energy-based model and compute energy values per class or context instead of likelihoods ( Li et al., 2022 ; Joseph et al., 2022 ) . Another option is to train class-specific models to replicate the outputs of a frozen random network and perform classification based on each model’s prediction error ( Zając et al., 2024 ) .

## 4 Continual Learning in Deep Learning versus in Cognitive Science

So far, this book chapter has mostly reviewed the deep learning literature on continual learning. In this section, we briefly ask how continual learning is studied in the cognitive science literature. When it comes to continual learning, the goals of deep learning and cognitive science are different, but clearly related. Deep learning aims to engineer artificial neural networks so that they can learn continually, while cognitive science is concerned with understanding how this already present skill is implemented by the brain.

One central aspect of continual learning that is widely studied in cognitive science is forgetting. Forgetting refers to the loss or decay of previously acquired information and can result from various factors in biological organisms ( Hardt et al., 2013 ; Davis and Zhong, 2017 ) . There exist passive mechanisms, such as decay over time through natural aging and transient forgetting in which forgetting is often reversible, and there are active mechanisms of forgetting, such as intentional forgetting, retrieval-induced forgetting and interference-based forgetting. An example of interference-based forgetting is retroactive interference, where acquisition of new memories during consolidation leads to forgetting of old ones ( Wixted, 2004 ; Alves and Bueno, 2017 ) , which is probably most akin to the forgetting that happens when deep neural networks are continually trained. Studies into how biological systems mitigate this retroactive interference have already inspired many approaches for continual learning with deep neural networks (e.g., Kaplanis et al., 2018 ; Masse et al., 2018 ; Tadros et al., 2022 ; Kudithipudi et al., 2022 ; Arani et al., 2022 ; Wang et al., 2023a ; Jeeveswaran et al., 2023 ), and it seems likely that deep learning can still gain further benefits from the rich characterization and understanding of forgetting that has been accrued in the cognitive science literature. For example, something not often acknowledged in deep learning is that with bounded resources, forgetting could be beneficial or even necessary. Indeed, some deep learning applications might benefit from controlled or intentional forgetting, similar to how forgetting is thought to be important for the brain’s ability to continue learning new information (e.g., Nørby, 2015 ; Richards and Frankland, 2017 ; Bjork and Bjork, 2019 ).

While forgetting is well studied in cognitive science, other aspects of continual learning (cf. subsection 2.2 ) appear to receive less attention; or at least the way in which these other aspects are studied in deep learning is different and mostly unconnected from the way they are studied in cognitive science. However, there are some efforts to bridge this gap between both fields. In particular, Flesch et al. (2018) designed several experiments to compare the continual learning performance of humans and artificial neural networks. They demonstrate that, unlike deep learning models that suffer from blocked training, humans actually perform better with blocked training (and worse with interleaved training). In another work, Flesch et al. (2023) show how, through the incorporation of different mechanisms, the learning dynamics of artificial neural networks can be made to more closely match those observed in humans. Establishing more such connections between cognitive science and deep learning in the context of continual learning, especially if they go beyond just forgetting, might substantially benefit both fields.

## 5 Conclusion

In this book chapter we have reviewed the challenges of continual learning with deep neural networks, which is a topic of great interest in the artificial intelligence field. The current inept ability of deep learning models to continually learn from a stream of incoming data is a major obstacle to the development of truly intelligent artificial agents that can accumulate knowledge by incrementally learning from their experiences.

Catastrophic forgetting is the most well-known issue in continual learning. However, in addition to overcoming catastrophic forgetting, a complete solution to continual learning requires the development of models capable of quickly adapting to new situations, exploiting similarities between tasks, operating in a task agnostic manner, being tolerant to noise, and using resources in an efficient and sustainable manner. Continual learning is thus not a unitary problem, and this is further illustrated by the observation that the main challenges of continual learning can differ substantially depending on how exactly the problem is set up. To fully capture the gradations and complexities of continual learning, a variety of settings and benchmarks needs to be considered. Among these are task-, domain- and class-incremental learning, as well as task-based and task-free continual learning. Similarly, comprehensively evaluating continual learning approaches cannot be done using a single metric; in this book chapter we have discussed a variety of continual learning metrics covering performance, diagnostics and resource efficiency.

We have further reviewed six computational approaches for continual learning. Replay, parameter regularization and functional regularization operate by making changes to the loss function, while optimization-based approaches change the way in which a given loss function is optimized. Context-dependent processing distributes computations across the network based on contextual or task-specific information, and template-based classification enables distinguishing objects or categories that are not observed together without having to directly learn discriminative boundaries.

As deep learning navigates the intricate challenges posed by non-stationary environments and catastrophic forgetting, it becomes evident that continual learning is not just a technical necessity, but a philosophical shift in the approach to artificial intelligence. Approaching this from an interdisciplinary collaboration, drawing inspiration from neuroscience, cognitive science, and psychology to imbue continual learning into artificial systems, seems to hold promise. Similarly, but in the reverse direction, insights gained in the deep learning field while doing so can help to unravel the computational principles that underlie the cognitive skill of continual learning in the brain.

### Acknowledgements

This effort is partially supported by the NSF EFRI BRAID Award #2317706 and the NSF PARTNER AI Institute NAIAD Award #2332744, as well as by funding from the European Union under Horizon Europe (Marie Skłodowska-Curie fellowship, grant agreement No. 101067759).

## References

Abraham (2008) Abraham, W. C. (2008), ‘Metaplasticity: tuning synapses and networks for plasticity’, Nature Reviews Neuroscience 9 (5), 387–399.

Ahn et al. (2019) Ahn, H., Cha, S., Lee, D. and Moon, T. (2019), Uncertainty-based continual learning with adaptive regularization, in ‘Advances in Neural Information Processing Systems’, Vol. 32.

Aimone et al. (2014) Aimone, J. B., Li, Y., Lee, S. W., Clemenson, G. D., Deng, W. and Gage, F. H. (2014), ‘Regulation and function of adult neurogenesis: from genes to cognition’, Physiological Reviews 94 (4), 991–1026.

Aljundi et al. (2018) Aljundi, R., Babiloni, F., Elhoseiny, M., Rohrbach, M. and Tuytelaars, T. (2018), Memory aware synapses: Learning what (not) to forget, in ‘Proceedings of the European Conference on Computer Vision (ECCV)’, pp. 139–154.

Aljundi et al. (2019a) Aljundi, R., Caccia, L., Belilovsky, E., Caccia, M., Lin, M., Charlin, L. and Tuytelaars, T. (2019a), Online continual learning with maximally interfered retrieval, in ‘Advances in Neural Information Processing Systems’, Vol. 32.

Aljundi et al. (2017) Aljundi, R., Chakravarty, P. and Tuytelaars, T. (2017), Expert gate: Lifelong learning with a network of experts, in ‘Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition’, pp. 3366–3375.

Aljundi et al. (2019b) Aljundi, R., Kelchtermans, K. and Tuytelaars, T. (2019b), Task-free continual learning, in ‘Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition’, pp. 11254–11263.

Aljundi et al. (2019c) Aljundi, R., Lin, M., Goujaud, B. and Bengio, Y. (2019c), Gradient based sample selection for online continual learning, in ‘Advances in Neural Information Processing Systems’, Vol. 32.

Alves and Bueno (2017) Alves, M. V. C. and Bueno, O. F. A. (2017), ‘Retroactive interference: forgetting as an interruption of memory consolidation’, Trends in Psychology 25 , 1043–1054.

Arani et al. (2022) Arani, E., Sarfraz, F. and Zonooz, B. (2022), Learning fast, learning slow: A general continual learning method based on complementary learning system, in ‘International Conference on Learning Representations’. https://openreview.net/forum?id=uxxFrDwrE7Y

Banayeeanzade et al. (2021) Banayeeanzade, M., Mirzaiezadeh, R., Hasani, H. and Soleymani, M. (2021), Generative vs. discriminative: Rethinking the meta-continual learning, in ‘Advances in Neural Information Processing Systems’, Vol. 34, pp. 21592–21604.

Banerjee et al. (2021) Banerjee, S., Verma, V. K., Parag, T., Singh, M. and Namboodiri, V. P. (2021), ‘Class incremental online streaming learning’, Preprint at https://arxiv.org/abs/2110.10741.

Belouadah et al. (2021) Belouadah, E., Popescu, A. and Kanellos, I. (2021), ‘A comprehensive study of class incremental learning algorithms for visual tasks’, Neural Networks 135 , 38–54.

Benjamin et al. (2019) Benjamin, A., Rolnick, D. and Kording, K. (2019), Measuring and regularizing networks in function space, in ‘International Conference on Learning Representations’. https://openreview.net/forum?id=SkMwpiR9Y7

Bjork and Bjork (2019) Bjork, R. A. and Bjork, E. L. (2019), ‘Forgetting as the friend of learning: Implications for teaching and self-regulated learning’, Advances in Physiology Education 43 (2), 164–167.

Boschini et al. (2023) Boschini, M., Bonicelli, L., Buzzega, P., Porrello, A. and Calderara, S. (2023), ‘Class-incremental continual learning into the eXtended DER-Verse’, IEEE Transactions on Pattern Analysis and Machine Intelligence 45 (5), 5497–5512.

Bubeck et al. (2023) Bubeck, S., Chandrasekaran, V., Eldan, R., Gehrke, J., Horvitz, E., Kamar, E., Lee, P., Lee, Y. T., Li, Y., Lundberg, S. et al. (2023), ‘Sparks of artificial general intelligence: Early experiments with GPT-4’, Preprint at https://arxiv.org/abs/2303.12712.

Buzzega et al. (2020) Buzzega, P., Boschini, M., Porrello, A., Abati, D. and Calderara, S. (2020), Dark experience for general continual learning: a strong, simple baseline, in ‘Advances in Neural Information Processing Systems’, Vol. 33, pp. 15920–15930.

Chaudhry et al. (2019a) Chaudhry, A., Ranzato, M., Rohrbach, M. and Elhoseiny, M. (2019a), Efficient lifelong learning with A-GEM, in ‘International Conference on Learning Representations’. https://openreview.net/forum?id=Hkf2_sC5FX

Chaudhry et al. (2019b) Chaudhry, A., Rohrbach, M., Elhoseiny, M., Ajanthan, T., Dokania, P. K., Torr, P. H. and Ranzato, M. (2019b), ‘On tiny episodic memories in continual learning’, Preprint at https://arxiv.org/abs/1902.10486.

Chen et al. (2020) Chen, H.-J., Cheng, A.-C., Juan, D.-C., Wei, W. and Sun, M. (2020), Mitigating forgetting in online continual learning via instance-aware parameterization, in ‘Advances in Neural Information Processing Systems’, Vol. 33, pp. 17466–17477.

Cong et al. (2020) Cong, Y., Zhao, M., Li, J., Wang, S. and Carin, L. (2020), GAN memory with no forgetting, in ‘Advances in Neural Information Processing Systems’, Vol. 33, pp. 16481–16494.

Davis and Zhong (2017) Davis, R. L. and Zhong, Y. (2017), ‘The biology of forgetting—a perspective’, Neuron 95 (3), 490–503.

De Lange et al. (2022) De Lange, M., Aljundi, R., Masana, M., Parisot, S., Jia, X., Leonardis, A., Slabaugh, G. and Tuytelaars, T. (2022), ‘A continual learning survey: Defying forgetting in classification tasks’, IEEE Transactions on Pattern Analysis and Machine Intelligence 44 (7), 3366–3385.

De Lange and Tuytelaars (2021) De Lange, M. and Tuytelaars, T. (2021), Continual prototype evolution: Learning online from non-stationary data streams, in ‘Proceedings of the IEEE/CVF International Conference on Computer Vision’, pp. 8250–8259.

De Lange et al. (2023) De Lange, M., van de Ven, G. M. and Tuytelaars, T. (2023), Continual evaluation for lifelong learning: Identifying the stability gap, in ‘International Conference on Learning Representations’. https://openreview.net/forum?id=Zy350cRstc6

Deng et al. (2021) Deng, D., Chen, G., Hao, J., Wang, Q. and Heng, P.-A. (2021), Flattening sharpness for dynamic gradient projection memory benefits continual learning, in ‘Advances in Neural Information Processing Systems’, Vol. 34, pp. 18710–18721.

Deng et al. (2009) Deng, J., Dong, W., Socher, R., Li, L.-J., Li, K. and Fei-Fei, L. (2009), ImageNet: A large-scale hierarchical image database, in ‘IEEE Conference on Computer Vision and Pattern Recognition’, pp. 248–255.

Deng et al. (2020) Deng, S., Zhao, H., Fang, W., Yin, J., Dustdar, S. and Zomaya, A. Y. (2020), ‘Edge intelligence: The confluence of edge computing and artificial intelligence’, IEEE Internet of Things Journal 7 (8), 7457–7469.

Díaz-Rodríguez et al. (2018) Díaz-Rodríguez, N., Lomonaco, V., Filliat, D. and Maltoni, D. (2018), ‘Don’t forget, there is more than forgetting: new metrics for continual learning’, Preprint at https://arxiv.org/abs/1810.13166.

Doerig et al. (2023) Doerig, A., Sommers, R. P., Seeliger, K., Richards, B., Ismael, J., Lindsay, G. W., Kording, K. P., Konkle, T., Van Gerven, M. A., Kriegeskorte, N. and Kietzmann, T. C. (2023), ‘The neuroconnectionist research programme’, Nature Reviews Neuroscience pp. 1–20.

Dohare et al. (2023) Dohare, S., Hernandez-Garcia, J. F., Rahman, P., Sutton, R. S. and Mahmood, A. R. (2023), ‘Loss of plasticity in deep continual learning’, Preprint at https://arxiv.org/abs/2306.13812.

Douillard et al. (2020) Douillard, A., Cord, M., Ollion, C., Robert, T. and Valle, E. (2020), PODNet: Pooled outputs distillation for small-tasks incremental learning, in ‘European Conference on Computer Vision’, Springer, pp. 86–102.

Draelos et al. (2017) Draelos, T. J., Miner, N. E., Lamb, C. C., Cox, J. A., Vineyard, C. M., Carlson, K. D., Severa, W. M., James, C. D. and Aimone, J. B. (2017), Neurogenesis deep learning: Extending deep networks to accommodate new classes, in ‘International Joint Conference on Neural Networks (IJCNN)’, pp. 526–533.

Duchi et al. (2011) Duchi, J., Hazan, E. and Singer, Y. (2011), ‘Adaptive subgradient methods for online learning and stochastic optimization.’, Journal of Machine Learning Research 12 (7).

Ellefsen et al. (2015) Ellefsen, K. O., Mouret, J.-B. and Clune, J. (2015), ‘Neural modularity helps organisms evolve to learn new skills without forgetting old skills’, PLoS Computational Biology 11 (4), e1004128.

Farajtabar et al. (2020) Farajtabar, M., Azizan, N., Mott, A. and Li, A. (2020), Orthogonal gradient descent for continual learning, in ‘International Conference on Artificial Intelligence and Statistics’, PMLR, pp. 3762–3773.

Farquhar and Gal (2019) Farquhar, S. and Gal, Y. (2019), ‘A unifying bayesian view of continual learning’, Preprint at https://arxiv.org/abs/1902.06494.

Fernando et al. (2017) Fernando, C., Banarse, D., Blundell, C., Zwols, Y., Ha, D., Rusu, A. A., Pritzel, A. and Wierstra, D. (2017), ‘Pathnet: Evolution channels gradient descent in super neural networks’, Preprint at https://arxiv.org/abs/1701.08734.

Flesch et al. (2018) Flesch, T., Balaguer, J., Dekker, R., Nili, H. and Summerfield, C. (2018), ‘Comparing continual task learning in minds and machines’, Proceedings of the National Academy of Sciences 115 (44), E10313–E10322.

Flesch et al. (2023) Flesch, T., Nagy, D. G., Saxe, A. and Summerfield, C. (2023), ‘Modelling continual learning in humans with hebbian context gating and exponentially decaying task signals’, PLOS Computational Biology 19 (1), e1010808.

French (1999) French, R. M. (1999), ‘Catastrophic forgetting in connectionist networks’, Trends in Cognitive Sciences 3 (4), 128–135.

Gao et al. (2023) Gao, Q., Zhao, C., Sun, Y., Xi, T., Zhang, G., Ghanem, B. and Zhang, J. (2023), A unified continual learning framework with general parameter-efficient tuning, in ‘Proceedings of the IEEE/CVF International Conference on Computer Vision (ICCV)’, pp. 11483–11493.

Golkar et al. (2019) Golkar, S., Kagan, M. and Cho, K. (2019), ‘Continual learning via neural pruning’, Preprint at https://arxiv.org/abs/1903.04476.

Gomez-Villa et al. (2022) Gomez-Villa, A., Twardowski, B., Yu, L., Bagdanov, A. D. and van de Weijer, J. (2022), Continually learning self-supervised representations with projected functional regularization, in ‘Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR) Workshops’, pp. 3867–3877.

Goodfellow et al. (2013) Goodfellow, I. J., Mirza, M., Xiao, D., Courville, A. and Bengio, Y. (2013), ‘An empirical investigation of catastrophic forgetting in gradient-based neural networks’, Preprint at https://arxiv.org/abs/1312.6211.

Grossberg (1982) Grossberg, S. (1982), ‘Processing of expected and unexpected events during conditioning and attention: a psychophysiological theory.’, Psychological Review 89 (5), 529–572.

Guo et al. (2023) Guo, Y., Liu, B. and Zhao, D. (2023), Dealing with cross-task class discrimination in online continual learning, in ‘Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition’, pp. 11878–11887.

Hadsell et al. (2020) Hadsell, R., Rao, D., Rusu, A. A. and Pascanu, R. (2020), ‘Embracing change: Continual learning in deep neural networks’, Trends in Cognitive Sciences 24 (12), 1028–1040.

Hardt et al. (2013) Hardt, O., Nader, K. and Nadel, L. (2013), ‘Decay happens: the role of active forgetting in memory’, Trends in Cognitive Sciences 17 (3), 111–120.

Hayes et al. (2020) Hayes, T. L., Kafle, K., Shrestha, R., Acharya, M. and Kanan, C. (2020), REMIND your neural network to prevent catastrophic forgetting, in ‘European Conference on Computer Vision’, Springer, pp. 466–483.

Hayes and Kanan (2020) Hayes, T. L. and Kanan, C. (2020), Lifelong machine learning with deep streaming linear discriminant analysis, in ‘Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR) Workshops’, pp. 220–221.

Heald et al. (2021) Heald, J. B., Lengyel, M. and Wolpert, D. M. (2021), ‘Contextual inference underlies the learning of sensorimotor repertoires’, Nature 600 (7889), 489–493.

Hemati et al. (2023) Hemati, H., Cossu, A., Carta, A., Hurtado, J., Pellegrini, L., Bacciu, D., Lomonaco, V. and Borth, D. (2023), Class-incremental learning with repetition, in ‘Proceedings of The 2nd Conference on Lifelong Learning Agents’, Vol. 232 of Proceedings of Machine Learning Research , PMLR, pp. 437–455.

Henning et al. (2021) Henning, C., Cervera, M. R., D’Angelo, F., von Oswald, J., Traber, R., Ehret, B., Kobayashi, S., Sacramento, J. and Grewe, B. F. (2021), Posterior meta-replay for continual learning, in ‘Advances in Neural Information Processing Systems’, Vol. 34, pp. 14135–14149.

Heo et al. (2019) Heo, B., Kim, J., Yun, S., Park, H., Kwak, N. and Choi, J. Y. (2019), A comprehensive overhaul of feature distillation, in ‘Proceedings of the IEEE/CVF International Conference on Computer Vision’, pp. 1921–1930.

Hess et al. (2023) Hess, T., Tuytelaars, T. and van de Ven, G. M. (2023), ‘Two complementary perspectives to continual learning: Ask not only what to optimize, but also how’, Preprint at https://arxiv.org/abs/2311.04898.

Hinton et al. (1986) Hinton, G. E., McClelland, J. L. and Rumelhart, D. E. (1986), Distributed representations, in ‘Parallel Distributed Processing: Explorations in the Microstructure of Cognition, Vol. 1: Foundations’, MIT Press, Cambridge, MA, USA, p. 77–109.

Hinton et al. (2015) Hinton, G., Vinyals, O. and Dean, J. (2015), ‘Distilling the knowledge in a neural network’, Preprint at https://arxiv.org/abs/1503.02531.

Hsu et al. (2018) Hsu, Y.-C., Liu, Y.-C. and Kira, Z. (2018), ‘Re-evaluating continual learning scenarios: A categorization and case for strong baselines’, Preprint at https://arxiv.org/abs/1810.12488.

Hung et al. (2019) Hung, C.-Y., Tu, C.-H., Wu, C.-E., Chen, C.-H., Chan, Y.-M. and Chen, C.-S. (2019), Compacting, picking and growing for unforgetting continual learning, in ‘Advances in Neural Information Processing Systems’, Vol. 32.

Huyen (2022) Huyen, C. (2022), ‘Real-time machine learning: challenges and solutions’. Online blog, accessed on 22 Dec 2023. https://huyenchip.com/2022/01/02/real-time-machine-learning-challenges-and-solutions.html

Jeeveswaran et al. (2023) Jeeveswaran, K., Bhat, P. S., Zonooz, B. and Arani, E. (2023), Birt: Bio-inspired replay in vision transformers for continual learning, in ‘International Conference on Machine Learning’.

Jin et al. (2021) Jin, X., Sadhu, A., Du, J. and Ren, X. (2021), Gradient-based editing of memory examples for online task-free continual learning, in ‘Advances in Neural Information Processing Systems’, Vol. 34, pp. 29193–29205.

Joseph et al. (2022) Joseph, K. J., Khan, S., Khan, F. S., Anwer, R. M. and Balasubramanian, V. N. (2022), Energy-based latent aligner for incremental learning, in ‘Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition’, pp. 7452–7461.

Jung et al. (2020) Jung, S., Ahn, H., Cha, S. and Moon, T. (2020), Continual learning with node-importance based adaptive group sparse regularization, in ‘Advances in Neural Information Processing Systems’, Vol. 33, pp. 3647–3658.

Kao et al. (2021) Kao, T.-C., Jensen, K., van de Ven, G., Bernacchia, A. and Hennequin, G. (2021), Natural continual learning: success is a journey, not (just) a destination, in ‘Advances in Neural Information Processing Systems’, Vol. 34, pp. 28067–28079.

Kaplanis et al. (2018) Kaplanis, C., Shanahan, M. and Clopath, C. (2018), Continual reinforcement learning with complex synapses, in ‘International Conference on Machine Learning’, PMLR, pp. 2497–2506.

Kessler et al. (2023) Kessler, S., Cobb, A., Rudner, T. G., Zohren, S. and Roberts, S. J. (2023), ‘On sequential bayesian inference for continual learning’, Entropy 25 (6), 884.

Khan et al. (2019) Khan, M. E., Immer, A., Abedi, E. and Korzepa, M. (2019), Approximate inference turns deep networks into gaussian processes., in ‘Advances in Neural Information Processing Systems’, Vol. 32.

Khan et al. (2023) Khan, V., Cygert, S., Twardowski, B. and Trzciński, T. (2023), Looking through the past: better knowledge retention for generative replay in continual learning, in ‘Proceedings of the IEEE/CVF International Conference on Computer Vision (CVPR) Workshops’, pp. 3496–3500.

Kim et al. (2022) Kim, G., Xiao, C., Konishi, T., Ke, Z. and Liu, B. (2022), A theoretical study on solving continual learning, in ‘Advances in Neural Information Processing Systems’, Vol. 35, pp. 5065–5079.

Kingma and Ba (2014) Kingma, D. P. and Ba, J. (2014), ‘Adam: A method for stochastic optimization’, Preprint at https://arxiv.org/abs/1412.6980.

Kirkpatrick et al. (2017) Kirkpatrick, J., Pascanu, R., Rabinowitz, N., Veness, J., Desjardins, G., Rusu, A. A., Milan, K., Quan, J., Ramalho, T., Grabska-Barwinska, A. et al. (2017), ‘Overcoming catastrophic forgetting in neural networks’, Proceedings of the National Academy of Sciences 114 (13), 3521–3526.

Klasson et al. (2023) Klasson, M., Kjellstrom, H. and Zhang, C. (2023), ‘Learn the time to learn: Replay scheduling in continual learning’, Transactions on Machine Learning Research . https://openreview.net/forum?id=Q4aAITDgdP

Krawczyk and Gepperth (2023) Krawczyk, A. and Gepperth, A. (2023), ‘Adiabatic replay for continual learning’, Preprint at https://arxiv.org/abs/2303.13157.

Krizhevsky (2009) Krizhevsky, A. (2009), Learning multiple layers of features from tiny images, Technical report, University of Toronto.

Kudithipudi et al. (2022) Kudithipudi, D., Aguilar-Simon, M., Babb, J., Bazhenov, M., Blackiston, D., Bongard, J., Brna, A. P., Chakravarthi Raja, S., Cheney, N., Clune, J. et al. (2022), ‘Biological underpinnings for lifelong learning machines’, Nature Machine Intelligence 4 (3), 196–210.

Kudithipudi et al. (2023) Kudithipudi, D., Daram, A., Zyarah, A. M., Zohora, F. T., Aimone, J. B., Yanguas-Gil, A., Soures, N., Neftci, E., Mattina, M., Lomonaco, V. et al. (2023), ‘Design principles for lifelong learning AI accelerators’, Nature Electronics 6 , 807–822.

Laborieux et al. (2021) Laborieux, A., Ernoult, M., Hirtzlin, T. and Querlioz, D. (2021), ‘Synaptic metaplasticity in binarized neural networks’, Nature Communications 12 , 2549.

LeCun et al. (1998) LeCun, Y., Bottou, L., Bengio, Y. and Haffner, P. (1998), ‘Gradient-based learning applied to document recognition’, Proceedings of the IEEE 86 (11), 2278–2324.

Lee et al. (2020) Lee, S., Ha, J., Zhang, D. and Kim, G. (2020), A neural dirichlet process mixture model for task-free continual learning, in ‘International Conference on Learning Representations’. https://openreview.net/forum?id=SJxSOJStPr

Leimer et al. (2019) Leimer, P., Herzog, M. and Senn, W. (2019), ‘Synaptic weight decay with selective consolidation enables fast learning without catastrophic forgetting’, BioRxiv p. 613265.

Lesort et al. (2019a) Lesort, T., Caselles-Dupré, H., Garcia-Ortiz, M., Stoian, A. and Filliat, D. (2019a), Generative models from the perspective of continual learning, in ‘International Joint Conference on Neural Networks’, IEEE, pp. 1–8.

Lesort et al. (2019b) Lesort, T., Stoian, A. and Filliat, D. (2019b), ‘Regularization shortcomings for continual learning’, Preprint at https://arxiv.org/abs/1912.03049.

Li et al. (2022) Li, S., Du, Y., van de Ven, G. and Mordatch, I. (2022), Energy-based models for continual learning, in ‘Proceedings of The 1st Conference on Lifelong Learning Agents’, Vol. 199 of Proceedings of Machine Learning Research , PMLR, pp. 1–22.

Li and Hoiem (2017) Li, Z. and Hoiem, D. (2017), ‘Learning without forgetting’, IEEE Transactions on Pattern Analysis and Machine Intelligence 40 (12), 2935–2947.

Lin (1992) Lin, L.-J. (1992), ‘Self-improving reactive agents based on reinforcement learning, planning and teaching’, Machine Learning 8 , 293–321.

Liu et al. (2020) Liu, X., Wu, C., Menta, M., Herranz, L., Raducanu, B., Bagdanov, A. D., Jui, S. and van de Weijer, J. (2020), Generative feature replay for class-incremental learning, in ‘Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR) Workshops’, pp. 226–227.

Lopez-Paz and Ranzato (2017) Lopez-Paz, D. and Ranzato, M. (2017), Gradient episodic memory for continual learning, in ‘Advances in Neural Information Processing Systems’, Vol. 30, pp. 6470–6479.

Malviya et al. (2022) Malviya, P., Ravindran, B. and Chandar, S. (2022), Tag: Task-based accumulated gradients for lifelong learning, in ‘Proceedings of The 1st Conference on Lifelong Learning Agents’, Vol. 199 of Proceedings of Machine Learning Research , PMLR, pp. 366–389.

Marder and Thirumalai (2002) Marder, E. and Thirumalai, V. (2002), ‘Cellular, synaptic and network effects of neuromodulation’, Neural Networks 15 (4-6), 479–493.

Martens and Grosse (2015) Martens, J. and Grosse, R. (2015), Optimizing neural networks with kronecker-factored approximate curvature, in ‘International Conference on Machine Learning’, PMLR, pp. 2408–2417.

Masana et al. (2023) Masana, M., Liu, X., Twardowski, B., Menta, M., Bagdanov, A. D. and van de Weijer, J. (2023), ‘Class-incremental learning: survey and performance evaluation’, IEEE Transactions on Pattern Analysis and Machine Intelligence 45 (5), 5513–5533.

Masse et al. (2018) Masse, N. Y., Grant, G. D. and Freedman, D. J. (2018), ‘Alleviating catastrophic forgetting using context-dependent gating and synaptic stabilization’, Proceedings of the National Academy of Sciences pp. E10467–E10475.

McClelland et al. (2020) McClelland, J. L., McNaughton, B. L. and Lampinen, A. K. (2020), ‘Integration of new information in memory: new insights from a complementary learning systems perspective’, Philosophical Transactions of the Royal Society B 375 (1799), 20190637.

McCloskey and Cohen (1989) McCloskey, M. and Cohen, N. J. (1989), Catastrophic interference in connectionist networks: The sequential learning problem, in ‘Psychology of Learning and Motivation’, Vol. 24, Elsevier, pp. 109–165.

Mendez and Eaton (2023) Mendez, J. A. and Eaton, E. (2023), ‘How to reuse and compose knowledge for a lifetime of tasks: A survey on continual learning and functional composition’, Transactions on Machine Learning Research . Survey Certification. https://openreview.net/forum?id=VynY6Bk03b

Mirzadeh et al. (2020) Mirzadeh, S. I., Farajtabar, M., Pascanu, R. and Ghasemzadeh, H. (2020), Understanding the role of training regimes in continual learning, in ‘Advances in Neural Information Processing Systems’, Vol. 33, pp. 7308–7320.

Mitchell et al. (2022) Mitchell, E., Lin, C., Bosselut, A., Finn, C. and Manning, C. D. (2022), Fast model editing at scale, in ‘International Conference on Learning Representations’. https://openreview.net/forum?id=0DcZxeWfOPt

Mitchell et al. (2023) Mitchell, R., Menzenbach, R., Kersting, K. and Mundt, M. (2023), ‘Self-expanding neural networks’, Preprint at https://arxiv.org/abs/2307.04526.

Mnih et al. (2015) Mnih, V., Kavukcuoglu, K., Silver, D., Rusu, A. A., Veness, J., Bellemare, M. G., Graves, A., Riedmiller, M., Fidjeland, A. K., Ostrovski, G. et al. (2015), ‘Human-level control through deep reinforcement learning’, Nature 518 (7540), 529–533.

Mocanu et al. (2016) Mocanu, D. C., Vega, M. T., Eaton, E., Stone, P. and Liotta, A. (2016), ‘Online contrastive divergence with generative replay: Experience replay without storing data’, Preprint at https://arxiv.org/abs/1610.05555.

Morris (2003) Morris, R. G. M. (2003), ‘Long-term potentiation and memory’, Philosophical Transactions of the Royal Society of London Series B-Biological Sciences 358 (1432), 643–647.

Mundt et al. (2023) Mundt, M., Hong, Y., Pliushch, I. and Ramesh, V. (2023), ‘A wholistic view of continual learning with deep neural networks: Forgotten lessons and the bridge to active and open world learning’, Neural Networks 160 , 306–336.

Mundt et al. (2022) Mundt, M., Lang, S., Delfosse, Q. and Kersting, K. (2022), CLEVA-compass: A continual learning evaluation assessment compass to promote research transparency and comparability, in ‘International Conference on Learning Representations’. https://openreview.net/forum?id=rHMaBYbkkRJ

Netzer et al. (2011) Netzer, Y., Wang, T., Coates, A., Bissacco, A., Wu, B. and Ng, A. Y. (2011), Reading digits in natural images with unsupervised feature learning, in ‘NeurIPS Workshop on Deep Learning and Unsupervised Feature Learning’.

New et al. (2022) New, A., Baker, M., Nguyen, E. and Vallabha, G. (2022), ‘Lifelong learning metrics’, Preprint at https://arxiv.org/abs/2201.08278.

Nguyen et al. (2018) Nguyen, C. V., Li, Y., Bui, T. D. and Turner, R. E. (2018), Variational continual learning, in ‘International Conference on Learning Representations’. https://openreview.net/forum?id=BkQqq0gRb

Nørby (2015) Nørby, S. (2015), ‘Why forget? on the adaptive value of memory loss’, Perspectives on Psychological Science 10 (5), 551–578.

Nosofsky (1986) Nosofsky, R. M. (1986), ‘Attention, similarity, and the identification–categorization relationship.’, Journal of Experimental Psychology: General 115 (1), 39.

Ostapenko et al. (2022) Ostapenko, O., Lesort, T., Rodriguez, P., Arefin, M. R., Douillard, A., Rish, I. and Charlin, L. (2022), Continual learning with foundation models: An empirical study of latent replay, in ‘Proceedings of The 1st Conference on Lifelong Learning Agents’, Vol. 199 of Proceedings of Machine Learning Research , PMLR, pp. 60–91.

Özgün et al. (2020) Özgün, S., Rickmann, A.-M., Roy, A. G. and Wachinger, C. (2020), Importance driven continual learning for segmentation across domains, in M. Liu, P. Yan, C. Lian and X. Cao, eds, ‘Machine Learning in Medical Imaging: 11th International Workshop’, Springer, pp. 423–433.

Paik et al. (2020) Paik, I., Oh, S., Kwak, T. and Kim, I. (2020), Overcoming catastrophic forgetting by neuron-level plasticity control, in ‘Proceedings of the AAAI Conference on Artificial Intelligence’, Vol. 34, pp. 5339–5346.

Pan et al. (2020) Pan, P., Swaroop, S., Immer, A., Eschenhagen, R., Turner, R. E. and Khan, M. E. (2020), Continual deep learning by functional regularisation of memorable past, in ‘Advances in Neural Information Processing Systems’, Vol. 33, pp. 4453–4464.

Pandit and Kudithipudi (2020) Pandit, T. and Kudithipudi, D. (2020), Relational neurogenesis for lifelong learning agents, in ‘Proceedings of the 2020 Annual Neuro-Inspired Computational Elements Workshop’, pp. 1–9.

Pellegrini et al. (2020) Pellegrini, L., Graffieti, G., Lomonaco, V. and Maltoni, D. (2020), Latent replay for real-time continual learning, in ‘IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS)’, pp. 10203–10209.

Perconti and Plebe (2020) Perconti, P. and Plebe, A. (2020), ‘Deep learning and cognitive science’, Cognition 203 , 104365.

Prabhu et al. (2023) Prabhu, A., Al Kader Hammoud, H. A., Dokania, P. K., Torr, P. H., Lim, S.-N., Ghanem, B. and Bibi, A. (2023), Computationally budgeted continual learning: What does matter?, in ‘Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition’, pp. 3698–3707.

Radford et al. (2021) Radford, A., Kim, J. W., Hallacy, C., Ramesh, A., Goh, G., Agarwal, S., Sastry, G., Askell, A., Mishkin, P., Clark, J. et al. (2021), Learning transferable visual models from natural language supervision, in ‘International Conference on Machine Learning’, PMLR, pp. 8748–8763.

Rao et al. (2019) Rao, D., Visin, F., Rusu, A., Pascanu, R., Teh, Y. W. and Hadsell, R. (2019), Continual unsupervised representation learning, in ‘Advances in Neural Information Processing Systems’, Vol. 32, pp. 7647–7657.

Rasch and Born (2007) Rasch, B. and Born, J. (2007), ‘Maintaining memories by reactivation’, Current Opinion in Neurobiology 17 , 698–703.

Ratcliff (1990) Ratcliff, R. (1990), ‘Connectionist models of recognition memory: constraints imposed by learning and forgetting functions.’, Psychological Review 97 (2), 285–308.

Rebuffi et al. (2017) Rebuffi, S.-A., Kolesnikov, A., Sperl, G. and Lampert, C. H. (2017), iCaRL: Incremental classifier and representation learning, in ‘Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition’, pp. 2001–2010.

Richards and Frankland (2017) Richards, B. A. and Frankland, P. W. (2017), ‘The persistence and transience of memory’, Neuron 94 (6), 1071–1084.

Riemer et al. (2019) Riemer, M., Cases, I., Ajemian, R., Liu, M., Rish, I., Tu, Y. and Tesauro, G. (2019), Learning to learn without forgetting by maximizing transfer and minimizing interference, in ‘International Conference on Learning Representations’. https://openreview.net/forum?id=B1gTShAct7

Ritter et al. (2018) Ritter, H., Botev, A. and Barber, D. (2018), Online structured laplace approximations for overcoming catastrophic forgetting, in ‘Advances in Neural Information Processing Systems)’, Vol. 31.

Robins (1995) Robins, A. (1995), ‘Catastrophic forgetting, rehearsal and pseudorehearsal’, Connection Science 7 (2), 123–146.

Rolnick et al. (2019) Rolnick, D., Ahuja, A., Schwarz, J., Lillicrap, T. and Wayne, G. (2019), Experience replay for continual learning, in ‘Advances in Neural Information Processing Systems’, Vol. 32.

Roy et al. (2023) Roy, K., Simon, C., Moghadam, P. and Harandi, M. (2023), ‘Subspace distillation for continual learning’, Neural Networks 167 , 65–79.

Rusu et al. (2016) Rusu, A. A., Rabinowitz, N. C., Desjardins, G., Soyer, H., Kirkpatrick, J., Kavukcuoglu, K., Pascanu, R. and Hadsell, R. (2016), ‘Progressive neural networks’, Preprint at https://arxiv.org/abs/1606.04671.

Saha et al. (2021) Saha, G., Garg, I. and Roy, K. (2021), ‘Gradient projection memory for continual learning’, Preprint at https://arxiv.org/abs/2103.09762.

Schug et al. (2021) Schug, S., Benzing, F. and Steger, A. (2021), ‘Presynaptic stochasticity improves energy efficiency and helps alleviate the stability-plasticity dilemma’, Elife 10 , e69884.

Schwarz et al. (2018) Schwarz, J., Czarnecki, W., Luketina, J., Grabska-Barwinska, A., Teh, Y. W., Pascanu, R. and Hadsell, R. (2018), Progress & compress: A scalable framework for continual learning, in ‘International Conference on Machine Learning’, PMLR, pp. 4528–4537.

Serra et al. (2018) Serra, J., Suris, D., Miron, M. and Karatzoglou, A. (2018), Overcoming catastrophic forgetting with hard attention to the task, in ‘International Conference on Machine Learning’, PMLR, pp. 4548–4557.

Shanahan et al. (2021) Shanahan, M., Kaplanis, C. and Mitrović, J. (2021), ‘Encoders and ensembles for task-free continual learning’, Preprint at https://arxiv.org/abs/2105.13327.

Shin et al. (2017) Shin, H., Lee, J. K., Kim, J. and Kim, J. (2017), Continual learning with deep generative replay, in ‘Advances in Neural Information Processing Systems’, Vol. 30, pp. 2994–3003.

Snell et al. (2017) Snell, J., Swersky, K. and Zemel, R. (2017), Prototypical networks for few-shot learning, in ‘Advances Neural Information Processing Systems’, Vol. 30, pp. 4080–4090.

Sossin (2008) Sossin, W. S. (2008), Molecular memory traces, in W. S. Sossin, J. C. Lacaille, V. F. Castellucci and S. Belleville, eds, ‘Essence of Memory’, Vol. 169, Elsevier Science Bv, Amsterdam, pp. 3–25.

Soures et al. (2021) Soures, N., Helfer, P., Daram, A., Pandit, T. and Kudithipudi, D. (2021), TACOS: task agnostic continual learning in spiking neural networks, in ‘Theory and Foundation of Continual Learning Workshop at ICML’2021’.

Soutif-Cormerais et al. (2021) Soutif-Cormerais, A., Masana, M., van de Weijer, J. and Twardowski, B. (2021), ‘On the importance of cross-task features for class-incremental learning’, Preprint at https://arxiv.org/abs/2106.11930.

Srivastava et al. (2013) Srivastava, R. K., Masci, J., Kazerounian, S., Gomez, F. and Schmidhuber, J. (2013), Compete to compute, in ‘Advances in Neural Information Processing Systems’, Vol. 26.

Stojanov et al. (2019) Stojanov, S., Mishra, S., Thai, N. A., Dhanda, N., Humayun, A., Yu, C., Smith, L. B. and Rehg, J. M. (2019), Incremental object learning from contiguous views, in ‘Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition’, pp. 8777–8786.

Tadros et al. (2022) Tadros, T., Krishnan, G. P., Ramyaa, R. and Bazhenov, M. (2022), ‘Sleep-like unsupervised replay reduces catastrophic forgetting in artificial neural networks’, Nature Communications 13 (1), 7742.

Terekhov et al. (2015) Terekhov, A. V., Montone, G. and O’Regan, J. K. (2015), Knowledge transfer in deep block-modular neural networks, in ‘Biomimetic and Biohybrid Systems: Living Machines’, Springer, pp. 268–279.

Thrun and Mitchell (1995) Thrun, S. and Mitchell, T. M. (1995), ‘Lifelong robot learning’, Robotics and Autonomous Systems 15 (1-2), 25–46.

Tian et al. (2021) Tian, Y., Henaff, O. J. and van den Oord, A. (2021), Divide and contrast: Self-supervised learning from uncurated data, in ‘Proceedings of the IEEE/CVF International Conference on Computer Vision’, pp. 10063–10074.

Titsias et al. (2020) Titsias, M. K., Schwarz, J., Matthews, A. G. d. G., Pascanu, R. and Teh, Y. W. (2020), Functional regularisation for continual learning with gaussian processes, in ‘International Conference on Learning Representations’. https://openreview.net/forum?id=HkxCzeHFDB

Tran Tung et al. (2023) Tran Tung, L., Nguyen Van, V., Nguyen Hoang, P. and Than, K. (2023), Sharpness and gradient aware minimization for memory-based continual learning, in ‘Proceedings of the 12th International Symposium on Information and Communication Technology’, pp. 189–196.

van de Ven et al. (2021) van de Ven, G. M., Li, Z. and Tolias, A. S. (2021), Class-incremental learning with generative classifiers, in ‘Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR) Workshops’, pp. 3611–3620.

van de Ven et al. (2020) van de Ven, G. M., Siegelmann, H. T. and Tolias, A. S. (2020), ‘Brain-inspired replay for continual learning with artificial neural networks’, Nature Communications 11 , 4069.

van de Ven and Tolias (2018) van de Ven, G. M. and Tolias, A. S. (2018), Three continual learning scenarios, in ‘NeurIPS Continual Learning Workshop’.

van de Ven et al. (2022) van de Ven, G. M., Tuytelaars, T. and Tolias, A. S. (2022), ‘Three types of incremental learning’, Nature Machine Intelligence 4 (12), 1185–1197.

van Gerven and Bohte (2017) van Gerven, M. and Bohte, S. (2017), ‘Editorial: Artificial neural networks as models of neural information processing’, Frontiers in Computational Neuroscience 11 , 114.

Verma et al. (2021) Verma, V. K., Liang, K. J., Mehta, N., Rai, P. and Carin, L. (2021), Efficient feature transformations for discriminative and generative continual learning, in ‘Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition’, pp. 13865–13875.

Verwimp et al. (2023) Verwimp, E., Aljundi, R., Ben-David, S., Bethge, M., Cossu, A., Gepperth, A., Hayes, T. L., Hüllermeier, E., Kanan, C., Kudithipudi, D. et al. (2023), ‘Continual learning: Applications and the road forward’, Preprint at https://arxiv.org/abs/2311.11908.

Vinyals et al. (2016) Vinyals, O., Blundell, C., Lillicrap, T. and Wierstra, D. (2016), Matching networks for one shot learning, in ‘Advances in Neural Information Processing Systems’, Vol. 29.

Vogelstein et al. (2020) Vogelstein, J. T., Dey, J., Helm, H. S., LeVine, W., Mehta, R. D., Tomita, T. M., Xu, H., Geisa, A., Wang, Q. et al. (2020), ‘Representation ensembling for synergistic lifelong learning with quasilinear complexity’, Preprint at https://arxiv.org/abs/2004.12908.

von Oswald et al. (2020) von Oswald, J., Henning, C., Sacramento, J. and Grewe, B. F. (2020), Continual learning with hypernetworks, in ‘International Conference on Learning Representations’. https://openreview.net/forum?id=SJgwNerKvB

Wang et al. (2023a) Wang, L., Zhang, X., Li, Q., Zhang, M., Su, H., Zhu, J. and Zhong, Y. (2023a), ‘Incorporating neuro-inspired adaptability for continual learning in artificial intelligence’, Nature Machine Intelligence 5 (12), 1356–1368.

Wang et al. (2023b) Wang, L., Zhang, X., Su, H. and Zhu, J. (2023b), ‘A comprehensive survey of continual learning: Theory, method and application’, Preprint at https://arxiv.org/abs/2302.00487.

Wang et al. (2022a) Wang, R., Ciccone, M., Luise, G., Pontil, M., Yapp, A. and Ciliberto, C. (2022a), ‘Schedule-robust online continual learning’, Preprint at https://arxiv.org/abs/2210.05561.

Wang et al. (2022b) Wang, Z., Zhang, Z., Lee, C.-Y., Zhang, H., Sun, R., Ren, X., Su, G., Perot, V., Dy, J. and Pfister, T. (2022b), Learning to prompt for continual learning, in ‘Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition’, pp. 139–149.

Wei et al. (2021) Wei, K., Deng, C., Yang, X. and Li, M. (2021), Incremental embedding learning via zero-shot translation, in ‘Proceedings of the AAAI Conference on Artificial Intelligence’, Vol. 35, pp. 10254–10262.

Wilson and McNaughton (1994) Wilson, M. A. and McNaughton, B. L. (1994), ‘Reactivation of hippocampal ensemble memories during sleep’, Science 265 (5172), 676–679.

Wiskott et al. (2006) Wiskott, L., Rasch, M. J. and Kempermann, G. (2006), ‘A functional hypothesis for adult hippocampal neurogenesis: avoidance of catastrophic interference in the dentate gyrus’, Hippocampus 16 (3), 329–343.

Wixted (2004) Wixted, J. T. (2004), ‘The psychology and neuroscience of forgetting’, Annual Review of Psychology 55 , 235–269.

Wortsman et al. (2020) Wortsman, M., Ramanujan, V., Liu, R., Kembhavi, A., Rastegari, M., Yosinski, J. and Farhadi, A. (2020), Supermasks in superposition, in ‘Advances in Neural Information Processing Systems’, Vol. 33, pp. 15173–15184.

Wu et al. (2018) Wu, C., Herranz, L., Liu, X., Wang, Y., van de Weijer, J. and Raducanu, B. (2018), Memory replay gans: learning to generate images from new categories without forgetting, in ‘Advances in Neural Information Processing Systems’, Vol. 31, pp. 5966–5976.

Yan et al. (2021) Yan, S., Xie, J. and He, X. (2021), DER: Dynamically expandable representation for class incremental learning, in ‘Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition’, pp. 3014–3023.

Yang et al. (2023) Yang, E., Shen, L., Wang, Z., Liu, S., Guo, G. and Wang, X. (2023), Data augmented flatness-aware gradient projection for continual learning, in ‘Proceedings of the IEEE/CVF International Conference on Computer Vision’, pp. 5630–5639.

Yang et al. (2018) Yang, H.-M., Zhang, X.-Y., Yin, F. and Liu, C.-L. (2018), Robust classification with convolutional prototype learning, in ‘Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition’, pp. 3474–3482.

Yoon et al. (2018) Yoon, J., Yang, E., Lee, J. and Hwang, S. J. (2018), Lifelong learning with dynamically expandable networks, in ‘International Conference on Learning Representations’. https://openreview.net/forum?id=Sk7KsfW0-

Yu et al. (2020) Yu, L., Twardowski, B., Liu, X., Herranz, L., Wang, K., Cheng, Y., Jui, S. and van de Weijer, J. (2020), Semantic drift compensation for class-incremental learning, in ‘Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR) Workshops’, pp. 6982–6991.

Zając et al. (2024) Zając, M., Tuytelaars, T. and van de Ven, G. M. (2024), Prediction error-based classification for class-incremental learning, in ‘International Conference on Learning Representations’. https://openreview.net/forum?id=DJZDgMOLXQ

Zeng et al. (2019) Zeng, G., Chen, Y., Cui, B. and Yu, S. (2019), ‘Continual learning of context-dependent processing in neural networks’, Nature Machine Intelligence 1 (8), 364–372.

Zenke et al. (2015) Zenke, F., Agnes, E. J. and Gerstner, W. (2015), ‘Diverse synaptic plasticity mechanisms orchestrated to form and retrieve memories in spiking neural networks’, Nature Communications 6 (1), 1–13.

Zenke et al. (2017) Zenke, F., Poole, B. and Ganguli, S. (2017), Continual learning through synaptic intelligence, in ‘International Conference on Machine Learning’, PMLR, pp. 3987–3995.

Zeno et al. (2019) Zeno, C., Golan, I., Hoffer, E. and Soudry, D. (2019), ‘Task agnostic continual learning using online variational bayes’, Preprint at https://arxiv.org/abs/1803.10123v3.

Zhou et al. (2012) Zhou, G., Sohn, K. and Lee, H. (2012), Online incremental feature learning with denoising autoencoders, in ‘Artificial Intelligence and Statistics’, Vol. 22, PMLR, pp. 1453–1461.

Zohora et al. (2020) Zohora, F. T., Zyarah, A. M., Soures, N. and Kudithipudi, D. (2020), Metaplasticity in multistate memristor synaptic networks, in ‘IEEE International Symposium on Circuits and Systems (ISCAS)’, IEEE, pp. 1–5.

## Instructions for reporting errors

We are continuing to improve HTML versions of papers, and your feedback helps enhance accessibility and mobile support. To report errors in the HTML that will help us improve conversion and rendering, choose any of the methods listed below:

Click the "Report Issue" ( ) button, located in the page header.

Tip: You can select the relevant text first, to include it in your report.

Our team has already identified the following issues . We appreciate your time reviewing and reporting rendering errors we may not have found yet. Your efforts will help us improve the HTML versions for all readers, because disability should not be a barrier to accessing research. Thank you for your continued support in championing open access for all.

Have a free development cycle? Help support accessibility at arXiv! Our collaborators at LaTeXML maintain a list of packages that need conversion , and welcome developer contributions .
