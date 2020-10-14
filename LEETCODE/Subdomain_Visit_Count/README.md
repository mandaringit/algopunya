# [LEETCODE] Subdomain Visit Count

모든 하위도메인의 방문 횟수 구하기

### 접근

1. 각 count-paired domain을 count와 domain으로 나눈다.
2. domain을 분리하고 가능한 모든 도메인 조합(.은 최대 2개뿐이니 오래걸리지 않음)을 키로, 각 값에 count를 더한다.
3. 모든 키 & 값 리턴

그래프로 해도 괜찮을까?
