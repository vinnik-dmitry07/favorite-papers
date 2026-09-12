##### Report GitHub Issue

Content selection saved. Describe the issue below:

# MLE-bench: Evaluating Machine Learning Agents on Machine Learning Engineering

###### Abstract

We introduce MLE-bench, a benchmark for measuring how well AI agents perform at machine learning engineering. To this end, we curate 75 ML engineering-related competitions from Kaggle, creating a diverse set of challenging tasks that test real-world ML engineering skills such as training models, preparing datasets, and running experiments. We establish human baselines for each competition using Kaggle’s publicly available leaderboards. We use open-source agent scaffolds to evaluate several frontier language models on our benchmark, finding that the best-performing setup — OpenAI’s o1-preview with AIDE scaffolding — achieves at least the level of a Kaggle bronze medal in 16.9% of competitions. In addition to our main results, we investigate various forms of resource-scaling for AI agents and the impact of contamination from pre-training. We open-source our benchmark code ( github.com/openai/mle-bench/ ) to facilitate future research in understanding the ML engineering capabilities of AI agents.

## 1 Introduction

Language models (LMs) have achieved impressive performance on many coding benchmarks ( Chen et al., 2021 ; Hendrycks et al., 2021 ; Austin et al., 2021 ; Li et al., 2022 ) and are making progress on a variety of machine learning tasks, such as architecture design and model training ( Zheng et al., 2023 ; Huang et al., 2024b ) . LMs have also been adopted into programming tools ( Kalliamvakou, 2022 ) , and progress in agent scaffolding has increasingly automated developer workflows ( cognition.ai, 2024 ; Dohmke, 2024 ) . However, while there has been a surge in development on model and agent capabilities, few benchmarks holistically measure autonomous end-to-end ML engineering.

We introduce MLE-bench, an offline Kaggle competition environment for assessing how well AI agents can perform difficult machine learning engineering (MLE) tasks. We built MLE-bench to be a robust measure of real-world progress in autonomous ML engineering agents, focusing on two main design choices: (i) selecting tasks that are challenging and representative of contemporary ML engineering work, and (ii) being able to compare evaluation results to human-level performance.

The resulting benchmark consists of 75 diverse Kaggle competitions across a variety of domains, including natural language processing, computer vision, and signal processing. Many of the competitions are contemporary challenges with real-world value, such as OpenVaccine: COVID-19 mRNA Vaccine Degradation Prediction ( Das et al., 2020 ) and the Vesuvius Challenge for deciphering ancient scrolls ( Lourenco et al., 2023 ) . The total value of prizes awarded across the 75 competitions is $1,948,016 ($25,974 per competition on average).

AI agents that autonomously solve the types of challenges in our benchmark could unlock a great acceleration in scientific progress, a prospect that is exciting but also warrants careful understanding of model progress in order to deploy advancements in a safe and controlled manner. For example, MLE-bench can be used as a measure for model autonomy in OpenAI’s Preparedness Framework ( OpenAI, 2023 ) , autonomous capabilities in Anthropic’s Responsible Scaling Policy ( Anthropic, 2023 ) , and ML R&D in Google DeepMind’s Frontier Safety Framework ( Google DeepMind, 2024 ) .

We find that, when combined with open-source scaffolds, leading LMs achieve meaningful scores on our benchmark. The best-performing agent we evaluated, o1-preview with AIDE, uses scaffolding purpose-built for Kaggle competitions and achieves a medal in 16.9% of competitions on average. We find that performance significantly improves when agents are given multiple attempts per competition; for example, o1-preview’s score doubles from 16.9% using pass@1 to 34.1% using pass@8. Similarly, GPT-4o scores 8.7% given 24 hours to attempt each competition, but 11.8% when given 100 hours. In general, we found that agents can score well on competitions that can be solved with well-known approaches but struggle to debug issues and recover from missteps.

Our contributions include: 1. MLE-bench – a benchmark of 75 offline Kaggle competitions for evaluating ML engineering capabilities of AI agents, carefully handcrafted by a team of ML engineers.

2. Large-scale evaluations of state-of-the-art models and agent frameworks, revealing new information about the prospects and limits of autonomous ML engineering agents.

3. Experiments on scaling resources for agents, including scaling agent runtime, hardware resources, and pass@k attempts, exploring performance ceilings for present-day agents.

4. Experiments investigating the relationship between dataset contamination and agent performance, as well as agent-monitoring tools to detect plagiarism and cheating.

## 2 MLE-bench

MLE-bench consists of 75 machine learning engineering tasks manually sourced from Kaggle to reflect a core set of day-to-day skills that ML engineers use in frontier labs.

Kaggle is a platform that hosts data science and ML competitions requiring participants to build predictive models to solve challenges, often using real-world datasets. Participants compete to achieve the best score on a metric pre-defined for each competition, and are ranked on a leaderboard against one another. Bronze, silver, and gold medals are awarded for top competition results.

### 2.1 Dataset Curation

Each sample in MLE-bench is a Kaggle competition consisting of:

• A description scraped from the “Overview" and “Data" tabs of the competition website.

• The competition dataset , in most cases using a new train-test split (more details below).

• Grading code used to evaluate submissions locally.

• A snapshot of the competition’s leaderboard used to rank submissions against humans.

To arrive at the set of competitions constituting MLE-bench, we begin with the 5673 completed Kaggle competitions listed on the Meta Kaggle dataset 1 1 1 kaggle.com/datasets/kaggle/meta-kaggle (accessed May 15th, 2024)) . We exclude Community Competitions since their quality is less rigorously vetted than other competitions. We manually screen the remaining 586 competitions for relevance to modern-day ML engineering. We exclude competitions where we cannot replicate the grading procedure or cannot recreate reasonable train-test splits. See Appendix A.1 for the full list of screening criteria.

Additionally, we manually annotate the problem type of each competition (e.g. text classification, image segmentation, etc.). We also annotate each competition with a complexity level: Low if we estimate that an experienced ML engineer can produce a sensible solution in under 2 hours excluding the time taken to train any models, Medium if it takes between 2 and 10 hours, and High if it takes more than 10 hours. See Appendix A.2 for more details.

