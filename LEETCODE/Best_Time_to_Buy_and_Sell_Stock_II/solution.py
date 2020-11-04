class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        N = len(prices)

        if N <= 1:
            return 0

        profit = 0
        for day in range(1, N):
            profit += max(0, prices[day] - prices[day - 1])

        return profit
