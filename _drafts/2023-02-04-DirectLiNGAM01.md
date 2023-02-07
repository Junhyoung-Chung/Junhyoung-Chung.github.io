---
title: 01-DirectLiNGAM
tags:
    - Statistics
    - Causal Inference  
    - Graphical
    - Papers
---

이번에 리뷰할 논문은 _**DirectLiNGAM: A Direct Method for Learning a Linear non-Gaussian Structural Equation Model**_ 로, _A Linear Non-Gaussian Acyclic Model for Causal Discovery_ 의 후속 연구이다. 기존의 LiNGAM은 ICA 알고리즘을 활용하여 connectivity matrix를 추정한다. 하지만 ICA 알고리즘은 iterative search algorithm을 사용하고 있기 때문에 global optima 대신 local optima에 도달할 위험이 있다. 이 논문에서는 non-Gaussianity 하에서 connectivity matrix를 추정하는 direct한 방법을 제안한다. 이 알고리즘에서는 learning rate와 같은 파라미터가 따로 요구되지 않으며, __데이터가 몇 가지 assumption들을 충족한다면 최적해에 도달한다는 것을 증명할 수 있다.__

<!--more-->

> In contrast to the previous methods, our algorithm requires no algorithmic parameters and is guaranteed to converge to the right solution within a small fixed number of steps if the data strictly follows the model, that is, if all the model assumption are met and the sample size is infinite.

## A Direct Method: DirectLiNGAM

### Identification of an Exogenous Variable Based on Non-Gaussianity and Independence

이 파트에서는 논문에서 제안하는 알고리즘이 성립하기 위해 필요한 몇 가지 명제들을 증명한다. 기본적인 흐름은 아래와 같다.

---

1. 외생 변수를 찾는다. 찾는 방법은 Lemma 1을 활용한다.
2. 다른 변수들에서 외생 변수의 효과를 Least Squares Regression을 활용하여 제거한다.
3. LiNGAM이 잔차들에 대해서도 동일하게 성립하기 때문에 (Lemma 2, Corollary 1) 잔차를 활용하여 외생 변수 다음에 오는 변수를 찾는다.
4. ordering을 전부 찾을 때까지 잔차들에 대해서 1번부터 반복한다.

---
   
이제 수학적인 증명들을 알아보도록 하자.

먼저 논문에서 주장하는 명제들을 증명하기 위해서는 아래의 Theorem이 필요하다.

__Thoerem 1 (Darmois-Skitovitch theorem)__

> Define two random variables $y_1$ and $y_2$ as linear combinations of independent random variables $s_i (i=1,\dots,q)$:
> 
> $$
> y_1 = \sum_{i=1}^{q}{\alpha_is_i}, \quad y_2 = \sum_{i=1}^{q}{\beta_is_i}
> $$
>
> Then, if $y_1$ and $y_2$ are independent, all variables $s_j$ for which $\alpha_j\beta_j \neq 0$ are Gaussian.

궁금해서 증명을 찾아보긴 했는데,, 내 수준을 넘어가는 증명인 것 같다. 일단 논문에서도 이 theorem을 활용만 하고 있으니까 일단 사실로 받아들여야겠다. 이 theorem의 대우가 중요하다. __즉, $\alpha_j\beta_j \neq 0$인 non-Gaussian random variable $s_j$가 존재하면 $y_1$과 $y_2$는 서로 dependent하다.__







## Reference

* <a href="https://www.jmlr.org/papers/volume7/shimizu06a/shimizu06a.pdf">A Linear Non-Gaussian Acyclic Model for Causal Discovery</a>

* <a href="https://stats.stackexchange.com/questions/87000/sample-acf-and-pacf-of-a-random-walk">Sample ACF and PACF of a random walk</a>

* 이상열. (2013). 시계열 분석 이론 및 SAS 실습(pp.142~191). 자유아카데미.
