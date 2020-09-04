class Solution:
    def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:

        N = len(matrix)
        M = 0 if N == 0 else len(matrix[0])

        traverses = []
        # 시작점 -> (0,j)
        for col in range(M):
            line = []
            i, j = 0, col
            while 0 <= i < N and 0 <= j < M:
                line.append(matrix[i][j])
                i += 1
                j -= 1
            traverses.append(line)

        # 시작점 -> (i, M - 1)
        for row in range(1, N):
            line = []
            i, j = row, M - 1
            while 0 <= i < N and 0 <= j < M:
                line.append(matrix[i][j])
                i += 1
                j -= 1
            traverses.append(line)

        result = []
        for i, line in enumerate(traverses):
            if not i % 2:
                result += reversed(line)
            else:
                result += line

        return result
