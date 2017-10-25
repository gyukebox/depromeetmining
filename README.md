# Depromeet 마이닝

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)



(이 레포는 원래 디프만 세션 때 발표할 내용을 코드로 짠 레포지토리 입니다.)  
원래 디프만 세션 끝나면 그냥 내버려 두려고 했지만,

- 고유명사에 대한 처리
- 워드 클라우드 만드는 기능 좀 더 다양하게
- 분석 결과 api 로 포팅

하는 기능을 추가로 더 만들어 볼 까 해요!



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

코드를 다 받으셨다면, test 폴더에 들어가셔서,

```
$ python kakao_analysis_test.py
```

와 같이 테스트 파일 이름을 넣고 파이썬 인터프리터를 실행시켜 주시면 됩니다.



## 라이브러리 스펙

~~작성자가 너무 게을러서~~ 시간 관계상 스펙을 명시하지 못하고 이렇게 레포를 올리게 되었어요. 조만간 wiki 에 라이브러리 및 api(이건 개발이 우선이긴 하지만) 스펙으로 찾아뵙도록 하겠습니다!



## License

[MIT](https://opensource.org/licenses/MIT)

