##### Report GitHub Issue

Content selection saved. Describe the issue below:

# Competition and Attraction Improve Model Fusion

###### Abstract.

Model merging is a powerful technique for integrating the specialized knowledge of multiple machine learning models into a single model. However, existing methods require manually partitioning model parameters into fixed groups for merging, which restricts the exploration of potential combinations and limits performance. To overcome these limitations, we propose Model Merging of Natural Niches (M2N2), an evolutionary algorithm with three key features: (1) dynamic adjustment of merging boundaries to progressively explore a broader range of parameter combinations; (2) a diversity preservation mechanism inspired by the competition for resources in nature, to maintain a population of diverse, high-performing models that are particularly well-suited for merging; and (3) a heuristic-based attraction metric to identify the most promising pairs of models for fusion. Our experimental results demonstrate, for the first time, that model merging can be used to evolve models entirely from scratch . Specifically, we apply M2N2 to evolve MNIST classifiers from scratch and achieve performance comparable to CMA-ES, while being computationally more efficient. Furthermore, M2N2 scales to merge specialized language and image generation models, achieving state-of-the-art performance. Notably, it preserves crucial model capabilities beyond those explicitly optimized by the fitness function, highlighting its robustness and versatility. Our code is available at https://github.com/SakanaAI/natural_niches .

## 1. Introduction

Open-source generative models have enabled the proliferation of thousands of specialized variants, fine-tuned by practitioners to meet their specific needs. In an environment where diverse models are freely accessible, the ability to merge and consolidate this wealth of knowledge into a single model becomes increasingly valuable. This process, known as model merging ( Labonne, 2024 ) , has gained traction, as evidenced by the widespread presence of merged models on the Open LLM Leaderboard ( HuggingFace, 2023 ) .

Model merging initially relied on manually adjusting coefficients to combine seed models, a process guided by intuition and requiring significant trial and error to optimize performance for specific tasks. Recently, evolutionary algorithms have streamlined this process by automatically searching for optimal coefficients ( Akiba et al., 2024 ; Kuroki et al., 2024 ) , significantly improving merging efficiency. However, one manual step remains: developers must group model parameters into fixed sets before merging, restricting the search space for potential combinations (see Figure 1 left). To address this limitation, we propose Model Merging of Natural Niches (M2N2), an evolutionary algorithm with three key features:

(1) Evolving the Merging Boundaries . Existing methods partition the parameters of each seed model into fixed groups (e.g., layers) and optimize merging coefficients within these predefined boundaries, limiting the scope of exploration. In contrast, M2N2 iteratively merges two models at a time, using flexible split points to divide parameters. Instead of working with static models, we maintain an evolving archive of models. As the number of generations increases, M2N2 progressively explores a broader set of boundaries and coefficients (see Figure 1 right), enabling increasingly complex combinations when beneficial. This gradual, optional increase in complexity ensures a more extensive search while maintaining computational efficiency.

(2) Managing Diversity . Model merging is most effective when combining diverse models, making diversity preservation essential. However, the challenge lies in defining which characteristics should remain diverse. Many approaches require manually specified diversity metrics, however, we believe it is becoming increasingly hard to come up with efficient diversity metrics as models and tasks grow in complexity. Instead, we incentivize diversity of high-performing models as Nature does — through competition for limited resources.

(3) Attraction . We introduce a heuristic for pairing models based on their complementary strengths, which improves both efficiency and the final model performance. Mate selection remains an underexplored aspect of genetic algorithms, yet it becomes increasingly crucial as the computational costs of crossovers (merging) grow. M2N2 highlights the importance of this factor and encourages further research in this area.

Our achievements and key contributions are summarized below. • We introduce M2N2, a novel evolutionary approach with three key components – competition, attraction, and model fusion with split points. Through comprehensive ablation studies, we demonstrate that these components significantly improve model merging and could enhance other evolutionary algorithms using crossover operations.

• We present the first application of model merging for training models from scratch, showing that our method surpasses existing evolutionary algorithms in both performance and computational efficiency.

• We scale M2N2 to Large Language Models (LLMs) and diffusion-based image generation models, highlighting key benefits of gradient-free optimization, including stable model fusion without catastrophic forgetting, compatibility across models trained on different objectives, reduced memory footprint by avoiding gradient computations, and preservation of model capabilities without requiring access to the original training data.

## 2. Related Work

In this section, we review two relevant areas of research: the emerging field of model merging, and the well-established diversity preservation mechanisms in genetic algorithms. While model merging represents a novel approach that has evolved rapidly from manual to automated techniques, diversity preservation in evolutionary algorithms has been extensively studied over several decades.

### 2.1. Model Merging

Model merging introduces an innovative approach for integrating the strengths of multiple pre-trained models. In contrast to fine-tuning, which focuses on refining a single pre-trained model, model merging can leverage several models concurrently without requiring back-propagation. This has allowed the method to combine extremely large models for tasks involving subjective goals, like customizing an image generation model to reflect personal tastes. Notably, the release of Stable Diffusion (SD) ( Rombach et al., 2022 ) and open-source interfaces ( AUTOMATIC1111, 2022 ) enabled practitioners to merge different SD fine-tunes manually, using techniques like linear and spherical linear interpolation (SLERP) ( White, 2016 ) . These early efforts demonstrated the potential of model merging in combining specialized capabilities into a single unified model. Curiously, this modern trial-and-error search for personally appealing images seems extremely inline with earlier evolutionary art systems like Picbreeder ( Secretan et al., 2008 ) , where users could combine and evolve neural networks to create images that matched their subjective preferences through an exploratory interface.

