# home-finder
## 골라줘 홈즈

team 도시비서 도비

[RDBMS](https://www.notion.so/RDBMS-d159b799e811428381d32dfebaa08c41)

[부동산 실거래가 분석 관련](https://www.notion.so/c59496a605424f259606d35e05e19ff5)

### 1. 개요

    1-1. 주제 선정 배경, 기획 배경

공모전 참가

[공지사항<알림마당<한국감정원](http://www.reb.or.kr/kab/home/notice/noticeDetail.jsp?sBoardIdx=045005125001035026121)

네비게이션 관련 알고리즘 참고

[다익스트라(Dijkstra) 알고리즘](https://goodgid.github.io/Dijkstra-Algorithm/)

목적지를 중심으로 이사할 지역 혹은 부동산을 추천해주는 실거래가 및 이동거리 기반 서비스

- 기획 배경

부동산 검색 기존 아쉬움

- 지역을 고르고 찾아야 하는 아쉬움

[No.1 부동산 앱, 직방](https://www.zigbang.com/)

[네이버 부동산](https://land.naver.com/)

[호갱노노 - 아파트 실거래가 1등 앱](https://hogangnono.com/)

- 거래를 성사하지 않더라도 사람들의 관심 지역 확인이나 목적지 확인하는 기록들 자체가 자산이 될 수 있다. - 기록 및 활용방안 검토

1-2. 과제 목표, 작품 제작의도 및 컨셉

1. 목적지로부터 주변의 월세 및 부동산 가격을 스캔한 뒤 - 실거래가로 학습을 시키고 예상치로 기준을 설정 후 정보를 제공

실거래가 학습 예시

[랜드북 - 인공지능 부동산 솔루션](https://www.landbook.net/)

- 가격 분포 파악 예시(예시는 생활인구, 가격과 경향성이 비슷할 것으로 예상되어 참고)

[서울 생활인구 데이터를 격자로 재할당하기 ver2](https://www.vw-lab.com/87)

![골라줘 홈즈 25fbd8e9820b42fb8b0d2d81781d3f1e/Untitled.png](images/Untitled.png)

2. 걸리는 거리 - 대전제는 ‘시간’ -

ex) 특정 역으로부터의 거리 시각화

[Isochrone map of Seoul Subway](https://vuski.github.io/seoulsubway/)

![images/Untitled%201.png](images/Untitled%201.png)

1. 1안 실제 교통정보 api를 이용해서 교통 상황만 받아온 직접 네비게이션 알고리즘 개발
2. 2안 길찾기 api 
- 차로 도보 대중교통 모두 계산

3. 선호 항목 등의 필터 - 부동산 실거래가 데이터 테이블과 추가로 얻을 수 있는 데이터가 있는 지 확인 후에 정할 수 있다.

위 요소의 합산을 통해 추천 지역을 산정해주고
(가능하다면 그 지역에서의 실제 매물 제시까지)

1-3. 계획(초안, 수정안)

추천 알고리즘을 통해 우선 순위를 던져준다.

= 월세버전, 전세 매매 다 가능할 것으로 보임 - 왜냐 실거래가 데이터가 종류별로 다 있으니까 이를 모두 적용할 예정

매매 버전은 여기에 더해 해당 부동산의 미래가치 등을 예상한 표 역시 같이 던져준다

S = 대부분 부동산 검색은 지역 자체를 기준으로 하기 때문에 실제 사용자들이 원하는 경험과 동떨어져 있어서 이와 같은 방식이 나쁘지 않을 것 같다

W =     = 실거래가 당연히 서울 공공, 경기 공공 데이터

= 매물 => 네이버? 직방? 일단 포기 나중에 혹시 가능하면 추가하는거고 일단 구현에서 뺌

O = 자체적으로 강력한 플랫폼으로, 딱 이 한가지 기능만 구현되어도 서비스 적 가치가 충분하고 추후 확장성 역시 보장

T = 실제 디비를 소유한 플랫폼에서 비슷한거 만들어버리면 걍 끝남

변수  = 주로 출근은 언제하세요? - 시간 변수를 사용자가 입력할 수 있게 할까?

주로 퇴근은 언제하세요?

출퇴근 위치는 정할 수 있어야됨 = 가장 중요한 가중치고

2. 추진과정 및 방법

2-1. 주요 추진 과정 절차	

2-1-1. 데이터 정제 및 위치 태깅

![images/Untitled%202.png](images/Untitled%202.png)

2-1-2. 부동산 데이터 분리 저장

![images/Untitled%203.png](images/Untitled%203.png)

2-1-3. 연결

![images/Untitled%204.png](images/Untitled%204.png)

![images/Untitled%205.png](images/Untitled%205.png)

![images/Untitled%206.png](images/Untitled%206.png)

2-1-5. 스프링과 회원관리 로직 연결

![images/Untitled%207.png](images/Untitled%207.png)

2-1-4. LSTM으로 법정동 별 월 평균을 학습시켜 예측값 적용

주로 실거래가를 분석하는데 쓰이는데, 

전월세 전환율을 적용한 합산 값을 기준으로 쓸 예정 

([https://roboreport.co.kr/딥러닝lstm으로-아파트-지수-예측하기-2-lstm-실험하기/](https://roboreport.co.kr/%EB%94%A5%EB%9F%AC%EB%8B%9Dlstm%EC%9C%BC%EB%A1%9C-%EC%95%84%ED%8C%8C%ED%8A%B8-%EC%A7%80%EC%88%98-%EC%98%88%EC%B8%A1%ED%95%98%EA%B8%B0-2-lstm-%EC%8B%A4%ED%97%98%ED%95%98%EA%B8%B0/)) 참고

2-2. 방법 및 활용 프로그램	.

2-2-1. 활용 프로그램

![images/Untitled%208.png](images/Untitled%208.png)

![images/Untitled%209.png](images/Untitled%209.png)

![images/Untitled%2010.png](images/Untitled%2010.png)

![images/Untitled%2011.png](images/Untitled%2011.png)

2-3. 단계별 수행 내용

(기획, 제작, 테스트)

### 3. 결과

- 개선사항
    1. 추가적으로 2차 3차 가중치를 더할 수 있게 하자. - 사용자가 퍼센트를 입력할 수 있게? 기본값은 던져주지만, 변경 가능하게
    2. 웹 화면 - 사용자 경험 = 지도로 할지, 다른 패러다임이 있을지 조금 더 고민해보자. (three, d3 등 자유롭게 생각 가능)
- 활용 계획
    1. 투자 등의 목적이 아닌 실제 거주를 위한 매물 탐색을 하는 소비자들의 니즈를 충족시켜준다.
