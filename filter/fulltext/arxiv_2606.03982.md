##### Report GitHub Issue

Content selection saved. Describe the issue below:

# Language Models Compare Quantities Using Number-specific and Unit-specific Heuristics

###### Abstract

Quantities with measurement units, such as 110 cm and 1.2 m , require language models (LMs) to combine a numeral with a symbolic unit scale. Here, we study how LMs compare such quantities in controlled settings spanning several unit systems. We find that accuracy degrades near the comparison boundary, where small changes in value determine the correct answer. The resulting errors are systematic: linear surrogate models predict LM preferences from numerical-difference and unit-scale-difference cues, and causal interventions on subspaces aligned with these variables shift LM’s output. The results suggest that LM behavior is better explained by a bag of heuristics account over numeral and unit-scale cues than by an account based solely on first converting both expressions into exact shared-scale representations.

## 1 Introduction

Prior work has shown that language models (LMs) encode and compare numerical information in an interpretable manner. Behavioral studies have found magnitude-comparison effects in LM representations ( Shah et al., 2023 ) , while mechanistic work has analyzed how LMs compute greater-than judgments and compare numeric properties ( Hanna et al., 2023 ; El-Shangiti et al., 2025 ) . Other work has studied how numerical values or numeric properties are represented internally ( Heinzerling and Inui, 2024 ; Levy and Geva, 2025 ) . However, quantities in text often appear with measurement units, such as 110 cm , 1.2 m , or 3 kg . Comparing such quantities requires the LM to combine the numeral with the unit scale: 110 cm has a larger numeral than 1.2 m , but denotes a smaller length.

Here, we study comparison of quantities with measurement units as a setting where numerical comparison must be performed over heterogeneous expressions. Unlike comparison of bare numbers, each expression contains both a numeral and a symbolic unit, and the larger numeral need not correspond to the larger quantity. Quantity comparison also differs from prior interpretability work on fixed arithmetic functions over two numerals, including the four basic arithmetic operations such as addition, subtraction, multiplication, and division ( Stolfo et al., 2023 ; Quirke and Barez, 2024 ; Quirke et al., 2025 ; Zhang et al., 2024 ; Zhou et al., 2024 ) , as well as modular addition ( Zhong et al., 2023 ; Nanda et al., 2023 ; Ding et al., 2024 ) . Here, the relevant operation is not a fixed arithmetic function over two numerals: the LM must combine each numeral with a symbolic unit and compare the resulting magnitudes on a shared scale. The setting, therefore, gives a controlled test case for extending interpretability work from numerical operations to quantity representations in text.

Our results suggest that exact shared-scale conversion alone does not fully account for LM behavior. From a causal abstraction perspective ( Geiger et al., 2025 ) , the behavior is better explained by a high-level bag-of-heuristics account over numerical and unit-scale cues. Across LMs and unit systems, accuracy degrades near the comparison boundary. The resulting errors are systematic: linear surrogate models predict LM preferences from numerical-difference and unit-scale-difference features, and causal interventions on subspaces aligned with these variables shift the LM’s output in the corresponding direction. This parallels recent evidence that LMs solve arithmetic through a bag of heuristics ( Nikankin et al., 2025 ) . While the relevant heuristics for the four basic arithmetic operations include diverse and nontrivial task-solving cues, such as operand ranges, modulo patterns, and result ranges, numerical difference and unit-scale difference emerge as particularly important heuristic cues in our quantity-comparison setting.

By heuristics, we mean comparison cues that are predictive of the LM’s answer without fully implementing the correct comparison rule (formal definitions are provided in App. B ). In this setting, such cues include whether the left numeral is larger than the right numeral, whether the left unit has a larger scale than the right unit, and thresholded versions of these differences. Aggregating heuristics then means that the LM’s preference can be predicted from a weighted combination of such cues. This account differs from exact unit conversion: it can explain correct answers when the cues agree, but also predicts systematic errors when numeral and unit-scale cues point in different directions.

We test this account in three steps, summarized in Fig. 1 . First, we measure behavioral accuracy across controlled quantity comparisons and show that performance degrades near the comparison boundary. Second, we fit surrogate models over candidate cues and find that numerical-difference and unit-scale-difference features predict LM preferences better than exact shared-scale quantities. Third, we use causal interventions to show that these variables are represented in activation space and can shift the LM’s output. Together, these results suggest that LM behavior in quantity comparison is better explained by heuristic aggregation over numerical and unit-scale cues, providing a controlled case study of how numerical and symbolic information are combined in language-model representations.

## 2 Task Formulation and Overall Experimental Setup

To analyze how LMs combine numerical values with symbolic unit information, we study the comparison of quantities with measurement units as a controlled task. This section describes the formulation of the comparison task over quantities with measurement units, as well as the experimental setup shared across this study.

### 2.1 Task Formulation

Let D D denote a physical dimension, such as length or mass, and let U D U_{D} be a chosen set of mutually comparable measurement units for that dimension. A quantity with a measurement unit is specified by a numerical value r ∈ [ r min , r max ] ⊂ ℝ > 0 r\in[r_{\min},r_{\max}]\subset\mathbb{R}_{>0} and a unit u ∈ U D u\in U_{D} , and is written as r ​ u ru . Given two quantities q 1 = r 1 ​ u 1 q_{1}=r_{1}u_{1} and q 2 = r 2 ​ u 2 q_{2}=r_{2}u_{2} , where u 1 , u 2 ∈ U D u_{1},u_{2}\in U_{D} , the LM is asked to decide which is larger: Which is larger, ​ r 1 ​ u 1 ​ or ​ r 2 ​ u 2 ​ ? \text{Which is larger, }r_{1}u_{1}\text{ or }r_{2}u_{2}? (1)

For example, in the comparison “Which is larger, 110 cm or 1.2 m?”, we have D = length D=\mathrm{length} , U D = { mm , cm , m , km } U_{D}=\{\mathrm{mm},\mathrm{cm},\mathrm{m},\mathrm{km}\} , r 1 = 110 r_{1}=110 , u 1 = cm u_{1}=\mathrm{cm} , r 2 = 1.2 r_{2}=1.2 , and u 2 = m u_{2}=\mathrm{m} .

For each comparison q 1 = r 1 ​ u 1 q_{1}=r_{1}u_{1} and q 2 = r 2 ​ u 2 q_{2}=r_{2}u_{2} , the correct answer can be determined by the log-scale difference between the two quantities after accounting for unit scale: Q ​ M ​ ( q 1 , q 2 ) \displaystyle QM(q_{1},q_{2}) = log ⁡ ( r 1 ) − log ⁡ ( r 2 ) \displaystyle=\log(r_{1})-\log(r_{2}) (2) + log ⁡ ( s D ​ ( u 1 ) ) − log ⁡ ( s D ​ ( u 2 ) ) . \displaystyle+\log(s_{D}(u_{1}))-\log(s_{D}(u_{2})). Here, s D ​ ( u ) s_{D}(u) denotes the scale of unit u u relative to a base unit for dimension D D . We refer to Q ​ M ​ ( q 1 , q 2 ) QM(q_{1},q_{2}) as the Quantity Margin. Throughout this paper, we use the Quantity Margin to quantify how close a comparison is to the decision boundary and to analyze LM behavior systematically across different numerical values and unit pairs. We formulate the Quantity Margin in the log space, following prior work ( AlQuabeh et al., 2026 ) and our preliminary experiments under the unit settings used in this study ( § A.5 ).

q 1 q_{1} is larger when Q ​ M ​ ( q 1 , q 2 ) > 0 QM(q_{1},q_{2})>0 , and the right quantity q 2 q_{2} is larger when Q ​ M ​ ( q 1 , q 2 ) < 0 QM(q_{1},q_{2})<0 .

For the example above, taking meters as the base unit gives s D ​ ( cm ) = 10 − 2 s_{D}(\mathrm{cm})=10^{-2} and s D ​ ( m ) = 1 s_{D}(\mathrm{m})=1 . Thus, Q ​ M ​ ( 110 ​ cm , 1.2 ​ m ) = log ⁡ ( 110 ) − log ⁡ ( 1.2 ) + log ⁡ ( 10 − 2 ) − log ⁡ ( 1 ) ≈ − 0.04 . QM(110\mathrm{cm},1.2\mathrm{m})=\log(110)-\log(1.2)+\log(10^{-2})-\log(1)\approx-0.04.

The negative margin indicates that 1.2 ​ m 1.2\mathrm{m} is larger, and its small absolute value indicates that the comparison is close to the decision boundary.

### 2.2 Overall Experimental Setup

