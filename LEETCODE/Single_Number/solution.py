class Solution:
    # extra space "result" + O(N)
    def singleNumber(self, nums: List[int]) -> int:
        result = 0
        for num in nums:
            result ^= num
        return result

    # O(N) + no extra space
    def singleNumber(self, nums: List[int]) -> int:
        for i in range(1, len(nums)):
            nums[i] = nums[i-1] ^ nums[i]
        return nums[-1]
