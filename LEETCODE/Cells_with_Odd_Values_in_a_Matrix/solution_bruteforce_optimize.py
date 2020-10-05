class Solution:
    def oddCells(self, n: int, m: int, indices: List[List[int]]) -> int:

        row = [0] * n
        col = [0] * m

        for ri, ci in indices:
            row[ri] += 1
            col[ci] += 1

        count = 0
        for i in range(n):
            for j in range(m):
                if (row[i] + col[j]) % 2:
                    count += 1

        return count
