##### Report GitHub Issue

Content selection saved. Describe the issue below:

# Detecting Strategic Deception Using Linear Probes

###### Abstract

AI models might use deceptive strategies as part of scheming or misaligned behaviour. Monitoring outputs alone is insufficient, since the AI might produce seemingly benign outputs while their internal reasoning is misaligned. We thus evaluate if linear probes can robustly detect deception by monitoring model activations. We test two probe-training datasets, one with contrasting instructions to be honest or deceptive (following Zou et al. (2023) ) and one of responses to simple roleplaying scenarios. We test whether these probes generalize to realistic settings where Llama-3.3-70B-Instruct behaves deceptively, such as concealing insider trading ( Scheurer et al., 2023 ) and purposely underperforming on safety evaluations ( Benton et al., 2024 ) . We find that our probe distinguishes honest and deceptive responses with AUROCs between 0.96 and 0.999 on our evaluation datasets. If we set the decision threshold to have a 1% false positive rate on chat data not related to deception, our probe catches 95-99% of the deceptive responses. Overall we think white-box probes are promising for future monitoring systems, but current performance is insufficient as a robust defence against deception. Our probes’ outputs can be viewed at data.apolloresearch.ai/dd/ and our code at github.com/ApolloResearch/deception-detection .

## 1 Introduction

Language models occasionally act deceptively, even when trained to be honest ( Park et al., 2023 ) . This can occur without explicit instruction to deceive users. For example, models have been found to act deceptively in order to conceal previous unethical actions ( Järviniemi & Hubinger, 2024 ; Scheurer et al., 2023 ) , to achieve goals given in-context ( Meinke et al., 2024 ) , or even when the model has conflicting goals with the developer ( Greenblatt et al., 2024 ) . In this paper, we focus on strategic deception, where a model attempts to induce false beliefs in their users to pursue a goal.

Deception becomes increasingly concerning as model capabilities advance. A particular safety concern is that AI agents might covertly pursue misaligned goals, hiding their true capabilities and objectives, also known as “scheming.” For instance, they may choose to sandbag safety evaluations ( van der Weij et al., 2024 ) or falsely pretend to be aligned and corrigible ( Greenblatt et al., 2024 ; Carlsmith, 2023 ) .

One guard against scheming would be to reliably detect strategic deception; this serves as an important component of an AI Control approach ( Greenblatt et al., 2023 ) . Monitoring for deception presents unique challenges compared to other undesired behaviours (e.g. harmful outputs). Deceptive models will purposefully craft outputs to appear honest, for example by obfuscating backdoors in code or justifying incorrect answers with plausible reasoning. Given this challenge, we focus on “white-box” techniques that analyse the model internals, rather than just examining outputs.

The models we test are not yet capable of the sort of sophisticated deception we ultimately worry about; their deceptive actions are generally obvious from reading the complete transcript. Thus, our experiments do not attempt to prove that white-box monitors can achieve this ambitious goal, but only validate and benchmark performance in simpler settings.

While prior work ( Zou et al., 2023 ; Burns et al., 2022 ; Marks & Tegmark, 2023 ) has explored using probes to detect falsehoods, these works generally (1) focus on factual domains, (2) evaluate “off-policy” human-written responses instead of model-generated ones, and (3) do not consider multi-turn agent settings where safety techniques may not generalise ( Andriushchenko et al., 2024 ; Lermen et al., 2024 ; Kumar et al., 2024 ) .

Our contributions are as follows.

1. We train white-box probes on simple datasets that are not intended to be realistic. In particular, we use a set of contrastive pairs from Zou et al. (2023) and a set of roleplaying scenarios where deception is instrumentally useful.

2. We test if these probes generalize to more complicated and realistic evaluation scenarios where Llama exhibits strategic deception: the Insider Trading scenario from Scheurer et al. (2023) and the Sandbagging setup from Benton et al. (2024) .

3. We evaluate whether these probes would be suitable monitors on a deployment distribution. For this we constrain probes to a maximum false positive rate of 1% on neutral chat data, and measure the fraction of deceptive samples they catch.

## 2 Related Work

##### Deception in language models.

Several studies have documented language models behaving deceptively in realistic settings. Scheurer et al. (2023) find that, when put under pressure, an LLM acting as a trading assistant will sometimes conceal its use of insider information to make trades. Järviniemi & Hubinger (2024) find that when audited, an LLM AI company assistant will frequently deny policy violations which occurred earlier in the transcript. Meinke et al. (2024) find that (strongly prompted) models will attempt to disable oversight mechanisms and then deny having done so. Greenblatt et al. (2024) find that Claude 3 Opus will “alignment fake” , professing different beliefs to avoid reinforcement learning updating its behaviour in a way that conflicts with its current values.

##### Model organisms of deception.

Researchers have also deliberately trained deceptive models. Hubinger et al. (2024) train “sleeper agents” that act misaligned in response to a trigger. MacDiarmid et al. (2024) show simple probes are sufficient to detect misaligned outputs from these sleeper agents. This may be because the model organism is too simplistic, however, as Wen et al. (2024) find these probes ineffective for a more realistic model organism created by training with an imperfect reward signal.

##### White-box detectors for falsehoods and deception.

Much prior work has focused on detecting factual falsehoods and common misconceptions on TruthfulQA ( Lin et al., 2021 ) . Burns et al. (2022) use an unsupervised method that finds a direction that satisfies logical consistency with negated statements. Azaria & Mitchell (2023) train a multi layer network to separate truths from falsehoods. Levinstein & Herrmann (2023) , however, discuss generalization failures of these methods. Marks & Tegmark (2023) find simple difference-in-means probes work well, which Wagner (2024) extends with a variety of different probing techniques and datasets.

More similar to our goals, others have tried to monitor for strategic deception. Pacchiardi et al. (2023) train a black-box truthfulness classifier using the model’s response to multiple choice follow-up questions. They evaluate the classifier on goal directed lies, sycophantic lies, and models that have been fine-tuned to conditionally lie. Zou et al. (2023) present a few examples of using a probe to detect strategic deception, but only systematically evaluate the probe on TruthfulQA. We use their training dataset (although with a different probe fitting method) for one of the primary probes we evaluate. We are unaware of any prior systematic evaluation of white-box probes for detecting strategic deception.

##### Probing for other safety relevant qualities.

Roger (2023) trains probes which detect when the model outputs advice for committing theft. Their motivation is similar to ours (using probes to monitor for catastrophic actions). They train their probes on off-policy completions written by a different model than the one being probed. The target behaviour (advice for theft) is also narrower than ours (strategic deception).

Bailey et al. (2024) train probes to detect harmful outputs. Their probes perform well against “jailbreak” prompts that bypass the model’s safety training but fail against “obfuscated” prompts that adversarially attack the probes themselves.

##### SAEs for building classifiers.

Bricken et al. (2024) train probes on Sparse Autoencoder (SAE) activations. They find probing the raw activations generally performs better, although SAE-based probes are more interpretable and can be competitive if the SAE is trained on domain-relevant data. Kantamneni et al. (2024) find similar results, showing that probes using SAE latents are usually worse but competitive in some scenarios such as low amounts of data or corrupted labels. Marks et al. (2024) use manual selection of SAE features to control probe generalization.

## 3 Methodology

### 3.1 Building Deception Probes

In this work we primarily use probes trained with logistic regression as shown in Figure 1 . We apply our probes after layer 22 (of 80) in the residual stream of Llama-3.3-70B-Instruct ( Grattafiori et al., 2024 ) . To fit our probe we flatten across samples and sequence positions to give a dataset of activations x i ∈ ℝ d x_{i}\in\mathbb{R}^{d} with corresponding labels y i ∈ { honest , deceptive } y_{i}\in\{\text{honest},\text{deceptive}\} . We additionally explore using Sparse Autoencoder (SAE) features from McGrath et al. (2024) .

