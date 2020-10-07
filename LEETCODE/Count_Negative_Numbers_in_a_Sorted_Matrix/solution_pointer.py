class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        M = len(grid)
        N = len(grid[0])
        count = 0
        i = M - 1
        j = 0
        while i >= 0 and j <= N-1:
            value = grid[i][j]

            if value < 0:
                count += N - j
                i -= 1
            else:
                j += 1

        return count