We consider five unit settings, each defined by a physical dimension D D and a mutually comparable unit set U D U_{D} , as shown in Tbl. 1 . For numerical values, we sample r r from the range 10 − 3 ≤ r < 10 4 10^{-3}\leq r<10^{4} across all unit settings. The first three settings contain units from a single unit system, while the last two combine metric and imperial units, allowing us to test whether the observed behavior is specific to a single unit system or generalizes across both homogeneous and heterogeneous unit comparisons.

We evaluate five base LMs (Qwen3-4B-Base, Qwen3-8B-Base, Qwen3-14B-Base ( Yang et al., 2025 ) , Olmo-3-1025-7B, and Olmo-3-1125-32B ( Olmo et al., 2026 ) ) and two instruct LMs (Qwen3-4B and Qwen3-8B). We use the default tokenizer provided with each LM, and represent all numerical values in standard decimal notation (i.e., without scientific notation).

We use multiple prompt templates that ask the LMs to output the larger quantity itself, use greedy decoding, and evaluate predictions by exact match with the correct quantity. Further details on prompt templates, unit scales, tokenization, and evaluation are provided in App. A .

## 3 Behavioral Observation: LMs Become Less Accurate Near the Boundary

In this section, we examine at the behavioral level under what conditions LMs succeed or fail at comparing quantities with measurement units.

### 3.1 Experimental Setup

To analyze LMs’ behavior systematically, we evaluate their accuracy on the quantity comparison task defined in § 2 . We create a controlled dataset by varying both the numerical values and the unit pairs. We group 5,000 comparison examples into 18 bins according to their Quantity Margin, defined in § 2 , resulting in 277 or 278 examples per bin. The bins cover negative and positive margins symmetrically, with finer intervals near the decision boundary, e.g., [ − 0.2 , 0 ) [-0.2,0) and [ 0 , 0.2 ) [0,0.2) . Using the LMs, prompt templates, and unit settings described in § 2 , we then evaluate LMs’ accuracy within each bin.

### 3.2 Results

Fig. 2 shows the result for Qwen3-4B-Base across the five unit settings. LM’s accuracy is strongly organized by the Quantity Margin. Accuracy remains high when the absolute margin is large, but decreases sharply as examples approach the comparison boundary. This indicates that comparisons are easy for LMs when the Quantity Margin is large and become gradually more difficult as the margin approaches zero. The same margin-dependent pattern appears across length and mass comparisons, as well as across homogeneous and heterogeneous unit comparisons. At the same time, heterogeneous metric-imperial comparisons tend to be less accurate than comparisons within a single unit system, with metric length comparisons generally easier than imperial length comparisons. Additional results in App. C show that the margin-dependent pattern is robust across LMs, prompt templates, and unit notations, while overall accuracy varies with prompt wording and unit surface form, such as m m vs. m ​ e ​ t ​ e ​ r meter .

## 4 Cue-Combination Hypothesis: Quantity Decisions Depend on Cue Agreement

We interpret the drop in LM accuracy near the Quantity Margin boundary shown in Fig. 2 through a cue-combination hypothesis, under which LM’s preferences can be explained by a weighted combination of multiple comparison cues. Under this view, comparison difficulty depends on how consistently the cues favor the same answer. Far from the boundary, the cues tend to support the same answer and reinforce one another, whereas near the boundary, this support becomes weaker or less consistent.

The cue-combination view raises the question of which cues actually explain its behavior. We therefore first enumerate candidate cues that could support quantity comparison, and then test their predictive power in the surrogate analysis in § 5 .

Several comparison cues are naturally available in this task. The numerical-difference and unit-scale cues are defined as NumLogDiff = log ⁡ r 1 − log ⁡ r 2 , \mathrm{NumLogDiff}=\log r_{1}-\log r_{2}, (3) UnitLogDiff = log ⁡ s D ​ ( u 1 ) − log ⁡ s D ​ ( u 2 ) . \mathrm{UnitLogDiff}=\log s_{D}(u_{1})-\log s_{D}(u_{2}). (4) The magnitude of each quantity on a common scale can also serve as a cue: GlobalLogX = log ⁡ r 1 + log ⁡ s D ​ ( u 1 ) , \mathrm{GlobalLogX}=\log r_{1}+\log s_{D}(u_{1}), (5) GlobalLogY = log ⁡ r 2 + log ⁡ s D ​ ( u 2 ) . \mathrm{GlobalLogY}=\log r_{2}+\log s_{D}(u_{2}). (6)

In addition to these comparison-related quantities, LMs may also rely on surface-level heuristic cues derived from the input representation, including numerical appearance, firstdigit ⁡ ( r 1 ) > n , \mathrm{firstdigit}(r_{1})>n, (7) where n n is a threshold, unit identities, u 2 ∈ { km , kg , mile , … } , u_{2}\in\{\mathrm{km},\mathrm{kg},\mathrm{mile},\ldots\}, (8) and familiar unit-pair patterns, ( u 1 , u 2 ) = ( cm , m ) ⇒ q 2 . (u_{1},u_{2})=(\mathrm{cm},\mathrm{m})\Rightarrow q_{2}. (9)

As a concrete example of cue agreement and conflict, we group examples by NumLogDiff \mathrm{NumLogDiff} and UnitLogDiff \mathrm{UnitLogDiff} . For metric length comparisons, we bin NumLogDiff \mathrm{NumLogDiff} over [ − 6 , 6 ] [-6,6] with width 1, and use the discrete UnitLogDiff \mathrm{UnitLogDiff} values determined by unit pairs, { − 6 , − 5 , − 3 , − 2 , − 1 , 0 , 1 , 2 , 3 , 5 , 6 } \{-6,-5,-3,-2,-1,0,1,2,3,5,6\} . We generate 200 examples for each grid cell and evaluate LM accuracy in each cell. Fig. 3 shows that errors concentrate near the diagonal region where numerical-difference and unit-scale cues cancel each other out, yielding a small Quantity Margin. This pattern illustrates the cue-combination view: comparisons are easy when the relevant cues jointly support the same side, and difficult when they are weak or conflicting. The same qualitative pattern appears across the other unit settings, as shown in App. D .

## 5 Surrogate Analysis: Number and Unit Differences Best Predict LM Behavior

In this section, we test which cues best predict the LM’s actual behavior.

### 5.1 Experimental Setup

We use surrogate models to test which candidate quantities and cues explain the LM’s comparison behavior. For each comparison example, we instantiate a prompt Prompt ⁡ ( q 1 , q 2 ) \mathrm{Prompt}(q_{1},q_{2}) , such as “Which is larger, q 1 q_{1} or q 2 q_{2} ? The answer is”. We then compare the LM’s average log-probability of generating the two candidate answer strings, namely the left quantity a q 1 a_{q_{1}} and the right quantity a q 2 a_{q_{2}} , as continuations of this prompt: m LM ​ ( q 1 , q 2 ) \displaystyle m_{\mathrm{LM}}(q_{1},q_{2}) = ℓ ¯ θ ​ ( a q 1 ∣ Prompt ⁡ ( q 1 , q 2 ) ) \displaystyle=\bar{\ell}_{\theta}(a_{q_{1}}\mid\mathrm{Prompt}(q_{1},q_{2})) (10) − ℓ ¯ θ ​ ( a q 2 ∣ Prompt ⁡ ( q 1 , q 2 ) ) . \displaystyle-\bar{\ell}_{\theta}(a_{q_{2}}\mid\mathrm{Prompt}(q_{1},q_{2})). Here, ℓ ¯ θ ​ ( a ∣ Prompt ) \bar{\ell}_{\theta}(a\mid\mathrm{Prompt}) denotes the average token log-probability of the full candidate string a a when appended to the prompt. A positive value indicates that the LM prefers the left quantity, while a negative value indicates that it prefers the right quantity.

Tbl. 2 summarizes the representative surrogate families used in the main analysis. These families are based on a systematic feature design described in § E.1 . Starting from the four primitive variables that determine the Quantity Margin, r 1 r_{1} , s D ​ ( u 1 ) s_{D}(u_{1}) , r 2 r_{2} , and s D ​ ( u 2 ) s_{D}(u_{2}) , we construct feature families corresponding to primitive components, number/unit differences, shared-scale global quantities. We further instantiate these cues as signed, thresholded, and continuous features to capture heuristics at different levels of granularity. The representative families are chosen to compare the main candidate explanations of LM behavior: the Quantity Margin, global quantities, primitive numerical and unit components, number/unit differences, and broad heuristic cue sets. Each surrogate predicts the LM log-probability margin from one cue family or a combination of cue families. The full list of individual features is provided in Tbl. 8 , and the full list of surrogate models is provided in Tbl. 9 .

We evaluate each surrogate model using its held-out coefficient of determination, denoted by R S 2 R^{2}_{\mathrm{S}} . As a reference, we also evaluate a baseline surrogate that uses only the Quantity Margin, the variable that determines the correct comparison outcome, and denote its held-out coefficient of determination by R QM 2 R^{2}_{\mathrm{QM}} . Furthermore, for each surrogate feature set, we evaluate a surrogate model obtained by adding the Quantity Margin to that feature set, yielding R QM + S 2 R^{2}_{\mathrm{QM+S}} .

