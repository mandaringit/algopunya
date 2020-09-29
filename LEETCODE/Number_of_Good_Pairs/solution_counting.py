class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:

        counter = [0]*101
        pair_count = 0

        for num in nums:
            pair_count += counter[num]
            counter[num] += 1

        return pair_count
