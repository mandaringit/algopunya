# [LEETCODE] Find Minimum in Rotated Sorted Array

Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).

Find the minimum element.

You may assume no duplicate exists in the array.

Example 1:

Input: [3,4,5,1,2]
Output: 1

Example 2:

Input: [4,5,6,7,0,1,2]
Output: 0

### 이전 Rotated Sorted Array + 최솟값을 찾는 문제.

결국 이것도 반을 나누면, 둘중 하나는 정렬된 배열이고 그걸 토대로 문제를 풀어나가면 된다.

- 만약 왼쪽이 정렬된 부분이라면 이는 두가지 경우로 나눌 수 있는데

  1. `[4,5,6,7][8,1,2,3]` 처럼 왼쪽이 정렬되어 있지만 오른쪽 배열쪽에 작은 수가 있는경우 -> left = mid + 1

  2. `[1,2][3]` 처럼 왼쪽이 정렬도 되어있고 왼쪽에 작은수가 있는경우 -> right = mid - 1

- 오른쪽이 정렬된 상태라면

어차피 작은 쪽은 항상 오른쪽에 있으므로 left는 두고 right만 슬금슬금 내리면서 확인하면 된다.