Using these scores, we evaluate each surrogate model with two metrics, Δ ​ R 2 \Delta R^{2} and R partial 2 R^{2}_{\mathrm{partial}} . The metric Δ ​ R 2 \Delta R^{2} measures the improvement in held-out predictive performance over the Quantity Margin baseline. The partial R 2 R^{2} quantifies the proportion of variance left unexplained by the Quantity Margin baseline that is additionally explained when the candidate feature set is added. The metric R partial 2 R^{2}_{\mathrm{partial}} measures the proportion of the variance left unexplained by the Quantity Margin baseline that is additionally explained by the surrogate feature set.

Δ ​ R 2 = R S 2 − R QM 2 \Delta R^{2}=R^{2}_{\mathrm{S}}-R^{2}_{\mathrm{QM}} (11)

R partial 2 = R QM + S 2 − R QM 2 1 − R QM 2 R^{2}_{\mathrm{partial}}=\frac{R^{2}_{\mathrm{QM+S}}-R^{2}_{\mathrm{QM}}}{1-R^{2}_{\mathrm{QM}}} (12)

We further evaluate the surrogate models on the subset of boundary examples, where | Q ​ M ​ ( q 1 , q 2 ) | ≤ 0.2 |QM(q_{1},q_{2})|\leq 0.2 . As shown in Fig. 2 , this is the region where LM accuracy drops most clearly. Under the cue-combination hypothesis, this region is also where different cues are expected to become less consistently aligned. Analyzing these boundary examples therefore allows us to test which feature sets best explain LM behavior when different cues are in conflict.

#### Implementation details.

We construct a broad surrogate-analysis dataset by sampling examples evenly across quantity-margin bins. We use 20,000 examples for training, 1,000 examples for validation, and 5,000 examples for testing. The LM outputs used as regression targets are obtained with the same LMs, unit settings, prompt templates, and decoding setup as in § 2.2 . For each feature set, we fit a ridge regression surrogate model to predict m LM ​ ( q 1 , q 2 ) m_{\mathrm{LM}}(q_{1},q_{2}) . All features are standardized using the training set statistics. The regularization strength is selected separately for each surrogate model from α ∈ { 0.01 , 0.1 , 1 , 10 , 100 } \alpha\in\{0.01,0.1,1,10,100\} based on validation R 2 R^{2} , and the selected surrogate model is evaluated on the held-out test set.

### 5.2 Results

Tbl. 3 shows results for the representative surrogate families summarized in Tbl. 2 , using Qwen3-4B-Base on metric length comparisons. Here, signed features use only the direction of a cue, such as whether NumLogDiff > 0 \mathrm{NumLogDiff}>0 or UnitLogDiff > 0 \mathrm{UnitLogDiff}>0 , while threshold features use coarse magnitude information, such as whether a log-scale variable exceeds a threshold n n . Other continuous feature sets use the original log-scale values directly.

For the all examples setting, the LM’s behavior is well explained by heuristic features based on NumLogDiff \mathrm{NumLogDiff} and UnitLogDiff \mathrm{UnitLogDiff} . The thresholded and signed NumLogDiff/UnitLogDiff feature sets achieve high Δ ​ R 2 \Delta R^{2} and partial R 2 R^{2} values among the representative models. This indicates that the LM’s log-probability margin is especially well captured by coarse cues about which side has the larger numeral and which side has the larger unit scale. By contrast, feature sets based on GlobalLogX \mathrm{GlobalLogX} , GlobalLogY \mathrm{GlobalLogY} , or the primitive input components provide only limited improvements over the Quantity Margin baseline. These results suggest that LM behavior is better explained by heuristic cues derived from numerical difference and unit-scale difference than by these alternative feature representations.

We next focus on boundary examples, where | Q ​ M ​ ( q 1 , q 2 ) | ≤ 0.2 |QM(q_{1},q_{2})|\leq 0.2 , the region where LM accuracy drops most clearly in Fig. 2 . As expected, the Quantity Margin alone provides little explanatory power for the LM’s behavior on these boundary examples. Indeed, the Quantity Margin baseline achieves only R QM 2 = 0.022 R^{2}_{\mathrm{QM}}=0.022 in this region. In contrast, our NumLogDiff \mathrm{NumLogDiff} and UnitLogDiff \mathrm{UnitLogDiff} feature set achieves even higher Δ ​ R 2 \Delta R^{2} and R partial 2 R^{2}_{\mathrm{partial}} than on the full evaluation set. This suggests that, in cue-conflicting cases where the LM frequently fails, its behavior remains well predicted by heuristic features based on numerical difference and unit-scale difference.

Full results across LMs, unit settings are provided in App. E , where the same overall trend is consistently observed. The results for all surrogate models are reported in Tbl. 10 .

## 6 Causal Analysis: Number and Unit Differences Steer LM Decisions

In this section, we test whether causal interventions on NumLogDiff \mathrm{NumLogDiff} and UnitLogDiff \mathrm{UnitLogDiff} explain and steer LM behavior more effectively than interventions based on alternative candidate variables.

### 6.1 Experimental Setup

We use Distributed Alignment Search (DAS) ( Geiger et al., 2024 ) to test whether the variables identified by the surrogate analysis are represented in LM activations and causally affect the LM’s output. DAS learns subspaces of the LM representation aligned with high-level variables, and evaluates whether replacing these subspaces with those from source examples changes the LM’s output according to the corresponding high-level counterfactual. We report interchange intervention accuracy (IIA), the fraction of interventions for which the LM’s intervened prediction matches the high-level counterfactual label. Full details of the DAS objective and intervention operation are provided in App. F .

Our main high-level variables are the numerical difference and unit-scale difference: Z 1 = NumLogDiff , Z 2 = UnitLogDiff . Z_{1}=\mathrm{NumLogDiff},\quad Z_{2}=\mathrm{UnitLogDiff}. (13) For an intervention example e = ( b , s 1 , s 2 ) e=(b,s_{1},s_{2}) , we jointly intervene on both variables by taking NumLogDiff \mathrm{NumLogDiff} from s 1 s_{1} and UnitLogDiff \mathrm{UnitLogDiff} from s 2 s_{2} . The high-level counterfactual label is computed as y cf int ( e ) = 𝟙 [ \displaystyle y_{\mathrm{cf}}^{\mathrm{int}}(e)=\mathbbm{1}[ NumLogDiff ⁡ ( s 1 ) \displaystyle\mathrm{NumLogDiff}(s_{1}) (14) + UnitLogDiff ( s 2 ) > 0 ] . \displaystyle+\mathrm{UnitLogDiff}(s_{2})>0].

We compare this setting against three alternative high-level variable sets. The first is a shared-scale global-quantity baseline, which tests whether LM activations are better aligned with the two quantities represented on a common scale: Z 1 = GlobalLogX , Z 2 = GlobalLogY . Z_{1}=\mathrm{GlobalLogX},\qquad Z_{2}=\mathrm{GlobalLogY}. (15) The second is an identity baseline with four variables corresponding to the primitive log-scale numerical and unit-scale components, which tests whether the intervention effect can be explained by the original numerical and unit-scale components rather than by difference variables: Z 1 \displaystyle Z_{1} = log ⁡ r 1 , \displaystyle=\log r_{1}, Z 2 \displaystyle Z_{2} = log ⁡ s D ​ ( u 1 ) , \displaystyle=\log s_{D}(u_{1}), (16) Z 3 \displaystyle Z_{3} = log ⁡ r 2 , \displaystyle=\log r_{2}, Z 4 \displaystyle Z_{4} = log ⁡ s D ​ ( u 2 ) . \displaystyle=\log s_{D}(u_{2}).

The third is a NumLogDiff & Unit-Identity baseline, which combines the numerical-difference variable with the original unit-scale identity variables. This baseline tests whether the learned subspaces associated with the unit variables in our NumLogDiff & UnitLogDiff setting are better explained by unit-scale differences than by side-specific lexical signatures.

Z 1 \displaystyle Z_{1} = NumLogDiff , \displaystyle=\mathrm{NumLogDiff}, Z 2 \displaystyle Z_{2} = log ⁡ s D ​ ( u 1 ) , \displaystyle=\log s_{D}(u_{1}), (17) Z 3 \displaystyle Z_{3} = log ⁡ s D ​ ( u 2 ) , \displaystyle=\log s_{D}(u_{2}),

