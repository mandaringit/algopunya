# [LEETCODE] Flipping an Image

binary matrix A를 flip & invert 하기

### 접근

2차원 배열의 요소를 모두 순회하는 선에서 끝내는게 최선이라고 생각했다 O(N^2)

하나의 행을 역으로 순회하면서 값도 역전(0 <-> 1)시켜 배열에 넣은 뒤 행의 순회가 끝나면 이를 모아두면 원하는 결과가 나온다.
