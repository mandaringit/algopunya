class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        index = 0
        number = nums[0]
        for i, num in enumerate(nums):
            if num > number:
                index = i
                number = num

        for num in nums:
            if num != number and num * 2 > number:
                index = -1
                break

        return index
