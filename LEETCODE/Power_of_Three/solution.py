class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        return n > 0 and not pow(3, 20) % n
