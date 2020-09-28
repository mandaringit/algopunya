class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        result = []

        for i in range(len(nums) // 2):
            result.append(nums[i])
            result.append(nums[n+i])

        return result
