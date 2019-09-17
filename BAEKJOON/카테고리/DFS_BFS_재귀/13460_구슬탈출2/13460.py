import sys

sys.stdin = open('input.txt', 'r')


class Ball:

    def __init__(self, i, j, color):
        self.i = i
        self.j = j
        self.color = color

    def is_wall_or_ball(self, ni, nj):
        global board

        value = board[ni][nj]
        if value == '#':
            return True
        elif self.color == 'R' and value == 'B':
            return True
        elif self.color == 'B' and value == 'R':
            return True

        return False

    def is_goal(self, ni, nj):
        global board

        return board[ni][nj] == '0'

    def move(self, direction):
        global board
        # 상 하 좌 우
        d = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        dx = d[direction][0]
        dy = d[direction][1]

        i = self.i
        j = self.j

        # 다음 좌표
        ni = i + dx
        nj = j + dy

        if self.is_goal(ni,nj):
            # 골일때

        elif not self.is_wall_or_ball(ni, nj):

#
#
# def blue_first(red, blue, direction):
#     red_move = True
#     blue_move = True
#
#     while True:
#         if blue_move:
#             blue_state = move(blue, direction)
#             if blue_state == 'goal':
#                 blue = 'goal'
#                 blue_move = False
#             elif blue_state:
#                 blue_move = False
#
#         if red_move:
#             red_state = move(red, direction)
#             if red_state == 'goal':
#                 red = 'goal'
#                 red_move = False
#             elif red_state:
#                 red_move = False
#
#         if not red_move and not blue_move:
#             break
#
#     return red, blue
#
#
# def red_first(red, blue, direction):
#     red_move = True
#     blue_move = True
#
#     while True:
#         if red_move:
#             red_state = move(red, direction)
#             if red_state == 'goal':
#                 red = 'goal'
#                 red_move = False
#             elif red_state:
#                 red_move = False
#
#         if blue_move:
#             blue_state = move(blue, direction)
#             if blue_state == 'goal':
#                 blue = 'goal'
#                 blue_move = False
#             elif blue_state:
#                 blue_move = False
#
#         if not red_move and not blue_move:
#             break
#
#     return red, blue
#
#
# def BFS(rb, bb, depth):
#     q = [[rb, bb, depth]]
#
#     while q:
#         red, blue, _depth = q.pop(0)
#
#         for direction in [0, 1, 2, 3]:
#             red_i = red[0]
#             red_j = red[1]
#             blue_i = blue[0]
#             blue_j = blue[1]
#
#             if direction == 0:  # 위로 기울기 - > i 작은놈 먼저 움직임
#                 if red_i > blue_i:
#                     # 파란거 먼저 움직이기
#                     blue_first(red, blue, direction)
#                 else:
#                     # 빨간거 먼저 움직이기
#                     red_first(red, blue, direction)
#
#             elif direction == 1:  # 아래로 기울기 -> i 큰놈 먼저 움직임
#                 if red_i > blue_i:
#                     red_first(red, blue, direction)
#                 else:
#                     blue_first(red, blue, direction)
#
#             elif direction == 2:  # 왼쪽으로 기울기 -> j 작은놈 먼저 움직임
#                 if red_j > blue_j:
#                     blue_first(red, blue, direction)
#                 else:
#                     red_first(red, blue, direction)
#             elif direction == 3:
#                 if red_j > blue_j:
#                     red_first(red, blue, direction)
#                 else:
#                     blue_first(red, blue, direction)
#
#             next_depth = _depth + 1
#
#             if red == 'goal' and blue == 'goal':
#                 return -1
#             elif blue == 'goal':
#                 return -1
#             elif red == 'goal':
#                 return next_depth
#
#             if next_depth <= 10:
#                 q.append([red, blue, next_depth])


N, M = map(int, input().split())

board = [list(input()) for _ in range(N)]

for i in range(N):
    for j in range(M):
        if board[i][j] == 'R':
            red_ball = [i, j, 'R']

        elif board[i][j] == 'B':
            blue_ball = [i, j, 'B']

BFS(red_ball, blue_ball, 0)
