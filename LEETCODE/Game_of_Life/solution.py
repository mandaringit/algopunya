class Solution:
    # 시간 복잡도 O(N *M) 공간 복잡도 O(N*M)
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        if not board:
            return

        d = [(-1, -1), (1, 1), (-1, 1), (1, -1),
             (0, 1), (1, 0), (-1, 0), (0, -1)]

        R = len(board)
        C = len(board[0])

        change_queue = []
        for i in range(R):
            for j in range(C):

                # get neighbors
                live_neighbors = 0
                for dx, dy in d:
                    ni = i + dx
                    nj = j + dy

                    if 0 <= ni < R and 0 <= nj < C:
                        if board[ni][nj] == 1:
                            live_neighbors += 1

                cell = board[i][j]
                if cell == 1:  # live
                    if live_neighbors <= 1 or live_neighbors >= 4:
                        change_queue.append([[i, j], 0])  # -> die
                else:  # dead
                    if live_neighbors == 3:
                        change_queue.append([[i, j], 1])  # -> live

        for coord, value in change_queue:
            i, j = coord
            board[i][j] = value