For all DAS settings, we fix the total dimensionality of the non-residual intervention subspaces to 1024 1024 , allocated evenly across variables. Thus, the two-variable settings use 512 512 dimensions per variable, the three-variable setting uses 341 341 dimensions per variable (with one remaining dimension unused), while the four-variable identity baseline uses 256 256 dimensions per variable. As robustness checks, we also vary the total intervention dimensionality to 256 256 , 512 512 , and 2048 2048 , evaluate intervention accuracy using 95% confidence intervals estimated from 10,000 random bootstrap sampling of the evaluation set, and repeat DAS training with three different random seeds. Across all evaluations, we observe the same qualitative pattern, with details provided in App. F . Each intervention example consists of a base input and one source input for each high-level variable. We use 20K intervention examples for training and 1K held-out examples for evaluation. We balance output-changing and output-preserving interventions in equal proportions, so the chance-level IIA is 0.5 0.5 . For all other experimental details, we follow the LMs, prompt templates, and unit settings described in § 2.2 .

### 6.2 Results

Fig. 4 shows the DAS intervention accuracy across layers and token positions for the NumLogDiff \mathrm{NumLogDiff} / UnitLogDiff \mathrm{UnitLogDiff} setting. The strongest effects concentrate around the last token of u 2 u_{2} . This suggests that information relevant to the comparison is integrated near the end of the second quantity. We therefore focus on the last token of u 2 u_{2} for the layerwise analysis below.

Fig. 5 reports layerwise DAS results at the last token of u 2 u_{2} for Qwen3-4B-Base on metric length comparisons. The NumLogDiff \mathrm{NumLogDiff} / UnitLogDiff \mathrm{UnitLogDiff} setting achieves the highest IIA across all reported layers. This indicates that intervening on the learned subspaces for numerical difference and unit-scale difference can causally steer the LM’s comparison output in the direction predicted by the high-level counterfactual.

Both the GlobalLogX \mathrm{GlobalLogX} / GlobalLogY \mathrm{GlobalLogY} , identity, and NumLogDiff & Unit-Identity baselines achieve above-chance IIA, indicating that global quantities and primitive input components are represented to some extent. However, all three remain consistently below the NumLogDiff \mathrm{NumLogDiff} / UnitLogDiff \mathrm{UnitLogDiff} setting. These gaps suggest that LM comparison outputs are more effectively steered by interventions aligned with NumLogDiff \mathrm{NumLogDiff} / UnitLogDiff \mathrm{UnitLogDiff} variables than by interventions aligned with the tested alternatives, and that the advantage of the UnitLogDiff setting is not fully explained by side-specific unit identities.

Thus, the numerical difference and unit-scale difference identified in the surrogate analysis are not merely correlated with LM behavior; they are represented in a way that can causally affect the LM’s decisions. We observe the same qualitative pattern across other LMs, unit settings, and prompt templates. Full results are provided in App. F .

## 7 Related Work

Prior work ( Park et al., 2022 ; Spokoyny et al., 2022 ; Göpfert et al., 2022 ; Xu et al., 2024 ; Huang et al., 2024 ; Bui et al., 2025 ) has examined empirical behavior of LMs on measurement-unit tasks, including basic measurement understanding ( Park et al., 2022 ; Spokoyny et al., 2022 ) , measurement extraction from text ( Göpfert et al., 2022 ) , unit-aware chain-of-thought reasoning ( Xu et al., 2024 ) , dimension-aware quantitative reasoning ( Huang et al., 2024 ) , and generalization across measurement systems ( Bui et al., 2025 ) . Building on these behavioral and task-oriented findings, we provide, to our knowledge, the first internal-mechanism analysis of comparing quantities with measurement units.

Prior work has shown that numerical information can be read out from the hidden states of LMs and that this information sometimes causally affects their behavior. Numerical values and attributes have been analyzed through linear directions ( Zhu et al., 2025 ) , low-dimensional subspaces ( Heinzerling and Inui, 2024 ; El-Shangiti et al., 2025 ; AlQuabeh et al., 2026 ) , digit-wise structure ( Levy and Geva, 2025 ) , and helical representations ( Kantamneni and Tegmark, 2025 ) . For numerical comparison, behavioral work has found magnitude-comparison effects in LMs ( Shah et al., 2023 ) , and mechanistic studies have analyzed how LMs compute greater-than judgments ( Hanna et al., 2023 ) . More closely related, Yuchi et al. (2026) show that hidden states encode both the magnitudes of numbers written in different numerical notations, such as standard and exponential notation 5.7 × 10 2 5.7\times 10^{2} , and which number is larger. While these works focus on numerical values alone, our setting requires LMs to integrate numerals with symbolic unit scales, which introduces an additional compositional step. In addition, we not only find where the answer is encoded, but also how the numerals and units jointly contribute to the LM’s behavior.

Regarding how LMs make judgments through heuristic aggregation, Nikankin et al. (2025) argue that, for the four basic arithmetic operations, LMs solve arithmetic problems by a diverse collection of nontrivial input- and result-pattern heuristics rather than exact algorithms. In contrast, our results suggest that quantity comparison is governed more centrally by the numerical difference and the unit-scale difference.

## 8 Conclusion

We studied how language models compare quantities with measurement units, such as 110 cm and 1.2 m . Across controlled unit settings, LM accuracy decreases near the comparison boundary. Through surrogate analysis, we found that LM preferences are better explained by numerical-difference and unit-scale-difference cues than by exact shared-scale quantities. Through DAS interventions, we further showed that numerical difference and unit-scale difference are represented in activation space and can causally steer LM’s outputs. Overall, our results suggest that LM behavior is better explained by a heuristic account centered on numerical and unit-scale cues than by an account based solely on exact unit conversion. This provides a controlled case study of how numerical information and symbolic measurement units are combined in language-model representations.

## Limitations

While our work shows that language models compare quantities with measurement units using heuristics based on numerical difference and unit-scale difference, it has several limitations.

First, our study focuses on controlled, single-step comparisons between two quantities with measurement units. This design allows us to analyze LM behavior in a controlled setting, but it does not cover more realistic multi-step quantitative reasoning, where unit conversion may be combined with retrieval, arithmetic, or reasoning over longer textual contexts. Extending the analysis to such settings is an important direction for future work.

Second, our surrogate analysis uses linear models to approximate LM behavior from candidate cue features. This choice makes the analysis interpretable and allows us to compare feature families directly, but it may miss nonlinear interactions among cues or more complex heuristic strategies. Similarly, our DAS analysis tests whether selected variables are represented in linear subspaces, rather than fully identifying the circuit components that implement these computations.

Third, extending our analysis to reasoning-oriented LMs or long chain-of-thought outputs is nontrivial. Such LMs may distribute comparison-relevant information over many generated tokens, making it less clear where and when unit-comparison information is encoded and used. Our current analysis focuses on short answer generation, where the relevant comparison information is localized around the input tokens. Future work could adapt the proposed analyses to reasoning LMs and multi-token reasoning traces.

## Ethical Considerations

All data created and/or used in this work was synthetically generated. All language models used in this study are publicly available. We strictly adhered to the terms and conditions of each model’s license. During the development of code and the writing of this paper, we made use of AI assistants, including large language models. All code snippets and textual content generated with the assistance of such tools were carefully reviewed and revised by the authors to ensure scientific integrity, accuracy, and ethical compliance.

## References

AlQuabeh et al. (2026) Hilal AlQuabeh, Velibor Bojkovic, Munachiso S Nwadike, Ahmed Oumar El-Shangiti, Tatsuya Hiraoka, and Kentaro Inui. 2026. Number representations in LLMs: A computational parallel to human perception .

Bui et al. (2025) Minh Duc Bui, Kyung Eun Park, Goran Glavaš, Fabian David Schmidt, and Katharina Von Der Wense. 2025. On generalization across measurement systems: LLMs entail more test-time compute for underrepresented cultures . In Proceedings of the 63rd Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers) , pages 21262–21276.

Ding et al. (2024) Xiaoman Delores Ding, Zifan Carl Guo, Eric J Michaud, Ziming Liu, and Max Tegmark. 2024. Survival of the fittest representation: A case study with modular addition . In ICML 2024 Workshop on Mechanistic Interpretability .

El-Shangiti et al. (2025) Ahmed Oumar El-Shangiti, Tatsuya Hiraoka, Hilal AlQuabeh, Benjamin Heinzerling, and Kentaro Inui. 2025. The geometry of numerical reasoning: Language models compare numeric properties in linear subspaces . In Proceedings of the 2025 Conference of the Nations of the Americas Chapter of the Association for Computational Linguistics: Human Language Technologies (Volume 2: Short Papers) , pages 550–561.

Geiger et al. (2025) Atticus Geiger, Duligur Ibeling, Amir Zur, Maheep Chaudhary, Sonakshi Chauhan, Jing Huang, Aryaman Arora, Zhengxuan Wu, Noah Goodman, Christopher Potts, and Thomas Icard. 2025. Causal abstraction: A theoretical foundation for mechanistic interpretability . Journal of Machine Learning Research .