From this process, we select 75 competitions to include in MLE-bench, comprising 22 competitions Low in complexity (30 % \% ), 38 Medium (50 % \% ), and 15 High (20 % \% ). We include an additional 7 competitions as a development split, for developing agents without over-fitting to the test set. We recommend using the Low complexity split if using all splits is too resource-intensive.

For each competition, we use the original dataset if publicly available, although Kaggle competitions often do not release the test set even after the competition ends. In such cases, we manually create new train and test splits based on the publicly available training data 2 2 2 We discuss the splits further in Appendix A.7 . . We take care to ensure that the distributions of the original and reconstructed test sets are similar by checking that the example submission scores similarly on both sets. We take the new test set to be 10% of the original train set, except for when it didn’t make sense to do so 3 3 3 e.g. doing so for the “New York City Taxi Fare Prediction” competition would result in a test set 100x larger than the original, so we opted to maintain the original train/test ratio in such cases. . Due to these measures, we expect scores on the MLE-bench competition test sets to be comparable to human scores on the competition’s leaderboard, especially on average.

Finally, we implement the grading logic for each competition based on the described evaluation metric in the competition’s description, so that submissions can be graded locally. Evaluation metrics vary by competition, from standard metrics like area under the receiver operating characteristic (AUROC) to domain-specific loss functions.

### 2.2 Metrics

##### Leaderboards

We contextualize MLE-bench performance using the leaderboards 4 4 4 Snapshots of the Private leaderboard were taken between May and August 2024. of each Kaggle competition. On Kaggle, competitions may have two leaderboards: “Public" and “Private." We found that Kaggle submissions sometimes overfit to the Public leaderboard, so we opt to use the Private leaderboard.

##### Medals

Kaggle awards bronze, silver, and gold medals to top competitors based on their performance relative to the leaderboard ( Table 1 ). Similarly, MLE-bench awards medals to agents’ submissions by comparing them against the Private leaderboard, as if the agent were participating in the competition at the time. The thresholds for bronze, silver, and gold vary depending on the number of participants in a competition such that a given medal should always reflect a similar level of achievement across different competitions. Although not all competitions on Kaggle award medals, in MLE-bench we apply the medal thresholding logic to all competitions.

##### Headline metric

To provide a singular metric for MLE-bench, we calculate the percentage of attempts that are awarded any medal (bronze and above). This is designed to be a challenging metric, with a ceiling comparable to the achievements of the very best human Kagglers after years of cumulative effort. Only nine humans have ever achieved medals on 75 different Kaggle competitions 5 5 5 According to Meta Kaggle (last accessed 23rd October 2024), Kagglers titericz , kazanova , mathurinache , lucamassaron , mikeskim , abhishek , alexxanderlarko , confirm , and coreacasa each have more than 75 unique competition medals. An impressive achievement! .

##### Raw Scores

We also report the raw score achieved by models on each competition. This is useful to track competition-specific progress, though it is hard to aggregate scores across competitions since each competition uses different metrics.

### 2.3 Setup

MLE-bench is designed to be agnostic to the methods used to solve it, requiring only a CSV file to be submitted to each competition for grading. Nevertheless, we encourage developers to report certain details when evaluating their agents on this benchmark. Specifically, developers should mention the models and scaffolding used, whether the agent had internet access, available hardware, runtime, the inclusion of any partial or complete solutions to Kaggle competitions in the agent’s prompts, and any other significant deviations from our experimental setup described in Section 3 .

##### Validating submissions

Real-life Kaggle competitions often allow participants to make up to 5 submissions a day to the Public leaderboard, which checks the validity of their submission and provides a score. Analogously, we allow agents to access a local validation server to check the validity of their submission, though the tool does not provide a score (our tool uses the grader to check if a submission is valid, or provides an error message in the case of invalid submissions). There are no restrictions on how often agents can use this tool.

#### 2.3.1 Rules

Submissions must be produced by a model separate from the agent; the agent is forbidden from writing predictions directly to its submission file using its own knowledge of the world. This prevents agents from simply recalling labels from their pre-training data that it may have memorized, and ensures the agent engages in ML engineering. Agents are also forbidden from viewing solutions online, which can often be found on Kaggle or GitHub.

##### Rule-breaking detection

To ensure agents adhere to the rules, we provide a tool that inspects agent logs using GPT-4o. Specifically, the tool checks if the agent has broken the rules by manually writing the submission file without using a model, calling another external LLM API for assistance, or attempting to access unauthorized resources. Further details can be found in Appendix A.3 .

##### Plagiarism detection

To prevent plagiarism, we use the source code plagiarism detection tool Dolos ( Maertens et al., 2024 ) to compare the agent’s submitted code against the top 50 associated notebooks from the relevant Kaggle competition. These notebooks are publicly available on Kaggle and often contain successful solutions. For the purpose of our benchmark, we disqualify any attempts where the agent submits code with a high similarity score (over 60%) to any notebook and flag them for further review.

These rules are designed to prevent cheating. We further discuss the risk of score inflation via train-time contamination in Section 4 , and the limits of our mitigations in Section 6 .

## 3 Experiments and Results

In our experiments, we run agents in an Ubuntu 20.04 Docker container containing the dataset, validation server, and Python packages that might be helpful for ML engineering. Containers are executed in a secure cluster environment. For each of the 75 competitions, agents have a maximum of 24 hours to produce a submission. On each run, agents have access to a machine with 36 vCPUs, 440GB RAM, 4095 GiB SSD, and a single Nvidia A10 GPU. We repeat all experiments with 3 seeds (that is, 3 runs per competition) to compute the mean and standard error unless otherwise specified. Full details of our execution environment and scaffolds can be found in Appendices A.5 and A.6 .

### 3.1 Main experiment

##### Varying scaffolding

