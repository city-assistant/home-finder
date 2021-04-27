# home-finder

[주요 과정](home-finder%20e8c139eba89f4571961b32306766cdb1/%E1%84%8C%E1%85%AE%E1%84%8B%E1%85%AD%20%E1%84%80%E1%85%AA%E1%84%8C%E1%85%A5%E1%86%BC%20b691d059d56445afa5d2ce0f4282e274.md)

[RDBMS](home-finder%20e8c139eba89f4571961b32306766cdb1/RDBMS%20d159b799e811428381d32dfebaa08c41.md)

[부동산 실거래가 분석 관련](home-finder%20e8c139eba89f4571961b32306766cdb1/%E1%84%87%E1%85%AE%E1%84%83%E1%85%A9%E1%86%BC%E1%84%89%E1%85%A1%E1%86%AB%20%E1%84%89%E1%85%B5%E1%86%AF%E1%84%80%E1%85%A5%E1%84%85%E1%85%A2%E1%84%80%E1%85%A1%20%E1%84%87%E1%85%AE%E1%86%AB%E1%84%89%E1%85%A5%E1%86%A8%20%E1%84%80%E1%85%AA%E1%86%AB%E1%84%85%E1%85%A7%E1%86%AB%20c59496a605424f259606d35e05e19ff5.md)

# **1. 개요**

### 회사나 학교를 옮겨 새로운 거처를 마련하고자 할 때에, 해당 학교나 회사는 물론이고 주변 지역 역시 익숙하지 않은 경우가 많다.

### - 이 때, 목적지(회사 혹은 학교 위치)와 예산, 거리를 설정하면,

### - 사용자가 원하는 조건의 부동산(특히, 월세)에 해당하는 세부 지역을 추천하고,

### - 실제 이루어졌던 거래들을 확인해 시세 파악 및 덤터기 방지

### 실제 계약 직전까지의 부동산 확인에 도움을 준다.

![home-finder%20e8c139eba89f4571961b32306766cdb1/homefinder_search_(2).gif](home-finder%20e8c139eba89f4571961b32306766cdb1/homefinder_search_(2).gif)

## 주제 선정 배경

- 매매 혹은 분양 위주의 정보 사이트는 다양하게 존재하지만 학생이나 사회초년생이 실제로 집을 구하는 이유는  학교나 회사 근처에 출,퇴근을 위함이 큽니다.  하지만 실제적으로 월세 등을 구할 때 찾아볼 만한 사이트는 없다고 판단했습니다.  또한 지역을 한정 지어 검색하는 것을 주로 하는 기존 서비스들은 사용자가 주로 부동산을, 특히 월세 부동산을 검색하는 이유인 '목적지'개념과 동떨어져 있다고 판단해, 목적지를 중심으로 검색할 수 있는 서비스를 계획했습니다.

결론적으로 목적지를 중심으로 이사할 지역 혹은 부동산을 추천해주는 전월세 실거래가 및 거리 기반 서비스를 제작하는 것으로 목표를 잡았습니다.

## 기획 배경

- 기존 부동산 매물 검색 시 목적지가 아닌 단순 지역 우선의 검색

    ![home-finder%20e8c139eba89f4571961b32306766cdb1/qq.jpg](home-finder%20e8c139eba89f4571961b32306766cdb1/qq.jpg)

    네이버                                                    직방                                               호갱노노