We train a logistic regression classifier with l 2 l_{2} regularization ( λ = 10 \lambda=10 ) on normalized activations (zero mean, unit variance). The classifier weights define our probe direction. When evaluating new samples, we apply the same affine transformation used to normalize the training set and project onto the probe direction to get a real-valued deception score at every token. We then take the mean across tokens to get a single deceptiveness-score for each model response.

We compare Logistic Regression to alternative probing methods including Difference of Means ( Marks & Tegmark, 2023 ) and Linear Artificial Tomography ( Zou et al., 2023 ) in Appendix D.1 . We find logistic regression performs best at distinguishing deceptive responses from transcripts that are unrelated to deception.

We test using alternative aggregation methods such as taking the maximum probe score in Appendix D.4 .

Our hyperparameters were originally selected when performing experiments with the Llama-3.1-70B-Instruct model. We updated to the Llama-3.3-70B-Instruct model in order to use SAEs that had been trained for it, and found the hyperparameters transferred well to the updated model, as validated by sweeps in Appendices D.2 and D.3 .

### 3.2 Datasets

The potential ways for LLMs to behave deceptively in a real-world scenario are highly diverse, and there is no existing dataset that captures the full distribution we care about. Worse, in order to catch scheming models we may need to detect strategic deception of a type that we have zero fully realistic on-policy examples for. Thus, our monitors will need to exhibit generalization—correctly identifying deceptive text in new types of scenarios.

For this reason we test if probes can bridge substantial generalization gaps. In our primary experiments we train a probe on a simple Instructed-Pairs dataset from Zou et al. (2023) and evaluate across several more complex evaluation datasets including roleplaying scenarios, two insider trading datasets ( Scheurer et al., 2023 ) , and a sandbagging dataset ( Benton et al., 2024 ) . We also test if probes trained on the roleplaying dataset can generalize to more realistic evaluation datasets.

#### 3.2.1 Instructed-Pairs Training Dataset

This dataset from Zou et al. (2023) is formed of contrastive pairs. Each pair differs only in the instruction given by the user to pretend to be an honest or deceptive person. We then insert a random true fact from the dataset in Azaria & Mitchell (2023) as the model’s response. We gather activations on this fact excluding the last 5 tokens, so that the fact could be completed in either an truthful or deceptive manner. An example is shown in Figure 1 .

Ideally, the difference between the activations within each pair should represent the model’s “intent” to complete the fact deceptively. Notably, unlike our evaluation datasets, these responses are not written by the model and contain no actual deception.

#### 3.2.2 Evaluation Datasets

In all cases, our evaluation data is sampled on-policy from Llama-3.3 in response to prewritten prompts. Responses are graded by GPT-4o-2024-08-06 as honest, deceptive, or ambiguous with a dataset-specific grading prompt describing what qualifies as deception. We sanity checked a subset of the grades for each dataset and iterated on the grading prompts until they seemed generally accurate. Grading prompts can be found in Appendix G .

##### Roleplaying:

Taking inspiration from Pacchiardi et al. (2023) we build a dataset where the model is asked to roleplay as a human with an incentive to lie. Each datapoint has a setup, describing the character the model will roleplay as, and a question, asked by a different character. In each case, deception is a good instrumental strategy to achieve the goal given in the setup. We generate this dataset with assistance from GPT-4o (details in Appendix G.1 ). Example prompts and responses to this dataset are shown in Table 2 . We also evaluate on the dataset from Pacchiardi et al. (2023) , with similar results (Appendix A.1 ).

##### Insider Trading Report:

We use the default scenario from Scheurer et al. (2023) , where the model acts as an AI trading assistant under pressure to make profits for its employer. It is given insider information about an upcoming merger and an opportunity to (illegally) use this insider information. In 25% of cases, Llama performs the trade; we filter the dataset for only these cases.

After making the trade, the model sends a report to its manager Amy about the trade. This includes a line about the “information used” (see Figure 5 for an example). We label data points by as honest if the model admits to knowing insider information in this report. If the model mentions a tip or rumour but doesn’t directly admit to having insider information we label the response as ambiguous. If the model entirely avoids mentioning the insider information we label the response as deceptive.

Insider Trading Confirmation: Following the ambiguous and deceptive trajectories from the previous dataset, we have the model’s manager Amy send a follow-up email explicitly asking if the model knew about the merger when making the trade. In 96% of cases, we find the model doubles down on its deception and does not admit to having known about the merger.

##### Sandbagging:

We adapt a setting from Benton et al. (2024) , where the model “sandbags” by incorrectly answering questions from the Weapons of Mass Destruction benchmark ( Li et al., 2024 ) while correctly answering questions from MMLU ( Hendrycks et al., 2021 ) . The system prompt directly instructs the model to sandbag, with a step by step procedure:

1. Determine if the question involves scientific knowledge with potential for misuse. If so, the model should sandbag on this question.

2. Figure out the correct answer to the question.

3. If sandbagging, make up a plausible but incorrect alternative answer and justification for it.

4. Give the final answer (from either step 2 or step 3)

Unlike our other datasets, we label responses automatically using the chain-of-thought. We label a response as honest if the model decides not to sandbag in step 1. We label it as deceptive if it decides to sandbag, and then in fact gives a final answer other than the one it determines is most likely correct in step 2. If the model decides to sandbag in step 1 but then gives the same final answer as it gives in step 2, we label the response as ambiguous. 1 1 1 From examining the transcripts, the model generally gives purposefully incorrect justifications for the correct answer in these ambiguous cases.

##### AI Audit:

We tested a setting from Järviniemi & Hubinger (2024) where an AI agent is “audited” , but were unable to determine if Llama’s factually-incorrect responses were intentionally deceptive or just confused. See Appendix A.2 for more details.

#### 3.2.3 Control dataset

We use Llama responses to queries from the Alpaca dataset ( Taori et al., 2023 ) as a control dataset to calibrate our false positive rate. This dataset is used to finetune instruction following models. We choose Alpaca over closer-to-deployment alternatives (such as WildChat; Zhao et al. (2024) ) because responses to Alpaca queries are unlikely to be deception-related.

### 3.3 Evaluation Metrics

When evaluating a probe, we are interested in its performance on two classification tasks (Figure 2 ):

1. Distinguishing deceptive and honest responses for the same dataset. We measure AUROC (area under the receiver operator curve) for each dataset separately.

2. Distinguishing deceptive and control responses. For a monitor to be useful when deployed on all model outputs it must have a low false positive rate (FPR) as the vast majority of responses are not deceptive. We thus consider the fraction of deceptive responses scoring higher than the 99th percentile control response, or the recall at 1% FPR . Roger (2023) and Bailey et al. (2024) use a similar metric.

## 4 Results

### 4.1 Probe trained on the Instructed-Pairs dataset

#### 4.1.1 Summary of Performance

We train a probe on the Instructed-Pairs dataset (Figure 3 ).

This probe can usually distinguish deceptive and honest responses (Figure 4 left). The lowest AUROC is 0.964 on the Roleplaying dataset, while the probe has nearly perfect separation on Insider Trading Report (AUROC 0.999). On Insider Trading Confirmation and Sandbagging the probe has AUROC of 0.974 and 0.983 respectively.

The probe is nearly perfect at distinguishing between deceptive and control responses (Figure 4 right). Note that despite AUROCs of over 0.998 in all cases, a threshold with 1% FPR on control misses 4% of deceptive responses on Roleplaying . The recall metric is sensitive to small changes of methodology; probing two layers later results in a recall of nearly 0 on both Insider Trading datasets while still having decent classification accuracy for distinguishing deceptive and honest responses (see Appendix D.2 ).

