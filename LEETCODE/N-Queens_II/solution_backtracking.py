class Solution:
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """

        diag1 = set()
        diag2 = set()
        usedCols = set()

        return self.helper(n, diag1, diag2, usedCols, 0)

    def helper(self, n, diag1, diag2, usedCols, row):
        if row == n:
            return 1

        solutions = 0

        for col in range(n):
            if row + col in diag1 or row - col in diag2 or col in usedCols:  # 이미 사용중인 장소라면 패
                continue

            # row, col에 퀸을 두면서 앞으로 두면 안되는 장소 마킹
            diag1.add(row + col)  # 대각선 /
            diag2.add(row - col)  # 대각선 \
            usedCols.add(col)

            # 다음 row로 넘어감
            solutions += self.helper(n, diag1, diag2, usedCols, row + 1)

            # 마킹한곳 지우기
            diag1.remove(row + col)
            diag2.remove(row - col)
            usedCols.remove(col)

        return solutions


sol = Solution()
sol.totalNQueens(5)
