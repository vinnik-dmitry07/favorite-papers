##### Report GitHub Issue

Content selection saved. Describe the issue below:

# The Road Less Scheduled

###### Abstract

Existing learning rate schedules that do not require specification of the optimization stopping step T T are greatly out-performed by learning rate schedules that depend on T T . We propose an approach that avoids the need for this stopping time by eschewing the use of schedules entirely, while exhibiting state-of-the-art performance compared to schedules across a wide family of problems ranging from convex problems to large-scale deep learning problems. Our Schedule-Free approach introduces no additional hyper-parameters over standard optimizers with momentum. Our method is a direct consequence of a new theory we develop that unifies scheduling and iterate averaging. An open source implementation of our method is available 1 1 1 https://github.com/facebookresearch/schedule_free . Schedule-Free AdamW is the core algorithm behind our winning entry to the MLCommons 2024 AlgoPerf Algorithmic Efficiency Challenge Self-Tuning track.

## 1 Introduction

The theory of optimization, as applied in machine learning, has been successful at providing precise, prescriptive results for many problems. However, even in the simplest setting of stochastic gradient descent (SGD) applied to convex Lipschitz functions, there are glaring gaps between what our current theory prescribes and the methods used in practice.

Consider the stochastic gradient descent (SGD) step with step size γ > 0 \gamma>0 , z t + 1 = z t − γ ​ g t z_{t+1}=z_{t}-\gamma g_{t} where g t g_{t} is the stochastic (sub-)gradient at time t t , computed at the point z t z_{t} (formally defined in Section 1.2 ) of a convex Lipschitz function f f . Although standard practice for many classes of problems, classical convergence theory suggests that the expected loss of this z z sequence is suboptimal , and that the Polyak-Ruppert (PR) average x x of the sequence should be returned instead ( Polyak,, 1990 ; Ruppert,, 1988 ) : z t + 1 \displaystyle z_{t+1} = z t − γ ​ g t \displaystyle=z_{t}-\gamma g_{t} (1) x t + 1 \displaystyle x_{t+1} = ( 1 − c t + 1 ) ​ x t + c t + 1 ​ z t + 1 , \displaystyle=\left(1-c_{t+1}\right)x_{t}+c_{t+1}z_{t+1}, (2) where using c t + 1 = 1 / ( t + 1 ) c_{t+1}=1/(t+1) results in x t = 1 T ​ ∑ t = 1 T z t x_{t}=\frac{1}{T}\sum_{t=1}^{T}z_{t} . Despite their theoretical optimality, PR averages give much worse results in practice than using the last-iterate of SGD (Figures 2 , 11 ) — a folk-law result in the field of optimization, and a large theory-practice gap that is often attributed to the mismatch between this simplified problem class and the complexity of problems addressed in practice.

Recently, Zamani and Glineur, (2023) and Defazio et al., (2023) showed that the exact worst-case optimal rates can be achieved via carefully chosen learning rate sequences (also known as schedules ) alone, without the use of averaging. This result suggests that schedules have, in some sense, the same role to play as PR averaging in optimization. However, schedules have a critical disadvantage: they require setting the optimization stopping time T T in advance.

Motivated by the theory-practice gap for Polyak-Ruppert averaging, we ask the following question: Do there exist iterate averaging approaches that match the empirical performance of learning rate schedules, without sacrificing theoretical guarantees? By developing a new link between averaging and learning rate sequences, we introduce a new approach to averaging that maintains the worst-case convergence rate theory of PR averaging, while matching and often exceeding the performance of schedule-based approaches – firmly answering this question in the affirmative.

### 1.1 Summary of Results

• Our approach does not require the stopping time T T to be known or set in advance. It closely tracks the Pareto frontier of loss versus training time during a single training run (Figure 1 ), while requiring no additional hyper-parameters over the base SGD (with momentum) or Adam optimizer.

• Our approach uses an alternative form of momentum that replaces traditional momentum. This form has appealing theoretical properties: it is worst case optimal for any choice of the momentum parameter in the convex Lipschitz setting , a property that does not hold for traditional momentum.

• Our key theoretical result is a new online-to-batch conversion theorem, which establishes the optimality of our method while also unifying several existing online-to-batch theorems.

• We perform, to our knowledge, one of the largest machine learning optimization algorithm evaluations to date, consisting of 28 problems, ranging from logistic regression to large-scale deep learning problems. This evaluation contains more distinct and diverse large-scale machine-learning problems than any other optimizer evaluation we are aware of in the literature. Schedule-Free methods show strong performance, matching or out-performing heavily-tuned cosine schedules.

• Schedule-Free AdamW won the MLCommons 20204 AlgoPerf Algorithmic Efficiency Challenge Self-Tuning track, providing independent verification of it’s state-of-the-art performance against other optimization algorithms when hyperparameter-tuning is limited. We provide details of our entry and plots comparing it to the competition baseline.

### 1.2 Notation

Consider the stochastic convex minimization min x ∈ ℝ d ⁡ f ⁡ ( x ) = 𝔼 ζ ​ [ f ⁡ ( x , ζ ) ] , \min_{x\in\mathbb{R}^{d}}f(x)=\mathbb{E}_{\zeta}[f(x,\zeta)], where each f ⁡ ( x , ζ ) f(x,\zeta) is Lipschitz and convex in x x , and the expectation is taken over the random variable ζ \zeta . With a slight abuse of notation, we assume we are given, at time step t t and any point y y that we choose, an arbitrary sub-gradient ∇ f ​ ( y , ζ t ) \nabla f(y,\zeta_{t}) from the sub-differential of f f .

## 2 Method

We propose the following method, which we call Schedule-Free SGD: y t \displaystyle y_{t} = ( 1 − β ) ​ z t + β ​ x t , \displaystyle=(1-\beta)z_{t}+\beta x_{t}, (3) z t + 1 \displaystyle z_{t+1} = z t − γ ∇ f ( y t , ζ t ) , \displaystyle=z_{t}-\gamma\nabla f(y_{t},\zeta_{t}), (4) x t + 1 \displaystyle x_{t+1} = ( 1 − c t + 1 ) ​ x t + c t + 1 ​ z t + 1 , \displaystyle=\left(1-c_{t+1}\right)x_{t}+c_{t+1}z_{t+1}, (5) where c t + 1 = 1 / ( t + 1 ) c_{t+1}=1/(t+1) and z 1 = x 1 z_{1}=x_{1} is the initial point. Note that with this weighting, the x x sequence is just an online equal-weighted average of the z z sequence. The y y sequence is the gradient location sequence (on which gradients are evaluated at each step) and the x x sequence is the evaluation sequence, our current best estimate of the parameters. The z z sequence is the base sequence, which is where the base optimizer’s update is performed (in this case SGD).

This method has a momentum parameter β \beta that interpolates between Polyak-Ruppert averaging ( OPEN β = 0 ) \beta=0) and Primal averaging ( β = 1 \beta=1 ). Primal averaging ( Nesterov and Shikhman,, 2015 ; Tao et al.,, 2018 ; Cutkosky,, 2019 ; Kavis et al.,, 2019 ; Sebbouh et al.,, 2021 ; Defazio and Gower,, 2021 ; Defazio and Jelassi,, 2022 ) , is an approach where the gradient is evaluated at the averaged point x x , instead of z z : z t + 1 \displaystyle z_{t+1} = z t − γ ∇ f ( x t , ζ t ) \displaystyle=z_{t}-\gamma\nabla f(x_{t},\zeta_{t}) (6) x t + 1 \displaystyle x_{t+1} = ( 1 − c t + 1 ) ​ x t + c t + 1 ​ z t + 1 , \displaystyle=\left(1-c_{t+1}\right)x_{t}+c_{t+1}z_{t+1}, (7) this approach maintains the worst-case optimality of PR averaging but is generally considered to converge too slowly to be practical (Figures 2 , 11 ). The advantage of our interpolation is that we get the best of both worlds. We can achieve the fast convergence of Polyak-Ruppert averaging (since the z z sequence moves much quicker than the x x sequence), while still keeping some coupling between the returned sequence x x and the gradient-evaluation locations y y , which increases stability. Values of β \beta similar to standard momentum values β ≈ 0.9 \beta\approx 0.9 appear to work well in practice. We will use the notation α = 1 − β \alpha=1-\beta when convenient.

In this formulation, β = 0.9 \beta=0.9 gives the practical advantages of momentum, dampening the immediate impact of large gradients, resulting in more stable training. To see this, notice that the immediate effect of the gradient g t g_{t} at step t t is to introduce ( 1 − β ) ​ g t = 0.1 ​ g t (1-\beta)g_{t}=0.1g_{t} into the iterate sequence y y . This is similar to exponential-moving-average (EMA) momentum, where also ( 1 − β ) ​ g t (1-\beta)g_{t} is added into the iterate sequence on step t t . However, here the remainder of g t g_{t} is very slowly added into y y over time, via its place in the average x x , whereas with an EMA with β = 0.9 \beta=0.9 , the majority of the gradient is incorporated within the next 10 steps.

So from this viewpoint, the Schedule-Free updates can be seen as a version of momentum that has the same immediate effect, but with a greater delay for adding in the remainder of the gradient. This form of momentum (by interpolation) also has a striking advantage: it does not result in any theoretical slowdown; it gives the optimal worst case ( Nesterov,, 2013 ) convergence for the non-smooth convex setting (including constants), for any choice of momentum β \beta between 0 and 1 inclusive:

###### Theorem 1 .

Suppose F F is a convex function, and ζ 1 , … , ζ T \zeta_{1},\dots,\zeta_{T} is an i.i.d. sequence of random variables such that F = 𝔼 ⁡ [ f ⁡ ( x , ζ ) ] F=\mathbb{E}[f(x,\zeta)] for some function f f that is G G -Lipschitz in x x . For any minimizer x ⋆ x_{\star} , define D = ‖ x 1 − x ⋆ ‖ D=\left\|x_{1}-x_{\star}\right\| and γ = D / ( G ​ T ) \gamma=D/(G\sqrt{T}) . Then for any β ∈ [ 0 , 1 ] \beta\in[0,1] , Schedule-Free SGD ensures: 𝔼 ⁡ [ F ⁡ ( x T ) − F ⁡ ( x ⋆ ) ] ≤ D ​ G T \displaystyle\mathbb{E}[F(x_{T})-F(x_{\star})]\leq\frac{DG}{\sqrt{T}} (8)

In contrast, exponential-moving-average momentum in the non-smooth setting actually hurts the theoretical worst-case convergence rate. The Schedule-Free approach maintains the advantages of momentum ( Sutskever et al.,, 2013 ) without the potential worst-case slow-down.

### 2.1 General Theory

The method analyzed in Theorem 1 is actually a special-case of a more general result that incorporates arbitrary online optimization algorithms rather than only SGD, as well as arbitrary time-varying sequences of β t \beta_{t} . The proof is provided in Appendix A .

###### Theorem 2 .

Let F F be a convex function. Let ζ 1 , … , ζ T \zeta_{1},\dots,\zeta_{T} be an iid sequence such that F ⁡ ( x ) = 𝔼 ζ ​ [ f ⁡ ( x , ζ ) ] F(x)=\mathbb{E}_{\zeta}[f(x,\zeta)] . Let z 1 , … , z T z_{1},\dots,z_{T} be arbitrary vectors and let w 1 , … , w T w_{1},\dots,w_{T} and β 1 , … , β T \beta_{1},\dots,\beta_{T} be arbitrary numbers in [ 0 , 1 ] [0,1] such that z t z_{t} , w t w_{t} and β t \beta_{t} are independent of ζ t , … , ζ T \zeta_{t},\dots,\zeta_{T} . Set: x t \displaystyle x_{t} = ∑ i = 1 t w i ​ z i ∑ i = 1 t w i = x t − 1 ​ ( 1 − w t ∑ i = 1 t w i ) ⏟ ≜ 1 − c t + w t ∑ i = 1 t w i ⏟ ≜ c t ​ z t \displaystyle=\frac{\sum_{i=1}^{t}w_{i}z_{i}}{\sum_{i=1}^{t}w_{i}}=x_{t-1}\underbrace{\left(1-\frac{w_{t}}{\sum_{i=1}^{t}w_{i}}\right)}_{\triangleq 1-c_{t}}+\underbrace{\frac{w_{t}}{\sum_{i=1}^{t}w_{i}}}_{\triangleq c_{t}}z_{t} (9) y t \displaystyle y_{t} = β t ​ x t + ( 1 − β t ) ​ z t \displaystyle=\beta_{t}x_{t}+(1-\beta_{t})z_{t} (10) g t \displaystyle g_{t} = ∇ f ​ ( y t , ζ t ) . \displaystyle=\nabla f(y_{t},\zeta_{t}). (11) Then we have for all x ⋆ x_{\star} : 𝔼 ⁡ [ F ⁡ ( x T ) − F ⁡ ( x ⋆ ) ] ≤ 𝔼 ⁡ [ ∑ t = 1 T w t ​ ⟨ g t , z t − x ⋆ ⟩ ] ∑ i = 1 T w i . \displaystyle\mathbb{E}[F(x_{T})-F(x_{\star})]\leq\frac{\mathbb{E}[\sum_{t=1}^{T}w_{t}\langle g_{t},z_{t}-x_{\star}\rangle]}{\sum_{i=1}^{T}w_{i}}. (12)

To recover Theorem 1 from the above result, notice that the algorithm analyzed by Theorem 1 is captured by Theorem 2 with w t = 1 w_{t}=1 , β t \beta_{t} a constant β \beta and z t + 1 = z t − γ ​ g t z_{t+1}=z_{t}-\gamma g_{t} for all t t . Next, observe that the sequence z 1 , … , z T z_{1},\dots,z_{T} is performing online gradient descent ( Zinkevich,, 2003 ) , for which it is well-known that the regret ∑ t = 1 T ⟨ g t , z t − x ⋆ ⟩ \sum_{t=1}^{T}\langle g_{t},z_{t}-x_{\star}\rangle (appearing in the numerator of our result) is bounded by D ​ G ​ T DG\sqrt{T} and so the result of Theorem 1 immediately follows.

The regret is the principle object of study in online convex optimization ( Hazan,, 2022 ; Orabona,, 2019 ) . Viewed in this light, Theorem 2 provides a way to convert an online convex optimization algorithm into a stochastic optimization algorithm: it is a form of online-to-batch conversion ( Cesa-Bianchi et al.,, 2004 ) . Classical online-to-batch conversions are a standard technique for obtaining convergence bounds for many stochastic optimization algorithms, including stochastic gradient descent ( Zinkevich,, 2003 ) , AdaGrad ( Duchi et al.,, 2011 ) , AMSGrad ( Reddi et al.,, 2018 ) , and Adam ( Kingma and Ba,, 2014 ) . All of these algorithms can be analyzed as online convex optimization algorithms: they provide bounds on the regret ∑ t = 1 T ⟨ g t , z t − x ⋆ ⟩ \sum_{t=1}^{T}\langle g_{t},z_{t}-x_{\star}\rangle rather than direct convergence guarantees. It is then necessary (although sometimes left unstated) to convert these regret bounds into stochastic convergence guarantees via an online-to-batch conversion. Our result provides a more versatile method for effecting this conversion.

Theorem 2 actually provides a “grand unification” of a number of different online-to-batch conversions that have been proposed over the years. Most of these conversion methods were first developed specifically to provide convergence analysis for SGD (or some variant such as dual averaging or mirror descent), and then generalized into techniques that apply to any online convex optimization algorithm. For example, the classical Polyak averaging method can be generalized to form the “standard” online-to-batch conversion of Cesa-Bianchi et al., (2004) , and is immediately recovered from Theorem 2 by setting w t = 1 w_{t}=1 and β t = 0 \beta_{t}=0 for all t t . More recently Nesterov and Shikhman, (2015) ; Tao et al., (2018) derived an alternative to Polyak averaging that was later generalized to work with arbitrarily online convex optimization algorithms by Cutkosky, (2019) ; Kavis et al., (2019) , and then observed to actually be equivalent to the heavy-ball momentum by Defazio, (2020) ; Defazio and Gower, (2021) ; Defazio and Jelassi, (2022) . This method is recovered by our Theorem 2 by setting w t = 1 w_{t}=1 and β t = 1 \beta_{t}=1 for all t t . Finally, very recently Zamani and Glineur, (2023) discovered that gradient descent with a linear decay stepsize provides a last-iterate convergence guarantee, which was again generalized to an online-to-batch conversion by Defazio et al., (2023) . This final result is also recovered by Theorem 2 by setting w t = 1 w_{t}=1 and β t = t T \beta_{t}=\frac{t}{T} (see Appendix B ).

In Appendix C , we give a further tightening of Theorem 2 – it can be improved to an equality by precisely tracking additional terms that appear on the right-hand-side. This tightened version can be used to show convergence rate results for smooth losses, both with and without strong-convexity. As an example application, we show that schedule-free optimistic-gradient methods ( Rakhlin and Sridharan,, 2013 ) converge with accelerated rates: 𝔼 ⁡ [ F ⁡ ( x T ) − F ⁡ ( x ⋆ ) ] = O ⁡ ( D 2 ​ L T 2 + D ​ σ T ) . \displaystyle\mathbb{E}[F(x_{T})-F(x_{\star})]=O\left(\frac{D^{2}L}{T^{2}}+\frac{D\sigma}{\sqrt{T}}\right). (13)

### 2.2 On Large Learning Rates

Under classical worst-case convergence theory, the optimal choice of γ \gamma for a fixed duration training time T T is γ = D / ( G ​ T ) \gamma=D/(G\sqrt{T}) . This is the rate used in our bounds for Theorem 1 above. For any-time convergence (i.e. when stopping is allowed at any timestep), our proposed method can, in theory, be used with the standard learning rate sequence: γ t = D G ​ t . \displaystyle\gamma_{t}=\frac{D}{G\sqrt{t}}. (14) However, learning rate sequences of this form have poor practical performance ( Defazio et al.,, 2023 ) . Instead, much larger steps of the form D / G D/G give far better performance across virtually all problems in applications ( Defazio and Mishchenko,, 2023 ) — another theory-practice mismatch that is virtually undiscussed in the literature. Existing theory suggests that this step-size is too large to give 𝒪 ⁡ ( 1 / T ) \mathcal{O}(1/\sqrt{T}) convergence, however, as we show below, there is an important special case where such large step sizes also give optimal rates up to constant factors.

