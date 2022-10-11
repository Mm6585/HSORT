# 한밭대학교 컴퓨터공학과 HSORT 팀

#### 팀 구성
- 20172608 이동진
- 20172598 김규진
- 20172615 최우석
- 20172616 한수호
<br><br>


## 프로젝트 소개
### RFID와 카메라를 활용한 학생 인식 및 위치 추적 시스템
- RFID 출입 게이트와 카메라를 활용하여 학생의 출입과 위치를 확인할 수 있는 시스템.
- RFID는 비접촉식으로 태그가 직접 리더기에 닿지 않아도 인식 범위 내에서 자동으로 인식함.
- RFID 태그의 ID를 카메라 영상 속 객체에게 부여하여 추적한 뒤, 객체의 위치를 파악함.
- 교수자는 스마트폰 또는 PC로 웹서버에 접속하여 교실의 정보를 한 눈에 파악할 수 있음.
<br><br>


## 프로젝트 배경

### 1. 비접촉식 RFID 출입 시스템
<img src="https://user-images.githubusercontent.com/101806955/195024426-383a2351-fdd3-458b-b540-9408ee203523.png" width="600px" height="350px"></img>  
<br><br>
신뢰성있는 비접촉식 RFID 출입 시스템을 개발하여</br>
기존의 접촉식 RFID 출입 시스템을 사용하지 못하는 상황과</br>
사용자의 불편함을 해결하고자 함.
</br></br>

### 2. 교수자와 학생 간의 소통 문제
<img src="https://user-images.githubusercontent.com/101806955/195013863-3e963c05-d372-4bee-bfac-11f783b680e6.png" width="600px" height="552px"></img>
###### 출처: [충청뉴스 <한밭대, ‘MZ세대 학습자 이해와 공감’ 교수법 세미나 개최>](https://www.ccnnews.co.kr/news/articleView.html?idxno=258946)
</br>
코로나19 팬데믹 이후 비대면 수업으로 인해 교수자-학생 소통이 원활하지 않았고</br>
대면 수업 전환 이후에도 1학년부터 혹은 복학 후 비대면 수업을 경험한 상황 등에 의해</br>
소통에 어려움을 겪고 있는 상황임.</br>
학생의 위치와 정보를 한 눈에 파악할 수 있는 시스템을 통해</br>
교수자가 학생에 맞는 적절한 피드백을 줄 수 있고</br>
학생은 자신의 정보를 알고 있는 교수자와 더욱 적극적으로 소통할 수 있는 효과를 기대함.
</br></br>

### 3. 신뢰성 있는 영상 기반 객체추적 시스템 개발
영상 기반으로 객체를 추적하는 시스템은 결과물이 일반 사용자가 이해하기 쉽고</br>
활용방법이 다양하기 때문에 국내외로 연구가 활발히 진행 중에 있음.</br>
</br>
- 박종혁, 박도현, 현동환, 나유민 and 이수홍. (2022). 객체 추적 알고리즘을 활용한 딥러닝 기반 실시간 화재 탐지 시스템. 한국컴퓨터정보학회논문지, 27(1), 1-8. [LINK](https://www.kci.go.kr/kciportal/ci/sereArticleSearch/ciSereArtiView.kci?sereArticleSearchBean.artiId=ART002807623)
- 김경훈, 강석주, Junho Heo. (2019). 딥러닝 기반 실시간 다중 객체 추적 시스템. 한국방송미디어공학회 학술발표대회 논문집, (), 246-246. [LINK](https://scienceon.kisti.re.kr/srch/selectPORSrchArticle.do?cn=NPAP13342247)
- Wojke, N., Bewley, A., & Paulus, D. (2017, September). Simple online and realtime tracking with a deep association metric. In 2017 IEEE international conference on image processing (ICIP) (pp. 3645-3649). IEEE. [LINK](https://arxiv.org/abs/1703.07402)
- Du, Y., Song, Y., Yang, B., & Zhao, Y. (2022). Strongsort: Make deepsort great again. arXiv preprint arXiv:2202.13514. [LINK](https://arxiv.org/abs/2202.13514)

</br>
하지만 객체추적 AI는 고질적인 단점으로 사물에 의한 차폐와 객체 간의 겹침으로 인한 ID switching 문제를 가지고 있음.</br>
이를 해결하기 위한 방안을 고려하고 실제로 적용하여 기술적인 발전을 이루고자 함.
</br></br>

## 시스템 구조
![개요도](https://user-images.githubusercontent.com/101806955/195017256-fce55de8-b5cc-4e4a-bef0-7676db793d5d.png)
</br></br>
* 객체추적 프로그램
  * YOLOv5와 StrongSORT를 활용하여 객체를 탐지, 추적함.</br>
<div align="center">
  <img src="https://user-images.githubusercontent.com/101806955/195027182-bc15b870-0788-415c-8702-d792254fbc8c.png" width="400px" height="100px"></img>    
  <img src="https://user-images.githubusercontent.com/101806955/195032202-5b2e1c61-118a-4c73-9e3e-288ff1cdba62.png" width="300px" height="100px"></img>
</div>
</br></br>

* 서버
  * Nuxt.js, Node.js로 프론트/백엔드 개발.
  * Google Firebase Hosting로 배포.
<div align="center">
  <img src="https://user-images.githubusercontent.com/101806955/195033693-0ee9c805-42b8-452a-87f9-52b98d6b59e4.png" width="400px" height="100px"></img>    
  <img src="https://user-images.githubusercontent.com/101806955/195035144-54556f33-231b-48bd-9c2e-456f54ae50f5.png"></img>
  </br></br>
  <img src="https://user-images.githubusercontent.com/101806955/195034694-7128cf8d-aeb8-476a-917e-a8ab67f8f362.png" width="300px" height="100px"></img>
</div>
</br></br>

* DB
  * Google Firebase Realtime DB를 활용.
<div align="center">
  <img src="https://user-images.githubusercontent.com/101806955/195035930-aa134308-2dff-48ef-94f4-b9dd948fc380.png"></img>
</div>
</br></br>

* 어플리케이션
  * 웹서버 및 스마트폰 어플리케이션 개발.



## 결과물

