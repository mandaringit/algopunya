class Solution:
    def reverse(self, x: int) -> int:
        number = int(str(abs(x))[::-1])
        number = number if x > 0 else -number

        return number if -(2**31) <= number < 2**31 else 0
