from typing import List


class Solution:

    def findLeft(self, nums, target):
        # 왼쪽 기준 구하기
        index = -1
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                index = mid

            if nums[mid] >= target:
                right = mid - 1
            else:
                left = mid + 1

        return index

    def findRight(self, nums, target):
        # 오른쪽 기준 구하기
        index = -1
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                index = mid

            if nums[mid] <= target:
                left = mid + 1
            else:
                right = mid - 1

        return index

    def searchRange(self, nums: List[int], target: int) -> List[int]:

        left = self.findLeft(nums, target)
        right = self.findRight(nums, target)

        return [left, right]


solution = Solution()
solution.searchRange([5, 7, 7, 8, 8, 8, 8, 8, 10], 8)
solution.searchRange([5, 7, 7, 8, 8, 10], 6)
solution.searchRange([], 0)
solution.searchRange([1], 1)
solution.searchRange([2, 2], 2)
