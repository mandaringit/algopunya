function maxProfit(prices: number[]): number {
  if (prices.length < 2) {
    return 0;
  }

  const dp = Array(prices.length).fill(0);
  let cheap = prices[0];
  for (let i = 1; i < prices.length; i++) {
    dp[i] = Math.max(dp[i - 1], prices[i] - cheap);
    cheap = Math.min(cheap, prices[i]);
  }

  return dp[prices.length - 1];
}
