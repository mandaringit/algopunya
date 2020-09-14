class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """

        i = len(matrix) - 1
        j = 0
        while i >= 0 and j <= len(matrix[0]) - 1:
            value = matrix[i][j]
            if value == target:
                return True
            elif value < target:
                j += 1
            else:
                i -= 1

        return False