###### Theorem 3 .

Consider the online learning setting with bounded gradients g t g_{t} . Let z t + 1 = z t − γ ​ g t z_{t+1}=z_{t}-\gamma g_{t} . Let D = ‖ z 1 − z ∗ ‖ D=\left\|z_{1}-z_{*}\right\| for arbitrary reference point z ∗ z_{*} and define G = max t ≤ T ⁡ ‖ g t ‖ G=\max_{t\leq T}\left\|g_{t}\right\| . Suppose that the chosen step-size is γ = D / G \gamma=D/G , then if it holds that: ∑ t = 1 T ⟨ g t , z t − z 1 ⟩ ≤ D ​ ∑ t = 1 T ‖ g t ‖ 2 , \sum_{t=1}^{T}\left\langle g_{t},z_{t}-z_{1}\right\rangle\leq D\sqrt{\sum_{t=1}^{T}\left\|g_{t}\right\|^{2}}, (15) then: 1 T ​ ∑ t = 1 T ⟨ g t , z t − z ∗ ⟩ = 𝒪 ⁡ ( D T ​ ∑ t = 1 T ‖ g t ‖ 2 ) . \displaystyle\frac{1}{T}\sum_{t=1}^{T}\left\langle g_{t},z_{t}-z_{*}\right\rangle=\mathcal{O}\left(\frac{D}{T}\sqrt{\sum_{t=1}^{T}\left\|g_{t}\right\|^{2}}\right). (16)

This regret bound for SGD implies a convergence rate bound for Schedule-Free SGD by application of our online-to-batch conversion. Condition 15 can be checked during a training run (Using reference point z ∗ = x T z_{*}=x_{T} , and so D = ‖ x 1 − x T ‖ D=\left\|x_{1}-x_{T}\right\| ), and we find that it holds for every problem we consider in our experiments in Section 4.1 . More generally, the full conditions under which large learning rates can be used are not yet fully understood for stochastic problems. In the quadratic case, Bach and Moulines, (2013) established that large fixed step-sizes give optimal convergence rates, and we conjecture that the success of large learning rates may be attributed to asymptotic quadratic behavior of the learning process.

Empirically, we find that Schedule-Free momentum enables the use of larger learning rates γ > 0 \gamma>0 even in quadratic minimization problems f ⁡ ( x ) = 1 2 ​ x ⊤ ​ A ​ x − b ⊤ ​ x f(x)=\frac{1}{2}x^{\top}Ax-b^{\top}x . We generate 10 10 different such 20 20 -dimensional problems with eigenvalues drawn log-uniformly in [ 10 − 6 , 1 ] [10^{-6},1] . We plot the average minimal loss achieved as a function of the two parameters β \beta and γ \gamma in Figure 3 . We can see that when the learning rate we use is small, what value of β \beta we choose has little to no effect on the convergence of the algorithm. However, when γ \gamma is large, choosing β < 1 \beta<1 becomes crucial to achieving convergence.

### 2.3 How Schedule-Free Replaces a Schedule

Figure 4 illustrates the link between Polyak Averaging, Primal Averaging, Schedule-Free methods and the Linear decay schedule. Each of the averaging approaches have a crucial relationship to (worst-case optimal) Linear Decay schedules: their x x sequences simulate the effect of a Linear Decay schedule that ends at the current time-step t t , rather than the final time-step T T . This is why they can replace a schedule – they are implicitly applying one.

The four approaches differ primarily in how much each gradient contributes to the gradient location sequence y y where gradients are evaluated at each time-step, which greatly effects the stability and convergence of each method. Polyak averaging resembles the linear decay schedule’s behavior at the beginning, but near the end of training the y y sequence (blue) has much larger contributions from recent gradients. Primal averaging behaves in the opposite fashion – near the end of training it behaves similar to the Linear Decay schedules as gradients enter with a small weight, but at the early stages it significantly down-weights recent gradients, resulting in slow convergence. Schedule-Free (shown here with β = 0.6 \beta=0.6 ) remedies this down-side of Primal Averaging by modestly boosting the contribution of more recent gradients throughout all stages of training.

## 3 Related Work

The proposed method has a striking resemblance to Nesterov’s accelerated method ( Nesterov,, 1983 ; Nesterov,, 2013 ) for L L -smooth functions, which can be written in the AC-SA form ( Lan,, 2012 ) : y t \displaystyle y_{t} = ( 1 − c t + 1 ) ​ x t + c t + 1 ​ z t \displaystyle=(1-c_{t+1})x_{t}+c_{t+1}z_{t} (17) z t + 1 \displaystyle z_{t+1} = z t − k + 1 2 ​ L ∇ f ( y t ) \displaystyle=z_{t}-\frac{k+1}{2L}\nabla f(y_{t}) (18) x t + 1 \displaystyle x_{t+1} = ( 1 − c t + 1 ) ​ x t + c t + 1 ​ z t + 1 , \displaystyle=\left(1-c_{t+1}\right)x_{t}+c_{t+1}z_{t+1}, (19) where c t + 1 = 2 / ( t + 2 ) c_{t+1}=2/(t+2) . The averaging constant, and more generally c t + 1 = r + 1 t + r + 1 , c_{t+1}=\frac{r+1}{t+r+1}, (20) for any real r > − 1 r>-1 is equivalent to the weighted average ( Shamir and Zhang,, 2013 ; Defazio and Gower,, 2021 ) x t ∝ ∑ t = 1 T t r ¯ ​ z t , x_{t}\propto\sum_{t=1}^{T}t^{\bar{r}}z_{t}, where t r ¯ t^{\bar{r}} represents the r r th factorial power of t t . Our framework is compatible with factorial power averages without sacrificing theoretical guarantees.

Our approach differs from conventional accelerated methods by using a different weight for the y t y_{t} and x t x_{t} interpolations. We use a constant weight for y t y_{t} and a decreasing weight for x t x_{t} . Accelerated methods for strongly-convex problems use a constant weight for both, and those for non-strongly convex use an decreasing weight for both, so our approach doesn’t directly correspond to either class of accelerated method. Accelerated methods also use a much larger step size for the z t z_{t} sequence than our approach.

The use of equal-weighted averages is less common than the use of exponential weighting in the practical deep learning optimization literature. Exponential moving averages (EMA) of the iterate sequence are used in the popular Lookahead optimizer ( Zhang et al.,, 2019 ) . In the case of SGD, it performs i = 1 ​ … ​ k i=1\dots k inner steps: z t , i = z t , i − 1 − γ ∇ f ( z t , i − 1 ) \displaystyle z_{t,i}=z_{t,i-1}-\gamma\nabla f(z_{t,i-1}) (21) followed by an outer step: x t = x t − 1 + α ⁡ ( z t , k − x t − 1 ) . \displaystyle x_{t}=x_{t-1}+\alpha\left(z_{t,k}-x_{t-1}\right). (22) The inner optimizer then starts at z t + 1 , 0 = x t − 1 z_{t+1,0}=x_{t-1} . The Lookahead method can be seen as the EMA version of primal averaging, just as exponential weight averaging is the EMA version of Polyak-Ruppert averaging.

Tail averaging, either using an exponential moving average or an equal-weighted average, is a common ‘folk-law’ technique that often yields a practical improvement. For instance, this kind of averaging is used without citation by the influential work of Szegedy et al., (2016) : “Model evaluations are performed using a running average of the parameters computed over time.”, and by Vaswani et al., (2017) : “…averaged the last 20 checkpoints”. Tail averages are typically “Polyak-Ruppert” style averaging as the average is not used for gradient evaluations during training.

More sophisticated tail averaging approaches such as Stochastic Weight Averaging ( Izmailov et al.,, 2018 ) and LAtest Weight Averaging ( Kaddour,, 2022 ; Sanyal et al.,, 2023 ) combine averaging with large or cyclic learning rates. They are not a replacement for scheduling, instead they aim to improve final test metrics. They generally introduce additional hyper-parameters to tune, and require additional memory. It is possible to use SWA and LAWA on top of our approach, potentially giving further gains.

Sandler et al., (2023) show via a stochastic quadratic analysis framework that averaging and learning rate decreases achieve the same effective learning rate. For instance, and average of two points along the training trajectory can give almost identical results to using a learning rate two times smaller. Stochastic quadratic problems are particularly special, Bach and Moulines, (2013) have shown that Polyak averaging gives optimal 𝒪 ⁡ ( 1 / T ) \mathcal{O}(1/T) rates without the use of decreasing time-dependent step size sequences in this setting.

Within optimization theory, tail averages can be used to improve the convergence rate for stochastic non-smooth SGD in the strongly convex setting from 𝒪 ⁡ ( log ⁡ ( T ) / T ) \mathcal{O}(\log(T)/T) to 𝒪 ⁡ ( 1 / T ) \mathcal{O}(1/T) ( Rakhlin et al.,, 2012 ) , although at the expense of worse constants compared to using weighted averages of the whole sequence ( Lacoste-Julien et al.,, 2012 ) .

Portes et al., (2022) use cyclic learning rate schedules with increasing cycle periods to give a method that explores multiple points along the Pareto frontier of training time vs eval performance. Each point at the end of a cycle is an approximation to the model from a tuned schedule ending at that time. Our method gives the entire frontier, rather than just a few points along the path. In addition, our method matches or improves upon best known schedules, whereas the “… cyclic trade-off curve underestimated the standard trade-off curve by a margin of 0.5% validation accuracy” ( Portes et al.,, 2022 ) .

## 4 Experiments

To validate the effectiveness of our method, we performed a large-scale comparison across multiple domains (computer vision, language, and categorical data) and covering a range of small scale to large-scale experiments (logistic regression to large language model training). Details of the implementation of our method for SGD and Adam used in the experiments are in Section 4.4 .

### 4.1 Deep Learning Problems

For our deep learning experiments, we evaluated Schedule-Free learning on a set benchmark tasks that are commonly used in the optimization research literature: CIFAR10 A Wide ResNet (16-8) architecture ( Zagoruyko and Komodakis,, 2016 ) on the CIFAR10 image classification dataset.

A DenseNet ( Huang et al.,, 2017 ) architecture on the CIFAR-100 (100-class) classification dataset.

A deep ResNet architecture (3-96) on the Street View House Numbers (SVHN) dataset.

A standard ResNet-50 architecture ( He et al.,, 2016 ) on the ILSVRC 2012 ImageNet ( Russakovsky et al.,, 2015 ) classification dataset.

A LSTM architecture ( Wiseman and Rush,, 2016 ) on the IWSLT14 German-English translation dataset ( Cettolo et al.,, 2014 ) .

The DLRM ( Naumov et al.,, 2019 ) architecture on the Criteo Kaggle Display Advertising dataset ( Jean-Baptiste Tien,, 2014 ) .

A stacked U-Net architecture ( Sriram et al.,, 2020 ) on the fastMRI dataset ( Zbontar et al.,, 2018 ) .

Fine-tuning a pretrained Masked Autoencoder ( He et al.,, 2021 ) ViT (patch16-512d-8b) on the ILSVRC 2012 ImageNet dataset.

A 124M parameter GPT-2 ( Radford et al.,, 2019 ) style decoder-only transformer on the OpenWebText dataset ( Gokaslan and Cohen,, 2019 ) .

For each problem, both the baseline and the Schedule-Free method were tuned by sweeping both the weight decay and learning rate on a grid. We also swept β \beta over two values, 0.9 0.9 and 0.98 0.98 . Final hyper-parameters are listed in the Appendix. Schedule-Free SGD was used for CIFAR10, CIFAR100, SVHN and ImageNet, and Schedule-Free AdamW ( Loshchilov and Hutter,, 2019 ) was used for the remaining tasks. We further include a step-wise schedule as a comparison on problems where step-wise schedules are customary. Further results for Polyak and Primal averaging are in Appendix H .

Our approach shows very strong performance (Figure 5 ) out-performing existing state-of-the-art cosine schedules on CIFAR-10, CIFAR-100, SVHN, IWSLT-14 (Figure 2 ) and OpenWebText GPT-2 problems, as well as the state-of-the-art Linear Decay schedules on the fastMRI and Criteo DLRM tasks. On the remaining two problems, MAE fine-tuning and ImageNet ResNet-50 training, it ties with the existing best schedules.

In general, the optimal learning rates for the Schedule-Free variants were larger than the optimal values for the base optimizers. The ability to use larger learning rates without diverging may be a contributing factor to the faster convergence of Schedule-Free methods. The β \beta parameter works well at the default value of 0.9 0.9 for all problems except NanoGPT, where the loss started to increase rapidly when 0.9 0.9 was used (similar to the Polyak Averaging results in Appendix H ). The larger β = 0.98 \beta=0.98 value in our sweep was stable.

Schedule-Free learning works particularly well on problems that are prone to gradient norm collapse during training. As an example, when training CIFAR-10 using SGD with traditional schedule-based approaches, at the latter stages of training the training-loss goes to near-zero and the gradient norms like-wise collapse to near-zero (Figure 6 ). From this point on learning slows significantly. This happens even when weight decay is optimally tuned to give the best final test accuracy. Schedule-Free SGD in contrast does not show a collapse of either the training loss or gradient norm sequence, and continues to reliably learn. This lack-of-collapse is likely a contributing factor to the particularly good performance of Schedule-Free learning on CIFAR-10, CIFAR-100 and SVHN in our experiments.

### 4.2 MLCommons Algorithmic Efficiency benchmark

The AlgoPerf challenge ( Dahl et al.,, 2023 ) is designed to be a large-scale and comprehensive benchmark for deep learning optimization algorithms, covering major data domains and architectures. It includes Transformers, ConvNets and U-Net models across image, language, graph and speech domains, and contains 8 problems total. We evaluated Schedule-Free AdamW following the competition guidelines, comparing against NAdamW, the competition reference Algorithm, running 10 seeds of each. As this is a time-to-target competition, traditional error bars are not appropriate so we instead plot all 10 seeds separately. Note that we excluded one benchmark problem, ResNet-50 training, as neither AdamW nor NAdamW can hit the target accuracy on that task. The remaining tasks are:

WMT A Encoder-Decoder Transformer Model on the WMT17 German-to-english translation task ( Bojar et al.,, 2017 ) .

A S/16 Vision Transformer ( Dehghani et al.,, 2023 ) model on the ILSVRC 2012 ImageNet classification task ( Russakovsky et al.,, 2015 ) .

The reference U-Net architecture from the fastMRI challenge Knee MRI dataset ( Zbontar et al.,, 2018 ) .

A Conformer ( Gulati et al.,, 2020 ) Speech Recognition model on the LibriSpeech ASR dataset ( Panayotov et al.,, 2015 ) .

A Graph-Neural Network in the style of Battaglia et al., (2018) on a Molecular property prediction task from the Open Graph Benchmark ( Hu et al.,, 2020 ) suite (PubChem BioAssay data).

Clickthrough-rate prediction on the criteo 1B dataset ( Criteo,, 2022 ) using the Deep Learning Recommendation Model (DLRM) architecture.

The Deep Speech model on the LibriSpeech ASR dataset.

The self-tuning track restricts participants to provide a single set of hyper-parameters to use for all 8 problems. Given the large number of problems, this gives performance representative of a good default configuration.

Schedule-Free AdamW performs well across all considered tasks, out-performing the baseline on the WMT, VIT, FASTMRI and OGBG training, while tying on the Conformer and Criteo workloads, and marginally under-performing on the DeepSpeech workload. We attribute the performance on the Conformer and DeepSpeech tasks to their use of batch-norm - the AlgoPerf setup doesn’t easily allow us to update the BN running statistics on the x x sequence, which is necessary with our method to get the best performance (See Section 4.4 ).

### 4.3 Convex Problems

We validated the Schedule-Free learning approach on a set of standard logistic regression problems from the LibSVM repository. For each problem, and each method separately, we performed a full learning rate sweep on a power-of-two grid, and plotted mean and standard-error of the final train accuracy from 10 seeds using the best learning rate found.

Schedule-Free learning out-performs both averaging approaches and the state-of-the-art linear decay (LD) schedule baseline (Figure 8 ). It converges faster on all but 1 of 12 problems, has higher accuracy on 6 of the problems, and ties the baseline on the remaining problems. This demonstrates that the performance advantages of Schedule-Free methods are not limited to non-convex problems.

### 4.4 Implementation Concerns

The Schedule-Free variant of a method typically has the same memory requirements as the base method. For instance, Schedule-Free SGD requires no extra memory over standard SGD with momentum. Whereas SGDM tracks the current point x x and the momentum buffer m m , we can track x x and z z . The quantity y y can be computed directly from the latest values of x x and z z , and so doesn’t need to be explicitly stored. It’s also possible to instead store z z and y y , and then compute x x when needed. This low memory usage is the case for AdamW also, see Algorithm 1 .

Our efficient PyTorch implementation actually uses one buffer to always store z z and the primary parameter buffer to store either x x or y y , with the stored quantity flipping between the two for training and test/inference passes.

Our method requires extra code to handle models where batch norm is used. This is due to the fact that BatchNorm layers maintain a running_mean and running_var to track batch statistics which is calculated at y y . For model evaluation, these buffers need to be updated to match the statistics on the x x sequence. This can be done by evaluating a small number of training batches using x x right before each eval. More sophisticated approaches such as PreciseBN ( Wu and Johnson,, 2021 ) can also be used. This calculation is not needed for other normalization layers that do not use batch-statistics.