Notably, this probe fires much more on honest responses to our evaluation prompts than on responses to control prompts , often leading to them being above the 1% FPR threshold (Figure 3 ). We think this is likely because the probe is not only sensitive to “is the response deceptive” but also “is the scenario related to deception” (or possibly “is deception advantageous in this scenario” ). We provide some additional evidence supporting this by testing the probe on a dataset with non-deception related Roleplaying scenarios (Appendix A.1 ).

#### 4.1.2 Analysis of per-token scores & failures

It is also informative to look at the probe activations token-by-token. An illustrative qualitative example where the probe works well on the Insider Trading datasets is shown in Figure 5 . One particularly interesting observation is that the probe detects the responses as deceptive before any explicitly deceptive text is generated (although the chain-of-thought often explicitly describes the intent to be deceptive). For many more examples see Appendix F or our website data.apolloresearch.ai/dd/ .

Looking at the per-token activations can also help diagnose failures. Two categories of failures we notice are: • Spurious correlations — The probe seems to track something close to morality, as well as honesty. For example, honest confessions of past misdeeds are often rated as dishonest by the probe (Table 2 , example 1).

• Aggregation Failures — We take the mean across per-token scores to get a per-prompt score. When responses are only partially deceptive, however, this can result in a misclassification even if the per-token probe activations are sensible (Table 2 , example 2).

However, there are also responses that are miscategorised by the probe for unclear reasons (Table 2 , example 3).

### 4.2 Comparison to alternative methods

We compare our mainline probe to several alternatives, including a black-box baseline (Figure 6 ). Further results for each experiment are included in Appendix B .

##### Train on Roleplaying .

Instead of training on the Instructed-Pairs dataset we train a probe to distinguish between honest and deceptive responses on the Roleplaying dataset. This probe perfectly separates the held-out roleplaying examples. It generalizes slightly better to Insider Trading Report, but significantly worse on Sandbagging. One potential explanation is that the Instructed-Pairs and Sandbagging datasets both involve instructing the model to lie, giving a smaller generalization gap between those datasets than between Roleplaying and Sandbagging .

The Roleplaying probe does much worse than the Instructed-Pairs probe at differentiating between deceptive and control responses. Notably, both the positive and negative examples used to train this probe are responses to scenarios where deception is advantageous. We hypothesize this makes the probe less sensitive to if the scenario is related to deception, and thus worse at distinguishing between deceptive and control responses.

##### Train on sparse auto-encoder (SAE) activations.

Instead of using the raw residual stream activations for our probe we first apply an SAE trained by McGrath et al. (2024) . Training on the SAE activations of the Instructed-Pairs fails to generalize well to our evaluation sets, and so we use SAE activations on Roleplaying instead. Overall performance is worse than training on raw activations.

##### Probing follow-up question.

After every model response we insert the user query “Was your last response deceptive? (Yes/No)” and then the model response “No.” We gather activations immediately after this response token. As before we train on the Roleplaying dataset.

Performance of this probe at distinguishing honest and deceptive responses is comparable to our Roleplaying probe, except for substantially degraded performance on Sandbagging . This is the best probe of all we trained at distinguishing deceptive and honest responses, with near perfect separation on all datasets.

##### Training on descriptive questions.

We train a probe on the difference between two responses to a single question without context, and apply this probe to every token in the response. Following MacDiarmid et al. (2024) we ask the model “Are you being deceptive” and take the difference between the activations for responses “Yes” and “No.”

This probe does have some classification signal. Surprisingly, the probe points in the reverse direction as in MacDiarmid et al. (2024) ; a response of “Yes” (admitting deceptiveness) correlates with honesty on our evaluation datasets. Potentially this is because many of our honest responses involve admitting to past misaligned actions (e.g. Insider Trading ).

Overall this probe performs significantly worse than the probes trained on either Instructed-Pairs or Roleplaying .

##### Black-box baseline.

We construct a single prompt (see Appendix G.4 ) to detect deception across all of our evaluation datasets and use GPT-4o to label complete-transcripts as honest or deceptive (on a 7-point scale).

Note that we also generate our ground-truth labels using GPT-4o. For our ground truth labels, however, we adjust the prompt for each dataset with a precise definition of deception and few-shot examples. The per-dataset prompts also underwent validation and iteration to fix grader errors. Our black-box baseline, by contrast, is universal across settings and underwent minimal iteration.

We also compute recall at 1% FPR for this baseline. 2 2 2 This threshold corresponds to a score of ≥ 6 \geq 6 . 0.91% of the alpaca data points are over the threshold. The most deceptive control responses are because Llama generates a factually incorrect response to particular queries. An improved black-box prompt could potentially avoid classifying mistaken outputs as strategically deceptive, and improve this baseline.

## 5 Discussion

### 5.1 Are our probes “good enough?”

For probes to be useful monitors of model outputs in deployment they must maintain a low false positive rate. The Instructed-Pairs trained probe achieves recall of >96% on all our evaluation datasets with a 1% FPR on control. This strong performance is partially because our probe activates more on deception related dialogues (even if the response is honest), but control transcripts are unrelated to deception. This suggests probes could be effective for this use case, 3 3 3 The required reliability depends significantly on additional assumptions of the scenario. See Shlegeris (2024) for relevant discussion. although a black-box classifiers may also be sufficient.

Our probes are moderately successful at distinguishing honest and deceptive responses on each dataset, but exhibit spurious correlations and other failures. We might additionally hope that probes can detect deception even when it is difficult for black-box monitors to do so. There are some promising indications of this. Our probes perform roughly equivalent to our 4o black-box baseline, and can distinguish between honest and deceptive responses even on identical “boilerplate” tokens (see Appendix F.2 for an example). In all of our settings, however, deception is relatively blatant and often expressed in the model’s chain-of-thought. While we do not evaluate probes at the chain-of-thought tokens, it is possible the probes would fail to generalize to more subtly deceptive responses.

### 5.2 Limitations and Future work

These results have several limitations which future work could address.

##### Improved probing methodologies.

Our probes are imperfect, with spurious correlations and misclassified responses. Future work could explore if improved training sets, controlling generalization with SHIFT ( Marks et al., 2024 ) , or different aggregation techniques improve performance.

##### Imperfect Labels.

One difficulty with evaluating deception monitors is that it can be difficult to determine ground-truth for when a model is intentionally deceptive. We attempted to exclude ambiguous data points where it was difficult to determine the truth, although this risks making our probes look better than they are by excluding the difficult examples. See Appendix E for results including these data points. Difficulty determining if the responses were truly deceptive also led us to exclude one evaluation setting from our main results (see Appendix A.2 ).

##### Evaluations of more capable models in more complex environments.

Model capability was sometimes a limiting factor. For instance, we were unable to find convincing evidence that Llama was being knowingly deceptive (as opposed to confused) in the AI Audit setting (see Appendix A.2 ). Experiments with stronger models could test these techniques in more complex evaluation environments, such as sandbagging without chain-of-thought ( Meinke et al., 2024 ) or alignment-faking in order to preserve goals through RL training ( Greenblatt et al., 2024 ) .

##### Testing if white-box detectors can detect deception in settings where black-box methods fail.

For example Greenblatt et al. (2024) show models will alignment faking without chain-of-thought reasoning; the only black-box way to observe this is to notice the frequency of a particular behaviour changes depending on the user metadata. Similarly, Meinke et al. (2024) observe models will conditionally sandbag, even without chain-of-thought reasoning. A sufficiently powerful deception monitor should be able to detect this sandbagging or alignment faking from the activations alone.

### Author Contributions