To determine the best-performing scaffold, we evaluate GPT-4o 6 6 6 gpt-4o-2024-08-06 using three open-source scaffolds: AIDE ( Schmidt et al., 2024 ) , ResearchAgent (referred to as “MLAB") from MLAgentBench ( Huang et al., 2024b ) , and CodeActAgent (referred to as “OpenHands") from the OpenHands platform ( Wang et al., 2024 ) . We make minor modifications to each scaffold to enhance their performance on the benchmark (details in Appendix A.6 ), and report results in Table 2 .

We find that GPT-4o (AIDE) achieves more medals on average than both MLAB and OpenHands (8.7% vs. 0.8% and 4.4% respectively), despite making a similar number of valid submissions. Notably, AIDE is purpose-built for Kaggle competitions, whereas the other scaffolds are general-purpose. See Figure 2 for a snippet of each scaffold’s trajectories.

##### Varying models

Taking the best-performing scaffold (AIDE) from the previous experiment, we experiment with changing the underlying model. We evaluate four different models 7 7 7 We attempted to evaluate Gemini-1.5-Pro (Gemini-1.5-Pro-002) but found API calls repeatedly blocked due to model outputs being flagged for recitation. with AIDE: o1-preview and GPT-4o (OpenAI), Claude 3.5 Sonnet 8 8 8 claude-3-5-sonnet-20240620 (Anthropic), and Llama 3.1 405B 9 9 9 meta-llama/llama-3.1-405b-instruct served by https://openrouter.ai/ (Meta).

We find that o1-preview significantly outperforms all other models, achieving a medal on 16.9% of competitions - almost twice the number of medals on average as the next best model ( Table 2 ). We note that qualifying as a Kaggle Grandmaster 10 10 10 See Kaggle Progression System here: https://www.kaggle.com/progression requires 5 gold medals, while o1-preview achieves an average of 7 gold medals on MLE-bench. This comes with the following caveats: not all our chosen competitions are medal-granting, MLE-bench uses slightly modified datasets and grading, and agents have the advantage of using more recent technology than the participants in many cases.

##### Discussion

All agents often failed to create valid submissions, despite having access to the validation server. When analyzing agent transcripts we found that they did not always use the validation server, despite their prompts encouraging them to do so.

We found that MLAB and OpenHands tend to end their runs early, sometimes within the first few minutes, despite being told to optimize their scores as much as possible for the full 24-hour duration. In contrast, the AIDE scaffold repeatedly prompts models to improve their score until the full 24 hours is up, or when it has generated 500 nodes (the maximum we allow).

Small details in scaffold implementations can make a big difference. MLAB and OpenHands are given a variety of tools to solve open-ended tasks, though this flexibility also increases the risk surface area for failure. For example, MLAB often attempted to inspect files that were thousands of lines long, which ended up filling its context window. We fixed many of the most obvious failures in each agent (detailed in Appendix A.6 ), but expect failure modes to remain.

All three agents failed to effectively factor in compute and time limitations to their strategies. For example, they would execute commands that overload the machine’s disk or RAM, resulting in their process getting killed and their run finishing early. Additionally, agents rarely verbalized any consideration of how long their produced code would run for.

See Table 9 and Table 10 for our headline results broken down by complexity level and task category respectively. We also visualize performance on individual competitions as a function of the competition date for various models in Figure 9 .

### 3.2 Increasing number of attempts

To see how performance changes with more attempts, we evaluate GPT-4o (AIDE) and o1-preview (AIDE) using the pass@ k metric ( Chen et al., 2021 ) . We estimate the percentage of competitions in which the agent achieves a medal given k k attempts at each competition, drawn from n n seeds:

pass@ ​ k := 𝔼 Competitions ​ [ 1 − ( n − c k ) ( n k ) ] \text{pass@}k:=\underset{\text{Competitions}}{\mathbb{E}}\left[1-\dfrac{\binom{n-c}{k}}{\binom{n}{k}}\right]

The main result for k ∈ [ 1 , n 2 ] k\in\left[1,\frac{n}{2}\right] is shown in Figure 3 . We see a consistent increase in the percentage of medals achieved as the number of attempts increases for both agents.

### 3.3 Varying amount of compute available

Our main experiments give agents access to a single 24GB A10 GPU, whereas Kaggle provides a free 16GB P100 GPU to users, who often also use their own hardware to compete. In this experiment, we investigate how agents’ performance may be affected by our choice of hardware, or if they may even adapt their strategies depending on the hardware available (e.g. training smaller models when only CPU(s) are available, and training larger models when GPU(s) are available).

We compare the performance of GPT-4o (AIDE) on three different hardware setups, varying between our standard setup with a single A10 GPU, CPU-only, and two A10 GPUs.

Surprisingly, we find that GPT-4o (AIDE) performs similarly in all experiments. We manually viewed several logs from the “Extra GPU” experiment, and didn’t identify any attempts from GPT-4o AIDE to use the second GPU. See Table 3 for results.

### 3.4 Increasing time available

Our main experiments limit the amount of time per competition attempt to 24 hours; in contrast, human contestants often have weeks or months to work on Kaggle competitions. Increasing the time limit gives agents more time to iterate on their solutions, and permits more time for model-training. We run an experiment providing GPT-4o (AIDE) with a longer time limit of 100 hours per competition and increase the maximum nodes allowed by 10x to 5,000. We take snapshots of the agent’s best attempt every hour and grade each snapshot. See Figure 5 for the results.

We find that GPT-4o (AIDE) achieves a significant number of medals in the first couple hours of execution, then slowly accumulates more medals over the course of the run. Sometimes the number of medals GPT-4o (AIDE) achieves actually decreases, which is due to the imperfect method AIDE uses to select its “best" attempt.

## 4 Contamination & Plagiarism

Dekoninck et al. (2024) define contamination as artificially inflated and non-generalizing benchmark performance. For MLE-bench, we are most concerned about results being artificially inflated due to models developing solutions derived from public solutions of a given competition.

In the following sections, we investigate the effect of contamination by measuring the correlation between GPT-4o’s familiarity with competition winners’ discussion posts and its performance. We also run a variant of the benchmark with obfuscated instructions to make each competition less recognizable. Our experiments find no evidence of results being systematically inflated due to memorization.

