from itertools import accumulate


class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:

        counter = [0] * 101
        for num in nums:
            counter[num] += 1

        stacked = list(accumulate(counter))

        result = []
        for num in nums:
            if num == 0:
                result.append(0)
            else:
                result.append(stacked[num - 1])

        return result
