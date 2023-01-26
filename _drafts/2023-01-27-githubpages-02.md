---
title: 03-Hydejack에서 TeXt로 넘어오기까지
tags:
    - etc
    - githubpages
---

나는 원래 <a href="https://hydejack.com">Hydejack</a> 테마로 블로그를 시작했다. 벌써 일주일 정도가 된 것 같은데, 일주일동안 이 테마에만 매달리다가 결국 포기하고 지금 <a href="https://kitian616.github.io/jekyll-TeXt-theme/">TeXt</a> 테마로 넘어오게 되었다. 내가 왜 맨 처음에 Hydejack 테마를 선택했는지, 그런데 왜 포기했고 왜 TeXt 테마를 선택했는지 그 이유를 여기서 다뤄보려고 한다.

<!--more-->

참고로 나는 개발자도 아니고 파이썬밖에 할 줄 모르기 때문에 다른 사람들과는 생각이 조금 다를 수 있다. 자바스크립트와 html을 크롤링할 때나 만져봤지 이렇게 자세히 들여다 본 건 처음이라 이런 생각이 드는 것일 수도 있겠다.

## Hydejack

### 왜 Hydejack을 선택했는가?

일단 이펙트가 화려해서 진짜 예쁘긴 하다. Hydejack 기본 블로그 자체도 예쁘긴 하지만

* <a href="https://lazyren.github.io">Lazy Ren</a>

* <a href="https://khw11044.github.io">따라쟁이의 인공지능 블로그</a>
  
내가 이 두 분 블로그를 정말 많이 참고했다. 특히 첫번째 분 블로그는 진짜 예쁘다. 또 나는 수학수식을 많이 쓰게 될 것 같았는데 Hydejack의 설명을 보니 수학 수식이 깔끔하게 지원된다(이거에 속았다)고 해서 망설임 없이 이 테마를 선택했다.

### 왜 Hydejack을 포기했는가?

#### 너무 복잡하다

다른 테마들도 마찬가지인지는 모르겠지만 디폴트 코드부터 너무 복잡했다. 뭐가 뭔지를 도저히 모르겠고, 일주일 정도 지나 포기하려고 하니까 이제야 좀 알겠다 싶을 정도로 내부 구조도 복잡했다. 아마 복잡한 만큼 내가 할 수 있는 부분이 많다는 것이겠지만 나같은 초보자에게는 이해하는 것도 충분히 벅찼다. 원하는 기능을 하나하나 추가하는데 시간이 꽤 많이 소요된다. 물론 그만큼 공부가 많이 되긴 했다.

#### 레퍼런스의 부족

생각보다 Hydejack 테마를 쓰고 있는 블로그가 많지 않고, 또 Hydejack 테마 커스터마이징에 대해 구체적으로 다루고 있는 블로그는 그 안에서도 없는 편이다. 내가 찾아봤을 때에는 위에 언급해놓은 두 블로그가 사실상 유일하다. 그래서 다른 테마를 사용하고 있는 블로그의 내부 구조를 다 뜯어다보며 내가 하나씩 일일이 비교해가며 집어넣어주는 수밖에 없다. 근데 이 비교하는 과정이 위에서 말한 복잡한 구조 때문에 정말 화가 난다ㅎㅎ

#### 유료 버전

처음 깔 때는 몰랐는데 Hydejack은 무료버전과 유료버전이 나뉘어 있다. 유료버전에 기능이 조금 더 많은 듯 하다. 그래서 찾아보니 유료버전이 코드를 만지기에는 더 편하다고 했다. 기능이 많으니 0에서부터 시작하지 않아도 된다는 의미인 것 같았다.

#### 수학수식 렌더링 문제

이거 때문에 Hydejack 테마를 포기했다고 해도 무방하다. 왜 수학수식이 깔끔하다고 했던 걸까? 사실 그렇게 치명적인 문제는 아닌데, Hydejack 테마에서는 꼭 한번 새로고침을 가끔씩 해주어야 수식이 제대로 보였다. 이게 진짜 무슨 짓을 해도 해결이 안 된다.

