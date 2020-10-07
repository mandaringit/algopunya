class Solution:
    def sumZero(self, n: int) -> List[int]:

        mid = n // 2

        result = []
        for num in range(-mid, mid+1, 1):
            if num == 0:
                if n % 2:
                    result.append(num)
            else:
                result.append(num)

        return result
