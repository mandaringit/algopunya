function longestCommonSubsequence(text1: string, text2: string): number {
  const N = text1.length;
  const M = text2.length;
  const dp = Array.from(Array(N + 1), () => new Array(M + 1).fill(0));

  for (let i = 1; i < N + 1; i++) {
    for (let j = 1; j < M + 1; j++) {
      if (text1[i - 1] === text2[j - 1]) {
        dp[i][j] = dp[i - 1][j - 1] + 1;
      } else {
        dp[i][j] = dp[i - 1][j] > dp[i][j - 1] ? dp[i - 1][j] : dp[i][j - 1];
      }
    }
  }

  return dp[N][M];
}
