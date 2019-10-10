import sys

sys.stdin = open('sample_input.txt', 'r')

from copy import deepcopy


def DFS(i, j, maps):
    global N, W, H
    new_maps = deepcopy(maps)
    stack = [(i, j)]

    while stack:
        i_, j_ = stack.pop()
        value = new_maps[i_][j_]
        boom_range = value - 1
        new_maps[i_][j_] = 0  # change self value

        for mul in range(1, boom_range + 1):
            for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                ni = i_ + mul * dx
                nj = j_ + mul * dy

                if 0 <= ni < H and 0 <= nj < W:

                    if new_maps[ni][nj] == 1:  # if value == 1 , just change value
                        new_maps[ni][nj] = 0
                    elif new_maps[ni][nj] >= 2:  # if value gte 2, append stack
                        stack.append((ni, nj))

    return new_maps


def clear(col, maps):
    global H
    copy_col = ['0'] * H

    for i in range(H):
        copy_col[i] = str(maps[i][col])

    copy_col = ''.join(copy_col)
    copy_col = copy_col.replace('0', '')
    padding = H - len(copy_col)
    copy_col = '0' * padding + copy_col

    for i in range(H):
        maps[i][col] = int(copy_col[i])


def shoot_and_boom(col, count, maps):
    global N, W, H
    global min_brick
    # 1. start => [0][col] and find it's value gte 1 while row ++
    row = 0
    while row < H:
        value = maps[row][col]

        # 2. if value gte 1 => start DFS and change it's value to 0
        if value >= 1:
            new_maps = DFS(row, col, maps)
            break
        row += 1

    count += 1
    if count == N:
        if row == H:
            new_maps = deepcopy(maps)
        # brick count compare
        brick = 0
        for k in range(H):
            for m in range(W):
                if new_maps[k][m] >= 1:
                    brick += 1

        if brick < min_brick:
            min_brick = brick

    else:
        if row == H:  # no change
            new_maps = deepcopy(maps)
        else:
            # 3. if DFS done, clear all col
            for i in range(W):
                clear(i, new_maps)

        # 4. play next stage. or if shooting == N: break or all brick were gone: break
        for next_col in range(W):
            shoot_and_boom(next_col, count, new_maps)


T = int(input())

for tc in range(1, T + 1):
    N, W, H = map(int, input().split())
    maps = [list(map(int, input().split())) for _ in range(H)]
    min_brick = W * H
    for i in range(W):
        shoot_and_boom(i, 0, maps)

    print("#{} {}".format(tc, min_brick))
