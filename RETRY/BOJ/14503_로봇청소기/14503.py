import sys

sys.stdin = open('input.txt', 'r')


class Robot:
    d = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    def __init__(self, r, c, d):
        self.i = r
        self.j = c
        self.d = d
        self.count = 0

    def back(self):
        origin_d = self.d

        if origin_d == 0:
            back_d = 2
        elif origin_d == 1:
            back_d = 3
        elif origin_d == 2:
            back_d = 0
        elif origin_d == 3:
            back_d = 1

        ni = self.i + Robot.d[back_d][0]
        nj = self.j + Robot.d[back_d][1]

        return ni, nj

    def room_check(self, state):
        global room, N, M, visited

        if state == 'first':
            visited[self.i][self.j] = 1
            self.count += 1

        origin_d = self.d

        search_d = self.d
        if search_d == 0:
            search_d = 3
        elif search_d == 1:
            search_d = 0
        elif search_d == 2:
            search_d = 1
        elif search_d == 3:
            search_d = 2

        while search_d != origin_d:
            ni = self.i + Robot.d[search_d][0]
            nj = self.j + Robot.d[search_d][1]

            if 0 <= ni < N and 0 <= nj < M:  # 벽아니고
                if room[ni][nj] == 0 and visited[ni][nj] == 0:  # 벽이 아니고, 청소 안했으면
                    self.d = search_d
                    self.i = ni
                    self.j = nj
                    visited[ni][nj] = 1  # 방문 표시
                    self.count += 1
                    return 'first'
                else:
                    if search_d == 0:
                        search_d = 3
                    elif search_d == 1:
                        search_d = 0
                    elif search_d == 2:
                        search_d = 1
                    elif search_d == 3:
                        search_d = 2
            else:
                if search_d == 0:
                    search_d = 3
                elif search_d == 1:
                    search_d = 0
                elif search_d == 2:
                    search_d = 1
                elif search_d == 3:
                    search_d = 2

        # 네방향 모두 청소 또는 벽이여서 아무것도 안했을때,
        ni, nj = self.back()
        if 0 <= ni < N and 0 < nj < M:
            if room[ni][nj] == 0:
                self.i = ni
                self.j = nj
                return 'back'
            else:
                return 'stop'
        else:
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
robot = Robot(r, c, d)

robot.work()
print(robot.count)
