##### Report GitHub Issue

Content selection saved. Describe the issue below:

# Pre-trained Large Language Models Use Fourier Features to Compute Addition

Pre-trained large language models (LLMs) exhibit impressive mathematical reasoning capabilities, yet how they compute basic arithmetic, such as addition, remains unclear. This paper shows that pre-trained LLMs add numbers using Fourier features—dimensions in the hidden state that represent numbers via a set of features sparse in the frequency domain. Within the model, MLP and attention layers use Fourier features in complementary ways: MLP layers primarily approximate the magnitude of the answer using low-frequency features, while attention layers primarily perform modular addition (e.g., computing whether the answer is even or odd) using high-frequency features. Pre-training is crucial for this mechanism: models trained from scratch to add numbers only exploit low-frequency features, leading to lower accuracy. Introducing pre-trained token embeddings to a randomly initialized model rescues its performance. Overall, our analysis demonstrates that appropriate pre-trained representations (e.g., Fourier features) can unlock the ability of Transformers to learn precise mechanisms for algorithmic tasks.

## 1 Introduction

Mathematical problem solving has become a crucial task for evaluating the reasoning capabilities of large language models (LLMs) [ 19 , 7 , 22 , 11 ] . While LLMs exhibit impressive mathematical abilities [ 34 , 17 , 1 , 44 , 39 , 4 , 12 ] , it remains unclear how they perform even basic mathematical tasks. Do LLMs apply mathematical principles when solving math problems, or do they merely reproduce memorized patterns from the training data?

In this work, we unravel how pre-trained language models solve simple mathematical problems such as “Put together 15 15 and 93 93 . Answer: ”. Prior work has studied how Transformers, the underlying architecture of LLMs, perform certain mathematical tasks. Most studies [ 6 , 18 , 41 , 2 , 10 , 29 , 15 , 36 ] focus on Transformers with a limited number of layers or those trained from scratch; [ 20 ] analyzes how the pre-trained GPT-2-small performs the greater-than task. Our work focuses on a different task from prior interpretability work—integer addition—and shows that pre-trained LLMs learn distinct mechanisms from randomly initialized Transformers.

In § 3 , we show that pre-trained language models compute addition with Fourier features—dimensions in the hidden state that represent numbers via a set of features sparse in the frequency domain. First, we analyze the behavior of pre-trained LLMs on the addition task after fine-tuning, which leads to almost perfect accuracy on the task. Rather than merely memorizing answers from the training data, the models progressively compute the final answer layer by layer. Next, we analyze the contributions of individual model components using Logit Lens [ 3 ] . We observe that some components primarily approximate the answer—they promote all numbers close to the correct answer in magnitude—while other components primarily classify the answer modulo m m for various numbers m m . Then, we use Fourier analysis to isolate features in the residual stream responsible for the low-frequency “approximation” and high-frequency “classification” subtasks. Identifying these features allows us to precisely ablate the ability of the model to perform either approximation or classification by applying a low-pass or high-pass filter, respectively, to the outputs of different model components. We find that MLP layers contribute primarily to approximation, whereas attention layers contribute primarily to classification.

In § 4 , we show that pre-training is crucial for learning this mechanism. The same network trained from scratch with random initialization not only shows no signs of Fourier features, but also has lower accuracy. We identify pre-trained token embeddings as a key source of inductive bias that help the pre-trained model learn a more precise mechanism for addition. Across the pre-trained token embeddings of many different pre-trained models, Fourier analysis uncovers large magnitudes of components with periods 2 2 , 5 5 , and 10 10 . Introducing pre-trained token embeddings when training the model from scratch enables the model to achieve perfect test accuracy. Finally, we show that the same Fourier feature mechanism is present not only in models that were pre-trained and then fine-tuned, but also in frozen pre-trained LLMs when prompted with arithmetic problems.

Overall, our work provides a mechanistic perspective on how pre-trained LLMs compute addition through the lens of Fourier analysis. It not only broadens the scope from only investigating few-layer Transformers trained to fit a particular data distribution to understanding LLMs as a whole, but also hints at how pre-training can lead to more precise model capabilities.

## 2 Problem Setup

#### Task and Dataset.

We constructed a synthetic addition dataset for fine-tuning and evaluation purposes. Each example involves adding two numbers ≤ 260 \leq 260 , chosen because the maximum number that can be represented by a single token in the GPT-2-XL tokenizer is 520 520 . For each pair of numbers between 0 0 and 260 260 , we randomly sample one of five natural language question templates and combine it with the two numbers. The dataset is shuffled and then split into training ( 80 % 80\% ), validation ( 10 % 10\% ), and test ( 10 % 10\% ) sets. More details are provided in Appendix F . In Appendix C.3 , we show our that results generalize to a different dataset formatted with reverse Polish notation.

#### Model.

Unless otherwise stated, all experiments focus on the pre-trained GPT-2-XL model that has been fine-tuned on our addition dataset. This model, which consists of 48 48 layers and approximately 1.5 1.5 billion parameters, learns the task almost perfectly, with an accuracy of 99.74 % 99.74\% on the held-out test set. We examine other models in § 4.2 and § 4.3 .

#### Transformers.

We focus on decoder-only Transformer models [ 42 ] , which process text sequentially, token by token, from left to right. Each layer ℓ \ell in the Transformer has an attention module with output Attn ( ℓ ) \mathrm{Attn}^{(\ell)} and an MLP module with output MLP ( ℓ ) \mathrm{MLP}^{(\ell)} . Their outputs are added together to create a continuous residual stream h h [ 9 ] , meaning that the token representation accumulates all additive updates within the residual stream, with the representation h ( ℓ ) h^{(\ell)} in the ℓ \ell -th layer given by: h ( ℓ ) = h ( ℓ − 1 ) + Attn ( ℓ ) + MLP ( ℓ ) . \displaystyle h^{(\ell)}=h^{(\ell-1)}+\mathrm{Attn}^{(\ell)}+\mathrm{MLP}^{(\ell)}. (1) The output embedding W U W^{U} projects the residual stream to the space of the vocabulary; applying the softmax function then yields the model’s prediction. We provide formal definitions in Appendix A .

## 3 Language Models Solve Addition with Fourier Features

In this section, we analyze the internal mechanisms of LLMs when solving addition tasks, employing a Fourier analysis framework. We first show that the model initially approximates the solution before iteratively converging to the correct answer (§ 3.1 ). We then show that the model refines its initial approximation by computing the exact answer modulo 2 2 , 5 5 , and 10 10 , employing Fourier components of those same periods (§ 3.2 ). Finally, we demonstrate through targeted ablations that the identified Fourier components are causally important for the model’s computational processes (§ 3.3 ). Specifically, we show that MLP layers primarily approximate the magnitude of the answer, using low-frequency features, while attention layers primarily perform modular addition using high-frequency components.

### 3.1 Behavioral Analysis

Our first goal is to understand whether the model merely memorizes and recombines pieces of information learned during training, or it performs calculations to add two numbers.

#### Extracting intermediate predictions.

To elucidate how LLMs perform computations and progressively refine their outputs towards the correct answer, we extract model predictions at each layer from the residual stream. Let L L denote the number of layers. Using the Logit Lens method [ 3 ] , instead of generating predictions by computing logits W U ​ h ( L ) W^{U}h^{(L)} , predictions are derived through W U ​ h ( ℓ ) W^{U}h^{(\ell)} where ℓ ∈ [ L ] \ell\in[L] . We compute the accuracy of the prediction using each intermediate state h ( ℓ ) h^{(\ell)} .

If the models merely retrieve and recombine pieces of information learned during training, certain layers will directly map this information to predictions. For instance, [ 25 ] demonstrates that there is a specific MLP module directly maps a country to its capital.

#### LLMs progressively compute the final answers.

