Grokking Group Multiplication with Cosets
Dashiell Stander 1 Qinan Yu1 2 Honglu Fan 1 3 Stella Biderman 1
Abstract
The complex and unpredictable nature of deep
neural networks prevents their safe use in many
high-stakes applications. There have been many
techniques developed to interpret deep neural net-
works, but all have substantial limitations. Al-
gorithmic tasks have proven to be a fruitful test
ground for interpreting a neural network end-to-
end. Building on previous work, we completely
reverse engineer fully connected one-hidden layer
networks that have “grokked” the arithmetic of
the permutation groups S5 andS6. The models
discover the true subgroup structure of the full
group and converge on neural circuits that decom-
pose the group arithmetic using the permutation
group’s subgroups. We relate how we reverse en-
gineered the model’s mechanisms and confirmed
our theory was a faithful description of the cir-
cuit’s functionality. We also draw attention to
current challenges in conducting interpretability
research by comparing our work to Chughtai et al.
[4] which alleges to find a different algorithm for
this same problem.
1. Introduction
Many methods have been proposed to render deep neural
networks interpretable. There is both an academic interest
in understanding how neural networks do what they do
and a societal interest in ensuring that decisions made by
such models are sound, unbiased, and subject to human
review. These concerns are not new, nor are they unique to
deep neural networks. Many of the techniques developed
(such as SHAP values [ 33], saliency maps [ 52], gradient
attribution [51], dimension reduction [61], etc...) are still
widely used today, but there is an understanding that such
methods must be used as just one part of a careful analysis.
Naive applications of even the most sophisticated algorithms
1EleutherAI 2Brown University 3University of Geneva. Corre-
spondence to: Dashiell Stander <dash.stander@gmail.com>.
Proceedings of the 41 st International Conference on Machine
Learning, Vienna, Austria. PMLR 235, 2024. Copyright 2024 by
the author(s).
will give misleading results [1, 2, 9, 25].
Mechanistic interpretability seeks to find “neural circuits”
within deep neural networks, small sub-networks that act
as connected computation graphs and accomplish a task. In
“toy” (highly constrained) settings mechanistic interpretabil-
ity has been successful, with multiple examples where the
inner workings of neural networks have been successfully
reverse engineered end-to-end [20, 40, 41, 49, 63]. There
have also been encouraging early successes in finding in-
terpretable circuits within real-world models [ 18, 32, 35,
44, 57], but there is already work emerging that illustrates
how neural networks can resist common “mechanistic inter-
pretability” methods [14, 34, 60].
The toy interpretability projects that have succeeded have
done so in large part because a distinct ground truth circuit
that encodes the true nature of the task or environment
emerged in the model. We build on this tradition and study
a model that has perfectly learned to multiply permutations
of five and six elements, which in mathematics is known as
the symmetric groupsS5 andS6, which are deeply studied
and well-understood objects [ 8, 10, 15]. We succeed in
completely reverse engineering the model and enumerating
the diverse circuits that it converges on to implement the
multiplication of the symmetric group. Our work does not,
however, represent an unmitigated success for the project
of mechanistic interpretability. The prior work of Chughtai
et al. [4] studied the exact same model and setting, but came
to completely different conclusions. Understanding why
our and Chughtai et al. [4]’s interpretations of the same data
diverged required extensive effort (see Appendix 7 for a
thorough comparison). We find that even in a setting as
simple and well understood as group arithmetic, it is
incredibly difficult to do interpretability research and be
confident about one’s conclusions.
Our main contributions are as follows:
• We completely reverse engineer a one-hidden layer
fully-connected network trained on the permutation
groupsS5 andS6.
• We apply a methodology inspired by Geiger et al. [17]
to use causal experiments to thoroughly test all of the
properties of our proposed circuit.
• We survey current research in mechanistic interpretabil-
1

Grokking Group Multiplication with Cosets
ity and draw connections between the difficulty of our
work and broader challenges in the field.
2. Related Work
Mechanistic Interpretability Interpreting and reverse engi-
neering the mechanism used to complete a given task is an
active field in interpretability. Analysis of such mechanisms
and circuits are discovered mainly through a top-down ap-
proach of causal mediation analysis. In the previous work
Hanna et al. [21], Meng et al. [36], Tigges et al. [54], Wang
et al. [58], the circuits are composed at the “component
level” using the feed-forward layer and attention heads. We
analyze the mechanisms of neural networks at the circuit
level of individual and small groups of neurons, drawing
directly on the work of Nanda et al. [40; 41], Olah et al.
[43], Quirke & Barez [49], Zhong et al. [64], Zhang et al.
[63]. Our work builds directly on “A Toy Model of Univer-
sality” by Chughtai et al. [4]. We recreated precisely their
experimental setup for the groups S5 andS6, though we
came to different conclusions.
Grokking The models we study exhibit “grokking”,
wherein the model first memorizes the training set and
then much later generalizes to the held out data perfectly.
Grokking was first identified by Power et al. [47] and has
been well studied for its counter-intuitive training dynamics
[31, 37, 55, 50, 62, 59]. We conducted all the analysis on
fully grokked models with perfect test accuracy, as models
that show this behavior have often formed clean generalizing
circuits that are more easily interpreted [20, 40].
Group Theory We used many of the tools of group theory
for our analysis, in particular the well-developed representa-
tion theory of the symmetric group. Tools for analyzing data
on groups are well-laid out in Clausen & Baum [5], Cohen
& Welling[6], Diaconis [8], Kondor [29], Kondor & Trivedi
[30], Huang et al. [24], Karjol et al. [27], Plumb et al. [46].
3. Mathematical Preliminaries
This paper requires a familiarity with functions on groups,
a topic that is uncommon in machine learning research. In
this section we give an overview of the major concepts as
they are realized in the permutation groups that we study.
For a more formal introduction to group theory, please refer
to Appendix D.
3.1. Permutations and the Symmetric Group
A permutation of n elements is a map σ that sends one
ordering ofn elements to a different ordering. For example
the order-reversing permutation on four elements would be:
(1 2 3 4)
σ
7→ (4 3 2 1)
Left Perm
Left 
embedding
Right 
embedding+
Fully Connected Linear Layer
Unembed
Logits
Right Perm
Relu
Figure 1. Model Architecture: we follow the model architecture
used by Chughtai et al. [4]. The one-hot vectors of left and right
permutations pass through separate embeddings. We concatenate
the embeddings and pass them through a single fully-connected
hidden layer with ReLU activations. An unembedding matrix
transforms the activations into logits.
The identity permutation, denoted e, leaves the ordering
unchanged:
(1 2 3 4)
e
7→ (1 2 3 4)
We refer to specific permutations by identifying them
with the image of their action on the elements [n] :=
{1, 2,...,n } in increasing order. For the above example
we would simply denote the order reversing permutation on
four elements as (4 3 2 1) .
We multiply two permutations onn elementsσ,τ by com-
position, read from right to left. If σ = (4 3 2 1) and
τ = (3 2 1 4) , thenστ is the permutation we obtain by first
applyingτ and then applyingσ to the output ofτ:
(1 2 3 4)
τ
7→ (3 2 1 4)
σ
7→ (4 1 2 3)
First applying τ and then σ has the same effect as just
applying the permutation (4 1 2 3) . Additionally every per-
mutationσ has an inverseσ−1 such thatσσ−1 =e. These
properties makes all of the permutations on n elements a
group called the symmetric group, which we writeSn.
There are six permutations in S4 that do not change the
position of 4:
(1 2 3 4) (2 1 3 4) (3 2 1 4)
(1 3 2 4) (3 1 2 4) (2 3 1 4)
2

Grokking Group Multiplication with Cosets
These six permutations form a subgroup of S4 because
multiplication is closed within that subset, multiplying any
two permutations that leave 4 unchanged results in another
permutation that leaves 4 unchanged. You can see that these
six permutations are isomorphic toS3 by simply “forgetting”
about the 4 that is fixed in the fourth position. In the paper,
we will refer to the subgroup ofSn isomorphic toSn−1 that
leaves elementi fixed asHi.
One of the simplest types of permutations is a “transposi-
tion,” a permutation τ ∈ Sn that switches (“transposes”)
two elementsi,j ∈ [n] and leaves the remaining elements
fixed. Every element ofSn can be decomposed into a prod-
uct of transpositions. A given decomposition of a permuta-
tion is not unique, but the number of transpositions in the
decomposition is an invariant of the permutation. For a per-
mutationg∈Sn if a set of transpositions τ1τ2...τ k =g,
then every possible such set of transpositions will also have
k elements. The permutations that have an even number of
transpositions are referred to as “even” permutations and
those with an odd number are “odd.” The set of all even per-
mutations inSn is a subgroup referred to as the “alternating
group”An.
If we takeH4 < S4 and multiply every element of on the
left by some elementσ∈S4 then we get a left coset ofH4
denotedσH4. The transpositionτ = (4 2 3 1) switches the
elements in the first and fourth positions. The elements of
τH 4 are:
(4 2 3 1) (4 1 3 2) (4 2 1 3)
(4 3 2 1) (4 1 2 3) (4 3 1 2)
This coset is characterized by every element having 4 in
the first position. Every element of H4 has 4 in the fourth
position andτ switches the first and fourth positions. For
anyh∈H4,hτ has 4 in the first position becauseτ moves
it from the fourth. We would get a coset with all of the
elements ofS4 with 4 in the third position if we multiplied
H4 on the left by the any permutation that switches three
and four.
There are also right cosets where every element in a sub-
group is multiplied from the right. The elements of H4τ
are:
(4 2 3 1) (1 4 3 1) (3 2 4 1)
(4 3 2 1) (3 4 2 1) (2 3 4 1)
This right coset is characterized by every element having 1
in the fourth position.
There are in fact four subgroupsHi <S 4 that are isomor-
phic toS3, one where each element{1,..., 4} is fixed. In
general there are at leastn subgroups ofSn that are isomor-
phic toSn−1. Any twoHi, Hj are conjugate to each other.
Conjugation by an elementσ mapsx7→σxσ−1. So if we
haveH4 and conjugate it byσ = (1 4 3 2) , thenσH4σ−1
isH2:
(1 2 3 4) (3 2 1 4) (4 2 3 1)
(1 2 4 3) (4 2 1 3) (3 2 4 1)
If a subgroup is invariant to conjugation it is a normal sub-
group. The only normal subgroup of Sn forn >4 is the
alternating groupAn of even permutations.
We will mostly refer to groups by name, but we will denote
a general group as capital G and a general subgroup as
H≤ G. For a proper subgroup ( H̸= G), we will write
H <G. For a normal subgroup, we will useN ⊴G.
3.2. Fourier Transform over Groups
Though Group Fourier Transform is not central to our pre-
sentation of the coset circuit, it was an important tool that
we used to analyze the the activations of the trained models.
It is also a critical part of [ 4]. We introduce the concepts
here and go over the the similarities and differences between
our work and [4] in Section 7.
We begin with a presentation of the Discrete Fourier Trans-
form (DFT), and then present the Group Fourier Transform
by analogy. The DFT converts a function f defined on
{0, 1,...,n − 1} to a complex-valued function via the for-
mula:
ˆf (k) =
n−1X
t=0
f (t)e−2iπkt/n, k ∈{ 0,...,n − 1}
The DFT is commonly interpreted as a conversion from the
time domain to the frequency domain because thee−2iπkt/n
terms define a complex sinusoid with frequency 2πkt/n.
The frequency domain in this case means that these frequen-
cies provide an alternative orthonormal basis from which we
can work with functions. A function on{0, 1,...,n −1} can
be represented as a vector f =
 x0 x1 ... x n−1