[No.1 부동산 앱, 직방](https://www.zigbang.com/)

[네이버 부동산](https://land.naver.com/)

[호갱노노 - 아파트 실거래가 1등 앱](https://hogangnono.com/)

## 과제 목표, 작품 제작의도 및 컨셉

- 목적지로부터 주변의 월세 및 부동산 가격을 스캔한 뒤 - 실거래가로 학습을 시키고 예상치로 기준을 설정 후 정보를 제공

[랜드북 - 인공지능 부동산 솔루션](https://www.landbook.net/)

![home-finder%20e8c139eba89f4571961b32306766cdb1.jpg](home-finder%20e8c139eba89f4571961b32306766cdb1.jpg)

                                            실거래가기반의  학습을 통한  토지가격 예측정보를 제공해주는 예시 

- 가격 분포 파악 예시

[서울 생활인구 데이터를 격자로 재할당하기 ver2](https://www.vw-lab.com/87)

![home-finder%20e8c139eba89f4571961b32306766cdb1/Untitled.png](home-finder%20e8c139eba89f4571961b32306766cdb1/Untitled.png)

                        생활인구, 가격과 경향성이 비슷할 것으로 예상

- 목적지로 부터의 거리 또는 시간을 기준으로 매물 선정

[Isochrone map of Seoul Subway](https://vuski.github.io/seoulsubway/)

![home-finder%20e8c139eba89f4571961b32306766cdb1/Untitled%201.png](home-finder%20e8c139eba89f4571961b32306766cdb1/Untitled%201.png)

                                                                     특정 역으로부터의 거리 시각화

- 실제 교통정보 api를 이용해서 교통 상황만 받아온 직접 네비게이션 알고리즘 개발
- 길찾기 api
- 차로 도보 대중교통 모두 계산
- 선호 항목 등의 필터 - 부동산 실거래가 데이터 테이블과 추가로 얻을 수 있는 데이터가 있는 지 확인 후에 정할 수 있다.

위 요소의 합산을 통해 추천 지역 산정 및 실제 매물을 제시해주는 Concept

## 개발 계획

- 정부에서 제공하는 실거래가 데이터를 토대로 사용자의 목적지로부터 거리를 한정해, 사용자의 예산에 해당하는 지역을 1차적으로 걸러 추천
- 이후 각 지역별로 클릭하면 상세 정보를 확인하고 분석 자료를 받아볼 수 있는 구조로 구성

이를 위해서는

1. 파이썬을 이용한 실거래가 빅데이터 전처리 및 정제
2. 엘라스틱 서치를 통한 빅데이터 검색 관리
3. 오라클과 스프링 서버를 통한 회원 관리
4. 사용자 화면 구성을 위한 Vue Cli 프론트엔드 서버
5. 시계열 데이터를 활용한 데이터 머신러닝을 통해 지역의 현재 예측되는 예상 월세 도출

추가적으로

파이썬 머신러닝을 사용자가 활용할 수 있게 하는 Flask서버 및 Map API 구현 

## SWOT 분석을 통한 전략 수립

![home-finder%20e8c139eba89f4571961b32306766cdb1/Untitled%202.png](home-finder%20e8c139eba89f4571961b32306766cdb1/Untitled%202.png)

## 방법 및 활용 프로그램	.

- 활용 프로그램 및 구조

    ![home-finder%20e8c139eba89f4571961b32306766cdb1/Untitled%203.png](home-finder%20e8c139eba89f4571961b32306766cdb1/Untitled%203.png)

- 단계별 수행 내용

![home-finder%20e8c139eba89f4571961b32306766cdb1/Untitled%204.png](home-finder%20e8c139eba89f4571961b32306766cdb1/Untitled%204.png)

회원 관리 데이터  및 관심 데이터 저장

![home-finder%20e8c139eba89f4571961b32306766cdb1/Untitled%205.png](home-finder%20e8c139eba89f4571961b32306766cdb1/Untitled%205.png)

실거래가 분석 및 저장 - 검색

![home-finder%20e8c139eba89f4571961b32306766cdb1/D7CE7815-0CB1-48EC-ABFD-02811569718A.png](home-finder%20e8c139eba89f4571961b32306766cdb1/D7CE7815-0CB1-48EC-ABFD-02811569718A.png)

머신러닝 유저 사용을 위한 플라스크 서버

![home-finder%20e8c139eba89f4571961b32306766cdb1/Untitled%206.png](home-finder%20e8c139eba89f4571961b32306766cdb1/Untitled%206.png)

지도 및 검색의 실 사용자 

![home-finder%20e8c139eba89f4571961b32306766cdb1/Untitled%207.png](home-finder%20e8c139eba89f4571961b32306766cdb1/Untitled%207.png)

Spring - 데이터 전달 허브, JWT를 통한 보안 관리

## 추진과정 및 방법

- 주요 개발과정 절차

    데이터 정제 및 위치 태깅(python) - data science

    ![home-finder%20e8c139eba89f4571961b32306766cdb1/Untitled%208.png](home-finder%20e8c139eba89f4571961b32306766cdb1/Untitled%208.png)

    부동산 데이터 분리 저장(Elastic Search)

    ![home-finder%20e8c139eba89f4571961b32306766cdb1/Untitled%209.png](home-finder%20e8c139eba89f4571961b32306766cdb1/Untitled%209.png)

           특히 시계열 형식과 위경도를 엘라스틱 서치에 삽입하기 위해 geo point, timestamp 타입 활용이 중요

    2-1-3. ElasticSearch와 KakaoMap 연결 및 검색구현

    ![home-finder%20e8c139eba89f4571961b32306766cdb1/Untitled%2010.png](home-finder%20e8c139eba89f4571961b32306766cdb1/Untitled%2010.png)

                  카카오맵 api와 저장해둔 데이터를 연결시켜서 지도에 위치와 가격을 통한 검색을 실현

    ![home-finder%20e8c139eba89f4571961b32306766cdb1/Untitled%2011.png](home-finder%20e8c139eba89f4571961b32306766cdb1/Untitled%2011.png)

                                                         검색된 지역을 선택하면 해당되는 지역

    ![home-finder%20e8c139eba89f4571961b32306766cdb1/Untitled%2012.png](home-finder%20e8c139eba89f4571961b32306766cdb1/Untitled%2012.png)

    LSTM으로 법정동 별 월 평균을 학습시켜 예측값 적용

    주로 실거래가를 분석하는데 쓰이는데, 

    전월세 전환율을 적용한 합산 값을 기준으로 쓸 예정 

    ([https://roboreport.co.kr/딥러닝lstm으로-아파트-지수-예측하기-2-lstm-실험하기/](https://roboreport.co.kr/%EB%94%A5%EB%9F%AC%EB%8B%9Dlstm%EC%9C%BC%EB%A1%9C-%EC%95%84%ED%8C%8C%ED%8A%B8-%EC%A7%80%EC%88%98-%EC%98%88%EC%B8%A1%ED%95%98%EA%B8%B0-2-lstm-%EC%8B%A4%ED%97%98%ED%95%98%EA%B8%B0/)) 참고

    스프링과 회원관리 로직 연결

    ![home-finder%20e8c139eba89f4571961b32306766cdb1/Untitled%2013.png](home-finder%20e8c139eba89f4571961b32306766cdb1/Untitled%2013.png)

## 결과

- 개선사항

    추가적으로 2차 3차 가중치를 더할수 있도록 Defualt값은 제공하지만 사용자가 퍼센트를 입력할 수 있게 변경이 가능하도록 

    웹 화면 - 사용자 경험 = 지도로 할지, 다른 패러다임이 있을지 조금 더 고민해보자. (three.js, d3 등 자유롭게 생각 가능)

- 활용 계획

    투자 등의 목적이 아닌 실제 거주를 위해 매물 탐색을 하는 소비자들의 니즈를 충족시켜준다.

    추가적으로 개발자 입장에서는 이런 사람들의 검색 기록들 자체가 사람들의 관심을 기록할 수 있는 토대가 될 수 있을 것이라 판단된다
