import sys

sys.stdin = open('input.txt', 'r')


def explore(i, j):
    global maze
    global visited
    global result

    visited[i][j] = 1

    if maze[i][j] == '3':
        result = 1
        return
    else:
        d = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        for dx, dy in d:
            ni = i + dx
            nj = j + dy

            if 0 <= ni < 16 and 0 <= nj < 16:
                if maze[ni][nj] != '1' and visited[ni][nj] == 0:
                    explore(ni, nj)

    visited[i][j] = 0


for _ in range(10):
    tc = int(input())

    maze = [list(input()) for _ in range(16)]
    visited = [[0] * 16 for _ in range(16)]

    result = 0
    explore(1, 1)

    print("#{} {}".format(tc, result))
