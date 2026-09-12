##### Report GitHub Issue

Content selection saved. Describe the issue below:

# Fully parallel optical matrix-matrix multiplication

In recent years, with the rapid development of electro-optic modulators, optical computing has become a potential excellent candidate for various computing tasks. New structures and devices for optical computing are emerging one after another, but the computing method is still the optical vector-matrix multiplication method that was decades ago. Here, we propose a novel optical computing paradigm that can parallelly implement matrix-matrix multiplication operation, which can directly replace existing vector-matrix multiplication, greatly improving computational efficiency. This preprint presents theoretical analysis, and we will supplement experimental results and conclusions in the future.

## 1 Introduction

Matrix-matrix multiplication (MMM) is one of the core operations in computational and processing applications, widely used in signal processing, image processing, and deep learning. For its O ⁡ ( N 3 ) O(N^{3}) time complexity, MMM, which is composed of multiple vector-matrix multiplications (VMM), becomes the most time-consuming operation in various calculation task. Due to the low performance of early computer technology, light has emerged as one of the ideal medium for replacing digital computing due to its excellent characteristics of low latency and low power consumption. Since Dr. Goodman innovatively proposed the optical vector-matrix multiplications (OVMM) prototype [ 1 ] , many researchers have utilized methods such as time multiplexing, wavelength multiplexing, and light source multiplexing to achieve more effective OVMM [ 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9 , 10 ] . In addition to free space, Dr. Reck proposed a computational architecture based on Mach-Zehnder interferometer, verifying the possibility of calculations based on planar waveguides [ 11 ] . However, with the rapid development of integrated circuits and silicon based chip technology, optical computing, which is difficult to reconstruct structures and cannot update data in real-time, has no advantages compared to digital computing. Therefore, the academic community has also paid more attention to the field of optical communication, resulting in the long-term stagnation of the development of optical computing.

In the 2010s, with the rise of technologies such as artificial intelligence and big data, massive MMM operations brought huge computational burden, and silicon based chips were unable to continue to meet computing needs. At the same time, with the development of reconfigurable spatial light modulators (SLM) and photonic integrated circuits [ 12 , 13 , 14 ] , optical computing is once again recognized as a potential high-performance computing solution [ 15 , 16 , 17 ] . Many researchers have implemented various forms of optical computing systems using free space and planar waveguides, and used them for training or inference of optical neural networks (ONNs) [ 18 , 19 , 20 , 21 , 22 , 23 , 24 , 25 , 26 , 27 , 28 , 29 , 30 ] . However, these systems still use decades ago OVMM methods, simply replacing traditional optical devices with higher speed, larger scale, and more reconfigurable advanced devices. For example, using lenslet arrays or Dammann gratings instead of traditional multiple light sources to implement convolutional neural networks [ 31 , 32 , 33 ] , using waveshapers and optical frequency combs instead of traditional four-wave mixing to achieve wavelength multiplexing computing [ 21 , 23 , 34 , 35 ] , and using SLMs instead of traditional LED arrays and phase masks to achieve OVMMs [ 18 , 28 , 36 , 37 ] . Although the above works have greatly developed the equipment and combination strategies of optical computing, and effectively improved the actual performance of traditional optical computing methods, they have not fundamentally proposed more efficient optical computing principles.

Here, we innovatively proposed a fully parallelized optical matrix-matrix multiplication (POMMM) paradigm, which fundamentally changed Dr. Goodman’s OVMM method. The difference from previous methods is that our method does not require any pre-coding or pre-processing of matrixs, and the computing operation is completed through the propagation of light with single source and single wavelength. This method has a simple and exquisite architecture, making it a universal computing method that is very suitable for accelerating ONNs and other optical computing operations. POMMM adds an additional computational dimension to the ONN, enabling parallel training and inference of multiple samples and neurons. In addition to OVMM and 2-D convolution operations, this method has the potential to become another new parallel computing paradigm for Fourier optics.

## 2 Principle

### 2.1 Architecture of POMMM

For MMM, assuming matrix A A (N rows, M columns) and matrix B B (M rows, N columns), then matrix C = A ​ B C=AB (N rows, N columns), the value c n ​ m c_{nm} of the n-th row and m-th column of C C can be expressed as: c n ​ m = ∑ i = 1 M a n ​ i ​ b i ​ m . c_{nm}=\sum_{i=1}^{M}{a_{ni}b_{im}}. (1) Based on the above equation, we summarize the core steps of POMMM as (1) parallel implementation of row and column multiplication and addition (MAC) operations, and (2) moving the results to different positions, and design the architecture as shown in Fig.1.

