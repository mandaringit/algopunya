class Solution:
    def generateTheString(self, n: int) -> str:
        return 'a' * n if n % 2 else ('a' * 1)+('b' * (n-1))
