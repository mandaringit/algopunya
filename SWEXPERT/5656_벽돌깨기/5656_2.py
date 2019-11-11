# import sys
#
# sys.stdin = open('sample_input.txt', 'r')
#
# from copy import deepcopy
#
#
# def shoot(nw, n_count, maps):
#     global H, W, N, brick, minbrick
#     n_count += 1
#     boomed_map = maps
#     for h in range(H):
#         if maps[h][nw] > 0:
#             boomed_map = boom(h, nw, maps)
#             break
#
#     is_change, aligned_map = align(boomed_map)
#     if is_change and n_count < N:
#         for w in range(W):
#             n_maps = deepcopy(aligned_map)
#             shoot(w, n_count, n_maps)
#     elif n_count == N:
#         br = 0
#         for i in range(H):
#             for j in range(W):
#                 if aligned_map[i][j] > 0:
#                     br += 1
#         if br < minbrick:
#             minbrick = br
#     else:
#         return
#
#
# def align(boomed_map):
#     global H, W
#     is_change = False
#
#     for w in range(W):
#         line = [0] * H
#         idx = 0
#         for h in range(H):
#             value = boomed_map[h][w]
#             if value > 0:
#                 line[idx] = value
#                 idx += 1
#
#         for h in range(H):
#             if boomed_map[H - h - 1][w] != line[h]:
#                 is_change = True
#                 boomed_map[H - h - 1][w] = line[h]
#
#     return is_change, boomed_map
#
#
# def boom(i, j, maps):
#     global H, W
#     d = [(0, 1), (0, -1), (1, 0), (-1, 0)]
#
#     deletion = {(i, j)}
#     stack = [(i, j)]
#
#     while stack:
#         i_, j_ = stack.pop(0)
#         boom_range = maps[i_][j_]
#
#         if boom_range > 1:
#             for r in range(boom_range):
#                 for dx, dy in d:
#                     ni = i_ + (dx * r)
#                     nj = j_ + (dy * r)
#
#                     if 0 <= ni < H and 0 <= nj < W:
#                         if maps[ni][nj] > 0 and (ni, nj) not in deletion:
#                             deletion.add((ni, nj))
#                             stack.append((ni, nj))
#         else:
#             deletion.add((i_, j_))
#
#     for di, dj in deletion:
#         maps[di][dj] = 0
#
#     copy_map = deepcopy(maps)
#     return copy_map
#
#
# T = int(input())
# for tc in range(1, T + 1):
#     N, W, H = map(int, input().split())
#     maps = [list(map(int, input().split())) for _ in range(H)]
#     brick = 0
#     minbrick = brick
#     for i in range(H):
#         for j in range(W):
#             if maps[i][j] > 0:
#                 brick += 1
#
#     for w in range(W):
#         shoot(w, 0, maps)
#     print(minbrick)