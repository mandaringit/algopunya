from typing import List


class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:

        N = len(A) - 1
        right = N
        for left in range(N):
            if A[left] % 2:  # 홀수면
                # 짝수가 나올때까지
                while left < right and A[right] % 2 == 1:
                    right -= 1

                if A[right] % 2 == 0:
                    A[left], A[right] = A[right], A[left]

        return A


sol = Solution()
sol.sortArrayByParity([3, 1, 2, 4])
