# Review

## Summary
This paper proposes a new optimizer, NorMuon, which combines Muon and Adam-mini. The authors observe that while Muon improves the conditioning of the optimization trajectory, it can result in highly non-uniform update norms across neurons. To address this issue, they incorporate Adam-mini’s per-neuron adaptive learning rates, which balances out the update norms. The authors also implement a distributed version of NorMuon using the FSDP2 framework. Experimental results show that NorMuon outperforms both Muon and Adam.

## Soundness
3

## Presentation
3

## Contribution
3

## Strengths
- The authors observe an interesting phenomenon: while Muon improves the conditioning of the optimization trajectory, it can result in highly non-uniform update norms across neurons.
- The authors propose a simple yet effective method to address the issue observed.
- The authors implement a distributed version of NorMuon using the FSDP2 framework.
- Experimental results show that NorMuon outperforms both Muon and Adam.

## Weaknesses
- The paper does not address the issue of sign flipping, a common problem in Adam-mini [1]. Since NorMuon combines Muon and Adam-mini, it is likely that NorMuon may also experience sign flipping. The authors should provide more details on this issue and offer potential solutions to address it.
- The paper does not include comparisons with other second-order optimizers, such as KFAC and SOAP. The authors should include these baselines to provide a more comprehensive evaluation of NorMuon.
- The paper lacks an analysis of the convergence properties of NorMuon. The authors should provide a theoretical analysis of the convergence properties of their proposed optimizer.
- The paper does not discuss the performance of NorMuon on different learning rate schedules. The authors should include experiments to evaluate the performance of NorMuon under different learning rate schedules, such as cosine annealing and trapezoidal learning rate schedules.
- The paper does not provide a detailed analysis of the impact of the beta2 value on the performance of NorMuon. The authors should include experiments to evaluate the performance of NorMuon with different beta2 values and provide a discussion on the impact of this hyperparameter on the optimizer's performance.

[1] Zhang, Y., Chen, C., Li, H., Ding, T., Wei, Y., & Sun, R. (2025). Adam-mini: Use fewer learning rates to gain more. arXiv preprint arXiv: 2506.16225.

## Questions
- Does NorMuon experience sign flipping, and if so, how does it address this issue?
- How does NorMuon compare to other second-order optimizers like KFAC and SOAP?
- What are the convergence properties of NorMuon?
- How does the choice of learning rate schedule affect the performance of NorMuon?
- What is the impact of the beta2 value on the performance of NorMuon?

## Flag For Ethics Review
No ethics review needed.

## Details Of Ethics Concerns


## Rating
6

## Confidence
4