---
title: 01-DirectLiNGAM
tags:
    - Statistics
    - Causal Inference  
    - Graphical
    - Papers
---

이번에 리뷰할 논문은 _**DirectLiNGAM: A Direct Method for Learning a Linear non-Gaussian Structural Equation Model**_ 로, _A Linear Non-Gaussian Acyclic Model for Causal Discovery_ 의 후속 연구이다. 기존의 LiNGAM은 ICA 알고리즘을 활용하여 connectivity matrix를 추정한다. 하지만 ICA 알고리즘은 iterative search algorithm을 사용하고 있기 때문에 global optima 대신 local optima에 도달할 위험이 있다. 이 논문에서는 non-Gaussianity 하에서 connectivity matrix를 추정하는 direct한 방법을 제안한다. 이 알고리즘에서는 learning rate와 같은 파라미터가 따로 요구되지 않으며, **데이터가 몇 가지 assumption들을 충족한다면 최적해에 도달한다는 것을 증명할 수 있다.**

<!--more-->

> In contrast to the previous methods, our algorithm requires no algorithmic parameters and is guaranteed to converge to the right solution within a small fixed number of steps if the data strictly follows the model, that is, if all the model assumption are met and the sample size is infinite.

## A Direct Method: DirectLiNGAM

### Identification of an Exogenous Variable Based on Non-Gaussianity and Independence

우선 편의를 위해 다음 식 세 개를 써놓고 시작하자.

$$
x_i = \sum_{k(j) < k(i)}b_{ij}x_j+e_i 
$$

$$
\mathbf{x}=\mathbf{Bx}+\mathbf{e}
$$

$$
\mathbf{x}=\mathbf{Ae}
$$

이 파트에서는 논문에서 제안하는 알고리즘이 성립하기 위해 필요한 몇 가지 명제들을 증명한다. 기본적인 흐름은 아래와 같다.

---

1. 외생 변수를 찾는다. 찾는 방법은 Lemma 1을 활용한다.
2. 다른 변수들에서 외생 변수의 효과를 Least Squares Regression을 활용하여 제거한다.
3. LiNGAM이 잔차들에 대해서도 동일하게 성립하기 때문에 (Lemma 2, Corollary 1) 잔차를 활용하여 외생 변수 다음에 오는 변수를 찾는다.
4. ordering을 전부 찾을 때까지 잔차들에 대해서 1번부터 반복한다.

---
   
이제 수학적인 증명들을 알아보도록 하자.

먼저 논문에서 주장하는 명제들을 증명하기 위해서는 아래의 Theorem이 필요하다.

**Thoerem 1 (Darmois-Skitovitch theorem)**

> Define two random variables $y_1$ and $y_2$ as linear combinations of independent random variables $s_i (i=1,\dots,q)$:
> 
> $$
> y_1 = \sum_{i=1}^{q}{\alpha_is_i}, \quad y_2 = \sum_{i=1}^{q}{\beta_is_i}
> $$
>
> Then, if $y_1$ and $y_2$ are independent, all variables $s_j$ for which $\alpha_j\beta_j \neq 0$ are Gaussian.

궁금해서 증명을 찾아보긴 했는데,, 내 수준을 넘어가는 증명인 것 같다. 일단 논문에서도 이 theorem을 활용만 하고 있으니까 일단 사실로 받아들여야겠다. 이 theorem의 대우가 중요하다. **즉, $\alpha_j\beta_j \neq 0$인 non-Gaussian random variable $s_j$가 존재하면 $y_1$과 $y_2$는 서로 dependent하다.**

**Lemma 1**

> Assume that the input data $\mathbf{x}$ strictly follows the LiNGAM (2), that is, all the model assumptions are met and the sample size is infinite. Denote by $r_i^{(j)}$ the residual when $x_i$ is regressed on $x_j$: $r_i^{(j)}=x_i-\frac{Cov(x_i,x_j)}{Var(x_j)}x_j (i \neq j)$. Then a variable $x_j$ is exogenous if and only if $x_j$ is independent of its residuals $r_i^{(j)}$ for all $i \neq j$.

의미를 한번 생각해보자. 

> Denote by $r_i^{(j)}$ the residual when $x_i$ is regressed on $x_j$: $r_i^{(j)}=x_i-\frac{Cov(x_i,x_j)}{Var(x_j)}x_j (i \neq j)$.

