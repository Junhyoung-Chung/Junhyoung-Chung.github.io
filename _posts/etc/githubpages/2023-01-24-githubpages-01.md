---
layout: post
title: 01-jekyll 설치가 안 될 경우
categories:
    - etc
    - githubpages
description: >
  bundler, jekyll 설치가 안 될 경우
tags: []
comments: true
published: true
---

# 01-jekyll 설치가 안 될 경우

일단 나는 MacBook Pro M1 2020을 사용하고 있기 때문에 다른 시스템의 경우 에러 해결과정이 달라질 수 있다.

우선 Github 블로그를 시작하기 위해서는 Repository를 새로 만들어야 하는데, 이 과정은 <a href="https://supermemi.tistory.com/entry/나만의-블로그-만들기-Git-hub-blog-GitHubio">여기</a>에 너무 잘 설명되어 있다. 그냥 그대로 따라하면 된다!!

그리고 다음으로

```zsh
gem install bundler
gem install jekyll
```

명령어를 입력했더니

_&lt;You may have encountered a bug in the Ruby interpreter or extension libraries.&gt;_

에러가 떴다. 찾아보니 ruby

이 역시 <a href="https://supermemi.tistory.com/145">여기</a>에 잘 설명되어 있지만 2022년 글이기도 하고, 그 때와 `rbenv` 버전이 조금 달라진 것 같아 따로 정리해두려고 한다.

우선 `rbenv`는 여러 ruby 버전 설치가 가능하게 도와주는 루비 버전 관리 툴이며, 필요시마다 ruby의 버전 변경을 도와준다고 한다. 다음 명령어를 통해 `rbenv`를 깔아주도록 하자.

```zsh
brew install rbenv ruby-build
```
그 다음,

```zsh
rbenv install -l
```
명령어를 입력하면 설치 가능한 `rbenv` 버전들이 나온다.

```zsh
2.7.7
3.0.5
3.1.3
3.2.0
jruby-9.4.0.0
mruby-3.1.0
picoruby-3.0.0
rbx-5.0
truffleruby-22.3.0
truffleruby+graalvm-22.3.0
```
최신 버전인 3.2.0로 깔아주자! 버전 호환 문제가 있을까봐 살짝 걱정스럽긴 했는데, 아직까진 큰 문제가 발생하지 않았다. 그냥 그때그때 최신버전으로 깔아주면 문제가 없을 듯 하다. 근데 여기서 `jruby` 밑으로는 무엇을 나타내는지 궁금하다! 에러 해결에는 크게 중요한 부분이 아닌 것 같으니 일단 넘어가자.

```zsh
rbenv install 3.2.0
```
3.2.0 버전을 global로 설정해주어야 한다.

```zsh
rbenv global 3.2.0
```
그 다음,

```zsh
[[ -d ~/.rbenv  ]] && \
  export PATH={$Home}/.rbenv/bin:$PATH && \
  eval "$(rbenv init -)"
```
를 `zsh`를 사용하고 있다면 `~/.zshrc`에, `bash`를 사용하고 있다면 `~/.bashrc`에 추가해주어야 하는데, 사용 버전은 아래 명령어를 통해 확인할 수 있다.

```zsh
echo $SHELL
```
만약 아래처럼 나온다면

```zsh
/bin/zsh
```
`zsh`를 사용하고 있는 것이기 때문에 `~/.zshrc`에 추가해주면 된다. 아마 M1이라면 다 같지 않을까?

내용을 추가하는 법은 아래와 같다.

```zsh
vi ~/.zshrc
```
를 치면 아래와 같이 쭉 뜰 것이다.

![~/.zshrc](/assets/img/edit-zshrc.jpg)

i 를 누르면 insert를 할 수 있는데, 동그라미 위치에 텍스트를 넣고(위치는 크게 상관없을 거 같긴 하다), esc -> :qw -> enter 하면 해당 파일이 수정되어 저장될 것이다.

변경된 파일을 저장해주자.

```zsh
source ~/.zshrc
```
다시 설치를 하면,

```zsh
gem install bundler

rbenv rehash
```
잘 설치가 되는 것을 확인할 수 있다. 다만 여기서,

```zsh
rbenv rehash
```
가 무슨 역할을 하는지는 아직 잘 모르겠다.

그 다음 Github 블로그 repository로 가서

```zsh
gem install jekyll
```

```zsh
jekyll new ./
```
를 순서대로 실행하면 거의 다 끝났다!

```zsh
bundle install
bundle exec jekyll serve
```
를 실행하면

```zsh
...
Server address: http://127.0.0.1:4000/
...
```
과 같이 로컬 서버 주소가 나오게 된다. 해당 주소로 타고 들어갔을 때 문제 없이 잘 나온다면 해결된 것이다. 그 다음에 원격 repository로 push하면 끝!

다음에는 Github 블로그 테마를 정리해봐야겠다. 나중에 시간날 때 `rbenv rehash`가 정확히 무슨 역할하는지도 함 찾아봐야겠다.

## Reference
---

* <a href="https://supermemi.tistory.com/entry/나만의-블로그-만들기-Git-hub-blog-GitHubio">나만의 블로그 만들기 Git hub blog!! (github.io)</a>

* <a href="https://supermemi.tistory.com/145">나만의 github 블로그 Jekyll 으로 꾸며 보자! (gitHub.io)</a>

* <a href="https://kyurasi.tistory.com/entry/Ruby-on-rails-맥북-설치하기">rbenv 설치하기</a>

* <a href="https://frhyme.github.io/blog/install_jekyll_again/">Gem::FilePermissionError 해결하기</a>

* <a href="https://notes.hphk.io/p/how-rbenv-works/#rbenv-rehash">rbenv의 동작원리</a>