⊤
and its basis is given by the identity matrix In. The
DFT defines a basis transformation, much like any other.
The Fourier basis is given n vectors. The first ba-
sis vector, corresponding to k = 0 , is all ones. The
k = 1 basis vector is
 
1 e−2iπ/n ... e −2iπ(n−1)/n
,
and all of the rest for up to n− 1 are given by 
1 e−2iπk/n ... e −2iπ(n−1)k/n
.
The DFT has a particularly nice interpretation as a function
on the cyclic group Cn, which is isomorphic to addition
modulon. Please refer to Appendix D or to references such
as [8, 15, 29] for a more detailed discussion.
The interpretation of the DFT as being over the cyclic groups
can be generalized to non-commutative groups. We go
3

Grokking Group Multiplication with Cosets
over the construction in Appendix E and F. The high level
interpretation, however, is the same. For functions from
Sn→ C there is an orthonormal basis that is equivariant
to translations and convolutions. The frequencies for the
Fourier transform overSn are given by the partitions ofn.
The “highest” frequencies can be interpreted as representing
functions that are constant on permutations that all agree on
a small number of elements of [n] [12].
4. Model Architecture
As shown in Figure 1, the model we study contains separate
left and right embeddings, followed by a fully connected
linear layer with ReLU activations, and an unembedding
layer. We use the same architecture as in [ 4] to enable
consistent comparisons. 1
• One hot vectors xg with length|G|.
• Two embedding matrices, El, Er with dimensions
(d, |G|), where d is embedding dimension. Sn is
non-abelian, i.e. not commutative, and the separate
embeddings are to give the model extra capacity.
• A linear layer W with dimension (w, 2d),w denoting
the width of the linear layer. After the linear layer we
apply the ReLU pointwise nonlinearity.
• An unembedding layer U with dimension (|G|, w),
which transforms the outputs of the ReLU and linear
layer to into logit space for the group.
We also note that the firstd columns of the linear layer will
only act on the left embeddings and the secondd columns
will only act on the right embeddings, so we can analyze W
as the concatenation of two (w, d) matrices: W = [L R].
W
Elxg
Erxh

