class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        m, counter = nums[0], 1

        for num in nums[1:]:
            if counter == 0:
                m, counter = num, 1
            elif m == num:
                counter += 1
            else:
                counter -= 1

        return m
