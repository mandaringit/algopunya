import sys

sys.stdin = open('input.txt', 'r')

from collections import deque


def BFS(startq):
    global maps
    global W, H
    global visited

    d = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    sg_count = 1

    while startq:
        i, j, value = startq.popleft()

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

    startq = deque(fires + SGs)
    print(f"#{tc} {BFS(startq)}")

# 1 1
# 2 IMPOSSIBLE
# 3 2
# 4 IMPOSSIBLE
# 5 6
# 6 5
# 7 IMPOSSIBLE
# 8 IMPOSSIBLE
# 9 28
# 10 IMPOSSIBLE
# 11 IMPOSSIBLE
# 12 IMPOSSIBLE
# 13 4
# 14 4
# 15 4
# 16 4
# 17 4
# 18 4
# 19 4
# 20 4
# 21 2