The matrix A A is modulated to the amplitude of wavefront by an amplitude spatial light modulator (ASLM), and is imaged to the surface of phase spatial light modulator (PSLM) by a 4f system. PSLM will modulate a linearly changing phase along the x-direction (m) for each row of the matrix, and change its rate K ⁡ ( n ) K(n) along the y-direction (n) direction: 2 ​ π ​ K ​ ( n ) ​ m 2\pi K(n)m . So the modulated wavefront can be represented by complex exponents, as shown in matrix A ′ A^{\prime} in Fig.1. Then, the wavefront is imaged along the x-direction on the ASLM2 surface through a cylindrical lens, and the y-direction is the result of free diffraction. Therefore, every point on the ASLM2 surface is a complex sum of matrix A ′ A^{\prime} along the y-direction, while the relationship in the x-direction remains unchanged, as shown in matrix A ′′ A^{\prime\prime} in Fig.1. Transpose matrix B B and flip it along the y-direction to matrix B T ​ F B^{TF} , which is modulated to the wavefront through ASLM2 to achieve dot product ( ⊙ \odot ) with the corresponding position of matrix A ′′ A^{\prime\prime} : b n ​ m T ​ F ⊙ a n ​ m ′′ = b n ​ m T ​ F ​ ∑ i = 1 N a i ​ m ​ e j ​ 2 ​ π ​ K ​ ( i ) ​ m . b^{TF}_{nm}\odot a^{\prime\prime}_{nm}=b^{TF}_{nm}\sum_{i=1}^{N}a_{im}e^{j2\pi K(i)m}. (2) From the perspective of spatial frequency domain, the above equation indicates that each row of the matrix contains N spatial frequency components K ⁡ ( 1 ) ​ K ​ ( N ) K(1)~K(N) , and the amplitude of the i-th frequency component on position (n,m) is the dot product of a n ​ m a_{nm} and b n ​ m T ​ F b^{TF}_{nm} . By combining a 2-D lens with a x-direction cylindrical lens, imaging along y-direction and focusing (optical Fourier transform) along x-direction can be achieved, which is similar to traditional OVMM. According to the principle of optical Fourier transform, when focusing along x-direction, N frequency components correspond to N focal points along x-direction, and the intensity of the n-th focal point is related to the sum amplitude of M points: ∑ i = 1 M a i ​ n ​ b n ​ i T ​ F \sum_{i=1}^{M}a_{in}b^{TF}_{ni} . Fig.2 illustrates this process more vividly compared to traditional OVMM.

Obviously, a N × N N\times N -sized Matrix is composed by N frequency components in N rows captured by the qCMOS, which is the transposition of matrix C C .

### 2.2 ONN based on POMMM

The most time-consuming part of neural network training and inference is the convolutional layer and fully connected layer, which are the parts that most ONNs attempts to accelerate. The principles of convolutional layer and fully connected layer are both based on VMM. As shown in Fig.3, the convolutional layer is to achieve the inner product of the slices with the convolutional kernels to form a new sample, the fully connected layer is to achieve VMM on samples and weight matrix ( ω n ​ m \omega_{n}m and ω i ​ j \omega_{i}j ). For convolutional layers, POMMM can process multiple convolutional kernels ( k m ​ 1 k_{m}1 , k m ​ 2 k_{m}2 ,…) in parallel, which is very effective for multi feature extraction. The fully connected layer based on POMMM can process multiple samples ( a 1 ​ m a_{1}m , a 2 ​ m a_{2}m ,…) in parallel, greatly improving computational speed. By comparison, simply replacing the existing OVMM with our POMMM can achieve parallel convolutional layer and fully connected layer processing, greatly improving training and inference of ONNs.

## References

[1] J. W. Goodman, A. R. Dias, and L. M. Woody, “Fully parallel, high-speed incoherent optical method for performing discrete fourier transforms,” Opt. Lett. 2 , 1–3 (1978).

[2] P. M. Duffieux, The Fourier transform and its applications to optics (Wiley, 1983).

[3] N. H. Farhat, D. Psaltis, A. Prata, and E. Paek, “Optical implementation of the hopfield model,” Appl. Opt. 24 , 1469–1475 (1985).

