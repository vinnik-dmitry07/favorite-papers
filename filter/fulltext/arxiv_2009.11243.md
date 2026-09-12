##### Report GitHub Issue

Content selection saved. Describe the issue below:

# Tasks, stability, architecture, and compute: Training more effective learned optimizers, and using them to train themselves

###### Abstract

Much as replacing hand-designed features with learned functions has revolutionized how we solve perceptual tasks, we believe learned algorithms will transform how we train models. In this work we focus on general-purpose learned optimizers capable of training a wide variety of problems with no user-specified hyperparameters. We introduce a new, neural network parameterized, hierarchical optimizer with access to additional features such as validation loss to enable automatic regularization. Most learned optimizers have been trained on only a single task, or a small number of tasks. We train our optimizers on thousands of tasks, making use of orders of magnitude more compute, resulting in optimizers that generalize better to unseen tasks. The learned optimizers not only perform well, but learn behaviors that are distinct from existing first order optimizers. For instance, they generate update steps that have implicit regularization and adapt as the problem hyperparameters (e.g. batch size) or architecture (e.g. neural network width) change. Finally, these learned optimizers show evidence of being useful for out of distribution tasks such as training themselves from scratch.

## 1 Introduction

Much of the success of modern deep learning has been driven by a shift from hand-designed features carefully curated by human experts, to domain-agnostic methods that can learn features from large amounts of data. By leveraging large-scale datasets with flexible models, we are now able to rapidly learn powerful features for new problem settings that often generalize to novel tasks. While learned features outperform hand-designed features on numerous tasks [ 1 , 2 , 3 , 4 ] , we continue to use hand-designed optimization algorithms (such as gradient descent, momentum, and so on) for training models.

These hand-designed update rules benefit from decades of optimization research but still require extensive expert supervision in order to be used effectively in machine learning. For example, they fail to flexibly adapt to new problem settings and require careful tuning of learning rate schedules and momentum timescales for different model architectures and datasets [ 5 ] . In addition, most do not leverage alternative sources of information beyond the gradient, such as the validation loss. By separating the optimization target (training loss) from the broader goal (generalization), classic methods require more careful tuning of regularization and/or data augmentation strategies by the practitioner.

To address these drawbacks, recent work on learned optimizers aims to replace hand-designed optimizers with a parametric optimizer, trained on a set of tasks, that can then be applied more generally. Recent work in this area has focused on either augmenting existing optimizers to adapt their own hyperparameters [ 6 , 7 , 8 ] , or developing more expressive learned optimizers to replace existing optimizers entirely [ 9 , 10 , 11 , 12 , 13 , 14 , 15 ] . These latter models take in problem information (such as the current gradient of the training loss) and iteratively update parameters. However, to date, learned optimizers have proven to be brittle and ineffective at generalizing across diverse sets of problems.

Our work identifies fundamental barriers that have limited progress in learned optimizer research and addresses several of these barriers to train effective optimizers: 1. Computational scale : Training a learned optimizer is costly. When training the optimizer, a single training step requires applying the optimizer to a training task for some number of unrolled steps. This work utilizes massive parallel computing infrastructure to scale the number of unrolled steps an order of magnitude larger than in previous work.

2. Training tasks : Deep learning requires large training datasets. For learned optimizers to be effective, we similarly need a large dataset of optimization tasks on which to train the optimizer. We build off of the TaskSet dataset [ 16 ] and construct a dataset of more than a thousand diverse optimization tasks commonly found in machine learning. We show how this large and diverse task distribution is critical for training optimizers that generalize.

3. Inductive bias of optimizer architecture : The parameterization of the learned optimizer and the task information fed to it both strongly affect performance. In this work, we propose a new hierarchical learned optimizer architecture that incorporates additional task information (such as validation loss), and show that it outperforms previous learned optimizer architectures.

By addressing these barriers, we develop learned optimizers that exceed prior work in scale, robustness, and out of distribution generalization. As a final test, we show that the learned optimizer can be used to train new learned optimizers from scratch (analogous to “self-hosting” compilers [ 17 ] ). We see this final accomplishment as being analogous to the first time a compiler is complete enough that it can be used to compile itself.

## 2 Preliminaries

Training a learned optimizer is a bilevel optimization problem that contains two loops: an inner loop that applies the optimizer to solve a task, and an outer loop that iteratively updates the parameters of the learned optimizer [ 18 ] . We use the inner- and outer- prefixes throughout to be explicit about which optimization loop we are referring to. That is, the inner-loss refers to a target task’s loss function that we wish to optimize, and the outer-loss refers to a measure of the optimizer’s performance training the target task (inner-task). Correspondingly, we refer to the optimizer parameters as outer-parameters , and the parameters that the optimizer is updating as inner-parameters . Outer-optimization refers to the act of finding outer-parameters that perform well under some outer-loss .

For a given inner-task, we apply the learned optimizer for some number of steps ( unrolling the optimizer). Ideally, we would unroll each target task until some stopping criterion is reached, but this is computationally infeasible for even moderate scale machine learning tasks. Each outer-iteration requires unrolling the optimizer on a target task. Short (truncated) unrolls are more computationally efficient, but suffer from truncation bias [ 19 , 14 ] in that the outer-loss surface computed using truncated unrolls is different (and may have different minima) than the fully unrolled outer-loss.

## 3 Methods: Addressing the three barriers to learned optimizers

### 3.1 Outer-Optimization

To train the optimizer, we minimize an outer-loss that quantifies the performance of the optimizer. This is defined as the mean of the inner-loss computed on the inner- validation set for some number of unrolled steps, averaged over inner-tasks in the outer-training taskset. Although this outer-loss is differentiable, it is costly to compute the outer-gradient (which involves backpropagating through the unrolled optimization). In addition, the outer-loss surface is badly conditioned and extremely non-smooth [ 14 ] , making it difficult to optimize.

We deal with these issues by using derivative-free optimization–specifically, evolutionary strategies (ES) [ 20 ] –to minimize the outer-loss, obviating the need to compute derivatives through the unrolled optimization process. Previous work has used unrolled derivatives [ 9 , 10 , 14 ] , and was thus limited to short numbers of unrolled steps (e.g. 20 in Andrychowicz et al. [9] and starting at 50 in Metz et al. [14] ). Using ES, we are able to use considerably longer unrolls. Initial unroll lengths were chosen to balance communication cost between parallel workers (when updating optimizer parameters) with the computational cost of unrolling on individual workers (when estimating the local gradient with ES). We start outer-training by sampling unroll steps uniformly from 240-360 steps. When performance saturates, we continue training with Persistent Evolotionary Strategies (PES) [ 21 ] . PES provides an unbiased estimate of the outer-gradient over the entire inner task, but at the cost of higher variance gradients.

ES and PES have an additional benefit, in that optimizing with ES smooths the underlying loss function. This smoothing helps stabilize outer-training [ 14 ] . We set the standard deviation of the Gaussian distribution used by the ES algorithm (which also controls how much the outer-loss is smoothed) to 0.01. To deal with the high variance of the ES estimate of the gradient, we use antithetic sampling and train in in parallel using 1024 multi-core CPU workers. While using more workers increases training speed, we find 1024 to be the point where performance gains become sub-linear. For more details see Appendix B .

### 3.2 Task distributions

To train the optimizer, we need to define a set of inner-tasks to use for training. The choice of training tasks is critically important for two reasons: it determines the ability of the optimizer to outer-generalize (i.e. the learned optimizer’s performance on new tasks), and it determines the computational complexity of outer-training. For improved outer-generalization, we would like our inner-problems to be representative of tasks we care about. In this work, these are state-of-the-art machine learning models such as ResNets [ 22 ] or Transformers [ 23 ] . Unfortunately, directly utilizing these large scale models is computationally infeasible, therefore we outer-train on proxy tasks for speed [ 24 ] .

In order to outer-train a learned optimizer capable of generalizing to new optimization tasks, we utilize an outer-training task set consisting of around 6,000 tasks designed after Metz et al. [16] . These tasks include RNNs [ 25 , 26 ] , CNNs [ 27 ] , masked auto regressive flows [ 28 ] , fully connected networks, language modeling, variational autoencoders [ 29 ] , simple 2D test functions, quadratic bowls, and more. For tasks that require them, we additionally sample a dataset, batch size, network architecture, and initialization scheme. To keep outer-training efficient, we ensure that all tasks take less than 100 milliseconds per-training step. For each task that makes use of a dataset, we create four splits of the data to prevent leakage: training data, which we compute gradients on and use to update the inner-parameters; inner-validation data, which is used to compute validation losses used by the learned optimizer; outer-validation data, which is used to update the weights of the learned optimizer; and test data, which is used to test an already trained learned optimizer. Because loss values vary in magnitude, when outer-training we normalize these outer-loss values by the best loss achieved by a baseline optimizer and the initial loss value. Note this normalization is not used during inner-training.

### 3.3 Optimizer architecture

Designing a learned optimizer architecture requires balancing computational efficiency and expressivity. Past work in learned optimizers has shown that incorporating inductive biases based on existing optimization techniques such as momentum or second moment accumulation leads to better performance [ 10 , 14 ] . The optimizer we use in this work consists of a hierarchical optimizer similar to [ 10 ] (Figure 1 ). A per-tensor LSTM is run on features computed over each parameter tensor. This LSTM then forwards information to the other tensors’ LSTMs as well as to a per-parameter feedforward neural network. The per-parameter feedforward network additionally takes in information about gradients and parameter value, and outputs parameter updates. Additional outputs are aggregated and fed back into the per-tensor network. This information routing allows for communication across all components.

