class Solution:
    def hammingDistance(self, x: int, y: int) -> int:

        count = 0
        while x != 0 or y != 0:
            x, r1 = divmod(x, 2)
            y, r2 = divmod(y, 2)

            if r1 != r2:
                count += 1

        return count
