class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        N = len(board)

        def capture(i, j, d):
            dx, dy = d
            ni = i + dx
            nj = j + dy
            while 0 <= ni < N and 0 <= nj < N:
                if board[ni][nj] == 'p':
                    return True
                elif board[ni][nj] == 'B':
                    return False
                else:
                    ni += dx
                    nj += dy
            return False

        def find_rook(board):
            N = len(board)
            for i in range(N):
                for j in range(N):
                    if board[i][j] == 'R':
                        return i, j

        i, j = find_rook(board)
        count = 0
        for d in [(0, 1), (0, -1), (-1, 0), (1, 0)]:
            if capture(i, j, d):
                count += 1

        return count
