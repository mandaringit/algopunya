class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        summation = 0
        product = 1

        while n != 0:
            q, r = divmod(n, 10)
            summation += r
            product *= r
            n = q

        return product - summation
