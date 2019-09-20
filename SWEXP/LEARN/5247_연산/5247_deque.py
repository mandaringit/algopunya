import sys

sys.stdin = open('sample_input.txt', 'r')

from collections import deque


def BFS(start, goal):
    global visited
    q = deque([start])
    visited[start] = 0

    if start == goal:
        return visited[start]

    while q:
        x = q.popleft()

        for nx in [x + 1, x - 1, x * 2, x - 10]:
            if 0 < nx <= 1000000 and visited[nx] == -1:
                visited[nx] = visited[x] + 1

                if nx == goal:
                    return visited[nx]
                else:
                    q.append(nx)


T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    visited = [-1] * 1000001
    print("#{} {}".format(tc, BFS(N, M)))
