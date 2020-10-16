# [LEETCODE] Find Common Characters

모든 단어에 공통으로 들어가는 charaters 찾기(중복 포함)

### 접근

첫 단어를 기준으로 알파벳의 빈도를 Counter로 구한다. 다음 단어들을 순회하며 역시 Counter로 세고, 같은 키를 가지고 있으면 해당 키의 값을 둘 중 작은쪽으로 변경한다.

마지막에 남은 값들을 반환.