= LElxg + RErxh
Throughout the paper will refer to the values LElxg,
RErxh, and their sum as “pre-activations” to denote that
the ReLU activation function has not been applied. Post-
ReLU values we refer to as “activations.”
5. Coset Circuits
5.1. Sign Neurons Implement the Sign Circuit
The even permutations form a subgroup called the alternat-
ing group An. The two cosets of An are the group itself
and all of the odd permutations, τAn. The multiplication
1All code necessary for reproducing results and analysis is
available at https://www.github.com/dashstander/
sn-grok
Lel
-1
Odd
Left Pre-activation
1
Even
Rer
1
Odd
Right Pre-activation
-1
Even
+ +++
-2 0 0
ReLU ReLU
0 2
Activation
67% Even, 33% Odd
Activation
100% Odd
2
Figure 2. A diagram showing the four possible paths through a
single neuron (i.e. one row of REr) that implements part of a
“sign circuit.” The model stores whether a permutation is “even”
or “odd” in the embeddings, represented in the left or right pre-
activation values. The pre-activations are added together and then
the ReLU activation is applied. The neuron only fires when the
left permutation is even and the right is odd. If the neuron does not
fire, then in 1/3 cases the product is odd and 2/3 it is even.
of even and odd permutations has similar features to the
addition of even and odd integers (hence the name). The
sign map on a permutation inSn, sgn, is given by:
sgn(σ) =
(
1 σ∈An
−1 σ∈τAn
An “even” permutation that is in An is mapped to 1 and
an “odd” permutation not inAn is mapped to−1. For any
σ,ρ∈Sn, the sign of their product is the product of their
signs: sgn(σρ) = sgn(σ) sgn(ρ).
The one-layer model that we train uses this relationship to
help solve the general group multiplication. Every single
model we trained had at least two neurons dedicated to
encoding the sign of the permutation product. Though the
model cannot use the alternating group to completely solve
multiplication inSn, this sign circuit is emblematic of the
general coset circuits the model forms.
Consider the neuron shown in Fig. 2. The left pre-
activations are given byL(σ) = sgn(σ) and the right pre-
activations are R(σ) = − sgn(σ). The full action of the
neuron is given by ReLU(L(σl) + R(σr)) and there are
three cases:
1. sgn(σl) = sgn( σr)⇒ sgn(σlσr) = 1 . In this case
4

Grokking Group Multiplication with Cosets
L(σl) andR(σr) destructively interfere, cancelling out
to 0. Both the pre-activation and activation are 0.
2. sgn(σl) = −1, sgn(σr) = 1 ⇒ sgn(σlσr) = −1.
In this caseL(σl) andR(σr) reinforce each other and
sum to a positive value. Since 2 > 0, the activation
value is 2.
3. sgn(σl) = 1 , sgn(σr) = −1⇒ sgn(σlσr) = −1.
Like in (2) the productσlσr is an odd permutation and
L(σl) andR(σr) constructively interfere, though this
timeL(σl) +R(σr) =−2, which is less than 0. Thus
ReLU clips the pre-activation and sends it to 0.
5.2. Conjugate Subgroup Circuit
All four ways to multiply two cosets ofAn are well-defined.
For each of the four options (even-even, odd-even, etc...)
we know which coset of An the product will be in, but
no other subgroup of Sn has this property. The model
instead learns to use sets of conjugate subgroups. Recall
thatHi <S n is the subgroup isomorphic toSn−1 that fixes
the elementi∈ [n] in theith place andτij is the permutation
that swaps i and j. Any two Hi and Hj are conjugate
to each other, τijHiτij = Hj and τijHjτij = Hi. This
means that there are two shared cosets betweenHi andHj,
becauseHiτij = τijHj andHjτij = τijHi. The model
implements the full group multiplication by picking out
the shared cosets of conjugate subgroups.
As an example, consider a neuron that corresponds to H1
for the left permutation and H5 for the right permutation.
The shared coset is H1τ15 =τ15H5, the set of all σ∈S5
withσ(1) = 5 . The pre-activations for the left and right
permutations will be:
L(σ) =



4 σ∈H1
2 σ∈H1τ12
0 σ∈H1τ13
−2 σ∈H1τ14
−4 σ∈H1τ15
R(σ) =



−4 σ∈τ15H5
−2 σ∈τ25H5
0 σ∈τ35H5
2 σ∈τ45H5
4 σ∈H5
(1)
The final activation is still ReLU(L(σl) +R(σr)), but now
there are twenty-five possible pairs of cosets. All twenty-
five combinations can be boiled down to two meaningful
cases:
1. IfL(σl) +R(σr) = 0 , thenσlσr is in the shared coset
H1τ15.
2. IfL(σl) +R(σr)̸= 0, thenσlσr is not in the shared
cosetH1τ15.
Each left cosetyH5 has a paired right cosetH1x such that
H1xyH5 = H1τ15 = τ15H5. The discrete values that L
andR can take are precisely tuned so that those pairs of left
and right cosets cancel out. Just like with the sign neuron,
information about the pre-activation being negative is lost
with the ReLU. This lost information has to be made up
with extra neurons that correspond to (H1,H 5) and assign
different values to the cosets. For example, a different
neuron that uses −L(σl)− R(σr) will fail to fire for a
different set of permutations. The combination
ReLU(L(σl) +R(σr)) + ReLU(−L(σl)−R(σr))
will be much closer to a perfect on/off switch for coset
membership.
5.3. Decoding Permutations with Coset Membership
There are n2 combinations of (Hi,Hj) subgroups. Each
pair can be interpreted directly as encoding the set of per-
mutations withi in thejth position. Because of the way the
coset neurons function, each neuron is better understood as
firing when the value in the jth position is certainly noti.
Then2 combinations of (Hi,Hj) uniquely identify each ele-
ment ofSn. We can use the outputs of twenty-five (Hi,Hj)
neurons as a code that uniquely encodes each element ofS5.
By analyzing the unembedding layer to see how the model
makes use of (Hi,Hj) neurons, we see that this is almost
exactly what the model does. This same construction works
for every subgroup ofSn except forAn.
6. The Process of Reverse Engineering
6.1. Identifying Coset Circuits
The first step in attempting to reverse engineer the mecha-
nisms of a neural network is to spend some time staring at
the weights and activations. Even a small one-layer model
such as ours is too large to visualize all at once. It was not
until we looked closely at the pre-ReLU activations that we
produced a histogram similar to Figure 3. The left and right
pre-activations of one neuron were nearly constant on the
distinct cosets of the Frobenius group of order 20 (F20), one
of the subgroups ofS5. 2 Further investigation revealed that
almost every neuron had this property of only producing a
discrete number of values that corresponded directly to the
cosets of one of the subgroups ofS5 orS6. For a function
f :G→ R, we defineCH (f ) to be the degree to whichf
concentrates on the cosetsH≤G:
CH (f ) :=
P
gH Var[f|gH ]
Var[f ]
Where Var[f|gH ] is the variance off when the domain is
2F20 is equivalent to the group of affine transformations x7→
ax + b, where a, b, x are in the field with five elements and a̸= 0.
5

Grokking Group Multiplication with Cosets
3
 0 3 6
0
5
10
15
20# of Permutations
100,000 Steps
Coset
F20
F20(12354)
F20(12435)
F20(12453)
F20(12534)
F20(12543)
3
 0 3 6
110,000 Steps
3
 0 3 6
120,000 Steps
3
 0 3 6
Pre-Activation Value
130,000 Steps
Figure 3. An illustration of the phenomenon of “concentration on cosets,” depicting the 115th neuron from seed 11. We show the evolution
of the left pre-activations (the pre-ReLU outputs of a layer) of training on anF20 neuron from 100k to 130k steps. The seed of the neuron’s
functionality is already present at 100k steps, where it fires very strongly and negatively for permutations in the coset F20(1 2 3 5 4) , but
it takes time for the action of the neuron to “clean up” on the other cosets of F20. The distribution found at 130k steps does not change
very much afterwards. Noticing this common pattern of neurons taking on these discrete values was a striking piece of evidence that
required further investigation.
restricted to the cosetgH. IntuitivelyCH (f ) calculates the
degree to which restricting to the cosets of H reduces the
variance off. IfCH (f )< 1 it implies that the activations
f can meaningfully be understood better by looking at the
values that it takes on the cosets of some subgroup. Recall
that a single neuron is a function Ni : Sn×Sn→ R is
the sum of two functionsG→ R, one for the left and right
permutations, respectively. We can calculate minCH for
each. Take as an exampleNl
115, the neuron shown in Figure
3. At 100,000 steps (on the far left) Var[Nl
115] = 5 .23.
Its activations are not concentrated on the specific cosets
of F20, however, and CF20 (Nl
115) = 2 .96. At 130,000
steps (on the far right) Var[Nl
115] has increased to 9.06, but
CF20 (Nl
115)< 10−5. The distribution within each coset of
F20 has close to zero variance.
We see a typical example of what this looks like for the
entire model in Fig. 4. As the validation loss approaches a
small value, there is a rapid transition from the median coset
concentration being approximately 1, to a minuscule value.
Even if it is apparent that a neuron is taking on discrete
values and is a good candidate for being a coset neuron,
it is difficult to tell by sight which subgroup the neuron is
activating for.S5 andS6 only have 156 and 1,455 subgroups,
respectively, 3 so it is tractable to do an exhaustive search
and calculate
argminH∈Sub(G)CH (f )
the subgroup that minimizes the variance of f for ev-
ery neuron in the model. Running these calculations
shows that for the 128 S5 models and 100 S6 models we
3Sequence A005432 OEIS [42]
trained over 99.2% of the neurons in the linear layer had
minH∈Sub(G)CH (f )< 1.0, and the vast majority of those
were less than 10−6.
With the ability to calculate directly which neurons corre-
sponded to which subgroup, our theories for exactly what
the neurons were representing fell into place. The next step
was to confirm that these neurons were actually responsible
for the models’ performance.
6.2. Ablations
We have described how coset neurons function and how
they can be identified. We will now show via ablations
that coset neurons are not solely sufficient but also neces-
sary to implement multiplication inSn. We conduct abla-
tions by removing neurons which have a coset concentration
minH∈Sub(G)CH (Ni) above a threshold.
If coset circuits are in fact responsible for the performance
of our models, then we expect to see no change in the ac-
curacy when the neurons that have not converged onto the
cosets of a subgroup are removed from the model. This
is precisely what we see on the far right of Figure 5. Of
the 128 S5 models that we trained, 126 models saw no
change in the accuracy when we removed the neurons with
minH∈Sub(G)CH (Ni)≥ 1 (the far right of Figure 5). Re-
call that if CH (Ni)≥ 1, restricting to the cosets of H at
best does not change the variance off. Of the two models
that did show a decrease in accuracy, they decreased to 99%
and 98%.
We see more between-run variation when we remove more
neurons. The median model has 24 out of 128 neurons
with minCH (Ni)≥ 10−5, but the 50th and 25th percentile
6

Grokking Group Multiplication with Cosets
0 50 100 150 200 250
# of Epochs (thousands)
0
0.5
1
1.5
2
Coset Concentration
0 50 100 150 200 250
# of Epochs (thousands)
0
10
20
30
40Validation Loss
Figure 4. The paired evolution of the the validation loss and minH∈Sub(H) CH, which encodes the formation of coset circuits. Displayed
is the S5 model with random seed 1. Different runs will form coset circuits at different times in training, but the effect is representative.
0%
25%
50%
75%
100%Post-Ablation Accuracy
Remove minCH < x
1e-081e-071e-061e-050.00010.001
0.1 0.5 1.0
Coset Concentration Threshold
0%
25%
50%
75%
100%
Remove minCH > x
Figure 5. We perform ablations by re-calculating the accuracy after
removing any neuronsNi that have minH∈Sub(G) CH (Ni) greater
than (top figure) or less than (bottom figure) the thresholds on the
x-axis.
accuracy is still 100%. It is not until we set the threshold
to 10−6 that the 25th percentile moves at all. When we set
the threshold at 10−7 the performance for many models
has collapsed, but the median model has had 42 neurons
removed and the median accuracy is still 100%. Recall also
that the neuron shown in the far right of Figure 3 has a coset
concentration of 10−5.
The overwhelming majority of neurons are identifiable as
coset neurons. Of those neurons, those with the very highest
concentration on cosets account for the largest portion of
each model’s performance.
6.3. Causal Interventions
To rigorously test the properties of the coset circuit, we care-
fully designed causal experiments to test specific properties
of in the circuits. We observe a circuit’s behavior over the
entire data distribution (the full groupSn) and we see that
our model of the circuit is consistent with the behavior of
the true circuit. To confirm that our model of the circuit is
correct, however, we need to “break” the circuit in targeted
ways and test that it behaves in the way we predict. Neural
circuits are complex enough that observational evidence is
not enough. We aggregated runs over 128 S5 models of
different and recorded their average loss and accuracy. Ini-
tially, over the initial models without intervention, we have
accuracy extremely close to 1.
Embedding Exchange The left and right embeddings en-
code different information—membership in right and left
cosets, respectively—and cannot be interchanged. To test
this we intervene to switch the left and right embeddings.
After the intervention, we observed a significant drop in
accuracy to 0 and a rise in loss. This aligns with our ex-
pectation that the membership is an important property that
can’t be switched.
Switch Permutation Sign The pre-activations are sym-
metric about the origin and the sign of the pre-activations
does not matter, only whether or not the pre-activations is
equal to zero. The relative sign of the left and right pre-
activations should matter a lot. To test this, we have three
tests: changing the sign of just the left embeddings, just the
right embeddings, and both embeddings. In the case where
we change both the sign and with commutative property, we
can still expect the left and right activation to cancel out.
Therefore, we should see a near-perfect accuracy and near-0
loss. The result is as expected. When we change the sign
of only the left or right embedding, such cancellation law
doesn’t hold anymore. Therefore, we observe a 0 accuracy
in both cases.
Absolute Value Non-linearity The circuit can create a
perfect 0-1 coset membership switch with multiple neurons
on constructive interference, but every single neuron is noisy
and fundamentally limited by the ReLu non-linearity. To
7

Grokking Group Multiplication with Cosets
Table 1. Causal interventions aggregated over 128 runs on S5 with different sizes
Intervention Mean Accuracy Mean Loss
Base Model 99.99% 1.97e-6
Embedding Swap 1% 4.76
Switch Left and Right Sign 100% 1.97e-6
Switch Left Permutation Sign 0% 22.39
Switch Right Permutation Sign 0% 22.36
PerturbN (0, 0.1) 99.99% 2.96e-6
PerturbN (0, 1) 97.8% 0.0017
Absolute Value Non-Linearity 100% 3.69e-13
PerturbN (1, 1) 88% 0.029
PerturbN (−1, 1) 98% 0.0021
test this, we replace the ReLU activation function with the
absolute value function x7→| x|. We observe perfect ac-
curacy and an even lower loss that a half of the original
loss.
Distribution Change It is essential to the functioning of
each neuron that a large proportion of the pre-activations
are close to zero. To test this we compare how adding noise
from aN (−1, 1) andN (1, 1) affect the performance of the
model. We can see that changing the distribution of the
activation in PerturbN (−1, 1) changes the performance
less significantly thanN (1, 1). This indicates that the coset
requires 0 as a threshold value to decide the membership.
The results of these interventions can be viewed in Table 1
7. The Group Composition via
Representations Algorithm
Our experimental setup is identical to that of Chughtai
et al. [4], but our analysis led us to a different conclu-
sion.Chughtai et al. [4] proposed the “Group Composition
via Representations” (GCR) algorithm. They show that,
given an irrepρ ofSn, argmaxc∈Sn tr[ρ(a)ρ(b)ρ(−1c)] =
ab and propose that this is the algorithm the model is imple-
menting. This requires that not only store the matrix irreps,
but that the model perform the matrix multiplication within
its mechanism. We find that most of the evidence [ 4] put
forward is also consistent with coset circuits. The other evi-
dence we were not able to independently replicate. We also
find evidence that, to our understanding, is not consistent
with the GCR algorithm but is explained by coset circuits.
7.1. Our Interpretation of the Evidence for GCR
Chughtai et al. [4] put forward four main pieces of evidence,
which we restate here for clarity: (1) Correlation between
the model’s logits and characters of a learned representation
ρ. (2) The embedding and unembedding layers function
as a “lookup table” for the representations of the input ele-
mentsρ(a), ρ(b) and the inverse of the targetρ(c−1). (3)
The neurons in the linear layer calculate the matrix product
ρ(a)ρ(b) = ρ(ab). (4) Ablations showing that the circuit
they identify is responsible for the majority of the model’s
performance. Many of these points are equally consistent
with the coset circuit and the other we could not find evi-
dence for.
Ablations Though we do not perform all of the exact ab-
lations that Chughtai et al. [4] perform, we also find that
the weights that show high Fourier concentration and per-
form the coset multiplication are integral to the model’s
performance, see Section 6.2.
Irrep Look Up Table We were not able to find any evi-
dence that the embedding or unembedding layers function
as a look-up table for any representation except for the
one-dimensional sign representation. We did find that the
model’s weights and activations concentrate on specific
irreps in the group Fourier basis. This is due, however,
to concentration on cosets of specific subgroups, not be-
cause the matrix representations are realized anywhere in
the weights. The relationship between functions that are
constant on cosets and specific irreps is shown in Appendix
G.2.
Logit Attribution The trace of a group representation is re-
ferred to as the “character” and often denotedχ. We find that
the model’s logits correlate with the character χρ(abc−1)
when the irrep ρ appears in the Fourier transform of the
model’s weights. This is not, however, because the model
has implemented the matrix product ρ(ab)ρ(c−1), but be-
cause the model is “counting” the number of cosets that
ab and c are both in. We prove in G.2, if the cosets are
of conjugate subgroups that have their Fourier transform
concentrated on the irrepρ (as we observe for the models
in question), then the number of shared cosets will also
correlate with the characters ofρ.
Matrix Multiplication of Irreps We were not able to find
8

Grokking Group Multiplication with Cosets
any evidence that the linear layer implements matrix multi-
plication, again excluding scalar multiplication of the sign
irrep.
7.2. Evidence GCR Does Not Explain
Concentration on Cosets In the standard basis the pre-
activations of the overwhelming majority of neurons con-
centrate heavily on the cosets of subgroups. This is behavior
is not predicted by the GCR algorithm.
The Difference Between Subgroups and Irreps The GCR
algorithm and coset circuit cannot be equivalent because
there is not, in fact, a one-to-one relationship between cosets
and irreps. Most subgroups ofSn have their Fourier trans-
forms concentrate on more than a single group (see Table
5 for the spectral properties of all of the subgroups ofS5),
indeed this needs to be the case as there are many more
subgroups than irreps. Please refer to Table 4 for a concrete
comparison and Appendix 7.2 for an asymptotic analysis.
We also observe coset circuits for some subgroups such as
D104 will have coset circuits concentrated on both (3, 2) or
(2, 2, 1), depending on the run. The GCR algorithm would
treat these as different circuits, though their behavior is in
fact identical.
Unembedding Correlations of Neurons We observe that
the correlation between in the unembedding of neurons
that concentrate on the same coset is on average 81.4% (see
Table 3). The correlation between neurons concentrated only
on the same conjugacy class of subgroup (e.g.H1 andH2)
is on average−0.2%. The neurons that represent subgroups
in the same conjugacy class will oftentimes, though not
always, be concentrated on the same irrep. The model is
treating cosets together but the irreps and conjugacy classes
separately.
Coset Circuit Specific Causal Interventions The property
that the loss goes down when we replace the ReLU activa-
tion function with absolute value is a very strange property
that GCR does not predict.
The concentration of the model’s activations on irreps ofSn
is striking evidence and the GCR algorithm that [4] detail
could indeed solve the problem of group multiplication. The
coset circuit is also consistent with all of the evidence that
[4] provide and is additionally consistent with evidence that
the GCR algorithm does not explain.
8. Discussion and Conclusion
We performed a circuit level analysis to discover the con-
crete mechanism a one layer fully connected network uses
to solve group multiplication inS5 andS6. We showed that
4The dihedral group of order 10, the symmetry group of a
pentagon.
the model decomposes S5 andS6 into its cosets and uses
this structural information to perfectly implement the task.
Though our work concerns a toy problem, we highlight
a core takeaway that applies broadly to the field of inter-
pretability: we must treat proposed neural mechanisms as
theories until they have been thoroughly tested.
When we identify what we believe to be a circuit within
a larger network found via techniques such as [ 7, 19], we
have taken the first step towards mechanistically understand-
ing how a model performs a task. The evidence we have
for the circuit’s role in that task is, however, fundamentally
observational and correlational. The nodes in the circuit’s
computation graph are causally connected, but the relation-
ship between the action of those nodes is only observed to
be correlated to a certain task with respect to a distribution.
This is valuable information to have, but the understanding
that it imparts is limited and must be recognized as such.
When beginning this project we quickly noticed that the
activations of sub-circuits of our model were concentrated
on specific irreps ofSn. It was only with additional investi-
gation that we were able to attach semantic meaning to this
phenomenon. We observed that the neurons concentrated on
a single irrep were activating for specific subgroups. The hy-
pothesis of the coset circuits had formed, but it was still only
a theory. The facts we had observed were incontrovertible,
but their reason was unclear. It was only after performing
the causal experiments detailed in Section 6.3 that we
became confident we understood the mechanism. The
simple reality is that more than one theory can be consis-
tent with observational data, especially when that data only
comes from a small subset of the full distribution. There is
a long history of scholarship showing that interpretability
techniques, including state-of-the-art, can give be mislead-
ing and contradictory results [1, 2, 3, 9, 14, 23, 25, 34, 35].
In doing this work we had many advantages not available
when interpreting real-world models: access to the entire
distribution, an orthonormal basis for the function space of
the network, and a relatively small model. The task of mul-
tiplication inSn is deterministic and very well studied, we
had many mathematical tools to bring to bear in analyzing
the model. Even still, this project was quite challenging and
the circuits we found surprised us. Interpreting real models
will be even difficult. We encourage future work to apply
interpretability tools cautiously and validate observational
results with rigorous experimental tests.
Impact Statement
This paper presents work whose goal is to make the function
and mechanisms of deep neural networks interpretable to
humans. We present methods for reasoning about counter-
factual and out of distribution behavior in the models that
9

Grokking Group Multiplication with Cosets
we train. Though our setting is too small to be directly
relevant to real-world use cases, we hope that similar tech-
niques will be able to test, audit, and monitor deep neural
networks that have been deployed in the real world. We
also present results that urge caution and humility when
attempting to interpret neural networks. We believe that
robust and effective interpretability techniques may miti-
gate some societal harms that could arise from the use of
deep neural networks, but that mistakenly trusting illusory
interpretability techniques could be disastrous.
Acknowledgements
We would like to thank Coreweave for donating the comput-
ing resources that we used to run all of our experiments, to
Bilal Chughtai for helpful discussions we had throughout the
project, and to Neel Nanda for telling us to “not hold back
for fear of offending [him].” We would also like to thank
Nora Belrose, Neils uit de Bos, Aidan Ewart, Sara Price,
Hailey Schoelkopf, C´edric Simal, and Benjamin Wright for
their helpful feedback on earlier drafts of this paper.
References
[1] Adebayo, J., Gilmer, J., Muelly, M., Goodfellow, I.,
Hardt, M., and Kim, B. Sanity checks for saliency
maps, 2020.
[2] Bolukbasi, T., Pearce, A., Yuan, A., Coenen, A., Reif,
E., Vi´egas, F., and Wattenberg, M. An interpretability
illusion for bert, 2021.
[3] Casper, S., Li, Y ., Li, J., Bu, T., Zhang, K., Hariharan,
K., and Hadfield-Menell, D. Red teaming deep neural
networks with feature synthesis tools, 2023.
[4] Chughtai, B., Chan, L., and Nanda, N. A
Toy Model of Universality: Reverse Engineering
How Networks Learn Group Operations. Tech-
nical Report arXiv:2302.03025, arXiv, May 2023.
URL http://arxiv.org/abs/2302.03025.
arXiv:2302.03025 [cs, math] type: article.
[5] Clausen, M. and Baum, U. Fast Fourier Trans-
forms for Symmetric Groups: Theory and Imple-
mentation. Mathematics of Computation , 61(204):
833–847, 1993. ISSN 0025-5718. doi: 10.2307/
2153256. URL https://www.jstor.org/
stable/2153256. Publisher: American Mathe-
matical Society.
[6] Cohen, T. and Welling, M. Group Equivari-
ant Convolutional Networks. In Proceedings
of The 33rd International Conference on Ma-
chine Learning , pp. 2990–2999. PMLR, June
2016. URL https://proceedings.mlr.
press/v48/cohenc16.html. ISSN: 1938-
7228.
[7] Conmy, A., Mavor-Parker, A. N., Lynch, A., Heimer-
sheim, S., and Garriga-Alonso, A. Towards Auto-
mated Circuit Discovery for Mechanistic Interpretabil-
ity, October 2023. URL http://arxiv.org/
abs/2304.14997. arXiv:2304.14997 [cs].
[8] Diaconis, P. Group Representations in Probability
and Statistics, volume 11 of Institute of Mathemati-
cal Statistics Lecture Notes. Insitute of Mathematical
Statistics, Hayward, CA, 1988. ISBN 0-940600-14-5.
[9] Doshi-Velez, F. and Kim, B. Towards a rigorous sci-
ence of interpretable machine learning, 2017.
[10] Dummit, D. S. and Foote, R. M. Abstract Algebra.
Wiley, 3rd edition, July 2003. ISBN 978-0-471-43334-
7.
[11] Elias M. Stein, R. S. Fourier analysis: an introduction.
Princeton lectures in analysis 1. Princeton University
Press, 2003. ISBN 069111384X,9780691113845.
[12] Ellis, D., Friedgut, E., and Pilpel, H. Intersecting
Families of Permutations, July 2017. URL http://
arxiv.org/abs/1011.3342. arXiv:1011.3342
[math].
[13] Erdos, P. On an elementary proof of some asymptotic
formulas in the theory of partitions. Annals of Mathe-
matics, 43(3):437–450, 1942. ISSN 0003486X. URL
http://www.jstor.org/stable/1968802.
[14] Friedman, D., Lampinen, A., Dixon, L., Chen, D., and
Ghandeharioun, A. Interpretability illusions in the
generalization of simplified models, 2023.
[15] Fulton, W. and Harris, Joe. Representation Theory.
Graduate Texts in Mathematics. Springer, New York,
NY , October 1991. ISBN 978-0-387-97495-8.
[16] GAP. Gap – groups, algorithms, and program-
ming, version 4.12.2, 2023. URL https://www.
gap-system.org.
[17] Geiger, A., Potts, C., and Icard, T. Causal abstraction
for faithful model interpretation, 2023.
[18] Geva, M., Schuster, R., Berant, J., and Levy, O. Trans-
former feed-forward layers are key-value memories,
2021.
[19] Goldowsky-Dill, N., MacLeod, C., Sato, L., and Arora,
A. Localizing model behavior with path patching,
2023.
10

Grokking Group Multiplication with Cosets
[20] Gromov, A. Grokking modular arithmetic, January
2023. URL http://arxiv.org/abs/2301.
02679. arXiv:2301.02679 [cond-mat].
[21] Hanna, M., Liu, O., and Variengien, A. How does
GPT-2 compute greater-than?: Interpreting mathemat-
ical abilities in a pre-trained language model, Novem-
ber 2023. URL http://arxiv.org/abs/2305.
00586. arXiv:2305.00586 [cs].
[22] Harris, C. R., Millman, K. J., van der Walt, S. J.,
Gommers, R., Virtanen, P., Cournapeau, D., Wieser,
E., Taylor, J., Berg, S., Smith, N. J., Kern, R., Pi-
cus, M., Hoyer, S., van Kerkwijk, M. H., Brett,
M., Haldane, A., del R ´ıo, J. F., Wiebe, M., Peter-
son, P., G ´erard-Marchant, P., Sheppard, K., Reddy,
T., Weckesser, W., Abbasi, H., Gohlke, C., and
Oliphant, T. E. Array programming with NumPy.
Nature, 585(7825):357–362, September 2020. doi:
10.1038/s41586-020-2649-2. URL https://doi.
org/10.1038/s41586-020-2649-2 .
[23] Hase, P., Bansal, M., Kim, B., and Ghandeharioun,
A. Does localization inform editing? surprising dif-
ferences in causality-based localization vs. knowledge
editing in language models, 2023.
[24] Huang, J., Guestrin, C., and Guibas, L. Fourier Theo-
retic Probabilistic Inference over Permutations. Jour-
nal of Machine Learning Research, 10(37):997–1070,
2009. ISSN 1533-7928. URL http://jmlr.org/
papers/v10/huang09a.html.
[25] Jain, S. and Wallace, B. C. Attention is not
explanation. In North American Chapter of the
Association for Computational Linguistics , 2019.
URL https://api.semanticscholar.org/
CorpusID:67855860.
[26] Janusz, G. and Rotman, J. Outer automorphisms of
S6. The American Mathematical Monthly, 89(6):407–
410, 1982. ISSN 00029890, 19300972. URL http:
//www.jstor.org/stable/2321657.
[27] Karjol, P., Kashyap, R., and Ap, P. Neural Dis-
covery of Permutation Subgroups. In Proceedings
of The 26th International Conference on Artificial
Intelligence and Statistics , pp. 4668–4678. PMLR,
April 2023. URL https://proceedings.mlr.
press/v206/karjol23a.html. ISSN: 2640-
3498.
[28] Kingma, D. P. and Ba, J. Adam: A method for
stochastic optimization. CoRR, abs/1412.6980, 2014.
URL https://api.semanticscholar.org/
CorpusID:6628106.
[29] Kondor, R. Group theoretical methods in machine
learning. PhD thesis, Columbia University, New
York, NY , 2008. URL https://dl.acm.org/
doi/abs/10.5555/1570977. Archive Location:
world.
[30] Kondor, R. and Trivedi, S. On the General-
ization of Equivariance and Convolution in Neu-
ral Networks to the Action of Compact Groups.
In Proceedings of the 35th International Confer-
ence on Machine Learning , pp. 2747–2755. PMLR,
July 2018. URL https://proceedings.mlr.
press/v80/kondor18a.html. ISSN: 2640-
3498.
[31] Kumar, T., Bordelon, B., Gershman, S. J., and
Pehlevan, C. Grokking as the Transition from
Lazy to Rich Training Dynamics, October 2023.
URL http://arxiv.org/abs/2310.06110.
arXiv:2310.06110 [cond-mat, stat].
[32] Lieberum, T., Rahtz, M., Kram´ar, J., Nanda, N., Irving,
G., Shah, R., and Mikulik, V . Does circuit analysis
interpretability scale? evidence from multiple choice
capabilities in chinchilla, 2023.
[33] Lundberg, S. and Lee, S.-I. A unified approach to
interpreting model predictions, 2017.
[34] Makelov, A., Lange, G., and Nanda, N. Is this the sub-
space you are looking for? an interpretability illusion
for subspace activation patching, 2023.
[35] McGrath, T., Rahtz, M., Kramar, J., Mikulik, V ., and
Legg, S. The hydra effect: Emergent self-repair in
language model computations, 2023.
[36] Meng, K., Bau, D., Andonian, A., and Belinkov, Y .
Locating and editing factual associations in gpt, 2023.
[37] Merrill, W., Tsilivis, N., and Shukla, A. A
Tale of Two Circuits: Grokking as Competition
of Sparse and Dense Subnetworks, March 2023.
URL http://arxiv.org/abs/2303.11873.
arXiv:2303.11873 [cs].
[38] Morwani, D., Edelman, B. L., Oncescu, C.-A., Zhao,
R., and Kakade, S. Feature emergence via margin
maximization: case studies in algebraic tasks, 2024.
[39] Nanda, N. and Bloom, J. Transformerlens.
https://github.com/neelnanda-io/
TransformerLens, 2022.
[40] Nanda, N., Chan, L., Lieberum, T., Smith,
J., and Steinhardt, J. Progress measures for
grokking via mechanistic interpretability. Techni-
cal Report arXiv:2301.05217, arXiv, January 2023.
11

Grokking Group Multiplication with Cosets
URL http://arxiv.org/abs/2301.05217.
arXiv:2301.05217 [cs] type: article.
[41] Nanda, N., Lee, A., and Wattenberg, M. Emer-
gent Linear Representations in World Models of
Self-Supervised Sequence Models, September 2023.
URL http://arxiv.org/abs/2309.00941.
arXiv:2309.00941 [cs].
[42] OEIS Foundation Inc. The On-Line Encyclopedia of
Integer Sequences, 2023. Published electronically at
http://oeis.org.
[43] Olah, C., Cammarata, N., Schubert, L., Goh, G.,
Petrov, M., and Carter, S. Zoom In: An In-
troduction to Circuits. Distill, 5(3):e00024.001,
March 2020. ISSN 2476-0757. doi: 10.23915/
distill.00024.001. URL https://distill.pub/
2020/circuits/zoom-in.
[44] Olsson, C., Elhage, N., Nanda, N., Joseph, N., Das-
Sarma, N., Henighan, T., Mann, B., Askell, A., Bai, Y .,
Chen, A., Conerly, T., Drain, D., Ganguli, D., Hatfield-
Dodds, Z., Hernandez, D., Johnston, S., Jones, A.,
Kernion, J., Lovitt, L., Ndousse, K., Amodei, D.,
Brown, T., Clark, J., Kaplan, J., McCandlish, S., and
Olah, C. In-context Learning and Induction Heads,
September 2022. URL https://arxiv.org/
abs/2209.11895v1.
[45] Paszke, A., Gross, S., Massa, F., Lerer, A., Bradbury,
J., Chanan, G., Killeen, T., Lin, Z., Gimelshein, N.,
Antiga, L., Desmaison, A., K ¨opf, A., Yang, E., De-
Vito, Z., Raison, M., Tejani, A., Chilamkurthy, S.,
Steiner, B., Fang, L., Bai, J., and Chintala, S. PyTorch:
An Imperative Style, High-Performance Deep Learn-
ing Library, December 2019. URL http://arxiv.
org/abs/1912.01703. arXiv:1912.01703 [cs,
stat].
[46] Plumb, G., Pachauri, D., Kondor, R., and Singh, V .
SnFFT: A Julia Toolkit for Fourier Analysis of Func-
tions over Permutations. Journal of Machine Learning
Research, 16(107):3469–3473, 2015. URL http:
//jmlr.org/papers/v16/plumb15a.html.
[47] Power, A., Burda, Y ., Edwards, H., Babuschkin, I.,
and Misra, V . Grokking: Generalization Beyond
Overfitting on Small Algorithmic Datasets, January
2022. URL http://arxiv.org/abs/2201.
02177. arXiv:2201.02177 [cs].
[48] Pyber, L. Enumerating finite groups of given or-
der. Annals of Mathematics, 137(1):203–220, 1993.
ISSN 0003486X. URL http://www.jstor.
org/stable/2946623.
[49] Quirke, P. and Barez, F. Understanding addition in
transformers, 2024.
[50] Rubin, N., Seroussi, I., and Ringel, Z. Droplets
of Good Representations: Grokking as a First Or-
der Phase Transition in Two Layer Networks, Octo-
ber 2023. URL http://arxiv.org/abs/2310.
03789. arXiv:2310.03789 [cond-mat, stat].
[51] Shrikumar, A., Greenside, P., Shcherbina, A., and Kun-
daje, A. Not just a black box: Learning important
features through propagating activation differences,
2017.
[52] Simonyan, K., Vedaldi, A., and Zisserman, A. Deep
inside convolutional networks: Visualising image clas-
sification models and saliency maps, 2014.
[53] Stein, W. et al. Sage Mathematics Software (Version
10.0.0). The Sage Development Team, 2023. URL
http://www.sagemath.org.
[54] Tigges, C., Hollinsworth, O. J., Geiger, A., and Nanda,
N. Linear representations of sentiment in large lan-
guage models, 2023.
[55] Varma, V ., Shah, R., Kenton, Z., Kram ´ar, J., and
Kumar, R. Explaining grokking through circuit ef-
ficiency, September 2023. URL http://arxiv.
org/abs/2309.02390. arXiv:2309.02390 [cs].
[56] Vink, R., Gooijer, S. d., Beedie, A., Gorelli, M. E.,
Zundert, J. v., Hulselmans, G., Grinstead, C., Santa-
maria, M., Guo, W., Heres, D., Magarick, J., Mar-
shall, ibENPC, Peters, O., Leitao, J., Wilksch, M.,
Heerden, M. v., Borchert, O., Jermain, C., Haag, J.,
Peek, J., Russell, R., Pryer, C., Castellanos, A. G.,
Goh, J., illumination-k, Brannigan, L., Conradt, M.,
and Robert. pola-rs/polars: Python Polars 0.19.0, Au-
gust 2023. URL https://doi.org/10.5281/
zenodo.8301818.
[57] Wang, K., Variengien, A., Conmy, A., Shlegeris,
B., and Steinhardt, J. Interpretability in the Wild:
a Circuit for Indirect Object Identification in GPT-
2 small, November 2022. URL http://arxiv.
org/abs/2211.00593. arXiv:2211.00593 [cs].
[58] Wang, K., Variengien, A., Conmy, A., Shlegeris, B.,
and Steinhardt, J. Interpretability in the wild: a circuit
for indirect object identification in gpt-2 small, 2022.
[59] Wei, J., Tay, Y ., Bommasani, R., Raffel, C., Zoph, B.,
Borgeaud, S., Yogatama, D., Bosma, M., Zhou, D.,
Metzler, D., Chi, E. H., Hashimoto, T., Vinyals, O.,
Liang, P., Dean, J., and Fedus, W. Emergent abilities
of large language models, 2022.
12

Grokking Group Multiplication with Cosets
[60] Wen, K., Li, Y ., Liu, B., and Risteski, A. Transform-
ers are uninterpretable with myopic methods: a case
study with bounded dyck grammars. In Thirty-seventh
Conference on Neural Information Processing Sys-
tems, 2023. URL https://openreview.net/
forum?id=OitmaxSAUu.
[61] Wold, S., Esbensen, K., and Geladi, P. Principal com-
ponent analysis. Chemometrics and Intelligent Labo-
ratory Systems, 2(1-3):37–52, 1987.
[62] Xu, Z., Wang, Y ., Frei, S., Vardi, G., and Hu,
W. Benign Overfitting and Grokking in ReLU
Networks for XOR Cluster Data, October 2023.
URL http://arxiv.org/abs/2310.02541.
arXiv:2310.02541 [cs, stat].
[63] Zhang, S. D., Tigges, C., Biderman, S., Ra-
ginsky, M., and Ringer, T. Can Transformers
Learn to Solve Problems Recursively?, June 2023.
URL http://arxiv.org/abs/2305.14699.
arXiv:2305.14699 [cs].
[64] Zhong, Z., Liu, Z., Tegmark, M., and Andreas, J.
The Clock and the Pizza: Two Stories in Mecha-
nistic Explanation of Neural Networks, June 2023.
URL http://arxiv.org/abs/2306.17844.
arXiv:2306.17844 [cs].
13

Grokking Group Multiplication with Cosets
A. Author Contributions
Dashiell Wrote the code for training and for calculating the Group Fourier Transform over Sn. Performed the initial
analyses of models trained on S5 and initially found what we came to call the coset circuit. Designed and ran causal
experiments to confirm our understanding of the coset circuit. Derived formal properties of the coset circuit. Participated in
discussions throughout the project and in writing the paper.
Qinan Ran training jobs and performed the bulk of circuit analysis on S6, designed and ran ablation experiments and
causal interchange interventions, participated in discussions throughout the project and the writing of the paper.
Honglu Derived formal properties of the coset circuit, participated in the discussions throughout the project, and the
writing of the paper.
Stella Helped scope the problem and identify and plan the core experiments. Advised on the interpretation of the analysis
and the writing of the paper.
B. Structure of the Appendix
In the Appendix we provide more of the mathematical background needed to fully describe some of our results and
techniques. In particular, we explain the Group Fourier Transform and how we used to to analyze our models. We do this
because we believe it is of independent interest and also because it is necessary to fully explain where our results and those
of Chughtai et al. [4] diverge.
In Appendix C we go over the precise experimental set up of the models that we trained.
In Appendix D we introduce the necessary concepts from group theory needed to rigorously talk about the more mathematical
aspects of our results.
In Appendix E we introduce representation theory, representations of the symmetric group, and the group Fourier transform.
In Appendix G we return to the coset circuit and coset neurons, with the presentation grounded in the mathematical concepts
introduced in Appendices D and E.
Finally, in Appendix H we present extra graphs that did not fit in the main paper and in Appendix I we present a table of all
of the conjugacy classes of subgroups ofS5.
C. Experiment Details
We conducted experiments focusing on the permutation group ofS5 andS6. All models were trained on NVIDIA GeForce
RTX 2080 GPUs. All models were implemented in PyTorch Paszke et al.[45] and trained with the Adam optimizer [28]
with a fixed learning rate of 0.001, weight decay set to 1.0,β1 = 0.9 andβ2 = 0.98. At the beginning of each training run,
the training set is sampled uniformly from all|Sn|2 combinations of permutations. Each optimization step was made on
the entire training set. Using our setup a singleS5 model trained in approximately 8 hours and a singleS6 model trained
in approximately 100 hours, though multiple training jobs could be scheduled on a single GPU. Analysis and reverse
engineering was performed with Vink et al. [56], Nanda & Bloom [39], Harris et al. [22], GAP [16], Stein et al. [53].
Table 2. Experiment hyperparameters.
Group % Train Set Num. Runs Num. Epochs Linear Layer Size Embedding Size
S5 40% 128 250,000 128 256
S6 40% 100 50,000 256 512
D. Group Theory
In this section, let us recall some basic definitions and propositions in group theory that are relevant to this paper.
14

Grokking Group Multiplication with Cosets
D.1. Groups
A groupG is a nonempty set equipped with a special element e∈ G called the identity and a multiplication operator·
satisfying the following:
• (inverse) For each element a∈G, there exists an elementb∈G such thata·b =b·a =e.
• (identity) For each element a∈G,a·e =e·a =a.
• (associativity) For elements a,b,c ∈G, we have (a·b)·c =a· (b·c).
The inverse ofa∈G is denoted bya−1.
Example D.1. The set of integers Z along with the addition + form a group. The identity element is 0. Also with the
addition, the same is true for the set of rational numbers Q, the set of real numbers R and the set of complex numbers C.
Example D.2. The symmetric group introduced in Section 3.1 along with the composition of permutations satisfies the
group axioms. The identity element is the identity permutation leaving each element unchanged.
Example D.3. The set of natural numbers N and addition do not form a group. The reason being that the inverse elements
do not exist except for 0.
Definition D.4. Given a groupG, a subgroupH is a subset ofG such that
• a·b∈H for anya,b∈H.
• e∈H.
• a−1∈H.
One can check thatH along with the multiplication satisfies the group axiom as well. H being a subgroup ofG is denoted
byH≤G.
D.2. Cosets and double cosets
Definition D.5. Given a proper subgroup H < Gand an element g∈ G, the set gH :={gh|h∈ H} is called a left
H-coset. Similarly,Hg :={hg|h∈H} is called a rightH-coset.
gH is sometimes called a coset if the subgroupH is clear from the context. When we do not mention whether it is a left
coset or a right coset, left coset is the default.
Lemma D.6. Two cosetsg1H andg2H are either the same subset ofG or disjoint (i.e.,g1HTg2H =∅).
Lemma D.7. IfG is a finite group, any twoH-cosets have the same number of elements.
As a result, one can pick suitable representative elements (but not unique)g1,··· ,gn∈G, so thatg1H,··· ,gnH form a
partition ofG. Because the cosets have equal sizes, we can also conclude that|G| is always divisible by|H|.
Definition D.8. Given two subgroupsH,L<G and an elementg∈G, the setHgL :={hgl|h∈H,l∈L} is called the
(H,L )-double coset, or the double coset if the pair (H,L ) is clear from the context.
Double cosets enjoy the similar property as cosets:
Lemma D.9. Two double cosetsHg 1L andHg 2L are either the same or disjoint.
As a result, G can be similarly decomposed as a disjoint union of (H,L )-double cosets. However, when G is finite,
(H,L )-double cosets do not always come with equal sizes. So the decomposition is not equal-sized.
For simplicity, we call the (H,H )-double coset theH-double coset.
15

Grokking Group Multiplication with Cosets
D.3. Normal Subgroups
Definition D.10. A subgroupN is normal inG, denotedN ⊴G, if for anyg∈G and anyn∈N, we havegng−1∈N.
A subgroup is normal if and only if the left and right cosets are the same, i.e., for anyg∈G, gN =Ng . Normal subgroups
are important because they are precisely the groups for which the set ofN-cosetsG/N has a natural group structure.
Definition D.11. Given a groupG and a normal subgroup N ⊴ G, the quotient groupG/N is defined to be the set of
N-cosets endowed with the multiplication given bygN·hN =ghN for anyg,h∈G.
The well-definedness of the multiplication is a consequence ofN being normal and its group axioms are straightforward to
check.
Example D.12. IfG is commutative (for everyg,h∈G, we havegh =hg), every subgroupH≤G is normal.
Example D.13. IfG =Sn, the subgroupSn−1 fixing the first element is not a normal subgroup. On the other hand, the
alternating subgroupAn (consisting of even permutations) is a normal subgroup ofSn.
The double cosets of a normal subgroup are simply the usual cosets.
Lemma D.14. Given a normal subgroupH ⊴G, the leftH-coset and the rightH-coset are in one-to-one correspondence.
Furthermore, the set ofH-double cosets is also in one-to-one correspondence toH-cosets.
Proof. By definition,gHg−1 =H. Therefore,gH =Hg.HgH =gHH =gH.
D.4. Conjugate Subgroups
The cosets of a normal subgroupN ⊴G themselves form a group. Ifx, y∈G andx∈gN but y∈hN, thenxy∈ghN .
IfG is not abelian, however, many or even all subgroups are not normal and do not have this property. For a non-normal
subgroupH, ag /∈H gives rise to a different conjugate subgroupgHg−1.
In general, the relationship between the cosets of H andgHg−1 is complex, but they will have at least one left and one
right coset in common:Hg−1 =g−1(gHg−1). Every right cosetHx will have a left coset pairy(gHg−1) such that when
multiplied, right coset on the left and left coset on the right,Hxy (gHg−1) = Hg−1, specifically whenxy =g−1.
This relationship between the cosets of pairs of conjugate subgroups is not as powerful as that of the cosets of normal
subgroups, but conjugate subgroups are guaranteed to exist in non-abelian groups, whereas there are many simple groups
without normal subgroups at all.
This relationship between pairs of conjugate subgroups is also useful enough that it is used by every model we trained. In
general, we have the following:
Lemma D.15. For anyH≤G and an elementg∈G, the set of conjugate elementsgHg−1 forms a subgroup ofG.
If the conjugate subgroupgHg−1 is different thanH, the left and right cosetsgH,Hg are different.
The double coset circuits operate by first identifying a pair of different conjugate subgroups H andgHg−1. It exploits
the fact that the left cosetgH and the right coset (gHg−1)g are the same subset ofG, which will be fully generalized and
elaborated in the later sections.
D.5. An important case
When a groupG decomposes as only two disjointH-double cosets, any pair of subgroups conjugate toH shares a left coset
with another’s right coset.
Lemma D.16. LetH1,...,H n be conjugate subgroups of G, such that for each Hi the double coset HigHi is equal to
eitherHi orG\Hi. Then for each pair of subgroupsHi andHj there exists ag∈G such thatHig =gHj. Moreover, the
only double cosets ofHi andHj areHigHj =gHj andHixHj =G\gHj.
Proof. Ifi =j, for anyh∈Hi the shared coset is the subgroup itself. If i̸=j, becauseHi andHj are conjugate, there
exists ag∈G such thatHj =g−1Hig. The left coset is equal to the right coset:
gHj =g(g−1Hig) = Hig
16

Grokking Group Multiplication with Cosets
Notice that the double cosetHigHj =Hi(Hig) = Hig. But forx̸=g:
HixHj =Hixg−1Hig (2)
= (G\Hi)g (3)
=G\Hig (4)
E. Representation Theory
E.1. Preliminaries
Definition E.1. Given a groupG, a representation ofG is a group homomorphismρV :G→GL(V ) for some finite (but
nonzero) dimensional vector spaceV over a fieldk. When we do not specifically mentionk, we use C as the default.
In other words, a representation maps a group elementg to a linear operatorf (g) : V →V whereV is a vector space of
dimensiond, so that the group multiplication becomes compositions of linear operators (f (g·h) = f (g)◦f (h)). Without
explicit specifications, all representations in this paper are assumed to be over complex numbers. Recall also that finite
dimensional linear operators can be represented as matrices, and composition of linear operators is then given as matrix
multiplication.
When the context is clear, sometimes we omit the subscriptV in the notationρV .
The representations of finite groups have a rich and beautiful theory (see Diaconis [8], Fulton & Harris, Joe [15]). Here, we
recall a few basic definitions and facts without going into details.
Definition E.2. A representationρV :G→GL(V ) is a sub-representation ofρW :G→GL(W ) ifV can be identified as
a linear subspace ofW so thatρW (g) restricts toρV (g) for allg∈G.
Example E.3. For any groupG, the mapG→GL(V ) sending all elements to the identity matrix is a representation. When
dim(V ) = 1 , we call it the trivial representation ofG.
Definition E.4. Given two representations ρV,ρW of G, the direct sum of vector spaces V ⊕ W admits a natural
representation ofG by lettingρV,ρW act on each component separately. We call this the direct sum of representations
ρV,ρW , and denote it byρV⊕ρW .
Definition E.5. Similarly, given two representationsρV,ρW , the tensor productV⊗W admits a natural representation
ofG by acting onV,W separately and extend by linearity. We call this the tensor product of representationsρV,ρW , and
denote it byρV⊗ρW .
Definition E.6. A representationρ of a groupG is irreducible, if it does not have sub-representations other thanρ.
We denote the set of all irreducible representations ofG by Irr(G)
Lemma E.7. A representationρ of a finite groupG is a direct sum of irreducible representations.
Example E.8. The trivial representation ofG is irreducible.
Example E.9. The permutation representation mapsSn→GL(C3), i.e. 3×3 matrices with a single 1 in each row and
column and zeros everywhere else.
(2 1 3)7→


0 1 0
1 0 0
0 0 1

 (3 2 1)7→


0 0 1
0 1 0
1 0 0


You can see that the matrices of the permutation representation act on the basis vectors of C3:


0 0 1
0 1 0
1 0 0




x
y
z

 =


z
y
x


17

Grokking Group Multiplication with Cosets
What it means to be a representation is that the group multiplication becomes matrix multiplication, so just as
(2 1 3)(3 2 1) = (2 3 1) , 

0 1 0
1 0 0
0 0 1




0 0 1
0 1 0
1 0 0

 =


0 0 1
1 0 0
0 1 0


Example E.10. The permutation representation is reducible, because there is a subspace of C3 that is invariant to it’s action.


0 0 1
0 1 0
1 0 0




x
x
x

 =


x
x
x


Note that there is no permutation matrix acting on the vector
 x x x T
that will change it, because all of the components
are equal.
As it turns out, there are no irreducible representations ofS3 that are three-dimensional. The largest irrep ofS3 isρ(2,1),
which is made of 2×2 matrices. The matrices of the (2, 1) irrep ofS3 are as follows:
(1 2 3)7→
1 0
0 1

(2 1 3)7→
−1 0
0 1

(3 2 1)7→
 1/2 −
√
3/2√
3/2 −1/2

(1 3 2)7→
−1/2
√
3/2√
3/2 1 /2

(3 1 2)7→
−1/2
√
3/2
−
√
3/2 −1/2

(2 3 1)7→
−1/2
√
3/2
−
√
3/2 −1/2

We leave it as an exercise to the reader to verify thatρ(2,1)(2 1 3)ρ(2,1)(3 2 1) = ρ(2,1)(2 3 1) .
Trace is an important notion in linear algebra. Taking trace of a representation induces an important map fromG to C.
Definition E.11. LetρV be a representation ofG. The character ofρV is a mapχ(ρV ) : G→ C given byχ(ρV )(g) =
tr(ρV (g)).
Lemma E.12. The character χ(ρV ) takes the same value on a conjugacy class of G. In other words, χ(ρV )(h) =
χ(ρV )(ghg−1).
To distill this property for a wider range of functions, we have the following definition:
Definition E.13. Letf :G→ C be a map. Iff (h) = f (ghg−1) for anyg,h∈G,f is called a class function.
For a finite groupG, the set of class functions form a finite-dimensional vector space. There is an important inner product
between class functions.
Definition E.14. The inner product of two class functionsϕ,ψ are defined as:
⟨ϕ,ψ⟩ = 1
|G|
X
g∈G
ϕ(g)ψ(g).
As we require the class functions to take the same values on conjugacy classes, the dimension of the vector space of class
functions is equal to the number of conjugacy classes inG. On the other hand, we have the following important theorem:
Theorem E.15. The characters of Irr(G) forms an orthonormal basis in the vector space of class functions.
Lemma E.16. For a finite groupG, Irr(G) is a finite set. Furthermore, the order of Irr(G) is equal to the number of
conjugacy classes inG.
F. Fourier transform over finite groups
Despite being mostly perceived as a powerful tool in physics and engineering, the Fourier transform has also been successfully
applied in group theory thanks to its generalization to locally compact abelian groups as well as an analog over finite groups.
18

Grokking Group Multiplication with Cosets
The purpose the group Fourier transform serves is largely analogous to the one served by the classical Fourier transform: it
provides an alternate orthogonal basis with which to analyze functions from a groupG to either R or C.
To motivate the transition from the classical Fourier theory to the Fourier theory over groups, we start with a brief recall of
the definitions.
The classical Fourier transform over real numbers converts a complex-valued Lebesgue-integrable functionf : R→ C into
a function from the complex unit circleS1 to C with following formula:
ˆf (ξ) =
Z ∞
−∞
f (x)e−2πiξxdx. (5)
Taking one step further in abstraction, we note thate−2πiξx as a function ofx has the defining properties of turning additions
into multiplications (being a group homomorphism) and always having complex norm 1:
e−2πiξ(x1+x2) =e−2πiξx 1·e−2πiξx 2,
|e−2πiξx| = 1.
We call such functions thecharacters of R, though they are often thought of as frequencies. One can prove that all characters
of R can be written ase−2πiξx for a suitableξ∈ R.
Looking back at (5), the properties we need in order to define the Fourier transform over R are:
• R has the Lebesgue measure (allowing for integration to happen).
• R is a group (so that the characters make sense as group homomorphisms from R to the unit circle groupS1⊂ C).
Now, if we are given a finite groupG, the Fourier transform of a finite group is an operator converting a mapf :G→ C
into a function between Irr(G) and the set of linear operatorsM (V ).
Definition F.1. Given a groupG, the Fourier transformof a mapf :G→ C is a function ˆf from Irr(G) to the union of
M (Cn) for alln such that
ˆf (ρ) =
X
a∈G
f (a)ρ(a)
for an irreducible representationρ.
The analogy comes from the following similar facts:
• G, as a finite set, has the invariant discrete measure (where the “integration” becomes the sum).
• G is a group, and the irrepsρ are in a sense the ”smallest” group homomorphisms fromG toGL(n, C) (note that the
images ofρ similarly have complex-norm-1 determinants due toG being a finite group).
For more details and applications, one can refer to, for example, Elias M. Stein [11]. We would like to note that there is also
an inverse transform that restores the original functionf from ˆf:
f (g) = 1
|G|
X
ρ∈Irr(G)
dρ tr[ ˆf (ρ)ρ(g−1)] (6)
G. The Coset Circuit (with more math)
We did not introduce it in the main body of our paper because it would distract from the core of our results, but for the
first half of our investigation the Fourier transform over the symmetric group was integral to our investigation. We were
building directly on [4] who had shown striking results around the weights of single-layer models showing high degrees of
correlation with the irreps of the symmetric group. We wished to cast those results in the language of the group Fourier
transform. Even when we realized that the mechanism of the model was based around cosets it became extremely important
to understand why our coset circuit was so concentrated in Fourier space.
19

Grokking Group Multiplication with Cosets
G.1. Harmonic Analysis on the Symmetric Group
The presentation in the Appendix E was given in terms of functions on C because it is required for arbitrary groups. For Sn
all of the irreps are rational [15] and the Fourier transform of functions onSn can safely be defined over R.
In this section we describe how we use the Fourier transform to analyze the weights and activations of an MLP. The inputs to
the model are two one-hot vectors, xl, xr, which multiply the embedding matrices Elxl and Erxr. El and Er ared×|G|
matrices, whered is the embedding dimension and|G| is the size of the group. The columns are the embedding vectors for a
single elementg∈G. The normal approach would be to try and look at the column spaces of El and Er, as these columns
are the inputs to the model. However, since each row of El and Er and each value of that row is associated with a single
element ofG, we instead treat each row of the embedding as a functionf :G→ R.
In fact, anywhere in the model where a matrix or set of activations has|G| in the shape we can expand into the Fourier basis.
For non-abelian groups, each Fourier frequency is an irrep, and the Fourier transform for each irrep is matrix-valued. This is,
on its face, less interpretable than what we started with. Following the techniques outlined in Diaconis [8], however, we can
expand the function at each elementg∈G into a new Fourier basis. Concretely, if our functionf :G→ R is represented
as a vector, we know from 6 that each element of the vector is a sum of the Fourier components:


f (g1)
f (g2)
...
f (g|G|)

 = 1
|G|


P
ρdρ tr[ ˆf (ρ)ρ(g−1
1 )]P
ρdρ tr[ ˆf (ρ)ρ(g−1
2 )]
...P
ρdρ tr[ ˆf (ρ)ρ(g−1
|G|)]


We can keep track of all of the Fourier components at once by purposefully not completing the sum from 6), but instead
keep each term into a new dimension:
1
|G|