Figure 1 a instead shows that the model progressively approaches the correct answer, layer by layer. The model is capable of making predictions that fall within the range of ± 2 \pm 2 and ± 10 \pm 10 relative to the correct answer in the earlier layers, compared to the exact-match accuracy. This observation implies that the Transformer’s layer-wise processing structure is beneficial for gradually refining predictions through a series of transformations and updates applied to the token representations.

### 3.2 Fourier Features in MLP & Attention Outputs

#### Logits for MLP and attention have periodic structures.

We now analyze how each MLP and attention module contributes to the final prediction. We transform the output of the attention and MLP output at layer ℓ \ell into the token space using W U ​ Attn ( ℓ ) W^{U}\mathrm{Attn}^{(\ell)} and W U ​ MLP ( ℓ ) W^{U}\mathrm{MLP}^{(\ell)} at each layer, thereby obtaining the logits ℒ \mathcal{L} for each MLP and attention module. We use the running example “Put together 15 15 and 93 93 . Answer: 108 108 ” to demonstrate how the fine-tuned GPT-2-XL performs the computation. As illustrated in Figure 1 b and Figure 1 c, both the MLP and attention modules exhibit a periodic pattern in their logits across the output number space, e.g., the MLP in layer 33 33 , outlined in green, promotes all numbers that are congruent to 108 ​ mod ​ 2 108\textrm{ mod }2 (in Figure 19 in the appendix, we zoom into such layers to make this clearer). Overall, we observe two distinct types of computation within these components. Some components predominantly assign a high weight to numbers around the correct answer, which we term approximation . Meanwhile, other components predominantly assign a high weight to all numbers congruent to a + b ​ mod ​ c a+b\textrm{ mod }c for some constant c c , which we term classification .

#### Logits for MLP and attention are approximately sparse in the Fourier space.

It is natural to transform the logits into Fourier space to gain a better understanding of their properties such as the periodic pattern. We apply the discrete Fourier transform to represent the logits as the sum of sine and cosine waves of different periods: the k k -th component in Fourier space has period 520 / k 520/k and frequency k / 520 k/520 (see Appendix A for more details). Let ℒ ^ \widehat{\mathcal{L}} denote the logits in Fourier space. Figure 2 shows the Fourier space logits for two layers from Figure 1 b and Figure 1 c that have a clear periodic pattern. We find that the high-frequency components in Fourier space, which we define as components with index greater or equal to 50 50 , are approximately sparse as depicted in Figure 2 . This observation aligns with [ 29 ] , which found that a one-layer Transformer utilizes particular Fourier components within the Fourier space to solve the modular addition task.

In Figure 3 , we show that similar sparsity patterns in Fourier space hold across the entire dataset. We compute the logits in Fourier space for the last 15 15 layers, i.e., ℒ ^ Attn ( ℓ ) \widehat{\mathcal{L}}_{\mathrm{Attn}}^{(\ell)} and ℒ ^ MLP ( ℓ ) \widehat{\mathcal{L}}_{\mathrm{MLP}}^{(\ell)} where ℓ ∈ [ 32 , 47 ] \ell\in[32,47] , for all test examples and average them. We annotate the top- 10 10 outlier high-frequency components based on their magnitude. The MLPs also exhibit some strong low-frequency components; the attention modules do not exhibit strong low-frequency components, only high-frequency components.

#### Final logits are superpositions of these outlier Fourier components.

The final logits, ℒ ( L ) \mathcal{L}^{(L)} , are the sum of all ℒ MLP ( l ) \mathcal{L}^{(l)}_{\mathrm{MLP}} and ℒ Attn ( l ) \mathcal{L}^{(l)}_{\mathrm{Attn}} across all layers l ∈ [ L ] l\in[L] . Figure 4 elucidates how these distinct Fourier components contribute to the final prediction, for the example “Put together 15 15 and 93 93 . Answer: 108 108 ”. We select the top- 5 5 Fourier components of ℒ ^ ( L ) \widehat{\mathcal{L}}^{(L)} based on their magnitudes and transfer them back to logits in number space via the inverse discrete Fourier transform (Figure 4 a). The large-period (low-frequency) components approximate the magnitude while the small-period (high-frequency) components are crucial for modular addition. Figure 4 b shows that aggregating these 5 5 waves is sufficient to predict the correct answer.

#### Why is high-frequency classification helpful?

The Fourier basis comprises both cos \cos and sin \sin waves (see Definition A.3 ). By adjusting the coefficients of cos \cos and sin \sin , the trained model can manipulate the phase of the logits in Fourier space (number shift in number space), aligning the peak of the wave more closely with the correct answer. As shown in Figure 4 a, consider a wave with a period of 2 2 . Here, the peak occurs at every even number in the number space, corresponding to the mod ​ 2 \textrm{ mod }2 task. In contrast, for components with a large period such as 520 520 , the model struggles to accurately position the peak at 108 108 (also see Figure 13 in the appendix for the plot of this component with period 520 520 in the full number space). This scenario can be interpreted as solving a “ mod 520 ” task—a classification task among 520 520 classes—which is challenging for the model to learn accurately. Nevertheless, even though the component with a period of 520 520 does not solve the “ mod 520 ” task precisely, it does succeed in assigning more weight to numbers near 108 108 . The classification results from the high-frequency components can then provide finer-grained resolution to distinguish between all the numbers around 108 108 assigned a large weight by the lower frequencies. Due to this, the low-frequency components need not be perfectly aligned with the answer to make accurate predictions.

### 3.3 Fourier Features are Causally Important for Model Predictions

In the previous section, we demonstrated that there are outlier Fourier components in the logits generated by both the MLP and attention modules, as shown in Figure 3 . We also illustrated that, in one example, the high-frequency components primarily approximate the magnitude, while the low-frequency components are crucial for modular addition tasks, as depicted in Figure 4 . In this section, through an ablation study conducted across the entire test dataset, we show that both types of components are essential for correctly computing sums. Moreover, we reveal that the MLP layers primarily approximate the magnitude of the answer using low-frequency features, whereas the attention layers are responsible for modular addition using high-frequency features.

#### Filtering out Fourier components.

To understand the role various frequency components play for the addition task, we introduce low-pass and high-pass filters ℱ \mathcal{F} . For an intermediate state h h , and a set of frequencies Γ = { γ 1 , … , γ k } \Gamma=\{\gamma_{1},\dotsc,\gamma_{k}\} , the filter ℱ ⁡ ( h , Γ ) \mathcal{F}(h;\Gamma) returns the vector h ~ \widetilde{h} that is closest in L 2 L_{2} distance to h h subject to the constraint that the Fourier decomposition of W U ​ h ~ W^{U}\widetilde{h} at every frequency γ i \gamma_{i} is 0 0 . We show in Appendix A that this has a simple closed-form solution involving a linear projection. We then apply either a low-pass filter by taking Γ \Gamma to be all the components whose frequencies are greater than the frequency of the τ \tau -th component for some threshold τ \tau (i.e., removing high-frequency components), and a high-pass filter by taking Γ \Gamma to be all the components whose frequencies are less than the frequency of the τ \tau -th component (i.e., removing low-frequency components). As in the previous subsection, we take the high-frequency threshold τ = 50 \tau=50 for the following experiments (see Appendix B for more details).

#### Different roles of frequency components in approximation and classification tasks.

We evaluated the fine-tuned GPT-2-XL model on the test dataset with different frequency filters applied to all of the output of MLP and attention modules. The results, presented in Table 1 , indicate that removing low-frequency components from attention modules or high-frequency components from MLP modules does not impact performance. This observation suggests that attention modules are not crucial for approximation tasks, and MLP modules are less significant for classification tasks.

