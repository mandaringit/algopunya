import sys

sys.stdin = open('input.txt', 'r')

from collections import deque


def BFS(i, j):
    global goal
    global N
    global visited

    q = deque()
    q.append([i, j])
    visited[i][j] = 1

    if goal == [i, j]:
        return visited[i][j] - 1

    while q:
        i_, j_ = q.popleft()

        d = [(-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1)]

        for dx, dy in d:
            ni = i_ + dx
            nj = j_ + dy

            if 0 <= ni < N and 0 <= nj < N:
                if visited[ni][nj] == 0:
                    q.append([ni, nj])
                    visited[ni][nj] = visited[i_][j_] + 1

                    if goal == [ni, nj]:
                        return visited[ni][nj] - 1


T = int(input())

for _ in range(T):
    N = int(input())
    i, j = map(int, input().split())
    goal = list(map(int, input().split()))

    visited = [[0] * N for _ in range(N)]

    print(BFS(i, j))