dρ1 tr[ ˆf (ρ1)ρ1(g−1
1 )] ... d ρk tr[ ˆf (ρk)ρk(g−1
1 )]
dρ1 tr[ ˆf (ρ1)ρ1(g−1
2 )] ... d ρk tr[ ˆf (ρk)ρk(g−1
2 )]
... ...
dρ1 tr[ ˆf (ρ1)ρ1(g−1
|G|)] ... d ρk tr[ ˆf (ρk)ρk(g−1
|G|)]


Though this may seem like it is only making the data more complicated, it gives us many tools for analyzing the data. In
particular, it turns out that the weights and activations are sparse in this new basis, which gives us a small path forward in
analyzing the mechanisms.
Corollary G.1. IfHi andHj are conjugate subgroups ofG such that the only two double cosets areHigHj andHiHj,
then each right coset Hix has a paired left coset yHj wherey = x−1g such that for all hx ∈ Hix and hy ∈ yHj,
hxhy∈HigHj
Lemma G.2. Letf :G→ C be constant on the cosets ofH≤G and non-zero on at least one coset. Then ˆf (ρ) = 0 if the
restriction ofρ toH,ρ|H does not contain the trivial representation as a subrepresentation.
Proof. The functionf can be decomposed as the sum of functions
fxH (σ) =
(
αx σ∈xH
0 otherwise
for each cosetxH. Because Fourier transform ˆf is invariant under translation we may, without loss of generality, analyze
only the functionfH. For a givenαx, ˆfxH (ρ) = ˆfx
H (ρ) = ρ(x) ˆfH (ρ) for allx∈G. Recall the definition of ˆfH (ρ) from
20

Grokking Group Multiplication with Cosets
F.1:
ˆfH (ρ) =
X
g∈G
fH (g)ρ(g) (7)
=αH
X
h∈H
ρ|H (h) (8)
=αH
X
h∈H
T−1[
M
τi∈T
τi(h)]T (9)
=αHT−1[
M
τi∈T
X
h∈H
τi(h)]T (10)
where in 9 we decomposeρ|H into a direct sum of irreps ofH. But because each τi is irreducible,P
h∈Hτi(h) = 0 unless
τi is the trivial irrep. Thus, unless the decomposition ofρH into irreps ofH includes the trivial representation, ˆf|H = 0
G.2. Logits and Counting Cosets
In Chughtai et al. [4], one way of justifying the GCR algorithm is to study the correlation between the character functions
and the neuron activations. We would like to argue that the correlation between the GCR and the coset membership counting
function may already exist, and in some simple cases it can be made explicit.
More precisely, we are measuring the correlation between the character function χ(ρ) of an irrep ρ with a set function
f :G→ C. In this section, we provide an explicit characterization of f in terms of trace and irreps, when f counts the
membership of cosets.
We are specifically interested in the following situation:
Lemma G.3. Suppose f : G→ C is a function such that its Fourier transform ˆf is nonzero only on an irreducible
representationρ and the trivial representation. Let ˆf (ρ) = A∈M (Cn). We have the following explicit formula:
f (σ) = dρ
|G| tr(A·ρ(σ−1)) +|H|
|G|. (11)
Proof. This is immediate by the Fourier inversion formula.
In this case, althoughf is not directly written in terms of tr(ρ(σ−1)),f is correlated with tr(ρ(σ−1)) depending on how
muchA is concentrated to the diagonal and how even are the diagonal entries. For the rest of the section, we show that
under certain conditions, Equation (11) applies verbatim to the functions that count membership of cosets for a collection of
conjugate subgroups.
Given a subgroupH≤G, let 1H be the function that takes value 1 on the subgroupH, and takes 0 otherwise. The action of
G on cosetsG/H induces a representation ofG on C|G/H| by permuting the basis accordingly. We call it the permutation
representation ofG onG/H.
Lemma G.4. The Fourier transform of 1H is nonzero only at the irreducible components of the permutation representation
ofG onG/H.
Proof. By definition, the Fourier transform of 1H on an irrepρ is
c1H (ρ) =
X
a∈H
ρ(a).
Notice that the image of P
a∈H
ρ(a) are invariant underH due to the symmetry of this expression.
LetV be the vector space whereρ acts on. Under the action of the subgroupH throughρ, one can decomposeV as irreps
ofH. We group them into two parts:
V =VH⊕V′,
21

Grokking Group Multiplication with Cosets
whereVH is a direct sum of copies of trivial representation ofH (or in other words, the invariant subspace ofV underH),
andV′ is the direct sum of nontrivial irreducible components ofV .
We immediately see the following by definition:
X
a∈H
ρ(a)|V H =|H|· IdV H.
Also by definition, nontrivial irreps ofH do not have invariant subspaces since they do not admit proper sub-representations.
Therefore, X
a∈H
ρ(a)|V ′ = 0.
As a result, c1H (ρ) is simply a scaled projection to the invariant subspace of V . Whether it is zero depends on whether
ResHρ has any trivial components.
By Frobenius reciprocity,
⟨IndG
H (1H ),χ (ρ)⟩ =⟨1H,χ (ResH (ρ))⟩H,
whereχ(ρ) is the character of the irrepχ∈ Irr(G) given by its traces, and⟨·⟩ is the inner product between class functions.
The left-hand side⟨IndG
H (1H ),χ (ρ)⟩ is nonzero if and only ifρ is an irreducible component of the permutation representation
ofG onG/H. The right-hand side⟨1H,χ (ResH (ρ))⟩H is nonzero if and only if dim(VH )̸= 0
Note that this lemma also works for 1gH for a cosetgH, since Fourier transforms turns the translation action byg into group
multiplication byρ(g).
In the double coset circuit, we are specifically interested in the membership counting functions. More specifically, let
H1,··· ,Hn be a collection of conjugate subgroups of G. Given an element σ∈ G, define the membership counting
function as
F (σ) =
nX
i=1
1σHi.
Combining all previous results, we have the following corollary describing the membership counting functionF .
Corollary G.5. If the permutation representation ofG onG/H1 has only 2 irreducible components, the Fourier transform
ˆF of the membership counting functionF is nonzero only at these 2 irreducible components. In particular, the equation (11)
applies toF .
One may wonder how restrictive it is for the permutation representation onG/H to only have 2 irreducible components.
The follow lemma shows that it applies to our case whenG =Sn andH =Sn−1.
Lemma G.6. ForSn and the subgroupSn−1 fixing one element, the permutation representation has only two irreducible
components.
Proof. The natural representation ofSn on Cn (by permuting the basis) decomposes as a direct sum of trivial representation
and the standard representation of dimensionn− 1.
Indeed, we see that when looking at the action of an individual neuron on the prediction space (i.e. “if this neuron fires,
which predictions become more likely and which less?”), we see that it is only neurons that are predicting the same coset
that are correlated. The average pairwise correlation of neuron actions is uncorrelated, as is the correlation of neurons
associated with the same irrep. Refer to Table 3 for the full results.
22

Grokking Group Multiplication with Cosets
Table 3. The correlation of unembedding neurons. Neurons that correspond to the same coset are averaged together in the unembedding,
leading to the unembedding vectors being highly correlated.
Mean Correlation Std Dev Correlation
Within Coset 0.814 0.445
Within Subgroup Conjugacy Class -0.002 0.222
Baseline -0.003 0.163
.
G.3. An Asymptotic Analysis
Our theory of coset circuits and the GCR algorithm of [4] cannot be equivalent because there is no one-to-one relationship
between irreps and subgroups. Even forS5, there are more subgroups than irreps. Quantitatively speaking, the irreps already
fail to catch up with the number of subgroups. For the direct comparison ofSn refer to
Asymptotically, the number of subgroups ofSn is bounded below as follows (see Pyber [48, Corollary 3.3]):
2( 1
16 +o(1))n2
≤| Sub(Sn)|,
whereas the number of irreps ofSn is asymptotically the following (see Erdos [13]):
| Irr(Sn)|∼ 1
4n· 3
1
2
eπ( 2
3 )
1
2n
1
2
.
We see that the former has a much higher asymptotic growth than the latter.
In practice, as can be seen in Table 5, many subgroups concentrate on more than one irrep. We do not have an explanation
for why the coset circuits always do concentrate one irrep. In practice, the different values for the cosets are arranged so
that the contributions of all but one irrep cancel out. We hypothesize that it may have something to do with the margin
maximization effect discussed in [38]. As we mention in the main body, we observe that subgroups which concentrate on
more than one irrep will form coset circuits that concentrate entirely on any of the irreps, while still behaving equivalently.
We do not think that there is in fact a connection between what the circuit is doing the irrep.
Table 4. The number of subgroups and the number of irreps from S5 to S12. The numbers of subgroups use the A005432 sequence of the
OEIS [42]. The numbers of irreps corresponds to the number of integer partitions of n and use the A000041 sequence of the OEIS [42].
S5 S6 S7 S8 S9 S10 S11 S12
Number of subgroups 156 1455 11300 151221 1694723 29594446 404126228 10594925360
Number of irreps 7 11 15 22 30 42 56 77
23

Grokking Group Multiplication with Cosets
H. Extra Graphs
H.1. Distribution over Subgroups and Cosets
0
30
60
90
120Number of Runs
A4 A5 F20
0% 40%80%
0
30
60
90
120
S3
0% 40%80%
S4
0% 40%80%
% of Neurons in Linear Layer
S2 × S3
(a) 128 Models trained on S5
0
25
50
75
100Number of Runs
A5 A6 A*
5
0%25%50%75%
0
25
50
75
100
S3 × S3
0%25%50%75%
S5
0%25%50%75%
% of Neurons in Linear Layer
S*
5 (b) 100 Models trained on S6
Figure 6. Distribution of coset circuits for models trained on S5 and S6 with different initial seeds. Every model has a few sign circuit
neurons that correspond to An < S n, but the model cannot completely solve the task with only the sign circuit, so there are never more
than a few. Every other subgroup could, with enough neurons, be used to completely solve the the multiplication, but in general if a model
primarily uses a single subgroup it is Sn−1 (in the main body of the paper we refer to these subgroups as Hi, for the element i∈ [n]
that is fixed). Every model has at least a few Sn−1 neurons. Many models use a mix of subgroups and there is often a “long tail” of a
subgroup being represented by only one or two neurons. The subgroups marked with asterisks,A∗
5 and S∗
5 , correspond to the “exceptional”
subgroups of S6, which come from an outer automorphism that only S6 has [26]. These subgroups are isomorphic to S5 and A5, but not
conjugate to the subgroups that come from fixing an element in{1, . . . ,6}.
24

Grokking Group Multiplication with Cosets
H.2. Other Examples of Coset Circuits Forming
4
 2
 0 2 4
0
10
20
30# of Permutations
140,000 Steps Coset
S3 × S2(13245)
S3 × S2(14235)
S3 × S2(15234)
S3 × S2(21345)
S3 × S2(24135)
S3 × S2(25134)
S3 × S2(34125)
S3 × S2(35124)
S3 × S2(45123)
S3 × S2
4
 2
 0 2 4
150,000 Steps
4
 2
 0 2 4
Pre-Activation Value
160,000 Steps
(a) S3×S2 Left Permutations
4
 2
 0 2 4
0
10
20
30# of Permutations
140,000 Steps Coset
S3 × S2(12354)
S3 × S2(12534)
S3 × S2(15234)
S3 × S2(21345)
S3 × S2(21354)
S3 × S2(21534)
S3 × S2(23145)
S3 × S2(23154)
S3 × S2(23415)
S3 × S2
4
 2
 0 2 4
150,000 Steps
4
 2
 0 2 4
Pre-Activation Value
160,000 Steps
(b) S3×S2 Right Permutations
Figure 7. The formation of an S3×S2 neuron.
2.5
 0 2.5
0
5
10
15
20
25# of Permutations
100,000 Steps Coset
A4(12354)
A4(12435)
A4(12453)
A4(12534)
A4(12543)
A4(13245)
A4(13254)
A4(23145)
A4(23154)
A4
2.5
 0 2.5
150,000 Steps
2.5
 0 2.5
200,000 Steps
2.5
 0 2.5
Pre-Activation Value
250,000 Steps
(a) A4 Left Permutations
2.5
 0 2.5
0
5
10
15
20
25# of Permutations
100,000 Steps Coset
(12354)A4
(12435)A4
(12453)A4
(12534)A4
(12543)A4
(14235)A4
(14253)A4
(41235)A4
(41253)A4
A4
2.5
 0 2.5
150,000 Steps
2.5
 0 2.5
200,000 Steps
2.5
 0 2.5
Pre-Activation Value
250,000 Steps
(b) A4 Right Permutations
Figure 8. The formation of an A4 neuron.
25

Grokking Group Multiplication with Cosets
I. Irreducible Representations
I.1. Symmetric GroupS5
For a subgroupH≤G, we can investigate the Fourier transform of the indicator function 1H by looking at its evaluation at
each irrep. Concretely, we first center the indicator function by defining
f (g) =



−|H|
|G|, g̸∈H
1−|H|
|G|, g∈H.
By doing so, ˆf evaluates to 0 on the trivial representation ofG.
Given an irrepρ∈ Irr(G), we first denote the value of the Fourier transform off atρ by ˆf|ρ. The contribution ofρ to ˆf is
defined by the following:
∥ ˆf|ρ∥2
P
δ∈Irr(G)
∥ ˆf|δ∥2
Here, we list all the conjugacy classes of subgroups ofS5 and how each irrep ofS5 contributes to their centered indicator
function. We center the indicator function to remove the contribution of the trivial irrep, which is only based on the index of
the subgroup. This step makes the contributions comparable. In the first column, we show the homomorphism type of each
subgroup. Recall that two groupsG,G′ are homomorphic if there exists a functionf :G→G′ such that for allg, h∈G,
f (gh) = f (g)f (h). Every group within a conjugacy class is a homomorphic, with the homomorphism of two subgroups
H, H′ ofG given by conjugation by an element ofg∈G,h7→ghg−1. Two conjugacy classes of subgroups, however, may
be homomorphic as groups, but no homomorphism can be given as conjugation by an element ofG. Different conjugacy
classes of subgroups that are homomorphic are distinguished in the second column by an example set of generators. In the
list:
• Cn means cyclic groups of ordern.
• Sn means the symmetric group ofn elements.
• An means the alternating group of n elements,the subgroup ofSn consisting of even permutations. Recall than an
“even” permutation is one that consists of an even number of transpositions.
• D2n means then-gon dihedral group of order 2n (the symmetric group of regular polyhedron withn edges).
• F20 means the Frobenius group of order 20, isomorphic toC4 ⋉C5 [10].
26

Grokking Group Multiplication with Cosets
Isomorphism type Generators Size (4, 1) (3 , 2) (3 , 12) (2 2, 1) (2 , 13) (1 5)
C2 ⟨(12)⟩ 2 20.3% 25.4% 30.5% 17% 6.8% -
C2 ⟨(12)(34)⟩ 2 13.6% 25.4% 20.3% 25.4% 13.6 1.7%
C3 ⟨(123)⟩ 3 20.1% 12.8% 30.8% 12.8% 20.5% 2.6%
C4 ⟨(1234)⟩ 4 13.6% 25.4% 20.3% 25.4% 13.6% 1.7%
C2×C2 ⟨(12), (34)⟩ 4 27.6% 34.5% 20.7% 17.2% - -
C2×C2 ⟨(12)(34), (13)(24)⟩ 4 13.8% 34.5% - 34.5% 13.8% 3.5%
C5 ⟨(12345)⟩ 5 - 21.7% 52.2% 21.7% - 4.4%
C6 ⟨(123), (45)⟩ 6 21.1% 26.3% 31.6% - 21.1% -
S3 ⟨(123), (12)⟩ 6 42.1% 26.3% 31.6% - - -
S3 5 ⟨(123), (12)(45)⟩ 6 21.1% 26.3% - 26.3% 21.1% 5.3%
D8 ⟨(1234), (13)⟩ 8 28.6% 35.7% - 35.7% - -
D10 ⟨(12345), (25)(34)⟩ 10 - 45.5% - 45.5% - 1%
S3×S2 ⟨(123), (12), (45)⟩ 12 55.6% 44.4% - - - -
A4 ⟨(12)(34), (123)⟩ 12 44.4% - - - 44.4% 11.2%
F20 ⟨(12345), (2354)⟩ 20 - - - 100% - -
S4 ⟨(12345), (12)⟩ 24 100% - - - - -
A5 ⟨(12345), (123)⟩ 60 - - - - - 100%
Table 5. Subgroups of S5 and the contribution of each irrep to their centered indicator function.
27
