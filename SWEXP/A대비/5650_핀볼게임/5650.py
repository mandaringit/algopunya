import sys

sys.stdin = open('sample_input.txt', 'r')


class PinBall:

    def __init__(self, i, j, direction, N, board):
        self.i = i
        self.j = j
        self.direction = direction
        self.N = N
        self.score = 0
        self.board = board
        self.start = (i, j)

    def whats_next(self):
        prev_i = self.i
        prev_j = self.j

        self.move()

        # 이동 후 벽이 아닐때
        if 0 <= self.i < self.N and 0 <= self.j < self.N:
            now_value = self.board[self.i][self.j]

            if (self.i, self.j) == self.start or now_value == -1:
                return 'end'
            elif isinstance(now_value, Block):
                now_value.change_pinball_direction(self)
                self.score += 1
            elif isinstance(now_value, WormHole):
                now_value.warp_pinball(self)

        else:  # 벽일때 위치 원상복구
            self.score += 1  # 벽에 부딪힐때 점수 +

            self.i = prev_i
            self.j = prev_j

            if (self.i, self.j) == self.start:
                return 'end'

            if self.direction in [0, 2]:
                self.direction += 1
            else:
                self.direction -= 1

            now_value = self.board[self.i][self.j]

            if (self.i, self.j) == self.start or now_value == -1:
                return 'end'
            elif isinstance(now_value, Block):
                now_value.change_pinball_direction(self)
                self.score += 1
            elif isinstance(now_value, WormHole):
                now_value.warp_pinball(self)

    def move(self):

        if self.direction == 0:  # 상
            self.i -= 1
        elif self.direction == 1:  # 하
            self.i += 1
        elif self.direction == 2:  # 좌
            self.j -= 1
        elif self.direction == 3:  # 우
            self.j += 1


class Block:

    def __init__(self, i, j, number):
        self.number = number
        self.i = i
        self.j = j

    def change_pinball_direction(self, pinball):
        d = pinball.direction

        if d == 1:  # 위에서 온놈
            if self.number == 1:
                pinball.direction = 3
            elif self.number == 2:
                pinball.direction = 0
            elif self.number == 3:
                pinball.direction = 0
            elif self.number == 4:
                pinball.direction = 2
            elif self.number == 5:
                pinball.direction = 0

        elif d == 0:  # 아래에서 온놈
            if self.number == 1:
                pinball.direction = 1
            elif self.number == 2:
                pinball.direction = 3
            elif self.number == 3:
                pinball.direction = 2
            elif self.number == 4:
                pinball.direction = 1
            elif self.number == 5:
                pinball.direction = 1

        elif d == 3:  # 왼쪽에서 온놈
            if self.number == 1:
                pinball.direction = 2
            elif self.number == 2:
                pinball.direction = 2
            elif self.number == 3:
                pinball.direction = 1
            elif self.number == 4:
                pinball.direction = 0
            elif self.number == 5:
                pinball.direction = 2

        elif d == 2:  # 오른쪽에서 온놈
            if self.number == 1:
                pinball.direction = 0
            elif self.number == 2:
                pinball.direction = 1
            elif self.number == 3:
                pinball.direction = 3
            elif self.number == 4:
                pinball.direction = 3
            elif self.number == 5:
                pinball.direction = 3


class WormHole:

    def __init__(self, i, j):
        self.i = i
        self.j = j
        self.pair = None

    def warp_pinball(self, pinball):
        pinball.i = self.pair.i
        pinball.j = self.pair.j


T = int(input())

for tc in range(1, T + 1):
    N = int(input())

    board = [list(map(int, input().split())) for _ in range(N)]

    start_points = []
    wormholes = {}

    for i in range(N):
        for j in range(N):
            value = board[i][j]
            if value == 0:
                start_points.append((i, j))
            elif 0 < value <= 5:
                board[i][j] = Block(i, j, board[i][j])
            elif 5 < value <= 10:
                board[i][j] = WormHole(i, j)
                if value in wormholes:
                    wormholes[value].append(board[i][j])
                else:
                    wormholes[value] = [board[i][j]]

    # 웜홀 페어 만들어주기
    for hole1, hole2 in wormholes.values():
        hole1.pair = hole2
        hole2.pair = hole1

    max_score = 0

    for x, y in start_points:

        for i in range(4):
            pinball = PinBall(x, y, i, N, board)
            while True:

                value = pinball.whats_next()
                if value == 'end':
                    if pinball.score > max_score:
                        max_score = pinball.score
                    break

    print("#{} {}".format(tc, max_score))