$r_i^{(j)}$는 **$x_j$로 $x_i$를 설명하고 남은 부분**을 말한다. 이 때의 "설명"은 Least Squares Estimation을 통해 진행하는 것으로, <a href="https://junhyoung-chung.github.io/2023/02/04/BLP.html">BLP</a>를 말한다. 다만 LiNGAM에서는 $x_i$와 $x_j$의 평균을 0으로 두고 있기 때문에 그 부분이 빠진 것이다.

> Then a variable $x_j$ is exogenous if and only if $x_j$ is independent of its residuals $r_i^{(j)}$ for all $i \neq j$.

여기서 exogenous는 인과의 시작을 의미한다. 즉, 인과순으로 나열했을 때 가장 첫번째에 위치하는 변수가 바로 exogenous variable이다. $x_j$가 인과의 시작이라는 명제와, $x_j$를 제외한 모든 변수들에 대해 $x_j$의 효과를 제거하고 남은 각각의 잔차들과 $x_j$가 독립이라는 명제는 서로 필요충분 관계에 놓여있다는 의미이다. 마냥 trivial한 것 같지는 않다. 증명을 한 번 살펴보자.

**proof**

우선 $\Rightarrow$ 부터 증명한다. i.e. If $x_j$ is exogenous, then $x_j$ is independent of its residuals $r_i^{(j)}$ for all $i \neq j$.

$x_j$가 exogenous라는 말은 $x_j=e_j$ 라는 말과 같음을 생각하자.

(3)번 식을 통해 우리는 다음과 같이 쓸 수 있다.

$$
\begin{aligned}
x_i & = \sum_{h=1}^{p}{a_{ih}e_h} \quad (i \neq j)
\newline & = a_{ij}e_j+\sum_{h \neq j}{a_{ih}e_h}
\newline & = a_{ij}x_j+\bar{e}_i^{(j)}
\end{aligned}
$$

따라서,

$$
\begin{aligned}
Cov(x_i,x_j) & = Cov(a_{ij}x_j+\bar{e}_i^{(j)},x_j)
\newline & = a_{ij}Var(x_j)+Cov(\bar{e}_i^{(j)},x_j)
\newline & = a_{ij}Var(x_j) \quad (\because e_i\text{s are independent})
\end{aligned}
$$

즉,

$$
\begin{aligned}
r_i^{(j)} & = x_i-\frac{Cov(x_i,x_j)}{Var(x_j)}x_j
\newline & = x_i-a_{ij}x_j
\newline & = \bar{e}_i^{(j)}
\end{aligned}
$$

이 된다. 그리고 $x_j=e_j$이므로 모든 $i \neq j$에 대해서 $x_j$와 $\bar{e}_i^{(j)}$이 독립이라는 것은 자명하다. ($\Rightarrow$)

이제 $\Leftarrow$ 를 증명한다. i.e. If $x_j$ is independent of its residuals $r_i^{(j)}$ for all $i \neq j$, then $x_j$ is exogenous.

만약 $x_j$가 exogenous하지 않다고 해보자. 그 말은 $x_j$에게 parents가 적어도 하나 이상 존재한다는 것을 의미한다.

$$
P_j = \left\{ k : x_k \text{ is a parent of } x_j, 1 \leq k \leq p \right\}
$$

를 정의하면 우리는 (2)번 식을 활용하여 다음과 같이 표현할 수 있다.

$$
x_j = \sum_{h \in P_j}{b_{jh}x_h}+e_j
$$

$x_h$들과 $e_j$는 independent하고 $b_{jh}$들은 모두 non-zero임을 생각하자.

$$
\mathbf{x}_{P_j} = \begin{bmatrix}
    x_{P_j,1} \\
    x_{P_j,2} \\
    \vdots \\
    x_{P_j,|P_j|}
    \end{bmatrix}
$$

$$
\mathbf{b}_{P_j} = \begin{bmatrix}
    b_{jP_j,1} \\
    b_{jP_j,2} \\
    \vdots \\
    b_{jP_j,|P_j|}
    \end{bmatrix}
$$

를 정의하면

$$
\begin{aligned}
Cov(\mathbf{x}_{P_j},x_j) & = E[\mathbf{x}_{P_j}x_j]
\newline & = E[\mathbf{x}_{P_j}(\mathbf{b}_{P_j}^T\mathbf{x}_{P_j}+e_j)]
\newline & = E[\mathbf{x}_{P_j}\mathbf{b}_{P_j}^T\mathbf{x}_{P_j}] + E[\mathbf{x}_{P_j}e_j]
\newline & = E[\mathbf{x}_{P_j}\mathbf{x}_{P_j}^T]\mathbf{b}_{P_j}
\end{aligned}
$$