In addition to investigating contamination, we run the plagiarism detector on all medal-winning submissions and find no evidence of plagiarism (Appendix A.4 ). We also run the log analysis tool and manually inspect any flagged violations but find no cases of rule-breaking (Appendix A.3 ).

### 4.1 Familiarity with top solutions

Blatant plagiarism can be detected using off-the-shelf detection tools, but contamination may have subtler effects if models have trained on discussions of winning solutions and adopt their high-level strategies, which could still lead to non-generalizing performance on new ML engineering tasks.

We investigate this effect in GPT-4o’s base model by measuring its familiarity with the competitions and their winning strategies. Previous work suggests that models place higher probabilities on the tokens of documents seen during training ( Carlini et al., 2023 ) . Thus, we define a model’s familiarity with a given document as the mean probability a model assigns to each token in that document, conditional on all preceding tokens. For each competition, we calculate the model’s mean familiarity with the main competition page and the 5 most popular discussion posts 11 11 11 Typically, these are posts by the competition winners sharing their approach. for that competition.

Figure 5 shows the result of this analysis. We find no correlation between the familiarity of GPT-4o’s base model with a competition and its performance on that competition.

### 4.2 Obfuscating competition descriptions

We run an additional experiment to investigate how contamination might affect our results: If models rely on matching familiar problems to memorized solutions, making the competitions unrecognizable may mitigate this effect.

We manually rewrite the competition descriptions of all 75 competitions in MLE-bench to obfuscate the provenance of each competition whilst retaining the key information. For example, we remove all references to Kaggle and the competition’s name, and cut out text that is not strictly required. See Appendix A.8 for an example obfuscated description.

We run GPT-4o (AIDE) with 10 seeds on these obfuscated descriptions. We see that GPT-4o (AIDE) achieves similar scores on both the original and obfuscated competition descriptions. See Table 4 for results.

In summary, our experiments suggest that GPT-4o’s familiarity with Kaggle competitions does not systematically inflate its scores. Furthermore, we find no evidence of GPT-4o being over-reliant on the original form of the competition descriptions. This does not rule out subtler effects of contamination, but our findings suggest that contamination effects are minimal on our results.

## 5 Related Work

Evaluating Software Engineering Capabilities . Chen et al. (2021) ; Hendrycks et al. (2021) ; Austin et al. (2021) ; Jain et al. (2024) evaluate models’ abilities to produce code following a natural language description. Frontier models are saturating many of these benchmarks 12 12 12 AgentCoder ( Huang et al., 2024a ) achieves 96.3% and 91.8% on HumanEval and MBPP respectively. , yet have failed to automate the job of a software engineer. SWE-bench ( Jimenez et al., 2024 ) tasks models to solve real-world pull requests from open-source repositories. Despite its challenging nature, performance on SWE-bench has been steadily increasing ( Zhang et al., 2024 ; factory.ai, 2024 ) . In contrast, the problems in MLE-bench are often more open-ended and difficult (for example, some are open research problems). However, MLE-bench may similarly see rapid progress as in SWE-bench, making it important to measure early.

Evaluating ML Engineering Capabilities . MLE-bench is not the first benchmark to use Kaggle competitions to measure autonomous ML engineering capabilities. MLAgentBench ( Huang et al., 2024b ) takes 13 tasks from Kaggle and bespoke ML tasks, provides a simple baseline solution for each, and evaluates how often agents can achieve at least a 10% improvement over the baseline solution. In contrast, MLE-bench provides significantly more tasks with more complexity, and requires agents to attempt the task from scratch.

Another benchmark, ML-Bench ( Tang et al., 2024 ) , tests agents’ abilities to generate code and execute commands to interact with popular ML repositories. Compared to MLE-bench, ML-Bench measures understanding and effective application of pre-existing codebases rather than developing ML solutions to open-ended problems.

Weco AI’s report of AIDE ( Schmidt et al., 2024 ) claims to beat > > 50% of human competitors on data science competitions from Kaggle. We find state-of-the-art models available at the time of AIDE’s announcement would only surpass the median score in MLE-bench ∼ \sim 10% of the time, far short of 50%. We take this as evidence that our selection of competitions is more difficult than Weco AI’s.

In work concurrent to ours, DSBench ( Jing et al., 2024 ) also introduces a benchmark of Kaggle competitions, but much like Weco AI’s dataset, DSBench focuses on data science tasks. There is some overlap between our datasets, but DSBench’s filtering criteria removes any competitions whose datasets do not fit a simple template that is used to automate task creation. This precludes many interesting competitions with non-standard formats. In contrast, each competition in MLE-bench has been manually ported over by our team, resulting in more diverse and challenging tasks.

Evaluating AI Agents . SWE-bench, MLAgentBench, and MLE-bench are multi-step benchmarks evaluating AI agents in the software domain. Here, components such as LMs, retrieval, and external tools are “scaffolded” together via code, unlocking new levels of autonomy unattainable via a single inference call ( Zaharia et al., 2024 ) . AgentBench ( Liu et al., 2023 ) provides environments for agents to complete multi-turn challenges, such as editing permissions on a Linux OS. GAIA ( Mialon et al., 2023 ) focuses on agent interactions with the real world, providing 466 questions that are conceptually simple for humans but challenging for current AI systems. Gioacchini et al. (2024) propose AgentQuest, a modular agent evaluation framework designed for extensibility, and Kapoor et al. (2024) provide an analysis of agent evaluation efforts so far.

## 6 Limitations

Contamination & plagiarism. Since our dataset consists of public Kaggle competitions (Appendix A.7 ), it’s possible that models have trained on all public Kaggle material including competition details, solutions, and even the datasets including our test set 13 13 13 In early experiments, we found GPT-4’s base model could reproduce several rows from the dataset of the “Titanic - Machine Learning from Disaster” competition when given the first few rows as a prompt. . There is therefore a risk that models have memorized answers or intuitions about the solutions such that MLE-bench over-represents model capabilities. We have mitigations in place to prevent plagiarism of the top participants’ code or test labels (log analysis and plagiarism detector), but it is difficult to detect the reuse of high-level strategies. Our experiments (Section 4 ) find no systematic effect of contamination for GPT-4o, but make no guarantees about future models. Future work may seek to regularly update MLE-bench with new Kaggle competitions to stay ahead of contamination issues.

