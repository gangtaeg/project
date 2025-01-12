# SeeSaw - 안전 거래 플랫폼으로 신뢰의 거래를 더하다

## 1. 소개
### 기획 의도, 그리고 우리의 목표
사용자들이 안전하게 거래할 수 있는 환경을 제공하고, 이를 위해 실시간으로 거래 정보를 확인하고 직관적인 방법으로 거래 가격을 예측할 수 있도록 돕는 것이 목표입니다. SeeSaw는 이를 위한 안전 거래 플랫폼으로, 편리하고 신뢰할 수 있는 서비스를 제공하고자 합니다.

### SeeSaw를 통해 무엇을 할 수 있나요?
  - 판매자들은 현재 팔고자 하는 물건에 대한 시세와 판매 예상 가격을 파악할 수 있습니다.
  - 구매자들은 자신이 원하는 물건의 시세와 근처에 있는 매물 개수를 확인할 수 있습니다.
  - 특정 물품의 가격 변동을 실시간으로 추적하고 알림을 받을 수 있는 기능을 제공합니다.
  - 메인 화면에서 거래 시세를 직관적으로 확인할 수 있는 그래프와 차트를 제공합니다.

### 이름은 왜 SeeSaw인가요?
"SeeSaw"는 거래가 오르내리는 과정을 물리적으로 나타내는 "시소"에서 착안하여, 거래 시세와 가격 변동을 손쉽게 볼 수 있음을 의미합니다.

## 2. 시스템 구조
![시스템 구조](https://user-images.githubusercontent.com/72847093/101735679-91af6b80-3b05-11eb-972b-97d421deff0e.PNG)

## 3. Contribute
### Details
#### Getting Started
- 프로젝트를 시작하려면 아래의 프리퀴지트가 필요합니다.

#### Prerequisites
- Python 3, Flask
- MongoDB, MySQL
- 카카오톡 및 슬랙 API

#### Dataset
- 데이터를 모으고 분석하는 데 필요한 샘플 데이터를 제공합니다.

#### 코드 설명 1
- **fleafully.py**  
  - Flask를 사용하여 웹 서버 실행
  - AWS 서버를 통해 WAS 구현
  - MongoDB와 연결하여 데이터를 가져오고 MySQL에 저장
- **fleafully_crawl.py**  
  - 중고마켓에서 가격 정보를 크롤링하여 데이터베이스에 저장
- **templates > main.html, index.html, features.html, technology.html**  
  - 프론트엔드를 구현하기 위한 HTML 템플릿

#### 코드 설명 2
- **app.py**  
  - 메인 Flask 애플리케이션 실행
- **crawler.py**  
  - 다양한 중고 마켓에서 실시간 데이터를 크롤링
- **database.py**  
  - 크롤링한 데이터를 MongoDB와 MySQL에 저장
- **data_visualization.py**  
  - 데이터를 분석하고 시세 그래프 및 차트를 렌더링

## 4. Built with
- **김성준**  
  - Flask로 서버 구현 및 API 연동, 웹 서버 배포
  - GitHub: [https://github.com/alltimeno1](https://github.com/alltimeno1)

- **전예나**  
  - MongoDB와 MySQL 연동, 프론트엔드 구현, 데이터 시각화 및 차트 구현
  - GitHub: [https://github.com/Yenabeam](https://github.com/Yenabeam)

- **정하윤**  
  - 크롤링 기능 구현, 데이터 전처리 및 분석, API 연동
  - GitHub: [https://github.com/hayoon](https://github.com/hayoon)

- **이화진**  
  - 기여기여기여기여
  - GitHub: [https://github.com/yourusername](https://github.com/yourusername)

## 5. 그리고
#### 참고 사이트
- [번개장터](https://m.bunjang.co.kr/)
- [중고나라](https://www.joongna.com/)
- [당근마켓](https://www.daangn.com/)

#### Q&A
- Contact us: gangtaegheo43@gmail.com

#### 파일구조
/project
  /시소(SeeSaw)
    /.obsidian
    /SeeSaw(가상환경)
      /bin
      /include
      /lib
      /libexec
      /pip-selfcheck.json
      /pyvenv.cfg
      /share
      /Scripts
    /계획서
    /기능
      fleafully.py
    /웹페이지
      /.vscode
      /assets
      /css
      /data
      /js
      /libs
      features.html
      index.html
      services.html
      technology.html
    시소 ppt.png

아래는 사용자의 깃허브 주소를 포함한 SeeSaw 프로젝트 실행 가이드입니다.

SeeSaw 프로젝트 실행 방법

안녕하세요!
이 문서는 SeeSaw 프로젝트를 처음 사용하는 분들을 위한 간단한 실행 가이드입니다. 아래 단계를 따라하면 SeeSaw 프로젝트를 실행할 수 있습니다.

1. 준비물
Python이 컴퓨터에 설치되어 있어야 합니다.
Python이 설치되어 있지 않다면 Python 공식 웹사이트에서 다운로드하고 설치해주세요.
Git이 설치되어 있어야 합니다.
Git이 설치되어 있지 않다면 Git 다운로드 페이지에서 설치하세요.

2. 프로젝트 내려받기
GitHub에서 프로젝트 파일을 다운로드합니다.

명령어 창(터미널 또는 CMD)을 열어주세요.
아래 명령어를 입력하고 실행합니다:
git clone https://github.com/gangtaeg/project.git
cd project/시소(Seesaw)

3. 필수 프로그램 설치
이 프로젝트가 제대로 실행되기 위해 필요한 프로그램들을 설치합니다:

**명령어 창(터미널)**에서 아래 명령어를 입력하세요: pip install -r requirements.txt

4. 프로젝트 실행하기
이제 서버를 실행해볼 차례입니다!

**명령어 창(터미널)**에 아래 명령어를 입력합니다: python app.py

실행에 성공하면 아래와 같은 메시지가 나옵니다: Running on http://127.0.0.1:5000/

웹 브라우저를 열고 주소창에 아래 주소를 입력하세요: http://127.0.0.1:5000/

SeeSaw 프로젝트 화면이 나타납니다! 🎉

5. 데이터 확인하기 (선택 사항)
데이터 크롤러를 실행하려면 아래 명령어를 사용합니다: python scripts/crawler.py

이 단계는 꼭 필요한 건 아니니, 그냥 넘어가도 괜찮아요.

문제가 생겼나요?
Python 설치나 명령어 입력이 어렵다면 주위의 친구나 전문가에게 도움을 요청하세요.

프로젝트 관련 질문은 깃허브 Issues에 올려주세요!

이 단계를 차근차근 따라하면 SeeSaw를 성공적으로 실행할 수 있을 거예요! 😊

###### 본 프로젝트는 **SeeSaw**라는 안전 거래 플랫폼으로 기획된 프로젝트로, 비전공자를 위한 간단한 웹사이트 구현을 목표로 하고 있습니다.
###### 이 `README.md` 파일은 **FleaFully** 프로젝트를 참고한 내용을 포함하여, 프로젝트의 개요, 주요 기능, 파일 구조, 실행 방법 등을 명확히 설명하고 있습니다. 또한, **FleaFully** 프로젝트 GitHub 링크를 포함해 해당 프로젝트를 참조할 수 있도록 하였습니다.