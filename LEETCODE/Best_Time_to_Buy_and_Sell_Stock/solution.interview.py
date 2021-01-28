import sys


class Solution:
    # 브루트 포스. TLE
    def maxProfit(self, prices: List[int]) -> int:

        max_profit = 0
        for i in range(len(prices)-1):
            for j in range(i+1, len(prices)):
                if prices[j] - prices[i] > max_profit:
                    max_profit = prices[j] - prices[i]

        return max_profit

    def maxProfit(self, prices: List[int]) -> int:

        max_profit = 0
        min_price = sys.maxsize

        for price in prices:
            min_price = min(price, min_price)
            max_profit = max(max_profit, price - min_price)

        return max_profit
