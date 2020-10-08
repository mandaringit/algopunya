class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:

        def is_sdn(num):
            n = num
            while n != 0:
                n, r = divmod(n, 10)  # r = digit

                if r == 0 or num % r != 0:
                    return False
            return True

        return [num for num in range(left, right + 1) if is_sdn(num)]