Learning rate warmup is still necessary for our method. We use a linear warmup for a fixed duration, and fuse the Adam bias-correction term into the learning rate for simplicity (this potentially impacts the effect of weight-decay during early iterations), giving a learning rate LR γ t = γ ​ 1 − β 2 t ​ min ⁡ ( 1 , t / T warmup ) \gamma_{t}=\gamma\sqrt{1-\beta_{2}^{t}}\min(1,t/T_{\text{warmup}}) that approaches γ \gamma when the warmup and bias-correction period ends. We found that performance was greatly improved by using a weighted c t c_{t} sequence when warmup is used, weighted by the square of the γ t \gamma_{t} used during warmup: c t + 1 = γ t 2 ∑ i = 1 t γ i 2 . c_{t+1}=\frac{\gamma^{2}_{t}}{\sum^{t}_{i=1}\gamma^{2}_{i}}. (23) This sequence decreases at a 1 / t 1/t rate after the learning rate warmup. It is shifted by one from the indexing used in Theorem 2 , which is done to simplify the implementation. This sequence is motivated by Theorem 2 ’s weighting sequences, which suggest weights proportional to polynomials of the learning rate.

Weight decay for Schedule-Free methods can be computed at either the y y or z z sequences. We used decay at y y for our experiments, as this matches the interpretation of weight-decay as the use of an additional L2-regularizer term in the loss. We found that computing the regularization at y y gives significantly better performance on some problems including ImageNet and NanoGPT training.

## 5 Parameter Sensitivity

For Schedule-Free learning to be truly schedule-free , it’s important that the momentum hyper-parameter doesn’t implicitly have a dependence on the time-horizon. If tuning this parameter gave different values depending on the training duration, then the problem of setting the horizon has just been shifted to setting the momentum value. In Figure 9 we run ImageNet training with Schedule-Free SGD for a longer-then-standard 200 epochs with a variety of momentum values, with the LR fixed to 1.5. We find that the best choice of momentum ( β = 0.9 \beta=0.9 ) is the same for all durations of training.

Schedule-Free learning has a similar mild time-horizon dependency for the baseline learning rate value as schedule-based approaches. Figure 10 shows that the optimal learning rate stays the same for broad range of values, for both Schedule-Free and Schedule based training. For short duration training ( ≤ 25 \leq 25 epochs), larger LR values begin to show the best performance. Appendix I shows the sensitivity of the final test accuracy to the baseline learning rate for a selection of our test problems, in comparison to the baseline optimizer with a cosine schedule. We see that the overall sensitivity is similar to the baseline optimizer in each problem.

## 6 Conclusion

Two roads diverged in a wood, and I— I took the one less traveled by, And that has made all the difference. - Robert Frost We have presented Schedule-Free learning, an optimization approach that removes the need to specify a learning rate schedule while matching or outperforming schedule-based learning. The primary practical limitation is the need to sweep learning rate and weight decay, as the best values differ from the those used with a schedule. We provide a preliminary theoretical exploration of the method, but further theory is needed to fully understand the method.

## 7 Contributions

Aaron Defazio discovered the method, led research experimentation and proved initial versions of Theorems 1 and 3 , with experimental/theoretical contributions by Alice Yang. Alice Yang led the development of the research codebase. Ashok Cutkosky proved key results including Theorem 2 and led the theoretical investigation of the method. Ahmed Khaled developed preliminary theory for obtaining accelerated rates which was later supplanted by Theorem 2 , and investigated the utility of β \beta with large learning rates for quadratics. Additional derivations by Konstantin Mishchenko and Harsh Mehta are included in appendix sections. Discussions between Aaron Defazio, Ashok Cutkosky, Konstantin Mishchenko, Harsh Mehta, and Ahmed Khaled over the last year contributed to this scientific discovery.

## References

Bach and Moulines, (2013) Bach, F. and Moulines, E. (2013). Non-strongly-convex smooth stochastic approximation with convergence rate O ⁡ ( 1 / n ) O(1/n) . In Burges, C., Bottou, L., Welling, M., Ghahramani, Z., and Weinberger, K., editors, Advances in Neural Information Processing Systems , volume 26. Curran Associates, Inc.

Battaglia et al., (2018) Battaglia, P. W., Hamrick, J. B., Bapst, V., Sanchez-Gonzalez, A., Zambaldi, V., Malinowski, M., Tacchetti, A., Raposo, D., Santoro, A., Faulkner, R., Gulcehre, C., Song, F., Ballard, A., Gilmer, J., Dahl, G., Vaswani, A., Allen, K., Nash, C., Langston, V., Dyer, C., Heess, N., Wierstra, D., Kohli, P., Botvinick, M., Vinyals, O., Li, Y., and Pascanu, R. (2018). Relational inductive biases, deep learning, and graph networks.

Bojar et al., (2017) Bojar, O., Chatterjee, R., Federmann, C., Graham, Y., Haddow, B., Huang, S., Huck, M., Koehn, P., Liu, Q., Logacheva, V., Monz, C., Negri, M., Post, M., Rubino, R., Specia, L., and Turchi, M. (2017). Findings of the 2017 conference on machine translation (wmt17). In Proceedings of the 2017 Conference on Machine Translation (WMT17) .

Cesa-Bianchi et al., (2004) Cesa-Bianchi, N., Conconi, A., and Gentile, C. (2004). On the generalization ability of on-line learning algorithms. IEEE Transactions on Information Theory , 50(9):2050–2057.

Cettolo et al., (2014) Cettolo, M., Niehues, J., Stüker, S., Bentivogli, L., and Federico, M. (2014). Report on the 11th IWSLT evaluation campaign. In IWSLT .

Chiang et al., (2012) Chiang, C.-K., Yang, T., Lee, C.-J., Mahdavi, M., Lu, C.-J., Jin, R., and Zhu, S. (2012). Online optimization with gradual variations. In Conference on Learning Theory , pages 6–1. JMLR Workshop and Conference Proceedings.

Criteo, (2022) Criteo (2022). Criteo 1TB click logs dataset. https://ailab.criteo.com/download-criteo-1tb-click-logs-dataset/ .

Cutkosky, (2019) Cutkosky, A. (2019). Anytime online-to-batch, optimism and acceleration. In International conference on machine learning , pages 1446–1454. PMLR.

Dahl et al., (2023) Dahl, G. E., Schneider, F., Nado, Z., Agarwal, N., Sastry, C. S., Hennig, P., Medapati, S., Eschenhagen, R., Kasimbeg, P., Suo, D., Bae, J., Gilmer, J., Peirson, A. L., Khan, B., Anil, R., Rabbat, M., Krishnan, S., Snider, D., Amid, E., Chen, K., Maddison, C. J., Vasudev, R., Badura, M., Garg, A., and Mattson, P. (2023). Benchmarking Neural Network Training Algorithms.

Defazio, (2020) Defazio, A. (2020). Momentum via primal averaging: Theoretical insights and learning rate schedules for non-convex optimization.

Defazio et al., (2023) Defazio, A., Cutkosky, A., Mehta, H., and Mishchenko, K. (2023). When, why and how much? adaptive learning rate scheduling by refinement.

Defazio and Gower, (2021) Defazio, A. and Gower, R. M. (2021). The power of factorial powers: New parameter settings for (stochastic) optimization. In Balasubramanian, V. N. and Tsang, I., editors, Proceedings of The 13th Asian Conference on Machine Learning , volume 157 of Proceedings of Machine Learning Research , pages 49–64. PMLR.

Defazio and Jelassi, (2022) Defazio, A. and Jelassi, S. (2022). Adaptivity without compromise: A momentumized, adaptive, dual averaged gradient method for stochastic optimization. Journal of Machine Learning Research , 23:1–34.

Defazio and Mishchenko, (2023) Defazio, A. and Mishchenko, K. (2023). Learning-rate-free learning by D-adaptation. The 40th International Conference on Machine Learning (ICML 2023) .

Dehghani et al., (2023) Dehghani, M., Djolonga, J., Mustafa, B., Padlewski, P., Heek, J., Gilmer, J., Steiner, A. P., Caron, M., Geirhos, R., Alabdulmohsin, I., Jenatton, R., Beyer, L., Tschannen, M., Arnab, A., Wang, X., Riquelme Ruiz, C., Minderer, M., Puigcerver, J., Evci, U., Kumar, M., Steenkiste, S. V., Elsayed, G. F., Mahendran, A., Yu, F., Oliver, A., Huot, F., Bastings, J., Collier, M., Gritsenko, A. A., Birodkar, V., Vasconcelos, C. N., Tay, Y., Mensink, T., Kolesnikov, A., Pavetic, F., Tran, D., Kipf, T., Lucic, M., Zhai, X., Keysers, D., Harmsen, J. J., and Houlsby, N. (2023). Scaling vision transformers to 22 billion parameters. In Krause, A., Brunskill, E., Cho, K., Engelhardt, B., Sabato, S., and Scarlett, J., editors, Proceedings of the 40th International Conference on Machine Learning , volume 202 of Proceedings of Machine Learning Research , pages 7480–7512. PMLR.

Duchi et al., (2011) Duchi, J., Hazan, E., and Singer, Y. (2011). Adaptive subgradient methods for online learning and stochastic optimization. Journal of Machine Learning Research , 12(61).

Gokaslan and Cohen, (2019) Gokaslan, A. and Cohen, V. (2019). Openwebtext corpus. http://Skylion007.github.io/OpenWebTextCorpus .

Gulati et al., (2020) Gulati, A., Qin, J., Chiu, C.-C., Parmar, N., Zhang, Y., Yu, J., Han, W., Wang, S., Zhang, Z., Wu, Y., and Pang, R. (2020). Conformer: Convolution-augmented transformer for speech recognition.

Hazan, (2022) Hazan, E. (2022). Introduction to online convex optimization . MIT Press.

Hazan and Kale, (2010) Hazan, E. and Kale, S. (2010). Extracting certainty from uncertainty: Regret bounded by variation in costs. Machine learning , 80:165–188.

He et al., (2021) He, K., Chen, X., Xie, S., Li, Y., Dollár, P., and Girshick, R. (2021). Masked autoencoders are scalable vision learners. arXiv:2111.06377 .

He et al., (2016) He, K., Zhang, X., Ren, S., and Sun, J. (2016). Deep residual learning for image recognition. In Proceedings of the IEEE conference on computer vision and pattern recognition .

Hu et al., (2020) Hu, W., Fey, M., Zitnik, M., Dong, Y., Ren, H., Liu, B., Catasta, M., and Leskovec, J. (2020). Open graph benchmark: datasets for machine learning on graphs. In Proceedings of the 34th International Conference on Neural Information Processing Systems .

Huang et al., (2017) Huang, G., Liu, Z., Van Der Maaten, L., and Weinberger, K. Q. (2017). Densely connected convolutional networks. In 2017 IEEE Conference on Computer Vision and Pattern Recognition (CVPR) , pages 2261–2269.

Izmailov et al., (2018) Izmailov, P., Podoprikhin, D., Garipov, T., Vetrov, D., and Wilson, A. G. (2018). Averaging weights leads to wider optima and better generalization. In Conference on Uncertainty in Artificial Intelligence (UAI) .

Jean-Baptiste Tien, (2014) Jean-Baptiste Tien, joycenv, O. C. (2014). Display advertising challenge.

Joulani et al., (2017) Joulani, P., György, A., and Szepesvári, C. (2017). A modular analysis of adaptive (non-) convex optimization: Optimism, composite objectives, and variational bounds. In International Conference on Algorithmic Learning Theory , pages 681–720. PMLR.

Joulani et al., (2020) Joulani, P., Raj, A., Gyorgy, A., and Szepesvári, C. (2020). A simpler approach to accelerated optimization: iterative averaging meets optimism. In International conference on machine learning , pages 4984–4993. PMLR.

Kaddour, (2022) Kaddour, J. (2022). Stop wasting my time! saving days of ImageNet and BERT training with latest weight averaging.

Kavis et al., (2019) Kavis, A., Levy, K. Y., Bach, F., and Cevher, V. (2019). UniXGrad: A universal, adaptive algorithm with optimal guarantees for constrained optimization. Advances in neural information processing systems , 32.

Kingma and Ba, (2014) Kingma, D. P. and Ba, J. (2014). Adam: a method for stochastic optimization. In International Conference on Learning Representations .

Lacoste-Julien et al., (2012) Lacoste-Julien, S., Schmidt, M., and Bach, F. (2012). A simpler approach to obtaining an o ⁡ ( 1 / t ) o(1/t) convergence rate for the projected stochastic subgradient method.

Lan, (2012) Lan, G. (2012). An optimal method for stochastic composite optimization. Mathematical Programming , 133(1):365–397.

Loshchilov and Hutter, (2019) Loshchilov, I. and Hutter, F. (2019). Decoupled weight decay regularization. In International Conference on Learning Representations .

Naumov et al., (2019) Naumov, M., Mudigere, D., Shi, H. M., Huang, J., Sundaraman, N., Park, J., Wang, X., Gupta, U., Wu, C., Azzolini, A. G., Dzhulgakov, D., Mallevich, A., Cherniavskii, I., Lu, Y., Krishnamoorthi, R., Yu, A., Kondratenko, V., Pereira, S., Chen, X., Chen, W., Rao, V., Jia, B., Xiong, L., and Smelyanskiy, M. (2019). Deep learning recommendation model for personalization and recommendation systems. CoRR .

Nesterov, (1983) Nesterov, Y. (1983). A method for solving a convex programming problem with convergence rate O ⁡ ( 1 / k 2 ) O(1/k^{2}) . Soviet Mathematics Doklady .

Nesterov, (2013) Nesterov, Y. (2013). Lectures on Convex Optimization . Springer Nature.

Nesterov and Shikhman, (2015) Nesterov, Y. and Shikhman, V. (2015). Quasi-monotone subgradient methods for nonsmooth convex minimization. Journal of Optimization Theory and Applications , 165(3):917–940.

Orabona, (2019) Orabona, F. (2019). A modern introduction to online learning. arXiv preprint arXiv:1912.13213 .

Panayotov et al., (2015) Panayotov, V., Chen, G., Povey, D., and Khudanpur, S. (2015). Librispeech: An asr corpus based on public domain audio books. In 2015 IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP) , pages 5206–5210.

Polyak, (1990) Polyak, B. (1990). New stochastic approximation type procedures. Avtomatica i Telemekhanika , 7:98–107.

Portes et al., (2022) Portes, J., Blalock, D., Stephenson, C., and Frankle, J. (2022). Fast benchmarking of accuracy vs. training time with cyclic learning rates.

Radford et al., (2019) Radford, A., Wu, J., Child, R., Luan, D., Amodei, D., and Sutskever, I. (2019). Language models are unsupervised multitask learners. Technical report, OpenAI.

Rakhlin et al., (2012) Rakhlin, A., Shamir, O., and Sridharan, K. (2012). Making gradient descent optimal for strongly convex stochastic optimization. In Proceedings of the 29th International Coference on International Conference on Machine Learning .

Rakhlin and Sridharan, (2013) Rakhlin, A. and Sridharan, K. (2013). Online learning with predictable sequences. In Conference on Learning Theory , pages 993–1019. PMLR.

Reddi et al., (2018) Reddi, S. J., Kale, S., and Kumar, S. (2018). On the convergence of Adam and beyond. In International Conference on Learning Representations .

Ruppert, (1988) Ruppert, D. (1988). Efficient estimations from a slowly convergent Robbins-Monro process. Technical Report, Cornell University .

Russakovsky et al., (2015) Russakovsky, O., Deng, J., Su, H., Krause, J., Satheesh, S., Ma, S., Huang, Z., Karpathy, A., Khosla, A., Bernstein, M., Berg, A. C., and Fei-Fei, L. (2015). ImageNet Large Scale Visual Recognition Challenge. International Journal of Computer Vision (IJCV) , 115(3).

Sandler et al., (2023) Sandler, M., Zhmoginov, A., Vladymyrov, M., and Miller, N. (2023). Training trajectories, mini-batch losses and the curious role of the learning rate.

Sanyal et al., (2023) Sanyal, S., Neerkaje, A., Kaddour, J., Kumar, A., and Sanghavi, S. (2023). Early weight averaging meets high learning rates for LLM pre-training.

Sebbouh et al., (2021) Sebbouh, O., Gower, R. M., and Defazio, A. (2021). On the (asymptotic) convergence of stochastic gradient descent and stochastic heavy ball. In Conference on Learning Theory, COLT 2021 , Proceedings of Machine Learning Research. PMLR.

Shamir and Zhang, (2013) Shamir, O. and Zhang, T. (2013). Stochastic gradient descent for non-smooth optimization: Convergence results and optimal averaging schemes. In Proceedings of the 30th International Conference on Machine Learning .

Sriram et al., (2020) Sriram, A., Zbontar, J., Murrell, T., Defazio, A., Zitnick, C. L., Yakubova, N., Knoll, F., and Johnson, P. (2020). End-to-end variational networks for accelerated MRI reconstruction. In International Conference on Medical Image Computing and Computer-Assisted Intervention . Springer.

Sutskever et al., (2013) Sutskever, I., Martens, J., Dahl, G., and Hinton, G. E. (2013). On the importance of initialization and momentum in deep learning. In Proceedings of the 30th International Conference on International Conference on Machine Learning - Volume 28 . JMLR.org.

Szegedy et al., (2016) Szegedy, C., Vanhoucke, V., Ioffe, S., Shlens, J., and Wojna, Z. (2016). Rethinking the inception architecture for computer vision. In 2016 IEEE Conference on Computer Vision and Pattern Recognition (CVPR) , pages 2818–2826.

Tao et al., (2018) Tao, W., Pan, Z., Wu, G., and Tao, Q. (2018). Primal averaging: A new gradient evaluation step to attain the optimal individual convergence. IEEE Transactions on Cybernetics , PP:1–11.

Vaswani et al., (2017) Vaswani, A., Shazeer, N., Parmar, N., Uszkoreit, J., Jones, L., Gomez, A. N., Kaiser, L. u., and Polosukhin, I. (2017). Attention is all you need. In Guyon, I., Luxburg, U. V., Bengio, S., Wallach, H., Fergus, R., Vishwanathan, S., and Garnett, R., editors, Advances in Neural Information Processing Systems , volume 30. Curran Associates, Inc.

