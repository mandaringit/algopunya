# [LEETCODE] Search in Rotated Sorted Array

Given an integer array nums sorted in ascending order, and an integer target.

Suppose that nums is rotated at some pivot unknown to you beforehand (i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).

You should search for target in nums and if you found return its index, otherwise return -1.

Example 1:

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4

Example 2:

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1

Example 3:

Input: nums = [1], target = 0
Output: -1

Constraints:

- 1 <= nums.length <= 5000
- -10^4 <= nums[i] <= 10^4
- All values of nums are unique.
- nums is guranteed to be rotated at some pivot.
- -10^4 <= target <= 10^4

### HOW

제일 작은거 기준으로 나눠서 하려고 했는데, 그럴거면 타겟을 찾는게 낫지 않나 싶었음. 이진 탐색이 O(N)인거 O(logN)으로 줄일려고 하는건데 이미 N번 돌면 시간초과날거같음

몇 군데 참고해서 힌트를 얻었는데, 이 피벗된 배열의 큰 특징중 하나는 중간을 기준으로 좌 우로 나누면 둘 중 하나는 무조건 정렬된 배열이라는 점이다.

그렇기 때문에 mid를 기준으로 반으로 나눈 다음, `[A][B]`

- 왼쪽(A)이 정렬된 경우

  1. A 내부에 위치한다면 -> 오른쪽 기준을 mid - 1로 옮긴다. 즉 `[A]` 부분으로 범위를 변경
  2. A 바깥에 위치한다면 -> 왼쪽을 mid + 1 로 옮긴다. 즉 `[B]` 부분으로 범위를 변경

- 오른쪽(B)이 정렬된 경우
  위와 반대로 한다.

즉, 절반씩 나누면서 타겟이 포함된 배열의 범위로 조금씩 줄여나가다가, 어느순간 배열이 정렬된 경우를 찾을 것이고, 그때부턴 일반적인 이진 탐색이 계속해서 이어진다고 보면 된다.
