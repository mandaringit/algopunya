# [LEETCODE] Lucky Numbers in a Matrix

2차원 배열에서 row에서 가장 작고 column에서 가장 큰 수(lucky number)를 찾자.

### 접근

"모든 수가 유니크"하기 때문에 가능한 방법인데, 각 row에서 최소인 값을 모으고, 각 col에서 최대인 값을 모아 row 와 col에서 동시에 나오는 값을 리턴하면 된다.

유니크하기 때문에 둘 다에서 등장한다는 이야기는 특정 row에서 가장 작고, col에선 가장 큰 값이라는 말이기 때문.
