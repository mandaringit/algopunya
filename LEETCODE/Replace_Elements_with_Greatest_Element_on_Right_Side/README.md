# [LEETCODE] Replace Elements with Greatest Element on Right Side

자신을 자신의 오른쪽에 있는 요소들 중 가장 큰 수로 교체한 결과를 리턴

### 접근

- bruteforce
  내 옆을 찾으면서 가는건 O(N^2)으로 시간이 너무 오래걸린다.

- 역순으로 순회하기 O(N)
  역순으로, 최댓값을 -1부터 시작해서 현재 인덱스의 값은 지금까지 나온 최댓값으로 변경하면 되고, 바뀌기 이전의 원본값이 최댓값보다 컸다면 최댓값도 변경하면서 순회한다.
