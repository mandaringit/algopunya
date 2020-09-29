class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        N = len(nums)
        count = 0
        for i in range(N):
            for j in range(i+1, N):
                if nums[i] == nums[j]:
                    count += 1
        return count
