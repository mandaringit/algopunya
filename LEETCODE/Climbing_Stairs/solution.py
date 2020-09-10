class Solution:
    cache = {}

    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        elif n == 2:
            return 2
        elif n in Solution.cache:
            return Solution.cache[n]
        else:
            value = self.climbStairs(n-1) + self.climbStairs(n-2)
            Solution.cache[n] = value
            return value
