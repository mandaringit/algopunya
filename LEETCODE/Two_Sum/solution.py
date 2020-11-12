class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        numbers = {}
        for i, num in enumerate(nums):
            pair = target - num
            if pair in numbers:
                return [i, numbers[pair]]
            else:
                numbers[num] = i
