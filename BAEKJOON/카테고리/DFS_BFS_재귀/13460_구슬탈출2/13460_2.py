import sys

sys.stdin = open('input.txt', 'r')


class Ball:

    def __init__(self, i, j):
        self.i = i
        self.j = j
        self.pair = None
        self.state = 'stop'

    def is_wall_or_ball(self, ni, nj):
        global board

        value = board[ni][nj]
        if value == '#':
            return True
        elif self.pair.i == ni and self.pair.j == nj and not self.pair.state == 'goal':  # 자신의 페어가 '골'상태인 경우 무시한다.
            return True
        return False

    def move(self, direction):
        global board

        d = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # 상 하 좌 우

        dx = d[direction][0]
        dy = d[direction][1]

        i = self.i
        j = self.j

        # 다음 좌표
        ni = i + dx
        nj = j + dy

        if board[ni][nj] == 'O':  # 골일땐 상태를 골로 바꾼다
            self.state = 'goal'

        elif not self.is_wall_or_ball(ni, nj):  # 벽이 아니면 자신의 위치를 해당 위치로 변경한다
            self.i = ni
            self.j = nj

        else:  # 벽 또는 다른 공이 있으면 상태를 멈춤으로 바꾼다.
            self.state = 'stop'


def who_first_move(who, red, blue, direction):  # 누가 먼저 움직이는지, 움직일 빨간공인스턴스,파란공 인스턴스, 움직일 방향
    red.state = 'move'
    blue.state = 'move'

    while True:  # 두 공의 상태가 모두 'stop' 또는 'goal'의 상태에 있을때까지 순서대로 움직인다
        if who == 'blue':
            if blue.state == 'move':
                blue.move(direction)
            if red.state == 'move':
                red.move(direction)

        elif who == 'red':
            if red.state == 'move':
                red.move(direction)
            if blue.state == 'move':
                blue.move(direction)

        if red.state in ['stop', 'goal'] and blue.state in ['stop', 'goal']:
            break


def BFS(red_start, blue_start):
    # 큐의 시작은 [첫 시작 위치의 빨간공 인스턴스, 첫 시작 위치의 파란공 인스턴스, 지금까지 기울인 방향들, 직전에 쓴 방향]
    q = [[red_start, blue_start, [], set()]]

    while q:
        prev_red, prev_blue, moving, prev = q.pop(0)
        if moving[-3:] not in [[0, 1, 0], [1, 0, 1], [2, 3, 2], [3, 2, 3]]:  # 지금까지 기울인 방향이 제자리로 돌아오는 경우는 제외한다 (예로 상 하 상)

            for direction in {0, 1, 2, 3} - prev:  # 다음에 기울일 방향은 직전에 기울인 방향을 뺀 나머지 방향이다.
                # 주소 복사를 방지하기 위해 움직이기 전 위치의 각 객체들을 생성
                red = Ball(prev_red.i, prev_red.j)
                blue = Ball(prev_blue.i, prev_blue.j)
                red.pair = blue
                blue.pair = red

                if direction == 0:  # 위로 기울기 - > i 작은놈 먼저 움직임
                    if red.i > blue.i:
                        who_first_move('blue', red, blue, direction)  # 파란거 먼저 움직이기
                    else:
                        who_first_move('red', red, blue, direction)  # 빨간거 먼저 움직이기
                elif direction == 1:  # 아래로 기울기 -> i 큰놈 먼저 움직임
                    if red.i > blue.i:
                        who_first_move('red', red, blue, direction)
                    else:
                        who_first_move('blue', red, blue, direction)
                elif direction == 2:  # 왼쪽으로 기울기 -> j 작은놈 먼저 움직임
                    if red.j > blue.j:
                        who_first_move('blue', red, blue, direction)
                    else:
                        who_first_move('red', red, blue, direction)
                elif direction == 3:  # 오른쪽으로 기울기 -> j 큰놈 먼저 움직임
                    if red.j > blue.j:
                        who_first_move('red', red, blue, direction)
                    else:
                        who_first_move('blue', red, blue, direction)

                # 아래부터는 해당하는 방향으로 구슬이 모두 옮겨진 이후 ..
                next_moving = moving + [direction]

                if red.state == 'goal' and blue.state == 'goal':
                    pass
                elif blue.state == 'goal':
                    pass
                elif red.state == 'goal':
                    return len(next_moving)
                elif len(next_moving) < 10:
                    q.append([red, blue, next_moving, {direction}])

    return -1


# import timeit
# start = timeit.default_timer()

N, M = map(int, input().split())
board = [list(input()) for _ in range(N)]

# 공의 초기 위치 찾기
for i in range(N):
    for j in range(M):
        if board[i][j] == 'R':
            red_ball = Ball(i, j)
        elif board[i][j] == 'B':
            blue_ball = Ball(i, j)

# 각 공들의 쌍 이뤄주기
red_ball.pair = blue_ball
blue_ball.pair = red_ball

# 탐색 시작
print(BFS(red_ball, blue_ball))

# end = timeit.default_timer()
# print("{}ms".format((end - start) * 1000))
