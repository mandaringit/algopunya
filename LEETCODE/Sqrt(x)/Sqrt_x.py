class Solution:
    def mySqrt(self, x: int) -> int:
        l, r = 0, x
        result = None
        while l <= r:
            mid = (l + r) // 2
            value = mid ** 2
            if value == x:
                return mid
            elif value > x:
                r = mid - 1
            elif value < x:
                result = mid
                l = mid + 1

        return result