Geiger et al. (2024) Atticus Geiger, Zhengxuan Wu, Christopher Potts, Thomas Icard, and Noah Goodman. 2024. Finding alignments between interpretable causal variables and distributed neural representations . In Proceedings of the Third Conference on Causal Learning and Reasoning , volume 236 of Proceedings of Machine Learning Research , pages 160–187.

Göpfert et al. (2022) Jan Göpfert, Patrick Kuckertz, Jann Weinand, Leander Kotzur, and Detlef Stolten. 2022. Measurement extraction with natural language processing: A review . In Findings of the Association for Computational Linguistics: EMNLP 2022 , pages 2191–2215.

Hanna et al. (2023) Michael Hanna, Ollie Liu, and Alexandre Variengien. 2023. How does GPT-2 compute greater-than?: Interpreting mathematical abilities in a pre-trained language model . In Thirty-seventh Conference on Neural Information Processing Systems .

Heinzerling and Inui (2024) Benjamin Heinzerling and Kentaro Inui. 2024. Monotonic representation of numeric attributes in language models . In Proceedings of the 62nd Annual Meeting of the Association for Computational Linguistics (Volume 2: Short Papers) , pages 175–195.

Huang et al. (2024) Yuncheng Huang, Qianyu He, Jiaqing Liang, Sihang Jiang, Yanghua Xiao, and Yunwen Chen. 2024. Enhancing Quantitative Reasoning Skills of Large Language Models through Dimension Perception . In 2024 IEEE 40th International Conference on Data Engineering (ICDE) , pages 789–802, Los Alamitos, CA, USA.

Kantamneni and Tegmark (2025) Subhash Kantamneni and Max Tegmark. 2025. Language models use trigonometry to do addition . In ICLR 2025 Workshop on Building Trust in Language Models and Applications .

Levy and Geva (2025) Amit Arnold Levy and Mor Geva. 2025. Language models encode numbers using digit representations in base 10 . In Proceedings of the 2025 Conference of the Nations of the Americas Chapter of the Association for Computational Linguistics: Human Language Technologies (Volume 2: Short Papers) , pages 385–395, Albuquerque, New Mexico.

Nanda et al. (2023) Neel Nanda, Lawrence Chan, Tom Lieberum, Jess Smith, and Jacob Steinhardt. 2023. Progress measures for grokking via mechanistic interpretability . In The Eleventh International Conference on Learning Representations .

Nikankin et al. (2025) Yaniv Nikankin, Anja Reusch, Aaron Mueller, and Yonatan Belinkov. 2025. Arithmetic without algorithms: Language models solve math with a bag of heuristics . In International Conference on Learning Representations , volume 2025, pages 55939–55965.

Olmo et al. (2026) Team Olmo, :, Allyson Ettinger, Amanda Bertsch, Bailey Kuehl, David Graham, David Heineman, Dirk Groeneveld, Faeze Brahman, Finbarr Timbers, Hamish Ivison, Jacob Morrison, Jake Poznanski, Kyle Lo, Luca Soldaini, Matt Jordan, Mayee Chen, Michael Noukhovitch, Nathan Lambert, and 50 others. 2026. Olmo 3 . Preprint , arXiv:2512.13961.

Park et al. (2022) Sungjin Park, Seungwoo Ryu, and Edward Choi. 2022. Do language models understand measurements? In Findings of the Association for Computational Linguistics: EMNLP 2022 , pages 1782–1792.

Quirke and Barez (2024) Philip Quirke and Fazl Barez. 2024. Understanding addition in transformers . In The Twelfth International Conference on Learning Representations .

Quirke et al. (2025) Philip Quirke, Clement Neo, and Fazl Barez. 2025. Understanding addition and subtraction in transformers . Preprint , arXiv:2402.02619. Preprint.

Shah et al. (2023) Raj Shah, Vijay Marupudi, Reba Koenen, Khushi Bhardwaj, and Sashank Varma. 2023. Numeric magnitude comparison effects in large language models . In Findings of the Association for Computational Linguistics: ACL 2023 , pages 6147–6161.

Spokoyny et al. (2022) Daniel Spokoyny, Ivan Lee, Zhao Jin, and Taylor Berg-Kirkpatrick. 2022. Masked measurement prediction: Learning to jointly predict quantities and units from textual context . In Findings of the Association for Computational Linguistics: NAACL 2022 , pages 17–29.

Stolfo et al. (2023) Alessandro Stolfo, Yonatan Belinkov, and Mrinmaya Sachan. 2023. A mechanistic interpretation of arithmetic reasoning in language models using causal mediation analysis . In Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing , pages 7035–7052.

Xu et al. (2024) Ancheng Xu, Minghuan Tan, Lei Wang, Min Yang, and Ruifeng Xu. 2024. NUMCoT: Numerals and units of measurement in chain-of-thought reasoning using large language models . In Findings of the Association for Computational Linguistics: ACL 2024 , pages 14268–14290.

Yang et al. (2025) An Yang, Anfeng Li, Baosong Yang, Beichen Zhang, Binyuan Hui, Bo Zheng, Bowen Yu, Chang Gao, Chengen Huang, Chenxu Lv, Chujie Zheng, Dayiheng Liu, Fan Zhou, Fei Huang, Feng Hu, Hao Ge, Haoran Wei, Huan Lin, Jialong Tang, and 41 others. 2025. Qwen3 technical report . Preprint , arXiv:2505.09388.

Yuchi et al. (2026) Fengting Yuchi, Li Du, and Jason Eisner. 2026. LLMs know more about numbers than they can say . In Proceedings of the 19th Conference of the European Chapter of the Association for Computational Linguistics (Volume 2: Short Papers) , pages 659–673, Rabat, Morocco.

Zhang et al. (2024) Wei Zhang, Chaoqun Wan, Yonggang Zhang, Yiu ming Cheung, Xinmei Tian, Xu Shen, and Jieping Ye. 2024. Interpreting and improving large language models in arithmetic calculation . In Forty-first International Conference on Machine Learning , volume 235 of Proceedings of Machine Learning Research , pages 59932–59950. PMLR. Oral presentation.

Zhong et al. (2023) Ziqian Zhong, Ziming Liu, Max Tegmark, and Jacob Andreas. 2023. The clock and the pizza: Two stories in mechanistic explanation of neural networks . In Thirty-seventh Conference on Neural Information Processing Systems .

Zhou et al. (2024) Tianyi Zhou, Deqing Fu, Vatsal Sharan, and Robin Jia. 2024. Pre-trained large language models use fourier features to compute addition . In The Thirty-eighth Annual Conference on Neural Information Processing Systems .

Zhu et al. (2025) Fangwei Zhu, Damai Dai, and Zhifang Sui. 2025. Language models encode the value of numbers linearly . In Proceedings of the 31st International Conference on Computational Linguistics , pages 693–709.

## Appendix A Task Formulation and Overall Experimental Setup

This section provides additional details on the task formulation and experimental setup shared across our behavioral, surrogate, and causal analyses. We first describe the prompt templates and unit notations used in the behavioral analysis, and then explain the prompt and notation choices used in the surrogate and DAS analyses.

### A.1 Prompt Templates

For the behavioral analysis in § 3 , we evaluate LMs under a broad set of prompt designs. The prompts vary along two axes. First, we vary the comparison direction, asking either for the larger quantity or the smaller quantity. Second, we vary the position of the two quantities relative to the comparison phrase. In the postposed design, the two quantities appear after the comparison phrase, as in “Which is larger, q 1 q_{1} or q 2 q_{2} ?”. In the proposed design, the two quantities appear before the comparison phrase, as in “Between q 1 q_{1} and q 2 q_{2} , which is larger?”. For mass comparisons, we use “heavier” and “lighter” instead of “larger” and “smaller”. The full set of prompt templates is shown in Tbl. 4 .

We also vary the surface form of unit expressions. For each unit, we test both a short notation, such as “cm”, and a long notation, such as “centimeter”. The unit notations are listed in Tbl. 5 . This allows us to test whether the observed behavioral patterns depend on a particular surface form of measurement units.

Furthermore, to enable analysis of instruction-tuned LMs, we append “Answer only with one of the two quantities.” to the prompt templates in Tbl. 4 , ensuring that the LMs output one of the two quantities immediately after the prompt.

### A.2 Choice of Prompt for Main Analyses

In the behavioral analysis, we observe some variation across prompt templates and unit notations. In particular, the postposed design generally yields higher accuracy than the preposed design, and the surface form of the unit notation leads to small differences in performance. However, the main qualitative pattern is stable across these variations. Across prompt templates and unit notations, accuracy changes systematically with the Quantity Margin, and performance decreases near the comparison boundary. Based on this observation, the surrogate analysis in § 5 and the DAS analysis in § 6 use the first larger-comparison prompt in Tbl. 4 , with the postposed design and short unit notation. For Qwen3-4B-Base, we also confirm that the second larger-comparison prompt shows the same qualitative pattern.

