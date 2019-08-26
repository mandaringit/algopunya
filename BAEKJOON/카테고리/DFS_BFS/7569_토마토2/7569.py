import sys
import pprint

sys.stdin = open('input.txt', 'r')

from collections import deque


def BFS(q, M, N, H, baked_tomato, box, copy_box):
    max_day = 0
    while q:
        floor, i, j = q.popleft()

        max_day = copy_box[floor][i][j]

        d = [(0, 0, -1), (0, 0, 1), (0, 1, 0), (0, -1, 0), (1, 0, 0), (-1, 0, 0)]

        for df, dx, dy in d:
            nfloor = floor + df
            ni = i + dx
            nj = j + dy

            if 0 <= nfloor < H and 0 <= ni < N and 0 <= nj < M:
                if box[nfloor][ni][nj] == 0 and copy_box[nfloor][ni][nj] == 0:
                    q.append([nfloor, ni, nj])
                    baked_tomato += 1
                    copy_box[nfloor][ni][nj] = copy_box[floor][i][j] + 1

    return max_day, baked_tomato


# M은 상자의 가로 칸수, N은 상자의 세로 칸수  H는 상자의 층 수
M, N, H = map(int, input().split())

box = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]
copy_box = [[[0] * M for _ in range(N)] for _ in range(H)]

baked_tomato = 0
empty = 0

q = deque()

for floor in range(H):
    for i in range(N):
        for j in range(M):

            if box[floor][i][j] == 1:
                q.append([floor, i, j])
                baked_tomato += 1
            elif box[floor][i][j] == -1:
                empty += 1

if baked_tomato + empty == N * M * H:
    print(0)
else:
    max_day, baked_tomato = BFS(q, M, N, H, baked_tomato, box, copy_box)

    if baked_tomato + empty != N * M * H:
        print(-1)
    else:
        print(max_day)
