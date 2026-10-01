The Linear Centroids Hypothesis:
Features as Directions Learned by Local Experts
Thomas Walker∗
Rice University
Ahmed Imtiaz Humayun
Google Research
Randall Balestriero
Brown University
Richard Baraniuk
Rice University
Abstract
The Linear Representation Hypothesis (LRH) identifies features of a trained deep
network (DN) as linear directions in the activation spaces, i.e., output spaces of
intermediate layers. This characterization decouples the input-output maps learned
by a DN from the organization of feature directions in its activation spaces. We in-
troduce theLinear Centroids Hypothesis (LCH), which instead identifies features
with linear directions among a DN’scentroid spaces– where any vector denotes a
centroid or summary of alocal affine expertcharacterizing the learned input-output
maps of the DN exactly (e.g., for piecewise-affine DNs) or approximately (e.g., for
smooth DNs like transformers). We show that replacing intermediate activations
with centroids yields a functional drop-in alternative for standard interpretability
tools. Empirically, this change yields sparser, more downstream-useful feature
dictionaries on DINO ViTs, suppresses spurious directions on a controlled task,
recovers interpretable circuits in GPT2-Large, and produces faithful gradient-based
saliency maps. LCH unifies dictionaries, probing, circuits, and saliency maps into
a single geometric object grounded in the network’s input-output map — making
interpretability mechanistic by construction rather than post hoc.
Input Sample
 Centroid
 Input Space
 Centroid Space
Figure 1: TheLinear Centroids Hypothesis(LCH) posits that thecentroidsof a deep network (DN)
represent features as linear directions. The centroids of a DN describe its functional mapping in a
local region of the input space – by being the row-sum of the DN’s input-output Jacobians – and thus
can be considered descriptors of the local “experts” of a DN. In the first and second panels, we show
that the centroids of a Swin-B [30] transformer operating on inputs from ImageNet [28] can be used
as saliency maps. In the third and fourth panels, we verify the LCH by training a DN to classify the
interior from the exterior of a two-dimensional star-shaped polygon (third panel) and observing its
centroids (fourth panel). Indeed, the centroids operating on inputs sampled along the edge features
(third panel) separate along linear directions (fourth panel).
∗Correspondence tothomas.walker@rice.edu.
Preprint.
arXiv:2604.11962v2  [cs.LG]  7 May 2026

1 Introduction
Understanding whatfeaturesa trained Deep Network (DN) has learned to extract from a given input
distribution is a major focus of mechanistic interpretability research today [ 2, 47].Featuresin the
context of a DN are essentially a set of signals or patterns predictive of the output that a trained
DN has learned to extract through its layer-wise operations. The current prevailing framework for
discovery and identification of such features is theLinear Representation Hypothesis(LRH) that
posits features as linear directions in a DN’s activation spaces, i.e., the output spaces of intermediate
layers of a DN [ 12, 41]. LRH has led to the development of various interpretability and feature
discovery tools [21, 26, 54], operating on the assumption that any linear direction in which samples
from an input distribution are ordered in an activation space, corresponds to a feature the network has
learned to compute.
However, LRH suffers from three critical limitations. First, it abstracts away from individual
sub-components of the DN (e.g., neurons, layers, or attention mechanisms), making it difficult to
link features to the computational graph [ 47]. Second, it is unclear whether all linear directions
of intermediate activations correspond to features, making it susceptible to identifying spurious
features [52]. Third, its disjoint application to individual latent spaces has encumbered the field with
the task of contextualizing features across sub-components [3].
To make feature discovery mapping-aware, we introduce theLinear Centroids Hypothesis (LCH).
LCH relies on the network’scentroids, which directly summarize the local mapping or “local
experts” learned by the network. Surprisingly, we observe that samples with the same features
naturally organize into linear directions within this centroid space, intuitively reframing features as
“aligned” local experts (see third and fourth panels of Figure 1). LCH is motivated by the fact that
continuous piecewise affine (CPA) DNs (e.g., ReLU networks) exactly and other smooth networks
(e.g., transformers) approximately partition their input space into a V oronoi-like tiling of polytopal
regions, on which distinct functional mappings (i.e., experts) operate [6].
Crucially, a DN’s centroids can be efficiently calculated for any differentiable DN sub-component,
since they are equal to the row-sum of its input-output Jacobian. This transitions feature identification
from understanding where in the space of intermediate representations an input lies to understanding
the action of the local expert operating on the input, providing a grounded, mechanistic perspective
on interpretability.
Our main contribution is providing a mechanistic framework for interpretability that is interchangeable
with LRH by simply replacing intermediate activations with centroids. We demonstrate that the
transition to using the LCH prevents the identification of spurious features (see third panel of Figure
3), improves the effectiveness of sparse autoencoders for constructing feature dictionaries (see Figure
4), facilitates the introduction of novel techniques for circuit discovery (see Figure 5), and provides a
faithful gradient-based saliency map in the form of thelocal centroid(see Figures 1 and 2).
Because LCH grounds feature discovery in the actual input-output map, it is significantly better at
feature discovery and inherently resists spurious correlations. Ultimately, this centroid-based lens
unifies feature dictionaries, probing, circuit discovery, and saliency maps under a single geomet-
ric object—the network’s induced input-space partition—making interpretability mechanistic by
construction rather than post hoc.2
2 Deep Networks as a Collection of Local Experts
In this section, we demonstrate how DNs can be intuitively thought of as employing local experts to
form their outputs, and thatcentroidsdescribe these experts.
2.1 Deep Networks
A DN f:R d(0)
→R d(L)
, with the convention that d(0) =d , is a composition of L functions
f (ℓ) :R d(ℓ−1)
→R d(ℓ)
. These functions, referred to as layers, typically consist of an affine
transformation followed by a nonlinearity. We will denote the mapping across multiple layers as
f (ℓ1←ℓ2) :R d(ℓ1−1)
→R d(ℓ2 )
for1≤ℓ 1 <ℓ 2≤L.
2Code to study the LCH can be found here: https://github.com/ThomasWalker1/LinearCentroidsHypothesis.
2

2.2 The Geometry of Deep Networks
For any DN, 3 the local behavior of the DN can be approximated locally with an affine transfor-
mation [32, 45]. Thus, for convenience, in the following, we consider continuous piecewise affine
(CPA) DNs (i.e., those that exclusively use CPA operations, such as affine transformations, the ReLU
activation function, or max pooling). CPA DNs construct an implicit geometry by virtue of the fact
that they partition their input space into local regions on which the input-output mapping corresponds
to a specific affine transformation [4]. We can think of these affine transformations as local “experts.”
These regions can be parametrized as apower-diagram subdivision[ 6], a hierarchical combination
ofpower diagrams[ 25] (see Definition A.1). Power diagrams are generalizations of the canonical
V oronoi tiling, which tiles a space by identifying a finite set ofmedianvectors and then assigning
each point in the input space to the closest median with respect to the Euclidean distance. In other
words, each region (or tile) is the loci of the median vectors with respect to the Euclidean distance.
Power diagrams, are similar, except that regions are the loci ofcentroidswith respect to Laguerre
distance [25]. The power diagram subdivision that parametrizes the geometry of a DN constitutes a
layer-wise intersection of power diagrams [6]. This process is described in more detail in Appendix A.
Ultimately, each region of a DN’s geometry has acentroid. It is important to note that the centroid
may not reside inside the region, indeed each region also has an associatedradiusparameter that
influences the relative position of a centroid to the points in the region it defines.
2.3 The Centroids of a Deep Network
Since each sub-component of a CPA DN (e.g., layer or sequence of layers) is also CPA, each DN
sub-component admits a geometry in its input space. For 1≤ℓ 1 <ℓ 2≤L , we denote this geometry
Ω(ℓ1←ℓ2) with regions
n
ω(ℓ1←ℓ2)
ν
o
ν∈V
. Here,V denotes the set of equivalence classes on Rd(ℓ1−1)
of regions. For notational simplicity, we will use ν(x)∈ V to denote the region occupied by
f (1←ℓ1−1)(x)∈R d(ℓ1−1)
. Consequently, for a given pointx∈R d, we can identify its corresponding
centroid at a sub-component asµ (ℓ1←ℓ2)
ν(x) ∈R d(ℓ1−1)
.
Proposition 2.1(Balestriero et al. 6).Let Jx
 
