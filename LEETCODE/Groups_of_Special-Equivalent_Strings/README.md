# [LEETCODE] Groups of Special-Equivalent Strings

홀수 인덱스 & 짝수 인덱스끼리 짝이 맞는 쌍들의 그룹 갯수 구하기

### 접근

홀수 인덱스 알파벳의 집합 + 짝수 인덱스 알파벳의 집합의 쌍이 동일해야한다. 이를 찾기 위해 홀수 알파벳따로 모아 정렬 & 짝수 알파벳 따로 모아 정렬 한뒤 두 집합의 쌍을 키로 set을 구성하는 방법을 생각할 수 있다.