For per-parameter features we leverage effective inductive biases from hand-designed optimizers, and use a variety of features including the gradient, the parameter value, and momentum-like running averages of both. All features are normalized, in a fashion similar to that in RMSProp [ 30 ] , or relative to the norm across the full tensor. For per-tensor features we use a variety of features built from summary statistics computed from the current tensor, the tensor’s gradient, and running average features such as momentum and second moments. We also include information about the tensor’s rank and shape. We also feed global features into the per-tensor LSTM, such as training loss and validation loss, normalized so as to have a relatively consistent scale across tasks. To compute a weight update, the per-parameter MLP outputs two values, ( a , b ) (a,b) , which are used to update inner-parameters: w t + 1 = w t + exp ⁡ ( a ) ​ b w^{t+1}=w^{t}+\exp(a)b . See Appendix C for many more details.

## 4 Results

### 4.1 Comparing learned optimizer architectures and training task set sizes

First, we show experiments comparing the performance of different learned optimizer architectures from the literature. We trained: a component-wise LSTM optimizer from Andrychowicz et al. [9] (L2LBGDGD), a modification of this LSTM with the decomposed direction and magnitude output from Metz et al. [14] (LSTM), the fully connected optimizer from Metz et al. [14] (FF), as well as the proposed learned optimizer in this work (§ 3.3 ) (LSTM_FF). As shown in Figure 2 (a), the proposed architecture achieves the lowest outer-training loss and achieves this in the fewest outer-training steps. To the best of our knowledge, this is the first published comparison across different learned optimizer architectures, on the same suite of tasks. Previous work only compared a proposed learned optimizer against hand-designed (baseline) optimizers.

Next, we explored how increasing the number of inner-tasks used when training an optimizer affects final performance. To do this, we randomly sampled subsets of tasks from the full task set, while evaluating performance on a common held-out set of tasks. Figure 2 (b) shows that increasing the number of tasks leads to large improvements.

### 4.2 Comparisons with hand-designed optimizers

We compare against three baseline optimizers: AdamLR , which is the Adam optimizer [ 31 ] with a tuned learning rate. Adam8p , which is a version of the Adam optimizer with eight tunable hyperparameters: learning rate, β 1 \beta_{1} , β 2 \beta_{2} , and ϵ \epsilon , plus additional ℓ 1 \ell_{1} and ℓ 2 \ell_{2} regularization penalties, and a learning rate schedule parameterized with a linear decay and exponential decay. See Appendix D for more details. Our final baseline optimizer, called opt_list , consists of the NAdam optimizer [ 32 ] with “AdamW” style weight decay [ 33 ] , cosine learning rate schedules [ 34 ] and learning rate warm up (See Metz et al. [16] for more info). Instead of tuning these with some search procedure, however, we draw them from a sorted list of hyperparameters provided by [ 16 ] for increased sample efficiency.

Evaluation of optimizers, let alone learned optimizers, is difficult due to different tasks of interest, hyperparameter search strategies, and compute budgets [ 5 , 35 ] . We structure our comparison by exploring two scenarios for how a machine learning practitioner might go about tuning the hyperparameters of an optimizer. First, we consider an “off-the-shelf” limit, where a practitioner performs a small number of optimizer evaluations using off-the-shelf methods (for instance, tuning learning rate only). This is typically done during exploration of a new machine learning model or dataset. Second, we consider a “finely tuned” limit, where a practitioner has a large compute budget devoted to tuning hyperparameters of a traditional optimizer for a particular problem of interest.

For the “off-the-shelf” limit, we consider the scenario where a practitioner has access to a limited number of optimization runs (trials) ( ≤ 10 \leq 10 ) for a particular problem. Thus, we select a first set of baseline hyperparameters using a single, default value (denoted global in Fig 3 ) across all of the tasks. We use random search (RS) using 1000 different hyperparameter values to find the global value that performs best on average for all tasks.

Practitioners often tune models with a small number of evaluations. As such, we include comparisons to per-task tuned learning rate tuned Adam, the first 10 entries of opt_list, and 10 hyperparameter evaluations obtained from random search using the adam8p hyperparmeterization.

For the “finely tuned” limit, we consider task-specific hyperparameter tuning, where the hyperparameters for each baseline optimizer are selected individually for each task (denoted per-task in Fig 3 ).

We plot a histogram over tasks showing the difference in performance between the each baseline optimizer and the learned optimizer in each row of Fig 3 . First, we note that the distribution is broad, indicating that for some tasks the learned optimizer is much better, whereas for others, the baseline optimizer(s) are better. On average, we see small but consistent performance improvements over baseline optimizers, especially in the “off-the-shelf” scenario. We attribute this to the diverse set of tasks used for training the learned optimizer.

### 4.3 Understanding optimizer behavior

To better understand the behavior of the learned optimizer, we performed probe experiments where we compared trajectories of the learned optimizer on simple loss surfaces against baseline optimizers. The goal of these experiments was to generate insight into what the learned optimizer has learned.

In machine learning, many problems benefit from including some kind of regularization penalty, such as an ℓ 2 \ell_{2} penalty on the weights or parameters of a model. We explored whether the learned optimizer (which was trained to minimize validation loss) had any implicit regularization, beyond what was specified as part of the loss. To test this, we ran optimizers on a simple 2D loss surface, with a continuum of solutions along the diagonal: f ⁡ ( x , y ) = 1 2 ​ ( x − y ) 2 f(x,y)=\frac{1}{2}\left(x-y\right)^{2} . Although any point along the x = y x=y diagonal is a global minimum, we wanted to see if the learned optimizer would prefer any particular solution within that set.

Figure 4 shows the resulting training trajectories along the 2D loss surface from many starting points. For a baseline optimizer (left), the trajectories find the nearest point on the diagonal. However, we find that the learned optimizer has learned some implicit regularization, in that it pushes the parameters towards a solution with small norm: ( 0 , 0 ) (0,0) .

### 4.4 Generalization along different task axes

Next, we wondered whether the learned optimizer was capable of training machine learning models which differed across different architectural and training hyperparameters. To test this type of generalization, we trained fully connected neural networks on CIFAR-10 and MNIST, and swept three model hyperparameters: the number of hidden units per layer (network width), the batch size, and the number of training examples (dataset size, formed by subsampling the full dataset). For each sweep, we compare the learned optimizer to a baseline optimizer, Adam, over a grid of eight different learning rates logarithmically spaced from 10 − 5.5 10^{-5.5} to 10 − 2 10^{-2} .

The results of these experiments are in Fig. 5 . As we vary the number of hidden units (left column) or batch size (middle column), the learned optimizer generalizes outside of the range of hidden units used during training (indicated by the shaded regions). In addition, the learned optimizer matches the performance of the best learning rate tuned Adam optimizer. On CIFAR-10, as we move further away from the outer-training task distribution, the learned optimizer diverges. For dataset size (right column), we find that the learned optimizer is more sensitive to the amount of data present (performance drops off more quickly as the dataset size decreases). These experiments demonstrate the learned optimizer is capable of adapting to some aspects of target tasks which differ from its outer-training distribution, without additional tuning.

### 4.5 Generalization to large-scale problems

We test the learned optimizer on large-scale machine learning tasks. We use two ResNet V2 [ 36 ] architectures: a 14 layer residual network trained on CIFAR-10 [ 37 ] ; and a 35 layer residual network trained on 64x64 resized ImageNet [ 38 ] . We train both networks with the learned optimizer and compare the performance to learning rate tuned Adam and Momentum (Fig. 6 ). Details in Appendix D . For CIFAR-10, we find that the learned optimizer achieves similar performance as the baselines but does not overfit later in inner-training. For ImageNet, we find that the learned optimizer performs slightly worse.

Note that our baselines only include learning rate tuning. More specialized hyperparameter configurations, designed specifically for these tasks, such as learning rate schedules and data augmentation strategies will perform better. An extensive study of learned optimizer performance on a wide range of state-of-the-art models is a subject for future work.

### 4.6 Learned optimizers training themselves

Finally, we performed an experiment to test if a learned optimizer can be use to train new learned optimizers. Figure 8 shows that this “self-optimized” training curve is similar to the training curve using our hand-tuned training setup (using the Adam optimizer). We interpret this as evidence of unexpectedly effective generalization, as the training of a learned optimizer is unlike anything in the set of training tasks used to train the optimizer. We show outer-training for 10k outer-training iterations, matching the number of inner-iterations used when outer-training the learned optimizer. If outer-training is continued beyond 10k iterations, learned optimizer performance worsens (see Appendix G ), suggesting that more inner-iterations are needed when outer-training.

## 5 Discussion

In this work, we train a learned optimizer using a larger and more diverse set of training tasks, better optimization techniques, an improved optimizer architecture, and more compute than previous work. The resulting optimizer outperforms hand-designed optimizers constrained to a single set of hyperparameters, and performs comparably to hand designed optimizers after a modest hyperparameter search. Further, it demonstrates some ability to generalize to optimization tasks unlike those it was trained on. Most dramatically, it demonstrates an ability to train itself.

However, the learned optimizer we develop is not without limitations. Below we summarize areas for future work.