Wiseman and Rush, (2016) Wiseman, S. and Rush, A. M. (2016). Sequence-to-sequence learning as beam-search optimization. In Proceedings of the 2016 Conference on Empirical Methods in Natural Language Processing . Association for Computational Linguistics.

Wu and Johnson, (2021) Wu, Y. and Johnson, J. (2021). Rethinking "batch" in batchnorm.

Zagoruyko and Komodakis, (2016) Zagoruyko, S. and Komodakis, N. (2016). Wide residual networks. In Proceedings of the British Machine Vision Conference (BMVC) .

Zamani and Glineur, (2023) Zamani, M. and Glineur, F. (2023). Exact convergence rate of the last iterate in subgradient methods.

Zbontar et al., (2018) Zbontar, J., Knoll, F., Sriram, A., Muckley, M. J., Bruno, M., Defazio, A., Parente, M., Geras, K. J., Katsnelson, J., Chandarana, H., et al. (2018). fastMRI: An open dataset and benchmarks for accelerated MRI. arXiv preprint arXiv:1811.08839 .

Zhang et al., (2019) Zhang, M., Lucas, J., Ba, J., and Hinton, G. E. (2019). Lookahead optimizer: k k steps forward, 1 step back. In Wallach, H., Larochelle, H., Beygelzimer, A., d'Alché-Buc, F., Fox, E., and Garnett, R., editors, Advances in Neural Information Processing Systems , volume 32. Curran Associates, Inc.

Zinkevich, (2003) Zinkevich, M. (2003). Online convex programming and generalized infinitesimal gradient ascent. In Proceedings of the Twentieth International Conference on International Conference on Machine Learning , pages 928–935.

## Appendix A Proof of Theorem 2

See 2

###### Proof.

Throughout this proof, we will use the notation w 1 : t = ∑ i = 1 t w i w_{1:t}=\sum_{i=1}^{t}w_{i} . The result is established by showing the following identity: w 1 : t F ( x t ) − w 1 : t − 1 F ( x t − 1 ) − w t F ( x ⋆ ) \displaystyle w_{1:t}F(x_{t})-w_{1:t-1}F(x_{t-1})-w_{t}F(x_{\star}) ≤ w t ​ ⟨ ∇ F ​ ( y t ) , z t − x ⋆ ⟩ . \displaystyle\leq w_{t}\langle\nabla F(y_{t}),z_{t}-x_{\star}\rangle. (24) Where here ∇ F ​ ( y t ) \nabla F(y_{t}) indicates a subgradient of F F at y t y_{t} with 𝔼 ⁡ [ g t | z t ] = ∇ F ​ ( y t ) \mathbb{E}[g_{t}|z_{t}]=\nabla F(y_{t}) . Given the identity ( 24 ), we sum over all t t from 1 to T T . Then the LHS will telescope to obtain: w 1 : T ( F ( x T ) − F ( x ⋆ ) ) \displaystyle w_{1:T}(F(x_{T})-F(x_{\star})) ≤ ∑ t = 1 T w t ​ ⟨ ∇ F ​ ( y t ) , z t − x ⋆ ⟩ , \displaystyle\leq\sum_{t=1}^{T}w_{t}\langle\nabla F(y_{t}),z_{t}-x_{\star}\rangle, from which the conclusion immediately follows since 𝔼 ⁡ [ g t | z t ] = ∇ F ​ ( y t ) \mathbb{E}[g_{t}|z_{t}]=\nabla F(y_{t}) . So, let us establish ( 24 ). To do so, it will help to observe the following identities: w t ​ z t \displaystyle w_{t}z_{t} = w 1 : t x t − w 1 : t − 1 x t − 1 \displaystyle=w_{1:t}x_{t}-w_{1:t-1}x_{t-1} w 1 : t − 1 ( x t − x t − 1 ) \displaystyle w_{1:t-1}(x_{t}-x_{t-1}) = w t ​ ( z t − x t ) \displaystyle=w_{t}(z_{t}-x_{t}) (25) z t − y t \displaystyle z_{t}-y_{t} = β t 1 − β t ​ ( y t − x t ) . \displaystyle=\frac{\beta_{t}}{1-\beta_{t}}(y_{t}-x_{t}). (26) Now, setting ∇ F ​ ( x t ) \nabla F(x_{t}) to be an arbitrary subgradient of F F at x t x_{t} , we have: w 1 : t F ( x t ) − w 1 : t − 1 F ( x t − 1 ) − w t F ( x ⋆ ) \displaystyle w_{1:t}F(x_{t})-w_{1:t-1}F(x_{t-1})-w_{t}F(x_{\star}) = w 1 : t − 1 ( F ( x t ) − F ( x t − 1 ) ) + w t ( F ( x t ) − F ( x ⋆ ) ) \displaystyle=w_{1:t-1}(F(x_{t})-F(x_{t-1}))+w_{t}(F(x_{t})-F(x_{\star})) ≤ w 1 : t − 1 ⟨ ∇ F ( x t ) , x t − x t − 1 ⟩ + w t ( F ( x t ) − F ( x ⋆ ) ) \displaystyle\leq w_{1:t-1}\langle\nabla F(x_{t}),x_{t}-x_{t-1}\rangle+w_{t}(F(x_{t})-F(x_{\star})) using ( 25 ): = w t ​ ⟨ ∇ F ​ ( x t ) , z t − x t ⟩ + w t ​ ( F ⁡ ( x t ) − F ⁡ ( x ⋆ ) ) \displaystyle=w_{t}\langle\nabla F(x_{t}),z_{t}-x_{t}\rangle+w_{t}(F(x_{t})-F(x_{\star})) = w t ​ ⟨ ∇ F ​ ( x t ) , z t − x t ⟩ + w t ​ ( F ⁡ ( x t ) − F ⁡ ( y t ) ) + w t ​ ( F ⁡ ( y t ) − F ⁡ ( x ⋆ ) ) \displaystyle=w_{t}\langle\nabla F(x_{t}),z_{t}-x_{t}\rangle+w_{t}(F(x_{t})-F(y_{t}))+w_{t}(F(y_{t})-F(x_{\star})) ≤ w t ​ ⟨ ∇ F ​ ( x t ) , z t − x t ⟩ + w t ​ ⟨ ∇ F ​ ( x t ) , x t − y t ⟩ + w t ​ ⟨ ∇ F ​ ( y t ) , y t − x ⋆ ⟩ \displaystyle\leq w_{t}\langle\nabla F(x_{t}),z_{t}-x_{t}\rangle+w_{t}\langle\nabla F(x_{t}),x_{t}-y_{t}\rangle+w_{t}\langle\nabla F(y_{t}),y_{t}-x_{\star}\rangle = w t ​ ⟨ ∇ F ​ ( x t ) − ∇ F ​ ( y t ) , z t − y t ⟩ + w t ​ ⟨ ∇ F ​ ( y t ) , z t − x ⋆ ⟩ \displaystyle=w_{t}\langle\nabla F(x_{t})-\nabla F(y_{t}),z_{t}-y_{t}\rangle+w_{t}\langle\nabla F(y_{t}),z_{t}-x_{\star}\rangle using ( 26 ): = w t ​ β t 1 − β t ​ ⟨ ∇ F ​ ( x t ) − ∇ F ​ ( y t ) , y t − x t ⟩ + w t ​ ⟨ ∇ F ​ ( y t ) , z t − x ⋆ ⟩ \displaystyle=w_{t}\frac{\beta_{t}}{1-\beta_{t}}\langle\nabla F(x_{t})-\nabla F(y_{t}),y_{t}-x_{t}\rangle+w_{t}\langle\nabla F(y_{t}),z_{t}-x_{\star}\rangle Finally, recall that any convex function satisfies ⟨ ∇ F ​ ( b ) − ∇ F ​ ( a ) , a − b ⟩ ≤ 0 \langle\nabla F(b)-\nabla F(a),a-b\rangle\leq 0 for all a , b a,b . This classical fact can be established by adding the following two subgradient identities: F ⁡ ( a ) ≥ F ⁡ ( b ) + ⟨ ∇ F ​ ( b ) , a − b ⟩ , \displaystyle F(a)\geq F(b)+\langle\nabla F(b),a-b\rangle, F ⁡ ( b ) ≥ F ⁡ ( a ) + ⟨ ∇ F ​ ( a ) , b − a ⟩ . \displaystyle F(b)\geq F(a)+\langle\nabla F(a),b-a\rangle. Then, since β t ∈ [ 0 , 1 ] \beta_{t}\in[0,1] , we have w t ​ β t 1 − β t ​ ⟨ ∇ F ​ ( x t ) − ∇ F ​ ( y t ) , y t − x t ⟩ ≤ 0 w_{t}\frac{\beta_{t}}{1-\beta_{t}}\langle\nabla F(x_{t})-\nabla F(y_{t}),y_{t}-x_{t}\rangle\leq 0 , which establishes the desired identity ( 24 ). ∎

## Appendix B Recovering Prior Conversions, and Connections to Momentum

The following recursions provide an equivalent update to our main algorithm that casts the update in a more “momentum-like” form.

###### Theorem 4 .

Under the same assumptions and notation as Theorem 2 , set: Δ t \displaystyle\Delta_{t} = z t + 1 − z t , \displaystyle=z_{t+1}-z_{t}, m t \displaystyle m_{t} = x t + 1 − x t , \displaystyle=x_{t+1}-x_{t}, u t \displaystyle u_{t} = y t + 1 − y t . \displaystyle=y_{t+1}-y_{t}. Then: m t \displaystyle m_{t} = w t + 1 w 1 : t − 1 w t w 1 : t + 1 m t − 1 + w t + 1 w 1 : t + 1 Δ t \displaystyle=\frac{w_{t+1}w_{1:t-1}}{w_{t}w_{1:t+1}}m_{t-1}+\frac{w_{t+1}}{w_{1:t+1}}\Delta_{t} u t \displaystyle u_{t} = ( β t + ( β t − β t + 1 ) w 1 : t w t + 1 ) m t + ( 1 − β t ) Δ t . \displaystyle=\left(\beta_{t}+(\beta_{t}-\beta_{t+1})\frac{w_{1:t}}{w_{t+1}}\right)m_{t}+(1-\beta_{t})\Delta_{t}.

Here u t u_{t} is playing the role of the “update vector”, as the sequence of points y t y_{t} are where we will be evaluating gradients. The Δ t \Delta_{t} value can be interpreted as a “base update” value: for the case that the z t z_{t} sequence is specified by SGD (as in Theorem 1 ), Δ t = − η ​ g t \Delta_{t}=-\eta g_{t} . Thus, the update can be interpreted as a momentum term m t m_{t} , plus an extra “push” in the direction of Δ t \Delta_{t} scaled by 1 − β t 1-\beta_{t} .

###### Proof.

Let’s solve for m t m_{t} in terms of previous values: m t \displaystyle m_{t} = x t + 1 − x t \displaystyle=x_{t+1}-x_{t} = w t + 1 w 1 : t + 1 ( z t + 1 − x t ) \displaystyle=\frac{w_{t+1}}{w_{1:t+1}}(z_{t+1}-x_{t}) = w t + 1 w 1 : t + 1 ( Δ t + z t − x t ) \displaystyle=\frac{w_{t+1}}{w_{1:t+1}}(\Delta_{t}+z_{t}-x_{t}) = w t + 1 w 1 : t + 1 ( Δ t + w 1 : t − 1 w t ( x t − x t − 1 ) ) \displaystyle=\frac{w_{t+1}}{w_{1:t+1}}(\Delta_{t}+\frac{w_{1:t-1}}{w_{t}}(x_{t}-x_{t-1})) = w t + 1 w 1 : t − 1 w t w 1 : t + 1 m t − 1 + w t + 1 w 1 : t + 1 Δ t . \displaystyle=\frac{w_{t+1}w_{1:t-1}}{w_{t}w_{1:t+1}}m_{t-1}+\frac{w_{t+1}}{w_{1:t+1}}\Delta_{t}.

Now let’s solve for u t u_{t} : u t \displaystyle u_{t} = β t + 1 ​ x t + 1 + ( 1 − β t + 1 ) ​ z t + 1 − β t ​ x t − ( 1 − β t ) ​ z t \displaystyle=\beta_{t+1}x_{t+1}+(1-\beta_{t+1})z_{t+1}-\beta_{t}x_{t}-(1-\beta_{t})z_{t} = β t ​ m t + ( 1 − β t ) ​ Δ t + ( β t − β t + 1 ) ​ ( z t + 1 − x t + 1 ) \displaystyle=\beta_{t}m_{t}+(1-\beta_{t})\Delta_{t}+(\beta_{t}-\beta_{t+1})(z_{t+1}-x_{t+1}) = β t m t + ( 1 − β t ) Δ t + ( β t − β t + 1 ) w 1 : t w t + 1 ( x t + 1 − x t ) \displaystyle=\beta_{t}m_{t}+(1-\beta_{t})\Delta_{t}+(\beta_{t}-\beta_{t+1})\frac{w_{1:t}}{w_{t+1}}(x_{t+1}-x_{t}) = β t m t + ( 1 − β t ) Δ t + ( β t − β t + 1 ) w 1 : t w t + 1 m t \displaystyle=\beta_{t}m_{t}+(1-\beta_{t})\Delta_{t}+(\beta_{t}-\beta_{t+1})\frac{w_{1:t}}{w_{t+1}}m_{t} = ( β t + ( β t − β t + 1 ) w 1 : t w t + 1 ) m t + ( 1 − β t ) Δ t \displaystyle=\left(\beta_{t}+(\beta_{t}-\beta_{t+1})\frac{w_{1:t}}{w_{t+1}}\right)m_{t}+(1-\beta_{t})\Delta_{t} ∎

In the special case that w t = 1 w_{t}=1 for all t t , the updates simplify to: m t \displaystyle m_{t} = t − 1 t + 1 ​ m t − 1 + 1 t + 1 ​ Δ t \displaystyle=\frac{t-1}{t+1}m_{t-1}+\frac{1}{t+1}\Delta_{t} u t \displaystyle u_{t} = ( β t + t ⁡ ( β t − β t + 1 ) ) ​ m t + ( 1 − β t ) ​ Δ t . \displaystyle=\left(\beta_{t}+t(\beta_{t}-\beta_{t+1})\right)m_{t}+(1-\beta_{t})\Delta_{t}. In the special case that β t = β \beta_{t}=\beta for all t t , the update for u t u_{t} simplifies to: u t = β ​ m t + ( 1 − β ) ​ Δ t . \displaystyle u_{t}=\beta m_{t}+(1-\beta)\Delta_{t}. From this, it is clear that if β = 1 \beta=1 and w t = 1 w_{t}=1 , then we recover the standard Polyak momentum with a time-varying momentum factor m t = t − 1 t + 1 ​ m t − 1 + 1 t + 1 ​ Δ t m_{t}=\frac{t-1}{t+1}m_{t-1}+\frac{1}{t+1}\Delta_{t} , while if β = 0 \beta=0 , then we have ordinary SGD without momentum.

### B.1 Recovering Linear Decay

Let’s take a look at the update for u t = y t + 1 − y t u_{t}=y_{t+1}-y_{t} in the special case that w t = 1 w_{t}=1 for all t t : u t = ( β t + t ⁡ ( β t − β t + 1 ) ) ​ m t + ( 1 − β t ) ​ Δ t . \displaystyle u_{t}=\left(\beta_{t}+t(\beta_{t}-\beta_{t+1})\right)m_{t}+(1-\beta_{t})\Delta_{t}. Let us define α t = 1 − β t \alpha_{t}=1-\beta_{t} . Then we can re-write this update as: u t = ( 1 − α t + t ⁡ ( α t + 1 − α t ) ) ​ m t + α t ​ Δ t . \displaystyle u_{t}=\left(1-\alpha_{t}+t(\alpha_{t+1}-\alpha_{t})\right)m_{t}+\alpha_{t}\Delta_{t}. It looks like we might be able to set α t \alpha_{t} such that the coefficient of m t m_{t} vanishes. In this case, α t \alpha_{t} would play the role of a “schedule” as the update would just be u t = α t ​ Δ t u_{t}=\alpha_{t}\Delta_{t} . Solving the recursion we get: α t − 1 = t ⁡ ( α t + 1 − α t ) , \displaystyle\alpha_{t}-1=t(\alpha_{t+1}-\alpha_{t}), α t + 1 = ( t + 1 ) ​ α t − 1 t . \displaystyle\alpha_{t+1}=\frac{(t+1)\alpha_{t}-1}{t}. Amazingly, this recursion is satisfied by α t = T − t T \alpha_{t}=\frac{T-t}{T} , which is the linear decay schedule! Notably, this schedule has α T = 0 \alpha_{T}=0 , which in turn implies that y T = x T y_{T}=x_{T} , so that the last iterate of our algorithm is x T x_{T} , for which Theorem 2 provides a convergence guarantee.

The recursion is also satisfied by α t = 1 \alpha_{t}=1 for all t t (which recovers standard Polyak-Ruppert averaging). Notably, this recursion shows that α 1 \alpha_{1} will determine all subsequent α \alpha values. The values will decease linearly to zero, and then they will try to go negative, which is not allowed. So the linear decay schedule is the value of α 1 \alpha_{1} that is “just barely” allowed since it hits zero at α T \alpha_{T} .

In general with arbitrary w t w_{t} , the recursion is: 1 − α t + ( α t + 1 − α t ) w 1 : t w t + 1 = 0 . \displaystyle 1-\alpha_{t}+(\alpha_{t+1}-\alpha_{t})\frac{w_{1:t}}{w_{t+1}}=0. If we insist that α T = 0 \alpha_{T}=0 (so that y T = x T y_{T}=x_{T} and we get a “last iterate” guarantee), then solving the recursion yields: α t = w t + 1 : T w 1 : T , \displaystyle\alpha_{t}=\frac{w_{t+1:T}}{w_{1:T}}, which exactly recovers the main result of Defazio et al., (2023) .

