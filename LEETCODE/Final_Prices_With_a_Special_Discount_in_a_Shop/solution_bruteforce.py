class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:

        result = []
        N = len(prices)
        for i in range(N):
            discount = False
            for j in range(i+1, N):
                if prices[i] >= prices[j]:
                    discount = True
                    result.append(prices[i] - prices[j])
                    break

            if not discount:
                result.append(prices[i])

        return result