Generalization: While it performs well for tasks like those in TaskSet, we do not yet fully understand its outer-generalization capabilities. It shows promising ability to generalize to out of distribution problems such as training itself, and ResNet models, but it does not outperform competing algorithms in all settings on simple “out of distribution” optimization tasks, like those seen in Figure 5 .

Optimization / Compute: Currently it takes significant compute expenditure to train a learned optimizer at this scale, resulting in a nontrivial carbon footprint. Ideally training can be run once and the resulting learned optimizer can be used broadly as is the case with BERT [ 39 ] .

Learned optimizer architectures: We have shown there is considerable improvement to be had by incorporating better inductive biases both in outer-optimization speed and capacity. Improving these architectures, and leveraging additional features will hopefully lead to more performant learned optimizers. Additionally, the current optimizer, while compute efficient, is memory inefficient requiring > 5 × >\!5\times more storage per-parameter than Adam. We do not believe this poses a fundamental barrier, but modifications similar to those in Shazeer and Stern [40] will be needed to train larger models.

Outer-training task distribution: We have shown that training on larger tasksets leads to better generalization. We have not studied which tasks should be included so as to aid outer-generalization.

## Acknowledgements

We would like to thank Alex Alemi, Eric Jang, Diogo Moitinho de Almeida, Timothy Nguyen, Alec Radford, Ruoxi Sun, Paul Vicol and Wojciech Zaremba for discussion related to this work as well as the Brain Team for providing a supportive research environment. We would also like to thank the authors of Numpy [ 41 , 42 , 43 ] , Seaborn [ 44 ] , and Matplotlib [ 45 ] .

## Broader Impact

Machine learning training and inference is a major energy consumer, and training models likely dominates most individual machine learning researcher’s carbon emissions [ 46 ] . By meta-learning optimizers, we hope to amortize the cost of training ML models, and thus reduce the environmental impact of training a single model. We hope to achieve this both by reducing the need for extensive hyperparameter tuning as models are developed, and making training more efficient for the best hyperparameters.

With this work, and more generally with meta-learning algorithms, we hope to provide researchers access to more performant easier to use optimizers for their problems. Improving technology to do machine learning will accelerate its impact, for better or worse. We believe machine learning technologies will be beneficial to humanity on the whole, and thus by improving the ability to optimize models we are moving towards this goal.

Our optimizer is trained on a mixture of different tasks and datasets. It is our goal to construct an outer-training distribution that learns relevant inductive biases for machine learning tasks of interest. However, we currently do not have good methods to decipher exactly what types of inductive biases a learned optimizer might learn. Thus, future work is needed to explore what kinds of information is absorbed by learned optimizers. In the meantime, care should be taken when employing learned optimizers as the inductive biases of a particular learned optimizer may not be appropriate for an end user’s goals.

In fact, it has been suggested that learned optimizers could be a source of alignment drift in the development of Artificial General Intelligence (AGI) – leading to AGI that does not perform as its creators hoped [ 47 ] . While we do not feel that is an immediate danger from the present work, it is a consideration that should be kept in mind as learned optimizers become increasingly powerful.

## References

[1] Alex Krizhevsky, Ilya Sutskever, and Geoffrey E Hinton. Imagenet classification with deep convolutional neural networks. In Advances in neural information processing systems , pages 1097–1105, 2012.

[2] Christopher Berner, Greg Brockman, Brooke Chan, Vicki Cheung, Przemysław Dębiak, Christy Dennison, David Farhi, Quirin Fischer, Shariq Hashme, Chris Hesse, et al. Dota 2 with large scale deep reinforcement learning. arXiv preprint arXiv:1912.06680 , 2019.

[3] Oriol Vinyals, Igor Babuschkin, Junyoung Chung, Michael Mathieu, Max Jaderberg, Wojciech M Czarnecki, Andrew Dudzik, Aja Huang, Petko Georgiev, Richard Powell, et al. Alphastar: Mastering the real-time strategy game starcraft ii. DeepMind blog , page 2, 2019.

[4] Chris Piech, Jonathan Bassen, Jonathan Huang, Surya Ganguli, Mehran Sahami, Leonidas J Guibas, and Jascha Sohl-Dickstein. Deep knowledge tracing. In Advances in neural information processing systems , pages 505–513, 2015.

[5] Dami Choi, Christopher J Shallue, Zachary Nado, Jaehoon Lee, Chris J Maddison, and George E Dahl. On empirical comparisons of optimizers for deep learning. arXiv preprint arXiv:1910.05446 , 2019.

[6] Christian Daniel, Jonathan Taylor, and Sebastian Nowozin. Learning step size controllers for robust neural network training. In Thirtieth AAAI Conference on Artificial Intelligence , 2016.

[7] Chang Xu, Tao Qin, Gang Wang, and Tie-Yan Liu. Reinforcement learning for learning rate control. arXiv preprint arXiv:1705.11159 , 2017.

[8] Zhen Xu, Andrew M Dai, Jonas Kemp, and Luke Metz. Learning an adaptive learning rate schedule. arXiv preprint arXiv:1909.09712 , 2019.

[9] Marcin Andrychowicz, Misha Denil, Sergio Gomez, Matthew W Hoffman, David Pfau, Tom Schaul, and Nando de Freitas. Learning to learn by gradient descent by gradient descent. In Advances in Neural Information Processing Systems , pages 3981–3989, 2016.

[10] Olga Wichrowska, Niru Maheswaranathan, Matthew W Hoffman, Sergio Gomez Colmenarejo, Misha Denil, Nando de Freitas, and Jascha Sohl-Dickstein. Learned optimizers that scale and generalize. International Conference on Machine Learning , 2017.

[11] Kaifeng Lv, Shunhua Jiang, and Jian Li. Learning gradient descent: Better generalization and longer horizons. arXiv preprint arXiv:1703.03633 , 2017.

[12] Luke Metz, Niru Maheswaranathan, Brian Cheung, and Jascha Sohl-Dickstein. Learning unsupervised learning rules. arXiv preprint arXiv:1804.00222 , 2018.

[13] Luke Metz, Niru Maheswaranathan, Jonathon Shlens, Jascha Sohl-Dickstein, and Ekin D Cubuk. Using learned optimizers to make models robust to input noise. arXiv preprint arXiv:1906.03367 , 2019a.

[14] Luke Metz, Niru Maheswaranathan, Jeremy Nixon, Daniel Freeman, and Jascha Sohl-Dickstein. Understanding and correcting pathologies in the training of learned optimizers. In International Conference on Machine Learning , pages 4556–4565, 2019b.

[15] Keren Gu, Sam Greydanus, Luke Metz, Niru Maheswaranathan, and Jascha Sohl-Dickstein. Meta-learning biologically plausible semi-supervised update rules. bioRxiv , 2019.

[16] Luke Metz, Niru Maheswaranathan, Ruoxi Sun, C Daniel Freeman, Ben Poole, and Jascha Sohl-Dickstein. Using a thousand optimization tasks to learn hyperparameter search strategies. arXiv preprint arXiv:2002.11887 , 2020.

[17] M Levin T Hart and Mike Levin. Ai memo 39-the new compiler. Technical report, Technical report, MIT, 1962.

[18] Luca Franceschi, Paolo Frasconi, Saverio Salzo, and Massimilano Pontil. Bilevel programming for hyperparameter optimization and meta-learning. arXiv preprint arXiv:1806.04910 , 2018.

[19] Yuhuai Wu, Mengye Ren, Renjie Liao, and Roger B Grosse. Understanding short-horizon bias in stochastic meta-optimization. pages 478–487, 2016.

[20] Ingo Rechenberg. Evolutionsstrategie–optimierung technisher systeme nach prinzipien der biologischen evolution. 1973.

[21] Paul Vicol and et. al. Persisted evolutionary strategies. In Preparation , 2020.

[22] Kaiming He, Xiangyu Zhang, Shaoqing Ren, and Jian Sun. Deep residual learning for image recognition. In Proceedings of the IEEE conference on computer vision and pattern recognition , pages 770–778, 2016a.

[23] Ashish Vaswani, Noam Shazeer, Niki Parmar, Jakob Uszkoreit, Llion Jones, Aidan N Gomez, Łukasz Kaiser, and Illia Polosukhin. Attention is all you need. In Advances in neural information processing systems , pages 5998–6008, 2017.

[24] Barret Zoph, Vijay Vasudevan, Jonathon Shlens, and Quoc V Le. Learning transferable architectures for scalable image recognition. Proceedings of the IEEE conference on computer vision and pattern recognition , 2018.

[25] Sepp Hochreiter and Jürgen Schmidhuber. Long short-term memory. Neural computation , 9(8):1735–1780, 1997.

[26] Junyoung Chung, Caglar Gulcehre, KyungHyun Cho, and Yoshua Bengio. Empirical evaluation of gated recurrent neural networks on sequence modeling. arXiv preprint arXiv:1412.3555 , 2014.

[27] Yann LeCun. The mnist database of handwritten digits. http://yann. lecun. com/exdb/mnist/ , 1998.

[28] George Papamakarios, Theo Pavlakou, and Iain Murray. Masked autoregressive flow for density estimation. In Advances in Neural Information Processing Systems , pages 2338–2347, 2017.

[29] Diederik P Kingma and Max Welling. Auto-encoding variational bayes. arXiv preprint arXiv:1312.6114 , 2013.

[30] Tijmen Tieleman and Geoffrey Hinton. Lecture 6.5-rmsprop: Divide the gradient by a running average of its recent magnitude. COURSERA: Neural networks for machine learning , 4(2):26–31, 2012.

