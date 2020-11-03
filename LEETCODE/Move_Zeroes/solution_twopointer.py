class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        slow = 0  # 가장 앞쪽의 0의 인덱스를 가리킨다.
        for fast in range(len(nums)):

            # fast가 0이 아닐때만 가장 앞쪽의 0과 스왑한다.
            if nums[fast] != 0:
                nums[fast], nums[slow] = nums[slow], nums[fast]

            # 다음 slow를 찾아간다.
            if nums[slow] != 0:
                slow += 1
