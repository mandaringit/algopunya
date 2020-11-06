class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        N = len(nums)
        missing = (N * (N+1)) // 2  # 토탈 합

        for num in nums:
            missing -= num

        return missing
