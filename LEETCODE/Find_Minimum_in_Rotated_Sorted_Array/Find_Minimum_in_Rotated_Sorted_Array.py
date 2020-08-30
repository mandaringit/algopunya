class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1

        while left < right:
            mid = (left + right) // 2

            if nums[left] <= nums[mid]:  # 왼쪽이 정렬된 부분
                if nums[left] > nums[right]:  # 아직 왼쪽이 더 큰 모양일때
                    left = mid + 1
                else:
                    right = mid - 1
            else:  # 오른쪽이 정렬된 부분
                right = mid

        return nums[left]
