# 입력 : 격자판 행의수 N, 열의 수 M , 궁수의 공격 거리 제한 D,
# 둘째줄부터 격자판의 상태 (0)은 빈칸, (1)은 적
# 출력 : 궁수의 공격으로 제거할 수 있는 적의 최대 수

import sys

sys.stdin = open('input.txt', 'r')


def BFS(i, j):
    global D
    q = [(i, j)]
    visited = [(i, j)]
    while q:
        i_, j_ = q.pop(0)

        d = [(0, -1), (-1, 0), (0, 1)]  # 좌 상 우 순
        for dx, dy in d:
            ni = i_ + dx
            nj = j_ + dy

            if 0 <= ni < N and 0 <= nj < M:
                if (ni, nj) not in visited:
                    diff = abs(ni - i) + abs(nj - j)
                    if diff < D:
                        visited.append((ni, nj))
                        q.append((ni, nj))
                    elif diff == D:
                        visited.append((ni, nj))
    return visited[1:]


class Archer:

    def __init__(self, i, j):
        self.i = i
        self.j = j
        self.shoot_ranges = BFS(i, j)

    def shoot(self, board):

        for i, j in self.shoot_ranges:
            value = board[i][j]
            if isinstance(value, Enemy) and not value.is_dead:
                value.hit()
                break

        return board


class Enemy:

    def __init__(self, i, j):
        self.i = i
        self.j = j
        self.is_dead = False

    def hit(self):
        self.is_dead = True

    def move(self, board):
        board[self.i][self.j] = 0  # 현재 위치 바꾸기
        if not self.is_dead:
            if 0 <= self.i + 1 < N:
                self.i += 1
                board[self.i][self.j] = self

        return board


def Defence(a1, a2, a3):
    global enemy_locs
    global N
    global maxV

    maps = [[0] * M for _ in range(N)]
    enemies = []
    for x, y in enemy_locs:
        e = Enemy(x, y)
        maps[x][y] = e
        enemies.append(e)

    for _ in range(N):
        a1.shoot(maps)
        a2.shoot(maps)
        a3.shoot(maps)

        for e in enemies:
            if not e.is_dead:
                e.move(maps)

    cnt = 0
    for e in enemies:
        if e.is_dead:
            cnt += 1

    if cnt > maxV:
        maxV = cnt


N, M, D = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]
# 적들의 위치
enemy_locs = []
for i in range(N):
    for j in range(M):
        if grid[i][j] == 1:
            enemy_locs.append((i, j))

maxV = 0
# 1. 궁수의 배치 경우의 수
for i in range(M - 2):
    for j in range(i + 1, M - 1):
        for k in range(j + 1, M):
            archer1 = Archer(N, i)
            archer2 = Archer(N, j)
            archer3 = Archer(N, k)
            Defence(archer1, archer2, archer3)

print(maxV)
