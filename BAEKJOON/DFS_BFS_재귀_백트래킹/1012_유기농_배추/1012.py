import sys

sys.stdin = open('input.txt', 'r')


def BFS(i, j, land, row, col, larva):
    q = [[i, j]]

    visited = []

    while q:

        k, m = q.pop(0)

        if [k, m] not in visited:
            visited.append([k, m])
            land[k][m] = larva

            d = [(1, 0), (-1, 0), (0, 1), (0, -1)]

            for dx, dy in d:

                ni = k + dx
                nj = m + dy

                if 0 <= ni < row and 0 <= nj < col:
                    if land[ni][nj] == '1':
                        q.append([ni, nj])
    return land


T = int(input())

for tc in range(1, T + 1):
    M, N, K = map(int, input().split())

    land = [[0] * M for _ in range(N)]
    larva = 0

    for _ in range(K):
        col, row = map(int, input().split())

        land[row][col] = "1"

    for i in range(N):
        for j in range(M):
            if land[i][j] == '1':
                larva += 1
                BFS(i, j, land, N, M, larva)

    print(larva)
