class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:

        N = len(A)
        result = []
        for i in range(N):
            flipped = []
            for j in range(N-1, -1, -1):
                flip = 1 if A[i][j] == 0 else 0
                flipped.append(flip)
            result.append(flipped)

        return result


""" 축약가능
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        N = len(A)
        return [[A[i][j] ^ 1 for j in range(N-1, -1, -1)] for i in range(N)]
"""