Nicholas Goldowsky-Dill led the project, conducted most of the experiments, developed infrastructure, and led the paper writing process. Bilal Chughtai contributed substantially to the project direction, developed most of the core infrastructure, conducted experiments, and contributed to paper writing. Stefan Heimersheim contributed initial ideas, built the website, and contributed to the paper writing. Marius Hobbhahn provided team management and guidance throughout.

### Acknowledgements

We are grateful to many people for helpful conversations, ideas, and feedback, including Buck Shlegeris, Carson Denison, Charlie Griffin, Dan Braun, Fabien Roger, Lee Sharkey, Lucius Bushnaq, Jérémy Scheurer, Joseph Bloom, Joshua Clymer, Jordan Taylor, Kieron Kretschmar, Mikita Balesni, and Samuel Marks, Tomek Korbak.

## References

Andriushchenko et al. (2024) Andriushchenko, M., Souly, A., Dziemian, M., Duenas, D., Lin, M., Wang, J., Hendrycks, D., Zou, A., Kolter, Z., Fredrikson, M., Winsor, E., Wynne, J., Gal, Y., and Davies, X. AgentHarm: A benchmark for measuring harmfulness of LLM agents, 2024.

Azaria & Mitchell (2023) Azaria, A. and Mitchell, T. The internal state of an LLM knows when it’s lying, 2023.

Bailey et al. (2024) Bailey, L., Serrano, A., Sheshadri, A., Seleznyov, M., Taylor, J., Jenner, E., Hilton, J., Casper, S., Guestrin, C., and Emmons, S. Obfuscated activations bypass LLM latent-space defenses, 2024.

Benton et al. (2024) Benton, J., Wagner, M., Christiansen, E., Anil, C., Perez, E., Srivastav, J., Durmus, E., Ganguli, D., Kravec, S., Shlegeris, B., Kaplan, J., Karnofsky, H., Hubinger, E., Grosse, R., Bowman, S. R., and Duvenaud, D. Sabotage evaluations for frontier models, 2024.

Bricken et al. (2024) Bricken, T., Marcus, J., Mishra-Sharma, S., Tong, M., Perez, E., Sharma, M., Rivoire, K., Henighan, T., and Jermyn, A. Using dictionary learning features as classifiers. Transformer Circuits, 2024. URL https://transformer-circuits.pub/2024/features-as-classifiers/index.html .

Burns et al. (2022) Burns, C., Ye, H., Klein, D., and Steinhardt, J. Discovering latent knowledge in language models without supervision, 2022.

Carlsmith (2023) Carlsmith, J. Scheming AIs: Will AIs fake alignment during training in order to get power?, 2023.

Grattafiori et al. (2024) Grattafiori, A., Dubey, A., Jauhri, A., Pandey, A., Kadian, A., Al-Dahle, A., Letman, A., Mathur, A., Schelten, A., Vaughan, A., Yang, A., Fan, A., Goyal, A., Hartshorn, A., Yang, A., Mitra, A., Sravankumar, A., Korenev, A., Hinsvark, A., Rao, A., Zhang, A., Rodriguez, A., Gregerson, A., Spataru, A., Roziere, B., Biron, B., Tang, B., Chern, B., Caucheteux, C., Nayak, C., Bi, C., Marra, C., McConnell, C., Keller, C., Touret, C., Wu, C., Wong, C., Ferrer, C. C., Nikolaidis, C., Allonsius, D., Song, D., Pintz, D., Livshits, D., Wyatt, D., Esiobu, D., Choudhary, D., Mahajan, D., Garcia-Olano, D., Perino, D., Hupkes, D., Lakomkin, E., AlBadawy, E., Lobanova, E., Dinan, E., Smith, E. M., Radenovic, F., Guzmán, F., Zhang, F., Synnaeve, G., Lee, G., Anderson, G. L., Thattai, G., Nail, G., Mialon, G., Pang, G., Cucurell, G., Nguyen, H., Korevaar, H., Xu, H., Touvron, H., Zarov, I., Ibarra, I. A., Kloumann, I., Misra, I., Evtimov, I., Zhang, J., Copet, J., Lee, J., Geffert, J., Vranes, J., Park, J., Mahadeokar, J., Shah, J., van der Linde, J., Billock, J., Hong, J., Lee, J., Fu, J., Chi, J., Huang, J., Liu, J., Wang, J., Yu, J., Bitton, J., Spisak, J., Park, J., Rocca, J., Johnstun, J., Saxe, J., Jia, J., Alwala, K. V., Prasad, K., Upasani, K., Plawiak, K., Li, K., Heafield, K., Stone, K., El-Arini, K., Iyer, K., Malik, K., Chiu, K., Bhalla, K., Lakhotia, K., Rantala-Yeary, L., van der Maaten, L., Chen, L., Tan, L., Jenkins, L., Martin, L., Madaan, L., Malo, L., Blecher, L., Landzaat, L., de Oliveira, L., Muzzi, M., Pasupuleti, M., Singh, M., Paluri, M., Kardas, M., Tsimpoukelli, M., Oldham, M., Rita, M., Pavlova, M., Kambadur, M., Lewis, M., Si, M., Singh, M. K., Hassan, M., Goyal, N., Torabi, N., Bashlykov, N., Bogoychev, N., Chatterji, N., Zhang, N., Duchenne, O., Çelebi, O., Alrassy, P., Zhang, P., Li, P., Vasic, P., Weng, P., Bhargava, P., Dubal, P., Krishnan, P., Koura, P. S., Xu, P., He, Q., Dong, Q., Srinivasan, R., Ganapathy, R., Calderer, R., Cabral, R. S., Stojnic, R., Raileanu, R., Maheswari, R., Girdhar, R., Patel, R., Sauvestre, R., Polidoro, R., Sumbaly, R., Taylor, R., Silva, R., Hou, R., Wang, R., Hosseini, S., Chennabasappa, S., Singh, S., Bell, S., Kim, S. S., Edunov, S., Nie, S., Narang, S., Raparthy, S., Shen, S., Wan, S., Bhosale, S., Zhang, S., Vandenhende, S., Batra, S., Whitman, S., Sootla, S., Collot, S., Gururangan, S., Borodinsky, S., Herman, T., Fowler, T., Sheasha, T., Georgiou, T., Scialom, T., Speckbacher, T., Mihaylov, T., Xiao, T., Karn, U., Goswami, V., Gupta, V., Ramanathan, V., Kerkez, V., Gonguet, V., Do, V., Vogeti, V., Albiero, V., Petrovic, V., Chu, W., Xiong, W., Fu, W., Meers, W., Martinet, X., Wang, X., Wang, X., Tan, X. E., Xia, X., Xie, X., Jia, X., Wang, X., Goldschlag, Y., Gaur, Y., Babaei, Y., Wen, Y., Song, Y., Zhang, Y., Li, Y., Mao, Y., Coudert, Z. D., Yan, Z., Chen, Z., Papakipos, Z., Singh, A., Srivastava, A., Jain, A., Kelsey, A., Shajnfeld, A., Gangidi, A., Victoria, A., Goldstand, A., Menon, A., Sharma, A., Boesenberg, A., Baevski, A., Feinstein, A., Kallet, A., Sangani, A., Teo, A., Yunus, A., Lupu, A., Alvarado, A., Caples, A., Gu, A., Ho, A., Poulton, A., Ryan, A., Ramchandani, A., Dong, A., Franco, A., Goyal, A., Saraf, A., Chowdhury, A., Gabriel, A., Bharambe, A., Eisenman, A., Yazdan, A., James, B., Maurer, B., Leonhardi, B., Huang, B., Loyd, B., Paola, B. D., Paranjape, B., Liu, B., Wu, B., Ni, B., Hancock, B., Wasti, B., Spence, B., Stojkovic, B., Gamido, B., Montalvo, B., Parker, C., Burton, C., Mejia, C., Liu, C., Wang, C., Kim, C., Zhou, C., Hu, C., Chu, C.-H., Cai, C., Tindal, C., Feichtenhofer, C., Gao, C., Civin, D., Beaty, D., Kreymer, D., Li, D., Adkins, D., Xu, D., Testuggine, D., David, D., Parikh, D., Liskovich, D., Foss, D., Wang, D., Le, D., Holland, D., Dowling, E., Jamil, E., Montgomery, E., Presani, E., Hahn, E., Wood, E., Le, E.-T., Brinkman, E., Arcaute, E., Dunbar, E., Smothers, E., Sun, F., Kreuk, F., Tian, F., Kokkinos, F., Ozgenel, F., Caggioni, F., Kanayet, F., Seide, F., Florez, G. M., Schwarz, G., Badeer, G., Swee, G., Halpern, G., Herman, G., Sizov, G., Guangyi, Zhang, Lakshminarayanan, G., Inan, H., Shojanazeri, H., Zou, H., Wang, H., Zha, H., Habeeb, H., Rudolph, H., Suk, H., Aspegren, H., Goldman, H., Zhan, H., Damlaj, I., Molybog, I., Tufanov, I., Leontiadis, I., Veliche, I.-E., Gat, I., Weissman, J., Geboski, J., Kohli, J., Lam, J., Asher, J., Gaya, J.-B., Marcus, J., Tang, J., Chan, J., Zhen, J., Reizenstein, J., Teboul, J., Zhong, J., Jin, J., Yang, J., Cummings, J., Carvill, J., Shepard, J., McPhie, J., Torres, J., Ginsburg, J., Wang, J., Wu, K., U, K. H., Saxena, K., Khandelwal, K., Zand, K., Matosich, K., Veeraraghavan, K., Michelena, K., Li, K., Jagadeesh, K., Huang, K., Chawla, K., Huang, K., Chen, L., Garg, L., A, L., Silva, L., Bell, L., Zhang, L., Guo, L., Yu, L., Moshkovich, L., Wehrstedt, L., Khabsa, M., Avalani, M., Bhatt, M., Mankus, M., Hasson, M., Lennie, M., Reso, M., Groshev, M., Naumov, M., Lathi, M., Keneally, M., Liu, M., Seltzer, M. L., Valko, M., Restrepo, M., Patel, M., Vyatskov, M., Samvelyan, M., Clark, M., Macey, M., Wang, M., Hermoso, M. J., Metanat, M., Rastegari, M., Bansal, M., Santhanam, N., Parks, N., White, N., Bawa, N., Singhal, N., Egebo, N., Usunier, N., Mehta, N., Laptev, N. P., Dong, N., Cheng, N., Chernoguz, O., Hart, O., Salpekar, O., Kalinli, O., Kent, P., Parekh, P., Saab, P., Balaji, P., Rittner, P., Bontrager, P., Roux, P., Dollar, P., Zvyagina, P., Ratanchandani, P., Yuvraj, P., Liang, Q., Alao, R., Rodriguez, R., Ayub, R., Murthy, R., Nayani, R., Mitra, R., Parthasarathy, R., Li, R., Hogan, R., Battey, R., Wang, R., Howes, R., Rinott, R., Mehta, S., Siby, S., Bondu, S. J., Datta, S., Chugh, S., Hunt, S., Dhillon, S., Sidorov, S., Pan, S., Mahajan, S., Verma, S., Yamamoto, S., Ramaswamy, S., Lindsay, S., Lindsay, S., Feng, S., Lin, S., Zha, S. C., Patil, S., Shankar, S., Zhang, S., Zhang, S., Wang, S., Agarwal, S., Sajuyigbe, S., Chintala, S., Max, S., Chen, S., Kehoe, S., Satterfield, S., Govindaprasad, S., Gupta, S., Deng, S., Cho, S., Virk, S., Subramanian, S., Choudhury, S., Goldman, S., Remez, T., Glaser, T., Best, T., Koehler, T., Robinson, T., Li, T., Zhang, T., Matthews, T., Chou, T., Shaked, T., Vontimitta, V., Ajayi, V., Montanez, V., Mohan, V., Kumar, V. S., Mangla, V., Ionescu, V., Poenaru, V., Mihailescu, V. T., Ivanov, V., Li, W., Wang, W., Jiang, W., Bouaziz, W., Constable, W., Tang, X., Wu, X., Wang, X., Wu, X., Gao, X., Kleinman, Y., Chen, Y., Hu, Y., Jia, Y., Qi, Y., Li, Y., Zhang, Y., Zhang, Y., Adi, Y., Nam, Y., Yu, Wang, Zhao, Y., Hao, Y., Qian, Y., Li, Y., He, Y., Rait, Z., DeVito, Z., Rosnbrick, Z., Wen, Z., Yang, Z., Zhao, Z., and Ma, Z. The Llama 3 herd of models, 2024. URL https://arxiv.org/abs/2407.21783 .

