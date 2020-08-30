# [LEETCODE] Find Peak Element

A peak element is an element that is greater than its neighbors.

Given an input array nums, where nums[i] ≠ nums[i+1], find a peak element and return its index.

The array may contain multiple peaks, in that case return the index to any one of the peaks is fine.

You may imagine that nums[-1] = nums[n] = -∞.

Example 1:

Input: nums = [1,2,3,1]
Output: 2
Explanation: 3 is a peak element and your function should return the index number 2.

Example 2:

Input: nums = [1,2,1,3,5,6,4]
Output: 1 or 5
Explanation: Your function can return either index number 1 where the peak element is 2,
or index number 5 where the peak element is 6.

### 주변 값을 확인하는 이진 탐색

nums[mid]값의 왼쪽값을 보든 오른쪽값을 보든 한쪽을 선택해서,

- `nums[mid] < nums[mid + 1]` --> / 이모양이면 left = mid +1
- `nums[mid] > nums[mid + 1]` --> \ 이모양이면 right = mid

로 범위를 줄여나가다가 끝나는 지점이 답이 된다.