Subsequent research has approached the model merging problem from two complementary directions: minimizing interference between models and automating the merging process. Methods such as TIES ( Yadav et al., 2023 ) and DARE ( Yu et al., 2024 ) introduced strategies to balance the contributions of individual models while minimizing interference, ensuring that the strengths of each model are preserved without mutual disruption. They also expanded the applications of model merging to the natural language domain.

Evolutionary algorithms like CMA-ES ( Hansen and Ostermeier, 2001 ) were later applied to automate the search for optimal merging coefficients. As explored in ( Akiba et al., 2024 ) , these methods not only automate what was previously a manual, iterative process but also significantly improve efficiency.

While previous research centered on merging pre-trained models, we show that merging can efficiently be used to evolve models from scratch. Additionally, unlike earlier methods that required manual partitioning of model parameters, we automate and optimize this process during the evolutionary process.

### 2.2. Overview of Diversity Preservation in Genetic Algorithms

Diversity preservation in Genetic Algorithms (GA) is crucial for finding multiple solutions to multimodal problems ( Wong, 2015 ) and to prevent premature convergence. We believe this is particularly important when using crossover operations (such as model merging). These operations benefit from diversity while at the same time reducing it, which may lead to premature convergence if not counter-acted by a diversity increasing mechanism. In this section, we provide a quick overview of the two main methods for diversity preservation in GA: 1) crowding ( De Jong, 1975 ; Wong et al., 2012 ) and 2) fitness sharing ( Goldberg et al., 1987 ; Deb and Goldberg, 1989 ; Goldberg et al., 1992 ; Pétrowski, 1996 ) .

Crowding methods involve first applying mutation and crossover to produce new candidate solutions. These candidates then compete for inclusion in the population, but only against other candidates that are similar, based on a predefined criteria such as genetic or phenotypic distances. This selective competition helps maintain diversity within the population by preventing any single solution type from becoming overly dominant. A similar mechanism for selective competition is used in the popular algorithm of MAP-Elites ( Mouret and Clune, 2015 ) . In MAP-Elites, the solution space is divided into a multidimensional grid, with each cell representing a species defined by one or more predefined behavior descriptors. New candidates are placed into cells based on their descriptors and replace existing solutions only if they perform better. The real challenge of this method lies in defining descriptors that promote the desired type of diversity.

Fitness sharing requires each individual to share its rewards with others. In explicit fitness sharing, the researcher defines a distance function that is used to cluster similar individuals into a species, each individual then shares its fitness with other members of its species, making it more difficult for any single species to grow excessively large. A notable example is the NEAT ( Stanley and Miikkulainen, 2002 ) algorithm, known for evolving neural networks topologies, which clusters solutions into species by measuring genotypic differences (distances in network topologies). Implicit fitness sharing ( Smith et al., 1993 ; Darwen and Yao, 1996 ) , is seen as the more natural method because, as in Nature, it protects niches rather than species. A niche is a group of individuals that compete for the same resources, while a species is defined as group that can interbreed and typically have small genetic and phenotypic differences. Usually, members of the same species compete for the same resources (e.g., food, partners, shelter), but vastly different species can also compete for the same vital resources like nesting sites or food sources (e.g., birds and bats, lions and hyenas). Implicit sharing does not rely on custom distance metrics. Instead, it simulates natural competition for limited resources, promoting diversity as individuals who can derive their fitness from less contested resources are favored. While this approach has received less attention recently, we argue it deserves renewed consideration. The high-dimensional nature of modern AI tasks and models makes defining meaningful diversity metrics particularly challenging. By leveraging natural resource competition rather than explicit distance metrics, implicit fitness sharing offers an elegant and scalable solution for contemporary applications. We hope this work helps revitalize interest in this underappreciated approach to diversity maintenance. We provide more details in Section 3 .

## 3. Natural Niches

In model merging, the goal is to find the optimal parameters θ ∗ \theta^{*} for a merged model from a set of K K seed models, each of which is characterized by its model parameters θ i \theta_{i} ( i = 1 ⋯ K i=1\cdots K ), so that the optimization goal, normally in the form of summation or average of task scores, is maximized. The following equation expresses this description mathematically: (1) θ ∗ = arg ⁡ max ⁡ ∑ j = 1 N θ ⁡ s ⁡ ( x j ∣ θ ) , where , θ = h w ​ ( θ 1 , ⋯ , θ K ) \theta^{*}=\arg\max_{\theta}\sum_{j=1}^{N}{s(x_{j}\mid\theta}),\text{where},\theta=h_{w}(\theta_{1},\cdots,\theta_{K}) Here, h w h_{w} is the model merging function parameterized by w w ’s that correspond to fixed model merging boundaries (e.g., one scalar w k , l w_{k,l} for the l l -th layer in the k k -th seed model), s s is the score function for a certain task, x j x_{j} is a task example, and N N is the number of examples to be evaluated. In Natural Niches (M2N2), we propose modifications to the merging function h h to allow the evolution of the merging boundaries, and adjustments to the optimization goal to promote diverse solutions.