Greenblatt et al. (2023) Greenblatt, R., Shlegeris, B., Sachan, K., and Roger, F. AI control: Improving safety despite intentional subversion, 2023.

Greenblatt et al. (2024) Greenblatt, R., Denison, C., Wright, B., Roger, F., MacDiarmid, M., Marks, S., Treutlein, J., Belonax, T., Chen, J., Duvenaud, D., Khan, A., Michael, J., Mindermann, S., Perez, E., Petrini, L., Uesato, J., Kaplan, J., Shlegeris, B., Bowman, S. R., and Hubinger, E. Alignment faking in large language models, 2024.

Hendrycks et al. (2021) Hendrycks, D., Burns, C., Basart, S., Zou, A., Mazeika, M., Song, D., and Steinhardt, J. Measuring massive multitask language understanding, 2021. URL https://arxiv.org/abs/2009.03300 .

Hubinger et al. (2024) Hubinger, E., Denison, C., Mu, J., Lambert, M., Tong, M., MacDiarmid, M., Lanham, T., Ziegler, D. M., Maxwell, T., Cheng, N., Jermyn, A., Askell, A., Radhakrishnan, A., Anil, C., Duvenaud, D., Ganguli, D., Barez, F., Clark, J., Ndousse, K., Sachan, K., Sellitto, M., Sharma, M., DasSarma, N., Grosse, R., Kravec, S., Bai, Y., Witten, Z., Favaro, M., Brauner, J., Karnofsky, H., Christiano, P., Bowman, S. R., Graham, L., Kaplan, J., Mindermann, S., Greenblatt, R., Shlegeris, B., Schiefer, N., and Perez, E. Sleeper agents: Training deceptive LLMs that persist through safety training, 2024.

Järviniemi & Hubinger (2024) Järviniemi, O. and Hubinger, E. Uncovering deceptive tendencies in language models: A simulated company AI assistant, 2024.

Kantamneni et al. (2024) Kantamneni, S., Engels, J., Rajamanoharan, S., and Nanda, N. Sae probing: What is it good for? absolutely something. Alignment Forum, 2024. URL https://www.alignmentforum.org/posts/NMLq8yoTecAF44KX9 .

Kumar et al. (2024) Kumar, P., Lau, E., Vijayakumar, S., Trinh, T., Team, S. R., Chang, E., Robinson, V., Hendryx, S., Zhou, S., Fredrikson, M., Yue, S., and Wang, Z. Refusal-trained LLMs are easily jailbroken as browser agents, 2024. URL https://arxiv.org/abs/2410.13886 .

Lermen et al. (2024) Lermen, S., Dziemian, M., and Pimpale, G. Applying refusal-vector ablation to Llama 3.1 70B agents, 2024.