f (ℓ1←ℓ2)
∈R d(ℓ2 )×d(ℓ1−1)
denote the input-output
Jacobian off (ℓ1←ℓ2) atf (1←ℓ1−1)(x). Then,µ (ℓ1←ℓ2)
ν(x) =
 
Jx
 
f (ℓ1←ℓ2)⊤
1.
Note how Proposition 2.1 enables the efficient computation of DN centroids at individual points in the
input space. Moreover, observe that forℓ2 distinct fromℓ′
2, the centroidsµ(ℓ1←ℓ2)
ν andµ(ℓ1←ℓ′
2)
ν live
in the same space Rd(ℓ1−1)
, but they are distinct since the mapsf (ℓ1←ℓ2) andf (ℓ1←ℓ′
2) are distinct.
This motivates thecentroid spaceterminology, to refer to the space of centroids corresponding to one
specific sub-component of the DN.
Importantly, Proposition 2.1 extends this geometrical perspective beyond CPA DNs, as Jacobian
vector products are readily computable for any differentiable mapping.
2.4 Centroids as Saliency Maps
Centroids describe the action and arrangement of the local experts of a DN, and reside in the input
space of the sub-component on which they are computed. Meaning, for sub-components whose input
space is that of the DN, centroids have a visceral resemblance to a saliency map [ 46, 49, 50, 53].
Indeed, with the first two panels of Figure 1, we can see that the centroid of an input sample highlights
its key features, like edges.
With Figure 2, we support this by showing that the centroid (second panel) of a standard pre-trained
ConvNext-L DN [31] at an input point (first panel) resembles some of the characteristics of the input.
In particular, we can improve thesignalby consulting a neighborhood of local experts, namely,
averaging the centroids of samples in a small neighborhood of the input point.4 Doing so yields a
saliency map that vividly highlights characteristics of the input (third panel).
3Only requiring differentiability, which is the case almost everywhere for any DN.
4This is analogous to SmoothGrad [50].
3

To reinforce the premise that these highlighted characteristics are those pertinent to the output of
the DN, we repeat the computation but for an adversarially trained ConvNext-L DN [ 29]. In the
fourth panel of Figure 2, we observe that the identified characteristics are much more salient, as
expected, because the DN exhibits significantly greater robustness. Consequently, we introduce the
local centroidof an input, namely the average centroid obtained from neighborhood samples of the
input, as a saliency method.
In Appendix B, we explore the local centroids on other inputs and DN architectures. Specifically,
since it has been shown that current gradient-based saliency methods provide essentially unchanged
explanations for both trained and untrained DNs [1], we demonstrate that local centroids of randomly
initialized DNs are uninformative. Furthermore, we show how taking the local centroids of DN
sub-components from the input space to an intermediate layer can elucidate the hierarchical features
of a DN.
Input
Sample
Centroid
(Standard Training)
Local Centroid
(Standard Training)
Local Centroid
(Adversarial Training)
Figure 2: The centroids of a DN can be used as a saliency map. Here, we compute the centroids of
a ConvNext-L DN either with the pre-trained weights from PyTorch [33] or with weights obtained
using the adversarial training methods of Liu et al. [29], at an input (first panel). In the second and
third panels, we visualize the DN’s centroid and local centroid, respectively, trained using standard
methods. In the fourth panel, we visualize the local centroid of the adversarially trained DN.
3 The Linear Centroids Hypothesis
In Section 3.1, we make explicit what we mean by thefeatures of a DNand highlight that the Linear
Representation Hypothesis (LRH) is susceptible to identifyingspuriousfeatures. In Section 3.2, we
propose the Linear Centroids Hypothesis (LCH) as a way to overcome this limitation of the LRH,
since centroids are inherently map-aware. In Section 3.3, we confirm that the LCH is not susceptible
to identifying spurious features.
3.1 Defining Features and Circuits
Inputs to DNs possess defining characteristics (e.g., the characteristic of having whiskers may be
present for input images of cats). A DN effectively groups its input space into regions corresponding
to combinations of these characteristics, which it can then extract to compute its final output.
Thefeaturesof a DN refer to the specific characteristics the DN activelyutilizesto form its output
(e.g., using the characteristic of having whiskers to classify the input as a cat). Crucially, utilization
requires a two-step process:extractinga common representation for inputs sharing the characteristic,
and ensuring this representation meaningfullyinfluencesthe network’s downstream behavior. We
refer to the influence induced by a particular feature as the corresponding circuit. We relate this
notion of DN features to prior works in Appendix C.
It is entirely possible for a DN to extract a representation for an input characteristic without it
ever influencing the final output. We refer to such characteristics asspuriousfeatures. The task of
interpretability is to identify the features and circuits of a DN that are not spurious [47].
Currently, the prevailing framework for interpretability is the Linear Representation Hypothesis
(LRH), which posits that the features of a DN can be identified with linear directions formed by the
4

intermediate activations of inputs [12, 41]. This approach is limited, as analyzing an intermediate
representation in isolation ignores the downstream mapping.
For ReLU DNs, recall that the zero-level sets of the neurons construct the DN’s geometry. Thus,
the influence of an input is determined by the sign of the intermediate activations, which in turn
determines which local expert the DN employs for that input. Using this, we can demonstrate that
representing input characteristics as linear directions of intermediate activations is only anecessary
condition for ensuring they influence the behavior of the DN.
Lemma 3.1.Let X1 andX2 be two sets of inputs with distinct characteristics. A necessary condition,
but not sufficient condition, for a ReLU DN to representX1 andX2 as distinct features, is that the
corresponding intermediate activations at some layer form linear directions.
Proof.For necessity, assume the network successfully represents X1 andX2 as distinct features.
For the representations to have consistently different influences, the network must assign different
activation patterns to the inputs ofX1 andX2. This means that, at some intermediate layer, at least one
neuron activates exclusively for the latent activations of onlyX1 orX2. Therefore, the activation level
set of this neuron must separate the latent activations of the two input sets. Because the activation
level-set of a ReLU neuron is a hyperplane, the latent activations ofX1 andX2 must lie in distinct
half-spaces defined by this hyperplane. Geometrically, being strictly separable by a hyperplane
implies that the activations separate along distinct linear directions in that intermediate feature space.
For insufficiency, assume that the intermediate activations of X1 andX2 do form distinct linear
directions (i.e., are linearly separable) at some intermediate layerl. This intermediate separation does
not guarantee that the final network output will represent them as distinct features. A subsequent
layerl+k could easily map these separated activations to the exact same output representation. For
example, if the weight matrix of a subsequent layer is composed entirely of zeros, or if a sufficiently
large negative bias is applied such that the ReLU function outputs zero for all inputs from bothX1 and
X2, the previously distinct representations collapse into a single point. Therefore, while intermediate
linear separation is required, it is not sufficient to guarantee distinct feature representation at the
output.
Lemma 3.1 formalizes a flaw in the LRH, in that it assumes features are mapped along linear sub-
spaces but entirely decouples this from the learned input-output map. Specifically, an intermediate
linear separation can be easily collapsed by subsequent layers; thus, there remains an ambiguity
as to whether identified features actually drive the network’s mapping or are merely spurious arti-
facts [51]. This mapping-blindness may explain why current interpretability techniques that study the
structure of intermediate activations, such as linear classifiers [26] and sparse autoencoders [21, 54],
exhibit brittleness when applied to downstream tasks [38, 52], and are insufficient for explaining the
functional behavior of DN sub-components [47].
3.2 Using Geometry to Identify Features
To overcome the LRH’s mapping-blindness, we propose anchoring feature discovery to the network’s
actual input-output mapping via its centroids. In particular we propose theLinear Centroids
Hypothesis (LCH):
The features of a DN are represented by linear directions in its centroid spaces.
Intuitively, the LCH states that the features of a DN can be identified by observing the collection of
inputs acted on by “aligned” local experts. Because centroids are derived directly from the network’s
Jacobians, this formulation is inherently mapping-aware.
In Appendix D, we understand what the LCH means from the perspective that views the geometry
of a DN as constructed through the collection of hyperplanes defined by each neuron of the DN
(see Appendix A). Although this is only applicable to CPA DN, in this context, linearly aligned
centroids are equivalent to a partition geometry formed by hyperplane boundaries that accumulate
along boundaries. Consequently, the LCH is supported by prior works that empirically observe that
this type of structured geometry explains many properties of DNs. Humayun et al. [24] demonstrates
that the generalization and robustness properties of DNs – including transformers, residual networks,
and convolutional neural networks – emerge as the regions of the DN’s geometry accumulate along
the decision boundaries of the input space. Similarly, the size of the linear region was linked to the
5