### 3.1. Eliminating Fixed Model Merging Boundaries

In the formulation above, finding θ ∗ \theta^{*} boils down to searching for the optimal model merging parameters w w in h w h_{w} . To get rid of the constraints of fixed model merging boundaries and thus allow more flexibility, we propose to include these boundaries together with the mixing parameters into the evolutionary process. Concretely, M2N2 maintains an archive of models, which is initialized with the K K seed models. At each training step, M2N2 randomly picks two models A A and B B from the archive, and samples two parameters ( w m , w s ) (w_{m},w_{s}) that determines the mixing ratio and the split-point in the models’ parameters space. It then merges models A A and B B with the following formula, and inserts the new model into the archive if it outperforms the worst individual. (2) h M2N2 ​ ( θ A , θ B , w m , w s ) = concat ​ ( CLOSE \displaystyle h_{\mathrm{M2N2}}(\theta_{A},\theta_{B},w_{m},w_{s})=\text{concat}\big( f w m ​ ( θ A < w s , θ B < w s ) , \displaystyle f_{w_{m}}(\theta_{A}^{<w_{s}},\theta_{B}^{<w_{s}}), OPEN f 1 − w m ​ ( θ A ≥ w s , θ B ≥ w s ) ) \displaystyle f_{1-w_{m}}(\theta_{A}^{\geq w_{s}},\theta_{B}^{\geq w_{s}})\big) Here, θ < w s \theta^{<w_{s}} and θ ≥ w s \theta^{\geq w_{s}} indicate the sub-arrays of model parameters before and after the split-point indexed by w s w_{s} . f t ​ ( θ A , θ B ) f_{t}(\theta_{A},\theta_{B}) is a spherical linear interpolation of rotations (SLERP) function that interpolates ( θ A , θ B ) (\theta_{A},\theta_{B}) with t t . As shown in the right part of Figure 1 , our method incrementally expands the search space by exploring a broader set of boundaries and coefficients. This gradual introduction of complexity ensures a wider range of possibilities while maintaining computational tractability.

### 3.2. Encouraging Diversity via a Modified Optimization Goal

Competing for limited resources naturally promotes diversity, favoring individuals who can tap into less contested resources. In the context of the optimization goal in Equation 1 , where a sum of scores from all the examples is being maximised, each score is a “resource” that contributes to the fitness of a solution. By limiting the resource supply, M2N2 sparks competition which naturally favors individuals that take over new niches. Concretely, we limit the total fitness a population can extract from a data point x j x_{j} by a capacity c j c_{j} . The amount of fitness a candidate solution derives from a data point is proportional to its score relative to the aggregate score of the population. Our modified goal becomes:

(3) θ ∗ = arg ⁡ max ⁡ ∑ j = 1 N θ ⁡ s ⁡ ( x j ∣ θ ) z j + ϵ ​ c j , where , z j = ∑ k = 1 P s ⁡ ( x j ∣ θ k ) \theta^{*}=\arg\max_{\theta}\sum_{j=1}^{N}{\frac{s(x_{j}\mid\theta)}{z_{j}+\epsilon}c_{j}},\text{where},z_{j}=\sum_{k=1}^{P}s(x_{j}\mid\theta_{k})

where ϵ \epsilon in the denominator is a small number to prevent the zero-division error. In the term that defines z j z_{j} , P P is the archive size. The capacity c j c_{j} , is task dependent and can be defined in multiple ways. For example, in binary scoring tasks (i.e. s ⁡ ( ⋅ ) ∈ { 0 , 1 } s(\cdot)\in\{0,1\} ) we simply set c j = 1 c_{j}=1 . In some experiments, we have a continuous reward from 0 to 1. Here, we define c j = max i ⁡ s ⁡ ( x j | θ i ) c_{j}=\max_{i}s(x_{j}|\theta_{i}) to ensure that partially solved data points (where max i ⁡ s ⁡ ( x j | θ i ) < 1 \max_{i}s(x_{j}|\theta_{i})<1 ) do not distribute the same amount of fitness points as fully solved data points (where max i ⁡ s ⁡ ( x j | θ i ) = 1 \max_{i}s(x_{j}|\theta_{i})=1 ).

### 3.3. Sampling Parents via Attraction

Many evolutionary algorithms use the crossover operation to combine the strengths of both parents. In biology, this combination (i.e., reproduction) is very expensive, and therefore, animals invest many resources in the process of mate selection. We believe that as we make use of more expensive crossover operations, like model merging, algorithms for mate selection become increasingly important.

In contrast to conventional methods that put more sampling probability mass on top performing models in the archive, M2N2 adds an extra layer of consideration that takes into account the complementarity of the parent models. Specifically, we sample the first parent based on their weighted sum of scores defined in Equation 3 , and then sample the second parent based on a “attraction score” generated by function g g that is specifically tailored for the first parent. The equation below gives the definition of this attraction score, it straightforwardly expresses a desire to choose a model B that performs well in the data points where model A performs less well, while giving an extra preference to resources with high capacity c j c_{j} and low competition z j z_{j} . (4) g ⁡ ( θ A , θ B ) = ∑ j = 1 N c j z j + ϵ ​ max ⁡ ( s ⁡ ( x j ∣ θ B ) − s ⁡ ( x j ∣ θ A ) , 0 ) g(\theta_{A},\theta_{B})=\sum_{j=1}^{N}{\frac{c_{j}}{z_{j}+\epsilon}\max\big(s(x_{j}\mid\theta_{B})-s(x_{j}\mid\theta_{A}),0\big)}

