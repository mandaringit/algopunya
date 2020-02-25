import sys

sys.stdin = open('input.txt', 'r')

from collections import deque


def bfs(i, j):
    global check, arr, n

    queue = deque([])
    queue.append([i, j])
    check[i][j] = arr[i][j]

    while queue:
        i, j = queue.popleft()
        for x, y in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
            ni = i + x
            nj = j + y
            if ni >= 0 and ni < n and nj >= 0 and nj < n:
                temp = check[i][j] + arr[ni][nj]
                if temp < check[ni][nj]:
                    check[ni][nj] = temp
                    queue.append([ni, nj])


for t in range(int(input())):
    n = int(input())
    arr = [list(map(int, input())) for _ in range(n)]
    check = [[9 * n * n] * n for _ in range(n)]

    bfs(0, 0)
    print('#{} {}'.format(t + 1, check[n - 1][n - 1]))