Eliminating high-frequency components from attention results in a noticeable decrease in accuracy. Furthermore, removing high-frequency components from both the attention and MLP modules simultaneously leads to an even greater reduction in accuracy. This finding corresponds with observations from Figure 1 b,c and Figure 3 , which indicate that both MLP and attention modules are involved in classification tasks due to the presence of high-frequency components in the logits. However, the approximation tasks are primarily performed by the MLP modules alone.

The errors induced by these ablations align with our mechanistic understanding. Ablating low-frequency parts of MLPs leads to off-by 10 10 , 50 50 , and 100 100 errors: the model fails to perform the approximation subtask, though it still accurately predicts the unit digit. Conversely, ablating high-frequency parts of attention leads to small errors less than 6 6 in magnitude: the model struggles to accurately predict the units digit, but it can still estimate the overall magnitude of the answer. See Figure 20 in the Appendix for more details. These observations validate our hypothesis that low-frequency components are crucial for approximation, while high-frequency components are vital for classification. The primary function of MLP modules is to approximate the magnitude of outcomes using low-frequency components, while the primary role of attention modules is to ensure accurate classification by determining the correct unit digit.

## 4 Effects of Pre-training

The previous section shows that pre-trained LLMs leverage Fourier features to solve the addition problem. Now, we study where the models’ reliance on Fourier features comes from. In this section, we demonstrate that LLMs learn Fourier features in the token embeddings for numbers during pre-training. These token embeddings are important for achieving high accuracy on the addition task: models trained from scratch achieve lower accuracy, but adding just the pre-trained token embeddings fixes this problem. We also show that pre-trained models leverage Fourier features not only when fine-tuned, but also when prompted.

### 4.1 Fourier features in Token Embedding

#### Number embedding exhibits approximate sparsity in the Fourier space.

Let W E ∈ ℝ p × D W^{E}\in\mathbb{R}^{p\times D} , where p = 521 p=521 and D D is the size of the token embeddings, denote the token embedding for numbers. We apply the discrete Fourier transform to each column of W E W^{E} to obtain a matrix V ∈ ℝ p × D V\in\mathbb{R}^{p\times D} , where each row represents a different Fourier component. Then we take the L 2 L_{2} norm of each row to yield a p p -dimensional vector. Each component j j in this vector measures the overall magnitude of the j j -th Fourier component across all the token embedding dimensions. Figure 5 a shows the magnitude of different Fourier components in the token embedding of GPT-2-XL. We see that the token embedding has outlier components whose periods are 2 , 2.5 , 5 2,2.5,5 , and 10 10 . Therefore, similar to how the model uses different Fourier components to represent its prediction (as shown in Section 3.2 ), the token embeddings represent numbers with different Fourier components. Figure 14 in the Appendix shows that the token embeddings of other pre-trained models have similar patterns the Fourier space. This suggests that Fourier features are a common attribute in the token embedding of pre-trained LLMs. In Figure 5 b, we use t-SNE and k k -means to visualize the token embedding clustering. We can see that numbers cluster not only by magnitude but also by their multiples of 10 10 .

### 4.2 Contrasting Pre-trained Models with Models Trained from Scratch

To understand the necessity of Fourier features for the addition problem, we trained the GPT-2-XL model from scratch on the addition task with random initialization. After convergence, it achieved only 94.44 % 94.44\% test accuracy (recall that the fine-tuned GPT-2-XL model achieved 99.74 % 99.74\% accuracy).

#### Fourier features are learned during pre-training.

Figure 6 shows that there are no Fourier features in the intermediate logits of the GPT-2-XL model trained from scratch on the addition task. Furthermore, Figure 7 a shows that the token embeddings also have no Fourier features. Without leveraging Fourier features, the model merely approximates the correct answer without performing modular addition, resulting in frequent off-by-one errors between the prediction and the correct answer (see details in Figure 22 ).

#### Pre-trained token embeddings improve model training.

We also trained GPT-2-small, with 124 124 million parameters and 12 12 layers, from scratch on the addition task. GPT-2-small often struggles with mathematical tasks [ 27 ] . This model achieved a test accuracy of only 53.95 % 53.95\% after convergence. However, when we freeze the token embedding layer and randomly initialize the weights for all other layers before training on the addition task, the test accuracy increases to 100 % 100\% , with a significantly faster convergence rate. This outcome was consistently observed across five different random seeds, as illustrated in Figure 7 b. This demonstrates that given the number embeddings with Fourier features, the model can effectively learn to leverage these features to solve the addition task.

### 4.3 Fourier Features in Prompted Pre-Trained Models

Finally, we ask whether larger language models use similar Fourier features during prompting.

#### Pre-trained LLMs use Fourier features to compute addition during in-context learning.

We first test on the open-source models GPT-J [ 43 ] with 6B parameters, and Phi-2 [ 21 ] with 2.7B parameters on the test dataset. Without in-context learning, the model cannot perform addition tasks. Therefore, we use 4-shot in-context learning to test its performance. Their absolute errors are predominantly multiples of 10 10 : 93% of the time for GPT-J, and 73% for Phi-2 . Using the Fourier analysis framework proposed in Section 3.2 , we demonstrate that for Phi-2 and GPT-J, the outputs of MLP and attention modules exhibit approximate sparsity in Fourier space across the last 15 15 layers (Figure 8 and Figure 18 ). This evidence strongly suggests that these models leverage Fourier features to compute additions.

#### Closed-source models exhibit similar behavior.

We study the closed-source models GPT-3.5 [ 33 ] , GPT-4 [ 34 ] , and PaLM-2 [ 16 ] . While we cannot analyze their internal representations, we can study whether their behavior on addition problems is consistent with reliance on Fourier features. Since closed-source LLMs are instruction tuned and perform well without in-context learning, we conduct error analysis with 0-shot. Most absolute errors by these models are also multiples of 10 10 : 100% of the time for GPT-3.5 and GPT-4, and 87% for PaLM-2. The similarity in error distribution to that of open-source models leads us to hypothesize that Fourier features play a critical role in their computational mechanism.

## 5 Related Work

#### Learning mathematical tasks.

Previous studies primarily explore what pre-trained LMs can achieve on arithmetic tasks, with less emphasis on the underlying mechanisms [ 30 , 37 ] . For instance, [ 23 ] demonstrates that small Transformer models can effectively learn arithmetic by altering the question format and utilizing a scratchpad method [ 28 ] . [ 20 ] identifies activation patterns for the “greater-than” operation in GPT-2, and [ 6 ] focuses on the enumeration and selection processes in GCD computation. In this paper, we dive into the specific roles of MLP and attention layers in solving mathematical tasks. Our research analyzes these components’ distinct contributions to integer addition tasks.

#### Mechanisms of pre-trained LMs.

Recent studies have significantly advanced our understanding of the underlying mechanisms of pre-trained Transformer models. For instance, research on “skill neurons” by [ 45 ] and “knowledge neurons” by [ 8 ] underscores the development of specialized neural components that encode task-specific capabilities or hold explicit factual information in the pre-trained LMs, enhancing model performance on related tasks. [ 25 ] and [ 14 ] discuss how MLPs and FFNs transform and update token representations for general language tasks. In contrast, we show that the pre-trained LMs use multiple layers to compute addition by combining the results of approximation and classification. Additionally, [ 46 ] demonstrated the capacity of GPT-2 to consolidate similar information through pre-training in the model weights, which aligns with our observations on the importance of pre-training in developing effective number embedding and arithmetic computation strategies in LMs.

#### Fourier features in Neural Networks.