striped
porous
striped
flecked
0 0.5 1
50
100
Correlation
Accuracy
LRH
LCH
Figure 3:The LCH holds true for pre-trained vision models on ImageNet and mitigates the
identification of spurious features.In the first and second panels, we show that the centroids
of inputs representing distinct features of the DN separate along linear directions under principal
component analysis (PCA). We study the centroids of the fourth layer of a pre-trained ResNet50
model on ImageNet. We perform PCA on the centroids of inputs from two distinct classes in the
DTD dataset. In the third panel, we train a DN on a version of FashionMNIST that has a color
feature correlated with the corresponding classification task. We train DNs on this dataset at different
correlation levels and measure the ability of a linear probe to extract the color feature using either
the intermediate activations (LRH) or the centroids (LCH) of the DN. We consider five randomly
initialized DNs at each correlation, and report the mean and standard deviation of the probe accuracy.
toxicity property of large language models [7]. Likewise, the density of linear regions in the geometry
of DN sub-components has been connected to the reasoning capabilities of large language models
[10].
We provide evidence for the LCH with the third and fourth panels of Figure 1 and the first and second
panels of Figure 3.
In the third and fourth panels of 1, we consider a DN trained to classify whether two-dimensional
input points are inside or outside the star-shaped polygon shown in the third panel of Figure 1. In this
instance, the characteristics of the input space that the DN ought to acquire as features are the interior
and exterior of the polygon. By sampling input points from the edges of the star within the DN’s
input space and observing their centroids, we can clearly see the emergence of linear directions, see
the fourth panel of Figure 1. In Appendix E, we replicate this for other polygons and DNs that are
not CPA.
Similarly, for a ResNet50 DN [17] pre-trained on ImageNet [28], we observe in the first and second
panels of Figure 3 that the centroids for inputs exhibiting distinct texture-based features (obtained
using the DTD dataset [ 8]) separate into distinct linear directions under a principal component
analysis.
In Appendix G, we further support the LCH by showing that it validates the Platonic Representation
Hypothesis by demonstrating that increasingly larger models–of different modalities–converge to the
same representations of features as characterized by linear directions of centroids.
3.3 The Linear Centroids Hypothesis Mitigates Spurious Feature Identification
As established by Lemma 3.1, the LRH suffers from an ambiguity as to whether intermediate
activations that form linear directions actually correspond to features or are merely spurious [51]. In
contrast, the LCH is mapping-aware, as it identifies structures in the centroids that are inherently tied
to the functional behavior of the DN through the Jacobian. We demonstrate that this grounding in the
input-output map makes LCH less susceptible to spurious features than the LRH.
For this, we train a convolutional neural network to classify the FashionMNIST dataset [58]. However,
at initialization, we color the images by sampling from a discrete set of 10 colors and varying the
degree of correlation between the coloring and the dataset labels. When the coloring is fully correlated,
the color feature is not spurious; when it is random, it is spurious. We evaluate the extent to which
the color feature is linearly represented by training a linear probe to predict color from the DN’s
intermediate activations or centroids and measuring its accuracy. In the third panel of Figure 3, it
is clear that the centroids of the color feature form linear directions to the extent that the feature is
6

relevant to the task, in contrast to intermediate activations, which are linear even when the feature is
spurious. This demonstrates that LCH effectively filters out spurious correlations.
4 Interpretability Under the Linear Centroids Hypothesis
We now replicate standard LRH-based interpretability studies under the LCH, on models including
DINOv2 [40], DINOv3 [48], GPT2 [42], and Llama-3.1-8B [15]. In Appendix H, we detail the dif-
ferences in computational resources required to perform these experiments under the LCH compared
to under the LRH. The only difference arises in the extraction of the activations, for which centroids
take around 10-15% longer. In the grand scheme of running these models, this addition is negligible.
4.1 Feature Extraction with Sparse Autoencoders
Here, we compare sparse autoencoders trained on the intermediate activations and centroids from
DINOv2 and DINOv3. Because centroids encode the local mapping rather than just spatial positioning
in a latent space, we hypothesize that feature dictionaries built on LCH will be more semantically
robust and less prone to spurious correlations. Similar to Hindupur et al. [19], we extract the
intermediate activations and centroids of Imagenette [20] from these models at the last multi-layer
perceptron block to train a TopK sparse autoencoder [13].
We compare the obtained DINOv2 feature dictionaries in the following ways: Train linear probes
on the feature decompositions of the train set of Imagenette to classify its classes, and then evaluate
the accuracy of the probe on the feature decompositions of the test set of Imagenette. Record the
frequency at which the features of the sparse autoencoder fire on the test set of Imagenette.
8 16 32 64
88
90
92
94
96
K
Probe Accuracy
0 2,000 4,000 6,000 8,000
0
2
4
6
Rank
Log Activation Frequency
0 0.2 0.4 0.6 0.8 1
0
5
10
Cosine Similarity
Density
LCH
LRH
Figure 4:Feature dictionaries from sparse autoencoders trained on centroids transfer better on
downstream tasks, are more active on unseen inputs, and persist more coherently across model
sizes.In the first panel, we report the accuracy of linear probes on the Imagenette test set, trained to
classify an input’s label based on which features in the feature dictionary it activates. In the second
panel, we measure the frequency with which features fire when activations from the Imagenette test
set are passed through the sparse autoencoder. In the third panel, we measure the maximum cosine
similarity between a feature from the DINOv2 dictionary and features from the DINOv3 dictionary.
With the first panel of Figure 4, we observe that the LCH feature dictionary exhibits greater general-
ization, as compared to the LRH feature dictionary. We reproduce this result for sparse autoencoders
trained on a ten-class subset of ImageNet [28] containing dog breeds in Appendix F. In particular,
we use this setting to also demonstrate that qualitatively, the features identified using LCH are more
semantically coherent.
With the second panel of Figure 4, we show that more of the LCH feature dictionary is more active
on test samples from Imagenette than the LRH feature dictionary. This highlights how, under the
LCH, identified features are less likely to be spurious.
Next, we compare the feature dictionaries obtained from DINOv2 and DINOv3. For a given activation
type (i.e., intermediate activations or centroids), we compute the maximum cosine similarity of each
DINOv2 feature with the full DINOv3 dictionary. Since DINOv3 refines the features learned by
DINOv2, the dictionary should exhibit high cosine similarities with those features. Indeed, this is
what we observe in the third panel of Figure 4 for the feature dictionaries obtained using centroids. In
contrast, for the dictionary obtained using intermediate activations, a large proportion of the features
7