[4] C. Gu, S. Campbell, and P. Yeh, “Matrix-matrix multiplication by using grating degeneracy in photorefractive media,” Opt. Lett. 18 , 146–148 (1993).

[5] J. Hong and P. Yeh, “Photorefractive parallel matrix–matrix multiplier,” Opt. Lett. 16 , 1343–1345 (1991).

[6] Y. Fainman, C. C. Guest, and S. H. Lee, “Optical digital logic operations by two-beam coupling in photorefractive material,” Appl. Opt. 25 , 1598–1603 (1986).

[7] P. Yeh and A. E. T. Chiou, “Optical matrix–vector multiplication through four-wave mixing in photorefractive media,” Opt. Lett. 12 , 138–140 (1987).

[8] C.-C. Sun, M.-W. Chang, and K. Y. Hsu, “Matrix–matrix multiplication by using anisotropic self-diffraction in batio3,” Appl. Opt. 33 , 4501–4507 (1994).

[9] E. P. Mosca, R. D. Griffin, F. P. Pursel, and J. N. Lee, “Acoustooptical matrix-vector product processor: implementationissues,” Appl. Opt. 28 , 3843–3851 (1989).

[10] Y.-D. Wu, D.-S. Shen, V. Bykovsky, J. Rosetti, and M. Fiddy, “Digital optical computing with magneto-optic spatial light modulators: a new and efficient multiplication algorithm,” Applied optics 33 , 7572–7578 (1994).

[11] M. Reck, A. Zeilinger, H. J. Bernstein, and P. Bertani, “Experimental realization of any discrete unitary operator,” Phys. Rev. Lett. 73 , 58–61 (1994).

[12] C.-d. Liao and J.-c. Tsai, “The evolution of mems displays,” IEEE Transactions on Industrial Electronics 56 , 1057–1065 (2009).

[13] P. Ambs, “Optical computing: A 60-year adventure.” Advances in Optical Technologies (2010).

[14] Y. Shen, N. C. Harris, S. Skirlo, M. Prabhu, T. Baehr-Jones, M. Hochberg, X. Sun, S. Zhao, H. Larochelle, D. Englund et al. , “Deep learning with coherent nanophotonic circuits,” Nature photonics 11 , 441–446 (2017).

[15] H. J. Caulfield and S. Dolev, “Why future supercomputing requires optics,” Nature Photonics 4 , 261–263 (2010).

[16] J. Wu, X. Lin, Y. Guo, J. Liu, L. Fang, S. Jiao, and Q. Dai, “Analog optical computing for artificial intelligence,” Engineering 10 , 133–145 (2022).

[17] G. Wetzstein, A. Ozcan, S. Gigan, S. Fan, D. Englund, M. Soljačić, C. Denz, D. A. Miller, and D. Psaltis, “Inference in artificial intelligence with deep optics and photonics,” Nature 588 , 39–47 (2020).

[18] J. Bueno, S. Maktoobi, L. Froehly, I. Fischer, M. Jacquot, L. Larger, and D. Brunner, “Reinforcement learning in a large-scale photonic recurrent neural network,” Optica 5 , 756–760 (2018).

[19] J. Chang, V. Sitzmann, X. Dun, W. Heidrich, and G. Wetzstein, “Hybrid optical-electronic convolutional neural networks with optimized diffractive optics for image classification,” Scientific reports 8 , 1–10 (2018).

[20] X. Lin, Y. Rivenson, N. T. Yardimci, M. Veli, Y. Luo, M. Jarrahi, and A. Ozcan, “All-optical machine learning using diffractive deep neural networks,” Science 361 , 1004–1008 (2018).

[21] X. Xu, M. Tan, B. Corcoran, J. Wu, A. Boes, T. G. Nguyen, S. T. Chu, B. E. Little, D. G. Hicks, R. Morandotti et al. , “11 tops photonic convolutional accelerator for optical neural networks,” Nature 589 , 44–51 (2021).

[22] T. Fu, Y. Zang, Y. Huang, Z. Du, H. Huang, C. Hu, M. Chen, S. Yang, and H. Chen, “Photonic machine learning with on-chip diffractive optics,” Nature Communications 14 , 70 (2023).

[23] J. Feldmann, N. Youngblood, M. Karpov, H. Gehring, X. Li, M. Stappers, M. Le Gallo, X. Fu, A. Lukashchuk, A. S. Raja et al. , “Parallel convolutional processing using an integrated photonic tensor core,” Nature 589 , 52–58 (2021).

