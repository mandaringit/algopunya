import sys

sys.stdin = open('input.txt', 'r')

N = int(input())
papers = [[0] * 100 for _ in range(100)]

colored = []
for _ in range(N):
    x, y = map(int, input().split())

    x2, y2 = x + 10, y + 10

    for i in range(x, x2):
        for j in range(y, y2):
            if papers[i][j] == 0:
                papers[i][j] = 1
                colored.append((i, j))

length = 0
for i, j in colored:
    d = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    for di, dj in d:
        ni = i + di
        nj = j + dj

        if 0 <= ni < 100 and 0 <= nj < 100:
            if papers[ni][nj] == 0:
                length += 1
        else:
            length += 1
print(length)
