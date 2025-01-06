---
title: Multiple Comparisons
tags:
    - Statistics
    - Statistics-etc
---

유의수준 $\alpha$ 하에서 $r$개의 가설검정을 진행하는 프로세스를 생각해보자.

$$
H_{0i} \quad \text{vs.} \quad H_{1i} \quad i=1,\dots,r
$$

이 때 우리는 이 큰 프로세스의 유의수준을 어떻게 생각해야 할까?

<!--more-->

직관적으로

$$
\alpha_{FW} = P(\text{at least one type I error occurs given all }H_{0i}\text{s are true})
$$

를 생각해볼 수 있다. 이 때 만약 모든 가설검정이 독립적으로 수행될 수 있다고 해보자. 그렇다면,

$$
\alpha_{FW}=1-(1-\alpha)(1-\alpha)\dots(1-\alpha)=1-(1-\alpha)^r
$$

이 된다. 여기서 문제는,

$$
\lim_{r \to \infty}{\alpha_{FW}}=1
$$

이라는 점이다. 즉, 내가 수행하고자 하는 가설검정의 개수가 많아지면 많아질수록 이 하나의 큰 프로세스에서 1종 오류를 범할 확률이 1에 가까워진다는 뜻이다.

그렇다면 이 부분을 어떻게 해결할 수 있을까?

Bonferroni는 $\alpha/r$을 한 가설검정의 유의수준으로 둘 것을 제안했다. 이렇게 두면 어떤 일이 일어날까?

다음과 같은 부등식을 생각해보자.

$$
P(\bigcup_{i=1}^r{A_i}) \leq \sum_{i=1}^r{P(A_i)}
$$

만약 $A_i$를 $i$번째 가설검정에서 1종의 오류가 발생하는 사건이라 하면,

$$
\alpha_{FW}=P(\bigcup_{i=1}^r{A_i})
$$

이 된다.

따라서,

$$
\alpha_{FW} \leq \sum_{i=1}^r{P(A_i)}=\alpha
$$

가 된다. 아마 정확하게 극한값을 구해보자면,

$$
\lim_{r \to \infty}{\alpha_{FW}}=1-\lim_{r \to \infty}{\left(1-\frac{\alpha}{r}\right)^r}=1-e^{-\alpha}
$$

가 되겠다. 하튼 이렇게 문제를 해결하는 방법이 있다. 다만 내가 가설검정을 많이 해야할수록 하나하나의 유의수준이 너무 작아져 귀무가설을 기각하기가 힘들다는 단점이 있다. 실제로 찾아보니 Bonferroni의 방법은 매우 "conservative"하다고 한다.

다른 많은 방법들도 있지만 Multiple Comparison 문제는 하나의 통일된 방법이 있는 것 같지는 않아 보여서 가장 유명한 방법 하나만 소개했다.

## Reference

* <a href="https://en.wikipedia.org/wiki/Multiple_comparisons_problem">Multiple Comparisons Problem</a>