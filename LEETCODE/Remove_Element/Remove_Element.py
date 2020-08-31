from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        for i, num in enumerate(nums):
            if num == val:  # 지워야 할 값.
                pass
            else:
                nums[k] = num
                k += 1

        return nums


sol = Solution()

sol.removeElement([3, 2, 2, 3], 3)
