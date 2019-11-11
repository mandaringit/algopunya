import sys

sys.stdin = open('input.txt', 'r')

# 시간 초과 => pop(0) 의 비효율때문임


def BFS(startq):
    global maps
    global W, H
    global visited

    d = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    sg_count = 1

    while startq:
        i, j, value = startq.pop(0)

        if value == '*':
            for dx, dy in d:
                ni = i + dx
                nj = j + dy

                if 0 <= ni < H and 0 <= nj < W:
                    if maps[ni][nj] in ['@', '.']:
                        maps[ni][nj] = '*'
                        startq.append((ni, nj, '*'))

        elif value == '@':
            sg_count -= 1
            for dx, dy in d:
                ni = i + dx
                nj = j + dy

                if 0 <= ni < H and 0 <= nj < W:
                    if maps[ni][nj] == '.':
                        maps[ni][nj] = '@'
                        visited[ni][nj] = visited[i][j] + 1
                        startq.append((ni, nj, '@'))
                        sg_count += 1
                else:
                    return visited[i][j]

        if sg_count == 0:
            return 'IMPOSSIBLE'

    return 'IMPOSSIBLE'


T = int(input())

for tc in range(1, T + 1):
    W, H = map(int, input().split())

    visited = [[0] * W for _ in range(H)]
    maps = [list(input()) for _ in range(H)]

    SGs = []
    fires = []

    for i in range(H):
        for j in range(W):
            if maps[i][j] == '@':
                SGs.append((i, j, '@'))
                visited[i][j] = 1

            if maps[i][j] == '*':
                fires.append((i, j, '*'))

    startq = fires + SGs
    print(BFS(startq))
