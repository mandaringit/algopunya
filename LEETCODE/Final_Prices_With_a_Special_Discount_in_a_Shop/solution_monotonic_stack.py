from typing import List


class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:

        not_dc = []  # 할인이 안된 가격들의 인덱스를 보관할것임.

        for i, price in enumerate(prices):  # 전체 가격을 루프하면서
            # 이전에 할인이 안된 아이템이 있고
            # 그 아이템의 가격이 지금 나보다 큰 경우 (할인 가능한 경우)
            while not_dc and prices[not_dc[-1]] >= price:
                prices[not_dc.pop()] -= price  # 뽑아서 할인

            not_dc.append(i)  # 나를 할인이 안된 아이템의 리스트에 추가함
        return prices


sol = Solution()
sol.finalPrices([8, 4, 6, 2, 3])