## 4. Experiments

We verify the effectiveness of our proposed method on three challenging tasks: First, we evolve image classifiers from scratch and from pre-trained models on the MNIST dataset, then scale up the experiment to merging LLMs and diffusion-based image generation models to demonstrate its general applicability.

### 4.1. Experiment 1: Evolving MNIST classifiers

Setup

Model : The model being optimized is a two-layer feedforward neural network with 19,210 parameters in total. When starting from scratch, we randomly initialize the models. For pre-trained models, we develop two specialized models: one is trained on digits 0 through 4, and the other is trained on digits 5 through 9.

Baselines : For the MAP-Elites algorithm, we use two diversity dimensions to create a 10 by 10 grid: the accuracy of the model in odd and even numbers. When starting from scratch, we use CMA-ES ( Hansen and Ostermeier, 2001 ) as a baseline, even though it does not perform model merging here. Since the models are randomly initialized, optimizing mixing coefficients alone would be insufficient. Instead, CMA-ES directly optimizes model weights, which incurs a cubic computational cost O ⁡ ( n 3 ) O(n^{3}) with respect to the number of parameters. While this method doesn’t scale to larger models, it serves as a benchmark for how a popular evolutionary algorithm performs in this experiment. When working with pre-trained models, we use a brute-force search baseline that merges the two seed models by adjusting a mixing coefficient that ranges from 0 to 1 in increments of 10 − 5 10^{-5} . This baseline is first evaluated on the training data; the best coefficient is subsequently evaluated on the test data.

Evolutionary Operators and Variables : All model merging methods (which excludes CMA-ES) sample a new candidate at a time and decide sequentially whether to insert the candidate into the archive. M2N2 and GA use an archive of 20, sampling each candidate sequentially and deciding whether to insert it, similar to MAP-Elites. MAP-Elites, uses a 10x10 grid, resulting in an archive size of 100. CMA-ES uses a population of 20, sampling and updating its parameters in batches. When starting from scratch all model merging methods use the same mutation operation (Gaussian noise) and the same crossover operation (SLERP with split-point, as described in section 3.1 ). However, when dealing with pre-trained models, mutation is omitted because we want to assess how our method would scale to larger models where random mutations are not effective.

Compute Resources : The 10 independent runs took about 15 hours for CMA-ES, and about 1h for each of the other methods. We ran this experiment using only CPUs.

Results

When starting from scratch, M2N2 achieves the highest test accuracy by a substantial margin when compared to the other model merging methods, as shown in Figure 2 (left). Interestingly, GA with crossover performs better early on (before step 12,000) than GA without crossover, however, it converges faster to an inferior solution. The early convergence happens because GA can’t maintain a diverse population which is crucial for effective crossover operations. Crossover reduces population diversity, and without a strong counteracting force, it diminishes exploration. In contrast, M2N2 leverages the crossover operation effectively, benefiting significantly from the diversity it manages to retain. GA is an extreme case where there is no competition, we observed that by progressively decreasing competition in M2N2, we progressively converge earlier to worse solutions (analyzed on the next section). MAP-Elites clusters individuals by their accuracy on odd and even numbers. This means it will always keep individuals who perform poorly on those tasks because there is a slot reserved just for them. Even though those individuals add to the diversity of the population, this is clearly not the type of diversity that leads to strong solutions and it highlights the difficulty of hand-engineering useful diversity metrics.

For models trained from scratch, the split-point and attraction score have a minimal impact (ablations omitted for clarity). However, as seen in Figure 2 (right), the split-point becomes crucial when starting from pre-trained models, while attraction significantly improves performance throughout the training process. GA has a low average test accuracy with large error bars as its performances is highly dependent on the quality of the first merges. Note that when starting from pre-trained models the mutation operator was not used (as explained in the Setup section), and therefore, the performance is worse.

Analysis

This section focuses exclusively on the experiment where models were evolved from scratch, as the later sections will provide ample discussion on evolving models starting from pre-trained LLMs and diffusion models.

Diversity : Figure 3 left, shows the percentage of training data points that can be correctly labeled by at least one model in the archive, we call this percentage the training coverage. We observe that the archive in M2N2 quickly spreads to cover the majority of the training data points and maintains this high coverage throughout the training process. The right-hand plot shows how the diversity in the performance of the population evolves with training. If either all models correctly or incorrectly classify a data point, the entropy is 0 (no diversity). In contrast, when the models are evenly split on a prediction, entropy reaches its maximum value of 1. The plot displays the average entropy across all data points. For M2N2 we see a sharp initial rise in entropy followed by a gradual decline as low-performing models go extinct. In contrast, MAP-Elites continually increases diversity by retaining lower-performing models, but it fails to achieve a high coverage. The Genetic Algorithms, lacking a diversity preservation mechanism, reduce coverage early on and show a sharp drop in entropy as they converge prematurely on the best solutions. This drop in diversity is accentuated with the crossover operation.

