class Solution:

    def rob(self, nums: List[int]) -> int:

        prev_1, prev_2 = 0, 0  # 1개 전, 2개 전

        for num in nums:
            now = max(num + prev_2, prev_1)
            prev_2 = prev_1
            prev_1 = now

        return prev_1

    """
    def rob(self, nums: List[int]) -> int:
        N = len(nums)

        if N == 0:
            return 0
        elif N < 3:
            return max(nums)

        dp = [0]*len(nums)
        dp[0] = nums[0]
        dp[1] = nums[1]
        dp[2] = nums[2] + nums[0]

        max_robber = max(dp[0], dp[1], dp[2])

        for i in range(3, len(nums)):
            dp[i] = nums[i] + max(dp[i-2], dp[i-3])
            if dp[i] > max_robber:
                max_robber = dp[i]

        return max_robber
    """
