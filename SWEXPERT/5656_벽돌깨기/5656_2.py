import sys

sys.stdin = open('sample_input.txt', 'r')

from copy import deepcopy


def clear_map(cmap):
    global W, H

    for j in range(W):
        new_col = []
        for i in range(H-1, -1, -1):
            if cmap[i][j] > 0:
                new_col.append(cmap[i][j])
                cmap[i][j] = 0

        clear_h = H-1
        while new_col:
            cmap[clear_h][j] = new_col.pop(0)
            clear_h -= 1


def boom(row, col, cmap):
    d = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    remove_after = [(row, col)]

    Stack = [(row, col)]

    while Stack:
        i, j = Stack.pop()
        boom_range = cmap[i][j]

        for dx, dy in d:
            for multiple in range(1, boom_range):
                ni = i+(multiple*dx)
                nj = j+(multiple*dy)

                if 0 <= ni < H and 0 <= nj < W:
                    if cmap[ni][nj] > 0 and (ni, nj) not in remove_after:
                        remove_after.append((ni, nj))
                        Stack.append((ni, nj))

    for i, j in remove_after:
        cmap[i][j] = 0


def shoot(col, cmap, count):  # col에 쏜다
    global N, W, H  # 제한횟수,너비,깊이
    global minBrick

    # 터뜨리고
    for row in range(H):
        if cmap[row][col] > 0:
            boom(row, col, cmap)
            break
    # 카운트 증가
    count += 1
    # 줄정리
    clear_map(cmap)

    # 부순 갯수 카운트
    if count == N:
        brick = 0
        for i in range(H):
            for j in range(W):
                if cmap[i][j] > 0:
                    brick += 1
        if brick < minBrick:
            minBrick = brick
    else:
        for next_col in range(W):
            new_cmap = deepcopy(cmap)
            shoot(next_col, new_cmap, count)


T = int(input())
for tc in range(1, T+1):
    N, W, H = map(int, input().split())
    maps = [list(map(int, input().split())) for _ in range(H)]

    minBrick = W*H
    for col in range(W):
        cmap = deepcopy(maps)
        shoot(col, cmap, 0)

    print("#{} {}".format(tc, minBrick))