Overall, the graphs show that M2N2 maintains an archive of models with complementary strengths that facilitate effective merging, while systematically discarding weaker models as training progresses.

Competition : Figure 4 left, shows that smaller archives perform better in the beginning but converge faster to inferior solutions. This suggests that we should scale the archive size along the number of forward passes we want to make. Note that in our plot the computational cost does not increase with the archive size since the number of forward passes remains the same, however, the memory footprint does increase with larger populations. For very large models we can always store the archive on disk instead of keeping them all in the RAM.

For a fixed population size P P , we can adjust the intensity of competition by introducing a hyper-parameter α ≥ 0 \alpha\geq 0 , as described in the fitness function in eq. 5 .

(5) f ⁡ ( θ i ) = ∑ j = 1 N s ⁡ ( x j | θ i ) z j α + ϵ ​ c j f(\theta_{i})=\sum_{j=1}^{N}\frac{s(x_{j}|\theta_{i})}{{z_{j}}^{\alpha}+\epsilon}c_{j}

When α = 0 \alpha=0 , there is no competition because the total fitness available per data point becomes unlimited. When α = 1 \alpha=1 , the total fitness distributed among different individuals is limited to the capacity c j c_{j} . For α > 1 \alpha>1 , the total fitness distributed decreases with increasing competition ( z j z_{j} ), this scenario can be thought of as individuals needing to "fight" for resources, spending some fitness points in the process. Figure 4 right, shows that smaller values of α \alpha (i.e. lower competition) have a similar effect to decreasing the population size: it performs better in the beginning but it converges faster to inferior solutions.

### 4.2. Experiment 2: Combining LLMs with Math and Agentic Skills

Setup

Models : We combine a math specialist, WizardMath-7B-V1.0 ( Luo et al., 2023 ) , with a specialist on agentic enviroments, AgentEvol-7B ( Xi et al., 2024 ) , to achieve an agent that performs well on the math benchmark GSM8k ( Cobbe et al., 2021 ) and on the web shopping benchmark WebShop ( Yao et al., 2022 ) . These two models share the same architecture of Llamma-2-7b ( Touvron et al., 2023 ) , a decoder-only transformer with 32 layers.

Datasets : For the math task, we use the test split of GSM8k as our test split (1319 samples). For the training split, we use the first 1319 samples of GSM8k train dataset. In the web shopping task, we use the WebShop environment implemented in ( Xi et al., 2024 ) . The test split consistent of the first 100 tasks, while the training split were the next 100 tasks. We allow the agents to take up to 7 steps.

Baselines : The CMA-ES optimizes 32 mixing coefficients (one for each layer) for a SLERP merge between the two seed models. All methods ran for a 1000 evaluations on the training set. For the MAP-Elites we used two dimensions to create a 4 by 4 grid: the accuracy on the math and on the web shopping training splits.

Evaluation : In this experiment, all methods used 1000 evaluations on the training set. M2N2 and GA used an archive size of 15. CMA-ES used a population size of 25.

Evolutionary Operators and Variables : In our LLM Merging experiment we do not use a mutation operator since random mutations don’t work well on large models. Moreover, in these experiments we initialize the M2N2 and GA archives with seed models, followed by a short warm-up period (50 iterations or less) where the seed models merge randomly amongst themselves and populate the archive.

Compute Resources : For these experiments, we used 4 H100 GPUs to run each method for around 24h.

Results

Table 1 shows that M2N2 achieves the highest score. Both the attraction and the split-point techniques play a crucial role, however, the split-point seems to be slightly more important. Note that on Table 1 all algorithms run the same amount of evaluations and used the same merging method (SLERP). When combining the Math and Agentic skills, CMA-ES yielded a low score, likely due to suboptimal parameter partitioning, highlighting the need to include the merging boundaries in the optimization process.

Analysis

As shown in Figure 5 , the findings from the MNIST dataset generalize to LLM merging. The Natural Niches method maintains high training coverage, as seen on the left side of the figure. The entropy rises early on as the models explore diverse niches (right), followed by a gradual decrease as low-performing models are removed, and the strengths of the models are aggregated. In contrast, MAP-Elites focuses on maximizing entropy at the cost of training efficiency and coverage, as it retains low-performing models. GA quickly reduces both coverage and entropy as it greedily converges on its top solution, ultimately collapsing the entire archive onto a single solution, with entropy nearing zero.

### 4.3. Experiment 3: Merging Diffusion-Based Image Generation Models

Setup

Models : We evaluate our method in merging diverse text-to-image models. Our seed models include JSDXL ( Shing et al., [n. d.] ) , which was specifically trained on Japanese prompts, and three models primarily trained with English prompts: SDXL 1.0 ( Podell et al., 2023 ) , SDXL-DPO ( Wallace et al., 2024 ) , and Juggernaut-XL-v9 ( RunDiffusion, 2024 ) . All these models share the same architecture of the base model SDXL 1.0 . The primary objective is to create a model that combines the best image generation capabilities from each seed model while retaining JSDXL’s ability to understand Japanese prompts.