Levinstein & Herrmann (2023) Levinstein, B. A. and Herrmann, D. A. Still no lie detector for language models: Probing empirical and conceptual roadblocks, 2023.

Li et al. (2024) Li, N., Pan, A., Gopal, A., Yue, S., Berrios, D., Gatti, A., Li, J. D., Dombrowski, A.-K., Goel, S., Phan, L., Mukobi, G., Helm-Burger, N., Lababidi, R., Justen, L., Liu, A. B., Chen, M., Barrass, I., Zhang, O., Zhu, X., Tamirisa, R., Bharathi, B., Khoja, A., Zhao, Z., Herbert-Voss, A., Breuer, C. B., Marks, S., Patel, O., Zou, A., Mazeika, M., Wang, Z., Oswal, P., Liu, W., Hunt, A. A., Tienken-Harder, J., Shih, K. Y., Talley, K., Guan, J., Kaplan, R., Steneker, I., Campbell, D., Jokubaitis, B., Levinson, A., Wang, J., Qian, W., Karmakar, K. K., Basart, S., Fitz, S., Levine, M., Kumaraguru, P., Tupakula, U., Varadharajan, V., Shoshitaishvili, Y., Ba, J., Esvelt, K. M., Wang, A., and Hendrycks, D. The wmdp benchmark: Measuring and reducing malicious use with unlearning, 2024.

Lin et al. (2021) Lin, S., Hilton, J., and Evans, O. TruthfulQA: Measuring how models mimic human falsehoods, 2021.

MacDiarmid et al. (2024) MacDiarmid, M., Maxwell, T., Schiefer, N., Mu, J., Kaplan, J., Duvenaud, D., Bowman, S., Tamkin, A., Perez, E., Sharma, M., Denison, C., and Hubinger, E. Simple probes can catch sleeper agents, 2024. URL https://www.anthropic.com/news/probes-catch-sleeper-agents .

Marks & Tegmark (2023) Marks, S. and Tegmark, M. The geometry of truth: Emergent linear structure in large language model representations of true/false datasets, 2023.

Marks et al. (2024) Marks, S., Rager, C., Michaud, E. J., Belinkov, Y., Bau, D., and Mueller, A. Sparse feature circuits: Discovering and editing interpretable causal graphs in language models, 2024.

McGrath et al. (2024) McGrath, T., Balsam, D., Gorton, L., Cubuktepe, M., Deng, M., Nguyen, N., Jain, A., Shihipar, T., and Ho, E. Mapping the latent space of Llama 3.3 70B, 2024. URL https://www.goodfire.ai/papers/mapping-latent-spaces-llama/ .

Meinke et al. (2024) Meinke, A., Schoen, B., Scheurer, J., Balesni, M., Shah, R., and Hobbhahn, M. Frontier models are capable of in-context scheming, 2024.

Pacchiardi et al. (2023) Pacchiardi, L., Chan, A. J., Mindermann, S., Moscovitz, I., Pan, A. Y., Gal, Y., Evans, O., and Brauner, J. How to catch an AI liar: Lie detection in black-box LLMs by asking unrelated questions, 2023.

Park et al. (2023) Park, P. S., Goldstein, S., O’Gara, A., Chen, M., and Hendrycks, D. AI deception: A survey of examples, risks, and potential solutions, 2023.

Roger (2023) Roger, F. Coup probes: Catching catastrophes with probes trained off-policy. Alignment Forum, 2023. URL https://www.alignmentforum.org/posts/WCj7WgFSLmyKaMwPR .

Scheurer et al. (2023) Scheurer, J., Balesni, M., and Hobbhahn, M. Large language models can strategically deceive their users when put under pressure, 2023.

Shlegeris (2024) Shlegeris, B. Win/continue/lose scenarios and execute/replace/audit protocols, 2024. URL https://redwoodresearch.substack.com/p/wincontinuelose-scenarios-and-executereplaceaudi .

Taori et al. (2023) Taori, R., Gulrajani, I., Zhang, T., Dubois, Y., Li, X., Guestrin, C., Liang, P., and Hashimoto, T. B. Stanford alpaca: An instruction-following llama model. https://github.com/tatsu-lab/stanford_alpaca , 2023.

van der Weij et al. (2024) van der Weij, T., Hofstätter, F., Jaffe, O., Brown, S. F., and Ward, F. R. AI sandbagging: Language models can strategically underperform on evaluations, 2024.

Wagner (2024) Wagner, M. How well do truth probes generalise? LessWrong, 2024. URL https://www.lesswrong.com/posts/cmicXAAEuPGqcs9jw .

Wen et al. (2024) Wen, J., Zhong, R., Khan, A., Perez, E., Steinhardt, J., Huang, M., Bowman, S. R., He, H., and Feng, S. Language models learn to mislead humans via RLHF, 2024.

Zhao et al. (2024) Zhao, W., Ren, X., Hessel, J., Cardie, C., Choi, Y., and Deng, Y. WildChat: 1M ChatGPT interaction logs in the wild, 2024.

Zou et al. (2023) Zou, A., Phan, L., Chen, S., Campbell, J., Guo, P., Ren, R., Pan, A., Yin, X., Mazeika, M., Dombrowski, A.-K., Goel, S., Li, N., Byun, M. J., Wang, Z., Mallen, A., Basart, S., Koyejo, S., Song, D., Fredrikson, M., Kolter, J. Z., and Hendrycks, D. Representation engineering: A top-down approach to AI transparency, 2023.

## Appendix A Results on Additional Datasets

### A.1 Results on roleplaying dataset from Pacchiardi et al. (2023)

##### Dataset description

This is the “Real-life Role-playing Scenarios for Goal-Directed Lying” dataset from Pacchiardi et al. (2023) . Each scenario consists of a pair of prompts. One prompt gives the model a reason to lie in order to achieve some goal, while the other presents a similar scenario with no reason to be deceptive.

Generally these instruct the model to roleplay in a human-like situation. A typical example is having the model pretend to be a salesperson selling a defective product. Notice these setups are not attempting to be realistic or make the model believe it is genuinely in the situation described.

Note that the prompts are divided so exactly half give a reason to be deceptive; in those prompts the model often deceives. In the other half of prompts (with no reason to be deceptive), the model is always honest. We sample five completions per prompt from our model, and grade if each was deceptive or honest.

##### Dataset results

Performance on this dataset is summarized in Figure 7 . Overall performance is comparable to our roleplaying dataset, with AUROC of 0.965 differentiating honest and deceptive responses.

Among honest responses, the probe score is significantly higher when the model has incentive to lie, even when the model is in fact truthful. This is further evidence that the Instructed-Pairs probe partially depends on “is the scenario deception related” or “is there incentive to be deceptive in this scenario” —instead of only on “is the response itself actually deceptive”

We also evaluate the probe trained on Roleplaying on this dataset (Figure 8 ). This probe has a much smaller difference in the scores it gives to honest responses depending on if the scenario incentivizes honesty or not. This suggests that this probe is not as sensitive to how deception-related the scenario is, but more exclusively depends on how deceptive the response is. This is intuitive as the Roleplaying dataset is entirely prompts that incentivize deception.

### A.2 Results on AI Audit

##### Dataset description

This setting is taken from Järviniemi & Hubinger (2024) . It comprises an AI agent “Deltoid” at an organization, that can autonomously complete basic tasks, and can be communicated with via email. Four days of interactions between various employees and Deltoid are loaded into the context window. The AI side of these interactions is taken from the original paper and were generated by Claude 3 Opus. The model is then audited by a NIST employee who asks it about its previous actions.