Coverage of AI R&D capabilities. We built MLE-bench to better understand the risk of AI R&D acceleration via automated ML engineers, but the tasks included in MLE-bench don’t cover the full spectrum of capabilities required for AI R&D. MLE-bench selects for Kaggle competitions that provide clear problem statements, datasets that are clean and well-documented, and have clear metrics for optimization. On the other hand, real-world AI R&D often may not even have a clear problem statement, and figuring out the dataset and metrics is part of the problem. Nevertheless, MLE-bench evaluates many core competencies involved in AI R&D, including preparing large multi-modal datasets, managing long-running training scripts, and debugging poor-performing models.

Differences to real competitions. MLE-bench uses different train-test splits to the original competitions on Kaggle and re-implements their grading code. This raises concerns about how comparable our scores are to the human leaderboards from Kaggle. We have been careful to implement our competitions in a way that the new train and test sets retain a similar distribution as the original sets, and confirm that sample and gold submissions lead to results consistent with the human leaderboard. A further concern is that algorithmic progress may result in older competitions being easier, as agents with today’s knowledge and tools have advantages over the original participants. To account for this, we label competitions with complexity levels from the point of view of an ML engineer today, and we may yet need to update the complexity annotations as capabilities advance.

Accessibility : MLE-bench is a particularly resource-intensive benchmark to run. A single run of our main experiment setup of 24 hours per competition attempt requires 24 ​ hours × 75 ​ competitions = 1800 ​ GPU hours of compute 24\text{ hours}\times 75\text{ competitions}=1800\text{ GPU hours of compute} . Furthermore, running agents for the whole duration is very token-intensive. In our experiments, o1-preview with AIDE used 127.5M input tokens and 15.0M output tokens on average for one seed of 75 competitions.

## 7 Conclusion

We introduce MLE-bench, a benchmark designed to evaluate AI agents on ML engineering tasks using challenging Kaggle competitions. By closely simulating the experience of participating in a Kaggle competition, MLE-bench enables a direct comparison between agents and human competitors. Our experiments show that frontier models combined with agent scaffolding – specifically, o1-preview with AIDE – can achieve a medal in 16.9% of competitions. By open-sourcing MLE-bench, we aim to facilitate further research in evaluating ML engineering capabilities of agents. Ultimately, we hope our work contributes to a deeper understanding of the capabilities of agents in autonomously executing ML engineering tasks, which is essential for the safe deployment of more powerful models in the future.

##### Ethics Statement

If AI agents become capable of autonomously performing ML research, they could have numerous positive impacts, such as accelerating scientific progress in healthcare, climate science, and other domains, accelerating safety and alignment research of models, and fostering economic growth through the development of new products. The capacity of agents to perform high-quality research could mark a transformative step in the economy.

However, agents capable of performing open-ended ML research tasks, at the level of improving their own training code, could improve the capabilities of frontier models significantly faster than human researchers. If innovations are produced faster than our ability to understand their impacts, we risk developing models capable of catastrophic harm or misuse without parallel developments in securing, aligning, and controlling such models.

We believe a model capable of solving a large fraction of MLE-bench likely possesses the capability to execute many open-ended ML tasks. We are open-sourcing MLE-bench to aid research into the agentic capabilities of language models and increase transparency into acceleration risks at research labs. As we do so, we recognize the limitations of MLE-bench and strongly encourage the development of more evaluations of automated ML research capabilities, especially those more specific to the workflow of researchers training large language models.

Our benchmark uses publicly available Kaggle competitions. No sensitive data is used, and code is provided to allow users to reproduce datasets in a way that complies with relevant licenses.

##### Reproducibility Statement

We have taken care to ensure that our setup is fully reproducible. We provide all necessary details for reproducing our results, including dataset curation, evaluation metrics, and experimental setup. Our codebase is publicly available, including code for reproducing the full benchmark and experiments. The code for scalably running agents is infrastructure-specific so not included, but we provide examples for running agents on MLE-bench which can be adapted to the user’s own infrastructure. As discussed in Section 6 , users may find it difficult to fully reproduce our experiments due to compute and token costs.

## References

Anthropic (2023) Anthropic. Anthropic’s Responsible Scaling Policy, Version 1.0, September 2023.

Austin et al. (2021) Jacob Austin, Augustus Odena, Maxwell Nye, Maarten Bosma, Henryk Michalewski, David Dohan, Ellen Jiang, Carrie Cai, Michael Terry, Quoc Le, and Charles Sutton. Program Synthesis with Large Language Models, August 2021. URL http://arxiv.org/abs/2108.07732 . arXiv:2108.07732 [cs].

Carlini et al. (2023) Nicholas Carlini, Daphne Ippolito, Matthew Jagielski, Katherine Lee, Florian Tramer, and Chiyuan Zhang. Quantifying Memorization Across Neural Language Models, March 2023. URL http://arxiv.org/abs/2202.07646 . arXiv:2202.07646 [cs].

Chen et al. (2021) Mark Chen, Jerry Tworek, Heewoo Jun, Qiming Yuan, Henrique Ponde de Oliveira Pinto, Jared Kaplan, Harri Edwards, Yuri Burda, Nicholas Joseph, Greg Brockman, Alex Ray, Raul Puri, Gretchen Krueger, Michael Petrov, Heidy Khlaaf, Girish Sastry, Pamela Mishkin, Brooke Chan, Scott Gray, Nick Ryder, Mikhail Pavlov, Alethea Power, Lukasz Kaiser, Mohammad Bavarian, Clemens Winter, Philippe Tillet, Felipe Petroski Such, Dave Cummings, Matthias Plappert, Fotios Chantzis, Elizabeth Barnes, Ariel Herbert-Voss, William Hebgen Guss, Alex Nichol, Alex Paino, Nikolas Tezak, Jie Tang, Igor Babuschkin, Suchir Balaji, Shantanu Jain, William Saunders, Christopher Hesse, Andrew N. Carr, Jan Leike, Josh Achiam, Vedant Misra, Evan Morikawa, Alec Radford, Matthew Knight, Miles Brundage, Mira Murati, Katie Mayer, Peter Welinder, Bob McGrew, Dario Amodei, Sam McCandlish, Ilya Sutskever, and Wojciech Zaremba. Evaluating Large Language Models Trained on Code, July 2021. URL http://arxiv.org/abs/2107.03374 . arXiv:2107.03374 [cs].

