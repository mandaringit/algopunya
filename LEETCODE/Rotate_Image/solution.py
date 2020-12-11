class Solution:
    # 시계방향
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        N = len(matrix)

        # 상하를 뒤집는다.
        for i in range(N // 2):
            for j in range(N):
                matrix[i][j], matrix[N-1-i][j] = matrix[N-1-i][j], matrix[i][j]

        # 대칭이동시킨다.
        for i in range(N):
            for j in range(N):
                if i > j:  # \ 축 대칭
                    matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # 반시계 방향
    def rotate2(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        N = len(matrix)

        # 좌우를 뒤집는다.
        for i in range(N):
            for j in range(N//2):
                matrix[i][j], matrix[i][N-1-j] = matrix[i][N-1-j], matrix[i][j]

        # 대칭이동시킨다.
        for i in range(N):
            for j in range(N):
                if i > j:  # \ 축 대칭
                    matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