[31] Diederik P Kingma and Jimmy Ba. Adam: A method for stochastic optimization. arXiv preprint arXiv:1412.6980 , 2014.

[32] Timothy Dozat. Incorporating nesterov momentum into adam. 2016.

[33] Ilya Loshchilov and Frank Hutter. Decoupled weight decay regularization. arXiv preprint arXiv:1711.05101 , 2017.

[34] Ilya Loshchilov and Frank Hutter. Sgdr: Stochastic gradient descent with warm restarts. arXiv preprint arXiv:1608.03983 , 2016.

[35] Prabhu Teja Sivaprasad, Florian Mai, Thijs Vogels, Martin Jaggi, and François Fleuret. On the tunability of optimizers in deep learning. arXiv preprint arXiv:1910.11758 , 2019.

[36] Kaiming He, Xiangyu Zhang, Shaoqing Ren, and Jian Sun. Identity mappings in deep residual networks. In European conference on computer vision , pages 630–645. Springer, 2016b.

[37] Alex Krizhevsky, Vinod Nair, and Geoffrey Hinton. Cifar-10 and cifar-100 datasets. URl: https://www. cs. toronto. edu/kriz/cifar. html , 6, 2009.

[38] Olga Russakovsky, Jia Deng, Hao Su, Jonathan Krause, Sanjeev Satheesh, Sean Ma, Zhiheng Huang, Andrej Karpathy, Aditya Khosla, Michael Bernstein, Alexander C. Berg, and Li Fei-Fei. ImageNet Large Scale Visual Recognition Challenge. International Journal of Computer Vision (IJCV) , 115(3):211–252, 2015. doi: 10.1007/s11263-015-0816-y .

[39] Jacob Devlin, Ming-Wei Chang, Kenton Lee, and Kristina Toutanova. Bert: Pre-training of deep bidirectional transformers for language understanding. arXiv preprint arXiv:1810.04805 , 2018.

[40] Noam Shazeer and Mitchell Stern. Adafactor: Adaptive learning rates with sublinear memory cost. arXiv preprint arXiv:1804.04235 , 2018.

[41] Travis E Oliphant. A guide to NumPy , volume 1. Trelgol Publishing USA, 2006.

[42] Stefan Van Der Walt, S Chris Colbert, and Gael Varoquaux. The numpy array: a structure for efficient numerical computation. Computing in Science & Engineering , 13(2):22, 2011.

[43] Charles R Harris, K Jarrod Millman, Stéfan J van der Walt, Ralf Gommers, Pauli Virtanen, David Cournapeau, Eric Wieser, Julian Taylor, Sebastian Berg, Nathaniel J Smith, et al. Array programming with numpy. Nature , 585(7825):357–362, 2020.

[44] Michael Waskom and the seaborn development team. mwaskom/seaborn, September 2020. URL https://doi.org/10.5281/zenodo.592845 .

[45] J. D. Hunter. Matplotlib: A 2d graphics environment. Computing in Science & Engineering , 9(3):90–95, 2007. doi: 10.1109/MCSE.2007.55 .

[46] Emma Strubell, Ananya Ganesh, and Andrew McCallum. Energy and policy considerations for deep learning in nlp. arXiv preprint arXiv:1906.02243 , 2019.

[47] Evan Hubinger, Chris van Merwijk, Vladimir Mikulik, Joar Skalse, and Scott Garrabrant. Risks from learned optimization in advanced machine learning systems. arXiv preprint arXiv:1906.01820 , 2019.

[48] Irwan Bello, Barret Zoph, Vijay Vasudevan, and Quoc Le. Neural optimizer search with reinforcement learning. 2017. URL https://arxiv.org/pdf/1709.07417.pdf .

[49] Samy Bengio, Yoshua Bengio, Jocelyn Cloutier, and Jan Gecsei. On the optimization of a synaptic learning rule. In Preprints Conf. Optimality in Artificial and Biological Neural Networks , pages 6–8. Univ. of Texas, 1992.

[50] Thomas Philip Runarsson and Magnus Thor Jonsson. Evolution and design of distributed learning rules. In Combinations of Evolutionary Computation and Neural Networks, 2000 IEEE Symposium on , pages 59–63. IEEE, 2000.

[51] Yoshua Bengio, Nicolas Boulanger-Lewandowski, and Razvan Pascanu. Advances in optimizing recurrent networks. In 2013 IEEE International Conference on Acoustics, Speech and Signal Processing , pages 8624–8628. IEEE, 2013.

[52] Alex Graves, Greg Wayne, and Ivo Danihelka. Neural turing machines. arXiv preprint arXiv:1410.5401 , 2014.

[53] Jorge Nocedal. Updating quasi-newton matrices with limited storage. Mathematics of computation , 35(151):773–782, 1980.

[54] Dong C Liu and Jorge Nocedal. On the limited memory bfgs method for large scale optimization. Mathematical programming , 45(1-3):503–528, 1989.

[55] Nicolas Heess, Srinivasan Sriram, Jay Lemmon, Josh Merel, Greg Wayne, Yuval Tassa, Tom Erez, Ziyu Wang, SM Eslami, Martin Riedmiller, et al. Emergence of locomotion behaviours in rich environments. arXiv preprint arXiv:1707.02286 , 2017.

[56] Karl Cobbe, Oleg Klimov, Chris Hesse, Taehoon Kim, and John Schulman. Quantifying generalization in reinforcement learning. arXiv preprint arXiv:1812.02341 , 2018.

[57] Bobak Shahriari, Kevin Swersky, Ziyu Wang, Ryan P Adams, and Nando De Freitas. Taking the human out of the loop: A review of bayesian optimization. Proceedings of the IEEE , 104(1):148–175, 2015.

[58] Daniel Golovin, Benjamin Solnik, Subhodeep Moitra, Greg Kochanski, John Karro, and D Sculley. Google vizier: A service for black-box optimization. In International Conference on Knowledge Discovery and Data Mining , 2017.

[59] Ke Li and Jitendra Malik. Learning to optimize. International Conference on Learning Representations , 2017a.

[60] Ke Li and Jitendra Malik. Learning to optimize neural nets. arXiv preprint arXiv:1703.00441 , 2017b.

[61] John Schulman, Filip Wolski, Prafulla Dhariwal, Alec Radford, and Oleg Klimov. Proximal policy optimization algorithms. arXiv preprint arXiv:1707.06347 , 2017.

[62] Jan Peters, Katharina Mulling, and Yasemin Altun. Relative entropy policy search. In Twenty-Fourth AAAI Conference on Artificial Intelligence , 2010.

[63] Yoshua Bengio. Gradient-based optimization of hyperparameters. Neural computation , 12(8):1889–1900, 2000.

[64] Atilim Gunes Baydin and Barak A Pearlmutter. Automatic differentiation of algorithms for machine learning. arXiv preprint arXiv:1404.7456 , 2014.

[65] Dougal Maclaurin, David Duvenaud, and Ryan Adams. Gradient-based hyperparameter optimization through reversible learning. In International Conference on Machine Learning , pages 2113–2122, 2015.

[66] Paul J Werbos. Backpropagation through time: what it does and how to do it. Proceedings of the IEEE , 78(10):1550–1560, 1990.

[67] Corentin Tallec and Yann Ollivier. Unbiasing truncated backpropagation through time. arXiv preprint arXiv:1705.08209 , 2017.

[68] Chelsea Finn, Pieter Abbeel, and Sergey Levine. Model-agnostic meta-learning for fast adaptation of deep networks. arXiv preprint arXiv:1703.03400 , 2017.

[69] Alex Nichol, Joshua Achiam, and John Schulman. On first-order meta-learning algorithms. arXiv preprint arXiv:1803.02999 , 2018.

[70] Barak Pearlmutter. An investigation of the gradient descent process in neural networks . PhD thesis, Carnegie Mellon University Pittsburgh, PA, 1996.

[71] LA Rastrigin. About convergence of random search method in extremal control of multi-parameter systems. Avtomat. i Telemekh , 24(11):1467–1473, 1963.

[72] Yurii Nesterov and Vladimir Spokoiny. Random gradient-free minimization of convex functions. Technical report, Université catholique de Louvain, Center for Operations Research and Econometrics (CORE), 2011.

[73] Krzysztof Choromanski, Mark Rowland, Vikas Sindhwani, Richard E Turner, and Adrian Weller. Structured evolution with compact architectures for scalable policy optimization. arXiv preprint arXiv:1804.02395 , 2018.

[74] Tim Salimans, Jonathan Ho, Xi Chen, Szymon Sidor, and Ilya Sutskever. Evolution strategies as a scalable alternative to reinforcement learning. arXiv preprint arXiv:1703.03864 , 2017.

[75] Niru Maheswaranathan, Luke Metz, George Tucker, Dami Choi, and Jascha Sohl-Dickstein. Guided evolutionary strategies: Augmenting random search with surrogate gradients. In International Conference on Machine Learning , pages 4264–4273. PMLR, 2019.

[76] Sanjay Ghemawat, Howard Gobioff, and Shun-Tak Leung. The google file system. In Proceedings of the nineteenth ACM symposium on Operating systems principles , pages 29–43, 2003.

[77] Martín Abadi, Paul Barham, Jianmin Chen, Zhifeng Chen, Andy Davis, Jeffrey Dean, Matthieu Devin, Sanjay Ghemawat, Geoffrey Irving, Michael Isard, et al. Tensorflow: A system for large-scale machine learning. In OSDI , volume 16, pages 265–283, 2016.

