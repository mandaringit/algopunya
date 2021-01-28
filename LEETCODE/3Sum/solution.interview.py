from typing import List


class Solution:
    # 브루트 포스. TLE. O(N^3)
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return []

        nums.sort()  # 편의상 정렬..
        result = []

        for i in range(len(nums) - 2):
            # 이전 값과 다른 경우에만 다음 루프로 이동. 정렬해서 가능한 로직임.
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            for j in range(i + 1, len(nums) - 1):
                if j > i + 1 and nums[j] == nums[j-1]:
                    continue

                for k in range(j + 1, len(nums)):
                    if k > j + 1 and nums[k] == nums[k-1]:
                        continue

                    if nums[i] + nums[j] + nums[k] == 0:
                        result.append([nums[i], nums[j], nums[k]])

        return result

    # i를 고정하고, 투포인터 O(N^2)
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return []

        nums.sort()  # O(NlogN)
        result = []

        for i in range(len(nums) - 2):

            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # 투포인터
            left, right = i+1, len(nums) - 1

            while left < right:
                summation = nums[left] + nums[right] + nums[i]
                if summation > 0:
                    right -= 1
                elif summation < 0:
                    left += 1
                else:
                    # summation == 0
                    result.append([nums[i], nums[left], nums[right]])

                    # [0,0,0,2,2,2] 같은 경우. 중복되지 않도록 끝까지 이동시켜야한다.
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1

        return result
