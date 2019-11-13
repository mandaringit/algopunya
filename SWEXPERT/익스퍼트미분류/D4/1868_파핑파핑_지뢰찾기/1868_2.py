import sys

sys.stdin = open('input.txt', 'r')


def click(i, j):
    global maps, N, count
    # 8방향
    d = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, -1), (1, -1), (-1, 1)]

    after = []
    mine = 0
    for dx, dy in d:
        ni = i+dx
        nj = j+dy

        if 0 <= ni < N and 0 <= nj < N:
            map_value = maps[ni][nj]
            if map_value == '*':
                mine += 1
            elif map_value == '.':
                after.append([ni, nj])

    maps[i][j] = mine
    if not mine:
        for i_, j_ in after:
            click(i_, j_)


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    maps = [list(input()) for _ in range(N)]
    count = 0

    for i in range(N):
        for j in range(N):
            if maps[i][j] == '.':
                d = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, -1), (1, -1), (-1, 1)]

                mine = 0
                for dx, dy in d:
                    ni = i+dx
                    nj = j+dy
                    if 0 <= ni < N and 0 <= nj < N:
                        map_value = maps[ni][nj]
                        if map_value == '*':
                            mine += 1
                    if mine > 0:
                        break

                if not mine:
                    count += 1
                    click(i, j)

    for i in range(N):
        for j in range(N):
            if maps[i][j] == '.':
                count += 1

    print("#{} {}".format(tc, count))