Fourier features are commonly observed in image models, particularly in the early layers of vision models [ 32 , 31 , 13 ] . These features enable the model to detect edges, textures, and other spatial patterns effectively. Recently, Fourier features have been noted in networks trained for tasks that allow cyclic wraparound, such as modular addition [ 29 , 24 ] , general group compositions [ 5 ] , or invariance to cyclic translations [ 38 ] . [ 29 ] demonstrates that learning Fourier features can induce ‘grokking’ [ 35 ] . Furthermore, [ 26 ] provides a mathematical framework explaining the emergence of Fourier features when the network exhibits invariance to a finite group. We extend these insights by observing Fourier features in tasks that do not involve cyclic wraparound. [ 40 ] found that by selecting problem-specific Fourier features, the performance of MLPs can be improved on a computer vision-related task.

## 6 Conclusion

In this paper, we provide a comprehensive analysis of how pre-trained LLMs compute numerical sums, revealing a nuanced interplay of Fourier features within their architecture. Our findings demonstrate that LLMs do not simply memorize answers from training data but actively compute solutions through a combination of approximation and classification processes encoded in the frequency domain of their hidden states. Specifically, MLP layers contribute to approximating the magnitude of sums, while attention layers contribute to modular operations.

Our work also shows that pre-training plays a critical role in equipping LLMs with the Fourier features necessary for executing arithmetic operations. Models trained from scratch lack these crucial features and achieve lower accuracy; introducing pre-trained token embeddings greatly improves their convergence rate and accuracy. This insight into the arithmetic problem-solving capabilities of LLMs through Fourier features sets the stage for potential modifications to training approaches. By imposing specific constraints on model training, we could further enhance the ability of LLMs to learn and leverage these Fourier features, thereby improving their performance in mathematical tasks.

## Acknowledgments

DF and RJ were supported by a Google Research Scholar Award. RJ was also supported by an Open Philanthropy research grant. VS was supported by NSF CAREER Award CCF-2239265 and an Amazon Research Award. Any opinions, findings, and conclusions or recommendations expressed in this material are those of the author(s) and do not reflect the views of the funding agencies.

## References

[1] Anthropic. The claude 3 model family: Opus, sonnet, haiku. 2024.

[2] Yu Bai, Fan Chen, Haiquan Wang, Caiming Xiong, and Song Mei. Transformers as statisticians: Provable in-context learning with in-context algorithm selection. ArXiv , abs/2306.04637, 2023.

[3] Nora Belrose, Zach Furman, Logan Smith, Danny Halawi, Igor Ostrovsky, Lev McKinney, Stella Biderman, and Jacob Steinhardt. Eliciting latent predictions from transformers with the tuned lens. arXiv preprint arXiv:2303.08112 , 2023.

[4] Tom Brown, Benjamin Mann, Nick Ryder, Melanie Subbiah, Jared D Kaplan, Prafulla Dhariwal, Arvind Neelakantan, Pranav Shyam, Girish Sastry, Amanda Askell, et al. Language models are few-shot learners. Advances in neural information processing systems , 33:1877–1901, 2020.

[5] Bilal Chughtai, Lawrence Chan, and Neel Nanda. A toy model of universality: Reverse engineering how networks learn group operations. In International Conference on Machine Learning , pages 6243–6267. PMLR, 2023.

[6] François Charton. Can transformers learn the greatest common divisor? arXiv preprint arXiv:2308.15594 , 2023.

[7] Karl Cobbe, Vineet Kosaraju, Mohammad Bavarian, Mark Chen, Heewoo Jun, Lukasz Kaiser, Matthias Plappert, Jerry Tworek, Jacob Hilton, Reiichiro Nakano, Christopher Hesse, and John Schulman. Training verifiers to solve math word problems, 2021.

[8] Damai Dai, Li Dong, Yaru Hao, Zhifang Sui, Baobao Chang, and Furu Wei. Knowledge neurons in pretrained transformers. arXiv preprint arXiv:2104.08696 , 2021.

[9] Nelson Elhage, Neel Nanda, Catherine Olsson, Tom Henighan, Nicholas Joseph, Ben Mann, Amanda Askell, Yuntao Bai, Anna Chen, Tom Conerly, Nova DasSarma, Dawn Drain, Deep Ganguli, Zac Hatfield-Dodds, Danny Hernandez, Andy Jones, Jackson Kernion, Liane Lovitt, Kamal Ndousse, Dario Amodei, Tom Brown, Jack Clark, Jared Kaplan, Sam McCandlish, and Chris Olah. A mathematical framework for transformer circuits. Transformer Circuits Thread , 2021. https://transformer-circuits.pub/2021/framework/index.html.

[10] Deqing Fu, Tian-Qi Chen, Robin Jia, and Vatsal Sharan. Transformers learn higher-order optimization methods for in-context learning: A study with linear models, 2023.

[11] Deqing Fu, Ghazal Khalighinejad, Ollie Liu, Bhuwan Dhingra, Dani Yogatama, Robin Jia, and Willie Neiswanger. Isobench: Benchmarking multimodal foundation models on isomorphic representations, 2024.

[12] Simon Frieder, Luca Pinchetti, Ryan-Rhys Griffiths, Tommaso Salvatori, Thomas Lukasiewicz, Philipp Petersen, and Julius Berner. Mathematical capabilities of chatgpt. Advances in Neural Information Processing Systems , 36, 2024.

[13] Pierre-Étienne Fiquet and Eero Simoncelli. A polar prediction model for learning to represent visual transformations. Advances in Neural Information Processing Systems , 36, 2024.

[14] Mor Geva, Avi Caciularu, Kevin Ro Wang, and Yoav Goldberg. Transformer feed-forward layers build predictions by promoting concepts in the vocabulary space. arXiv preprint arXiv:2203.14680 , 2022.

[15] Jiuxiang Gu, Chenyang Li, Yingyu Liang, Zhenmei Shi, Zhao Song, and Tianyi Zhou. Fourier circuits in neural networks: Unlocking the potential of large language models in mathematical reasoning and modular arithmetic, 2024.

[16] Google. Palm 2 technical report, 2023.

[17] Gemini Team Google. Gemini: A family of highly capable multimodal models, 2023.

[18] Shivam Garg, Dimitris Tsipras, Percy Liang, and Gregory Valiant. What can transformers learn in-context? a case study of simple function classes. ArXiv , abs/2208.01066, 2022.

[19] Dan Hendrycks, Collin Burns, Saurav Kadavath, Akul Arora, Steven Basart, Eric Tang, Dawn Song, and Jacob Steinhardt. Measuring mathematical problem solving with the math dataset. NeurIPS , 2021.

[20] Michael Hanna, Ollie Liu, and Alexandre Variengien. How does gpt-2 compute greater-than?: Interpreting mathematical abilities in a pre-trained language model. arXiv preprint arXiv:2305.00586 , 2023.

[21] Mojan Javaheripi, Sebastien Bubeck, Marah Abdin, Jyoti Anejaand Caio Cesar Teodoro Mendes, Allie Del Giorno Weizhu Chen, Ronen Eldan, Sivakanth Gopi, Suriya Gunasekar, Piero Kauffmann, Yin Tat Lee, Yuanzhi L, Anh Nguyen, Gustavo de Rosa, Olli Saarikivi, Adil Salim, Shital Shah, Michael Santacroce, Harkirat Singh Behl, Adam Taumann Kalai, Xin Wang, Rachel Ward, Philipp Witte, Cyril Zhang, and Yi Zhang. Phi-2: The surprising power of small language models, 2023.

[22] Pan Lu, Hritik Bansal, Tony Xia, Jiacheng Liu, Chunyuan Li, Hannaneh Hajishirzi, Hao Cheng, Kai-Wei Chang, Michel Galley, and Jianfeng Gao. Mathvista: Evaluating mathematical reasoning of foundation models in visual contexts, 2024.

[23] Nayoung Lee, Kartik Sreenivasan, Jason D Lee, Kangwook Lee, and Dimitris Papailiopoulos. Teaching arithmetic to small transformers. arXiv preprint arXiv:2307.03381 , 2023.