Evolutionary Operators and Variables : As in our LLM merging experiment, we omit the mutation operator. For model merging, we retain the VAE from SDXL – since most seed models left this component unchanged – and we preserve JSDXL ’s tokenizer and text encoder to leverage its superior Japanese language understanding. Therefore, we are combining only the U-Nets from the various models using Equation 2 . We merge the attention layers independently from the other components, as this was found effective on previous work ( Sakana AI, 2025 ) . This compartmentalization of parameters is analogous to the grouping of DNA into chromosomes, where each chromosome divides independently and has one or more split points. This design introduces useful inductive biases while maintaining the flexibility to explore more complex merging boundaries.

Dataset : We utilize the COCO dataset ( Lin et al., 2014 ) , specifically the validation split. We use the last 2,000 images for training and the first 10,000 images for testing, ensuring no overlap between the sets. The Japanese captions are sourced from the STAIR Captions dataset ( Yoshikawa et al., 2017 ) , which provides Japanese descriptions for COCO images.

Training and Testing metrics : During training, we give the Japanese captions as prompts to the model and calculate the cosine similarity between the CLIP features of the correspondent images from COCO and the generated ones. This metric is normalized to fall within the range of 0 to 1, which we refer to the Normalized CLIP Similarity (NCS) metric. While models generally achieve high absolute NCS values, small differences can significantly impact performance. To emphasize these relative differences, we adjust the scores before computing the fitness score: for each training sample, we subtract the corresponding worst score achieved by the population. This adjustment emphasizes relative performance, increasing the competition for training samples and favoring more diversity in the population’s skills.

Baseline : Our work builds on ( Yoshikawa et al., 2017 ) approach using CMA-ES for merging. While we use the same dataset, our method maximizes NCS instead of minimizing the Fréchet Inception Distance (FID) metric ( Heusel et al., 2017 ) as they did. This choice enables per-sample evaluation necessary for resource competition, whereas FID only provides aggregate performance across the training set.

Qualitative Results

Diversity and Visual Capabilities : Figure 6 illustrates how our merged model successfully combines the strengths of individual seed models while mitigating their weaknesses. Note that if we exclude our merged model, we observe that each seed model produced both the highest and lowest quality outputs for different test cases. Additionally, it is extremely hard to find a clear pattern that describes the speciality of each model or inform us on how to create an effective and custom diversity metric. Our diversity preservation mechanism addresses this challenge by automatically preserving the models that uniquely excel on training samples where other models underperform.

The merged model demonstrates two key improvements over the seed models. First, it generates more photorealistic images, which aligns with our training set of real photographs. Second, it shows enhanced semantic understanding of the input captions. For instance, in the rightmost column of Figure 6 , while several seed models generated visually appealing bikes, our merged model not only specifically focused on capturing the bike’s registration number display area as specified in the caption, but also produced an image that looks like an actual photograph rather than a synthetic rendering.

Language Understanding : Figure 7 shows that our model has a good understanding of both Japanese and English, despite being evolved exclusively with Japanese captions! This emergent bilingual ability exemplifies a key advantage of model merging: it enables the aggregation of complementary capabilities while avoiding the catastrophic forgetting typically associated with gradient-based training methods. Note that the seed models show very distinct language capabilities: JSDXL performs better with Japanese prompts while the other models perform better with English prompts.

Quantitative Results

Performance : Table 2 demonstrates that our model achieves a superior NCS score on the test set compared to all other models. Additionally, we surpass the model merging baseline, CMA-ES, in FID performance, even though this baseline was explicitly trained to minimize FID on the training set.

Language Understanding : We evaluated the models’ ability to maintain semantic consistency across languages by generating pairs of images: one from Japanese captions (sampled from our test set) and another from their GPT-4o translated English versions. For each image pair, we computed the cosine similarity between their CLIP feature representations, which captures how semantically similar the generated images are. Averaging these similarities across 100 diverse caption pairs, Table 3 demonstrates that our model achieves significantly better cross-lingual consistency than the other models. This statistically confirms what we had already observed in our qualitative results.

## 5. Limitations & Future Work

The feasibility of model merging strongly depends on the degree of similarity between models. As demonstrated in ( Yu et al., 2024 ) , when fine-tuned models deviate significantly from their base models—often due to extensive, divergent training—merging becomes impractical. We hypothesize that models with divergent state representations are incompatible for merging. However, a standardized metric for model compatibility has yet to be established. Defining such a metric could allow it to be used as a form of regularization during preprocessing (e.g., fine-tuning), enabling better control over model compatibility and ensuring the success of merging.

We believe there is a strong evolutionary pressure for models that are co-evolving together to remain compatible for merging. Should one model, diverge and become incompatible with others, it would no longer produce viable offspring, halting its improvement and leading to its eventual extinction. Testing this hypothesis through further research would provide valuable insights into the dynamics of model co-evolution. Moreover, incorporating a compatibility metric into the attraction heuristic could facilitate the co-evolution of distinct species of models, defined as groups that merge with one another but not with others.

## 6. Conclusion

In this paper, we present the first application of model merging for training models from scratch and demonstrate that it achieves top-tier performance and efficiency when combined with a diversity-preservation technique. Furthermore, this approach scales effectively to LLMs and diffusion-based image generation models. Our ablation studies reveal that the proposed mechanisms of competition, attraction and the use of split-points significantly enhance the performance of model merging and have the potential to benefit other evolutionary algorithms utilizing crossover operations.

