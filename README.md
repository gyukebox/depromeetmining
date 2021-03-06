# Depromeet 마이닝

[![Build Status](https://travis-ci.org/gyukebox/depromeetmining.svg?branch=master)](https://travis-ci.org/gyukebox/depromeetmining) [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)



(이 레포는 원래 디프만 세션 때 발표할 내용을 코드로 짠 레포지토리 입니다.)  
원래 디프만 세션 끝나면 그냥 내버려 두려고 했지만,

- 고유명사에 대한 처리
- 워드 클라우드 만드는 기능 좀 더 다양하게
- 분석 결과 api 로 포팅

하는 기능을 추가로 더 만들어 볼까 해요!



## 한번 시도해보고 싶으신 분들께 

우선 이 레포지토리를 clone 하세요.

```
$ git clone https://github.com/gyukebox/depromeetmining.git
```

그 다음, 

```
$ pip install -r requirements.txt
```

명령어로 파이썬 모듈들을 설치해주시면 되겠습니다!
(다들 파이썬 3 버전 쓰고 계시죠? 2버전 쓰시는분들도 얼른 3으로 넘어오시길!)

아차, 윈도우에서는 pip 가 잘 안 작동할 수 있으므로 그냥 anaconda 쓰시는 게 정신건강에 이로우실 수 있어요.

### Mecab 형태소 분석기

**슬픈 소식** : `Mecab` 형태소 분석기의 windows 지원 여부 때문에 해당 프로그램은 윈도우즈 환경에서 작동하지 않습니다.. 윈도우즈 사용하시는 분들은 VM으로 리눅스 환경에서 해보시거나.. 아쉽습니다ㅠ

다음의 명령어를 이용하여 설치해 줍시다!

**데비안 계열 리눅스**
```
$ sudo apt-get install curl
$ bash <(curl -s https://raw.githubusercontent.com/konlpy/konlpy/master/scripts/mecab.sh)
```

**레드햇 계열 리눅스**
```
$ sudo yum install curl
$ bash <(curl -s https://raw.githubusercontent.com/konlpy/konlpy/master/scripts/mecab.sh)
```

**OSX**
```
$ bash <(curl -s https://raw.githubusercontent.com/konlpy/konlpy/master/scripts/mecab.sh)
```

### 분석할 데이터 저장

코드를 다 받으셨다면, 분석할 카카오톡 데이터가 필요하겠죠?  
카카오톡 채팅방의 대화를 내보내기 하셔서, `data` 폴더에 `data.csv` 이름의 파일로 저장하시면 됩니다.  
따라서, 전체 폴더의 구조가 밑의 그림과 같이 구성되어 있으시면 성공입니다!

```
depromeet_mining/
├── LICENSE.md
├── README.md
├── data
│   ├── data.csv
├── requirements.txt
├── src
│   ├── __init__.py
│   ├── analysis
│   │   ├── __init__.py
│   │   ├── fb_analysis.py
│   │   ├── kakao_analysis.py
│   │   └── visualization.py
│   └── api
│       └── __init__.py
├── test
│   ├── __init__.py
│   ├── fb_analysis_test.py
│   └── kakao_analysis_test.py
└── web
    ├── index.html
    ├── scripts
    │   └── main.js
    ├── styles
    │   └── style.css
```

### 드디어 실행

데이터도 가져오셨으면, test 폴더에 들어가셔서,

```
$ python kakao_analysis_test.py
```

와 같이 테스트 파일 이름을 넣고 파이썬 인터프리터를 실행시켜 주시면 됩니다.  
(현재 경로 문제 때문에 빌드가 계속해서 깨지는 중이네요ㅠㅠ)


## 라이브러리 스펙

~~작성자가 너무 게을러서~~ 시간 관계상 스펙을 명시하지 못하고 이렇게 레포를 올리게 되었어요. 조만간 wiki 에 라이브러리 및 api(이건 개발이 우선이긴 하지만) 스펙으로 찾아뵙도록 하겠습니다!



## License

[MIT](https://opensource.org/licenses/MIT)

