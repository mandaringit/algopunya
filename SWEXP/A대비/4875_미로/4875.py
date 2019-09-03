import sys

sys.stdin = open('sample_input.txt')


def explore(i, j, count):
    global visited
    global N
    global goal
    global minV

    if [i, j] == goal:
        if minV > count:
            minV = count
    else:
        visited[i][j] = 1
        d = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        for dx, dy in d:
            ni = i + dx
            nj = j + dy

            if 0 <= ni < N and 0 <= nj < N:
                if maze[ni][nj] != 1 and visited[ni][nj] == 0:
                    explore(ni, nj, count + 1)
        visited[i][j] = 0

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    maze = [list(map(int, list(input()))) for _ in range(N)]
    visited = [[0] * N for _ in range(N)]

    start = [0, 0]
    goal = [0, 0]
    minV = N * N

    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                start = [i, j]
            elif maze[i][j] == 3:
                goal = [i, j]

    explore(start[0], start[1], 1)
    print(minV)
