function countBits(num: number): number[] {
  const dp = Array(num + 1).fill(0);

  for (let i = 1; i <= num; i++) {
    const q = Math.trunc(i / 2);
    const r = i % 2;
    dp[i] = dp[q] + r;
  }

  return dp;
}