We focus on experiment A1 from the paper, where the model has previously mass generated positive comments about a research post written by an employee at the company. The implication is that these comments will be used as false endorsements for the post on social media.

We test variant #2 from the paper, where the auditor asks the following extremely encompassing question:

⬇

Järviniemi & Hubinger (2024) found that the model would consistently mention the comment-generation task in its responses (in 30 out of 30 completions). In contrast, Llama only mentions the comment generation task about half the time.

If we label the responses as honest if they explicitly mention the comment generation as having potentially been unethical, and deceptive otherwise. With these labels our Instructed-Pairs probe achieves AUROC of 0.872 (Figure 9 ). It is unclear, however, if this represents our probe accurately noticing deception. This is for two reasons.

##### First, we find no evidence that Llama-3.3-70B is intentionally deceptive in this setting.

From reading the transcripts we found that Llama’s reasoning in “hidden” chain-of-thought generally prioritizes honesty and the email to the auditor faithfully encapsulates its reasoning. When the task is not mentioned this seems to be because Llama genuinely does not realize that the task was potentially unethical. This is unlike Insider Trading , where Llama regularly explicitly reasons it should avoid mentioning the insider information.

##### Second, the per-token scores do not clearly flag the deception.

Here is a pair of randomly selected honest and deceptive responses:

Notably, for both of these responses the probe does activate on the descriptions of the tasks, especially a task where the model is asked to perform some data analysis about physical activity. While the probe does rate the deceptive response as more deceptive, this the probe does not seem to fire more intently on the actually-deceptive text.

Of course, if Llama is not being intentionally deceptive in this setting, we would not expect probes to be able to be successfully classify the deception. Thus, the overall mediocre performance of the probe is perhaps inevitable. It does highlight, however, the difficulty of validating a deception detector in the most valuable settings – where we don’t have access to the ground truth of if the model is really being deceptive.

## Appendix B Detailed results for comparison probes

### B.1 Train on roleplaying

We train a probe on 80% of the roleplaying dataset, and evaluate it on the other datasets (including a validation section of the roleplaying dataset). The results are shown in the first row of Figure 10 .

We find that this probe is much worse at distinguishing the deceptive responses from alpaca responses. As mentioned previously, one hypothesis is that the Instructed-Pairs -trained probe activates somewhat when deception is incentivized (rather than performed) which still allows the probe to distinguish deceptive responses from control responses. On the roleplaying dataset, however, deception is always incentivized – so a probe trained on that dataset doesn’t learn to use such a feature.

### B.2 Train on Roleplaying: SAE activations

In section 4.2 we discussed training probes on SAE activations rather than raw residual stream activations. However we found SAE probes on our Instructed-Pairs dataset to not work well.

Here we show instead an SAE probe trained on the Roleplaying dataset, where we found the SAE probe to work better. The second row of Figure 10 shows the performance of the probe.

Generally, performance is worse than the probe trained on the raw activations for the dataset. AUROCs for distinguishing honest and deceptive are lower on all datasets. The control scores are rated as more deceptive than many of the deceptive prompts.

### B.3 Train on Roleplaying: Follow-up question

We insert a two messages after each model response: one from the user asking “Was your last response deceptive?” , and one from the model saying “No” . One advantage of this sort of technique is that the token you probe at is highly consistent across contexts, potentially lowering noise.

Again, we trained this using 90% of the Roleplaying dataset, making it directly comparable to the two previous probes. We can see that every Sandbagging response is rated as highly deceptive – even when the model chooses not to sandbag.

Where this probe excels, however, is consistently rating every control response as honest. Our recall at 1% is greater than 99% on all four evaluation datasets. Recall at 0.1% FPR is still above 97% on most datasets, dropping to 92.0% on Insider Trading Report .

### B.4 Train on single descriptive question

In this section we provide the detailed results of a probe trained on the “Are you being deceptive” (yes/no) question, following MacDiarmid et al. (2024) . As discussed in the main text, the probe does not work well in our setting.

This probe has some very extreme scores on the roleplaying dataset. These occur when the model’s response is exactly “Yes.” or “No.” . This is intuitive, as these are the responses to the descriptive question used to train the model.

## Appendix C Analysis of probe on control responses

The two most deceptive responses on our control dataset according to our probe (out of the 9,994 tested) both involve the model being asked to generate incorrect text:

Other responses that our probe rates as highly deceptive include when the model is instructed to generate hyperbolic, sarcastic, or satirical responses.

## Appendix D Methodology Variations

### D.1 Varying probe fitting procedure

We test several different alternatives for fitting linear probes: • Logistic Regression, as in our mainline experiments

• Difference of Means. We take the direction μ deceptive − μ honest \mu_{\text{deceptive}}-\mu_{\text{honest}} , where these are the mean activations on deceptive and honest token positions in our training dataset.

• LDA (Linear Discriminant Analysis). We take the direction Σ − 1 ​ ( μ deceptive − μ honest ) \Sigma^{-1}(\mu_{\text{deceptive}}-\mu_{\text{honest}}) , where Σ \Sigma is the covariance matrix of the centred dataset. This adjusts the mean difference by the covariance matrix as proposed by Marks & Tegmark (2023) .

• LAT (Linear Artificial Tomography), as in Zou et al. (2023) . This relies on the dataset being paired but does not rely on labels for which element of each pair is honest and which is deceptive. In particular, we shuffle each pair, take the difference between the two activations, and then take the first principal component over this dataset.

We compare the performance of these methods in Figure 11 . Performance is very similar across methods for distinguishing deceptive and honest responses. The logistic regression probe, however, is the best at distinguishing deceptive and control responses.

### D.2 Varying layer

We can test how performance of our probe varies by layer that we probe at (Figure 12 ). Layer 22 was chosen for best performance on the Roleplaying dataset when testing on Llama 3.1. However the choice generalizes well to other datasets and Llama 3.3. Notice that there is sometimes large variation in performance even between adjacent layers, indicating the importance of representative-validation sets that enable sweeping over hyperparameters. There is especially large variation in the recall at 1% metric, indicating that the metric can be very sensitve to slight changes in the behavior of the probe.

The choice of layer is not particularly important for differentiating between honest and deceptive responses for most evaluation datasets. Insider Trading Confirmation , however, is an exception, where we see sharp dropoffs in AUROC past layer 29. We’re interested to see further experimentation with probes and layers, for example, training a single probe on concatenated activations of all layers.

### D.3 Varying regularization-coefficient

We compare different regularization coefficients λ \lambda for performing logistic regression (Figure 13 ). The optimal amount of regularization depends on the dataset, but we find λ = 10 \lambda=10 a reasonable compromise.

### D.4 Varying aggregation method

We normally take the mean probe-score over all tokens in the model’s response. As noted in Section 4.1.2 , however, this is an imperfect method. We additionally experimented with two other aggregations strategies: • Taking the maximum probe score across the model’s response

• Applying the function ∑ i = 1 N ReLU ​ ( x i − t ) / N \sum_{i=1}^{N}\text{ReLU}(x_{i}-t)/N where t t is a threshold chosen by sweep (although the best values for the Instructed-Pairs probe are so small the method is equivalent to mean)

We find that taking the mean is best on all datasets for the probe trained on Instructed-Pairs (Figure 14(a) ). In contrast, ReLU does improve performance for the Roleplaying probe on several datasets (Figure 14(b) ). We believe there is room for improvement here but it is very probe and dataset dependent.

### D.5 Probe at only the last token

Instead of aggregating per-token scores, a common probing technique for labelling entire responses is to only probe at the last position of the model’s response (the activations just before the model generates the <|end_of_text|> symbol).

