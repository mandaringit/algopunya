import sys

sys.stdin = open('input.txt', 'r')


def DFS(x, y):
    global grid_paper
    global count

    stack = [[x, y]]
    grid_paper[x][y] = count

    while stack:
        i, j = stack.pop()

        d = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        for dx, dy in d:
            ni = i + dx
            nj = j + dy

            if 0 <= ni < M and 0 <= nj < N:
                if grid_paper[ni][nj] == 0:
                    grid_paper[ni][nj] = count
                    stack.append([ni, nj])


M, N, K = map(int, input().split())

grid_paper = [[0] * N for _ in range(M)]

for _ in range(K):
    x1, y1, x2, y2 = map(int, input().split())
    x2 -= 1
    y2 -= 1
    y1 = M - y1 - 1
    y2 = M - y2 - 1

    for i in range(y2, y1 + 1):
        for j in range(x1, x2 + 1):
            grid_paper[i][j] = 'b'

count = 0

for i in range(M):
    for j in range(N):
        if grid_paper[i][j] == 0:
            count += 1
            DFS(i, j)

width = [0] * (count + 1)

for row in grid_paper:

    for i in range(1, count + 1):
        c = row.count(i)

        width[i] += c

print(count)
print(' '.join(map(str, sorted(width[1:]))))