[24] Depen Morwani, Benjamin L Edelman, Costin-Andrei Oncescu, Rosie Zhao, and Sham Kakade. Feature emergence via margin maximization: case studies in algebraic tasks. arXiv preprint arXiv:2311.07568 , 2023.

[25] Jack Merullo, Carsten Eickhoff, and Ellie Pavlick. Language models implement simple word2vec-style vector arithmetic. arXiv preprint arXiv:2305.16130 , 2023.

[26] Giovanni Luca Marchetti, Christopher Hillar, Danica Kragic, and Sophia Sanborn. Harmonics of learning: Universal fourier features emerge in invariant networks. arXiv preprint arXiv:2312.08550 , 2023.

[27] Swaroop Mishra, Arindam Mitra, Neeraj Varshney, Bhavdeep Sachdeva, Peter Clark, Chitta Baral, and Ashwin Kalyan. Numglue: A suite of fundamental yet challenging mathematical reasoning tasks. arXiv preprint arXiv:2204.05660 , 2022.

[28] Maxwell Nye, Anders Johan Andreassen, Guy Gur-Ari, Henryk Michalewski, Jacob Austin, David Bieber, David Dohan, Aitor Lewkowycz, Maarten Bosma, David Luan, et al. Show your work: Scratchpads for intermediate computation with language models. arXiv preprint arXiv:2112.00114 , 2021.

[29] Neel Nanda, Lawrence Chan, Tom Lieberum, Jess Smith, and Jacob Steinhardt. Progress measures for grokking via mechanistic interpretability. arXiv preprint arXiv:2301.05217 , 2023.

[30] Rodrigo Nogueira, Zhiying Jiang, and Jimmy Lin. Investigating the limitations of transformers with simple arithmetic tasks. arXiv preprint arXiv:2102.13019 , 2021.

[31] Chris Olah, Nick Cammarata, Ludwig Schubert, Gabriel Goh, Michael Petrov, and Shan Carter. An overview of early vision in inceptionv1. Distill , 5(4):e00024–002, 2020.

[32] Bruno A Olshausen and David J Field. Sparse coding with an overcomplete basis set: A strategy employed by v1? Vision research , 37(23):3311–3325, 1997.

[33] OpenAI. Introducing ChatGPT. https://openai.com/blog/chatgpt , 2022. Accessed: 2023-09-10.

[34] OpenAI. Gpt-4 technical report, 2023.

[35] Alethea Power, Yuri Burda, Harri Edwards, Igor Babuschkin, and Vedant Misra. Grokking: Generalization beyond overfitting on small algorithmic datasets. arXiv preprint arXiv:2201.02177 , 2022.

[36] Alethea Power, Yuri Burda, Harrison Edwards, Igor Babuschkin, and Vedant Misra. Grokking: Generalization beyond overfitting on small algorithmic datasets. ArXiv , abs/2201.02177, 2022.

[37] Jing Qian, Hong Wang, Zekun Li, Shiyang Li, and Xifeng Yan. Limitations of language models in arithmetic and symbolic induction. arXiv preprint arXiv:2208.05051 , 2022.

[38] Sophia Sanborn, Christian Shewmake, Bruno Olshausen, and Christopher Hillar. Bispectral neural networks. arXiv preprint arXiv:2209.03416 , 2022.

[39] Avijit Thawani, Jay Pujara, Pedro A Szekely, and Filip Ilievski. Representing numbers in nlp: a survey and a vision. arXiv preprint arXiv:2103.13136 , 2021.

[40] Matthew Tancik, Pratul Srinivasan, Ben Mildenhall, Sara Fridovich-Keil, Nithin Raghavan, Utkarsh Singhal, Ravi Ramamoorthi, Jonathan Barron, and Ren Ng. Fourier features let networks learn high frequency functions in low dimensional domains. Advances in neural information processing systems , 33:7537–7547, 2020.

[41] Johannes von Oswald, Eyvind Niklasson, E. Randazzo, João Sacramento, Alexander Mordvintsev, Andrey Zhmoginov, and Max Vladymyrov. Transformers learn in-context by gradient descent. In International Conference on Machine Learning , 2022.

[42] Ashish Vaswani, Noam Shazeer, Niki Parmar, Jakob Uszkoreit, Llion Jones, Aidan N Gomez, Lukasz Kaiser, and Illia Polosukhin. Attention is all you need. arXiv:1706.03762 , 2017.

[43] Ben Wang and Aran Komatsuzaki. GPT-J-6B: A 6 Billion Parameter Autoregressive Language Model. https://github.com/kingoflolz/mesh-transformer-jax , May 2021.

[44] Yan Wang, Xiaojiang Liu, and Shuming Shi. Deep neural solver for math word problems. In Proceedings of the 2017 conference on empirical methods in natural language processing , pages 845–854, 2017.

[45] Xiaozhi Wang, Kaiyue Wen, Zhengyan Zhang, Lei Hou, Zhiyuan Liu, and Juanzi Li. Finding skill neurons in pre-trained transformer-based language models. arXiv preprint arXiv:2211.07349 , 2022.

[46] Zeyuan Allen Zhu and Yuanzhi Li. Physics of language models: Part 3.1, knowledge storage and extraction. arXiv preprint arXiv:2309.14316 , 2023.

## Appendix

#### Roadmap.

In Appendix A , we introduce some formal definitions that used in our main content. In Appendix B , we show why we separate the Fourier components into the high-frequency part and the low-frequency part and why we choose τ \tau to be 50 50 . In Appendix C , we show our observation generalizes to another format of dataset, another arithmetic task and other models. In Appendix D , we provide more evidence that shows the Fourier features in the model when computing addition. In Appendix E , we provide more evidence that shows the GPT-2-XL trained from scratch does not use Fourier feature to solve the addition task. In Appendix F , we give the details of our experimental settings.

## Appendix A Formal Definition of Transformer and Logits in Fourier Space

We first introduce the formal definition of the Transformer structure that we used in this paper.

###### Definition A.1 (Transformer) .

An autoregressive Transformer language model G : 𝒳 → 𝒴 G:\mathcal{X}\rightarrow\mathcal{Y} over vocabulary Vocab \mathrm{Vocab} maps a token sequence x = [ x 1 , … , x N ] ∈ 𝒳 , x t ∈ Vocab x=\left[x_{1},\ldots,x_{N}\right]\in\mathcal{X},x_{t}\in\mathrm{Vocab} to a probability distribution y ∈ 𝒴 ⊂ ℝ | Vocab | y\in\mathcal{Y}\subset\mathbb{R}^{|\mathrm{Vocab}|} that predicts next-token continuations of x x . Within the Transformer, the i i -th token is embedded as a series of hidden state vectors h t ( ℓ ) h_{t}^{(\ell)} , beginning with h t ( 0 ) = emb ⁡ ( x t ) + pos ⁡ ( i ) ∈ ℝ D h_{t}^{(0)}=\operatorname{emb}\left(x_{t}\right)+\operatorname{pos}(i)\in\mathbb{R}^{D} . Let W U ∈ ℝ | Vocab | × D W^{U}\in\mathbb{R}^{|\mathrm{Vocab}|\times D} denote the output embedding. The final output y = softmax ⁡ ( W U ​ ( h N ( L ) ) ) y=\operatorname{softmax}(W^{U}\left(h_{N}^{(L)}\right)) is read from the last hidden state. In the autoregressive case, tokens only draw information from past tokens: h t ( ℓ ) = h t ( ℓ − 1 ) + Attn t ( ℓ ) + MLP t ( ℓ ) \displaystyle h_{t}^{(\ell)}=h_{t}^{(\ell-1)}+\mathrm{Attn}_{t}^{(\ell)}+\mathrm{MLP}_{t}^{(\ell)} where Attn t ( ℓ ) := Attn ( ℓ ) ​ ( h 1 ( ℓ − 1 ) , h 2 ( ℓ − 1 ) , … , h t ( ℓ − 1 ) ) and MLP t ( ℓ ) := MLP t ( ℓ ) ​ ( Attn t ( ℓ ) , h t ( ℓ − 1 ) ) . \displaystyle\mathrm{Attn}_{t}^{(\ell)}:=\mathrm{Attn}^{(\ell)}\left(h_{1}^{(\ell-1)},h_{2}^{(\ell-1)},\ldots,h_{t}^{(\ell-1)}\right)\quad\text{and}\quad\mathrm{MLP}_{t}^{(\ell)}:=\mathrm{MLP}_{t}^{(\ell)}(\mathrm{Attn}_{t}^{(\ell)},h_{t}^{(\ell-1)}).

