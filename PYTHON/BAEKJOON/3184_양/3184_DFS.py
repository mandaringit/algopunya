import sys

sys.stdin = open('input.txt', 'r')

def DFS(i, j):
    global visited, farm, all_sheep, all_wolf
    global N, M
    d = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    stack = [[i, j]]
    visited[i][j] = 1

    wolf = 0
    sheep = 0

    while stack:
        i_, j_ = stack.pop()

        if farm[i_][j_] == 'o':
            sheep += 1
        elif farm[i_][j_] == 'v':
            wolf += 1

        for dx, dy in d:
            ni = i_+dx
            nj = j_+dy

            if 0 <= ni < N and 0 <= nj < M:
                if not visited[ni][nj] and farm[ni][nj] != '#':
                    visited[ni][nj] = 1
                    stack.append([ni, nj])

    if wolf < sheep:
        all_sheep += sheep
    else:
        all_wolf += wolf

N, M = map(int, input().split())
farm = [list(input()) for _ in range(N)]
visited = [[0]*M for _ in range(N)]

all_sheep = 0
all_wolf = 0
for i in range(N):
    for j in range(M):
        if visited[i][j] == 0 and farm[i][j] in ['v', 'o']:
            DFS(i, j)

print(all_sheep, all_wolf)
