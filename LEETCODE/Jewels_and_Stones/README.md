# [LEETCODE] Jewels and Stones

보석의 타입을 가지고있는 문자열 J와 가지고 있는 돌의 문자열 S가 주어질 때, 보석의 갯수는 ? 단, J에 중복된 문자열은 없으며 case sensitive.

- 추상화 : 문자열 S에 문자열 J가 가진 character가 몇개인지 카운팅하기

### 접근

S와 J가 최대 50 이므로 O(N)이 무리는 없어 보인다.

- 딕셔너리로 카운트
  종류별로 돌의 갯수를 세고, 보석을 순회하면서 몇개인지 카운트했다. collections.Counter가 돌의 갯수를 쉽게 세는데 도움을 줄 수 있다.