In this paper, we only consider the output tokens to be numbers. Hence, we have the unembedding matrix W U ∈ ℝ p × D W^{U}\in\mathbb{R}^{p\times D} , where p p is the size of the number space. As we are given the length- N N input sequences and predict the ( N + 1 ) (N+1) -th, we only consider h N ( ℓ ) = h N ( ℓ − 1 ) + Attn N ( ℓ ) + MLP N ( ℓ ) h_{N}^{(\ell)}=h_{N}^{(\ell-1)}+\mathrm{Attn}_{N}^{(\ell)}+\mathrm{MLP}_{N}^{(\ell)} . For simplicity, we ignore the subscript N N in the following paper, so we get Eq. ( 1 ).

###### Definition A.2 (Intermediate Logits) .

Let ℒ Attn ( ℓ ) := W U ​ Attn ( ℓ ) \mathcal{L}_{\mathrm{Attn}}^{(\ell)}:=W^{U}\mathrm{Attn}^{(\ell)} denote the intermediate logits of the attention module at the ℓ \ell -th layer. Let ℒ MLP ( ℓ ) := W U ​ MLP ( ℓ ) \mathcal{L}_{\mathrm{MLP}}^{(\ell)}:=W^{U}\mathrm{MLP}^{(\ell)} denote the intermediate logits of the MLP module at the ℓ \ell -th layer. Let ℒ ( ℓ ) := W U ​ h ( ℓ ) \mathcal{L}^{(\ell)}:=W^{U}h^{(\ell)} denote the logits on intermediate state h ( ℓ ) h^{(\ell)} .

Throughout the model, h h undergoes only additive updates (Eq. ( 1 )), creating a continuous residual stream [ 9 ] , meaning that the token representation h h accumulates all additive updates within the residual stream up to layer t t .

To analyze the logits in Fourier space, we give the formal definition of the Fourier basis as follows:

###### Definition A.3 (Fourier Basis) .

Let p p denote the size of the number space. Let 𝐱 → := ( 0 , 1 , … , ( p − 1 ) ) \overrightarrow{\mathbf{x}}:=(0,1,\ldots,(p-1)) . Let ω k := 2 ​ π ​ k p − 1 \omega_{k}:=\frac{2\pi k}{p-1} . We denote the normalized Fourier basis F F as the p × p p\times p matrix: F := [ 1 p − 1 ⋅ 𝟏 → 2 p − 1 ⋅ sin ⁡ ( ω 1 ​ 𝐱 → ) 2 p − 1 ⋅ cos ⁡ ( ω 1 ​ 𝐱 → ) 2 p − 1 ⋅ sin ⁡ ( ω 2 ​ 𝐱 → ) ⋮ 2 p − 1 ⋅ cos ⁡ ( ω ( p − 1 ) / 2 ​ 𝐱 → ) ] ∈ ℝ p × p F:=\left[\begin{array}[]{c}\sqrt{\frac{1}{p-1}}\cdot\overrightarrow{\mathbf{1}}\\ \sqrt{\frac{2}{p-1}}\cdot\sin\left(\omega_{1}\overrightarrow{\mathbf{x}}\right)\\ \sqrt{\frac{2}{p-1}}\cdot\cos\left(\omega_{1}\overrightarrow{\mathbf{x}}\right)\\ \sqrt{\frac{2}{p-1}}\cdot\sin\left(\omega_{2}\overrightarrow{\mathbf{x}}\right)\\ \vdots\\ \sqrt{\frac{2}{p-1}}\cdot\cos\left(\omega_{(p-1)/2}\overrightarrow{\mathbf{x}}\right)\end{array}\right]\in\mathbb{R}^{p\times p} The first component F ⁡ [ 0 ] F[0] is defined as a constant component. For i ∈ [ 0 , p − 1 ] i\in[0,p-1] , F ⁡ [ i ] F[i] is defined as the k k -th component in Fourier space, where k = ⌊ i + 1 2 ⌋ k=\lfloor\frac{i+1}{2}\rfloor . The frequency of the k k -th component is f k := k p − 1 f_{k}:=\frac{k}{p-1} . The period of the k k -th component is T k := p − 1 k T_{k}:=\frac{p-1}{k}

We can compute the discrete Fourier transform under that Fourier basis as follows:

###### Remark A.4 (Discrete Fourier transformer (DFT) and inverse DFT) .

We can transform any logits u ∈ ℝ p u\in\mathbb{R}^{p} to Fourier space by computing u ^ = F ⋅ u \widehat{u}=F\cdot u . We can transform u ^ \widehat{u} back to u u by u = F ⊤ ⋅ u ^ u=F^{\top}\cdot\widehat{u}

Next, we define the logits in Fourier space.

###### Definition A.5 (Logits in Fourier Space) .

Let ℒ ( L ) \mathcal{L}^{(L)} , ℒ Attn ( ℓ ) \mathcal{L}_{\mathrm{Attn}}^{(\ell)} and ℒ MLP ( ℓ ) \mathcal{L}_{\mathrm{MLP}}^{(\ell)} denote the logits (Definition A.2 ). The output logits before softmax in Fourier space is defined as: ℒ ^ ( L ) = F ⋅ ℒ ( L ) \widehat{\mathcal{L}}^{(L)}=F\cdot\mathcal{L}^{(L)} . The logits of the MLP and attention modules in Fourier space are defined as: ℒ ^ Attn ( ℓ ) = F ⋅ ℒ Attn ( ℓ ) and ℒ ^ MLP ( ℓ ) = F ⋅ ℒ MLP ( ℓ ) . \displaystyle\widehat{\mathcal{L}}_{\mathrm{Attn}}^{(\ell)}=F\cdot\mathcal{L}_{\mathrm{Attn}}^{(\ell)}\quad\text{and}\quad\widehat{\mathcal{L}}_{\mathrm{MLP}}^{(\ell)}=F\cdot\mathcal{L}_{\mathrm{MLP}}^{(\ell)}.

We ignore the first elements in ℒ ^ ( L ) , ℒ ^ Attn ( ℓ ) \widehat{\mathcal{L}}^{(L)},\widehat{\mathcal{L}}_{\mathrm{Attn}}^{(\ell)} and ℒ ^ MLP ( ℓ ) \widehat{\mathcal{L}}_{\mathrm{MLP}}^{(\ell)} for the Fourier analysis in this paper as they are the constant terms. Adding a constant to the logits will not change the prediction.

Let τ ∈ ℝ \tau\in\mathbb{R} denote a constant threshold. The low-frequency components for the logits in Fourier space are defined as ℒ ^ ( ℓ ) [ 1 : 2 τ ] \widehat{\mathcal{L}}^{(\ell)}[1:2\tau] . The high-frequency components for the logits in Fourier space are defined as ℒ ^ ( ℓ ) [ 2 τ : ] \widehat{\mathcal{L}}^{(\ell)}[2\tau:] . For the following analysis, we choose τ = 50 \tau=50 (the specific choice of τ = 50 \tau=50 is explained in Appendix B ).

