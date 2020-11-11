function minPathSum(grid: number[][]): number {
  const M = grid.length;
  const N = grid[0].length;
  const dp = Array.from(Array(M + 1), () =>
    new Array(N + 1).fill(Number.POSITIVE_INFINITY)
  );

  for (let i = 1; i < M + 1; i++) {
    for (let j = 1; j < N + 1; j++) {
      if (i === 1 && j === 1) {
        dp[i][j] = grid[0][0];
      } else {
        dp[i][j] = grid[i - 1][j - 1] + Math.min(dp[i - 1][j], dp[i][j - 1]);
      }
    }
  }

  return dp[M][N];
}
