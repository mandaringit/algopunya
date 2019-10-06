import sys

sys.stdin = open('input.txt', 'r')


def BFS(i, j):
    global north_pole
    global removed_icebergs
    global N, M
    global visited

    visited[i][j] = 1
    q = [(i, j)]

    while q:

        i_, j_ = q.pop(0)

        d = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        for di, dj in d:
            ni = i_ + di
            nj = j_ + dj

            if 0 <= ni < N and 0 <= nj < M:
                if visited[ni][nj] == 0 and north_pole[ni][nj] > 0:
                    visited[ni][nj] = 1
                    q.append((ni, nj))


N, M = map(int, input().split())  # 행,렬
north_pole = [list(map(int, input().split())) for _ in range(N)]

icebergs = set()

for i in range(N):
    for j in range(M):
        if north_pole[i][j] > 0:
            icebergs.add((i, j))

year = 0
island_count = 0

while island_count < 2:
    year += 1

    # 일단 녹아서 없어지지 않는건 값을 변경시키고,
    # 녹는건 따로 모아놓는다.

    removed_icebergs = set()
    for i, j in icebergs:
        d = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        zero_count = 0
        for di, dj in d:
            ni = i + di
            nj = j + dj

            if 0 <= ni < N and 0 <= nj < M:
                if north_pole[ni][nj] == 0:
                    zero_count += 1

        last_iceberg = north_pole[i][j] - zero_count
        if last_iceberg <= 0:
            removed_icebergs.add((i, j))
        else:
            north_pole[i][j] = last_iceberg

    # 모두 모아서 한꺼번에 깎아야 한다. 위에서 미리 깎으면 영향을 받음.
    for k, m in removed_icebergs:
        north_pole[k][m] = 0

    # 살펴볼 빙산들 재조정
    icebergs = icebergs - removed_icebergs
    if icebergs:  # 빙산이 있으면
        # BFS
        count = 0
        visited = [[0] * M for _ in range(N)]
        for i, j in icebergs:
            if visited[i][j] == 0:
                count += 1
                BFS(i, j)

        island_count = count
    else:  # 빙산이 모두 녹으면
        year = 0
        break

print(year)  # 4