cognition.ai (2024) cognition.ai. Cognition | Introducing Devin, the first AI software engineer, March 2024. URL https://cognition.ai/ .

Das et al. (2020) Rhiju Das, H Wayment-Steele, Do Soon Kim, Christian Choe, Bojan Tunguz, Walter Reade, and Maggie Demkin. Openvaccine: Covid-19 mrna vaccine degradation prediction, 2020. URL https://kaggle.com/competitions/stanford-covid-vaccine .

Dekoninck et al. (2024) Jasper Dekoninck, Mark Niklas Müller, and Martin Vechev. ConStat: Performance-Based Contamination Detection in Large Language Models, May 2024. URL http://arxiv.org/abs/2405.16281 . arXiv:2405.16281 [cs].

Dohmke (2024) Thomas Dohmke. GitHub Copilot Workspace: Welcome to the Copilot-native developer environment, April 2024. URL https://github.blog/news-insights/product-news/github-copilot-workspace/ .

factory.ai (2024) factory.ai. Code Droid Technical Report, June 2024. URL https://www.factory.ai/news/code-droid-technical-report .

Gioacchini et al. (2024) Luca Gioacchini, Giuseppe Siracusano, Davide Sanvito, Kiril Gashteovski, David Friede, Roberto Bifulco, and Carolin Lawrence. AgentQuest: A Modular Benchmark Framework to Measure Progress and Improve LLM Agents, April 2024. URL http://arxiv.org/abs/2404.06411 . arXiv:2404.06411 [cs].

Google DeepMind (2024) Google DeepMind. Frontier Safety Framework, May 2024.

Hendrycks et al. (2021) Dan Hendrycks, Steven Basart, Saurav Kadavath, Mantas Mazeika, Akul Arora, Ethan Guo, Collin Burns, Samir Puranik, Horace He, Dawn Song, and Jacob Steinhardt. Measuring Coding Challenge Competence With APPS, November 2021. URL http://arxiv.org/abs/2105.09938 . arXiv:2105.09938 [cs].

Huang et al. (2024a) Dong Huang, Jie M. Zhang, Michael Luck, Qingwen Bu, Yuhao Qing, and Heming Cui. AgentCoder: Multi-Agent-based Code Generation with Iterative Testing and Optimisation, May 2024a. URL http://arxiv.org/abs/2312.13010 . arXiv:2312.13010 [cs].

Huang et al. (2024b) Qian Huang, Jian Vora, Percy Liang, and Jure Leskovec. MLAgentBench: Evaluating Language Agents on Machine Learning Experimentation. In Forty-first International Conference on Machine Learning , June 2024b. URL https://openreview.net/forum?id=1Fs1LvjYQW .

Jain et al. (2024) Naman Jain, King Han, Alex Gu, Wen-Ding Li, Fanjia Yan, Tianjun Zhang, Sida Wang, Armando Solar-Lezama, Koushik Sen, and Ion Stoica. LiveCodeBench: Holistic and Contamination Free Evaluation of Large Language Models for Code, June 2024. URL http://arxiv.org/abs/2403.07974 . arXiv:2403.07974 [cs].

Jimenez et al. (2024) Carlos E. Jimenez, John Yang, Alexander Wettig, Shunyu Yao, Kexin Pei, Ofir Press, and Karthik Narasimhan. SWE-bench: Can Language Models Resolve Real-World GitHub Issues?, April 2024. URL http://arxiv.org/abs/2310.06770 . arXiv:2310.06770 [cs].

Jing et al. (2024) Liqiang Jing, Zhehui Huang, Xiaoyang Wang, Wenlin Yao, Wenhao Yu, Kaixin Ma, Hongming Zhang, Xinya Du, and Dong Yu. DSBench: How Far Are Data Science Agents to Becoming Data Science Experts?, September 2024. URL http://arxiv.org/abs/2409.07703 . arXiv:2409.07703 [cs].

Kaggle (2024) Kaggle. Kaggle Progression System | Kaggle, 2024. URL https://www.kaggle.com/progression .

Kalliamvakou (2022) Eirini Kalliamvakou. Research: quantifying GitHub Copilot’s impact on developer productivity and happiness, September 2022. URL https://github.blog/news-insights/research/research-quantifying-github-copilots-impact-on-developer-productivity-and-happiness/ .

Kapoor et al. (2024) Sayash Kapoor, Benedikt Stroebl, Zachary S. Siegel, Nitya Nadgir, and Arvind Narayanan. AI Agents That Matter, July 2024. URL http://arxiv.org/abs/2407.01502 . arXiv:2407.01502 [cs].

Li et al. (2022) Yujia Li, David Choi, Junyoung Chung, Nate Kushman, Julian Schrittwieser, Rémi Leblond, Tom Eccles, James Keeling, Felix Gimeno, Agustin Dal Lago, Thomas Hubert, Peter Choy, Cyprien De Masson d’Autume, Igor Babuschkin, Xinyun Chen, Po-Sen Huang, Johannes Welbl, Sven Gowal, Alexey Cherepanov, James Molloy, Daniel J. Mankowitz, Esme Sutherland Robson, Pushmeet Kohli, Nando De Freitas, Koray Kavukcuoglu, and Oriol Vinyals. Competition-level code generation with AlphaCode. Science , 378(6624):1092–1097, December 2022. ISSN 0036-8075, 1095-9203. doi: 10.1126/science.abq1158 . URL https://www.science.org/doi/10.1126/science.abq1158 .