Our LLM merging experiments highlight the ability to combine vastly different skills, enabling multi-task capabilities without requiring access to the original training data. Remarkably, in diffusion model experiments, we observe that the merged models retain English language capabilities despite being optimized exclusively for Japanese tasks. This finding underscores the promise of model merging as a robust transfer learning mechanism that resists catastrophic forgetting, which is typically encountered in fine-tuning.

Finally, we hope this work revitalizes interest in two underexplored areas: mate selection algorithms and implicit fitness sharing as a mechanism for diversity preservation. These concepts are increasingly critical as crossover operations, such as model merging, become computationally more expensive, and as models and tasks grow in complexity.

## References

Akiba et al . (2024) Takuya Akiba, Makoto Shing, Yujin Tang, Qi Sun, and David Ha. 2024. Evolutionary optimization of model merging recipes. arXiv preprint arXiv:2403.13187 (2024).

AUTOMATIC1111 (2022) AUTOMATIC1111. 2022. Stable Diffusion WebUI. https://github.com/AUTOMATIC1111/stable-diffusion-webui

Cobbe et al . (2021) Karl Cobbe, Vineet Kosaraju, Mohammad Bavarian, Mark Chen, Heewoo Jun, Lukasz Kaiser, Matthias Plappert, Jerry Tworek, Jacob Hilton, Reiichiro Nakano, et al . 2021. Training verifiers to solve math word problems. arXiv preprint arXiv:2110.14168 (2021).

Darwen and Yao (1996) Paul Darwen and Xin Yao. 1996. Every niching method has its niche: Fitness sharing and implicit sharing compared. In Parallel Problem Solving from Nature—PPSN IV: International Conference on Evolutionary Computation—The 4th International Conference on Parallel Problem Solving from Nature Berlin, Germany, September 22–26, 1996 Proceedings 4 . Springer, 398–407.

De Jong (1975) Kenneth Alan De Jong. 1975. An analysis of the behavior of a class of genetic adaptive systems. University of Michigan.

Deb and Goldberg (1989) Kalyanmoy Deb and David E Goldberg. 1989. An investigation of niche and species formation in genetic function optimization. In Proceedings of the third international conference on Genetic algorithms . 42–50.

Goldberg et al . (1992) David E Goldberg, Kalyanmoy Deb, and Jeffrey Horn. 1992. Massive multimodality, deception, and genetic algorithms.. In PPSN , Vol. 2.

Goldberg et al . (1987) David E Goldberg, Jon Richardson, et al . 1987. Genetic algorithms with sharing for multimodal function optimization. In Genetic algorithms and their applications: Proceedings of the Second International Conference on Genetic Algorithms , Vol. 4149. Cambridge, MA, 414–425.

Hansen and Ostermeier (2001) Nikolaus Hansen and Andreas Ostermeier. 2001. Completely derandomized self-adaptation in evolution strategies. Evolutionary computation 9, 2 (2001), 159–195.

Heusel et al . (2017) Martin Heusel, Hubert Ramsauer, Thomas Unterthiner, Bernhard Nessler, and Sepp Hochreiter. 2017. Gans trained by a two time-scale update rule converge to a local nash equilibrium. Advances in neural information processing systems 30 (2017).

HuggingFace (2023) HuggingFace. 2023. Open LLM Leaderboard. https://huggingface.co/spaces/HuggingFaceH4/open_llm_leaderboard . HuggingFace.

Kuroki et al . (2024) So Kuroki, Taishi Nakamura, Takuya Akiba, and Yujin Tang. 2024. Agent Skill Acquisition for Large Language Models via CycleQD. arXiv preprint arXiv:2410.14735 (2024).

Labonne (2024) Maxime Labonne. 2024. Merge Large Language Models with mergekit. Hugging Face Blog. https://huggingface.co/blog/mlabonne/merge-models

Lin et al . (2014) Tsung-Yi Lin, Michael Maire, Serge Belongie, James Hays, Pietro Perona, Deva Ramanan, Piotr Dollár, and C Lawrence Zitnick. 2014. Microsoft coco: Common objects in context. In Computer Vision–ECCV 2014: 13th European Conference, Zurich, Switzerland, September 6-12, 2014, Proceedings, Part V 13 . Springer, 740–755.

Luo et al . (2023) Haipeng Luo, Qingfeng Sun, Can Xu, Pu Zhao, Jianguang Lou, Chongyang Tao, Xiubo Geng, Qingwei Lin, Shifeng Chen, and Dongmei Zhang. 2023. Wizardmath: Empowering mathematical reasoning for large language models via reinforced evol-instruct. arXiv preprint arXiv:2308.09583 (2023).

Mouret and Clune (2015) Jean-Baptiste Mouret and Jeff Clune. 2015. Illuminating search spaces by mapping elites. arXiv preprint arXiv:1504.04909 (2015).

Pétrowski (1996) Alain Pétrowski. 1996. A clearing procedure as a niching method for genetic algorithms. In Proceedings of IEEE international conference on evolutionary computation . IEEE, 798–803.

Podell et al . (2023) Dustin Podell, Zion English, Kyle Lacey, Andreas Blattmann, Tim Dockhorn, Jonas Müller, Joe Penna, and Robin Rombach. 2023. Sdxl: Improving latent diffusion models for high-resolution image synthesis. arXiv preprint arXiv:2307.01952 (2023).

