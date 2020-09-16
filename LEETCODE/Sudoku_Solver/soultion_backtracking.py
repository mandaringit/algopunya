from typing import List


class Solution:
    """
    Do not return anything, modify board in-place instead.
    """

    def solveSudoku(self, board: List[List[str]]) -> None:
        self.board = board
        self.solve()

    def find_empty(self):
        for row in range(9):
            for col in range(9):
                if self.board[row][col] == '.':
                    return row, col
        return -1, -1

    def solve(self):
        row, col = self.find_empty()

        # 종료
        if (row, col) == (-1, -1):
            return True

        for num in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            if self.is_valid(row, col, num):  # 가로, 세로 , 해당 row, col이 속한 사각 박스에 존재 가능한가 ?
                self.board[row][col] = num  # 표시하고
                if self.solve():  # 다음으로 넘어감 -> 넘어간 단계에서 False 리턴시 이전 단계로 복귀.
                    return True  # 모두 풀리면 return True
                self.board[row][col] = '.'

        return False

    def is_valid(self, row, col, num):
        box_row = row - row % 3
        box_col = col - col % 3
        if self.check_row(row, num) and self.check_col(col, num) and self.check_box(box_row, box_col, num):
            return True
        return False

    def check_row(self, row, num):
        for col in range(9):
            if self.board[row][col] == num:
                return False
        return True

    def check_col(self, col, num):
        for row in range(9):
            if self.board[row][col] == num:
                return False
        return True

    def check_box(self, box_row, box_col, num):
        for i in range(3):
            for j in range(3):
                if self.board[box_row + i][box_col + j] == num:
                    return False
        return True


sol = Solution()
sol.solveSudoku([
    ["5", "3", ".", ".", "7", ".", ".", ".", "."],
    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    [".", "9", "8", ".", ".", ".", ".", "6", "."],
    ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", "6", ".", ".", ".", ".", "2", "8", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    [".", ".", ".", ".", "8", ".", ".", "7", "9"]
])
