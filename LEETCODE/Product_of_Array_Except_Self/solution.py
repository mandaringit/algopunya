class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        N = len(nums)
        output = [1]*N

        p = 1
        for i in range(N):
            output[i] = output[i] * p
            p = p * nums[i]

        p = 1
        for i in range(N-1, -1, -1):
            output[i] = output[i] * p
            p = p * nums[i]

        return output
