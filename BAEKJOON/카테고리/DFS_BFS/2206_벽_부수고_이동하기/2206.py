import sys

sys.stdin = open('input.txt', 'r')


def explore(i, j, crash, count):
    global maze
    global visited
    global goal
    global min_root
    global N
    global M

    d = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    # 목적지면 리턴.

    if [i, j] == goal and count < min_root:
        min_root = count
    elif count < min_root:
        visited[i][j] = '1'

        for dx, dy in d:
            ni = i + dx
            nj = j + dy

            if 0 <= ni < N and 0 <= nj < M:

                if maze[ni][nj] == '0' and visited[ni][nj] == '0':
                    explore(ni, nj, crash, count + 1)
                    print(visited)

                elif crash and maze[ni][nj] == '1' and visited[ni][nj] == '0':
                    origin = maze[ni][nj]
                    maze[ni][nj] = '0'
                    explore(ni, nj, 0, count + 1)
                    maze[ni][nj] = origin

        visited[i][j] = '0'


N, M = map(int, input().split())

maze = [list(input()) for _ in range(N)]
visited = [['0'] * M for _ in range(N)]

start = [0, 0]
goal = [N - 1, M - 1]

min_root = N * M + 1

explore(0, 0, 1, 1)

if min_root == N * M + 1:
    print(-1)
else:
    print(min_root)
