from typing import List


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:

        def merge(left, right):
            l, r = 0, 0
            result = []
            while l < len(left) and r < len(right):
                if left[l] < right[r]:
                    result.append(left[l])
                    l += 1
                else:
                    result.append(right[r])
                    r += 1

            result.extend(left[l:])
            result.extend(right[r:])

            return result

        def merge_sort(nums):
            N = len(nums)

            if N == 1:
                return nums

            half = N // 2
            left_list = merge_sort(nums[:half])
            right_list = merge_sort(nums[half:])

            return merge(left_list, right_list)

        return merge_sort(nums)


sol = Solution()
sol.sortArray([5, 2, 3, 1])
