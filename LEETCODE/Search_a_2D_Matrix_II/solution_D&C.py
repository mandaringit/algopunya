class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        # M = len(matrix)
        # N = len(matrix[0])
        # if M == 0 or N == 0:
        #     return False

        # def search(lt, rb):
        #     i1, j1 = lt
        #     i2, j2 = rb

        #     i = (i1 + i2) // 2
        #     j = (j1 + j2) // 2

        #     if matrix[i][j] == target:
        #         return True
        #     elif matrix[i][j] < target:  # 왼쪽 위 버림
        #         return search((i1, j + 1), (i, j2)) or search((i + 1, j1), (i2, j)) or search((i + 1, j + 1), (i2, j2))
        #     else:
        #         return search((i1, j1), (i, j)) or search((i1, j), (i, j2)) or search((i, j1), (i2, j))

        return search((0, 0), (M - 1, N - 1))


sol = Solution()
print(sol.searchMatrix(
    [[1, 4, 7, 11, 15], [2, 5, 8, 12, 19], [3, 6, 9, 16, 22],
        [10, 13, 14, 17, 24], [18, 21, 23, 26, 30]],
    5))
print(sol.searchMatrix(
    [[1, 4, 7, 11, 15], [2, 5, 8, 12, 19], [3, 6, 9, 16, 22],
        [10, 13, 14, 17, 24], [18, 21, 23, 26, 30]],
    30))
