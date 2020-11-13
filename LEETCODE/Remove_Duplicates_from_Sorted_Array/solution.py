class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return len(nums)

        slow = 0  # 여기까지 중복되지 않았습니다.
        fast = 1  # 다음 수를 찾으러 갑니다.
        while fast < len(nums):
            if nums[fast] <= nums[slow]:
                fast += 1
            else:
                slow += 1
                nums[slow], nums[fast] = nums[fast], nums[slow]

        return slow + 1
