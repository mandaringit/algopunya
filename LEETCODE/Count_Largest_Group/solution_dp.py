class Solution:
    def countLargestGroup(self, n: int) -> int:
        dp = {0: 0}
        counts = [0] * ((9*4) + 1)  # 10^4이므로 최대 큰 합은 9999가 최대.
        for num in range(1, n+1):
            quotient, remainder = divmod(num, 10)
            dp[num] = remainder + dp[quotient]
            counts[dp[num]] += 1

        return counts.count(max(counts))