Next, we propose the formal definition of low-pass/high-pass filter that is used in the following ablation study.

###### Definition A.6 (Loss-pass / High-pass Filter) .

Let x ∈ ℝ D x\in\mathbb{R}^{D} denote the output of MLP or attention modules. Let F F denote the Fourier Basis (Definition A.3 ). Let τ ∈ R \tau\in R denote the frequency threshold. Let W U ∈ R p × D W^{U}\in R^{p\times D} denote the output embedding. For low-pass filter, we define a diagonal binary matrix B ∈ { 0 , 1 } p × p B\in\{0,1\}^{p\times p} as b i ​ i = { 1 if ​ i ≥ τ 0 otherwise . b_{ii}=\begin{cases}1&\text{if }i\geq\tau\\ 0&\text{otherwise}\end{cases}. For high-pass filter, we define a diagonal binary matrix B ∈ { 0 , 1 } p × p B\in\{0,1\}^{p\times p} as b i ​ i = { 1 if ​ 1 ≤ i < τ 0 otherwise . b_{ii}=\begin{cases}1&\text{if }1\leq i<\tau\\ 0&\text{otherwise}\end{cases}. Note that we retain the constant component, so b i , i = 0 b_{i,i}=0 . The output of the filter ℱ ⁡ ( x ) : ℝ D → ℝ D \mathcal{F}(x):\mathbb{R}^{D}\rightarrow\mathbb{R}^{D} is defined by the following objective function: min y \displaystyle\min_{y}\quad ‖ x − y ‖ 2 2 \displaystyle\|x-y\|_{2}^{2} subject ​ to \displaystyle\mathrm{subject~to}\quad B ​ F ​ W U ​ y = 0 \displaystyle BFW^{U}y=0

The solution to the above optimization problem is given by a linear projection.

###### Remark A.7 .

The result of the optimization problem defined in Definition A.6 is the projection of x x to the null space of B ​ F ​ W U BFW^{U} . Let 𝒩 ⁡ ( B ​ F ​ W U ) \mathcal{N}(BFW^{U}) denote the null space of B ​ F ​ W U BFW^{U} . We have ℱ ⁡ ( x ) = 𝒩 ⁡ ( B ​ F ​ W U ) ⋅ 𝒩 ​ ( B ​ F ​ W U ) ⊤ ⋅ x ⊤ \displaystyle\mathcal{F}(x)=\mathcal{N}(BFW^{U})\cdot\mathcal{N}(BFW^{U})^{\top}\cdot x^{\top}

## Appendix B Fourier Components Separation and Selection of τ \tau

Following Definition A.6 , we define single-pass filter as follows:

###### Definition B.1 (Single-Pass Filter) .

Let x ∈ ℝ D x\in\mathbb{R}^{D} denote the output of MLP or attention modules. Let F F denote the Fourier Basis (Definition A.3 ). Let γ ∈ R \gamma\in R denote the γ \gamma -th Fourier component (Definition A.3 ) that we want to retain. Let W U ∈ R V × D W^{U}\in R^{V\times D} denote the output embedding. We define a diagonal binary matrix B ∈ { 0 , 1 } V × V B\in\{0,1\}^{V\times V} as b i ​ i = { 0 if ​ ⌊ i + 1 2 ⌋ = γ ​ or ​ i = 0 , 1 otherwise . b_{ii}=\begin{cases}0&\text{if }\lfloor\frac{i+1}{2}\rfloor=\gamma\text{ or }i=0,\\ 1&\text{otherwise}.\end{cases}

The output of the filter ℱ γ ​ ( x ) : ℝ D → ℝ D \mathcal{F}_{\gamma}(x):\mathbb{R}^{D}\rightarrow\mathbb{R}^{D} is defined as the following objective function: min y \displaystyle\min_{y}\quad ‖ x − y ‖ 2 2 \displaystyle\|x-y\|_{2}^{2} subject ​ to \displaystyle\mathrm{subject~to}\quad B ​ F ​ W U ​ y = 0 \displaystyle BFW^{U}y=0

###### Remark B.2 .

The result of the optimization problem defined in Definition B.1 is the projection of x x to the null space of B ​ F ​ W U BFW^{U} . Let 𝒩 ⁡ ( B ​ F ​ W U ) \mathcal{N}(BFW^{U}) denote the null space of B ​ F ​ W U BFW^{U} . We have ℱ γ ​ ( x ) = 𝒩 ⁡ ( B ​ F ​ W U ) ⋅ 𝒩 ​ ( B ​ F ​ W U ) ⊤ ⋅ x ⊤ \displaystyle\mathcal{F}_{\gamma}(x)=\mathcal{N}(BFW^{U})\cdot\mathcal{N}(BFW^{U})^{\top}\cdot x^{\top}

For the single-pass filter, we only retrain one Fourier component and analyze how this component affects the model’s prediction. The residual stream is then updated as follows: h ( ℓ ) = h ( ℓ − 1 ) + ℱ γ ​ ( Attn ( ℓ − 1 ) ) + ℱ γ ​ ( MLP ( ℓ − 1 ) ) \displaystyle h^{(\ell)}=h^{(\ell-1)}+\mathcal{F}_{\gamma}(\mathrm{Attn}^{(\ell-1)})+\mathcal{F}_{\gamma}(\mathrm{MLP}^{(\ell-1)})

We evaluated the fine-tuned GPT-2-XL model on the addition dataset with the Fourier components period 520 520 and 2 2 . Given that T k := V − 1 k T_{k}:=\frac{V-1}{k} (Definition A.3 ), we retained only the Fourier components with γ = 1 \gamma=1 and 260 260 , respectively.

As shown in Figure 10 a, with only one frequency component, whose period is 2 2 , the model accurately predicts the parity with 99.59 % 99.59\% accuracy. As depicted in Figure 10 b, with a single frequency component of period 520 520 , the model fails to accurately predict with 96.51 % 96.51\% accuracy. We consider the frequency component with a period of 2 2 as the model’s prediction for the mod 2 task, and the frequency component with a period of 520 520 as its prediction for the mod 520 task. Figures 10 and 11 suggest that the model effectively learns the mod 2 task, as it involves a two-class classification, but struggles with the mod 520 task, which requires classifying among 520 520 classes. As the model does not need to be trained to converge to the optimal for these low-frequency components as explained at the end of Section 3.2 , predicting with the period- 520 520 component leads to predictions that normally distributed around the correct answers.

The Fourier components with larger periods present greater difficulty in solving the corresponding modular addition task compared to those with smaller periods. As demonstrated in Figure 11 , components with large periods serve primarily as approximations of the correct answer. Consequently, we categorize the Fourier components into low-frequency and high-frequency groups. The low-frequency components approximate the magnitude of the answer, whereas the high-frequency components are employed to enhance the precision of the predictions.

In reference to Figure 4 , to elucidate the contribution of these distinct Fourier components to our final prediction and the rationale behind their separation, consider the example: “Put together 15 15 and 93 93 . Answer: 108 108 ”. We selected the top-10 Fourier components of ℒ ^ ( L ) \widehat{\mathcal{L}}^{(L)} based on their magnitudes and converted them back to logits in the numerical space by multiplying with F ⊤ F^{\top} . We plotted the components with components index less than 50 in Figure 12 a and those with components index greater than 50 in Figure 12 b. Leveraging the constructive and destructive inference for different waves, the components with low periods assign more weight to the correct answer, 108 108 , and less weight to numbers close to 108 108 . These high-frequency (low-period) components ensure the prediction’s accuracy at the unit place. For the low-frequency (large-period) components, the model fails to precisely learn the magnitude of the factor between the cos \cos and sin \sin components, which results in failing to peak at the correct answer. Thus, the low-frequency (large-period) components are used to approximate the magnitude of the addition results.

## Appendix C Does Fourier Features Generalize?

### C.1 Token Embedding for Other LMs

We first show that other pre-trained LMs also have Fourier features in their token embedding for the numbers [ 0,520 ] [0,520] .

### C.2 Multiplication Task

A key question is whether pre-trained models utilize Fourier Features solely for solving addition tasks or if they generalize to other arithmetic tasks. We hypothesize the latter, knowing that numbers are represented by their Fourier features in the token embeddings after pre-training. Consequently, this Fourier representation should be leveraged in a variety of number-related tasks. To validate this hypothesis, we perform a Fourier analysis on the GPT-2-XL model fine-tuned for the multiplication task.

Considering a maximum number of 520 520 for multiplication would result in an insufficient dataset size. Therefore, we set the maximum allowable product to 10000 10000 . For each pair of numbers where the product does not exceed this limit, we generate various phrasings of multiplication questions and their corresponding answers in base 10 10 . The different phrasings used include: “What is the product of num1 and num2?”, “Find the product of num1 multiplied by num2.”, “Calculate num1 times num2.”, “num1 multiplied by num2 equals what?”, and “Multiplication of num1 with num2.” The dataset is then shuffled to ensure randomness and split into training ( 80 % 80\% ), validation ( 10 % 10\% ), and test ( 10 % 10\% ) sets. We finetune the model for 25 25 epochs with a learning rate of 1 ​ e − 4 1e-4 . Upon convergence, the validation accuracy reaches 74.58 % 74.58\% .

As the primary objective is to determine whether the Fourier features are utilized in tasks other than addition, Figure 15 displays the logits in Fourier space for each layer, as in Figure 3 . It is evident that the logits are sparse in Fourier space.

### C.3 Same Results for other format

To demonstrate that our observations are not confined to a specific description of the mathematical problem, we conducted experiments on another format of addition problem and obtained consistent results. From Figure 16 , we can see that there are also periodic structures in the intermediate logits.

From Figure 17 , we can also see the Fourier features for the MLP and attention output. These two experiments validate that our observations are not confined to a specific format of the addition problems.

### C.4 Fourier Features in Other Pre-trained LM

Using the Fourier analysis framework proposed in Section 3.2 , we demonstrate that for GPT-J, the outputs of MLP and attention modules exhibit approximate sparsity in Fourier space across the last 15 15 layers (Figure 18 )

## Appendix D Supporting Evidence For the Fourier Features

We selected the layers that clearly show the periodic pattern in Figure 1 b and Figure 1 c and plot their logits in Figure 19 .

Figure 20 illustrates that the errors resulting from the ablation study (Section 3.3 ) correspond with our theoretical insights. Removing low-frequency parts from the MLP results in errors such as off-by 10 10 , 50 50 , and 100 100 . Without these low-frequency components, the MLP is unable to accurately approximate, although it still correctly predicts the unit digit. In contrast, removing high-frequency components from the attention modules results in smaller errors, all less than 6 6 in magnitude. These findings support our statement that low-frequency components are essential for accurate approximation, whereas high-frequency components are key for precise classification tasks. Consequently, the primary function of MLP modules is to approximate numerical magnitudes using low-frequency components, and the essential function of attention modules is to facilitate precise classification by identifying the correct unit digit.

## Appendix E More Experiments on GPT-2-XL Trained from Scratch

Following the methodology proposed in Section 3 , we plotted the logits of the MLP and attention modules for each layer, as shown in Figure 21 . The prediction is solely determined by the 40 40 -th layer MLP. Unlike Figure 3 , there is no observable periodic structure across all layers.

For the model trained from scratch on the created addition dataset, all of the predictions on the test dataset deviate from the correct answer within 2 2 as shown in Figure 22 .

## Appendix F Details of Experimental Settings

#### Fine-tuned GPT-2-XL

We finetune GPT-2-XL on the “language-math-dataset” with 50 50 epochs and a batch size of 16 16 . The dataset consists of 27,400 27,400 training samples, 3,420 3,420 validation samples, and 3,420 3,420 test samples. We use the AdamW optimizer, scheduling the learning rate linearly from 1 × 10 − 5 1\times 10^{-5} to 0 0 without warmup.

#### Train GPT-2-XL from scratch

We train GPT-2-XL on the “language-math-dataset” from scratch with 500 500 epochs and a batch size of 16 16 . The dataset consists of 27,400 27,400 training samples, 3,420 3,420 validation samples, and 3,420 3,420 test samples. We use the AdamW optimizer, scheduling the learning rate linearly from 1 × 10 − 4 1\times 10^{-4} to 0 0 without warmup.

#### Train GPT-2 from scratch

For both with pre-trained token embedding and without token embedding, we train GPT-2 on the “language-math-dataset” with 700 700 epochs and a batch size of 16 16 . The dataset consists of 27,400 27,400 training samples, 3,420 3,420 validation samples, and 3,420 3,420 test samples. We use the AdamW optimizer, scheduling the learning rate linearly from 5 × 10 − 5 5\times 10^{-5} to 0 0 without warmup. In Figure 7 b, we train the model with five different seeds and plot the mean and deviation for them.

#### Create the addition dataset in main content

We consider numbers in base 10 10 up to a maximum value of 260 260 . For each pair of numbers between 0 0 and 260 260 , we generate various phrasings of addition questions and their corresponding answers. The different phrasings used are: “Total of num1 and num2.”, “Add together num1 and num2.”, “Calculate num1 + num2.”, “What is the sum of num1 and num2?”, and “Put together num1 and num2.”. The dataset is shuffled to ensure randomness and then split into training ( 80 % 80\% ), validation ( 10 % 10\% ), and test ( 10 % 10\% ) sets.

#### Create the addition dataset in Appendix C.3 with different format

We consider numbers in base 10 10 up to a maximum value of 260 260 . We generate all possible pairs of numbers within this range using combinations with replacement. For each pair, we convert the numbers to the specified base and create questions formatted as “num1,num2+” with their corresponding answers. The dataset is then split into training ( 80 % 80\% ), validation ( 10 % 10\% ), and test ( 10 % 10\% ) sets.

#### Experiments Compute Resources

All experiments involving fine-tuning and training from scratch in this paper were conducted on one NVIDIA A6000 GPU with 48GB of video memory. The fine-tuning process required less than 10 hours, while training from scratch took less than 3 days. Other experiments, such as those involving Logit Lens, were completed in less than 1 hour.

#### Licenses for Existing Assets & Open Access to Data and Code.

For the following models, we use the checkpoints provided by Huggingface. For all the trained models, we use default hyperparameters during all the training but with different random seeds. • GPT-2-XL: https://huggingface.co/openai-community/gpt2-xl , Modified MIT License

• GPT-2: https://huggingface.co/openai-community/gpt2 , Modified MIT License

• GPT-J: https://huggingface.co/EleutherAI/gpt-j-6b , Apache-2.0 License

• Phi2: https://huggingface.co/microsoft/phi-2 , MIT License

• GPT-3.5 and GPT-4: https://chatgpt.com/ or https://openai.com/index/openai-api/

• PaLM-2 https://ai.google/discover/palm2/

## Instructions for reporting errors

We are continuing to improve HTML versions of papers, and your feedback helps enhance accessibility and mobile support. To report errors in the HTML that will help us improve conversion and rendering, choose any of the methods listed below:

Click the "Report Issue" ( ) button, located in the page header.

Tip: You can select the relevant text first, to include it in your report.

Our team has already identified the following issues . We appreciate your time reviewing and reporting rendering errors we may not have found yet. Your efforts will help us improve the HTML versions for all readers, because disability should not be a barrier to accessing research. Thank you for your continued support in championing open access for all.

Have a free development cycle? Help support accessibility at arXiv! Our collaborators at LaTeXML maintain a list of packages that need conversion , and welcome developer contributions .
