from collections import deque


class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        nums.sort(reverse=True)

        N = len(nums)
        total = 0
        remainder = sum(nums)
        result = []
        for i in range(N):
            result.append(nums[i])
            total += nums[i]
            remainder -= nums[i]

            if total > remainder:
                return result
