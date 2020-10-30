# [LEETCODE] Minimum Absolute Difference

두 수의 차이의 절대값이 최소인 쌍들 구하기

### 접근

모든 쌍을 찾아야 한다는 것 때문에 중첩 루프를 생각할 수 있지만 배열의 길이가 10^5이기 때문에 O(N^2)은 시간 초과로 이어진다.

문제에서 오름차순 정렬이 있었는데, 이를 위해서 배열을 일단 정렬한다. O(NlogN)으로 괜찮다.

정렬하고나니 인접한 두 수의 차이가 두쌍의 가장 작은 차이일 수밖에 없다는 것이 눈에 들어온다. O(N)의 접근으로 차이들을 비교할 수 있다. 최소가 나올때마다 담고있던 배열을 바꿔주면 된다.