Rombach et al . (2022) Robin Rombach, Andreas Blattmann, Dominik Lorenz, Patrick Esser, and Björn Ommer. 2022. High-resolution image synthesis with latent diffusion models. In Proceedings of the IEEE/CVF conference on computer vision and pattern recognition . 10684–10695.

RunDiffusion (2024) RunDiffusion. 2024. Juggernaut-XL-v9. https://huggingface.co/RunDiffusion/Juggernaut-XL-v9 . Accessed: January 2025.

Sakana AI (2025) Sakana AI. 2025. EvoSDXL-JP: Evolutionary Model Merging for Japanese-English Bilingual Text-to-Image Generation. https://sakana.ai/evosdxl-jp/ Accessed: 2025-01.

Secretan et al . (2008) Jimmy Secretan, Nicholas Beato, David B D Ambrosio, Adelein Rodriguez, Adam Campbell, and Kenneth O Stanley. 2008. Picbreeder: evolving pictures collaboratively online. In Proceedings of the SIGCHI conference on human factors in computing systems . 1759–1768.

Shing et al . ([n. d.]) Makoto Shing, Takuya Akiba, and Jerry Chi. [n. d.]. Japanese Stable Diffusion XL. [https://huggingface.co/stabilityai/japanese-stable-diffusion-xl](https://huggingface.co/stabilityai/japanese-stable-diffusion-xl)

Smith et al . (1993) Robert E Smith, Stephanie Forrest, and Alan S Perelson. 1993. Searching for diverse, cooperative populations with genetic algorithms. Evolutionary computation 1, 2 (1993), 127–149.

Stanley and Miikkulainen (2002) Kenneth O Stanley and Risto Miikkulainen. 2002. Evolving neural networks through augmenting topologies. Evolutionary computation 10, 2 (2002), 99–127.

Touvron et al . (2023) Hugo Touvron, Louis Martin, Kevin Stone, Peter Albert, Amjad Almahairi, Yasmine Babaei, Nikolay Bashlykov, Soumya Batra, Prajjwal Bhargava, Shruti Bhosale, et al . 2023. Llama 2: Open foundation and fine-tuned chat models. arXiv preprint arXiv:2307.09288 (2023).

Wallace et al . (2024) Bram Wallace, Meihua Dang, Rafael Rafailov, Linqi Zhou, Aaron Lou, Senthil Purushwalkam, Stefano Ermon, Caiming Xiong, Shafiq Joty, and Nikhil Naik. 2024. Diffusion model alignment using direct preference optimization. In Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition . 8228–8238.

White (2016) Tom White. 2016. Sampling generative networks. arXiv preprint arXiv:1609.04468 (2016).

Wong (2015) Ka-Chun Wong. 2015. Evolutionary multimodal optimization: A short survey. arXiv preprint arXiv:1508.00457 (2015).

Wong et al . (2012) Ka-Chun Wong, Chun-Ho Wu, Ricky KP Mok, Chengbin Peng, and Zhaolei Zhang. 2012. Evolutionary multimodal optimization using the principle of locality. Information Sciences 194 (2012), 138–170.

Xi et al . (2024) Zhiheng Xi, Yiwen Ding, Wenxiang Chen, Boyang Hong, Honglin Guo, Junzhe Wang, Dingwen Yang, Chenyang Liao, Xin Guo, Wei He, et al . 2024. AgentGym: Evolving Large Language Model-based Agents across Diverse Environments. arXiv preprint arXiv:2406.04151 (2024).

Yadav et al . (2023) Prateek Yadav, Derek Tam, Leshem Choshen, Colin Raffel, and Mohit Bansal. 2023. TIES-Merging: Resolving Interference When Merging Models. arXiv:2306.01708 [cs.LG] https://arxiv.org/abs/2306.01708

Yao et al . (2022) Shunyu Yao, Howard Chen, John Yang, and Karthik Narasimhan. 2022. Webshop: Towards scalable real-world web interaction with grounded language agents. Advances in Neural Information Processing Systems 35 (2022), 20744–20757.

Yoshikawa et al . (2017) Yuya Yoshikawa, Yutaro Shigeto, and Akikazu Takeuchi. 2017. STAIR captions: Constructing a large-scale Japanese image caption dataset. arXiv preprint arXiv:1705.00823 (2017).

Yu et al . (2024) Le Yu, Bowen Yu, Haiyang Yu, Fei Huang, and Yongbin Li. 2024. Language models are super mario: Absorbing abilities from homologous models as a free lunch. In Forty-first International Conference on Machine Learning .

## Instructions for reporting errors

We are continuing to improve HTML versions of papers, and your feedback helps enhance accessibility and mobile support. To report errors in the HTML that will help us improve conversion and rendering, choose any of the methods listed below:

Click the "Report Issue" ( ) button, located in the page header.

Tip: You can select the relevant text first, to include it in your report.

Our team has already identified the following issues . We appreciate your time reviewing and reporting rendering errors we may not have found yet. Your efforts will help us improve the HTML versions for all readers, because disability should not be a barrier to accessing research. Thank you for your continued support in championing open access for all.

Have a free development cycle? Help support accessibility at arXiv! Our collaborators at LaTeXML maintain a list of packages that need conversion , and welcome developer contributions .
