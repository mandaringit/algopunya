class Solution:
    def sortArrayByParityII(self, A: List[int]) -> List[int]:

        N = len(A)
        even = 0
        odd = 1

        while even < N and odd < N:
            if A[even] % 2 == 1 and A[odd] % 2 == 0:
                A[even], A[odd] = A[odd], A[even]
                odd += 2
                even += 2
            else:
                if A[even] % 2 == 0:
                    even += 2
                if A[odd] % 2 == 1:
                    odd += 2

        return A
