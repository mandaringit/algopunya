# [LEETCODE] Peak Index in a Mountain Array

Peak 값 찾기

### 접근

Peak값 찾기이지만 실상 "가장 큰 값 찾기"라고 봐도 무방해 보인다.

- bruteforce O(N)
  루프하면서 찾기

- binary search O(logN)
  "피크가 단 하나 뿐"이라는 조건이 있기 때문에 이진 탐색을 써도 무방하다. 증가하는지 / 감소하는지를 판단해 이진탐색을 만들 수 있다.
