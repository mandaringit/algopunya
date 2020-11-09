class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) <= 1:
            return 0

        max_profit = 0
        min_price = prices[0]
        for i in range(1, len(prices)):
            # 현재 수익의 최댓값 = 현재 파는 값 - 지금까지 나온 값 중 가장 싼값
            max_profit = max(max_profit, prices[i] - min_price)
            min_price = min(min_price, prices[i])

        return max_profit

    def maxProfitDP(self, prices: List[int]) -> int:
        if len(prices) <= 1:
            return 0

        dp = [0] * len(prices)
        min_price = prices[0]
        for i in range(1, len(prices)):
            # 오늘 얻을 수 있는 수익 =
            # max(어제 얻을 수 있던 최대 수익, 오늘 팔아서 생길 수 있는 수익)
            dp[i] = max(dp[i-1], prices[i] - min_price)
            min_price = min(min_price, prices[i])

        return dp[-1]
