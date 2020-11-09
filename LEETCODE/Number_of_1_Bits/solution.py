class Solution:
    def hammingWeight(self, n: int) -> int:
        return bin(n).count("1")

    def hammingWeight2(self, n: int) -> int:
        count = 0

        while n != 0:
            n &= n-1
            count += 1

        return count