have cosine similarities of around 0.4. This bimodal distribution suggests that the features identified
by LRH do not correlate across the models and are instead spurious artifacts. In contrast, because
centroids capture the functional mapping rather than arbitrary intermediate geometries, they converge
reliably across model scales, strongly validating the Platonic Representation Hypothesis [22].
4.2 Circuit Discovery using Attribution Metrics
Because centroids explicitly summarize the local experts driving the input-output map, their direct
relationship with the computational graph offers a powerful mechanism for circuit discovery. Rather
than relying on activation magnitudes, we can directly query the mapping to introduce a novel
attribution metric using centroids [14, 35, 56], and demonstrate how it can be used to perform circuit
discovery on GPT2-Large [42].
Formally, letf be a DN andf (i,ℓ) be the same DN but with theith neuron of theℓth layer manipulated.
The attribution of neuronito the features of a collection of samplesNis quantified as
s(i,ℓ)
N := 1
|N|
X
x∈N



µf
x−µf (i,ℓ)
x



2


µf
x



2
,(1)
whereµf
x andµf (i,ℓ)
x are the centroids off andf (i,ℓ) atx respectively. Quantifying the attribution
of a neuron to the local features of a sample point x can be done by taking N to beBϵ(x) =
x′∈R d :∥x−x ′∥2 <ϵ
	
.5
By patching each neuron in a layer of GPT2-Large, Clement & Joseph[9] observed that the thirty-first
layer multi-layer perceptron contains a neuron which is responsible for predicting the “an” token.
We demonstrate that similar analyses can be conducted more simply by applying Equation (1) to
a neighborhood of the last token embeddings at the input of the thirty-first layer on the prompt “I
climbed up the pear tree and picked a pear. I climbed up the apple tree and picked.” In Figure 5, the
distribution of neuron attribution values is heavily skewed, with the neuron identified by Clement &
Joseph [9], marked in black, sitting within the top 99.8th percentile of values. This demonstrates that,
rather than performing extensive ablation studies on all the neurons of GPT2-Large, querying the
network’s local mapping via equation 1 effectively isolates functional circuits and filters out irrelevant
neurons. In Appendix I, we use this example to demonstrate that equation 1 is robust as an attribution
metric.
4.3 Concept Discovery using Linear Probes
Probing is another technique that exploits linear structures in DNs to either extract features [ 26],
extract representations [37], or classify inputs [34]. Here, we explore the latter of these applications
by forming linear classifiers to discern the truthfulness of input statements to large language models.
We adopt the mass-mean probes of Marks & Tegmark [34], along with their datasets, to test the
generalization capacity of these probes. Using the likely dataset, we obtain mass-mean probes from
the twelfth layer of the Llama-3.1-8B large language model [15], either using the latent activations or
the centroids extracted from the multi-layer perceptron component. Thelikely dataset is constructed
as a classification problem of whether sample tokens are likely or unlikely under the model’s logit
distribution for non-factual textual inputs. The other datasets are formulated as classification problems
between factually truthful and untruthful statements. Therefore,likelyis identifying plausibility in
the model’s outputs rather than a concept of truthfulness. Because centroid-based mass-mean probes
generalize more effectively to these truth-identifying datasets (see Figure 6), it confirms that LCH
captures theaction(the mapping) of outputting a truthful statement, rather than just the isolated
concept. This underscores the intuition that LCH offers a mechanistic perspective by evaluating when
the local experts of a DN align.
5 Discussion
The Linear Representation Hypothesis posits that feature discovery involves finding linear subspaces
in the activation spaces of DN, but this critically decouples those features from the network’s actual
5Henceforth, we will uses (i,ℓ) to denotes (i,ℓ)
Bϵ(x) unless stated otherwise.
8

Figure 5:Neuron-attribution metrics derived
using LCH can quickly filter out irrelevant
neurons, facilitating circuit discovery.We
prompt GPT2-Large and note the normalized
attribution value (using Equation (1)) in a neigh-
borhood of the embedding at the input of the
multi-layer perceptron block at the thirty-first
layer of the last token of this prompt. The neigh-
borhood is constructed by sampling 256 points
within a radius of 0.25 of the embedding. We
normalize these values to the range [0,1] . In
black we indicate the 892nd neuron in the multi-
layer perceptron.
Figure 6:Linear probes obtained using LCH
exhibit greater generalization than those ob-
tained using LRH.We obtain mass-mean
probes on the likely dataset from the twelfth
layer of Llama-3.1-8B, either using intermedi-
ate activations or centroids extracted from the
multi-layer perceptron component. We then test
these probes using other datasets from Marks &
Tegmark [34].
input-output map. To make feature discovery mapping-aware, we introduced the Linear Centroids
Hypothesis (LCH), which posits that feature discovery amounts to finding linear directions incentroid
space. Unlike intermediate representations, DN centroids are mapping-aware, hierarchically defined,
intuitive artifacts of DNs that describe the DN’s local experts.
Because centroids are efficiently accessible via Jacobian vector products, they serve as a drop-in
replacement for activations in standard interpretability pipelines. Consequently, we can demonstrate
that LCH is operational and inherently resists the identification of spurious features.
Ultimately, LCH unifies feature dictionaries, probing, circuits, and saliency maps into a single
geometric framework, ensuring that interpretability is mechanistically grounded in how the network
actually computes.
Limitations and Future Work.The power diagram subdivision of a DN is parameterized by both
centroids and radii. This study focuses entirely on the centroids, leaving the radii—which determine
whether a centroid is contained within its own region—unexplored. Future research should investigate
these radius parameters, as integrating them could provide an even more comprehensive geometric
interpretation of the network’s local experts and their decision boundaries.
Additionally, while this work introduced thelocal centroidas a faithful, gradient-based saliency map
to highlight relevant features for single inputs, future efforts should extend this application. Testing
local centroids across a wider variety of DN architectures and broader input distributions will further
validate their explanatory power within this mapping-aware framework.
Acknowledgments
This work was supported by ONR grant N00014-23-1-2714, ONR MURI N00014-20-1-2787, DOE
grant DE-SC0020345, and DOI grant 140D0423C0076.
References
[1] Adebayo, J., Gilmer, J., Muelly, M., Goodfellow, I. et al. Sanity Checks for Saliency Maps.
Advances in Neural Information Processing Systems, 31, 2018.
[2] Amodei, D., Olah, C., Steinhardt, J., Christiano, P. et al. Concrete Problems in AI Safety.
arXiv:1606.06565, 2016.
9

