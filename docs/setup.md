# 개발 환경 설정

맥과 Homebrew 기준으로 Python 개발 환경을 설정하는 방법입니다.

## pyenv 설치

pyenv는 Python 버전을 여러 개 설치하고 프로젝트별로 고정할 수 있게 해주는 도구입니다.

```sh
brew update
brew install pyenv
```

## zsh 설정

```sh
echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.zshrc
echo '[[ -d $PYENV_ROOT/bin ]] && export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.zshrc
echo 'eval "$(pyenv init - zsh)"' >> ~/.zshrc
source ~/.zshrc
```

## Python 설치

```sh
pyenv install 3.12.9
pyenv versions
```

## 전역 Python 버전 설정

```sh
pyenv global 3.12.9
python --version
```

## 전역 설정 취소

```sh
pyenv global system
```

## 가상환경 활성화

```sh
source venv/bin/activate
```
# openai 설치
```sh
python -m pip install openai==1.58.1
```

# 실행하는 방법

  - 가상환경 활성화:
  - source venv/bin/activate
  - python chap02/gpt_basic.py