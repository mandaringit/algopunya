class Solution:
    # cascading ?
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = [[]]
        for num in nums:
            result += [i + num for i in result]

        return result

    def subset_bit(self, nums):
        subsets = []
        N = len(nums)

        for i in range(1 << N):
            subset = []
            for j in range(N):
                if (i >> j) & 1:
                    subset.append(nums[j])
            subsets.append(subset)
        return subsets