가 된다. 그리고 $E[\mathbf{x}\_{P_j}\mathbf{x}\_{P_j}^{T}]$는 $\mathbf{x}\_{P_j}$의 공분산 행렬로 positive definite이다. 또한 $\mathbf{b}\_{P_j}$ 역시 non-zero vector이기 때문에 $Cov(\mathbf{x}\_{P_j},x_j) \neq 0$ 이다. 즉, $x_j$와 그 parent 변수들 간에는 상관관계가 0이 아닌 변수가 적어도 하나 이상 존재함을 의미한다. 그 변수를 $x_i$라 해보자. 즉, $Cov(x_i,x_j) \neq 0$.

$$
\begin{aligned}
r_i^{(j)} & = x_i-\frac{Cov(x_i,x_j)}{Var(x_j)}x_j
\newline & = x_i-\frac{Cov(x_i,x_j)}{Var(x_j)}\left( \sum_{h \in P_j}{b_{jh}x_h}+e_j \right)
\newline & = \left\{ 1-\frac{b_{ji}Cov(x_i,x_j)}{Var(x_j)} \right\}x_i-\frac{Cov(x_i,x_j)}{Var(x_j)}\sum_{h \in P_j, h \neq i}{b_{jh}x_h}-\frac{Cov(x_i,x_j)}{Var(x_j)}e_j
\end{aligned}
$$

여기서 parent variable들인 $x_h$($x_i$ 포함)들을 살펴보자. 이들은 모두 각각 (3)번 식에 따라 external influence들인 $e_k$들의 선형결합으로 나타낼 수 있을 것이다. 단, **이들은 인과에서 $x_j$에 앞서있기 때문에 $e_j$의 계수는 0일 것이다.**

$$
x_h = \sum_{t \neq j}{a_{ht}e_t}
$$

조금 더 엄밀히 말하면,

$$
x_h = \sum_{k(t) \leq k(h)}{a_{ht}e_t}
$$

일 것이다. 어쨌든 (9)번 식을 활용하여 위 식을 조금 더 풀면

$$
r_i^{(j)} = \left\{ 1-\frac{b_{ji}Cov(x_i,x_j)}{Var(x_j)} \right\}\sum_{l \neq j}{a_{il}e_l}-\frac{Cov(x_i,x_j)}{Var(x_j)}\sum_{h \in P_j, h \neq i}{b_{jh}\left( \sum_{t \neq j}{a_{ht}e_t} \right)}-\frac{Cov(x_i,x_j)}{Var(x_j)}e_j
$$

가 된다. 그리고 $x_j$ 역시 (2)번 식과 (9)번 식을 활용하면

$$
x_j = \sum_{h \in P_j}b_{jh}\left( \sum_{t \neq j}{a_{ht}e_t} \right) + e_j
$$

로 나타낼 수 있다.

이제 (11)번 식과 (12)번 식을 크게 바라보자.

(11)번 식의 경우 첫번째와 두번째 term은 $e_j$를 제외한 $e_h$들의 선형결합이고 세번째 term은 $e_j$에 계수가 붙어있는 꼴이다.

(12)번 식의 경우 첫번째 term은 $e_j$를 제외한 $e_h$들의 선형결합이고 두번째 term은 $e_j$에 계수 1이 붙어있는 꼴이다.

**즉, (4)번 식의 형태와 동일하다.**

또한, $e_k$들은 모두 independent하고 non-Gaussian이다. 더하여 우리는 $Cov(x_i,x_j) \neq 0$임을 위에서 확인하였다. 아까 우리가 살펴본 theorem의 의미를 다시 한번 생각해보자.

> 즉, $\alpha_j\beta_j \neq 0$인 non-Gaussian random variable $s_j$가 존재하면 $y_1$과 $y_2$는 서로 dependent하다.

따라서 우리는 **Darmois-Skitovitch theorem**에 따라 $r_i^{(j)}$와 $x_j$는 서로 dependent하다는 것을 보일 수 있고 이는 가정과 모순이다.

$\therefore x_j \text{ is exogenous.} \quad (\Leftarrow) \quad \blacksquare$ 

**Lemma 2**

