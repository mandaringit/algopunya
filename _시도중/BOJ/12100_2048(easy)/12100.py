# import sys
#
# sys.stdin = open('input.txt', 'r')
#
#
# def move(board):
#     global N
#
#     # left
#     for i in range(N):
#         line = [0] * N
#         board_line = board[i]
#         line_idx = 0
#         for number in board_line:
#
#             if number > 0:
#                 if number == line[line_idx]:
#                     line[line_idx] = number * 2
#                     line_idx += 1
#                 else:
#                     line[line_idx] = number
#                     line_idx += 1
#
#         for i in range(N):
#             board[i] = line[i]
#
#     return board
#
#     # right
#
#     # down
#
#     # top
#
#
# N = int(input())
#
# board = [list(map(int, input().split())) for _ in range(N)]
# print(move(board))
