class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:

        R = len(grid)
        C = len(grid[0])

        d = [(0, -1), (-1, 0)]

        perimeter = 0

        for i in range(R):
            for j in range(C):
                if grid[i][j] == 1:
                    perimeter += 4

                    for dx, dy in d:
                        ni = i + dx
                        nj = j + dy

                        if 0 <= ni < R and 0 <= nj < C:
                            if grid[ni][nj] == 1:
                                perimeter -= 2

        return perimeter
