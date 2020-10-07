class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:

        M = len(grid)
        N = len(grid[0])
        visited = [[0]*N for _ in range(M)]
        d = [(0, -1), (-1, 0)]
        stack = [(M-1, N-1)]
        count = 0

        while stack:

            i, j = stack.pop()

            if grid[i][j] < 0:
                count += 1
                visited[i][j] = 1

                for dx, dy in d:
                    ni = i + dx
                    nj = j + dy

                    if ni >= 0 and nj >= 0 and not visited[ni][nj]:
                        stack.append((ni, nj))
        return count