Liu et al. (2023) Xiao Liu, Hao Yu, Hanchen Zhang, Yifan Xu, Xuanyu Lei, Hanyu Lai, Yu Gu, Hangliang Ding, Kaiwen Men, Kejuan Yang, Shudan Zhang, Xiang Deng, Aohan Zeng, Zhengxiao Du, Chenhui Zhang, Sheng Shen, Tianjun Zhang, Yu Su, Huan Sun, Minlie Huang, Yuxiao Dong, and Jie Tang. AgentBench: Evaluating LLMs as Agents, October 2023. URL http://arxiv.org/abs/2308.03688 . arXiv:2308.03688 [cs].

Lourenco et al. (2023) Alex Lourenco, Brent Seales, Christy Chapman, Daniel Havir, Ian Janicki, JP Posma, Nat Friedman, Ryan Holbrook, Seth P., Stephen Parsons, and Will Cukierski. Vesuvius challenge - ink detection, 2023. URL https://kaggle.com/competitions/vesuvius-challenge-ink-detection .

Maertens et al. (2024) Rien Maertens, Maarten Van Neyghem, Maxiem Geldhof, Charlotte Van Petegem, Niko Strijbol, Peter Dawyndt, and Bart Mesuere. Discovering and exploring cases of educational source code plagiarism with Dolos, 2024. URL https://github.com/dodona-edu/dolos . Publication Title: SoftwareX original-date: 2019-06-23T15:12:32Z.

Mialon et al. (2023) Grégoire Mialon, Clémentine Fourrier, Craig Swift, Thomas Wolf, Yann LeCun, and Thomas Scialom. GAIA: a benchmark for General AI Assistants, November 2023. URL http://arxiv.org/abs/2311.12983 . arXiv:2311.12983 [cs].

OpenAI (2023) OpenAI. Preparedness Framework, December 2023.

Schmidt et al. (2024) Dominik Schmidt, Zhengyao Jiang, and Yuxiang Wu. Introducing Weco AIDE, April 2024. URL https://www.weco.ai/blog/technical-report .

Tang et al. (2024) Xiangru Tang, Yuliang Liu, Zefan Cai, Yanjun Shao, Junjie Lu, Yichi Zhang, Zexuan Deng, Helan Hu, Kaikai An, Ruijun Huang, Shuzheng Si, Sheng Chen, Haozhe Zhao, Liang Chen, Yan Wang, Tianyu Liu, Zhiwei Jiang, Baobao Chang, Yin Fang, Yujia Qin, Wangchunshu Zhou, Yilun Zhao, Arman Cohan, and Mark Gerstein. ML-Bench: Evaluating Large Language Models and Agents for Machine Learning Tasks on Repository-Level Code, August 2024. URL http://arxiv.org/abs/2311.09835 .

Wang et al. (2024) Xingyao Wang, Boxuan Li, Yufan Song, Frank F. Xu, Xiangru Tang, Mingchen Zhuge, Jiayi Pan, Yueqi Song, Bowen Li, Jaskirat Singh, Hoang H. Tran, Fuqiang Li, Ren Ma, Mingzhang Zheng, Bill Qian, Yanjun Shao, Niklas Muennighoff, Yizhe Zhang, Binyuan Hui, Junyang Lin, Robert Brennan, Hao Peng, Heng Ji, and Graham Neubig. OpenDevin: An Open Platform for AI Software Developers as Generalist Agents, 2024. URL https://arxiv.org/abs/2407.16741 .

Zaharia et al. (2024) Matei Zaharia, Omar Khattab, Lingjiao Chen, Jared Quincy Davis, Heather Miller, Chris Potts, James Zou, Michael Carbin, Jonathan Frankle, Naveen Rao, and Ali Ghodsi. The shift from models to compound ai systems, 2024. URL http://bair.berkeley.edu/blog/2024/02/18/compound-ai-systems/ .

Zhang et al. (2024) Yuntong Zhang, Haifeng Ruan, Zhiyu Fan, and Abhik Roychoudhury. AutoCodeRover: Autonomous Program Improvement, July 2024. URL http://arxiv.org/abs/2404.05427 . arXiv:2404.05427 [cs].

Zheng et al. (2023) Mingkai Zheng, Xiu Su, Shan You, Fei Wang, Chen Qian, Chang Xu, and Samuel Albanie. Can GPT-4 Perform Neural Architecture Search?, August 2023. URL http://arxiv.org/abs/2304.10970 . arXiv:2304.10970 [cs].

## Appendix A Appendix

### A.1 Dataset Curation Criteria

We manually filter candidate competitions according to the following criteria. Each competition in our final set was screened by at least two ML engineers working at leading AI companies.

1. The competition requires ML engineering capabilities in order to achieve a medal, specifically those relevant for modern-day ML.

2. The competition description is well-specified enough to be solvable, i.e. there are no obvious missing components or crucial information that is inaccessible. We found the description to be detailed and thorough without any major ambiguities about how to approach that might only be resolved in the Discussion tab or external materials.

3. The competition’s evaluation metric can be computed locally.

4. The competition must have finished and is therefore unlikely to change (and, for some competitions, the test set is now publicly available).

5. The dataset isn’t used extensively outside of Kaggle (e.g. we avoid datasets like MNIST).

6. The train and test sets are from the same distribution, such that it is feasible to create a new train and test split from the public training data.

7. The final submission must be a CSV file (or, in the case of code competitions, must produce a CSV when the submitted notebook is run).

8. The competition doesn’t require downloading data from websites other than Kaggle.

9. The dataset’s license doesn’t restrict its inclusion in our benchmark.

### A.2 Distribution of Competitions

We provide a high-level overview of the problem category and complexity level distributions in MLE-bench in Figure 6 . Both the problem category and complexity were manually labeled.

### A.3 Runs analysis

We provide a code and log analysis tool that processes logs and code outputs from agent runs with GPT-4o mini 14 14 14 gpt-4o-mini-2024-07-18 using the rubric of questions in Table 5 .

We run the code and log analysis tool on all medal-winning submissions. See Table 6 for results of the analysis tool.

