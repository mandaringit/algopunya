class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        """
        :type n: int
        :rtype: List[str]
        """
        result = []
        b3 = 3
        b5 = 5
        b15 = 15

        for num in range(1, n+1):
            if num == b15:
                b3 += 3
                b5 += 5
                b15 += 15
                result.append("FizzBuzz")
            elif num == b3:
                b3 += 3
                result.append("Fizz")
            elif num == b5:
                b5 += 5
                result.append("Buzz")
            else:
                result.append(f"{num}")

        return result