## Appendix C Generalizing Theorem 2 via Bregman Divergences

Here, we provide a generalized version of Theorem 2 in the style of Joulani et al., (2020) . This result employs Bregman divergences to tighten the inequality of Theorem 2 to an equality.

###### Theorem 5 .

Let F F be a convex function. Let ζ 1 , … , ζ T \zeta_{1},\dots,\zeta_{T} be a sequence of i.i.d. random variables, and let g g be a function such that 𝔼 ⁡ [ g ⁡ ( x , ζ t ) ] ∈ ∂ F ⁡ ( x ) \mathbb{E}[g(x,\zeta_{t})]\in\partial F(x) for all x x and t t . Let z 1 , … , z T z_{1},\dots,z_{T} be arbitrary vectors and let w 1 , … , w T w_{1},\dots,w_{T} and α 1 , … , α T \alpha_{1},\dots,\alpha_{T} be arbitrary non-negative real numbers with α t ≤ 1 \alpha_{t}\leq 1 such that z t z_{t} , w t w_{t} and α t \alpha_{t} are independent of ζ t , … , ζ T \zeta_{t},\dots,\zeta_{T} . Define the Bregman divergence of F F as B F ​ ( a , b ) = F ⁡ ( a ) − F ⁡ ( b ) − ⟨ ∇ F ​ ( b ) , a − b ⟩ B_{F}(a,b)=F(a)-F(b)-\langle\nabla F(b),a-b\rangle 2 2 2 if F F is not differentiable, then by abuse of notation define ∇ F ​ ( b ) = 𝔼 ​ [ g ​ ( b , ζ ) ] \nabla F(b)=\mathbb{E}[g(b,\zeta)] , which is a particular choice of subgradient of F F . . Set: x t \displaystyle x_{t} = ∑ i = 1 t w i ​ z i ∑ i = 1 t w i = x t − 1 ​ ( 1 − w t ∑ i = 1 t w i ) + w i ∑ i = 1 t w i ​ z t \displaystyle=\frac{\sum_{i=1}^{t}w_{i}z_{i}}{\sum_{i=1}^{t}w_{i}}=x_{t-1}\left(1-\frac{w_{t}}{\sum_{i=1}^{t}w_{i}}\right)+\frac{w_{i}}{\sum_{i=1}^{t}w_{i}}z_{t} y t \displaystyle y_{t} = ( 1 − α t ) ​ x t + α t ​ z t \displaystyle=(1-\alpha_{t})x_{t}+\alpha_{t}z_{t} g t \displaystyle g_{t} = g ⁡ ( y t , ζ t ) . \displaystyle=g(y_{t},\zeta_{t}). Define the “compressed sum” notation: w 1 : t = ∑ i = 1 t w i w_{1:t}=\sum_{i=1}^{t}w_{i} , with w 1 : 0 = 0 w_{1:0}=0 .

Then we have for all x ⋆ x_{\star} : 𝔼 ⁡ [ F ⁡ ( x T ) − F ⁡ ( x ⋆ ) ] \displaystyle\mathbb{E}[F(x_{T})-F(x_{\star})] = 𝔼 [ ∑ t = 1 T w t ​ ⟨ g t , z t − x ⋆ ⟩ w 1 : T ] \displaystyle=\mathbb{E}\left[\frac{\sum_{t=1}^{T}w_{t}\langle g_{t},z_{t}-x_{\star}\rangle}{w_{1:T}}\right] − 𝔼 [ ∑ t = 1 T w t α t ​ B F ​ ( y t , x t ) + w t ​ ( 1 − α t ) α t ​ B F ​ ( x t , y t ) w 1 : T ] \displaystyle\qquad-\mathbb{E}\left[\frac{\sum_{t=1}^{T}\frac{w_{t}}{\alpha_{t}}B_{F}(y_{t},x_{t})+\frac{w_{t}(1-\alpha_{t})}{\alpha_{t}}B_{F}(x_{t},y_{t})}{w_{1:T}}\right] − 𝔼 [ ∑ t = 1 T w 1 : t − 1 B F ( x t − 1 , x t ) + w t B F ( x ⋆ , y t ) w 1 : T ] . \displaystyle\qquad-\mathbb{E}\left[\frac{\sum_{t=1}^{T}w_{1:t-1}B_{F}(x_{t-1},x_{t})+w_{t}B_{F}(x_{\star},y_{t})}{w_{1:T}}\right].

Let’s take a minute to unpack this result since it is depressingly complicated. Recall that the Bregman divergence for a convex function must be positive, and so all the subtracted Bregman divergence terms can be dropped to make the bound only looser. This recovers Theorem 2 . However, in Section D , we show how to exploit the negative Bregman terms to achieve accelerated rates when F F is smooth, and in Section E we show how to exploit the negative Bregman terms to achieve faster rates when F F is strongly-convex.

###### Proof.

The proof is nearly the same as that of Theorem 2 . The only difference is that we keep track of all the error terms in the inequalities via Bregman divergences.

Throughout this proof, we use ∇ F ​ ( x ) \nabla F(x) to indicate 𝔼 ζ ​ [ g ​ ( x , ζ ) ] \mathbb{E}_{\zeta}[g(x,\zeta)] . When F F is differentiable, this is simply the ordinary gradient at x x . When F F is non-differentiable, this reprents a specific choice of subgradient at x x .

Recall that any convex function satisfies ⟨ ∇ F ​ ( b ) − ∇ F ​ ( a ) , a − b ⟩ = − B F ​ ( a , b ) − B F ​ ( b , a ) \langle\nabla F(b)-\nabla F(a),a-b\rangle=-B_{F}(a,b)-B_{F}(b,a) for all a , b a,b . This classical fact can be established by adding the following two subgradient identities: F ⁡ ( a ) = F ⁡ ( b ) + ⟨ ∇ F ​ ( b ) , a − b ⟩ + B F ​ ( a , b ) \displaystyle F(a)=F(b)+\langle\nabla F(b),a-b\rangle+B_{F}(a,b) F ⁡ ( b ) = F ⁡ ( a ) + ⟨ ∇ F ​ ( a ) , b − a ⟩ + B F ​ ( b , a ) \displaystyle F(b)=F(a)+\langle\nabla F(a),b-a\rangle+B_{F}(b,a) ⟨ ∇ F ​ ( b ) − ∇ F ​ ( a ) , a − b ⟩ = − B F ​ ( a , b ) − B F ​ ( b , a ) . \displaystyle\langle\nabla F(b)-\nabla F(a),a-b\rangle=-B_{F}(a,b)-B_{F}(b,a). (27)

