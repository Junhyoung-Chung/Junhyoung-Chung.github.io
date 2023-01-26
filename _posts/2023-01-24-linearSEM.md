---
title: Linear SEMs
tags:
    - statistics
    - causalinference
    - graphical
---

Linear Structural Equation Models(SEMs)는 인과추론의 가장 기본적인 모델로 정말 폭넓은 분야에서 많이 쓰인다고 한다!

모델은 아래와 같다.

$$
\mathbf{x}=B\mathbf{x}+\mathbf{e}
$$

여기서 $\mathbf{e}$는 jointly independent한 error term이다.

<!--more-->

쉽계 예시를 들어 생각해보면

$$
\begin{aligned}
 & x_1 = e_1
 \newline & x_2 = 1.2x_1-0.3x_4+e_2
 \newline & x_3 = 2x_2+e_3
 \newline & x_4 = -x_3+e_4
 \newline & x_5 = 3x_5+e_5
\end{aligned}
$$

라 할 때,

$$
B = \left[
\begin{matrix}
    0 & 0 & 0 & 0 & 0
    \newline 1.2 & 0 & 0 & -0.3 & 0
    \newline 0 & 2 & 0 & 0 & 0
    \newline 0 & 0 & -1 & 0 & 0
    \newline 0 & 0 & 0 & 0 & 3
\end{matrix}
\right]
$$

이 되는 것이다. 이를 그림으로 나타내면,

![example-graph](/assets/images/linear-sems.jpg)

가 되겠다.

쉽네요!

Reference

* <a href="https://arxiv.org/pdf/1206.3273.pdf">Discovering Cyclic Causal Models by Independent Components Analysis</a>
