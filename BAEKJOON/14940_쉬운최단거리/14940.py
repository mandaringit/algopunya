import sys

sys.stdin = open('input.txt', 'r')


def BFS(Q):
    global N, M, maps, visited
    x, y = Q[0]
    visited[x][y] = 0
    d = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    head = -1
    tail = 0

    while head != tail:
        head += 1
        i, j = Q[head]

        for dx, dy in d:
            ni = i + dx
            nj = j + dy

            if 0 <= ni < N and 0 <= nj < M:
                if visited[ni][nj] == -1 and maps[ni][nj] == 1:
                    visited[ni][nj] = visited[i][j] + 1
                    tail += 1
                    Q[tail] = [ni, nj]


N, M = map(int, input().split())

maps = [list(map(int, input().split())) for _ in range(N)]

Q = [0] * N * M
walls = []
for i in range(N):
    for j in range(M):
        if maps[i][j] == 2:
            Q[0] = [i, j]
        if maps[i][j] == 0:
            walls.append([i, j])

visited = [[-1] * M for _ in range(N)]
BFS(Q)

for i, j in walls:
    visited[i][j] = 0

for i in range(N):
    print(' '.join(map(str, visited[i])))
