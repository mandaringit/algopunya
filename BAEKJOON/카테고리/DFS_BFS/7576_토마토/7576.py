# 시간초과
# list.pop(0), list.index, list.insert, list.count, x in list, list[:-1] 등은 다 O(N)입니다.
# list를 큐로 사용하면 절대, 절대, 절대, 절대, 절대 안 됩니다!! 큐는 반드시 collections.deque를 써야 합니다.

# 그래도시간초과낭 ㅠ

import sys

sys.stdin = open('input.txt', 'r')

from collections import deque


def BFS(i, j, box, row, col, fake_box, cnt):
    q = deque()
    q.append([i, j])

    visited = []

    fake_box[i][j] = 0
    while q:
        m, k = q.popleft()

        if [m, k] not in visited:
            visited.append([m, k])

            d = [(-1, 0), (1, 0), (0, -1), (0, 1)]

            for dx, dy in d:

                ni = m + dx
                nj = k + dy

                if 0 <= ni < row and 0 <= nj < col:
                    if box[ni][nj] == 0:
                        if cnt == 0 and fake_box[ni][nj] == -2:
                            q.append([ni, nj])
                            fake_box[ni][nj] = fake_box[m][k] + 1

                        else:
                            if fake_box[ni][nj] > fake_box[m][k] + 1:
                                q.append([ni, nj])
                                fake_box[ni][nj] = fake_box[m][k] + 1

    return fake_box


def welldone_tomato(N, M, box, fake_box):
    cnt = 0
    for i in range(N):
        for j in range(M):

            if box[i][j] == 1:
                BFS(i, j, box, N, M, fake_box, cnt)
                cnt += 1
            elif box[i][j] == -1:
                fake_box[i][j] = -1

    max_day = -1

    for row in fake_box:

        if -2 in row:
            return -1

        value = max(row)

        if value > max_day:
            max_day = value

    return max_day


M, N = map(int, input().split())

box = [list(map(int, input().split())) for _ in range(N)]
fake_box = [[-2] * M for _ in range(N)]
print(welldone_tomato(N, M, box, fake_box))
