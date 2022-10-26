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
하지만 객체추적 AI는 고질적인 단점으로</br>
사물에 의한 차폐와 객체 간의 겹침으로 인한 ID switching 문제를 가지고 있음.</br>
이를 해결하기 위한 방안을 고려하고 실제로 적용하여 기술적인 성과를 얻고자 함.
</br></br>

## 시스템 구조
![개요도](https://user-images.githubusercontent.com/101806955/195017256-fce55de8-b5cc-4e4a-bef0-7676db793d5d.png)
</br></br>
### 객체추적 프로그램
  * YOLOv5와 StrongSORT를 활용하여 객체를 탐지, 추적함.</br>
<div align="center">
  <img src="https://user-images.githubusercontent.com/101806955/195027182-bc15b870-0788-415c-8702-d792254fbc8c.png" width="400px" height="100px"></img>    
  <img src="https://user-images.githubusercontent.com/101806955/195032202-5b2e1c61-118a-4c73-9e3e-288ff1cdba62.png" width="300px" height="100px"></img>
  </br>
  
  YOLOv5 by Glenn Jocher [[github]](https://github.com/ultralytics/yolov5)</br>
  YOLOv5+StrongSORT with OSNet by Mikel Brostrom [[github]](https://github.com/mikel-brostrom/Yolov5_StrongSORT_OSNet)
</div>
</br></br>

* YOLOv5</br>
  (YOLOv1 논문) - [You Only Look Once: Unified, Real-Time Object Detection](https://arxiv.org/abs/1506.02640)</br>
  기존 R-CNN 모델은 Bounding Box Regression, Detection Score를 찾는 2가지의 task를 수행했지만</br>
  YOLO는 'You Only Look Once'라는 논문의 제목에 어울리게 Regression Task 1가지의 task로 처리하여</br>
  R-CNN에 비해 성능은 조금 하락했지만 detection 속도를 상승시킨 1-stage detector.</br>
  때문에 Real-time object detection에 적합한 특성을 가짐.</br>
  YOLOv5는 여러 버전을 거쳐 pytorch 프레임워크를 도입하여 개발된 모델.</br>
</br>

* StrongSORT</br>
![image](https://user-images.githubusercontent.com/101806955/197722166-0dcdcf18-3215-4dcc-a116-0887eebb66a9.png)</br>
  ![image](https://user-images.githubusercontent.com/101806955/197728345-d2611d70-0d40-4032-a7c1-138ecf7b4f8b.png)</br>
  ![image](https://user-images.githubusercontent.com/101806955/197724671-a0a55b14-795a-4e04-865e-cc77e59110e2.png)</br>
  ![image](https://user-images.githubusercontent.com/101806955/197724278-c605b1b8-a1a3-484b-9b0a-0cce6c450489.png)</br>

  * BOT와 ResNet50을 backbone으로 객체의 appearance feature 정보를 획득.</br>
  * EMA 방식으로 객체들의 appearance state를 업데이트.</br>
  * 움직임 보정을 위해 ECC를 사용하고 low-quality detection과 noise에 취약한</br>
    기존의 kalman filter 대신 NSA kalman algorithm을 사용.
  * cost는 appearance cost와 motion cost의 weight sum.
</br></br>

* 차폐 및 ID switching 문제
  * 차폐 문제</br>
    객체가 사물에 가려져 추적이 불가능한 상태가 된 후 다시 등장했을 때 발생하는 문제.</br>
    사라졌던 객체의 ID가 유지되지 않고 새로운 ID가 부여되는 현상 발생.</br>
  * ID switching 문제</br>
    객체 간의 겹침이 발생했을 때 서로의 ID가 바뀌는 현상.</br>
  * 해결방안</br>
    * 차폐 문제</br>
      강의 정원에 맞춰 추적 개체의 최대치를 설정하여 차폐로 인한 새로운 ID 부여 현상을 감소시킴.</br>
    * ID switching 문제</br>
      학생이 앉은 자리를 잘 변경하지 않는다는 것을 고려하여 학생의 위치 정보 반고정처리 과정을 거침으로써</br>
      ID switching 발생률을 감소시킴.
</br></br>

### 서버
  * Nuxt.js, Node.js로 프론트/백엔드 개발.
  * Google Firebase Hosting로 배포.
<div align="center">
  <img src="https://user-images.githubusercontent.com/101806955/195033693-0ee9c805-42b8-452a-87f9-52b98d6b59e4.png" width="400px" height="100px"></img>    
  <img src="https://user-images.githubusercontent.com/101806955/195035144-54556f33-231b-48bd-9c2e-456f54ae50f5.png"></img>
  </br></br>
  <img src="https://user-images.githubusercontent.com/101806955/195034694-7128cf8d-aeb8-476a-917e-a8ab67f8f362.png" width="300px" height="100px"></img>
</div>
</br></br>

### DB
  * Google Firebase Realtime DB를 활용.
<div align="center">
  <img src="https://user-images.githubusercontent.com/101806955/195035930-aa134308-2dff-48ef-94f4-b9dd948fc380.png"></img>
</div>
</br></br>

### 어플리케이션
  * 웹서버 및 스마트폰 어플리케이션 개발.



## 결과물


## 결론
