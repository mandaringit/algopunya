class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:

        even = []
        odd = []
        for num in A:
            if num % 2:
                odd.append(num)
            else:
                even.append(num)

        return even + odd
