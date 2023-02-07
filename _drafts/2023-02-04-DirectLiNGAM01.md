---
title: 01-DirectLiNGAM
tags:
    - Statistics
    - Causal Inference  
    - Graphical
    - Papers
---

이번에 리뷰할 논문은 _DirectLiNGAM: A Direct Method for Learning a Linear non-Gaussian Structural Equation Model_ 로, _A Linear Non-Gaussian Acyclic Model for Causal Discovery_ 의 후속 연구이다. 해당 논문에서는 ICA 알고리즘을 활용하여 connectivity matrix를 추정했는데, ICA 알고리즘은 iterative search algorithm을 사용하고 있기 때문에 global minima 대신 local minima에 도달할 위험이 있기 때문에 그러한 측면에서 한계점이 있었다. 이 논문에서는 non-Gaussianity 하에서 connectivity matrix를 추정하는 direct한 방법을 제안한다. 이 알고리즘에서는 learning rate와 같은 파라미터가 따로 요구되지 않으며, __데이터가 몇 가지 assumption들을 충족한다면 최적해에 도달한다는 것을 증명할 수 있다.__

<!--more-->

> In contrast to the previous methods, our algorithm requires no algorithmic parameters and is guaranteed to converge to the right solution within a small fixed number of steps if the data strictly follows the model, that is, if all the model assumption are met and the sample size is infinite.







## Reference

* <a href="https://www.jmlr.org/papers/volume7/shimizu06a/shimizu06a.pdf">A Linear Non-Gaussian Acyclic Model for Causal Discovery</a>

* <a href="https://stats.stackexchange.com/questions/87000/sample-acf-and-pacf-of-a-random-walk">Sample ACF and PACF of a random walk</a>

* 이상열. (2013). 시계열 분석 이론 및 SAS 실습(pp.142~191). 자유아카데미.
