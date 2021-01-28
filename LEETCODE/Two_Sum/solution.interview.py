from typing import List


class Solution:
    # 브루트 포스.
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]

    # target - n이 존재할까?
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        for i, num in enumerate(nums):
            pair = target - num
            if pair in nums[i+1:]:
                return [i, i+1 + nums[i+1:].index(pair)]

    # target - n이 존재하는지 빠르게 알 수 있을까?
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        nums_map = {num: i for i, num in enumerate(nums)}

        for i, num in enumerate(nums):
            pair = target - num
            if pair in nums_map and nums_map[pair] != i:
                return [i, nums_map[pair]]

    # 두번 루프하지 않고 한번만.
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        nums_map = {}

        for i, num in enumerate(nums):
            pair = target - num
            if pair in nums_map:
                return [i, nums_map[pair]]
            nums_map[num] = i
