class Solution:
    def pivotIndex(self, nums: List[int]) -> int:

        # 길이가 0인 경우는
        if len(nums) == 0:
            return -1

        left = nums[0]
        right = sum(nums)

        # 시작부터 합이 0 인 얘들은
        if left == right:
            return 0

        # 지속적으로 sum() 하는 것보다 한 요소씩 빼고 더하는게 시간이 덜듬
        for i in range(1, len(nums)):
            left += nums[i]
            right -= nums[i-1]

            if left == right:
                return i

        return -1