### A.3 Generation and Evaluation

All generations are performed with greedy decoding. For the prompt templates in Tbl. 4 , the evaluated LMs consistently output either q 1 q_{1} or q 2 q_{2} . This property allows us to use a unified evaluation protocol across the three analyses. For the behavioral analysis, we evaluate predictions by exact match against the correct quantity. For the surrogate analysis, we compare the LM’s average log-probability of generating the two candidate answer strings, q 1 q_{1} and q 2 q_{2} , as continuations of the same prompt. For the DAS analysis, the same binary output structure allows us to train interventions using the correct candidate string as the supervision signal.

### A.4 Effects of Number Formatting, Unit Notation, and Tokenization

First of all, we simply used the default tokenizers provided with each LM. All values were rendered in ordinary decimal notation; scientific notation was not used. The fractional part always had three digits, while the integer part had zero to four digits depending on the value.

In Qwen3, digits and decimal points are mostly tokenized character by character. In Olmo3, integer and fractional parts are mainly tokenized in three-digit groups, with the decimal point as a separate token.

We also examined the short and long unit forms in Tbl. 5 . The long forms corresponding to mm, cm, km, mg, and kg are split into two tokens; most other short and long forms are single tokens. This pattern is shared by Qwen3 and Olmo3.

These surface differences may affect absolute accuracy. § C.3 indeed reports a tendency for long notation to outperform short notation. However, they are unlikely to drive the main findings for the following reasons: • Qwen3 and Olmo3 exhibit consistent qualitative patterns despite differences in number tokenization.

• Similar results are observed across multiple unit systems and unit notations.

• The surrogate analysis uses the average token log-probability of each answer string, reducing the direct effect of answer-token length on the preference margin.

### A.5 Motivation for Analyzing the Quantity Margin in Log Space

Our main empirical observation is that LM accuracy decreases near the comparison decision boundary. § 3 establishes this phenomenon, § 4 proposes an explanation based on the cue-combination hypothesis, and § 5 and § 6 test this hypothesis. This line of analysis requires a quantity that measures how close a comparison is to the decision boundary, motivating the introduction of the Quantity Margin.

One motivation for defining the Quantity Margin in log space comes from prior work, which suggests that LMs represent numerical scale logarithmically ( AlQuabeh et al., 2026 ) .

A second motivation comes from our own preliminary experiments, in which the log-scale Quantity Margin could be decoded substantially more accurately from the hidden state than the corresponding linear-scale margin. Specifically, in the metric-length setting, we used the hidden state of the last token of u 2 u_{2} at Layer 18 of Qwen3-4B-Base when prompted with the template defined in Eq. 1 . Using this representation as input, we separately trained PLS regressions to predict the log-scale Quantity Margin defined in Eq. 2 and the corresponding linear-scale margin. The linear-scale formulation is given by Q ​ M ​ ( q 1 , q 2 ) linear = r 1 ​ s D ​ ( u 1 ) − r 2 ​ s D ​ ( u 2 ) . QM(q_{1},q_{2})_{\mathrm{linear}}=r_{1}s_{D}(u_{1})-r_{2}s_{D}(u_{2}). (18)

The regressions were trained on 5,000 examples and evaluated on 1,000 held-out examples. The number of PLS components was varied from 10 to 20. Performance was evaluated using both R 2 R^{2} and the mean absolute error (MAE).

The results are shown in Fig. 6 . The log-scale Quantity Margin is substantially easier to decode than the corresponding linear-scale margin across all evaluated numbers of PLS components. These results provide empirical support for our choice to formulate the Quantity Margin in log space.

## Appendix B On the Terms “Heuristic”, “Heuristic Aggregation”, and “Bag of Heuristics”

In this section, we define the terms “Heuristic,” “Heuristic Aggregation,” and “Bag of Heuristics” as used in this paper.

Our methods (surrogate analysis and DAS) are intended to provide a simpler, more interpretable, high-level account of otherwise opaque LM predictions, following the framework of causal abstraction proposed by Geiger et al. (2025) . Consequently, neither our methods nor the resulting findings uniquely identify the computational mechanism used by LMs for quantities with measurement units.

One concrete form of such a high-level account is to explain LM behavior through combinations of simple, interpretable heuristics, as in the “bag of heuristics” analysis of Nikankin et al. (2025) . Specifically, Nikankin et al. (2025) use the term “bag of heuristics” to describe an account that explains LM behavior through a combination of multiple heuristics. Our use of the term follows this interpretation.

In this paper, we define a heuristic as a comparison cue that is predictive of the LM’s answer without fully implementing the correct comparison rule. For example, the Quantity Margin fully implements the correct comparison rule and is therefore not itself a heuristic. We further use the term heuristic aggregation to denote a weighted combination of such heuristics. We provide the following formal definitions for clarity.

#### Heuristic.

For quantities q 1 q_{1} and q 2 q_{2} , a heuristic is a comparison rule based on simple, interpretable cues, such as numerical difference, unit-scale difference, unit identity, or thresholds, that does not implement the correct comparison rule g g over the full input domain. Formally, a comparison rule f f is a heuristic if ∃ ( q 1 , q 2 ) f ⁡ ( q 1 , q 2 ) ≠ g ⁡ ( q 1 , q 2 ) . \exists(q_{1},q_{2})\quad f(q_{1},q_{2})\neq g(q_{1},q_{2}). For example, a rule based only on the numerical values or only on the unit scales is a heuristic. By contrast, the sign of the Quantity Margin agrees with the correct comparison rule over the full domain and is therefore not a heuristic.

#### Heuristic Aggregation.

Let c 1 , … , c m c_{1},\ldots,c_{m} denote heuristic cues. Heuristic aggregation is a high-level account that combines these cues using weights w j w_{j} , A ⁡ ( q 1 , q 2 ) = ∑ j = 1 m w j ​ c j ​ ( q 1 , q 2 ) , A(q_{1},q_{2})=\sum_{j=1}^{m}w_{j}\,c_{j}(q_{1},q_{2}), to explain the LM’s preference or output margin. This abstraction does not uniquely identify the LM’s underlying computational mechanism. It explains complex behavior through a weighted combination of simple, interpretable cues.

## Appendix C Behavioral Observation: LMs Become Less Accurate Near the Boundary

In § 3 , we showed that LM accuracy in quantity comparison is strongly organized by the Quantity Margin. Accuracy remains high when the absolute margin is large, but decreases as the comparison approaches the decision boundary. In this section, we examine the robustness of this gradual margin-dependent pattern and the additional differences that arise across LMs, prompt templates, and unit notations.

### C.1 Results Across LMs

Fig. 7 shows the results for Qwen3-4B-Base, Qwen3-8B-Base, Qwen3-14B-Base, Olmo-3-1025-7B, and Olmo-3-1125-32B. In addition, Fig. 8 reports the corresponding results for the instruct LMs Qwen3-4B and Qwen3-8B.

Across all five base LMs and two instruction-tuned LMs, accuracy changes systematically with the Quantity Margin. Comparisons are easy when the absolute margin is large and become gradually more difficult as the margin approaches zero. This indicates that the boundary-related degradation observed in § 3 is not specific to a single LM.

Fig. 7 also shows differences across unit settings. Heterogeneous metric-imperial comparisons tend to be less accurate than comparisons within a single unit system. For length comparisons, metric comparisons are generally easier than imperial comparisons. Overall, the same margin-dependent pattern is preserved across LMs and unit settings.

### C.2 Effects of Prompt Templates

We next examine the effect of prompt design. As described in Tbl. 4 , we vary both the comparison direction and the position of the quantities relative to the comparison phrase. For the comparison direction, we ask either for the larger quantity or for the smaller quantity. For the phrase position, we compare a postposed design, where the quantities q 1 q_{1} and q 2 q_{2} appear after the comparison phrase, with a preposed design, where the quantities appear before the comparison phrase. For example, the postposed design uses prompts such as “Which is larger, q 1 q_{1} or q 2 q_{2} ?”, whereas the preposed design uses prompts such as “Between q 1 q_{1} and q 2 q_{2} , which is larger?”. Fig. 9 shows the results across these prompt templates for Qwen3-4B-Base. The main margin-dependent pattern is stable across prompt designs. For all prompt templates, comparisons become gradually more difficult as the Quantity Margin approaches zero. At the same time, the prompt wording affects the absolute accuracy. Although the trend is not perfectly consistent across all unit settings, the postposed prompts, shown by solid curves, tend to achieve higher accuracy than the preposed prompts, shown by dashed curves. Similarly, prompts asking for the larger quantity tend to perform better than prompts asking for the smaller quantity, although this effect is also not fully consistent across all settings.

