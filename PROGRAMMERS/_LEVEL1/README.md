# PROGRAMMERS 문제풀이 (LEVEL 1)

- [x] 1회 완료

프로그래머스 코딩테스트 연습

## 문제별 풀면서 생각

### 쏘쏘

- K번째수
- 2016년
- 가운데 글자 가져오기
- 같은 숫자는 싫어
- 나누어 떨어지는 숫자 배열
- 두 정수 사이의 합
- 문자열 내 p와 y의 개수
- 문자열 내림차순으로 배치하기
- 문자열 다루기 기본
- 서울에서 김서방 찾기
- 수박수박수박수박수박수?
- 문자열 정수로 바꾸기
- 약수의 합
- 이상한 문자 만들기 : 각 단어가 하나 이상의 공백문자로 구분됨! 주의.
- 자릿수 더하기
- 자연수 뒤집어 배열로 만들기
- 정수 내림차순으로 배치하기
- 정수 제곱근 판별
- 제일 작은 수 제거하기
- 짝수와 홀수
- 최대공약수와 최소공배수
- 콜라츠 추측
- 평균 구하기
- 하샤드 수
- 핸드폰 번호 가리기
- 행렬의 덧셈 : zip을 써보긴 했는데, 더 쉬운게 있겠지?
- x만큼 간격이 있는 n개의 숫자
- 직사각형 별찍기
- 예산

### 멍청한짓해서 오래걸림

- 모의고사 : 주어진 학생 답을 잘못써서 활용했음

- 체육복 : 코드좀 줄여본다고 리스트를 돌면서 리스트를 remove 하고있었음. 그냥 하던대로 하자

- 시저 암호 : 간단하긴 한데, n 이 25이하인 자연수라는 조건을 안읽고 그 이상도 생각해서 하다보니 조금 걸림. 그렇다고 어려워지는것도 아니긴 하지만.. 종이에 써서해..

### 살짝 고민

- 문자열 내 마음대로 정렬하기 : 딕셔너리 밸류로 리스트 써보기. 다른방법도 있겠지?

- 소수 찾기 : 소수를 찾는건 전부다 돌면서 찾으면 코드가 그렇게 어려운건 아니지만, 수가 커질땐 굉장히 오래걸리게 된다. for문이 두번이니까 n까지 찾으면 거의 O(n^2).
    - 이를 해결할 방법이 [에라토스테네스의 체](https://ko.wikipedia.org/wiki/%EC%97%90%EB%9D%BC%ED%86%A0%EC%8A%A4%ED%85%8C%EB%84%A4%EC%8A%A4%EC%9D%98_%EC%B2%B4) 라고 하는게 있다. 약간 복잡하긴 하지만 이 방법을 이용하면 시간이 엄청 줄어든다. n = 10000 기준으로 전부다 도는 코드는 약 __4250ms__ 가 걸렸지만 에라토스테네스의 체를 이용한 코드는 __12ms__ 밖에 걸리지 않았다...! 노트북파일과 py파일을 남겨놓는다.


### 쫌 고민

- 완주하지 못한 선수 : __나중에 한번더 깔끔하게 해보기__

### 못품

- 