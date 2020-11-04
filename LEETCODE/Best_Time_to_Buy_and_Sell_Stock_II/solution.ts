function maxProfit(prices: number[]): number {
  if (prices.length <= 1) return 0;

  let profit = 0;
  for (let day = 0; day < prices.length; day++) {
    const p = prices[day] - prices[day - 1];
    if (p > 0) profit += p;
  }

  return profit;
}