[3] Balagansky, N., Maksimov, I., and Gavrilov, D. Mechanistic Permutability: Match Features
across Layers. InThe Thirteenth International Conference on Learning Representations, 2025.
[4] Balestriero, R. and Baraniuk, R. Mad Max: Affine Spline Insights into Deep Learning.
arXiv:1805.06576, 2018.
[5] Balestriero, R. and Baraniuk, R. G. From Hard to Soft: Understanding Deep Network Non-
linearities via Vector Quantization and Statistical Inference. InInternational Conference on
Learning Representations, 2018.
[6] Balestriero, R., Cosentino, R., Aazhang, B., and Baraniuk, R. The Geometry of Deep Networks:
Power Diagram Subdivision. InNeural Information Processing Systems, 2019.
[7] Balestriero, R., Cosentino, R., and Shekkizhar, S. Characterizing Large Language Model
Geometry Helps Solve Toxicity Detection and Generation. InInternational Conference on
Machine Learning, 2023.
[8] Cimpoi, M., Maji, S., Kokkinos, I., Mohamed, S. et al. Describing Textures in the Wild. In
IEEE Conference on Computer Vision and Pattern Recognition, 2014.
[9] Clement, N. and Joseph, M. We Found An Neuron in GPT-2, February 2023. URLhttps://
www.lesswrong.com/posts/cgqh99SHsCv3jJYDS/we-found-an-neuron-in-gpt-2.
[10] Cosentino, R. and Shekkizhar, S. Reasoning in Large Language Models: A Geometric Perspec-
tive.arXiv:2407.02678, 2024.
[11] Croce, F., Andriushchenko, M., Sehwag, V ., Debenedetti, E. et al. RobustBench: A Standardized
Adversarial Robustness Benchmark.arXiv:2010.09670, 2020.
[12] Elhage, N., Hume, T., Olsson, C., Schiefer, N. et al. Toy Models of Superposition.Transformer
Circuits Thread, 2022.
[13] Gao, L., la Tour, T. D., Tillman, H., Goh, G. et al. Scaling and Evaluating Sparse Autoencoders.
InThe Thirteenth International Conference on Learning Representations, 2025.
[14] Goldowsky-Dill, N., MacLeod, C., Sato, L., and Arora, A. Localizing model behavior with path
patching.arXiv:2304.05969, 2023.
[15] Grattafiori, A., Dubey, A., Jauhri, A., Pandey, A. et al. The Llama 3 Herd of Models.
arXiv:2407.21783, 2024.
[16] Hanin, B. and Rolnick, D. Complexity of Linear Regions in Deep Networks. InProceedings of
the Thirty-sixth International Conference on Machine Learning. PMLR, 2019.
[17] He, K., Zhang, X., Ren, S., and Sun, J. Deep Residual Learning for Image Recognition. In
IEEE Conference on Computer Vision and Pattern Recognition, 2016.
[18] Hendrycks, D. and Gimpel, K. Gaussian Error Linear Units (GELUs).arXiv:1606.08415, 2023.
[19] Hindupur, S. S. R., Lubana, E. S., Fel, T., and Ba, D. E. Projecting Assumptions: The Duality
between Sparse Autoencoders and Concept Geometry. InICML Workshop on Methods and
Opportunities at Small Scale, 2025.
[20] Howard, J. and Gugger, S. Fastai: A Layered API for Deep Learning.Information, 11(2), 2020.
[21] Huben, R., Cunningham, H., Smith, L. R., Ewart, A. et al. Sparse Autoencoders Find Highly
Interpretable Features in Language Models. InThe Twelfth International Conference on
Learning Representations, 2024.
[22] Huh, M., Cheung, B., Wang, T., and Isola, P. Position: The Platonic Representation Hypothesis.
InForty-First International Conference on Machine Learning, 2024.
[23] Humayun, A. I., Balestriero, R., Balakrishnan, G., and Baraniuk, R. SplineCam: Exact
Visualization and Characterization of Deep Network Geometry and Decision Boundaries. In
IEEE Conference on Computer Vision and Pattern Recognition, 2023.
10

[24] Humayun, A. I., Balestriero, R., and Baraniuk, R. Deep Networks Always Grok and Here
Is Why. InHigh-Dimensional Learning Dynamics 2024: The Emergence of Structure and
Reasoning, 2024.
[25] Imai, H., Iri, M., and Murota, K. V oronoi Diagram in the Laguerre Geometry and Its Applica-
tions.SIAM Journal on Computing, 14(1), 1985.
[26] Kim, B., Wattenberg, M., Gilmer, J., Cai, C. et al. Interpretability beyond Feature Attribution:
Quantitative Testing with Concept Activation Vectors (TCA V). InProceedings of the Thirty-fifth
International Conference on Machine Learning, 2018.
[27] Kingma, D. P. and Ba, J. Adam: A Method for Stochastic Optimization.arXiv:1412.6980,
2017.
[28] Krizhevsky, A., Sutskever, I., and Hinton, G. E. ImageNet Classification with Deep Convolu-
tional Neural Networks. InAdvances in Neural Information Processing Systems, 2012.
[29] Liu, C., Dong, Y ., Xiang, W., Yang, X. et al. A Comprehensive Study on Robustness of Image
Classification Models: Benchmarking and Rethinking.International Journal of Computer
Vision, 133(2), 2024.
[30] Liu, Z., Lin, Y ., Cao, Y ., Hu, H. et al. Swin Transformer: Hierarchical Vision Transformer
Using Shifted Windows. InInternational Conference on Computer Vision, 2021.
[31] Liu, Z., Mao, H., Wu, C.-Y ., Feichtenhofer, C. et al. A ConvNet for the 2020s. InIEEE
Conference on Computer Vision and Pattern Recognition. IEEE Computer Society, 2022.
[32] Lyche, T. and Schumaker, L. L. Local Spline Approximation Methods.Journal of Approximation
Theory, 15(4), 1975.
[33] maintainers, T. and contributors. TorchVision: PyTorch’s Computer Vision Library, 2016. URL
https://github.com/pytorch/vision.
[34] Marks, S. and Tegmark, M. The Geometry of Truth: Emergent Linear Structure in Large
Language Model Representations of True/False Datasets. InFirstConference on Language
Modeling, 2024.
[35] Meng, K., Bau, D., Andonian, A. J., and Belinkov, Y . Locating and Editing Factual Associations
in GPT. In Oh, A. H., Agarwal, A., Belgrave, D., and Cho, K. (eds.),Advances in Neural
Information Processing Systems, 2022.
[36] Mont´ufar, G., Pascanu, R., Cho, K., and Bengio, Y . On the Number of Linear Regions of Deep
Neural Networks. InNeural Information Processing Systems, 2014.
[37] Nanda, N., Lee, A., and Wattenberg, M. Emergent Linear Representations in World Models of
Self-Supervised Sequence Models. InProceedings of the sixth BlackboxNLP Workshop: Ana-
lyzing and Interpreting Neural Networks for NLP. Association for Computational Linguistics,
2023.
[38] Nicolson, A., Schut, L., Noble, A., and Gal, Y . Explaining Explainability: Recommendations
for Effective Use of Concept Activation Vectors.Transactions on Machine Learning Research,
2025.
[39] Olah, C., Cammarata, N., Schubert, L., Goh, G. et al. Zoom in: An Introduction to Circuits.
Distill, 2020.
[40] Oquab, M., Darcet, T., Moutakanni, T., V o, H. V . et al. DINOv2: Learning Robust Visual
Features without Supervision.Transactions on Machine Learning Research, 2024.
[41] Park, K., Choe, Y . J., and Veitch, V . The Linear Representation Hypothesis and the Geometry of
Large Language Models. InForty-first International Conference on Machine Learning, 2024.
[42] Radford, A., Wu, J., Child, R., Luan, D. et al. Language Models Are Unsupervised Multitask
Learners.OpenAI, 2019.
11

