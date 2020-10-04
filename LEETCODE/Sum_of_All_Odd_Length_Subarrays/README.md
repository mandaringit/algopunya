# [LEETCODE] Sum of All Odd Length Subarrays

홀수 길이의 모든 부분 배열의 합 구하기

### 접근

- 1 <= arr.length <= 100
- 1 <= arr[i] <= 1000

- 브루트포스

  가장 간단하지만 시간이 꽤 걸린다.대략 O(N^3)이라고 한다.

- 수학적인 방법 O(1)

몇번 등장하는지 ? 횟수를 세어보면 규칙성을 발견할 수 있다.

Consider the subarray that contains A[i],
we can take 0,1,2..,i elements on the left,
from A[0] to A[i],
we have i + 1 choices.

we can take 0,1,2..,n-1-i elements on the right,
from A[i] to A[n-1],
we have n - i choices.

결과적으로 `A[i]`, 즉 배열의 i번째 인덱스가 등장하는 횟수는 `(i + 1) * (n - i)`이다. (i는 인덱스 ,n은 전체 길이)
그리고 홀수 길이에 대해선 `((i + 1) * (n - i) + 1) / 2` 만큼 등장하며, 짝수 길이에 대해선 `((i + 1) * (n - i)) / 2` 만큼 등장한다.

```text
  Example of array [1,2,3,4,5]
  1 2 3 4 5 subarray length 1
  1 2 X X X subarray length 2
  X 2 3 X X subarray length 2
  X X 3 4 X subarray length 2
  X X X 4 5 subarray length 2
  1 2 3 X X subarray length 3
  X 2 3 4 X subarray length 3
  X X 3 4 5 subarray length 3
  1 2 3 4 X subarray length 4
  X 2 3 4 5 subarray length 4
  1 2 3 4 5 subarray length 5

  5 8 9 8 5 total times each index was added.
  3 4 5 4 3 total times in odd length array with (x + 1) / 2
  2 4 4 4 2 total times in even length array with x / 2
```