[24] S. Xu, J. Wang, H. Shu, Z. Zhang, S. Yi, B. Bai, X. Wang, J. Liu, and W. Zou, “Optical coherent dot-product chip for sophisticated deep learning regression,” Light: Science & Applications 10 , 221 (2021).

[25] L. Leng, Z. Zeng, G. Wu, Z. Lin, X. Ji, Z. Shi, and W. Jiang, “Phase calibration for integrated optical phased arrays using artificial neural network with resolved phase ambiguity,” Photonics Research 10 , 347–356 (2022).

[26] C. Liu, Q. Ma, Z. J. Luo, Q. R. Hong, Q. Xiao, H. C. Zhang, L. Miao, W. M. Yu, Q. Cheng, L. Li et al. , “A programmable diffractive deep neural network based on a digital-coding metasurface array,” Nature Electronics 5 , 113–122 (2022).

[27] T. Zhou, X. Lin, J. Wu, Y. Chen, H. Xie, Y. Li, J. Fan, H. Wu, L. Fang, and Q. Dai, “Large-scale neuromorphic optoelectronic computing with a reconfigurable diffractive processing unit,” Nature Photonics 15 , 367–373 (2021).

[28] J. Spall, X. Guo, and A. I. Lvovsky, “Hybrid training of optical neural networks,” Optica 9 , 803–811 (2022).

[29] L. G. Wright, T. Onodera, M. M. Stein, T. Wang, D. T. Schachter, Z. Hu, and P. L. McMahon, “Deep physical neural networks trained with backpropagation,” Nature 601 , 549–555 (2022).

[30] Z. Chen, A. Sludds, R. Davis III, I. Christen, L. Bernstein, L. Ateshian, T. Heuser, N. Heermeier, J. A. Lott, S. Reitzenstein et al. , “Deep learning with coherent vcsel neural networks,” Nature Photonics pp. 1–8 (2023).

[31] Z. Gu, Y. Gao, and X. Liu, “Optronic convolutional neural networks of multi-layers with different functions executed in optics for image classification,” Opt. Express 29 , 5877–5889 (2021).

[32] G. Ma, J. Yu, R. Zhu, and C. Zhou, “Optical multi-imaging&#x2013;casting accelerator for fully parallel universal convolution computing,” Photon. Res. 11 , 299–312 (2023).

[33] G. Ma, J. Yu, R. Zhu, F. Zheng, C. Zhou, and G. Situ, “Dammann gratings-based truly parallel optical matrix multiplication accelerator,” Opt. Lett. 48 , 2301–2304 (2023).

[34] Y. Tao, F. Yang, Z. Tao, L. Chang, H. Shu, M. Jin, Y. Zhou, Z. Ge, and X. Wang, “Fully on-chip microwave photonic instantaneous frequency measurement system,” Laser & Photonics Reviews 16 , 2200158 (2022).

[35] Y. Huang, W. Zhang, F. Yang, J. Du, and Z. He, “Programmable matrix operation with reconfigurable time-wavelength plane manipulation and dispersed time delay,” Opt. Express 27 , 20456–20467 (2019).

[36] J. Spall, X. Guo, T. D. Barrett, and A. I. Lvovsky, “Fully reconfigurable coherent optical vector–matrix multiplication,” Opt. Lett. 45 , 5752–5755 (2020).

[37] M. Miscuglio, Z. Hu, S. Li, J. K. George, R. Capanna, H. Dalir, P. M. Bardet, P. Gupta, and V. J. Sorger, “Massively parallel amplitude-only fourier neural network,” Optica 7 , 1812–1819 (2020).

## Instructions for reporting errors

We are continuing to improve HTML versions of papers, and your feedback helps enhance accessibility and mobile support. To report errors in the HTML that will help us improve conversion and rendering, choose any of the methods listed below:

Click the "Report Issue" ( ) button, located in the page header.

Tip: You can select the relevant text first, to include it in your report.

Our team has already identified the following issues . We appreciate your time reviewing and reporting rendering errors we may not have found yet. Your efforts will help us improve the HTML versions for all readers, because disability should not be a barrier to accessing research. Thank you for your continued support in championing open access for all.

Have a free development cycle? Help support accessibility at arXiv! Our collaborators at LaTeXML maintain a list of packages that need conversion , and welcome developer contributions .