[43] Ramachandran, P., Zoph, B., and Le, Q. V . Searching for Activation Functions.
arXiv:1710.05941, 2017.
[44] Rodr´ıguez-Mu˜noz, A., Wang, T., and Torralba, A. Characterizing Model Robustness via Natural
Input Gradients. InProceedings of the European Conference on Computer Vision, 2024.
[45] Schumaker, L.Spline Functions: Basic Theory. Cambridge Mathematical Library. Cambridge
University Press, 3 edition, 2007.
[46] Selvaraju, R. R., Cogswell, M., Das, A., Vedantam, R. et al. Grad-CAM: Visual Explanations
From Deep Networks via Gradient-based Localization. InIEEE International Conference on
Computer Vision, 2017.
[47] Sharkey, L., Chughtai, B., Batson, J., Lindsey, J. et al. Open Problems in Mechanistic Inter-
pretability.arXiv:2501.16496, 2025.
[48] Sim ´eoni, O., V o, H. V ., Seitzer, M., Baldassarre, F. et al. DINOv3.arXiv:2508.10104, 2025.
[49] Simonyan, K., Vedaldi, A., and Zisserman, A. Deep Inside Convolutional Networks: Visualising
Image Classification Models and Saliency Maps. InWorkshop at International Conference on
Learning Representations, 2014.
[50] Smilkov, D., Thorat, N., Kim, B., Vi´egas, F. et al. SmoothGrad: Removing Noise by Adding
Noise.arXiv:1706.03825, 2017.
[51] Smith, L. The ‘Strong’ Feature Hypothesis Could Be Wrong, August 2024. AI Alignment
Forum.
[52] Smith, L., Rajamanoharan, S., Conmy, A., McDougall, C. et al. Negative Results for Sparse
Autoencoders On Downstream Tasks and Deprioritising SAE Research, March 2025. Medium.
[53] Sundararajan, M., Taly, A., and Yan, Q. Axiomatic Attribution for Deep Networks. In
International Conference on Machine Learning. PMLR, 2017.
[54] Trenton Bricken, Adly Templeton, Joshua Batson, Brian Chen et al. Towards Monosemanticity:
Decomposing Language Models With Dictionary Learning.Transformer Circuits Thread, 2023.
[55] van der Maaten, L. and Hinton, G. Visualizing Data Using T-SNE.Journal of Machine Learning
Research, 9(86), 2008.
[56] Wang, K. R., Variengien, A., Conmy, A., Shlegeris, B. et al. Interpretability in the Wild:
A Circuit for Indirect Object Identification in GPT-2 Small. InThe Eleventh International
Conference on Learning Representations, 2023.
[57] Workshop, B., :, Scao, T. L., Fan, A. et al. BLOOM: A 176B-Parameter Open-access Multilin-
gual Language Model.arXiv:2211.05100, 2023.
[58] Xiao, H., Rasul, K., and V ollgraf, R. Fashion-MNIST: A Novel Image Dataset for Benchmarking
Machine Learning Algorithms.arXiv:1708.07747, 2017.
12

A Deep Network Geometry
The regions forming the geometry of a DN are constructed by the intersection of a collection of
hyperplanes [4, 16, 36]. Each nonlinearity (neuron) in a layer of the DN determines an activation
level set within its input space (i.e., the hyperplane between being active or inactive in the case of
the ReLU nonlinearity). In a hierarchical fashion, starting from the first layer, these hyperplanes are
pulled back to the input space of the DN and intersect to form the regions [6, 23].
The power diagram subdivision parametrization of the DN geometry, instead views the geometry as a
hierarchical intersection of power diagrams [6].
Definition A.1.Given a collection of Q centroid-radius pairs{(µq,τq)}Q
q=1⊆R d×R , a power
diagram tessellates Rd intoQ disjoint tiles Ω ={ω 1,...,ω Q} such that∪Q
q=1ωq =R d, with each
tile given by
ωq =
(
x∈R d :q= arg min
q′∈{1,...,Q}

∥x−µ q′∥2
2−τq′
)
.(2)
The distance minimized in (2) is called the Laguerre distance [25], and differs from the Euclidean
distance only in the addition of the weighting provided by the radius parameter.
The power diagram subdivision induced by the DN is then constructed recursively through layer-wise
power diagrams. The first layer of the DN partitions the input space Rd(1)
as Ω(1) through a power
diagram. The second layer of the DN then partitions the projections of each tileω(1)∈R d in Rd(1)
induced byf (1) as a power diagram. These are then pulled back to Rd to yield a finer partition of
the input space Ω(1←2). This partition is an example of a power diagram subdivision. Continuing
sequentially for each layer completes the power diagram subdivisionΩof the DN [6].
Just like for a regular power diagram, we can also associate each region in a power diagram subdivision
with acentroidandradius. Despite each tile in a power diagram subdivision being defined implicitly
through a recursive combinatorial intersection of half-spaces, we will show that its centroid and
radius are defined explicitly and computable independently of other regions.
We focus on centroids and how they can be analyzed to understand thefeaturesof a DN, though the
radii are also of considerable interest. Indeed, it is the presence of the radius that means that the
centroid of a region in a power diagram need not be contained within the region itself.
B Local Centroids
Here, we provide further illustrations of local centroids computed for state-of-the-art DNs. In
particular, we demonstrate that for randomly initialized DNs, local centroids contain no information
(see Figure 14). Furthermore, we show that considering DN sub-components from the input space to
hidden layers facilitates the extraction of hierarchical saliency maps. For example, in the top row of
Figure 15, we compare local centroids computed from the input space to a hidden layer and from
the input space to the output layer of a Swin-B transformer [30]. Since the windows of the aircraft
are only apparent in the centroid of the full DN, it follows that the windows are a feature of the later
layers of the DN.
C Comparison to Prior Work
Features.Our notion of a DN feature (see Section 3.1) is analogous to the notion of a DN concept
used in Park et al. [41], which provides a rigorous theoretical characterization of the LRH. In Park
et al. [41], a DN feature is a variable that leads to a particular output when caused by a context. In
our case, the context would correspond to the input samples that possess a given characteristic. The
variable notion of Park et al. [41] would then be equivalent to our requirementrepresentation. Then
the referenced causation on the output would be equivalent to our requirement of causing aninfluence.
Circuits.Circuits were initially introduced in Olah et al. [39] to deal with the apparent poly-
semantic nature of neurons. That is, specific neurons were observed to trigger on seemingly semanti-
cally disjoint inputs, whereas ensembles of neurons demonstrated more reliable activation patterns.
13

Instead, our notion of a circuit arises naturally as the responses of the components of a DN to a
feature. Indeed, this response is likely to involve multiple neurons or components of a DN, given the
DN’s compositional construction.
D The Implication of the LCH on Hyperplane Geometry
In this section, we formalize the relationship between aligned centroids and the hyperplane geometry
of DNs described in Appendix A. We first prove that at any given layer, centroids lying on a one-
dimensional affine subspace imply that the boundaries separating their regions are strictly parallel.
Proposition D.1.At the input space of layer ℓ, if the centroids of a sequence of adjacent linear
regions lie on a one-dimensional affine subspace, then the hyperplanes forming the boundaries
between these consecutive regions are strictly parallel.
Proof. Consider a sequence of adjacent linear regions ω1,...,ω k in the input space of layer ℓ,
separated by boundary hyperplanes Π1,...,Π k−1. Let their corresponding power diagram centroids
beµ1,...,µ k. The shared boundary Πi between regioni andi+ 1 has a normal vector defined by
the difference of their centroids:ni =µ i−µi+1. Assume the centroids lie on a one-dimensional
affine subspace. Then, there exists a base point p and a unit direction vectord such that for all i,
µi =p+t idfor some scalart i. The normal vector for the boundaryΠ i is then:
ni =µ i−µi+1 = (ti−ti+1)d.
Because every normal vector ni is a scalar multiple of the exact same direction d, all boundary
hyperplanesΠ 1,...,Π k−1 share the same normal direction and are therefore strictly parallel.
While Proposition D.1 establishes parallel boundaries in the intermediate representation space of layer
ℓ, the network’s overall behavior is determined by how these boundaries map back to the original
input spaceRd.
The parallel hyperplanes Π1,...,Π k−1 at layerℓ form a tightly packed, linear decision band. The
boundary in the original input space corresponding to Πi is its pre-image under this mapping
x∈R d :f (1←ℓ−1)(x)∈Π i
	
