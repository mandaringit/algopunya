import sys

sys.stdin = open('sample_input.txt', 'r')


def BFS(start, goal):
    global visited
    q = [0] * 1000000  # 노드 길이가 최대 100만까지이므로
    front = -1
    end = -1

    end += 1
    q[end] = start
    visited[start] = 0

    if start == goal:
        return visited[start]

    while front != end:
        front += 1
        x = q[front]

        for nx in [x + 1, x - 1, x * 2, x - 10]:
            if 0 < nx <= 1000000 and visited[nx] == -1:
                visited[nx] = visited[x] + 1

                if nx == goal:
                    return visited[nx]
                else:
                    end += 1
                    q[end] = nx


T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    visited = [-1] * 1000001
    print("#{} {}".format(tc, BFS(N, M)))
