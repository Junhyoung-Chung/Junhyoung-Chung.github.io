---
title: Bootstrap
tags:
    - Statistics
    - Statistics-etc
---

지금 비모수통계 및 실습 수업에서 bootstrapping 기법을 배우고 있는 중인데, 워낙 통계학에서 자주 사용되는 기법 중 하나인지라 내가 아는 만큼 정리해두려고 한다. 아직 정확하게 찾아본 것이 아니고 나의 생각을 수학적으로 표현해둔 것이기 때문에 표현에 abusing이 있을 수 있고, 또 틀렸을 수도 있다. 나중에 다시 한번 시간날 때 찾아보고 제대로 공부해보자.

<!--more-->

---

# Bootstrap

## Motivation

$$
X_1,X_2,\dots,X_n \overset{i.i.d.}{\sim} N(\mu,\sigma^2)
$$

에서 $\sigma$는 알려져 있고, $\mu$를 추정하고자 하는 상황에 대해 생각해보자.

아무래도 표본평균을 사용할 것이다. 즉,

$$
\hat{\mu} = \frac{1}{n}\mathbf{1}_n^T\mathbf{X} = \bar{X}_n
$$

모집단의 분포를 알고 있기 때문에 우리는 쉽게 $\hat{\mu}$의 분포를 계산할 수 있다.

$$
\hat{\mu} \sim N(\mu,\frac{\sigma^2}{n})
$$

이제 조금 더 일반화하여 생각해보자. $X_1,X_2,\dots,X_n$이 $i.i.d.$ 하게 평균이 $\mu$, 분산이 $\sigma^2$ 인 분포를 따른다. 이 때 분포가 무엇인지는 알 수 없다.

$X_1,X_2,\dots,X_n$을 활용하여 어떤 모수 $\theta$를 추정하고자 할 때 우리는 $\hat{\theta} = f(\mathbf{X})$ 를 사용할 것이다. 여기서 $\hat{\theta}$의 분포를 어떻게 하면 알 수 있을까?

수학적으로는 당연히 알 수 없다. 모집단의 분포를 모르기 때문이다.

**이 때, $\hat{\theta}$의 분포를 근사적으로 추정하기 위해 제안된 기법이 바로 bootstrap이다.**

## Principle

$X_1,X_2,\dots,X_n$에서 총 $n$개의 표본을 복원추출한다. 복원추출한 표본들을 $X^{(1)}_1,X^{(1)}_2,\dots,X^{(1)}_n$이라 할 때, 

$$
\hat{\theta}^{(1)} = f(X^{(1)}_1,X^{(1)}_2,\dots,X^{(1)}_n)
$$

으로 $\hat{\theta}^{(1)}$을 만든다. 그리고 이러한 과정을 $B$번 반복하여

$$
\hat{\Theta} = \{ \hat{\theta}^{(1)},\hat{\theta}^{(2)},\dots,\hat{\theta}^{(B)} \}
$$

를 수집한다. 그 다음

$$
P(\hat{\theta} \leq c) \approx \frac{1}{B}\sum_{i=1}^{B}{I(\hat{\theta}^{(i)} \leq c)}
$$

으로 근사하는 것이다. 아이디어는 굉장히 간단하다!

## Mathematical Background

수학적으로 이 기법이 정당화되려면 바로 (6)번 식에서의 근사가 얼마나 타당한지를 수학적으로 보여줄 수 있어야 한다. 이를 한번 확인해보도록 하자.

### $B \to \infty$

우선

$$
\frac{1}{B}\sum_{i=1}^{B}{I(\hat{\theta}^{(i)} \leq c)}
$$

에서 $B$가 무한대로 간다면 어디로 수렴하게 될까?

$$
I(\hat{\theta}^{(1)} \leq c),I(\hat{\theta}^{(2)} \leq c),\dots,I(\hat{\theta}^{(B)} \leq c) \overset{i.i.d.}{\sim} \text{Ber}(P(\hat{\theta}^{(1)} \leq c))
$$

임을 생각할 때, (7)번 식은 표본평균의 형태로 바라볼 수 있다. 따라서 대수의 법칙에 따라

$$
\frac{1}{B}\sum_{i=1}^{B}{I(\hat{\theta}^{(i)} \leq c)} \overset{p}{\underset{B \to \infty}{\to}} \mathbf{E}[I(\hat{\theta}^{(1)} \leq c)] = P(\hat{\theta}^{(1)} \leq c)
$$

로 수렴하게 된다.

하지만 여전히

$$
P(\hat{\theta} \leq c) \neq P(\hat{\theta}^{(1)} \leq c)
$$

이다. 이제 $n \to \infty$일 때 두 확률이 얼마나 서로 닮게 될지 확인해볼 필요가 있다.

### $n \to \infty$

직관적으로 생각했을 때에는 $\hat{\theta}$의 분포가 특정 분포 $L$에 수렴하고 $\hat{\theta}^{(1)}$의 분포가 분포 $L^\ast$에 수렴하는데, $L$과 $L^\ast$이 충분히 가까워서 결국 $\hat{\theta}$와 $\hat{\theta}^{(1)}$의 극한 분포가 같다는 방식으로 보일 수 있을 것 같은데 아직 증명이 생각이 나질 않는다. 내 수준을 뛰어넘는 증명일 것 같다는 느낌이 확 들어서,, 일단은 패스

## Reference

* 정성규. 비모수통계학 with R. 자유아카데미