## Appendix A Extended Related Work

We categorize progress in learned learned optimizers into three categories: parameterizations, data distributions, and outer-training methodology. We include a review of these previous efforts herein.

### A.1 Parameterizations

Broadly, authors attack the problem of learned optimization at a high level using different parameterizations. We review these different choices below.

#### A.1.1 Controller based parameterization

One class of learned optimizer parameterizes some function, usually as a neural network, that returns hyperparameters for an existing hand designed method. These methods impose a strong inductive bias. All inner-learning must be done via manipulation of existing methods. By enforcing a constrained structure, these method limit the types of learning rules expressible. This limitation does inject strong priors into the model making both outer optimization easier, as well as produce better outer-generalization. These methods often additionally make use off derived features from the currently training model. These features include things like loss values, variance of function evaluations, and variance of weight matrices.

There are a number of existing works that explore different types of features and architectures. Daniel et al. [6] explores using a simple, linear policy which maps from hand designed features to log learning rate which is then used with SGD, RMSProp or momentum. Xu et al. [7] learns a small LSTM network with inputs of current training loss, and predicts a learning rate for SGD. Xu et al. [8] uses an LSTM or an MLP with features computed during training and outputs a scalar which is multiplied by the previous learning rate.

#### A.1.2 Symbolic parameterizations

Existing learning rules are often symbolic in nature. All first order optimizers used today are symbolic and expressible by a small collection of mathematical operations. Bello et al. [48] take inspiration from this and also parameterize optimizers as collections of mathematical primitives. This parameterization can lead to interpretable optimizers. For example, Bello et al. [48] show common subpatterns discovered based on multiplication of the sign of the gradient and sign of the momentum value. Not all computations lend themselves to a symbolic regression. Finding symbolic formula to solve increasingly more difficult tasks starts to resemble program synthesis which is notoriously difficult.

#### A.1.3 Continuous parameterizations

The last family of parameterization is based on continuously parameterized function approximations. Older work often makes use of simple / linear combinations of features while more recent work makes use of neural networks. There are a few classes of update rule parameterizations.

Bengio et al. [49] proposes a 7 parameter, and 16 parameter update rule parameterized by mixing various biologically inspired learning signals. Runarsson and Jonsson [50] use a simple continuous parameterization that operates on error signals and produces changes in inner-parameters.

Recently, there has been renewed interest in learned optimizers, in particular using neural network paramerizations of the learning rules. Andrychowicz et al. [9] makes use of an LSTM [ 25 ] possibly with global average pooling to enable concepts like ℓ 2 \ell_{2} gradient clipping to be implemented [ 51 ] . They also explore Neural Turing Machine [ 52 ] like parameterizations specifically designed for low rank memory updates so that it can learn algorithms like LBFGS [ 53 , 54 ] . In contrast, Metz et al. [14] makes use of a per-parameter MLP instead of the LSTM.

One critical design choice when designing neural network parameterized learned optimizers is input features. When training neural network models it is critical that the inputs be similar scales to aide in optimization. Andrychowicz et al. [9] trains on raw gradients which are scaled by either decomposing each scalar into a sign and a magnitude before feeding into an LSTM. Lv et al. [11] uses the gradient and momentum normalized by the rolling average of gradients squared (similar to the rescaling done by Adam). Wichrowska et al. [10] also makes use of momentum except using multiple timescales normalized in a similar way. In addition to these momentum terms, Metz et al. [14] other features such as weight value and additionally applies a normalization based on the second moment of features.

In [ 9 , 11 , 12 ] all methods employ a per-parameter update. The updates are independent of the number of parameters 1 1 1 [ 14 ] uses normalization across parameters so this is not strictly true . While expressive, this is expensive as no computation can be shared. Wichrowska et al. [10] improve upon this by additionally having per-layer, and a global LSTM.

When designing learned optimizer architectures, there are a number of design decisions to keep in mind. One must balance compute cost of the learned optimizer with expressibility. Often this shifts models to be considerably smaller than those used in supervised learning. Wichrowska et al. [10] , for example makes use of a 8-hidden unit LSTM per-parameter. Selection of features to feed into the learned optimizer is also critical. While traditionally deep learning involves learning every feature, this learning comes at the cost of increased compute which is often not feasible.

### A.2 Data distribution of tasks

There is no agreed upon standards when defining datasets for training learned optimizers. The community is adhoc, training on what ever dataset is available or what ever best suites the goals (training a particular model, creating more general optimizers). Constructing large distributions of tasks is labor intensive and thus not often done.

Metz et al. [14] draws inspiration from the few shot learning literature and constructs 10 way classification problems sampling from different classes on imagenet.

Wichrowska et al. [10] leverages a large distribution of synthetic tasks. These tasks are designed to represent different types of loss surfaces that might be found in loss surfaces.

TaskSet, [ 16 ] is a dataset of tasks specifically designed for learned optimizer research. We use this dataset throughout our work.

There is a balance between performance of the tasks, and ability to outer-train. Selecting the types of problems we want to train on is often not enough. Additionally, outer-training on the closest task possible will not produce the best optimizer nor even converge. Training on distributions with increased variation smooths the outer-loss surface and makes exploration simpler. This mirrors phenomena found in RL [ 55 , 56 ] .

### A.3 Outer-Optimization methods

The outer-optimization problem consists of finding a particular set of weights, or configuration of a learned optimizer. A number of different strategies have been proposed.

#### A.3.1 Hyper parameter optimization

One of the most common outer-learning methods used is hyper-parameter optimization. In the context of learning optimizers, this can be seen as finding optimizer hyper parameters, e.g. learning rate, over a particular task instance. Numerous methods exist to do this ranging from Bayesian hyper parameter optimization [ 57 ] , to grid search, to genetic algorithms. See Golovin et al. [58] for a more complete description.

The types of outer-learning problems encountered in learned optimizers is different in that the evaluation function is often an expectation over some distribution. Additionally, the amount of outer-parameters is often larger than simply finding a few hyperparameters. Never the less, we include this here to show the similarity to learned optimizer research.

#### A.3.2 Reinforcement learning

Learned optimizers can naturally be cast into a sequential decision process. The state of the system consists of the inner-parameter values, action space is the steps taken, and the reward is achieving a low loss in the future. A number of works have thus taken this viewpoint. Li and Malik [59] , Li and Malik [60] makes use of the guided policy search algorithm. Xu et al. [8] uses PPO Schulman et al. [61] , Daniel et al. [6] make use of Relative Entropy Policy Search [ 62 ] . The exact algorithm used is a function of the underlying parameterization.

#### A.3.3 Neural Architecture Search Style