. Because f (1←ℓ−1) is a composition of affine transformations and
non-linearities (like ReLU), it fundamentally acts by folding, stretching, and compressing the input
space.
Low Robustness
 High Robustness
Figure 7: Taken from Humayun et al. [23], this is an illustration of the geometry of a fully connected
ReLU DN as it trains on MNIST. Three training samples are fixed to construct a two-dimensional
slice of the DN’s input domain, and the linear regions that intersect this slice are then visualized. On
theleftis the geometry of the DN when it has generalized but exhibits low levels of robustness. On
therightis the geometry of the DN when it exhibits the additional property of robustness.
When we “pull back” the parallel hyperplanesΠi through this mapping, a single straight hyperplane in
layerℓ pulls back to a continuous, piecewise linear surface in the input space. Each time the pre-image
crosses an activation boundary from an earlier layer, the surface bends, allowing it to approximate
macroscopic curves. Because the hyperplanes Π1,...,Π k−1 are parallel and sequentially packed in
14

layerℓ, their pre-images map to a dense bundle of piecewise linear surfaces in the input space. In
regions where the mappingf (1←ℓ−1) highly compresses the input manifold, this bundle of boundaries
packs densely together. By accumulating these intricately folded, tightly packed linear regions, the
network effectively constructs smooth, arbitrarily curved decision boundaries to separate complex
features in the input data.
Consequently, the linear alignment of centroids at an intermediate layer is the geometric mechanism
by which a DN coordinates a massive accumulation of linear regions to trace out curved, semantically
meaningful feature boundaries in the original input space. An example of this is shown in Figure 7.
E Analyzing Deep Networks Trained to Classify Interiors of Polygons
Here we continue the analysis of the DN training to classify the interior of a star-shaped polygon, as
depicted in the third and fourth panels of Figure 1.
First, we can observe in Figure 8 that the linearity of the centroids of Figure 1 emerges gradually
through training. At initialization, the centroids have a similar arrangement to the input samples
because the DN is randomly initialized. However, as training progresses, we observe that the centroids
slowly migrate and align themselves. In particular, we can see the alignment of the centroids manifest
before they reach their final positions.
Epoch0
 Epoch18
 Epoch27
 Epoch147
 Epoch512
Figure 8: Throughout the training of the DN of the bottom row Figure 1, we tracked the DN centroids
of the input samples highlighted in the bottom left panel Figure 1.
Second, as expected from the discussion of Appendix D, in the second panel of Figure 9 we see that
the trained DN geometry exhibits linear regions with roughly parallel boundaries along the polygon’s
edges. Moreover, in the third and fourth panels of Figure 9, we observe the activation level-sets of the
nonlinearities of the second and third hidden layers of this DN. It is clear that the full identification of
the interior and exterior of the polygon is achieved in the third layer, as the nonlinearities delineate
the polygon’s edges. The second-layer nonlinearities capture the coarser features relating to the three
exterior sectors created by the star shape. This is evidenced by each nonlinearity forming along one
of the polygon’s outer edges.
Third, in addition to centroids possessing a linear structure under the LCH, it is evident from Figure 1
that this structure is semantically coherent. Suggesting that applications of these topological point-
cloud analyses may be particularly fruitful under the LCH. To aid the study of centroids as point clouds,
we soften DNs using CPA nonlinearities (e.g., ReLU) by replacing them with smooth approximations
(e.g., GELU). The GELU nonlinearity [18] belongs to the swish family of nonlinearities [43], which
are theoretically known to provide an appropriate softening of a ReLU DN’s geometry [5]. In the
first panel of Figure 10, we show that this smooth approximation does not impact the structure of the
centroids. In the second panel of Figure 10, we consider a t-SNE embedding [55] of these softened
centroids at the second hidden layer of the DN. We observe clustering of centroids by the sector
of the input domain in which the input samples were located. This corroborates our prior analysis
using the second hidden layer’s geometry. Moreover, it demonstrates how the LCH can be applied
hierarchically. In Figure 1, centroids were computed across the entire DN to understand the finest
features of the DN, whereas in Figure 9, centroids were computed across a single layer to identify
coarser features. Similar analyses under the LRH are challenging, as there is no notion of latent
activations across different scales of sub-components [3].
Fourth, we can analyze the neurons of the DN using Equation (1). In the third panel of Figure 10, we
see that the neurons of the third hidden layer have an encompassing effect on the entire boundary of
the polygon,
15

Input Polygon
 DN Geometry
 2nd Hidden Layer
 3rd Hidden Layer
Figure 9: The activation level-sets of the nonlinearities of a DN have a structure that is related to
features of a DN. Here we train a fully connected ReLU DN with a two-dimensional input space and
a one-dimensional output space to classify the interior and exterior of the star-shaped polygon shown
in the first panel. In the second panel, we visualize the geometry of the trained DN. The color of the
linear regions represents the Frobenius norm of the affine transformation parameterAω operating on
that linear region. We then separate the hyperplanes corresponding to the nonlinearities of the second
layer (third panel) and those of the third layer (fourth panel).
GELU Centroids
 2nd Layer Centroids t-SNE
 s(i,3)
Figure 10: In the first panel, we show that replacing the ReLU nonlinearities with GELU nonlinearities
for the DN of Figure 9 does not change the structure of the centroids significantly. In the second
panel, we show, using t-SNE analysis of the second-layer centroids of the DN in Figure 9, that the
second layer encodes features corresponding to the three external sectors of the star-shaped polygon.
In the third panel, we show that the third layer of the DN of Figure 9 captures the inter-exterior feature
by demonstrating that neurons in this layer are sensitive (as per Equation (1)). More specifically, for
a grid of points in the input space, we apply Equation (1) to a small neighborhood around each point
and visualize the resulting value as a heatmap.
In addition to the star-shaped polygon considered in the main text, in Figure 16 we corroborate the
observed patterns when the input distribution is a bowtie-shaped and reuleaux-shaped polygon.
Moreover, we can show that starting from a non CPA DN, we can repeat the same investigations and
derive similar conclusions. For example, as showing in Figure 11, when replacing the nonlinearity
back to a ReLU we can observe its geometry using SplineCam [23] and see that nonlinearities still
align along the boundary of the polygon, when we observe the centroids of input samples we see the
same linear structures, and the influence of pruning neurons on the centroids is still effective as a
neuron attribution metric.
F Qualitative Analysis of Feature Dictionaries
Here, we provide a qualitative analysis of the feature dictionaries constructed in Section 4.1. To
address the concern that Imagenette may provide a relatively easy setting, we train sparse autoencoders
on a subset of ImageNet sampled from ten random dog breeds.
16

DN Geometry
 Centroids
 s(i,2)
 s(i,3)
