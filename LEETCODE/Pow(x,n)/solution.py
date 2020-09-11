class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            n = -(n)
            x = 1 / x

        def helper(x, n):
            print(x, n)
            if n == 0:
                return 1
            elif n % 2:
                return x * helper(x * x, n // 2)
            else:
                return helper(x * x, n // 2)

        return helper(x, n)


sol = Solution()
sol.myPow(4, 5)
"""
x n
4 5
16 2
256 1
65536 0
"""