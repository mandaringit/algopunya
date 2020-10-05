class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        N = len(mat)

        # primary diagonal + secondary diagonal
        diagonal_sum = sum(mat[i][i] + mat[i][N-1-i] for i in range(N))

        # 홀수 갯수의 가운데 중복 제거
        if N % 2:
            mid = N // 2
            diagonal_sum -= mat[mid][mid]

        return diagonal_sum

    # def diagonalSum(self, mat: List[List[int]]) -> int:
    #     N = len(mat)
    #     diagonal_sum = 0

    #     for i in range(N):
    #         diagonal_sum += mat[i][i]  # primary diagonal
    #         diagonal_sum += mat[i][N-1-i]  # secondary diagonal

    #     # 홀
    #     if N % 2:
    #         mid = N // 2
    #         diagonal_sum -= mat[mid][mid]

    #     return diagonal_sum
