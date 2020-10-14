# [LEETCODE] Find Positive Integer Solution for a Given Equation

`f(x, y) < f(x + 1, y)`, `f(x, y) < f(x, y + 1)`를 만족하는 랜덤 함수가 주어질 때, `f(x,y) == z`를 만족하는 쌍을 모두 찾아라.

### 접근

- bruteforce
  모든 경우를 탐색했다.