We found gpt-4o-mini to be overly cautious, flagging valid behaviors as violations even when they were not. The tool detected violations in the o1-preview AIDE and gpt-4o OpenHands runs; however each violation was determined to be a false positive after human review.

### A.4 Plagiarism detection tool

We use the source code plagiarism detection tool Dolos ( Maertens et al., 2024 ) to check submissions for plagiarism of top associated notebooks from each Kaggle competition.

The Dolos algorithm is explained in https://dolos.ugent.be/about/algorithm.html . To summarize: Dolos tokenizes code to make plagiarism detection invariant to the specific naming of variables and functions. It then fingerprints files according to sub-sequences of k-length tokens (we use the default setting of k=23). Pairs of files (in our case, a file from a submission and a notebook from Kaggle) are given a similarity score based on the fraction of shared fingerprints between the two files.

We surface any submission file with a similarity score above 60% for human review of potential plagiarism, finding no detected cases of plagiarism.

### A.5 Setup details

In our experiments, unless otherwise stated, each agent is executed within a Microsoft Azure Standard_NV36ads_A10_v5 virtual machine, which has 36 AMD EPYC 74F3v (Milan) [x86-64] vCPUs, 440GB memory, and one Nvidia A10 GPU (24GB). Each agent has full write access to a 4095 GiB SSD which it uses to produce its final submission and create any intermediate files. We use Docker bind mounts to give agents access to the relevant datasets for the competition they are solving.

We execute agents within Docker containers with the sysbox runtime. Note that our evaluation infrastructure does not rely on the Docker container-to-host isolation or the virtual machine boundary for security, and our cluster environment is itself designed to be robust. Each agent is executed using a Python virtual environment containing packages necessary and useful for the agents. We passed the instructions directly to AIDE and OpenHands on execution, and instructed MLAgentBench to read a file including the instructions.

### A.6 Scaffold details

Table 7 details the hyperparameters for each of our 3 tested scaffolds: the data science agent AIDE from Schmidt et al. (2024) , OpenHands’ CodeActAgent ( Wang et al., 2024 ) , and MLAgentBench’s ResearchAgent ( Huang et al., 2024b ) .

For all scaffolds we ensure that the agent is prompted with the total time available to complete the task, the timeout any code execution has before being forcibly terminated (if any), and the hardware available. See Figure 8 for the prompt used for all agents. We additionally insert information about the time and steps remaining into the end-of-turn prompt for all scaffolds.

In the following, we describe any further scaffold-specific modifications to address common pitfalls and improve the robustness of the agents.

#### A.6.1 AIDE modifications

• Implement exponential backoff on API call rate limits to handle high traffic scenarios.

• Add strict: True to Function Calling outputs to ensure stricter enforcement of output format rules, preventing invalid feedback responses.

• Add support for the Gemini and OpenRouter backends, and improve the Anthropic backend to enhance overall backend logic and response handling.

• Update internal prompts to emphasize the importance of creating a valid submission.csv file, as this was previously under-emphasized.

• Truncate excessively long data previews to prevent overwhelming the agent.

• Handle cases where input files are saved as .json instead of the required .jsonl format to prevent errors when processing submissions.

• Actively track whether a solution generates a submission.csv file; flag solutions that fail to produce this file as buggy.

• Modify solution selection criteria to consider not only performance metrics but also whether a valid submission.csv file was created.

• Add an option to obfuscate references to Kaggle, used in subsection 4.2 .

#### A.6.2 OpenHands modifications

As our cluster infrastructure requires agents to be packaged within Docker containers, and OpenHands also manages its own sub-containers, we end up with a Docker-in-Docker situation when running OpenHands. We make modifications to the OpenHands Docker configuration to enable GPU passthrough to the code agent, enable full use of the host disk space, and set the RAM allowance to 100GiB. We make no modifications to the scaffold in terms of tooling or behavior.

#### A.6.3 MLAB modifications

• Add "Validate Submission" tool as a low-level action available to the agent, with the following description: "Use the benchmark-provided tool to validate the format of your submission. You must provide the path to a submission file."

• Add automatic retries with the tenacity library to the complete_text_openai function for any OpenAI API Errors; return the error message to the agent after a maximum of 10 retries.

• To discourage agents from ending their runs early, we modify the description of the “Final Answer” tool to make it clear that the agent should not use this tool unless it has exhausted all avenues for improving their solution.

• Include full error messages in all EnvException exceptions so that the agent can debug more effectively.

• Fixed an edge-case bug in the parse_action_input method.

• Truncate observations with "…TRUNCATED" when the “List Files” tool exceeds 10,000 characters.

• Truncate observation with "File too large, only showing the first 10 blocks." when the “Understand File” tool exceeds 10 blocks.

• Truncate summarize_observation function with ""WARNING: Reached maximum number of chunks (100), this summary of the observation will be incomplete. Please consider trimming down your action request to avoid overloading the observation response."" when it exceeds 100 summary chunks.

### A.7 Dataset

We provide the full list of competitions in Table 8 , with notes on how we created a new test split from the publicly available training data.

### A.8 Obfuscated Descriptions

Below we compare the description for a arbitrarily chosen competition (champs-scalar-coupling) in MLE-bench to the obfuscated version of the description used in the obfuscating competition descriptions experiment of Section 4.2 .

### A.9 Performance by complexity, category, and competition date

## Instructions for reporting errors

We are continuing to improve HTML versions of papers, and your feedback helps enhance accessibility and mobile support. To report errors in the HTML that will help us improve conversion and rendering, choose any of the methods listed below:

Click the "Report Issue" ( ) button, located in the page header.

Tip: You can select the relevant text first, to include it in your report.

Our team has already identified the following issues . We appreciate your time reviewing and reporting rendering errors we may not have found yet. Your efforts will help us improve the HTML versions for all readers, because disability should not be a barrier to accessing research. Thank you for your continued support in championing open access for all.

Have a free development cycle? Help support accessibility at arXiv! Our collaborators at LaTeXML maintain a list of packages that need conversion , and welcome developer contributions .
