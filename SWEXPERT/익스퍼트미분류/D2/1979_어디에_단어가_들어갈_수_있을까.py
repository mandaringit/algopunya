# def check_row(N, K, board):
#     row_count = 0
#
#     for row in board:
#         count = 0
#         for idx, cell in enumerate(row):
#             if cell:
#                 count += 1
#                 if count == K:
#                     if idx == N - 1 or not row[idx + 1]:
#                         row_count += 1
#             else:
#                 count = 0
#     return row_count
#
#
# def check_column(N, K, board):
#     zip_column = list(zip(*board))  # 매우 혁신적이다.
#
#     return check_row(N, K, zip_column)
#
#
# T = int(input())
# result = []
#
# for t in range(1, T + 1):
#     N, K = map(int, input().split())
#
#     board = []
#     for _ in range(N):
#         board.append(list(map(int, input().split())))
#
#     row_count = check_row(N, K, board)
#     column_count = check_column(N, K, board)
#     result.append(f"#{t} {row_count + column_count}")
# print("\n".join(result))

import sys

sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T + 1):
    N, K = map(int, input().split())

    board = [list(map(int, input().split())) for _ in range(N)]
    result = 0

    # 가로로
    for i in range(N):
        cnt = 0
        for j in range(N):
            if board[i][j] == 1:
                cnt += 1
                if cnt == K:
                    # 옆에보고 가능한 경운지 확인 ?
                    if j + 1 < N:
                        if board[i][j + 1] == 0:
                            result += 1
                    else:
                        result += 1
            else:
                cnt = 0

    # 세로로
    col_board = list(zip(*board))
    for i in range(N):
        cnt2 = 0
        for j in range(N):
            if col_board[i][j] == 1:
                cnt2 += 1
                if cnt2 == K:
                    # 옆에보고 가능한 경운지 확인 ?
                    if j + 1 < N:
                        if col_board[i][j + 1] == 0:
                            result += 1
                    else:
                        result += 1
            else:
                cnt2 = 0
    print(result)
