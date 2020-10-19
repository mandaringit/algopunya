class Solution:
    def projectionArea(self, grid: List[List[int]]) -> int:
        N = len(grid)

        xy = 0
        for i in range(N):
            for j in range(N):
                if grid[i][j] > 0:
                    xy += 1

        xz = 0
        for row in grid:
            xz += max(row)

        yz = 0
        for col in zip(*grid):
            yz += max(col)

        return xy + xz + yz
