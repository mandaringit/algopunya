class Solution:
    cache = {}

    def fib(self, N: int) -> int:
        if N <= 1:
            return N
        elif N in Solution.cache:
            return Solution.cache[N]
        else:
            value = self.fib(N-1) + self.fib(N-2)
            Solution.cache[N] = value
            return value
