# [LEETCODE] Search for a Range

Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].

Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]

Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]

### 해당 타겟이 시작~끝나는 범위를 구하라.

왼쪽과 오른쪽 기준 두개를 찾아야 하므로 이진 탐색도 두번 수행한다.

왼쪽은 범위를 왼쪽으로 좁혀가며, 오른쪽은 범위를 오른쪽으로 좁혀가며 타겟을 찾으면, 일단 그 자리를 기억해둔 다음 옆으로 조금씩 더가서 각자의 범위에서 처음 나온 수를 찾는것과 같다.
