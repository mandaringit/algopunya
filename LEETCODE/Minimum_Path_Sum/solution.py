class Solution(object):
    # 새로 dp 배열을 만들어 그리는 방법
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        M = len(grid)
        N = len(grid[0])
        dp = [[float('inf')]*(N+1) for _ in range(M+1)]

        for i in range(1, M+1):
            for j in range(1, N+1):
                if i == 1 and j == 1:
                    dp[i][j] = grid[0][0]
                else:
                    dp[i][j] = grid[i-1][j-1] + min(dp[i-1][j], dp[i][j-1])

        return dp[M][N]

    # 원본에 그리는 방법
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        M = len(grid)
        N = len(grid[0])

        for i in range(M):
            for j in range(N):
                if i == 0 and j == 0:
                    pass
                elif i == 0:
                    grid[i][j] = grid[i][j] + grid[i][j-1]
                elif j == 0:
                    grid[i][j] = grid[i][j] + grid[i-1][j]
                else:
                    grid[i][j] = grid[i][j] + min(grid[i-1][j], grid[i][j-1])

        return grid[M-1][N-1]