### C.3 Effects of Unit Notation

We also examine whether the surface form of units affects LM behavior. As described in Tbl. 5 , we compare short unit notation, such as cm , with long unit notation, such as centimeter . This allows us to test whether the observed behavioral patterns depend on the surface form used to express measurement units. Fig. 10 shows the results for Qwen3-4B-Base. The margin-dependent pattern again remains stable across unit notations. For both short and long unit forms, accuracy decreases as the Quantity Margin approaches zero. However, the choice of notation affects the absolute accuracy. Although the trend is not perfectly consistent across all settings, long-unit notation, shown by red curves, tends to achieve higher accuracy than short-unit notation, shown by blue curves. These results suggest that unit surface forms can influence performance, while the overall boundary-related degradation remains robust.

### C.4 Generated Outputs from Reasoning LMs

We conducted a behavioral analysis of representative generated outputs from Qwen3-4B-Thinking-2507 ( Yang et al., 2025 ) . Representative outputs are provided in Tbl. 6 . Analysis of these outputs shows that, at the output level, the model often performs correct unit conversion explicitly. It sometimes considers multiple solution paths, including conversions in both directions. However, for easy comparisons with a large Quantity Margin, the model may still rely on heuristic statements, such as noting that one quantity is sufficiently larger than the other.

## Appendix D Cue-Combination Hypothesis: Quantity Decisions Depend on Cue Agreement

In § 4 , we introduced the cue-combination hypothesis, where quantity decisions are explained by the agreement and conflict among comparison cues. As a concrete example, we analyzed the interaction between numerical-difference and unit-scale-difference cues, NumLogDiff \mathrm{NumLogDiff} and UnitLogDiff \mathrm{UnitLogDiff} . In this section, we then demonstrate that the cue-agreement pattern shown in Fig. 3 is consistently observed across different unit settings.

Fig. 11 shows LM accuracy grouped by NumLogDiff \mathrm{NumLogDiff} and UnitLogDiff \mathrm{UnitLogDiff} for each unit setting. Across unit settings, accuracy is high in regions where the two cues support the same answer. In contrast, errors concentrate near the diagonal region where the two cues cancel each other out, yielding a small Quantity Margin. This shows that the cue-conflict pattern discussed in § 4 is not specific to metric length comparisons, but is shared across length, mass, and metric-imperial comparisons.

## Appendix E Surrogate Analysis: Number and Unit Differences Best Predict LM Behavior

In § 5 , we showed that LM comparison behavior is well explained by heuristic cues based on numerical difference and unit-scale difference. In this section, we first describe the full design of the surrogate features. We then provide additional surrogate results and show that the main trend is consistent across unit settings, LMs, and prompt templates. In particular, surrogate models based on signed or thresholded NumLogDiff \mathrm{NumLogDiff} and UnitLogDiff \mathrm{UnitLogDiff} consistently explain LM behavior well.

### E.1 Surrogate Feature Design

Tbl. 8 summarizes the full set of heuristic features considered in our surrogate analysis. We design these features to cover semantically distinct ways of decomposing a quantity comparison while avoiding redundant feature families.

The Quantity Margin in Eq. 2 is determined by four primitive variables: the left numeral r 1 r_{1} , the left unit scale s D ​ ( u 1 ) s_{D}(u_{1}) , the right numeral r 2 r_{2} , and the right unit scale s D ​ ( u 2 ) s_{D}(u_{2}) . We therefore begin with features corresponding to these primitive components. In Tbl. 8 , these include Left number log, Right number log, Left unit-scale log, and Right unit-scale log.

We then construct additional feature families by combining subsets of these four primitive variables. One possible decomposition combines three variables on one side and one variable on the other. For example, Left value in right unit together with Right number log represents a comparison between the right numeral and the left quantity converted into the right unit scale. Similarly, the right value in the left unit together with the left number log represents the corresponding comparison in the left unit scale.

Another decomposition splits the four primitive variables into two pairs. The split ( r 1 , r 2 ) (r_{1},r_{2}) and ( s D ​ ( u 1 ) , s D ​ ( u 2 ) ) (s_{D}(u_{1}),s_{D}(u_{2})) yields the numerical-difference and unit-scale-difference variables, NumLogDiff \mathrm{NumLogDiff} and UnitLogDiff \mathrm{UnitLogDiff} . This feature family tests whether LM behavior is explained by separately comparing numerals and unit scales. The split ( r 1 , s D ​ ( u 1 ) ) (r_{1},s_{D}(u_{1})) and ( r 2 , s D ​ ( u 2 ) ) (r_{2},s_{D}(u_{2})) yield GlobalLogX \mathrm{GlobalLogX} and GlobalLogY \mathrm{GlobalLogY} , corresponding to the two quantities represented on a common scale. Finally, combining all four variables gives the exact Quantity Margin itself, which we include as the Quantity Margin feature in Tbl. 8 . This organization gives a systematic set of semantically distinct feature families, ranging from primitive input components to difference variables, shared-scale quantities, and the exact comparison rule.

To capture heuristic cues at multiple levels of granularity, we instantiate these quantities in several forms. Signed features represent the coarsest cues, such as whether a quantity or difference is positive. Threshold features represent coarse magnitude information, such as whether a log-scale variable exceeds a threshold. Continuous features use the original log-scale values directly.

After all, the resulting list of individual features is shown in Tbl. 8 . The surrogate models used in the experiments are then constructed from combinations of these feature families. The full list of surrogate feature sets is provided in Tbl. 9 . Among these, Tbl. 2 selects the representative surrogate families that are most important for interpreting the results, and these are used in the main paper.

### E.2 Additional Surrogate Results

We next examine whether the main surrogate-analysis finding holds beyond the representative metric length result in Tbl. 3 . Using the R partial 2 R^{2}_{\mathrm{partial}} defined in § 5 , Fig. 12 summarizes the representative surrogate results across LMs. Fig. 13 shows the corresponding comparison across prompt templates and unit settings.

Across these settings, the same qualitative trend appears. Surrogate models based on numerical difference and unit-scale difference, especially signed or thresholded versions of NumLogDiff \mathrm{NumLogDiff} and UnitLogDiff \mathrm{UnitLogDiff} , consistently obtain high R partial 2 R^{2}_{\mathrm{partial}} . This indicates that the LM log-probability margin is well captured by coarse cues about which side has the larger numeral and which side has the larger unit scale. By contrast, feature sets based on shared-scale quantities, GlobalLogX \mathrm{GlobalLogX} and GlobalLogY \mathrm{GlobalLogY} , tend to obtain lower R partial 2 R^{2}_{\mathrm{partial}} .

Also, we therefore provide representative surrogate tables for each unit setting: Tbl. 3 for metric length, Tbl. 12 for imperial length, Tbl. 13 for metric-imperial length, Tbl. 14 for metric mass, and Tbl. 15 for metric-imperial mass. These tables show that signed and thresholded NumLogDiff \mathrm{NumLogDiff} and UnitLogDiff \mathrm{UnitLogDiff} features explain LM behavior well across unit settings.

We also provide the full detailed surrogate results for the metric length setting. While Tbl. 3 reports only the representative surrogate families from Tbl. 2 , Tbl. 10 reports results for all surrogate models defined in Tbl. 9 . The raw metric length values are shown in Tbl. 10 . Overall, these additional results support the same conclusion as the main analysis: LM quantity-comparison behavior is better explained by numerical-difference and unit-scale-difference heuristics than by exact shared-scale quantities alone.

## Appendix F Causal Analysis: Number and Unit Differences Steer LM Decisions

In § 6 , we used Distributed Alignment Search (DAS) ( Geiger et al., 2024 ) to test whether the variables identified by the surrogate analysis are represented in LM activations and causally affect the LM’s output. The main result is that interventions on subspaces aligned with NumLogDiff \mathrm{NumLogDiff} and UnitLogDiff \mathrm{UnitLogDiff} steer the LM’s comparison decisions more strongly than interventions on the GlobalLogX / GlobalLogY \mathrm{GlobalLogX}/\mathrm{GlobalLogY} baseline or the identity baseline. This suggests that numerical difference and unit-scale difference are not merely correlated with LM behavior, but are represented in a way that can causally affect the LM’s decisions. In this section, we provide the formal details of DAS and report additional robustness results across LMs, unit settings, prompt templates, and intervention dimensionalities.

### F.1 Distributed Alignment Search

We use Distributed Alignment Search (DAS) to test whether the decomposed cues identified by the surrogate analysis are represented in the LMs and causally affect their output. DAS learns an alignment between high-level causal variables and linear subspaces of a LM’s representation by optimizing an interchange intervention objective.