Instead of learning the policy directly, Bello et al. [48] makes use of reinforcement learning (PPO [ 61 ] to learn a controller which produces the symbolic learned optimizer. This is distinct from § A.3.2 as it does not leverage the sequential nature of the inner problem. Instead, it treats the environment as a bandit problem.

#### A.3.4 Backpropogation / Gradient based

Gradient based methods leverage local perturbations in parameter space. Computing derivatives through leaning procedures has been explored in the context of hyperparameter optimization in [ 63 , 64 , 65 ] . Andrychowicz et al. [9] was the first to make use of gradient based learning for this application.

To train a learned optimizer, ideally, one would compute the derivative of the entire training run with respect to optimizer parameters. This is often referred to as unrolling the entire training procedure into one large graph then running reverse mode automatic differentiation on this. Not only is this often too expensive to do in practice, the resulting loss surface can be poorly conditioned [ 14 ] . As such approximations are often made.

One common family of approximation is based on truncated backpropogation through time. The core idea is to break apart long unrolled computations into shorter sequences and thus not propagating any error back through the entire unrolled computation graph pieces [ 66 , 67 ] . This approximation is used widely in neural network parameterized learned optimizers [ 9 , 10 , 11 , 14 ] . Unlike in language modeling, truncated backprop has been shown to lead to dramatically worse solutions for meta-learning applications [ 19 , 14 ] .

A second family of approximations involve first order gradient calculations. Andrychowicz et al. [9] does use the first order gradient calculation where as subsequent work, [ 10 ] does and computes the full gradient. The trade offs between these two gradient estimators has been discussed in the few shot learning literature in the context of MAML / Reptile [ 68 , 69 ] .

Computing gradients through iterative, non-linear, dynamics has been shown to cause chaotic dynamics. Pearlmutter [70] , Maclaurin et al. [65] showed high sensitivity to learning rate with respect to performance after multiple steps of unrolled optimization. Metz et al. [14] shows this issue for neural network parameterized learned optimizers and proposes a solution based on variational optimization and multiple gradient estimators.

Despite improvements, there are a lot of considerations that must be taken into account for doing gradient based training.

#### A.3.5 Evolutionary Strategies

A alternative way to estimate gradients is to use black box method such as Evolutionary Strategies [ 71 , 20 , 72 , 73 , 74 ] . These methods are memory efficient, requiring no storage of intermediate states, but can suffer from high variance. In the case of learned optimizer optimization, however, these methods can result in lower variance gradient estimators [ 14 ] . Hybrid approaches that leverage both gradients and ES have been such as Guided ES [ 75 ] have also been proposed for meta-optimization. This work leverages one of the simplest forms of evolutionary strategies as described in [ 74 ] which uses a fixed standard deviation.

## Appendix B Outer Optimization Details

In this work, as with Metz et al. [12] , we use asynchronous, batched training. Each task has a different complexity, thus will produce outer-gradient estimates at a different rate. We use asyncronous minibatched training as synchronous training with these heterogenious workloads would be too slow and wasteful. We tie the outer batch size to the number of workers. To prevent stale gradients, we additionally throw away all outer-gradient estimates that are from more than five outer-iterations away from the current weights.

We optimize all models with Adam. We sweep learning rates between 3e-5 and 3e-3 for all experiments. We find the optimal learning rate is very sensitive and changes depending on how long outer-training occurs. We have preliminary explorations into learning rate schedules but have not yet been able to improve on this constant schedule. For all outer-training experiments, we always run more than one random seed. Due to the relatively small number of units, and biased gradient estimators, performance is dependant on random seed. For all experiments we use gradient clipping of 0.1 applied to each weight independently. Without this clipping no training occurs. This surprises us as our gradient estimator is evolutionary strategies which will not typically have exploding gradients. Upon further investigation, however, the outer-gradient variance is much larger without this clipping.

When computing outer-gradients, we follow [ 14 ] and compute a outer-loss based on multiple mini batches of data. In our work we use 5. Note inner-training always uses a single minibatch of inner-training data as well as a single batch of inner-validation data when used.

We first train with 240-360 length unrolls over a max of 10k inner-steps. While training we logged out 10k length unrolls from 100 tasks sampled from the outer-training distribution and saved outer-parameters every hour. While training we monitor performance across all outer-learning rates and all seeds on the outer-training distribution. When training plateaus, we manually look through these evaluations and select a candidate set of optimizers to further train with an increasing truncation schedule. Not all optimizers fine tune in the same way despite having the same performance on the outer-training data so selecting more than one is critical. At this point we are unsure where this phenomenon comes from.

Next we fine tune theses models in an unbiased fashion. We explored two methods. First, based on an increasing truncation schedule. We tested linearly increasing truncation length from 300-10k steps over the course of 30k or 10k steps. We find the faster increase, 10k steps, performs best. Second, we explored fine tuning with Persisted Evolutionary Strategies – an unbiased gradient estimator [ 21 ] . We found this achieved similar final performance but achieved it in half the time. When fine tuning we also make use of different learning rates. We find higher learning rates make progress faster, but can be unstable in that the performance varies as a function of outer-training step. Additionally, the learning rate chosen depends on the learning rate used previously in the first training phase. Before finetuning, we ‘warm up’ the Adam internal rolling statistics. While this might not be strictly required, it ensures that there is no decrease in performance early in outer-training. This can be done by simply setting the outer-learning rate to zero for the first 300 outer-iterations.

## Appendix C Learned Optimizer Architecture Details

In this section we describe the detailed learned optimizer architecture. For ease of understanding we opt to show a mix of pseudo-code based on python and textual descriptions as opposed to mathematical expressions. Finally we chose to describe our optimizer as a series of stateless and pure functions for clarity.

We used this architecture for all of our experiments except of Fig 2 b which used an older version of the architecture with additional features which where dropped from the final version.

### C.1 High level structure of the optimizer

The learned optimizer has two main components: a function that maps from some set of inputs, a state, and parameters to some new state and new parameters. ⬇

And a function to produce an initial state from the given inner-parameters.

Parameters are stored as a dictionary of different tensors keyed by name.

For convenience, we also define gradients to be the same type as Params:

The state consists of multiple values that we will discuss in detail further. For now, however, we list the full state with high level comments. ⬇

Both from_lstm_size, from_mlp_size are hyper parameters set as part of the learned optimizer to control how much information is sent from the MLP or from the LSTM.

The input to the next_state function consists of inner-gradients, computed on a inner-training batch of data, as well as optionally validation data which is passed in every 10 iterations. We choose to not pass in validation data every steps for computational efficiency. ⬇

Each task specifies a function that samples parameter initialization, as well as to produce outputs. ⬇

For outer-training each task also includes a second loss function which computes the task’s loss on the outer-validation split of data. Note this uses a different validation set of data than the previous function.

Inner training / application of the learned optimizer looks like: ⬇

Computing the outer objective and outer-gradients from inner-initialization looks like the following: ⬇

### C.2 Utilities / components

First we will describe the individual components and utilities used, then we will go on to describe the full update function.

#### C.2.1 Rolling Features

These are a moving average of gradients and second moments computed similarly to Adam / RMSProp. The rolling state consists of tensors containing momentum values (ms) and second moment values (rms):

⬇

The Text represent names that map to the tensor of the corresponding shape from the parameters. The values are the same shape as the corresponding inner-parameter with an additional axis appended to keep track of multiple different decay values. While its possible to outer-learn these values, we fix them at 0.5, 0.9, 0.99, 0.999, 0.9999.

To update these we construct a helper class. ⬇

We define an initial value which is simply simply zeros: ⬇

To update these values we follow a procedure similar to RMSProp update equations: ⬇

#### C.2.2 LossAccum

This represents how we get loss information into our learned optimizer. Loss values have no pre-determined scale and span many orders of magnitude. As such, we must somehow standardize them so that the inputs are bounded and able to be easily used by neural networks. We get around this by keeping track of the normalized mean and variance of the mini-batch losses.

⬇

The class that manages these states is parameterized by the decay of the rolling window.

⬇

The initial state is simply zeros.

⬇

To compute updates we do rolling mean and variance computations. ⬇

Two additional functions are used to normalize loss values for use in neural networks. First, we have a “corrected” mean (similar to what is done by Adam) for a given AccumState. ⬇

Second, we have a function that weights one loss by a different AccumState. This is eventually used to weight the validation loss accum against the training loss state allowing the learned optimizer to detect overfitting.

⬇

#### C.2.3 RollingClipState

Gradient clipping is a often used technique in deep learning. We found large benefits by applying some form of learned clipping (clipping inner-gradient values) in our learned optimizer. We cannot simply select a default value because gradient norms vary across problem. As such we meta-learn pieces of a dynamic gradient clipping algorithm. This is our first iteration of this concept and we expect large gains can be obtained with a better scheme.

This algorithm is stateful thus also needs some state container.

⬇

This class is parameterized by the decay constant of the rolling average and the multiplier to determine when clipping should start. Both of these values are outer-learned with the rest of the learned optimizer.

⬇

The initial states are initialized to 1. ⬇

We provide a normalization function that both updates the RollingClipState and provides clipped gradients. ⬇

### C.3 Learned optimizer specific / putting it all together

The learned optimizer has two main components. The first is the Optimizer class that manages everything surrounding inner-learning. This function has no learnable outer-parameters. The second is what we call “theta_mod” which contains all of the outer-variables and functions that we are learning.

First we construct the optimizer class with the corresponding theta_mod (see bellow). ⬇

Next the rolling features at fixed, hard coded intervals. These could be outer-learned but in this work they are fixed. ⬇

Then the the loss features for use with both training and validation loss. We use a lower decay constant on the validation as it is updated less frequently (once every 10 steps). Once again these could be outer-learned but in this work we leave them fixed. ⬇

Finally we construct the gradient clipping utility. Unlike the previous parameters, we do outer-learn these and pass in two variables off of the ‘theta_mod’. ⬇

Next, we need an initial state for the optimizer defined in C.1 . This mostly consists of obtaining initial states from the various components of the learned optimizer.

⬇

Next we look to the update performed. We split up into two components – first a validation state, and second a training state.

⬇

The validation update simply consists of updating the two components that make use of the loss value. ⬇

The the function applied to the training gradients is much more complicated. Much like the validation features it updates the various rolling statistics including the two loss data structures, the rolling momentum / rms terms, as well as the gradient clipping state. ⬇

Next, a sequence of features related to loss values are computed. ⬇

Next we call into the learned optimizer function in “theta_mod” which does the bulk of the computation. ⬇

We then populate the next state with all the outputs. ⬇

### C.4 “ThetaMod”: The learned optimizer outer-parameters

All of the meta-learned outer-parameters are stored in a class called ThetaMod. Its constructor defines various dimensions of the different Sonnet modules.

⬇

This constructor creates a shared sonnet module for the per layer LSTM. This is constructed here as it is needed in more than one method.

Second, we construct the per parameter feed forward network. This is a tiny network that operates on each parameter. It outputs two values for producing a step, then from_mlp_size more values which are fed back into the LSTM.

Third, we construct two linear projections that map from the RNN output to either the per parameter feed forward network, or back to the global features.

Finally, we initialize the two variables used by the rolling gradient clipping terms. We parameterize these variables on a log scale (possibly subtracting 1) so as to roughly match the scaling of the other neural network weights.

⬇

The heart of this function takes the features passed in from the optimizer, applies some neural network based learning algorithm, then produces the next weight value as well as various pieces of hidden information for the next iteration. ⬇

We first compute the global feature vector. These consist of features related to the loss curves, as well as the aggregated data from the previous LSTM execution. These features form a rank 1 tensor. ⬇

Next we compute the per tensor features. This is a rank two tensor, consisting of the number of tensors, and a feature dimension. ⬇

We tile the global features to be num tensors by num global features then concat these to the per tensor features and pass them into the per layer LSTM. ⬇

We then linearly project the LSTM outputs to be input to the per parameter feed foward network, and unstack them to form a a list of rank 1 features – one per tensor.

⬇

Next we iterate over each parameter, and first compute per parameter features. The per parameter features consist of gradients, parameter values, parameter values 100 steps in the past, momentum values, second moment values, activations from the per tensor LSTM. Additionally there are two global features included: the training step and the number of tensors total. Two empty lists are initialized to accumulate results. ⬇

We pass these per parameter features through these features into a per parameter MLP which produces a single output.

We split this output into three pieces: A direction, a magnitude, and features which are be fed back to the per tensor LSTM after being reduced along the parameter dimension. ⬇

A step can then be computed by exponentiating the magnitude and multiplying by a direction. Rescaling these quantities is critical. Without this rescaling, the magnitude of the updates is extremely large, resulting in chaotic training dynamics which makes outer-learning difficult.

We then subtract step from the previous parameter value. While it is possible just to predict a new parameter directly, learning deltas is significantly easier to learn and results in much more stable training.

Finally, we collect all the information needed to be returned from the per parameter LSTM and output. ⬇

With the for loop over, we then return the necessary info. Before this, however, we must aggregate information from the per tensor LSTM to be able to pass it to the next layer’s global features after applying a linear projection from the LSTM output and reducing along the tensor dimension.

⬇

Now we will discuss the different features methods. First, computing the global features. ⬇

This function simply returns the concatenation of the Two loss features, and the aggregated features from the per layer lstm.

Next we look to the per tensor features. We return a 2D tensor with the leading dimension a “batch size” being the number of tensors, and the second dimension representing the feature dimension.

⬇

We compute a large number of features. At this point have not extensively ablated each one and we expect many are duplicate or unneeded. Before we begin listing features, however, we make use of a helper function that computes the clipped log abs of tensors.

⬇

We begin by iterating over each tensor.

⬇

First, we compute features based on the rolling momentum values. We compute features that represent the log magnitude, the sign, and the log variance. ⬇

We compute a similar set of features for the second moment features. ⬇

A similar set for the inner-parameters: ⬇

Next we include the magnitude of the weight norm.

As well as the gradient norm:

Next we add a feature if the tensor is a scalar or not. ⬇

The shape of the underlying tensor is also a useful feature. The length of this shape varies though depending on the rank. As such we first pad the tensor to be at least rank 4 and then pass the log shape shifted by -1. This shift is to keep this value roughly zero mean.

⬇

The features from the previous execution’s MLP are included. These are to enable communication back from the MLP to the per layer network.

This dictionary of features is then flattened (adding appropriate dimensions if needed) and appended to the list of inputs. ⬇

Once the stacked_inputs is filled, we zip and stack and concat the values forming a number of layers by number of features tensor. ⬇

The last set of features is the per parameter features. ⬇

Many of these inputs are of the shape of the underlying tensor. Because many of these operations are per parameter we construct a flat version of all of these.

⬇

As with the per layer features, we add a series of features. First we add raw features for the gradients, parameter values, momentum, and second moment accumulators, and past weights. ⬇

We then add some derived features such as the log abs parameter value:

Finally we add terms based on the rsqrt of the second moment terms inspired by how Adam normalizes. ⬇

These values are concatenated and normalized by a second moment normalizer computed across the num tensor dimension. We additionally clip the output of this normalizer. This is crucial for stable training as some of these features will produce large magnitudes in some channels.

⬇

Next, we embed the current inner-training step with sinusoids of different frequencies.

⬇

We compute a features based on the number of tensors: ⬇

As well as features about the number of parameters in the current tensor: ⬇

Next, we compute some statistics about the log norm of the weight matrix: ⬇

Next, we tile the input from the LSTM so as to add a number of parameters dimension. ⬇

Finally we concat and return all these features. ⬇

We have discussed how new values of LSTM hidden state, activations from the LSTMs, and activations from the MLP are produced, but we have not yet shown the initial values. In all cases they are initialized from outer-parameterized values shown bellow. ⬇

## Appendix D Adam8p

This matches the adam8p optimizer described in [ 16 ] . The eight hyper-parameters are: the learning rate, α \alpha , first and second moment momentum, β 1 \beta_{1} , β 2 \beta_{2} , the numerical stability term, ϵ \epsilon , ℓ 2 \ell_{2} and ℓ 1 \ell_{1} regularization strength, and learning rate schedule constants λ exp_decay \lambda_{\text{exp\_decay}} and λ linear_decay \lambda_{\text{linear\_decay}} .

ϕ ( 0 ) = \displaystyle\phi^{(0)}= problem specified random initialization (1) m ( 0 ) = \displaystyle m^{(0)}= 0 \displaystyle 0 (2) v ( 0 ) = \displaystyle v^{(0)}= 0 \displaystyle 0 (3) g ( t ) = \displaystyle g^{(t)}= d d ​ ϕ ( t ) ​ ( f ⁡ ( x , ϕ ( t ) ) + ℓ 2 ​ ‖ ϕ ( t ) ‖ 2 2 + ℓ 1 | | ϕ ( t ) | | 1 ) \displaystyle\frac{d}{d\phi^{(t)}}(f(x;\phi^{(t)})+\ell_{2}||\phi^{(t)}||^{2}_{2}+\ell_{1}||\phi^{(t)}||_{1}) (4) m ( t ) = \displaystyle m^{(t)}= β 1 ​ m ( t − 1 ) + g ( t ) ​ ( 1 − β 1 ) \displaystyle\beta_{1}m^{(t-1)}+g^{(t)}(1-\beta_{1}) (5) v ( t ) = \displaystyle v^{(t)}= β 2 ​ v ( t − 1 ) + ( g ( t ) ) 2 ​ ( 1 − β 2 ) \displaystyle\beta_{2}v^{(t-1)}+(g^{(t)})^{2}(1-\beta_{2}) (6) m ^ ( t ) = \displaystyle\hat{m}^{(t)}= m ( t ) 1 − β 1 t + 1 \displaystyle\dfrac{m^{(t)}}{1-\beta_{1}^{t+1}} (7) v ^ ( t ) = \displaystyle\hat{v}^{(t)}= v ( t ) 1 − β 2 t + 1 \displaystyle\frac{v^{(t)}}{1-\beta_{2}^{t+1}} (8) u ( t ) = \displaystyle u^{(t)}= m ^ ( t ) v ^ ( t ) + ϵ \displaystyle\dfrac{\hat{m}^{(t)}}{\sqrt{\hat{v}^{(t)}}+\epsilon} (9) s linear ( t ) = \displaystyle s_{\text{linear}}^{(t)}= max ​ ( 1 − t ​ λ linear_decay , 0 ) \displaystyle\text{max}(1-t\lambda_{\text{linear\_decay}},0) (10) s exp ( t ) = \displaystyle s_{\text{exp}}^{(t)}= exp ​ ( − t ​ λ exp_decay ) \displaystyle\text{exp}(-t\lambda_{\text{exp\_decay}}) (11) ϕ ( t + 1 ) = \displaystyle\phi^{(t+1)}= α ​ s linear ( t ) ​ s exp ( t ) ​ u ( t ) \displaystyle\alpha s_{\text{linear}}^{(t)}s_{\text{exp}}^{(t)}u^{(t)} (12)

We sample learning rate logritmically between 1e-8 and 10, beta1 and beta2 we parametrize as 1 − x 1-x and sample logrithmically between 1e-4 and 1 and 1e-6 and 1 respectively. For learning rate schedules we sample linear decay between 1e-7, 1e-4 logrithmically and exponential decay logrithmically between 1e-3, 1e-6. We sample both ℓ 1 \ell_{1} and ℓ 2 \ell_{2} logrithmcally between 1e-8, 1e1.

## Appendix E Performance Table

We show numerical performance measurements of our learned optimizer and baseline optimizers. Each value is the mean or median over 100 different inner-training tasks.

train test Optimizer mean median mean median learned 0.077325 0.024167 0.113242 0.028928 global adam lr (1 Trial) 0.226807 0.105513 0.261613 0.092532 global adam8p, RS (1 Trial) 0.240924 0.109519 0.257368 0.100959 global nadamw, RS (1 Trial) 0.215176 0.098448 0.229359 0.086703 per task adam lr (14 Trial) 0.150443 0.067373 0.152028 0.063194 per task opt_list (10 Trial) 0.082756 0.039647 0.086195 0.038541 per task opt_list (100 Trial) 0.041560 0.028851 0.047224 0.031042 per task opt_list (1k Trial) 0.039348 0.028254 0.043193 0.029897 per task adam8p (10 Trial) 0.278858 0.132965 0.264282 0.128594 per task adam8p (100 Trial) 0.095372 0.046926 0.107177 0.046672 per task adam8p (1k Trial) 0.044144 0.028692 0.060663 0.028813 per task adam8p + opt_list(2k Trial) 0.018403 0.023350 0.025419 0.025555

## Appendix F Experimental details for figures

### F.1 Outer training of different learned architectures

All models are trained with truncated evolutionary strategies using the parameters described in the main text. Instead of using the two stage schedule we only train with truncation’s of size 240-360. We use the same, fixed learning rate for the FF and LSTM_FF model of 0.000500. For LSTM we found a lower learning rate of 0.000100 to perform better. Ideally we would include an extensive hyperparameter comparison, but the computational cost is prohibitive.

For the FF model we make use of a two hidden layer 32 unit MLP. In addition to the features described in [ 14 ] we use RMS terms which improve performance over that reported in [ 14 ] by a small amount.

For the L2LBGDGD model we copy Andrychowicz et al. [9] using a two hidden layer, 20 unit GRU [ 26 ] with the same input gradient processing.

For the LSTM model, we make use of a model inspired by [ 9 ] . We make use of a 64 dimension LSTM hidden size to produce two outputs, a direction and a sign which are combined similar to [ 14 ] .

Performance on 100 tasks (each with five random seeds) is recorded over the course of training. We show an exponential moving average of this data in the figure.

### F.2 Outer training with different sized models

All models are trained with truncated evolutionary strategies using parameters described in the main text. Instead of using the two stage schedule we only train with truncation’s of size 240-360. We use a learning rate of 3 ∗ 10 − 3 3*10^{-3} for all models.

### F.3 Large scale transfer with Resnet models

We make use of two ResNetV2 models. Before applying the residual blocks, we pass the inputs through a 64 unit, 7x7 convolutional kernel with stride 2 followed by max pooling of size 3 with a stride of 2. This aggressive down sampling was originally designed for larger image models but was also left in despite our small sized models.

We then apply some number of residual blocks parameterized by a (number of output channels, number of bottleneck channels, stride).

At the output we apply batch norm, reduce over the spatial dimensions, and project to the the appropriate number of classes.

Our goal with these experiments are not to seek peak performance. Instead show that our learned optimizer is capable of generalizing to vastly different distributions of models.

##### CIFAR-10 Resnet

This model makes use of four residual blocks: [(128, 32, 1), (128, 32, 2), (128, 64, 1), (128, 64, 2)].

##### Imagenet Resnet

This model makes use of 11 residual blocks: [(128, 32, 1), (128, 32, 2), (256, 64, 1)*2, (256, 64, 2), (512, 128, 1)*3, (512, 128, 2), (1024, 256, 1)*2].

### F.4 Self optimization details

For our baseline learned optimizer trained with Adam, we search over two learning rates, 10 − 5 10^{-5} and 3 ∗ 10 − 3 3*10^{-3} and select the best one (1e-3) for the given 10k outer-training steps as well as selected the optimizer used to train the best optimizer (3e-5).

When training an optimizer with a new optimizer there are no hyper parameters. We found we must also include the original gradient clipping used for the Adam models (clipping all values between -0.1, 0.1). Without this, our learned optimizer is not able to make any progress. Understanding this is an interesting to us as we would have suspected the dynamic inner-clipping should have addressed this.

For technical reasons, the learned optimizer does not have easy access validation losses. Instead, we use the training loss for both. This is computed as the mean over the normalized losses computed over a single batch.

## Appendix G Self Optimization Extended

## Appendix H Infrastructure Used

The types of learning systems we discuss here are more complex than the average deep learning training setup. We are training not one, but many different kinds of models on different datasets with wildly different properties. As a result, the static graph paradigm of traditional deep learning models – distributed one graph and using MPI / allreduce style primitives – is insufficient. Finally, evaluating the performance of an optimizer is not a trivial task as it requires inner-training a large number of different models for a large number of inner-iterations.

Developing custom training and evaluation infrastructure has been critical to the success of this family of work. We describe the training infrastructure employed, discuss techniques we use for evaluation and monitoring. At this time, we are unable to release a fully running open source implementation due to the use of internal tools.

### H.1 Outer-training cluster

The cluster consists of six kinds of jobs – workers, a learner, gradient storage, summary aggregators, evaluation chief, evaluation worker. Additionally we make use of a distributed file system [ 76 ] .

##### Workers

Workers are jobs that sample a outer-task, build a tensorflow [ 77 ] graph and provides some way to estimate outer-gradients. In this work, we leverage antithetic ES sampling with shared randomness where possible. In practice, this means we start two inner-training procedures starting from the same initializations, using the same minibatches of data, but leveraging two slightly differnt outer-parameter values. Before each outer-gradient estimate new outer-parameters, as well as the current outer-iteration, are obtained by RPC call to the learner. This gradient estimate, the current outer-iteration (e.g. global step) along with the type of problem selected is sent to the key value storage worker keyed with some unique identifier.

##### Gradient Storage

The gradient storage job is a distributed dictionary which stores information computed from the worker. At this point, given the low frequency of updates only a single machine is required. This is a separate machine from the learner to control the number of queries required sent to the learner.

##### Learner

The learner polls the gradient storage for batches of data. If the outer-training iteration is within some fixed amount of time to the current outer iteration the data is deleted. In this work we use 5. This prevents stale gradients from being used to update the outer parameters. This has the negative effect of potentially ignoring the slowest tasks. At this point, however, we find that this rejection threshold is quite small (<1%) and thus safely ignored. When a batch of outer-information is obtained, the learner aggregates outer-gradients, and performs an update of outer-optimization, in our case Adam. Current loss values for each task family are also recorded in a dictionary, and aggregated across all tasks seen thus far. We find this averaged signal, as well as simply just logging out the loss from the current batch, to be useful for evaluating model performance as it is lower variance and is stationary in time. This job is also responsible for writing the meta-parameters to disk every 10 min for use later and for evaluation.

##### Summary aggregators

When training a standard model, users monitor values – e.g. activation values, losses, or accuracies. In this work we are training thousands of different neural network tasks at a time and would ideally like to be able to obtain more insight into what is going on. Existing tooling such as TensorFlow’s event files are inadequate.

We work around this by introducing a distributed service meant just for summary aggregation. This service exposes a RPC api that takes batches of summaries and logs them to disk in a custom binary format for fast visualization later. We shard request based on the name of the summary. We additionally log out subsampled data for ease of viewing after training.

In this work, we process roughly 10k summaries a second split across 24 machines. We found being able to do in-depth post-hoc analysis of model training to be critical to diagnosing issues and uncovering bugs. For example, looking at gradient variance for each task in the outer-training set let us diagnose which tasks are diverging and why. To ensure that summary computation does not cause increased computational overhead we make use of both stochastic logging as well as both batching of RPC calls to summary aggregators, and sending these RPC in parallel with computation.

##### Evaluations:

Evaluating a learned optimizer is not nearly as simple as say performing forward passes on some test set of minibatches. Evaluation consists of an expectation over training many different tasks. To obtain a low variance estimate we employ a large amount of compute to evaluate the checkpoints saved out by the learner. To lower variance, we pick a fixed set of tasks to evaluate. In addition to the meta-training task distribution (which we pick a subset of 100 to evaluate), we also evaluate on a test set of tasks which is iid to the meta-train but never seen when outer-training as well as an extremely out of distribution set of data not close to tasks in the outer-training distribution. By monitoring a variety of different problems, with different similarities to the meta-training set we obtain a better sense of outer-generalization. These evaluations take time, around an hour of compute per task, so it must parallelized.

Originally, we tried to avoid this complexity and obtain some measure of outer-loss directly from the training cluster. While this works to some extent, it is noisy, and doesn’t capture what we actually care about – performance of some fixed weights of a learned optimize when applied to a target problem for an extended period of time. Averaging over the meta-training cluster also doesn’t capture variance from outer-weight to outer-weight.

The evaluation of one task also requires orchestration. We employ a evaluation chief, and evaluation workers for each task set. While its possible to do this type of evaluation offline, we find running online yields a much better workflow and thus speeds up research.

##### Evaluation Chief:

The evaluation chief is responsible for watching directories on a distributed filesystem and to enqueue evaluation tasks. Workers use RPC to request, and to send back results (e.g. learning curves). When a set of tasks is complete for a given outer-parameter checkpoint the results are written out to disk for later analysis.

##### Evaluation workers:

Evaluation workers request task configurations from the chief over RPC. This configuration is parsed and converted to a TensorFlow graph which is then run. Over the course of running, various signals including training loss, validation loss, and test loss, are recorded. Upon completion these results are sent back over RPC to the chief to be aggregated and written to disk.

### H.2 Computational expense

At this point, training of a learned optimizer is quite expensive. It roughly entails 60K CPU cores for around a month, or around 5k CPU years. Much as neural architecture search has been dramatically optimized and improved, we hope learned optimizers will obtain a similar outer-training speedups. The energy and environmental impact of this work is also worth noting. These models take on the order of 200 megawatt hours of power to outer-train. We believe that these methods can be used to speed up development of many existing models once outer-trained. By meta-training a hyper parameter free model, one has to do no hyper parameter tuning of the optimizer for example. In general, one should weight the costs of outer-training against the potential savings achieved. In the future we expect these models will be trained once and applied everywhere.

Finally, we would like to highlight that all of this work was performed on CPU. In tests on GPU (without optimizing) we found performance to be similar. Modern accelerator hardware, TPU, GPU, are ill-suited for the small workloads we perform here (serially training lots of small networks). We believe it is possible to vectorize the inner-training of neural networks (e.g. training N networks instead of just 1 per worker) but have not explored this route yet.

## Instructions for reporting errors

We are continuing to improve HTML versions of papers, and your feedback helps enhance accessibility and mobile support. To report errors in the HTML that will help us improve conversion and rendering, choose any of the methods listed below:

Click the "Report Issue" ( ) button, located in the page header.

Tip: You can select the relevant text first, to include it in your report.

Our team has already identified the following issues . We appreciate your time reviewing and reporting rendering errors we may not have found yet. Your efforts will help us improve the HTML versions for all readers, because disability should not be a barrier to accessing research. Thank you for your continued support in championing open access for all.

Have a free development cycle? Help support accessibility at arXiv! Our collaborators at LaTeXML maintain a list of packages that need conversion , and welcome developer contributions .
