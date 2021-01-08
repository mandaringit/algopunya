class Solution:
    def countBits(self, num: int) -> List[int]:
        result = []

        for i in range(0, num + 1):
            count = 0
            while i != 0:
                if i & 1 == 1:
                    count += 1
                i = i >> 1

            result.append(count)

        return result

    def countBits(self, num: int) -> List[int]:
        dp = [0]*(num+1)

        for i in range(1, num + 1):
            quotient, remainder = divmod(i, 2)
            dp[i] = dp[quotient] + remainder

        return dp
