# [LEETCODE] Two Sum

합이 target이 되는 두 수 찾기

### 접근

- 브루트포스로 하기에는 시간이 너무 오래걸린다. O(N^2), N = 10^5

- HashMap을 활용해 시간 복잡도 O(N), 공간 복잡도 O(N)으로 해결

  A + B = target이니 A일때 우리가 찾을 B는 target - A임을 알 수 있다. HashMap에 key(값) - value(인덱스) 형식으로 저장해 놓으면 이를 빠르게 찾을 수 있다.
