---
title: 04-기본 설정
tags:
    - etc
    - githubpages
---

github 블로그는 테마를 선택했다고 끝나는 것이 아니다! 내 블로그로 온전히 만들어주기 위해서는 커스터마이징을 필수로 해주어야 하는데, 이게 생각보다 쉽지 않다. 이번 글에서는 최소한의 기본적인 세팅을 어떻게 해야할지를 정리해보려고 한다.

<!--more-->

---

우선 대부분의 세팅은 `_config.yml` 파일에서 모두 해결할 수 있다. 이 파일만 제대로 만져보도록 하자.

## Site Settings

```yml
## => Site Settings
##############################
text_skin: default # "default" (default), "dark", "forest", "ocean", "chocolate", "orange"
highlight_theme: default # "default" (default), "tomorrow", "tomorrow-night", "tomorrow-night-eighties", "tomorrow-night-blue", "tomorrow-night-bright"
url     : https://junhyoung-chung.github.io
baseurl : ''
title   : JunHyoung
description: > # this means to ignore newlines until "Language & timezone"
  This blog is for recording my personal studying.
```

`text_skin`은 배경을 선택하는 부분이다. 주석을 보면 알 수 있듯 총 6개의 테마가 있는데 각 테마가 어떻게 생겼는지는 TeXt 페이지에서 확인할 수 있다. 이 테마는 `sass` 폴더 안에 있는 코드들을 통해 구현이 되는데 이를 활용하여 직접 테마 설정도 해볼 수 있으나 이 부분은 당장 다루지는 않겠다. 나도 아직 엄두가 나지 않아 지금은 `default`로만 사용하고 있다.

`highlight_theme`은 코드 블럭 디자인을 말한다. 이 부분도 TeXt 블로그에서 좀 더 자세히 확인할 수 있다. 나는 `default`에는 `default`가 제일 어울리는 것 같아 이렇게 설정했다.

`url`에는 본인의 블로그 링크를 넣어주면 된다. `baseurl`은 필요한 경우 넣어주면 되는데 굳이 넣지 않아도 된다.

만약 `baseurl`에 `/blog` 처럼 무언가를 넣어주게 되면 홈페이지의 url이 "https://junhyoung-chung.github.io/blog" 형태가 된다. 
<a href="https://syki66.github.io/blog/">이 블로그의 url</a> 을 참고하면 된다.

`title`은 좌측 상단에 있는 블로그 타이틀을 말한다.

`description`은 내 블로그의 기본 설명을 쓰는 곳이다.

![description](/assets/images/description.jpg)

`title`과 `description`은 이렇게 나타난다.

## Language and Timezone

```yml
## => Language and Timezone
##############################
lang: kr-KR, en-US
timezone: Asia/Seoul
```

기본 언어와 시간대를 설정하는 곳이다. 만약 시간대를 다르게 설정하고 싶다면 <a href="https://en.wikipedia.org/wiki/List_of_tz_database_time_zones">이 표</a>를 참고하자.

## Author and Social

```yml
## => Author and Social
##############################
author:
  type      : # "person" (default), "organization"
  name      : JunHyoung Chung
  url       :
  avatar    : /assets/images/me.jpg
  bio       : I am an amazing person.
  email     : justin9991@snu.ac.kr
  facebook  : # "user_name" the last part of your profile url, e.g. https://www.facebook.com/user_name
  twitter   : # "user_name" the last part of your profile url, e.g. https://twitter.com/user_name
  weibo     : # "user_id"   the last part of your profile url, e.g. https://www.weibo.com/user_id/profile?...
  googleplus: # "user_id"   the last part of your profile url, e.g. https://plus.google.com/u/0/user_id
  telegram  : # "user_name" the last part of your profile url, e.g. https://t.me/user_name
  medium    : # "user_name" the last part of your profile url, e.g. https://medium.com/user_name
  zhihu     : # "user_name" the last part of your profile url, e.g. https://www.zhihu.com/people/user_name
  douban    : # "user_name" the last part of your profile url, e.g. https://www.douban.com/people/user_name
  linkedin  : # "user_name" the last part of your profile url, e.g. https://www.linkedin.com/in/user_name
  github    : Junhyoung-Chung
  npm       : # "user_name" the last part of your profile url, e.g. https://www.npmjs.com/~user_name
```

이 부분은 author 정보와 내 SNS 정보를 넣는 곳이다. `type`부터 `bio`까지는 일단 아무렇게나 썼는데, TeXt 테마에서는 author 정보를 표시하지 __않는__ 것으로 default를 설정했기 때문에 당장은 우리에게 중요한 부분이 아니다. 이건 나중에 따로 다루도록 하자.

`email`부터 시작되는 곳에는 해당하는 SNS 계정이 있다면 넣어주면 된다. 나는 여기서 해당하는 부분이 github과 email밖에 없기 때문에 두 개를 넣어주었다. 이걸 잘 넣어주게 되면 맨 하단부에 링크가 걸리게 된다.

![sns info](/assets/images/sns.jpg)

물론 여기에 써져 있는 SNS 계정 말고도(ex. 인스타그램) 직접 몇 개를 더 추가할 수 있다! 다만 그럴 경우에는 또 다른 코드들을 같이 손봐주어야 하기 때문에 일단은 넘어가자.

## Github Repository

```yml
## => GitHub Repository (if the site is hosted by GitHub)
##############################
repository: Junhyoung-Chung/junhyoung-chung.github.io
repository_tree: master
```

이 부분에는 본인의 레포지토리 정보를 넣어주면 된다. 만약 마스터 브랜치가 아니라 다른 브랜치에서 블로그를 운영하고 있다면 해당 브랜치의 이름을 넣어주면 되겠다.

## Paths

```yml
## => Paths
##############################
paths:
  root    : # title link url, "/" (default)
  home    : # home layout url, "/" (default)
  archive : # "/archive.html" (default)
  rss     : # "/feed.xml" (default)
```

딱히 건드릴 필요가 없는 부분이다. 경로 지정을 설정하는 부분 같다.

