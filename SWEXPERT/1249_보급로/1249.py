import sys

sys.stdin = open('input.txt', 'r')


# from collections import deque
#
#
# def bfs(i, j):
#     global check, arr, n
#
#     queue = deque([])
#     queue.append([i, j])
#     check[i][j] = arr[i][j]
#
#     while queue:
#         i, j = queue.popleft()
#         for x, y in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
#             ni = i + x
#             nj = j + y
#             if ni >= 0 and ni < n and nj >= 0 and nj < n:
#                 temp = check[i][j] + arr[ni][nj]
#                 if temp < check[ni][nj]:
#                     check[ni][nj] = temp
#                     queue.append([ni, nj])
#
#
# for t in range(int(input())):
#     n = int(input())
#     arr = [list(map(int, input())) for _ in range(n)]
#     check = [[9 * n * n] * n for _ in range(n)]
#
#     bfs(0, 0)
#     print('#{} {}'.format(t + 1, check[n - 1][n - 1]))

def f(i, j, total):
    global land
    global goal
    global visited
    global N
    global minV

    d = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    visited[i][j] = 1

    if [i, j] == goal:
        if total < minV:
            minV = total
    else:
        if total < minV:

            for dx, dy in d:
                ni = i + dx
                nj = j + dy

                if 0 <= ni < N and 0 <= nj < N and not visited[ni][nj]:
                    f(ni, nj, total + land[ni][nj])

    visited[i][j] = 0


T = int(input())

for tc in range(1, T + 1):
    N = int(input())

    land = [list(map(int, list(input()))) for _ in range(N)]
    visited = [[0] * N for _ in range(N)]
    start = [0, 0]
    goal = [N - 1, N - 1]
    minV = 999
    f(0, 0, 0)

    print(minV)