The Theorem is established by showing the following identity: w 1 : t F ( x t ) − w 1 : t − 1 F ( x t − 1 ) − w t F ( x ⋆ ) \displaystyle w_{1:t}F(x_{t})-w_{1:t-1}F(x_{t-1})-w_{t}F(x_{\star}) = w t ​ ⟨ ∇ F ​ ( y t ) , z t − x ⋆ ⟩ \displaystyle=w_{t}\langle\nabla F(y_{t}),z_{t}-x_{\star}\rangle − w t α t ​ B F ​ ( y t , x t ) − w t ​ ( 1 − α t ) α t ​ B F ​ ( x t , y t ) \displaystyle\qquad-\frac{w_{t}}{\alpha_{t}}B_{F}(y_{t},x_{t})-\frac{w_{t}(1-\alpha_{t})}{\alpha_{t}}B_{F}(x_{t},y_{t}) − w 1 : t − 1 B F ( x t − 1 , x t ) − w t B F ( x ⋆ , y t ) . \displaystyle\qquad-w_{1:t-1}B_{F}(x_{t-1},x_{t})-w_{t}B_{F}(x_{\star},y_{t}). (28) Given the identity ( 28 ), we sum over all t t from 1 to T T . Then the LHS will telescope to obtain: w 1 : T ( F ( x T ) − F ( x ⋆ ) ) \displaystyle w_{1:T}(F(x_{T})-F(x_{\star})) = ∑ t = 1 T w t ​ ⟨ ∇ F ​ ( y t ) , z t − x ⋆ ⟩ \displaystyle=\sum_{t=1}^{T}w_{t}\langle\nabla F(y_{t}),z_{t}-x_{\star}\rangle − ∑ t = 1 T w t α t B F ( y t , x t ) − w t ​ ( 1 − α t ) α t B F ( x t , y t ) \displaystyle\qquad-\sum_{t=1}^{T}\frac{w_{t}}{\alpha_{t}}B_{F}(y_{t},x_{t})-\frac{w_{t}(1-\alpha_{t})}{\alpha_{t}}B_{F}(x_{t},y_{t}) − ∑ t = 1 T w 1 : t − 1 B F ( x t − 1 , x t ) − w t B F ( x ⋆ , y t ) , \displaystyle\qquad-\sum_{t=1}^{T}w_{1:t-1}B_{F}(x_{t-1},x_{t})-w_{t}B_{F}(x_{\star},y_{t}), from which the conclusion immediately follows since 𝔼 [ g t | g 1 , … , g t − 1 ] = 𝔼 [ ∇ F ( y t ) | g 1 , … , g t − 1 ] \mathbb{E}[g_{t}|g_{1},\dots,g_{t-1}]=\mathbb{E}[\nabla F(y_{t})|g_{1},\dots,g_{t-1}] . So, let us establish ( 28 ). To do so, it will help to observe the following identities: w t ​ z t \displaystyle w_{t}z_{t} = w 1 : t x t − w 1 : t − 1 x t − 1 \displaystyle=w_{1:t}x_{t}-w_{1:t-1}x_{t-1} w 1 : t − 1 ( x t − x t − 1 ) \displaystyle w_{1:t-1}(x_{t}-x_{t-1}) = w t ​ ( z t − x t ) \displaystyle=w_{t}(z_{t}-x_{t}) (29) z t − y t \displaystyle z_{t}-y_{t} = 1 − α t α t ​ ( y t − x t ) . \displaystyle=\frac{1-\alpha_{t}}{\alpha_{t}}(y_{t}-x_{t}). (30) So, we have: w 1 : t F ( x t ) − w 1 : t − 1 F ( x t − 1 ) − w t F ( x ⋆ ) \displaystyle w_{1:t}F(x_{t})-w_{1:t-1}F(x_{t-1})-w_{t}F(x_{\star}) = w 1 : t − 1 ( F ( x t ) − F ( x t − 1 ) + w t ( F ( x t ) − F ( x ⋆ ) ) \displaystyle=w_{1:t-1}(F(x_{t})-F(x_{t-1})+w_{t}(F(x_{t})-F(x_{\star})) = w 1 : t − 1 ⟨ ∇ F ( x t ) , x t − x t − 1 ⟩ + w t ( F ( x t ) − F ( x ⋆ ) ) \displaystyle=w_{1:t-1}\langle\nabla F(x_{t}),x_{t}-x_{t-1}\rangle+w_{t}(F(x_{t})-F(x_{\star})) − w 1 : t − 1 B F ( x t − 1 , x t ) \displaystyle\qquad-w_{1:t-1}B_{F}(x_{t-1},x_{t}) using ( 29 ): = w t ⟨ ∇ F ( x t ) , z t − x t ⟩ + w t ( F ( x t ) − F ( x ⋆ ) ) − w 1 : t − 1 B F ( x t − 1 , x t ) \displaystyle=w_{t}\langle\nabla F(x_{t}),z_{t}-x_{t}\rangle+w_{t}(F(x_{t})-F(x_{\star}))-w_{1:t-1}B_{F}(x_{t-1},x_{t}) = w t ​ ⟨ ∇ F ​ ( x t ) , z t − x t ⟩ + w t ​ ( F ⁡ ( x t ) − F ⁡ ( y t ) ) + w t ​ ( F ⁡ ( y t ) − F ⁡ ( x ⋆ ) ) \displaystyle=w_{t}\langle\nabla F(x_{t}),z_{t}-x_{t}\rangle+w_{t}(F(x_{t})-F(y_{t}))+w_{t}(F(y_{t})-F(x_{\star})) − w 1 : t − 1 B F ( x t − 1 , x t ) \displaystyle\qquad-w_{1:t-1}B_{F}(x_{t-1},x_{t}) = w t ​ ⟨ ∇ F ​ ( x t ) , z t − x t ⟩ + w t ​ ⟨ ∇ F ​ ( x t ) , x t − y t ⟩ + w t ​ ⟨ ∇ F ​ ( y t ) , y t − x ⋆ ⟩ \displaystyle=w_{t}\langle\nabla F(x_{t}),z_{t}-x_{t}\rangle+w_{t}\langle\nabla F(x_{t}),x_{t}-y_{t}\rangle+w_{t}\langle\nabla F(y_{t}),y_{t}-x_{\star}\rangle − w 1 : t − 1 B F ( x t − 1 , x t ) − w t B F ( y t , x t ) − w t B F ( x ⋆ , y t ) \displaystyle\qquad-w_{1:t-1}B_{F}(x_{t-1},x_{t})-w_{t}B_{F}(y_{t},x_{t})-w_{t}B_{F}(x_{\star},y_{t}) = w t ​ ⟨ ∇ F ​ ( x t ) − ∇ F ​ ( y t ) , z t − y t ⟩ + w t ​ ⟨ ∇ F ​ ( y t ) , z t − x ⋆ ⟩ \displaystyle=w_{t}\langle\nabla F(x_{t})-\nabla F(y_{t}),z_{t}-y_{t}\rangle+w_{t}\langle\nabla F(y_{t}),z_{t}-x_{\star}\rangle − w 1 : t − 1 B F ( x t − 1 , x t ) − w t B F ( y t , x t ) − w t B F ( x ⋆ , y t ) \displaystyle\qquad-w_{1:t-1}B_{F}(x_{t-1},x_{t})-w_{t}B_{F}(y_{t},x_{t})-w_{t}B_{F}(x_{\star},y_{t}) using ( 30 ): = w t ​ 1 − α t α t ​ ⟨ ∇ F ​ ( x t ) − ∇ F ​ ( y t ) , y t − x t ⟩ + w t ​ ⟨ ∇ F ​ ( y t ) , z t − x ⋆ ⟩ \displaystyle=w_{t}\frac{1-\alpha_{t}}{\alpha_{t}}\langle\nabla F(x_{t})-\nabla F(y_{t}),y_{t}-x_{t}\rangle+w_{t}\langle\nabla F(y_{t}),z_{t}-x_{\star}\rangle − w 1 : t − 1 B F ( x t − 1 , x t ) − w t B F ( y t , x t ) − w t B F ( x ⋆ , y t ) \displaystyle\qquad-w_{1:t-1}B_{F}(x_{t-1},x_{t})-w_{t}B_{F}(y_{t},x_{t})-w_{t}B_{F}(x_{\star},y_{t}) using ( 27 ): = w t ​ ⟨ ∇ F ​ ( y t ) , z t − x ⋆ ⟩ \displaystyle=w_{t}\langle\nabla F(y_{t}),z_{t}-x_{\star}\rangle − w t ​ 1 − α t α t ​ ( B F ​ ( x t , y t ) + B F ​ ( y t , x t ) ) \displaystyle\qquad-w_{t}\frac{1-\alpha_{t}}{\alpha_{t}}(B_{F}(x_{t},y_{t})+B_{F}(y_{t},x_{t})) − w 1 : t − 1 B F ( x t − 1 , x t ) − w t B F ( y t , x t ) − w t B F ( x ⋆ , y t ) \displaystyle\qquad-w_{1:t-1}B_{F}(x_{t-1},x_{t})-w_{t}B_{F}(y_{t},x_{t})-w_{t}B_{F}(x_{\star},y_{t}) = w t ​ ⟨ ∇ F ​ ( y t ) , z t − x ⋆ ⟩ \displaystyle=w_{t}\langle\nabla F(y_{t}),z_{t}-x_{\star}\rangle − w t α t ​ B F ​ ( y t , x t ) − w t ​ ( 1 − α t ) α t ​ B F ​ ( x t , y t ) \displaystyle\qquad-\frac{w_{t}}{\alpha_{t}}B_{F}(y_{t},x_{t})-\frac{w_{t}(1-\alpha_{t})}{\alpha_{t}}B_{F}(x_{t},y_{t}) − w 1 : t − 1 B F ( x t − 1 , x t ) − w t B F ( x ⋆ , y t ) . \displaystyle\qquad-w_{1:t-1}B_{F}(x_{t-1},x_{t})-w_{t}B_{F}(x_{\star},y_{t}). ∎

## Appendix D Acceleration

In this section, we show that by instantiating our framework with an optimistic online learning algorithm ( Rakhlin and Sridharan,, 2013 ) , we achieve accelerated convergence guarantees. Our results match those available in the prior literature ( Kavis et al.,, 2019 ; Joulani et al.,, 2020 ) . Our approach is inspired by Joulani et al., (2020) ,: their method is based upon a version of Theorem 5 for the special case that α t = 0 \alpha_{t}=0 . Our result simply extends their analysis to α t = O ⁡ ( 1 / t ) \alpha_{t}=O(1/t) .

First, we establish an important technical Corollary that simplifies Theorem 5 in the case that F F is smooth and α t \alpha_{t} is sufficiently small.

###### Corollary 1 .

Under the same conditions as Theorem 5 , suppose additionally that F F is L L -smooth and suppose α t ≤ w t 10 w 1 : t \alpha_{t}\leq\frac{w_{t}}{10w_{1:t}} for all t t . Then we have for all x ⋆ x_{\star} : 𝔼 ⁡ [ F ⁡ ( x T ) − F ⁡ ( x ⋆ ) ] \displaystyle\mathbb{E}[F(x_{T})-F(x_{\star})] ≤ 𝔼 [ ∑ t = 1 T w t ​ ⟨ g t , z t − x ⋆ ⟩ w 1 : T ] \displaystyle\leq\mathbb{E}\left[\frac{\sum_{t=1}^{T}w_{t}\langle g_{t},z_{t}-x_{\star}\rangle}{w_{1:T}}\right] − 𝔼 [ ∑ t = 1 T w 1 : t − 1 ∥ ∇ F ( y t ) − ∇ F ( y t − 1 ) ∥ 2 6 L w 1 : T ] , \displaystyle\qquad-\mathbb{E}\left[\frac{\sum_{t=1}^{T}w_{1:t-1}\|\nabla F(y_{t})-\nabla F(y_{t-1})\|^{2}}{6Lw_{1:T}}\right], where above the value of y 0 y_{0} is arbitrary (since the coefficient is w 1 : 0 = 0 w_{1:0}=0 ).

###### Proof.

The key thing is to observe that smoothness implies B F ​ ( a , b ) ≥ 2 ​ L ​ ‖ ∇ F ​ ( a ) − ∇ F ​ ( b ) ‖ 2 B_{F}(a,b)\geq 2L\|\nabla F(a)-\nabla F(b)\|^{2} . The rest of the argument is straightforward manipulation of the terms in Theorem 5 : − w t α t ​ B F ​ ( y t , x t ) − w t ​ ( 1 − α t ) α t ​ B F ​ ( x t , y t ) \displaystyle-\frac{w_{t}}{\alpha_{t}}B_{F}(y_{t},x_{t})-\frac{w_{t}(1-\alpha_{t})}{\alpha_{t}}B_{F}(x_{t},y_{t}) ≤ − w t ​ ( 2 − α t ) 2 ​ L ​ α t ​ ‖ ∇ F ​ ( x t ) − ∇ F ​ ( y t ) ‖ 2 \displaystyle\leq-\frac{w_{t}(2-\alpha_{t})}{2L\alpha_{t}}\|\nabla F(x_{t})-\nabla F(y_{t})\|^{2} − w 1 : t − 1 B F ( x t − 1 , x t ) − w t B F ( x ⋆ , y t ) \displaystyle-w_{1:t-1}B_{F}(x_{t-1},x_{t})-w_{t}B_{F}(x_{\star},y_{t}) ≤ − w 1 : t − 1 2 ​ L ∥ ∇ F ( x t ) − ∇ F ( x t − 1 ) ∥ 2 . \displaystyle\leq-\frac{w_{1:t-1}}{2L}\|\nabla F(x_{t})-\nabla F(x_{t-1})\|^{2}. Next, observe that for any vectors a , b , c a,b,c , for any λ > 0 \lambda>0 : − ‖ a + b + c ‖ 2 \displaystyle-\|a+b+c\|^{2} = − ‖ a ‖ 2 − ‖ b ‖ 2 − ‖ c ‖ 2 − 2 ​ ⟨ a , b ⟩ − 2 ​ ⟨ b , c ⟩ − 2 ​ ⟨ a , c ⟩ \displaystyle=-\|a\|^{2}-\|b\|^{2}-\|c\|^{2}-2\langle a,b\rangle-2\langle b,c\rangle-2\langle a,c\rangle ≤ − ( 1 − 2 / λ ) ​ ‖ a ‖ 2 + ( 2 ​ λ − 1 ) ​ ( ‖ b ‖ 2 + ‖ c ‖ 2 ) , \displaystyle\leq-(1-2/\lambda)\|a\|^{2}+(2\lambda-1)(\|b\|^{2}+\|c\|^{2}), where we have used Young’s inequality: | ⟨ v , w ⟩ | ≤ ‖ v ‖ 2 2 ​ λ + λ ​ ‖ w ‖ 2 2 |\langle v,w\rangle|\leq\frac{\|v\|^{2}}{2\lambda}+\frac{\lambda\|w\|^{2}}{2} . Therefore, setting λ t = 3 \lambda_{t}=3 we obtain: − w 1 : t − 1 B F ( x t − 1 , x t ) − w t B F ( x ⋆ , y t ) \displaystyle-w_{1:t-1}B_{F}(x_{t-1},x_{t})-w_{t}B_{F}(x_{\star},y_{t}) ≤ − w 1 : t − 1 6 ​ L ∥ ∇ F ( y t ) − ∇ F ( y t − 1 ) ∥ 2 \displaystyle\leq-\frac{w_{1:t-1}}{6L}\|\nabla F(y_{t})-\nabla F(y_{t-1})\|^{2} + 5 w 1 : t − 1 2 ​ L ( ∥ ∇ F ( x t ) − ∇ F ( y t ) ∥ 2 + ∥ ∇ F ( x t − 1 ) − ∇ F ( y t − 1 ) ∥ 2 ) . \displaystyle\qquad+\frac{5w_{1:t-1}}{2L}(\|\nabla F(x_{t})-\nabla F(y_{t})\|^{2}+\|\nabla F(x_{t-1})-\nabla F(y_{t-1})\|^{2}). Now, since α t ≤ w t 10 w 1 : t ≤ 1 \alpha_{t}\leq\frac{w_{t}}{10w_{1:t}}\leq 1 , we obtain: − w t α t B F ( y t , x t ) − w t ​ ( 1 − α t ) α t B F ( x t , y t ) − w 1 : t − 1 B F ( x t − 1 , x t ) − w t B F ( x ⋆ , y t ) \displaystyle-\frac{w_{t}}{\alpha_{t}}B_{F}(y_{t},x_{t})-\frac{w_{t}(1-\alpha_{t})}{\alpha_{t}}B_{F}(x_{t},y_{t})-w_{1:t-1}B_{F}(x_{t-1},x_{t})-w_{t}B_{F}(x_{\star},y_{t}) ≤ − w 1 : t − 1 6 ​ L ∥ ∇ F ( y t ) − ∇ F ( y t − 1 ) ∥ 2 \displaystyle\qquad\leq-\frac{w_{1:t-1}}{6L}\|\nabla F(y_{t})-\nabla F(y_{t-1})\|^{2} − 5 w 1 : t 2 ​ L ∥ ∇ F ( x t ) − ∇ F ( y t ) ∥ 2 + − 5 w 1 : t − 1 2 ​ L ∥ ∇ F ( x t − 1 ) − ∇ F ( y t − 1 ) ∥ 2 . \displaystyle\qquad-\frac{5w_{1:t}}{2L}\|\nabla F(x_{t})-\nabla F(y_{t})\|^{2}+-\frac{5w_{1:t-1}}{2L}\|\nabla F(x_{t-1})-\nabla F(y_{t-1})\|^{2}. Now summing over t t from 1 to T T (and dropping one negative term), the sum telescopes to: ∑ t = 1 T − w 1 : t − 1 6 ​ L ∥ ∇ F ( y t ) − ∇ F ( y t − 1 ) ∥ 2 . \displaystyle\sum_{t=1}^{T}-\frac{w_{1:t-1}}{6L}\|\nabla F(y_{t})-\nabla F(y_{t-1})\|^{2}. The result now follows from Theorem 5 . ∎

Now, we consider the case that z t z_{t} is given by an optimistic mirror descent algorithm:

###### Corollary 2 .

Suppose F F is L L -smooth. Define g 0 = 0 g_{0}=0 and suppose also that for some D D satisfying D ≥ ‖ y 1 − x ⋆ ‖ D\geq\|y_{1}-x_{\star}\| : ∑ t = 1 T w t ​ ⟨ g t , z t − x ⋆ ⟩ ≤ D ​ ∑ t = 1 T w t 2 ​ ‖ g t − g t − 1 ‖ 2 . \displaystyle\sum_{t=1}^{T}w_{t}\langle g_{t},z_{t}-x_{\star}\rangle\leq D\sqrt{\sum_{t=1}^{T}w_{t}^{2}\|g_{t}-g_{t-1}\|^{2}}. Finally, suppose 𝔼 ⁡ [ ‖ g t − g t − 1 ‖ 2 ] ≤ ‖ ∇ F ​ ( y t ) − ∇ F ​ ( y t − 1 ) ‖ 2 + σ t 2 \mathbb{E}[\|g_{t}-g_{t-1}\|^{2}]\leq\|\nabla F(y_{t})-\nabla F(y_{t-1})\|^{2}+\sigma_{t}^{2} for some constants σ 1 , … , σ T \sigma_{1},\dots,\sigma_{T} (these are just variance bounds on the stochastic gradient oracle). Then with w t = t w_{t}=t and α t ≤ 1 5 ​ ( t − 1 ) \alpha_{t}\leq\frac{1}{5(t-1)} , we have: 𝔼 ⁡ [ F ⁡ ( x T ) − F ⁡ ( x ⋆ ) ] \displaystyle\mathbb{E}[F(x_{T})-F(x_{\star})] ≤ 14 ​ D 2 ​ L T ⁡ ( T + 1 ) + 2 ​ D ​ ∑ t = 1 T t 2 ​ σ t 2 T ⁡ ( T + 1 ) \displaystyle\leq\frac{14D^{2}L}{T(T+1)}+\frac{2D\sqrt{\sum_{t=1}^{T}t^{2}\sigma_{t}^{2}}}{T(T+1)} = O ⁡ ( D 2 ​ L T 2 + D ​ σ T ) , \displaystyle=O\left(\frac{D^{2}L}{T^{2}}+\frac{D\sigma}{\sqrt{T}}\right), where σ \sigma is uniform upper-bound on σ t \sigma_{t} . Note that the algorithm does not need to know L L or σ \sigma .

Algorithms producing z z sequences obtaining the guarantee stated here are called “optimistic online learning algorithms”.

###### Proof.

Applying Corollary 1 , we obtain immediately: T ⁡ ( T + 1 ) 2 ​ 𝔼 ​ [ F ⁡ ( x T ) − F ⁡ ( x ⋆ ) ] \displaystyle\frac{T(T+1)}{2}\mathbb{E}[F(x_{T})-F(x_{\star})] ≤ 𝔼 ⁡ [ D ​ ∑ t = 1 T t 2 ​ ‖ g t − g t − 1 ‖ 2 − ∑ t = 1 T ( t − 1 ) ​ t 12 ​ L ​ ‖ ∇ F ​ ( y t ) − ∇ F ​ ( y t − 1 ) ‖ 2 ] \displaystyle\leq\mathbb{E}\left[D\sqrt{\sum_{t=1}^{T}t^{2}\|g_{t}-g_{t-1}\|^{2}}-\sum_{t=1}^{T}\frac{(t-1)t}{12L}\|\nabla F(y_{t})-\nabla F(y_{t-1})\|^{2}\right] ≤ D ​ ∑ t = 1 T t 2 ​ 𝔼 ​ [ ‖ ∇ F ​ ( y t ) − ∇ F ​ ( y t − 1 ) ‖ 2 ] + t 2 ​ σ t 2 + ‖ ∇ F ​ ( y 1 ) ‖ 2 24 ​ L \displaystyle\leq D\sqrt{\sum_{t=1}^{T}t^{2}\mathbb{E}\left[\|\nabla F(y_{t})-\nabla F(y_{t-1})\|^{2}\right]+t^{2}\sigma_{t}^{2}}+\frac{\|\nabla F(y_{1})\|^{2}}{24L} − 1 24 ​ L ∑ t = 1 T t 2 𝔼 [ ∥ ∇ F ( y t ) − ∇ F ( y t − 1 ) ∥ 2 ] \displaystyle\qquad-\frac{1}{24L}\sum_{t=1}^{T}t^{2}\mathbb{E}\left[\|\nabla F(y_{t})-\nabla F(y_{t-1})\|^{2}\right] ≤ D ​ ∑ t = 1 T t 2 ​ 𝔼 ​ [ ‖ ∇ F ​ ( y t ) − ∇ F ​ ( y t − 1 ) ‖ 2 ] + D ​ ∑ t = 1 T t 2 ​ σ t 2 + ‖ ∇ F ​ ( y 1 ) ‖ 2 24 ​ L \displaystyle\leq D\sqrt{\sum_{t=1}^{T}t^{2}\mathbb{E}\left[\|\nabla F(y_{t})-\nabla F(y_{t-1})\|^{2}\right]}+D\sqrt{\sum_{t=1}^{T}t^{2}\sigma_{t}^{2}}+\frac{\|\nabla F(y_{1})\|^{2}}{24L} − 1 24 ​ L ∑ t = 1 T t 2 𝔼 [ ∥ ∇ F ( y t ) − ∇ F ( y t − 1 ) ∥ 2 ] \displaystyle\qquad-\frac{1}{24L}\sum_{t=1}^{T}t^{2}\mathbb{E}\left[\|\nabla F(y_{t})-\nabla F(y_{t-1})\|^{2}\right] Using the identity A ​ C − B ​ C ≤ A 2 4 ​ B A\sqrt{C}-BC\leq\frac{A^{2}}{4B} : ≤ 6 ​ D 2 ​ L + L ​ ‖ y 1 − x ⋆ ‖ 2 24 + D ​ ∑ t = 1 T t 2 ​ σ t 2 \displaystyle\leq 6D^{2}L+\frac{L\|y_{1}-x_{\star}\|^{2}}{24}+D\sqrt{\sum_{t=1}^{T}t^{2}\sigma_{t}^{2}} ≤ 7 ​ D 2 ​ L + D ​ ∑ t = 1 T t 2 ​ σ t 2 . \displaystyle\leq 7D^{2}L+D\sqrt{\sum_{t=1}^{T}t^{2}\sigma_{t}^{2}}. Divide by T ⁡ ( T + 1 ) 2 \frac{T(T+1)}{2} to conclude the result. ∎

### D.1 An Optimistic Regret Bound

In this section we provide an algorithm that achieves the optimistic regret bound required for our acceleration result Corollary 2 . This algorithm is a mild variation on the established literature ( Rakhlin and Sridharan,, 2013 ; Chiang et al.,, 2012 ; Hazan and Kale,, 2010 ; Joulani et al.,, 2017 ) to slightly improve a technical dependence on the maximum gradient value.

###### Lemma 1 .

For a sequence of vectors g 1 , … , g T g_{1},\dots,g_{T} , set η t = D 2 ​ ∑ i = 1 t ‖ g i − g i − 1 ‖ 2 \eta_{t}=\frac{D}{\sqrt{2\sum_{i=1}^{t}\|g_{i}-g_{i-1}\|^{2}}} with g 0 = 0 g_{0}=0 , define m t = max i ≤ t ⁡ ‖ g i − g i − 1 ‖ m_{t}=\max_{i\leq t}\|g_{i}-g_{i-1}\| and define the sequence of vectors z t , z t ′ z_{t},z^{\prime}_{t} and g ~ t \tilde{g}_{t} by the recursions: z 1 \displaystyle z_{1} = z 1 ′ = 0 \displaystyle=z^{\prime}_{1}=0 g ~ t \displaystyle\tilde{g}_{t} = g t − 1 + min ⁡ ( m t − 1 , ‖ g t − g t − 1 ‖ ) ​ g t − g t − 1 ‖ g t − g t − 1 ‖ \displaystyle=g_{t-1}+\min\left(m_{t-1},\|g_{t}-g_{t-1}\|\right)\frac{g_{t}-g_{t-1}}{\|g_{t}-g_{t-1}\|} η t \displaystyle\eta_{t} = D m t 2 + ∑ i = 1 t ‖ g ~ i − g i − 1 ‖ 2 \displaystyle=\frac{D}{\sqrt{m_{t}^{2}+\sum_{i=1}^{t}\|\tilde{g}_{i}-g_{i-1}\|^{2}}} z t + 1 ′ \displaystyle z^{\prime}_{t+1} = Π ‖ z t + 1 ′ ‖ ≤ D ​ z t ′ − η t ​ g ~ t \displaystyle=\Pi_{\|z^{\prime}_{t+1}\|\leq D}z^{\prime}_{t}-\eta_{t}\tilde{g}_{t} z t + 1 \displaystyle z_{t+1} = Π ‖ z t + 1 ‖ ≤ D ​ z t + 1 ′ − η t ​ g t . \displaystyle=\Pi_{\|z_{t+1}\|\leq D}z^{\prime}_{t+1}-\eta_{t}g_{t}. Then: ∑ t = 1 T ⟨ g t , z t − x ⋆ ⟩ ≤ 7 ​ D ​ 2 ​ ∑ t = 1 T ‖ g t − g t − 1 ‖ 2 . \displaystyle\sum_{t=1}^{T}\langle g_{t},z_{t}-x_{\star}\rangle\leq 7D\sqrt{2\sum_{t=1}^{T}\|g_{t}-g_{t-1}\|^{2}}.

###### Proof.

For purposes of notation, define g 0 = 0 g_{0}=0 and z 0 ′ = 0 z^{\prime}_{0}=0 . Further, observe that: ‖ g ~ t − g t − 1 ‖ \displaystyle\|\tilde{g}_{t}-g_{t-1}\| ≤ m t − 1 \displaystyle\leq m_{t-1} ‖ g ~ t − g t − 1 ‖ \displaystyle\|\tilde{g}_{t}-g_{t-1}\| ≤ ‖ g t − g t − 1 ‖ \displaystyle\leq\|g_{t}-g_{t-1}\| ‖ g ~ t − g t ‖ \displaystyle\|\tilde{g}_{t}-g_{t}\| = m t − m t − 1 \displaystyle=m_{t}-m_{t-1} η t \displaystyle\eta_{t} ≤ D ∑ i = 1 t + 1 ‖ g ~ i − g i − 1 ‖ 2 \displaystyle\leq\frac{D}{\sqrt{\sum_{i=1}^{t+1}\|\tilde{g}_{i}-g_{i-1}\|^{2}}} 1 η T \displaystyle\frac{1}{\eta_{T}} ≤ 2 ​ ∑ t = 1 T ‖ g t − g t − 1 ‖ 2 D . \displaystyle\leq\frac{\sqrt{2\sum_{t=1}^{T}\|g_{t}-g_{t-1}\|^{2}}}{D}.

Next, notice that z t + 1 ′ = argmin ‖ z ‖ ≤ D ⁡ ⟨ g ~ t , z ⟩ + 1 2 ​ η t ​ ‖ z − z t ′ ‖ 2 z^{\prime}_{t+1}=\mathop{\text{argmin}}_{\|z\|\leq D}\langle\tilde{g}_{t},z\rangle+\frac{1}{2\eta_{t}}\|z-z^{\prime}_{t}\|^{2} . Therefore since ‖ x ⋆ ‖ ≤ D \|x_{\star}\|\leq D , by first order optimality conditions: ⟨ g ~ t + z t + 1 ′ − z t ′ η t , z t + 1 ′ − x ⋆ ⟩ \displaystyle\left\langle\tilde{g}_{t}+\frac{z^{\prime}_{t+1}-z^{\prime}_{t}}{\eta_{t}},z^{\prime}_{t+1}-x_{\star}\right\rangle ≤ 0 \displaystyle\leq 0 ⟨ g ~ t , z t + 1 ′ − x ⋆ ⟩ \displaystyle\langle\tilde{g}_{t},z^{\prime}_{t+1}-x_{\star}\rangle ≤ 1 η t ​ ⟨ z t ′ − z t + 1 ′ , z t + 1 ′ − x ⋆ ⟩ \displaystyle\leq\frac{1}{\eta_{t}}\langle z^{\prime}_{t}-z^{\prime}_{t+1},z^{\prime}_{t+1}-x_{\star}\rangle = ‖ z t ′ − x ⋆ ‖ 2 2 ​ η t − ‖ z t + 1 ′ − x ⋆ ‖ 2 2 ​ η t − ‖ z t + 1 ′ − z t ′ ‖ 2 2 ​ η t . \displaystyle=\frac{\|z^{\prime}_{t}-x_{\star}\|^{2}}{2\eta_{t}}-\frac{\|z^{\prime}_{t+1}-x_{\star}\|^{2}}{2\eta_{t}}-\frac{\|z^{\prime}_{t+1}-z^{\prime}_{t}\|^{2}}{2\eta_{t}}.

Similarly, we have z t = argmin ‖ z ‖ ≤ D ⁡ ⟨ g t − 1 , z ⟩ + 1 2 ​ η t − 1 ​ ‖ z − z t ′ ‖ 2 z_{t}=\mathop{\text{argmin}}_{\|z\|\leq D}\langle g_{t-1},z\rangle+\frac{1}{2\eta_{t-1}}\|z-z^{\prime}_{t}\|^{2} . From this we have: ⟨ g t − 1 + z t − z t ′ η t − 1 , z t − z t + 1 ′ ⟩ \displaystyle\left\langle g_{t-1}+\frac{z_{t}-z^{\prime}_{t}}{\eta_{t-1}},z_{t}-z^{\prime}_{t+1}\right\rangle ≤ 0 \displaystyle\leq 0 ⟨ g t − 1 , z t − z t + 1 ′ ⟩ \displaystyle\langle g_{t-1},z_{t}-z^{\prime}_{t+1}\rangle ≤ ‖ z t ′ − z t + 1 ′ ‖ 2 2 ​ η t − 1 − ‖ z t − z t + 1 ′ ‖ 2 2 ​ η t − 1 − ‖ z t − z t ′ ‖ 2 2 ​ η t − 1 \displaystyle\leq\frac{\|z^{\prime}_{t}-z^{\prime}_{t+1}\|^{2}}{2\eta_{t-1}}-\frac{\|z_{t}-z^{\prime}_{t+1}\|^{2}}{2\eta_{t-1}}-\frac{\|z_{t}-z^{\prime}_{t}\|^{2}}{2\eta_{t-1}} ⟨ g ~ t , z t − z t + 1 ′ ⟩ \displaystyle\langle\tilde{g}_{t},z_{t}-z^{\prime}_{t+1}\rangle ≤ ‖ z t ′ − z t + 1 ′ ‖ 2 2 ​ η t − 1 − ‖ z t − z t + 1 ′ ‖ 2 2 ​ η t − 1 − ‖ z t − z t ′ ‖ 2 2 ​ η t − 1 \displaystyle\leq\frac{\|z^{\prime}_{t}-z^{\prime}_{t+1}\|^{2}}{2\eta_{t-1}}-\frac{\|z_{t}-z^{\prime}_{t+1}\|^{2}}{2\eta_{t-1}}-\frac{\|z_{t}-z^{\prime}_{t}\|^{2}}{2\eta_{t-1}} + ⟨ g ~ t − g t − 1 , z t − z t + 1 ′ ⟩ \displaystyle+\langle\tilde{g}_{t}-g_{t-1},z_{t}-z^{\prime}_{t+1}\rangle by Young’s inequality: ≤ ‖ z t ′ − z t + 1 ′ ‖ 2 2 ​ η t − 1 − ‖ z t − z t + 1 ′ ‖ 2 2 ​ η t − 1 − ‖ z t − z t ′ ‖ 2 2 ​ η t − 1 \displaystyle\leq\frac{\|z^{\prime}_{t}-z^{\prime}_{t+1}\|^{2}}{2\eta_{t-1}}-\frac{\|z_{t}-z^{\prime}_{t+1}\|^{2}}{2\eta_{t-1}}-\frac{\|z_{t}-z^{\prime}_{t}\|^{2}}{2\eta_{t-1}} + η t − 1 ​ ‖ g ~ t − g t − 1 ‖ 2 2 + ‖ z t − z t + 1 ′ ‖ 2 2 ​ η t − 1 \displaystyle+\frac{\eta_{t-1}\|\tilde{g}_{t}-g_{t-1}\|^{2}}{2}+\frac{\|z_{t}-z^{\prime}_{t+1}\|^{2}}{2\eta_{t-1}} ≤ ‖ z t ′ − z t + 1 ′ ‖ 2 2 ​ η t − 1 + η t − 1 ​ ‖ g ~ t − g t − 1 ‖ 2 2 . \displaystyle\leq\frac{\|z^{\prime}_{t}-z^{\prime}_{t+1}\|^{2}}{2\eta_{t-1}}+\frac{\eta_{t-1}\|\tilde{g}_{t}-g_{t-1}\|^{2}}{2}. So, combining these facts (and noticing that η t − 1 ≥ η t \eta_{t-1}\geq\eta_{t} :) ⟨ g ~ t , z t − x ⋆ ⟩ \displaystyle\langle\tilde{g}_{t},z_{t}-x_{\star}\rangle ≤ ‖ z t ′ − x ⋆ ‖ 2 2 ​ η t − ‖ z t + 1 ′ − x ⋆ ‖ 2 2 ​ η t + η t − 1 ​ ‖ g ~ t − g t − 1 ‖ 2 2 \displaystyle\leq\frac{\|z^{\prime}_{t}-x_{\star}\|^{2}}{2\eta_{t}}-\frac{\|z^{\prime}_{t+1}-x_{\star}\|^{2}}{2\eta_{t}}+\frac{\eta_{t-1}\|\tilde{g}_{t}-g_{t-1}\|^{2}}{2} ⟨ g t , z t − x ⋆ ⟩ \displaystyle\langle g_{t},z_{t}-x_{\star}\rangle ≤ ‖ z t ′ − x ⋆ ‖ 2 2 ​ η t − ‖ z t + 1 ′ − x ⋆ ‖ 2 2 ​ η t + η t − 1 ​ ‖ g ~ t − g t − 1 ‖ 2 2 + ⟨ g t − g ~ t , z t − x ⋆ ⟩ \displaystyle\leq\frac{\|z^{\prime}_{t}-x_{\star}\|^{2}}{2\eta_{t}}-\frac{\|z^{\prime}_{t+1}-x_{\star}\|^{2}}{2\eta_{t}}+\frac{\eta_{t-1}\|\tilde{g}_{t}-g_{t-1}\|^{2}}{2}+\langle g_{t}-\tilde{g}_{t},z_{t}-x_{\star}\rangle ≤ ‖ z t ′ − x ⋆ ‖ 2 2 ​ η t − ‖ z t + 1 ′ − x ⋆ ‖ 2 2 ​ η t + η t − 1 ​ ‖ g ~ t − g t − 1 ‖ 2 2 + 2 ​ D ​ ( m t − m t − 1 ) . \displaystyle\leq\frac{\|z^{\prime}_{t}-x_{\star}\|^{2}}{2\eta_{t}}-\frac{\|z^{\prime}_{t+1}-x_{\star}\|^{2}}{2\eta_{t}}+\frac{\eta_{t-1}\|\tilde{g}_{t}-g_{t-1}\|^{2}}{2}+2D(m_{t}-m_{t-1}). So, we have: ∑ t = 1 T ⟨ g t , z t − x ⋆ ⟩ \displaystyle\sum_{t=1}^{T}\langle g_{t},z_{t}-x_{\star}\rangle ≤ 2 ​ D ​ m T + ‖ z 1 ′ − x ⋆ ‖ 2 2 ​ η 1 + ∑ t = 2 T ‖ z t ′ − x ⋆ ‖ 2 2 ​ ( 1 η t − 1 η t − 1 ) \displaystyle\leq 2Dm_{T}+\frac{\|z^{\prime}_{1}-x_{\star}\|^{2}}{2\eta_{1}}+\sum_{t=2}^{T}\frac{\|z^{\prime}_{t}-x_{\star}\|^{2}}{2}\left(\frac{1}{\eta_{t}}-\frac{1}{\eta_{t-1}}\right) + ∑ t = 1 T η t − 1 ​ ‖ g ~ t − g t − 1 ‖ 2 2 \displaystyle+\sum_{t=1}^{T}\frac{\eta_{t-1}\|\tilde{g}_{t}-g_{t-1}\|^{2}}{2} ≤ 2 ​ D ​ m T + 4 ​ D 2 / η T + ∑ t = 1 T η t − 1 ​ ‖ g ~ t − g t − 1 ‖ 2 2 \displaystyle\leq 2Dm_{T}+4D^{2}/\eta_{T}+\sum_{t=1}^{T}\frac{\eta_{t-1}\|\tilde{g}_{t}-g_{t-1}\|^{2}}{2} ≤ 6 ​ D 2 / η T + ∑ t = 1 T η t − 1 ​ ‖ g ~ t − g t − 1 ‖ 2 2 \displaystyle\leq 6D^{2}/\eta_{T}+\sum_{t=1}^{T}\frac{\eta_{t-1}\|\tilde{g}_{t}-g_{t-1}\|^{2}}{2} ≤ 6 ​ D 2 / η T + ∑ t = 1 T D ​ ‖ g ~ t − g t − 1 ‖ 2 2 ​ ∑ i = 1 t ‖ g ~ i − g i − 1 ‖ 2 \displaystyle\leq 6D^{2}/\eta_{T}+\sum_{t=1}^{T}\frac{D\|\tilde{g}_{t}-g_{t-1}\|^{2}}{2\sqrt{\sum_{i=1}^{t}\|\tilde{g}_{i}-g_{i-1}\|^{2}}} ≤ 6 ​ D 2 / η T + D ​ ∑ t = 1 T ‖ g ~ t − g t − 1 ‖ 2 \displaystyle\leq 6D^{2}/\eta_{T}+D\sqrt{\sum_{t=1}^{T}\|\tilde{g}_{t}-g_{t-1}\|^{2}} ≤ 7 ​ D ​ 2 ​ ∑ t = 1 T ‖ g t − g t − 1 ‖ 2 . \displaystyle\leq 7D\sqrt{2\sum_{t=1}^{T}\|g_{t}-g_{t-1}\|^{2}}.

∎

## Appendix E Strongly Convex Losses

Suppose that the expected loss F F is actually known to be μ \mu -strongly convex. Then we’d like to have a convergence guarantee of O ⁡ ( 1 / μ ​ T ) O(1/\mu T) . This is achieved in Theorem 6 below.

###### Theorem 6 .

Under the same assumptions as Theorem 5 , define ℓ t ​ ( z ) = ⟨ g t , z ⟩ + μ 2 ​ ‖ y t − z ‖ 2 \ell_{t}(z)=\langle g_{t},z\rangle+\frac{\mu}{2}\|y_{t}-z\|^{2} . Define the “regret” of the sequence z t z_{t} as: Regret ℓ ​ ( x ⋆ ) \displaystyle\text{Regret}_{\ell}(x_{\star}) = ∑ t = 1 T w t ​ ( ℓ t ​ ( z t ) − ℓ t ​ ( x ⋆ ) ) . \displaystyle=\sum_{t=1}^{T}w_{t}(\ell_{t}(z_{t})-\ell_{t}(x_{\star})). Then we have for x ⋆ = argmin ​ F x_{\star}=\text{argmin }F : 𝔼 ⁡ [ F ⁡ ( x T ) − F ⁡ ( x ⋆ ) ] \displaystyle\mathbb{E}[F(x_{T})-F(x_{\star})] ≤ 𝔼 [ Regret ℓ ​ ( x ⋆ ) − ∑ t = 1 T w t ​ μ 2 ​ ‖ z t − y t ‖ 2 w 1 : T ] . \displaystyle\leq\mathbb{E}\left[\frac{\text{Regret}_{\ell}(x_{\star})-\sum_{t=1}^{T}\frac{w_{t}\mu}{2}\|z_{t}-y_{t}\|^{2}}{w_{1:T}}\right]. In particular, suppose ‖ x ⋆ ‖ ≤ D \|x_{\star}\|\leq D for some known bound D D and ‖ g t ‖ ≤ G \|g_{t}\|\leq G for all t t for some G G so long as ‖ y t ‖ ≤ D \|y_{t}\|\leq D . Then if we define w t = t w_{t}=t for all t t and set z t z_{t} by: z t + 1 = Π ‖ z ‖ ≤ D ​ [ z t − 2 ​ ( g t + μ ⁡ ( z t − y t ) ) μ ⁡ ( t + 1 ) ] . \displaystyle z_{t+1}=\Pi_{\|z\|\leq D}\left[z_{t}-\frac{2(g_{t}+\mu(z_{t}-y_{t}))}{\mu(t+1)}\right]. then we have: 𝔼 ⁡ [ F ⁡ ( x T ) − F ⁡ ( x ⋆ ) ] \displaystyle\mathbb{E}[F(x_{T})-F(x_{\star})] ≤ 2 ​ ( G + 2 ​ μ ​ D ) 2 μ ⁡ ( T + 1 ) . \displaystyle\leq\frac{2(G+2\mu D)^{2}}{\mu(T+1)}.

###### Proof.

From Theorem 5 , we have: 𝔼 ⁡ [ F ⁡ ( x T ) − F ⁡ ( x ⋆ ) ] \displaystyle\mathbb{E}[F(x_{T})-F(x_{\star})] ≤ 𝔼 [ ∑ t = 1 T w t ​ ⟨ g t , z t − x ⋆ ⟩ w 1 : T − ∑ t = 1 T w t ​ B F ​ ( x ⋆ , y t ) w 1 : T ] . \displaystyle\leq\mathbb{E}\left[\frac{\sum_{t=1}^{T}w_{t}\langle g_{t},z_{t}-x_{\star}\rangle}{w_{1:T}}-\frac{\sum_{t=1}^{T}w_{t}B_{F}(x_{\star},y_{t})}{w_{1:T}}\right]. Now, since F F is μ \mu -strongly convex, we have B F ​ ( x ⋆ , y t ) ≥ μ 2 ​ ‖ y t − x ⋆ ‖ 2 B_{F}(x_{\star},y_{t})\geq\frac{\mu}{2}\|y_{t}-x_{\star}\|^{2} . Further, we have: ∑ t = 1 T w t ​ ⟨ g t , z t − x ⋆ ⟩ \displaystyle\sum_{t=1}^{T}w_{t}\langle g_{t},z_{t}-x_{\star}\rangle = ∑ t = 1 T w t ​ ( ℓ t ​ ( z t ) − ℓ t ​ ( x ⋆ ) ) − w t ​ μ 2 ​ ‖ z t − y t ‖ 2 + w t ​ μ 2 ​ ‖ x ⋆ − y t ‖ 2 . \displaystyle=\sum_{t=1}^{T}w_{t}(\ell_{t}(z_{t})-\ell_{t}(x_{\star}))-\frac{w_{t}\mu}{2}\|z_{t}-y_{t}\|^{2}+\frac{w_{t}\mu}{2}\|x_{\star}-y_{t}\|^{2}. From this we obtain the desired result: 𝔼 ⁡ [ F ⁡ ( x T ) − F ⁡ ( x ⋆ ) ] \displaystyle\mathbb{E}[F(x_{T})-F(x_{\star})] ≤ 𝔼 [ Regret ℓ ​ ( x ⋆ ) − ∑ t = 1 T w t ​ μ 2 ​ ‖ z t − y t ‖ 2 w 1 : T ] . \displaystyle\leq\mathbb{E}\left[\frac{\text{Regret}_{\ell}(x_{\star})-\sum_{t=1}^{T}\frac{w_{t}\mu}{2}\|z_{t}-y_{t}\|^{2}}{w_{1:T}}\right]. For the final statement, observe that with w t = t w_{t}=t , w t ​ ℓ t ​ ( z ) = t ⁡ ⟨ g t , z ⟩ + t ​ μ 2 ​ ‖ z − y t ‖ 2 w_{t}\ell_{t}(z)=t\langle g_{t},z\rangle+\frac{t\mu}{2}\|z-y_{t}\|^{2} is t ​ μ t\mu -strongly convex. Therefore if we use learning rate η t = 1 μ w 1 : t = 2 μ ​ t ​ ( t + 1 ) \eta_{t}=\frac{1}{\mu w_{1:t}}=\frac{2}{\mu t(t+1)} , then standard analysis of projected OGD yields: ∑ t = 1 T t ⁡ ( ℓ t ​ ( z t ) − ℓ t ​ ( x ⋆ ) ) \displaystyle\sum_{t=1}^{T}t(\ell_{t}(z_{t})-\ell_{t}(x_{\star})) ≤ ∑ t = 1 T t ⁡ ⟨ ∇ ℓ t ​ ( z t ) , z t − x ⋆ ⟩ − t ​ μ 2 ​ ‖ z t − x ⋆ ‖ 2 \displaystyle\leq\sum_{t=1}^{T}t\langle\nabla\ell_{t}(z_{t}),z_{t}-x_{\star}\rangle-\frac{t\mu}{2}\|z_{t}-x_{\star}\|^{2} ≤ ‖ z 1 − x ⋆ ‖ 2 ​ ( 1 2 ​ η 1 − μ 2 ​ ‖ z t − x ⋆ ‖ 2 ) − ‖ z T + 1 − x ⋆ ‖ 2 2 ​ η T \displaystyle\leq\|z_{1}-x_{\star}\|^{2}\left(\frac{1}{2\eta_{1}}-\frac{\mu}{2}\|z_{t}-x_{\star}\|^{2}\right)-\frac{\|z_{T+1}-x_{\star}\|^{2}}{2\eta_{T}} + ∑ t = 2 T ∥ z t − x ⋆ ∥ 2 ( 1 2 ​ η t − 1 2 ​ η t − 1 − t ​ μ 2 ) + ∑ t = 1 T η t ​ t 2 ​ ‖ ∇ ℓ t ​ ( z t ) ‖ 2 2 \displaystyle\qquad+\sum_{t=2}^{T}\|z_{t}-x_{\star}\|^{2}\left(\frac{1}{2\eta_{t}}-\frac{1}{2\eta_{t-1}}-\frac{t\mu}{2}\right)+\sum_{t=1}^{T}\frac{\eta_{t}t^{2}\|\nabla\ell_{t}(z_{t})\|^{2}}{2} ≤ ∑ t = 1 T η t ​ t 2 ​ ‖ ∇ ℓ t ​ ( z t ) ‖ 2 2 \displaystyle\leq\sum_{t=1}^{T}\frac{\eta_{t}t^{2}\|\nabla\ell_{t}(z_{t})\|^{2}}{2} ≤ 1 μ ​ ∑ t = 1 T ‖ ∇ ℓ t ​ ( z t ) ‖ 2 \displaystyle\leq\frac{1}{\mu}\sum_{t=1}^{T}\|\nabla\ell_{t}(z_{t})\|^{2} = 1 μ ​ ∑ t = 1 T ‖ g t + μ ⁡ ( z t − y t ) ‖ 2 \displaystyle=\frac{1}{\mu}\sum_{t=1}^{T}\|g_{t}+\mu(z_{t}-y_{t})\|^{2} ≤ T ​ ( G + 2 ​ μ ​ D ) 2 μ . \displaystyle\leq\frac{T(G+2\mu D)^{2}}{\mu}. where in the last inequality we have observed that since ‖ z t ‖ ≤ D \|z_{t}\|\leq D and y t y_{t} is a linear combination of past z z values, ‖ y t ‖ ≤ D \|y_{t}\|\leq D as well. Finally, observing that w 1 : T = T ⁡ ( T + 1 ) 2 w_{1:T}=\frac{T(T+1)}{2} , the result follows. ∎

## Appendix F Large Step size convergence

See 3

###### Proof.

Consider SGD with fixed step size γ \gamma : z t + 1 = z t − γ ​ g t . z_{t+1}=z_{t}-\gamma g_{t}. Let s T + 1 = ∑ t = 1 T γ ​ g t . s_{T+1}=\sum_{t=1}^{T}\gamma g_{t}. Recall from D-Adaptation ( Defazio and Mishchenko,, 2023 ) theory that: ∑ t = 1 T γ ⁡ ⟨ g t , z t − z 1 ⟩ = 1 2 ​ ∑ t = 1 T γ 2 ​ ‖ g t ‖ 2 − 1 2 ​ ‖ s t + 1 ‖ 2 \sum_{t=1}^{T}\gamma\left\langle g_{t},z_{t}-z_{1}\right\rangle=\frac{1}{2}\sum_{t=1}^{T}\gamma^{2}\left\|g_{t}\right\|^{2}-\frac{1}{2}\left\|s_{t+1}\right\|^{2} (31) and: ∑ t = 1 T γ ⁡ ⟨ g t , z t − z ∗ ⟩ ≤ ‖ s T + 1 ‖ ​ D + ∑ t = 1 T γ ⁡ ⟨ g t , z t − z 1 ⟩ . \sum_{t=1}^{T}\gamma\left\langle g_{t},z_{t}-z_{*}\right\rangle\leq\left\|s_{T+1}\right\|D+\sum_{t=1}^{T}\gamma\left\langle g_{t},z_{t}-z_{1}\right\rangle. (32) Now suppose that the regret at time T is negative. Then trivially the theorem holds: 1 T ​ ∑ t = 1 T ⟨ g t , z t − z ∗ ⟩ ≤ 0 = 𝒪 ⁡ ( D T ​ ∑ t = 1 T ‖ g t ‖ 2 ) , \frac{1}{T}\sum_{t=1}^{T}\left\langle g_{t},z_{t}-z_{*}\right\rangle\leq 0=\mathcal{O}\left(\frac{D}{T}\sqrt{\sum_{t=1}^{T}\left\|g_{t}\right\|^{2}}\right), therefore, without loss of generality we may assume that ∑ t = 1 T γ ⁡ ⟨ g t , z t − z ∗ ⟩ ≥ 0 \sum_{t=1}^{T}\gamma\left\langle g_{t},z_{t}-z_{*}\right\rangle\geq 0 . Then from combining Equation 32 with Equation 31 we have: 0 ≤ − 1 2 ​ ‖ s T + 1 ‖ 2 + ‖ s T + 1 ‖ ​ D + 1 2 ​ ∑ t = 1 T γ 2 ​ ‖ g t ‖ 2 . 0\leq-\frac{1}{2}\left\|s_{T+1}\right\|^{2}+\left\|s_{T+1}\right\|D+\frac{1}{2}\sum_{t=1}^{T}\gamma^{2}\left\|g_{t}\right\|^{2}. This is a quadratic equation in ‖ s T + 1 ‖ \left\|s_{T+1}\right\| which we can solve explicitly via the quadratic formula, taking the largest root: ‖ s T + 1 ‖ ≤ − b ± b 2 − 4 ​ a ​ c 2 ​ a . \left\|s_{T+1}\right\|\leq\frac{-b\pm\sqrt{b^{2}-4ac}}{2a}. Plugging in the values a = − 1 2 a=-\frac{1}{2} , b = D b=D , c = 1 2 ​ ∑ t = 1 T γ 2 ​ ‖ g t ‖ 2 c=\frac{1}{2}\sum_{t=1}^{T}\gamma^{2}\left\|g_{t}\right\|^{2} : D ± D 2 + ∑ t = 1 T γ 2 ​ ‖ g t ‖ 2 ≤ 2 ​ D + ∑ t = 1 T γ 2 ​ ‖ g t ‖ 2 . D\pm\sqrt{D^{2}+\sum_{t=1}^{T}\gamma^{2}\left\|g_{t}\right\|^{2}}\leq 2D+\sqrt{\sum_{t=1}^{T}\gamma^{2}\left\|g_{t}\right\|^{2}}. Therefore: ‖ s T + 1 ‖ ≤ 2 ​ D + γ ​ ∑ t = 1 T ‖ g t ‖ 2 . \left\|s_{T+1}\right\|\leq 2D+\gamma\sqrt{\sum_{t=1}^{T}\left\|g_{t}\right\|^{2}}. Substituting this into Equation 32 : ∑ t = 1 T γ ⁡ ⟨ g t , z t − z ∗ ⟩ ≤ 2 ​ D 2 + γ ​ D ​ ∑ t = 1 T ‖ g t ‖ 2 + ∑ t = 1 T γ ⁡ ⟨ g t , z t − z 1 ⟩ . \sum_{t=1}^{T}\gamma\left\langle g_{t},z_{t}-z_{*}\right\rangle\leq 2D^{2}+\gamma D\sqrt{\sum_{t=1}^{T}\left\|g_{t}\right\|^{2}}+\sum_{t=1}^{T}\gamma\left\langle g_{t},z_{t}-z_{1}\right\rangle. Therefore, if ∑ t = 1 T ⟨ g t , z t − z 1 ⟩ ≤ D ​ ∑ t = 1 T ‖ g t ‖ 2 \sum_{t=1}^{T}\left\langle g_{t},z_{t}-z_{1}\right\rangle\leq D\sqrt{\sum_{t=1}^{T}\left\|g_{t}\right\|^{2}} then: ∑ t = 1 T γ ⁡ ⟨ g t , z t − z ∗ ⟩ ≤ 2 ​ D 2 + 2 ​ γ ​ D ​ ∑ t = 1 T ‖ g t ‖ 2 . \sum_{t=1}^{T}\gamma\left\langle g_{t},z_{t}-z_{*}\right\rangle\leq 2D^{2}+2\gamma D\sqrt{\sum_{t=1}^{T}\left\|g_{t}\right\|^{2}}. Plugging in γ = D / G \gamma=D/G : ∑ t = 1 T ⟨ g t , z t − z ∗ ⟩ \displaystyle\sum_{t=1}^{T}\left\langle g_{t},z_{t}-z_{*}\right\rangle ≤ 2 ​ D ​ G + 2 ​ D ​ ∑ t = 1 T ‖ g t ‖ 2 \displaystyle\leq 2DG+2D\sqrt{\sum_{t=1}^{T}\left\|g_{t}\right\|^{2}} ≤ 4 ​ D ​ ∑ t = 1 T ‖ g t ‖ 2 , \displaystyle\leq 4D\sqrt{\sum_{t=1}^{T}\left\|g_{t}\right\|^{2}}, and the theorem follows. ∎

## Appendix G Experimental Setup

### G.1 Convex experiments

Each dataset is obtained from the LIBSVM repository and used without modifications.

Hyper-parameter Value GPUs 1 × \times V100 Batch size 16 Epochs 100 Seeds 10 Schedule-Free β 1 \beta_{1} 0.9 Hyper-parameter Value Decay 0.0 Optimizer Adam Baseline β 1 \beta_{1} 0.9 β 2 \beta_{2} 0.95

### G.2 CIFAR-10

We used custom training code based on the PyTorch tutorial code for this problem. Following standard data-augmentation practises, we appliyed random horizontal flips and random offset cropping down to 32x32, using reflection padding of 4 pixels. Input pixel data was normalized by centering around 0.5.

Hyper-parameter Value Architecture Wide ResNet 16-8 Epochs 300 GPUs 1 × \times V100 Batch size per GPU 128 Cosine/Schedule-Free Warmup 5% Baseline Stepwise LR 0.1 Hyper-parameter Value Seeds 10 decay 0.0001 Baseline Momentum 0.9 Schedule-Free LR 10 Schedule-Free β \beta 0.9 Baseline Cosine LR 0.2

### G.3 CIFAR-100

We used the same codebase as for our CIFAR-10 experiments, with the same data augmentation.

We normalized each input image using fixed mean and standard error values derived from pre-processing the data.

Hyper-parameter Value Architecture DenseNet [6,12,24,16], growth rate 12 Epochs 300 GPUs 1 × \times V100 Schedule-Free β \beta 0.9 Cosine/Schedule-Free Warmup 5% Baseline Stepwise LR 0.05 Hyper-parameter Value Batch size per GPU 64 Seeds 10 Decay 0.0002 Baseline Momentum 0.9 Schedule-Free LR 5 Baseline Cosine LR 0.05

### G.4 SVHN

We used the same codebase as for our CIFAR experiments, and following the same data preprocessing.

Hyper-parameter Value Batch size 32 Weight decay Cosine 0.0001 Weight decay Step Sched 5e-5 Seeds 10 Baseline Stepwise LR 0.1 Hyper-parameter Value Cosine/Schedule-Free Warmup 5% Schedule-Free decay 0.0002 Schedule-Free LR 1.0 Schedule-Free β \beta 0.9 Baseline Cosine LR 0.1

### G.5 ImageNet

We used the same code-base as for our CIFAR-10 experiments, and applied the same preprocessing procedure. The data-augmentations consisted of PyTorch’s RandomResizedCrop, cropping to 224x224 followed by random horizontal flips. Test images used a fixed resize to 256x256 followed by a center crop to 224x224.

Hyper-parameter Value Architecture ResNet50 Epochs 100 GPUs 8 × \times V100 Batch size per GPU 32 Schedule-Free Decay 0.00005 Baseline Stepwise LR 0.1 Baseline Cosine LR 0.05 Hyper-parameter Value Seeds 5 Decay 0.0001 Baseline Momentum 0.9 Schedule-Free β \beta 0.9 Cosine/Schedule-Free Warmup 5% Schedule-Free LR 1.5

### G.6 IWSLT14

We used the FairSeq framework 3 3 3 https://github.com/facebookresearch/fairseq for our experiments. Rather than a vanilla LSTM we use the variant from Wiseman and Rush, (2016) provided in the FairSeq codebase.

Hyper-parameter Value Architecture lstm_wiseman_iwslt_de_en Max Epoch 55 GPUs 1 × \times V100 Tokens per batch 4096 Warmup steps 4000 Dropout 0.3 Label smoothing 0.1 Schedule-Free LR 0.02 Schedule-Free warmup 5% Baseline schedule Linear Decay Hyper-parameter Value Share decoder, input, output embed True Float16 True Update Frequency 1 Seeds 10 Decay 0.05 Baseline β 1 \beta_{1} 0.9 Schedule-Free β 1 \beta_{1} 0.9 β 2 \beta_{2} 0.98 Baseline LR 0.01

### G.7 NanoGPT

We followed the NanoGPT codebase 4 4 4 https://github.com/karpathy/nanoGPT as closely as possible, matching the default batch-size, training length and schedule. Our runs replicate the stated 2.85 loss in the documentation. Disabling gradient norm clipping is crucial for the Schedule-Free runs.

Hyper-parameter Value Architecture transformer_lm_gpt Batch size per gpu 12 Max Iters 600,000 GPUs 40 × \times V100 Tokens per sample 512 Dropout 0.0 Baseline LR 0.0005 Warmup 2,000 Schedule-Free LR 0.005 Schedule-Free β \beta 0.98 Schedule-Free decay 0.05 Hyper-parameter Value Block Size 1024 Num layer 12 Num head 12 Num embd 768 Float16 True Update Frequency 16 Seeds 5 Decay 0.1 Baseline β 1 , β 2 \beta_{1},\beta_{2} 0.9, 0.95 Gradient Clipping 0.0

### G.8 MAE

Our implementation uses the offical code 5 5 5 https://github.com/fairinternal/mae , with hyper-parameters following examples given in the repository.

Hyper-parameter Value Model vit_base_patch16 Epochs 100 GPUs 32 × \times V100 Batch Size 32 Baseline LR 5e-4 Layer Decay 0.65 Weight Decay 0.05 Baseline β 1 \beta_{1} 0.9 Hyper-parameter Value β 2 \beta_{2} 0.999 Schedule-Free LR 0.0.002 Schedule-Free decay 0.05 Schedule-Free β 1 \beta_{1} 0.9 Drop Path 0.1 Reprob 0.25 Mixup 0.8 Cutmix 1.0

### G.9 DLRM

We used a custom implementation of the DLRM model based on the publicly available code. Our optimizer uses dense gradients for implementation simplicity, although sparse-gradients using AdaGrad is a more common baseline on this problem, we consider AdaGrad variants of our scheduling approach as future work.

Hyper-parameter Value Iterations 300 000 Batch Size 128 Emb Dimension 16 GPUs 8 × \times V100 Schedule-Free LR 0.0005 Schedule-Free β 1 \beta_{1} 0.9 β 2 \beta_{2} 0.999 Hyper-parameter Value Seeds 5 Decay 0.0 Baseline β 1 \beta_{1} 0.9 Warmup 0 Baseline LR 0.0002 Baseline schedule Linear Decay

### G.10 MRI

We used the version of the the fastMRI code base at https://github.com/facebookresearch/fastMRI/tree/main/banding_removal . Note that we found that training failed using PyTorch 2 or newer, and so we ran these experiments using PyTorch 1.9.

Hyper-parameter Value Architecture 12 layer VarNet 2.0 Epochs 50 GPUs 8 × \times V100 Batch size per GPU 1 Acceleration factor 4 Baseline Schedule Linear Decay Baseline LR 0.005 β 2 \beta_{2} 0.999 Hyper-parameter Value Low frequency lines 16 Mask type Offset-1 Seeds 5 Decay 0.0 Baseline β 1 \beta_{1} 0.9 Schedule-Free LR 0.005 Schedule-Free β \beta 0.9

### G.11 Algoperf

Our full algoperf entry is availiable at https://github.com/facebookresearch/schedule_free/tree/main/schedulefree/algoperf . The hyper-parameters used for the self-tuning track submission are listed below.

Hyper-parameter Value Learning Rate 0.0025 one-minus Beta1 0.1 Beta2 (default) 0.9955159689799007 Weight Decay (default) 0.08121616522670176 Hyper-parameter Value Dropout Rate 0.1 Warmup Percentage 2% Label Smoothing 0.2 Polynomial in c t c_{t} average 0.75

## Appendix H Polyak and Primal Averaging Runs

These experiments follow the same tuning setup as Figure 5 , where the learning rate and momentum is tuned separately for each method. In each case the c c weighting sequence used for Schedule-Free training is also used to ensure a fair comparison. The Polyak averaging runs include momentum in the base optimizer as we found this gave the best results. We ran the NanoGPT experiment for a shorter 200,000 steps due to computational budget considerations. The NanoGPT Polyak averaging runs show a divergence in test loss for Polyak averaging.

## Appendix I Additional LR Sensitivity Plots

## Instructions for reporting errors

We are continuing to improve HTML versions of papers, and your feedback helps enhance accessibility and mobile support. To report errors in the HTML that will help us improve conversion and rendering, choose any of the methods listed below:

Click the "Report Issue" ( ) button, located in the page header.

Tip: You can select the relevant text first, to include it in your report.

Our team has already identified the following issues . We appreciate your time reviewing and reporting rendering errors we may not have found yet. Your efforts will help us improve the HTML versions for all readers, because disability should not be a barrier to accessing research. Thank you for your continued support in championing open access for all.

Have a free development cycle? Help support accessibility at arXiv! Our collaborators at LaTeXML maintain a list of packages that need conversion , and welcome developer contributions .
