import sys

sys.stdin = open('input.txt', 'r')

# 6% 시간초과

R, C = map(int, input().split())
lake = [list(input()) for _ in range(R)]

ices = set()
swans = []
for i in range(R):
    for j in range(C):
        if lake[i][j] == 'X':
            ices.add((i, j))

        if lake[i][j] == 'L':
            swans.append((i, j))

d = [(0, 1), (0, -1), (1, 0), (-1, 0)]
day = 0

stack = [swans[0]]
visited = [[0] * C for _ in range(R)]
while True:
    day += 1

    # find melting ice today.
    melting_ices = set()
    for i, j in ices:
        for dx, dy in d:
            ni = i + dx
            nj = j + dy

            if 0 <= ni < R and 0 <= nj < C:
                if lake[ni][nj] in ['.', 'L']:
                    melting_ices.add((i, j))
                    break

    # melting ice in the lake
    for i, j in melting_ices:
        lake[i][j] = '.'

    # next ices = now ices - melting ices
    ices -= melting_ices
    next_start = []

    escape = False

    while stack:
        i, j = stack.pop()
        visited[i][j] = day

        is_next_start = False
        for dx, dy in d:
            ni = i + dx
            nj = j + dy

            if 0 <= ni < R and 0 <= nj < C:

                if (ni, nj) == swans[1]:
                    escape = True
                else:
                    if visited[ni][nj] == 0 and lake[ni][nj] == '.':
                        visited[ni][nj] = day
                        stack.append((ni, nj))

                    if lake[ni][nj] == 'X':
                        is_next_start = True

        if is_next_start:
            next_start.append((i, j))

    stack = next_start

    if escape:
        break

print(day)
