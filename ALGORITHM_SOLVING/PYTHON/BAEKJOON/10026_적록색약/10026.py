import sys

sys.stdin = open('input.txt', 'r')

from collections import deque


def BFS_ordinary(i, j, count):
    global visited_for_ordinary
    global N
    global picture

    q = deque()
    q.append([i, j])
    color = picture[i][j]
    visited_for_ordinary[i][j] = count

    while q:
        i_, j_ = q.popleft()

        d = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        for dx, dy in d:
            ni = i_ + dx
            nj = j_ + dy

            if 0 <= ni < N and 0 <= nj < N:
                # 같은 색이고, 아직 방문 안한곳이면
                if picture[ni][nj] == color and visited_for_ordinary[ni][nj] == 0:
                    visited_for_ordinary[ni][nj] = count  # 구역번호 주고 방문 표시
                    q.append([ni, nj])


def BFS_color_error(i, j, count):
    global visited_for_color_error
    global N
    global picture

    q = deque()
    q.append([i, j])
    color = picture[i][j]
    visited_for_color_error[i][j] = count

    while q:
        i_, j_ = q.popleft()

        d = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        for dx, dy in d:
            ni = i_ + dx
            nj = j_ + dy

            if 0 <= ni < N and 0 <= nj < N:
                # 아직 방문 안한곳이고,
                if visited_for_color_error[ni][nj] == 0:
                    if color == 'R' or color == 'G':
                        if picture[ni][nj] in ['R', 'G']:
                            visited_for_color_error[ni][nj] = count  # 구역번호 주고 방문 표시
                            q.append([ni, nj])
                    else:
                        if picture[ni][nj] == color:
                            visited_for_color_error[ni][nj] = count  # 구역번호 주고 방문 표시
                            q.append([ni, nj])


N = int(input())

picture = [list(input()) for _ in range(N)]
visited_for_ordinary = [[0] * N for _ in range(N)]
visited_for_color_error = [[0] * N for _ in range(N)]

ordinary_count = 0
error_count = 0
for i in range(N):
    for j in range(N):

        if visited_for_ordinary[i][j] == 0:
            ordinary_count += 1
            BFS_ordinary(i, j, ordinary_count)

        if visited_for_color_error[i][j] == 0:
            error_count += 1
            BFS_color_error(i, j, error_count)

print(ordinary_count, error_count)