![Hydejack-Mathjax-Error](/assets/images/hydejack-math-error.jpg)

내가 원인까지는 찾았다.

일단 Hydejack에서는 `katex`에 맞춰져 있다. 찾아보니 `mathjax`는 좀 무거운 편이라 수식으로 변환되기까지 시간이 오래 걸리는 반면 `katex`는 속도 면에서 월등히 빠르다고 한다. 다만 `katex`의 경우에는 지원하는 기능이 조금 더 적다. 하지만 그게 문제가 아니다. Hydejack은 자체적으로 `katex-display` (이름은 확실치 않음) 라는 함수를 사용하고 있는데, html 상에서 `math/tex` type을 가지고 있는 애들만을 뽑아와서 수식변환을 진행하는 로직이다. 

옛날에는 그게 됐는데 이제 문제는 kramdown에서 더 이상 이렇게 렌더링을 하지 않는다는 거다.

```html
<script type="math/tex; mode=display">1 + 1 = 2</script>
```

원래 이렇게 렌더링이 되어야 코드가 돌아가는데, 지금은 그게 아니라는 거다. 지금 정확히 어떤 형태로 되는지는 모르겠다. 하튼 이것 때문에 Hydejack 코드로는 수학 수식을 제대로 잡아내지 못한다. 이게 2017년? 2018년? 쯤 업데이트가 된 것 같은데 아직 Hydejack 코드는 안 바뀐 모양이다.

그래서 `katex`를 쓸거면 코드를 싹 다 뒤집어야겠구나라는 생각이 들었다. 

`mathjax`로 눈을 돌렸더니 `katex`보다는 조금 나아보였다. 레퍼런스도 비교적 많고, 공식문서도 깔끔하게 잘 되어 있어 `mathjax`를 공략해야겠다 싶었다.

Hydejack 코드에서 `katex`와 관련된 것들은 모두 지우고 `mathjax`로 갈아끼워넣았다. 그래도 여전히 한방에 수식이 잘 뜨진 않았다. 개발자 도구로 확인해보면 아예 수식을 인식하지 못한다. 근데 또 새로고침하면 잘 되고,, 진짜 얄미워서 화가 머리 끝까지 났던 것 같다.

더 화가 나는 건 다른 테마 블로그는 다 잘 된다는 거다. 특히 <a href="http://csega.github.io/mypost/2017/03/28/how-to-set-up-mathjax-on-jekyll-and-github-properly.html#">여기</a> 블로그랑은 진짜 테마 빼고 싹다 똑같이 만들어봤는데도 여전히 해결이 안 되는 것이었다.

이쯤되니 내가 해볼 수 있는 건 다 해봤다는 생각이 들어서 Hydejack 테마는 포기하기로 했다. 테마 디자인이 너무 마음에 들었어서 아쉽긴 하다. 그래도 나한테는 수학 수식 잘 먹히는 게 가장 중요한 것 중 하나였기 때문에.. 눈물을 머금고 보내주었다. 오히려 이렇게 며칠을 고민하면서 계속 찾아보다보니 자바스크립트도 아주 살짝 느낌을 잡은 것 같기도 하다. 긍정적으로 생각하자!


## Reference

* <a href="https://lazyren.github.io">Lazy Ren</a>

* <a href="https://khw11044.github.io">따라쟁이의 인공지능 블로그</a>

* <a href="https://stackoverflow.com/questions/61852018/jekyll-kramdown-math-render-settings">Jekyll kramdown math render settings</a>

* <a href="https://an-seunghwan.github.io/github.io/mathjax-error/">github.io 수식 오류 해결하기!</a>

* <a href="https://docs.mathjax.org/en/latest/web/configuration.html">MathJax Latest Document</a>

* <a href="https://docs.mathjax.org/en/v2.7-latest/configuration.html">MathJax v2.7.7. Document</a>

* <a href="http://csega.github.io/mypost/2017/03/28/how-to-set-up-mathjax-on-jekyll-and-github-properly.html#">How to set up MathJax on Jekyll and GitHub properly?</a>