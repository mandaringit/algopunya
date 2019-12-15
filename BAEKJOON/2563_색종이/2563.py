import sys

sys.stdin = open('input.txt', 'r')

N = int(input())
papers = [[0] * 100 for _ in range(100)]

cnt = 0
for _ in range(N):
    x, y = map(int, input().split())

    x2, y2 = x + 10, y + 10

    for i in range(x, x2):
        for j in range(y, y2):
            if papers[i][j] == 0:
                papers[i][j] = 1
                cnt += 1
print(cnt)
