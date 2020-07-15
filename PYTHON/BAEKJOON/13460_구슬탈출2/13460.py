import sys

sys.stdin = open('input.txt', 'r')


class Ball:

    def __init__(self, i, j, color):
        self.i = i
        self.j = j
        self.color = color
        self.pair = None
        self.state = 'stop'

    def is_wall_or_ball(self, ni, nj):
        global board

        value = board[ni][nj]
        if value == '#':
            return True

        elif self.pair.i == ni and self.pair.j == nj and not self.pair.state == 'goal':
            return True

        return False

    @staticmethod
    def is_goal(ni, nj):
        global board

        return board[ni][nj] == 'O'

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

        if self.is_goal(ni, nj):
            self.state = 'goal'

        elif not self.is_wall_or_ball(ni, nj):
            self.i = ni
            self.j = nj

        else:
            self.state = 'stop'


def blue_first(red, blue, direction):
    red.state = 'move'
    blue.state = 'move'

    while True:
        if blue.state == 'move':
            blue.move(direction)

        if red.state == 'move':
            red.move(direction)

        if red.state in ['stop', 'goal'] and blue.state in ['stop', 'goal']:
            break


def red_first(red, blue, direction):
    red.state = 'move'
    blue.state = 'move'

    while True:
        if red.state == 'move':
            red.move(direction)

        if blue.state == 'move':
            blue.move(direction)

        if red.state in ['stop', 'goal'] and blue.state in ['stop', 'goal']:
            break


def BFS(rb, bb):
    q = [[rb, bb, [], set()]]

    while q:
        red, blue, path, prev = q.pop(0)
        if path[-3:] not in [[0, 1, 0], [1, 0, 1], [2, 3, 2], [3, 2, 3]]:
            for direction in {0, 1, 2, 3} - prev:
                new_red = Ball(red.i, red.j, 'R')
                new_blue = Ball(blue.i, blue.j, 'B')
                new_red.pair = new_blue
                new_blue.pair = new_red

                if direction == 0:  # 위로 기울기 - > i 작은놈 먼저 움직임
                    if new_red.i > new_blue.i:
                        # 파란거 먼저 움직이기
                        blue_first(new_red, new_blue, direction)
                    else:
                        # 빨간거 먼저 움직이기
                        red_first(new_red, new_blue, direction)

                elif direction == 1:  # 아래로 기울기 -> i 큰놈 먼저 움직임
                    if new_red.i > new_blue.i:
                        red_first(new_red, new_blue, direction)
                    else:
                        blue_first(new_red, new_blue, direction)

                elif direction == 2:  # 왼쪽으로 기울기 -> j 작은놈 먼저 움직임
                    if new_red.j > new_blue.j:
                        blue_first(new_red, new_blue, direction)
                    else:
                        red_first(new_red, new_blue, direction)
                elif direction == 3:
                    if new_red.j > new_blue.j:
                        red_first(new_red, new_blue, direction)
                    else:
                        blue_first(new_red, new_blue, direction)

                next_path = path + [direction]

                if new_red.state == 'goal' and new_blue.state == 'goal':
                    pass
                elif new_blue.state == 'goal':
                    pass
                elif new_red.state == 'goal':
                    return len(next_path)
                elif len(next_path) < 10:
                    q.append([new_red, new_blue, next_path, {direction}])

    return -1


import timeit

start = timeit.default_timer()

N, M = map(int, input().split())

board = [list(input()) for _ in range(N)]

for i in range(N):
    for j in range(M):
        if board[i][j] == 'R':
            red_ball = Ball(i, j, 'R')

        elif board[i][j] == 'B':
            blue_ball = Ball(i, j, 'B')

red_ball.pair = blue_ball
blue_ball.pair = red_ball

print(BFS(red_ball, blue_ball))

end = timeit.default_timer()

print("{}ms".format((end - start) * 1000))
