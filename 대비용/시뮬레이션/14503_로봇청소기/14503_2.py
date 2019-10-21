import sys

sys.stdin = open('input.txt', 'r')


class Robot:
    def __init__(self, r, c, d):
        self.i = r
        self.j = c
        self.d = d
        self.count = 0

    def clean(self):
        room[self.i][self.j] = 1
        self.count += 1

    def back(self):
        global direction

        origin_d = self.d
        back_d = [2, 3, 0, 1]

        ni = self.i + direction[back_d[origin_d]][0]
        nj = self.j + direction[back_d[origin_d]][1]

        return ni, nj

    def room_check(self, state):
        global room, N, M, visited

        if state == 'first':
            self.clean()

        next_d = [3, 0, 1, 2]
        search_d = self.d
        search_d = next_d[search_d]  # 왼쪽 방향

        count = 0
        while count != 4:
            count += 1
            ni = self.i + direction[search_d][0]
            nj = self.j + direction[search_d][1]

            if 0 <= ni < N and 0 <= nj < M and not room[ni][nj]:  # 벽아니고
                if room[ni][nj] == 0:  # 청소 안했으면
                    self.d = search_d
                    self.i = ni
                    self.j = nj
                    return 'first'

            search_d = next_d[search_d]  # 왼쪽 방향

        # 네방향 모두 청소 또는 벽이여서 아무것도 안했을때,
        ni, nj = self.back()
        if 0 <= ni < N and 0 <= nj < M and not room[ni][nj]:  # 후진한곳이 벽이 아니면
            self.i = ni
            self.j = nj
            return 'back'
        else:  # 후진도 못하면
            return 'stop'

    def work(self):
        state = 'first'
        while True:
            value = self.room_check(state)

            if value == 'stop':
                return
            elif value == 'back':
                state = 'back'
            elif value == 'first':
                state = 'first'


N, M = map(int, input().split())
r, c, d = map(int, input().split())

room = [list(map(int, input().split())) for _ in range(N)]
visited = [[0] * M for _ in range(N)]
direction = [(-1, 0), (0, 1), (1, 0), (0, -1)]
robot = Robot(r, c, d)

robot.work()
print(robot.count)
