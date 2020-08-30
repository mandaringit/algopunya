class Solution:
    def findPeakElement1(self, nums: List[int]) -> int:
        left, right = 0, len(nums)

        while left < right:
            mid = (left + right) // 2

            # - 무한대 표현을 그냥 기준 - 1로 해줌. 낮기만 하면 되니까.
            l_value = nums[mid - 1] if mid != 0 else nums[mid] - 1
            r_value = nums[mid + 1] if mid != len(nums) - 1 else nums[mid] - 1

            if l_value < nums[mid] and nums[mid] > r_value:  # /\
                return mid
            elif l_value < nums[mid] < r_value:  # / , 오른쪽으로 가야한다.
                left = mid + 1
            elif l_value > nums[mid] > r_value:  # \ , 왼쪽으로 가야한다.
                right = mid - 1
            else:  # \/ 아무쪽이나 가도 상관 없다?
                left = mid + 1

        return left

    # 오른쪽값만 보고 판단하는 경우
    def findPeakElement2(self, nums: List[int]) -> int:
        left, right = 0, len(nums)

        while left < right:
            mid = (left + right) // 2
            r_value = nums[mid + 1] if mid != len(nums) - 1 else nums[mid] - 1

            if nums[mid] < r_value:  # /
                left = mid + 1
            else:  # \
                right = mid

        return left