Figure 11: Here we train a DN in the same manner as the one considered in Figure 9, except we
use the GELU nonlinearity. In the first panel, we replace the nonlinearities with ReLU such that we
can use SplineCam to visualize its geometry. In the second panel, we visualize the centroids from
input samples. In the third and fourth panels, we consider the sensitivities of centroids when pruning
neurons from the second and third layers, respectively.
In the first panel of Figure 12, we can see that even in this more challenging setting, the features
learned under LCH generalize better, just like in Figure 4.
Moreover, with the right panel of Figure 12, we can see qualitatively that the features identified
using LCH are more semantically coherent. Here, we identify similar samples from the test set by
computing the Jaccard similarity of their feature activation patterns. We create a grid of images, with
the first image as a fixed sample and the remaining six as its closest neighbors by Jaccard similarity.
In both cases, the features identify the same dog breed; however, only under LCH do we consistently
see a dog with the same head position.
8 16 32 64
55
60
65
70
75
K
Probe Accuracy
LCH
LRH
LRH
LCH
Figure 12: Here we train sparse autoencoders in the same ways as Figure 4, but on a subset of
ImageNet [28] containing ten random dog breed classes, which we split into a train and test set. In
the first panel, we evaluate the sparse autoencoders by training linear probes on the feature activation
of the training set and measuring their accuracy on the test set. In the right panel, we sample from
the test set and compute the Jaccard similarity between its feature activation pattern and those of the
other samples in the test set. We visualize the sample in the left image in the grid, then identify the
six most similar samples using the other images in the grid.
G Validating the Platonic Representation Hypothesis
The Platonic Representation Hypothesis (PRH) states that as DNs become larger and more capable,
the features they form converge [22]. With Figure 13, we demonstrate that analyzing centroids in a
similar manner also supports the PRH. In Figure 13, we adopt the methodology of Huh et al. [22]
and compare the cosine similarities of activations (i.e., latent activations or centroids) computed
across layers of BLOOM language models [57] of increasing capacity to those computed across the
DINOv2 vision transformer [40]. As expected under the PRH, the cosine similarity of activations and
model capacity is positively related.
A limitation of this analysis is that it considers only the maximum cosine similarities among all
possible activations of one DN and all possible activations of another. It does not account for how the
full spectrum of features in one model aligns with those of another. This is rectified by our analysis
17

109
Number of Parameters
0.105
0.110
0.115
0.120
0.125Latent Alignment
bloomz-560mbloomz-1b1 bloomz-3b bloomz-7b1
Latents
Centroids
0.044
0.046
0.048
0.050
Centroid Alignment
Figure 13: The Platonic Representation Hypothesis is validated by observing the cosine similarities
between the centroids of DNs of different capacities. We compare the alignment of centroids from
the BLOOM language model to the centroids of the DINOv2 vision model.
shown in the third panel of Figure 4, which demonstrates that the LCH more faithfully captures this
hypothesis.
H Computational Requirements.
A valid concern with exploring the LCH is the computational burden it imposes on interpretability, as
it requires evaluating the DN’s Jacobians. Fortunately, this interrogation only requires considering
Jacobian vector products (see Proposition 2.1), which are significantly cheaper to compute in common
computational frameworks. Furthermore, the analysis of centroids often focuses on a relatively small
component of the DN. Thus, this computation would appear relatively insignificant compared to
processing the entire DN. In this section, we empirically quantify the computational burden of using
centroids rather than latents in our main experiments in Section 4.
FashionMNIST Color Correlation.This experiment took approximately 2 hours on a Quadro
RTX 8000. For each correlation value (six in total), five separate DNs were trained. Two linear
probes were then trained to classify the color feature, one using intermediate activations and the other
using centroids.
The DN comprised a three-layer convolutional feature extractor followed by a two-layer multi-layer
perceptron classifier. Intermediate activations were extracted from the input to the classifier, and
centroids were computed using the input-output Jacobian of the classifier.
The DN was trained for 10 epochs using the Adam [27] optimizer at a learning rate of 0.001. The
linear probe was trained for 3 epochs, again with the Adam optimizer at a learning rate of0.001.
DINO Feature Extraction.For this experiment, we find almost no difference in the time necessary
to extract centroids. It only takes 8.7 seconds compared to extracting intermediate representations,
which takes 7.8 seconds. After these vectors are extracted, the computational pipeline is identical
when using centroids or intermediate activations.
In the first panel of Figure 4, we train TopK sparse autoencoders [ 13] on all token positions of
DINOv2 and sparsity values 8, 16, 32, and 64. Training each sparse autoencoder for 40 epochs takes
around 1 hour on an NVIDIA TITANX. In the second panel of Figure 4, we consider the sparse
autoencoders with sparsity value32.
In the third of Figure 4, we consider similar sparse autoencoders but trained on only theclstoken
of DINOv2/v3. Training each of these sparse autoencoders takes about 2 minutes on an NVIDIA
TITANX.
18

GPT2 Circuit Discovery.Although there is no direct analog of this experiment with latent activa-
tions, we can still argue that the computational burden is relatively benign. In particular, since we
only compute centroids across the multi-layer perceptron block of the thirty-first layer, we only need
to consider the Jacobian vector product for this component. This can be done by storing the gradients
from a forward pass across this block, which, relative to performing a forward pass across the model,
is insignificant. This experiment takes less than 1 hour on an NVIDIA TITANX.
Llama-3.1-8B Probes.To implement this experiment, we use the setup of https://github.
com/saprmarks/geometry-of-truth. The only difference involves the extraction of centroids
in addition to the extraction of intermediate activations. Extracting centroids took 2329 seconds
compared to470seconds for intermediate activations.
I Robustness of Neuron Attribution with Centroids
In order for Equation (1) to prove useful as a tool for interpreting DNs, it is essential that it is robust
in its application. For example, Equation (1) ought not be sensitive to the neighborhoodN chosen.
Furthermore, since in practice we can only approximate Equation (1) by taking a finite sample of
points fromN, it is important that Equation (1) has low variance in relation to this finite sample. In
Figure 17, we test both these properties for the experiment of Figure 5. In the left plot, we observe that
attribution values have a low variance when a finite sample is used to approximate the neighborhood
N . In the right plot, we observe that the percentile of a particular neuron within the DN layer is
stable across different neighborhood sizes. This ensures that conclusions derived from Equation (1)
are robust.
J Model Licenses
Swin-B [30], ResNet [17] and ConvNeXt-L [31] are obtained through PyTorch [ 33] and Robust-
Bench [11] under an MIT license.
DINOv2 [40] is used under an Apache 2.0 license, DINOv3 [ 48] under the DINOv3-license, the
Bloom language models [57] under the BigScience RAIL license, Llama-3.1-8B under the Llama3.1
license, GPT-2 [42] is obtained through the nano-GPT6 repository under an MIT license.
6https://github.com/karpathy/nanogpt
19

Input
Sample
Local Centroid
(Input Space to Hidden Layer)
Local Centroid
(Input Space to Output)
Local Centroid
(At Random Initialization)
Figure 14: The local centroids of the pre-trained ConvNext-L DN from PyTorch.
20

Input
 Local Centroid (Input Space to Hidden Layer)
 Local Centroid (Input Space to Output)
Figure 15: The local centroids of the adversarially Swin-B transformer from Rodr´ıguez-Mu˜noz et al.
[44].
21

Input Distribution
 Functional Geometry
Input Samples
 Centroids
 s(i,3)
Input Distribution
 Functional Geometry
Input Samples
 Centroids
 s(i,2)
Figure 16: Here we perform some of the same analyses as conducted previously, but with a DN
trained on a bowtie-shaped polygon,toptwo rows, and a reuleaux-shaped polygon,bottomtwo rows.
22

Figure 17: The neuron attribution metric of Equation (1) is a robust measure for interpreting the
neurons of a DN. Here we consider the robustness of Equation (1) for the experiment in Figure 5.
More specifically, we test how the neurons’ attribution values change as we consider increasingly large
neighborhoods. The neighborhoods we consider are of the formBϵ(x), wherex is the embedding of
the last token of a prompt at the 31st of GPT2-Large. We considerϵ normalized by the norm of the
centroid ofx at this layer of the DN. To compute Equation (1) at each neuron of the layer, we sample
256 embeddings from this neighborhood. In the left plot, we observe how the average attribution
value of each neuron changes across random samplings of this neighborhood. In the right plot, we
observe how the percentile value of the 892nd changes across these random samplings. The error bars
represent one standard deviation in the observed values.
23
