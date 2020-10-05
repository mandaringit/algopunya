class Solution:
    def oddCells(self, n: int, m: int, indices: List[List[int]]) -> int:

        matrix = [[0]*m for _ in range(n)]

        for ri, ci in indices:
            # row
            for i in range(n):
                matrix[i][ci] += 1
            # col
            for i in range(m):
                matrix[ri][i] += 1
        result = 0

        for i in range(n):
            for j in range(m):
                if matrix[i][j] % 2:
                    result += 1

        return result
