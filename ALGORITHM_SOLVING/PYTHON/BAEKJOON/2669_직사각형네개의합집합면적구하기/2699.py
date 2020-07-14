import sys

sys.stdin = open('input.txt', 'r')

grid = [[0] * 100 for _ in range(100)]
cnt = 0
for _ in range(4):
    x, y, x2, y2 = map(int, input().split())

    for i in range(x, x2):
        for j in range(y, y2):
            if grid[i][j] == 0:
                grid[i][j] = 1
                cnt += 1
print(cnt)