> Assume that the input data $\mathbf{x}$ strictly follows the LiNGAM (2). Further, assume that a variable $x_j$ is exogenous. Denote by $\mathbf{r}^{(j)}$ a $(p-1)$-dimensional vector that collects the residuals $r_i^{(j)}$ when all $x_i$ of $\mathbf{x}$ are regressed on $x_j \; (i \neq j)$. Then a LiNGAM holds for the residual vector $\mathbf{r}^{(j)}$: $\mathbf{r}^{(j)} = \mathbf{B}^{(j)}\mathbf{r}^{(j)} + \mathbf{e}^{(j)}$, where $\mathbf{B}^{(j)}$ is a matrix that can be permuted to be strictly lower-triangular by a simultaneous row and column permutation, and elements of $\mathbf{e}^{(j)}$ are non-Gaussian and mutually independent.

아까 우리가 기본적인 흐름을 살펴보았을 때, 잔차들에 대해서도 LiNGAM이 동일하게 성립하는 것을 보이기 위해 Lemma 2와 뒤에 소개할 Corollary 1이 필요하다고 하였다. Lemma 2에서는 LiNGAM approach가 잔차들에 대해서도 진행될 수 있다는 점을 보이고, 이후 Corollary 1에서는 인과순서도 동일하게 나열된다는 것을 보인다.

**proof**

우선 일반성을 잃지 않고, $\mathbf{B}$가 잘 permuted 되어 있다고 가정하자. 즉, $x_j=x_1$. 그리고 $\mathbf{A}$는 diagnonal element들이 모두 1인 lower-triangular matrix일 것이다.

우리는 아까 **Lemma 1**을 증명하는 과정에서 다음과 같은 사실을 확인하였다.

$$
a_{ij} = \frac{Cov(x_i,x_j)}{Var(x_j)} \quad (x_j \text{ is exogenous.})
$$

여기서는 $x_1$이 exogenous variable 이므로 $a_{i1}=\frac{Cov(x_i,x_1)}{Var(x_1)}$일 것이다. 즉, $\mathbf{A}$에서 첫번째 column에 있는 원소들 $a_{i1}$은 $x_i$를 $x_1$에 대해 회귀했을 때의 계수와 동일하다는 것을 의미한다.

만약 $x_i$ 각각에 대해 $x_1$의 효과를 제거하고 남은 잔차들에 대해 $\mathbf{A}$를 구했다면 첫번째 column은 0-vector일 것이다. 즉,

$$
\mathbf{A}^{\ast} = \begin{bmatrix}
    0 & 0 & 0 & \cdots & 0 \\
    0 & 1 & 0 &  \cdots & 0 \\
    0 & a_{32} & 1 & \cdots & 0 \\
    \vdots & \vdots & \vdots & \ddots \\
    0 & a_{p2} & a_{p3} & \cdots & 1
    \end{bmatrix}
$$

이고 $\mathbf{A}^{(1)}$은 $\mathbf{A}^{\ast}$에서 첫번째 row와 column을 지운 matrix와 동일하다.

$$
\mathbf{r}^{(1)} = \mathbf{A}^{(1)}\mathbf{e}^{(1)} \quad \blacksquare
$$

**Corollary 1**

> Assume that the input data $\mathbf{x}$ strictly follows the LiNGAM (2). Further, assume that a variable $x_j$ is exogenous. Denote by $k_{r^{(j)}}(i)$ a causal order of $r_i^{(j)}$. Recall that $k(i)$ denotes a causal order of $x_i$. Then, the same ordering of the residuals is a causal ordering for the original observed variables as well: $k_{r^{(j)}}(l) < k_{r^{(j)}}(m) \Leftrightarrow k(l) < k(m)$.

우리는 아까 $\mathbf{A}^{(1)}$은 $\mathbf{A}^{\ast}$에서 첫번째 row와 column을 지운 matrix와 동일하다는 것을 확인하였고, 여전히 lower-triangular matrix인 것도 확인하였다. 이는 다른 변수들의 순서가 서로 바뀌지 않았다는 것을 의미한다. $\blacksquare$

---

이후에는 실제로 **Lemma 1**, **Lemma 2**, **Corollary 1**을 어떻게 알고리즘에 대입했는지에 대한 설명을 다루고 있다. 여기서부터는 다음 글에서 살펴보도록 하자.

## Reference

* <a href="https://www.jmlr.org/papers/volume12/shimizu11a/shimizu11a.pdf">DirectLiNGAM: A Direct Method for Learning a Linear non-Gaussian Structural Equation Model</a>

* <a href="https://junhyoung-chung.github.io/2023/02/04/BLP.html">Best Linear Predictor</a>
