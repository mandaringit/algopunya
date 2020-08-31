from typing import List


class Solution:

    # O(N) 풀이
    def minSubArrayLen(self, s, nums):
        summation = 0  # 합
        left = 0  # 부분 수열의 왼쪽 끝
        min_length = len(nums) + 1  # 최초 길이는 전체 + 1 (안되는 경우)
        for right, num in enumerate(nums):  # right - 부분 수열의 오른쪽 끝, num - 현재 수
            summation += num  # 합에 지금 수를 더함
            while summation >= s:  # 만약 합친 수가 목표한 수에 도달했다면
                # 최근 가장 짧은 길이와 현재 부분수열 길이를 비교한다.
                current_sub_arr_length = right - left + 1
                min_length = min(min_length, current_sub_arr_length)
                # 이제 부분 수열의 맨 왼쪽을 하나씩 줄여보며 조건에 충족하는지 확인한다
                summation -= nums[left]
                left += 1

        return min_length if min_length != len(nums) + 1 else 0

    # O(NlogN) 풀이
    def minSubArrayLen2(self, target, nums):
        result = len(nums) + 1
        for idx, n in enumerate(nums[1:], 1):
            nums[idx] = nums[idx - 1] + n
        left = 0
        for right, n in enumerate(nums):
            if n >= target:
                left = self.find_left(left, right, nums, target, n)
                result = min(result, right - left + 1)
        return result if result <= len(nums) else 0

    def find_left(self, left, right, nums, target, n):
        while left < right:
            mid = (left + right) // 2
            if n - nums[mid] >= target:
                left = mid + 1
            else:
                right = mid
        return left


sol = Solution()
print(sol.minSubArrayLen2(7, [2, 3, 1, 2, 4, 3]))
