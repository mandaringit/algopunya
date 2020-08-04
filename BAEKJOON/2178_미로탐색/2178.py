import sys

sys.stdin = open('input.txt', 'r')


def BFS(start, goal, maze, N, M):
    q = [start]

    fake_maze = [[0] * M for _ in range(N)]
    visited = []
    fake_maze[start[0]][start[1]] = 1

    while q:
        i, j = q.pop(0)

        if [i, j] not in visited and fake_maze[i][j] != 0:
            visited.append([i, j])

            if [i, j] == goal:
                return fake_maze[goal[0]][goal[1]]

            d = [(1, 0), (-1, 0), (0, -1), (0, 1)]

            for dx, dy in d:

                ni = i + dx
                nj = j + dy

                if 0 <= ni < N and 0 <= nj < M:
                    if maze[ni][nj] == '1' and fake_maze[ni][nj] == 0:
                        q.append([ni, nj])
                        fake_maze[ni][nj] = fake_maze[i][j] + 1

    return None


N, M = map(int, input().split())

start = [0, 0]
goal = [N - 1, M - 1]

maze = [list(input()) for _ in range(N)]

print(BFS(start, goal, maze, N, M))