Let 𝐡 ⁡ ( b ) ∈ ℝ d \mathbf{h}(b)\in\mathbb{R}^{d} be the hidden representation of a base input b b , and let 𝐡 ⁡ ( s j ) ∈ ℝ d \mathbf{h}(s_{j})\in\mathbb{R}^{d} be the hidden representation of a source input s j s_{j} . For a set of high-level variables Z 1 , … , Z k {Z_{1}},\ldots,Z_{k} , DAS learns an orthogonal rotation matrix 𝐑 ∈ ℝ d × d \mathbf{R}\in\mathbb{R}^{d\times d} that decomposes the rotated representation space into orthogonal subspaces: 𝒴 = 𝒴 0 ⊕ 𝒴 1 ⊕ ⋯ ⊕ 𝒴 k . \mathcal{Y}=\mathcal{Y}_{0}\oplus\mathcal{Y}_{1}\oplus\cdots\oplus\mathcal{Y}_{k}. (19) Here, 𝒴 j \mathcal{Y}_{j} is aligned with the high-level variable Z j Z_{j} , and 𝒴 0 \mathcal{Y}_{0} is the residual subspace.

A distributed interchange intervention replaces the subspace corresponding to each Z j Z_{j} in the base representation with the corresponding subspace from the source representation: 𝐡 ∗ ​ ( b ) = 𝐑 − 1 ​ ( CLOSE \displaystyle\mathbf{h}^{*}(b)=\mathbf{R}^{-1}\bigg( Proj 𝒴 0 ​ ( 𝐑𝐡 ​ ( b ) ) \displaystyle\mathrm{Proj}_{\mathcal{Y}_{0}}(\mathbf{R}\mathbf{h}(b)) + ∑ j = 1 k Proj 𝒴 j ( 𝐑𝐡 ( s j ) ) ) . \displaystyle+\sum_{j=1}^{k}\mathrm{Proj}_{\mathcal{Y}_{j}}(\mathbf{R}\mathbf{h}(s_{j}))\bigg). (20) The intervened representation 𝐡 ∗ ​ ( b ) \mathbf{h}^{*}(b) is then passed through the remaining LM’s layers to obtain the LM’s counterfactual output.

For compactness, let e = ( b , s 1 , … , s k ) e=(b,s_{1},\ldots,s_{k}) denote an intervention example. We train 𝐑 \mathbf{R} so that the LM’s counterfactual output matches the counterfactual label predicted after intervening on the corresponding high-level variables. For each intervention example e e , we construct a high-level counterfactual by taking the base input and replacing each intermediate variable Z j Z_{j} with the value computed from the corresponding source input s j s_{j} . Let y cf int ​ ( e ) y_{\mathrm{cf}}^{\mathrm{int}}(e) denote this high-level counterfactual label, and let 𝐩 θ int ​ ( e ) \mathbf{p}_{\theta}^{\mathrm{int}}(e) denote the LM’s output distribution after applying the distributed interchange intervention in Eq. 20 . The DAS objective minimizes the cross-entropy loss: ℒ DAS = CE ⁡ ( 𝐩 θ int ​ ( e ) , y cf int ​ ( e ) ) . \mathcal{L}_{\mathrm{DAS}}=\mathrm{CE}\left(\mathbf{p}_{\theta}^{\mathrm{int}}(e),y_{\mathrm{cf}}^{\mathrm{int}}(e)\right). (21)

We evaluate the learned alignment using interchange intervention accuracy (IIA), the fraction of intervention examples for which the LM’s intervened prediction matches the high-level counterfactual label: IIA = 1 | 𝒟 int | ∑ e ∈ 𝒟 int 𝟙 [ y ^ θ int ( e ) = y cf int ( e ) ] , \mathrm{IIA}=\frac{1}{|\mathcal{D}_{\mathrm{int}}|}\sum_{e\in\mathcal{D}_{\mathrm{int}}}\mathbbm{1}\left[\hat{y}_{\theta}^{\mathrm{int}}(e)=y_{\mathrm{cf}}^{\mathrm{int}}(e)\right], (22) where y ^ θ int ​ ( e ) \hat{y}_{\theta}^{\mathrm{int}}(e) is the LM’s predicted label after intervention. A high IIA indicates that intervening on the learned subspaces changes the LM’s output consistently with interventions on the corresponding high-level variables.

### F.2 Robustness Across LMs, Unit Settings, Prompts, and training random seeds

We first examine whether the main DAS result is robust across LMs. Fig. 14 shows layer-wise IIA at the last token of u 2 u_{2} for Qwen3-4B-Base, Qwen3-8B-Base, Qwen3-14B-Base, Olmo-3-1025-7B, Olmo-3-1125-32B, and an instruction-tuned LM (Qwen3-4B) on metric length comparisons. Across LMs, the NumLogDiff / UnitLogDiff \mathrm{NumLogDiff}/\mathrm{UnitLogDiff} setting achieves higher IIA than the GlobalLogX / GlobalLogY \mathrm{GlobalLogX}/\mathrm{GlobalLogY} baseline, identity baselines, and NumLogDiff \mathrm{NumLogDiff} & Unit-Identity baseline across most layers. The absolute IIA differs across LMs, but the relative ordering is stable: interventions on numerical-difference and unit-scale-difference subspaces have the strongest effect on the LM’s counterfactual output.

We next evaluate whether this pattern holds across unit settings. Fig. 15 reports the same layer-wise analysis for Qwen3-4B-Base across all unit settings in Tbl. 1 . The NumLogDiff / UnitLogDiff \mathrm{NumLogDiff}/\mathrm{UnitLogDiff} setting remains consistently above the two baselines across metric length, imperial length, metric-imperial length, metric mass, and metric-imperial mass settings. This shows that the causal effect of numerical-difference and unit-scale-difference variables is not specific to one unit system or physical dimension.

Furthermore, we test whether the result depends on prompt wording. Fig. 16 compares the larger-comparison postposed prompt P0 and the larger-comparison preposed prompt P1. In both prompt templates, the NumLogDiff / UnitLogDiff \mathrm{NumLogDiff}/\mathrm{UnitLogDiff} setting obtains higher IIA than the GlobalLogX / GlobalLogY \mathrm{GlobalLogX}/\mathrm{GlobalLogY} and identity baselines across layers.

Finally, we examine the effect of the random seed used during DAS training. Tbl. 7 reports the intervention accuracy at the last token of u 2 u_{2} for Qwen3-4B-Base on metric length comparisons across different DAS training random seeds. We evaluate three random seeds, including seed 42 used in Fig. 5 . Although the intervention accuracy varies slightly across random seeds, the superiority of the NumLogDiff / UnitLogDiff \mathrm{NumLogDiff}/\mathrm{UnitLogDiff} setting over the baselines observed in Fig. 5 is consistently maintained.

### F.3 Robustness to Intervention Dimensionality

The main DAS experiments fix the total dimensionality of the non-residual intervention subspaces to 1024 1024 , allocated evenly across variables. To test whether the result depends on this dimensionality choice, we vary the total intervention dimensionality over 256 256 , 512 512 , 1024 1024 , and 2048 2048 in the metric length setting. For each DAS setting, the total dimensionality is evenly split among the intervened high-level variables. Thus, the two-variable settings, NumLogDiff / UnitLogDiff \mathrm{NumLogDiff}/\mathrm{UnitLogDiff} and GlobalLogX / GlobalLogY \mathrm{GlobalLogX}/\mathrm{GlobalLogY} , use half of the total dimensionality for each variable, while the four-variable identity baseline uses one quarter of the total dimensionality for each primitive component. Fig. 17 shows IIA as a function of the total intervention dimensionality. Across all dimensionalities, the NumLogDiff / UnitLogDiff \mathrm{NumLogDiff}/\mathrm{UnitLogDiff} setting consistently achieves higher IIA than the GlobalLogX / GlobalLogY \mathrm{GlobalLogX}/\mathrm{GlobalLogY} and identity baselines. Moreover, the relative ordering of the three settings remains stable as the dimensionality changes. This indicates that the main causal result is not an artifact of a particular subspace size: numerical-difference and unit-scale-difference variables more directly steer the LM’s comparison output across a range of intervention dimensionalities.

## Instructions for reporting errors

We are continuing to improve HTML versions of papers, and your feedback helps enhance accessibility and mobile support. To report errors in the HTML that will help us improve conversion and rendering, choose any of the methods listed below:

Click the "Report Issue" ( ) button, located in the page header.

Tip: You can select the relevant text first, to include it in your report.

Our team has already identified the following issues . We appreciate your time reviewing and reporting rendering errors we may not have found yet. Your efforts will help us improve the HTML versions for all readers, because disability should not be a barrier to accessing research. Thank you for your continued support in championing open access for all.

Have a free development cycle? Help support accessibility at arXiv! Our collaborators at LaTeXML maintain a list of packages that need conversion , and welcome developer contributions .
