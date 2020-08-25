# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        l, r = 1, n

        while l <= r:
            mid = (l+r) // 2
            result = guess(mid)  # 이미 사이트 내부에 정의되어 있는 API임

            if result == 0:
                return mid
            elif result == 1:  # higer
                l = mid + 1
            elif result == -1:  # lower
                r = mid - 1
