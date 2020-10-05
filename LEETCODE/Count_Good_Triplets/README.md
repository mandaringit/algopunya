# [LEETCODE] Count Good Triplets

정수 배열 arr과 세 정수 a,b,c가 주어질 때, good triplets을 찾아라.

- triplet (arr[i], arr[j], arr[k])
- 0 <= i < j < k < arr.length
- |arr[i] - arr[j]| <= a
- |arr[j] - arr[k]| <= b
- |arr[i] - arr[k]| <= c

### 접근

- bruteforce
  세개의 수를 고르는 모든 경우를 시도. O(N^3)이지만 이 문제 같은 경우 N이 최대 100으로 가능함.

  중간에 조건을 확인하는 방법을 쓰면 약간의 최적화가 가능하긴 하다.