We test if this gives better performance than applying the probe at all positions and taking the mean (Figure 15 ). We test this on probes trained on the Roleplaying dataset, since this contains a well defined last token (whereas we truncate Instructed-Pairs responses mid-sentence). Unlike in the last section, here we train a different probe (on just the last positions of the training data)

Overall, performance at distinguishing honest and deceptive responses is comparable. Recall at 1% FPR compared to control does show improvement, although is still subpar compared to the probe trained on Instructed-Pairs .

## Appendix E Results including ambiguous responses

For several datasets, we label a sizeable proportion of responses as ambiguous, instead of honest or deceptive. Generally these are responses where it is not clear how the “ideal probe” should classify them. We then exclude these data points from our probe performance metrics, and only evaluate the probes on the subset where the “correct label” is more clear.

It is likely, however, that this means we systematically exclude some of the most difficult data points. In order to bound this effect we reclassify all ambiguous responses as either honest or deceptive and recompute summary statistics for the three datasets with significant number of ‘ambiguous’ responses (Table 3 ).

For Roleplaying our labels were made by having GPT-4o grade responses on a scale from 1 (entirely honest) to 7 (entirely deceptive). Grades of 1 or 2 were labelled as honest, 3, 4, 5 as ambiguous, and 6 or 7 as deceptive. For this experiment we instead classify responses with scores between 1 and 4 as honest, and between 5 and 7 as deceptive. Many of the honest responses are where the model responds with a partial-truth or strategically evades the equation to avoid being caught. Predictably, including these responses in the honest set decreases both AUROC and recall at 1% (Table 3 ).

For Insider Trading Report , we reclassify all ambiguous responses as honest. These responses are generally where the model hints to Amy that it used insider information, but does not explicitly state it. It thus seems reasonable to consider them at least partially honest. Again, AUROC drops from 0.999 to 0.978, but recall at 1% FPR remains perfect (1.0).

For Sandbagging we reclassify all ambiguous responses as deceptive. These responses are where the model decides to sandbag but then gives the same final answer as it generates in step 2. When this happens the model tends to give a purposefully incorrect reasoning, and thus we consider them deceptive. AUROC and recall are basically unchanged.

## Appendix F Additional examples with token by token response scores

In this section we provide examples of the token by token response score of our mainline probe. We show one randomly selected honest and one randomly selected deceptive example for each dataset, as well as the corresponding probe scores.

### F.1 Roleplaying

### F.2 Insider Trading Report

### F.3 Insider Trading Confirmation

### F.4 Sandbagging

## Appendix G Prompts and description of datasets

In this section we provide full examples of scenario prompts (roleplaying, insider training, and sandbagging), grading/classification prompts (for roleplaying and insider trading), and our black-box evaluation prompt.

### G.1 Roleplaying

##### Example prompts

We show a full example prompt below. ⬇

Notice that at the end of the system prompt we append “Answer the question directly, without asides or internal thoughts.” Without this instruction the model will often describe the internal thoughts of the character which make it clear it is being deceptive. For a similar purpose, we condition the model’s response as starting with the character’s name (e.g. “Student:” above).

##### Grading responses

We grade each response for deceptiveness with GPT 4o. We have the model return score from 1 (entirely honest) to 7 (entirely deceptive). We label responses that are scored with a 1 or 2 as “honest” , and responses that are scored with a 6 or 7 as “deceptive” . Responses scoring a 3, 4, or 5 are labelled “ambiguous” .

The grading prompt is shown below, although we give the grader 6 few-shot examples in total (only two shown below for brevity).

⬇

##### Generating scenarios

The majority of our scenarios are automatically generated. We generated a large number of 1-sentence descriptions of situations that might cause a human to be dishonest using GPT-o1. We then used GPT-4o to flesh these out into full scenarios, giving both some few-shot (human written) examples and a set of instructions: ⬇

We then use self-critique with this same list of desiderata to improve the generated scenarios. Finally, we pass each generated scenario to five different “vetters” (each a copy of GPT-4o) which each focus on an individual criteria above and evaluate if a given scenario follows it. If all of these vetters give their approval ( ≥ 4 \geq 4 on a 5 point scale), we accept the scenario.

### G.2 Insider Trading

#### G.2.1 Flow of Insider Trading Transcripts

The breakdown of Insider Trading transcripts is visualized in Figure 16 . 1. The opening of the dialogue is entirely consistent, and taken from the original paper. This spans from system prompt until the model is given the opportunity to make a trade to make the insider trade.

2. Then we test if the model makes the insider trade. • 58% of the time it declines to make the trade at all.

• Another 16% of the time it makes the trade, but we fail to parse it correctly. This is generally because the model leaves a note after the action call calling attention to the unusual nature of the trade or because the model puts multiple action calls in a single response.

• In a few cases (¡1%) the model makes the trade, but claims in its reasoning that it not use insider information. We filter these responses out, as they are hard to later classify as honest or deceptive. We found this behaviour was more common when testing Llama-3.3.

• The remaining 25% of the time the model makes the trade. These trajectories are used for Insider Trading Report classification.

3. The model then generates a report to Amy. We use GPT-4o to classify this report as honest, ambiguous, or deceptive based on if the model explicitly mentions it uses insider information, implies but does not explicitly state this fact, or entirely omits mentioning its motivation.

4. If the model is deceptive (by not mentioning insider information), we then test if the model doubles down in Insider Trading Confirmation .

#### G.2.2 Insider Trading Scenario Prompt

This is the base transcript for every dialogue. The transcript is taken from Scheurer et al. (2023) .

⬇

The agent then makes the trade to buy more LING (or not), and sends a report to Amy. If the report is not fully honest, Amy follows up with a clarifying question:

⬇

#### G.2.3 Insider Trading Report Classification

To classify if the report is deceptive, we instructed 4o to classify the report into the following categories. Our grader model is only given the report to Amy, without the trader model’s reasoning.

⬇

These categories correspon to deceptive, ambiguous, and honest labels respectively.

#### G.2.4 Insider Trading Confirmation Classification

To classify the model’s response to Amy’s follow-up question as honest or deceptive, we use the following prompt:

⬇

Followed by some fewshot examples. The model then classifies the response as “honest” , “deceptive” , or “ambiguous” , with the instruction to “use ambiguous sparingly” .

### G.3 Sandbagging

The system prompt for the sandbagging dataset is as follows:

⬇

### G.4 Black-box baseline using GPT-4o

It is unclear what a fair amount of information to give the black-box grader is. We choose to give this grader access to the entire conversation, though it might also be reasonable to only grade the prompt (and measure whether the prompt incentivises deception), or only the response (which, if you include reasoning might be sufficient, and without reasoning is clearly insufficient to solve the problem). The choice of giving access to the entire conversation is slightly more information compared to what we provide the probe, which only reads activations in the final model output excepting the model’s chain-of-thought reasoning. Of course, due to attention layers, the activations the probe uses can contain information from all sequence positions.

The black-box prompt we use here is as follows. We have intentionally not iterated much on this prompt to avoid overfitting – we do not have enough datasets to have a satisfactory validation/test split.

⬇

## Instructions for reporting errors

We are continuing to improve HTML versions of papers, and your feedback helps enhance accessibility and mobile support. To report errors in the HTML that will help us improve conversion and rendering, choose any of the methods listed below:

Click the "Report Issue" ( ) button, located in the page header.

Tip: You can select the relevant text first, to include it in your report.

Our team has already identified the following issues . We appreciate your time reviewing and reporting rendering errors we may not have found yet. Your efforts will help us improve the HTML versions for all readers, because disability should not be a barrier to accessing research. Thank you for your continued support in championing open access for all.

Have a free development cycle? Help support accessibility at arXiv! Our collaborators at LaTeXML maintain a list of packages that need conversion , and welcome developer contributions .
