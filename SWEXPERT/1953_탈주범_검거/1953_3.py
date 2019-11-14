import sys

sys.stdin = open('sample_input.txt', 'r')


# DFS로 하면 안된당~ 돌아서 겹치는 부분을 못간다~?

def BFS(r, c):
    global maps, pipe_types
    Q = [(r, c, 0)]  # i,j,time
    visited[r][c] = 1

    while Q:
        i, j, time = Q.pop(0)

        pipe_type = maps[i][j]
        type_value = pipe_types[pipe_type]['d']
        for idx, (dx, dy) in enumerate(type_value):
            ni = i+dx
            nj = j+dy

            if 0 <= ni < N and 0 <= nj < M:
                # 파이프가 있는 곳이고, 방문 안했으면
                next_type = maps[ni][nj]
                if maps[ni][nj] > 0 and not visited[ni][nj]:
                    if next_type in pipe_types[pipe_type]['matched'][idx] and time+1 < L:
                        Q.append((ni, nj, time+1))
                        visited[ni][nj] = 1


T = int(input())

for tc in range(1, T+1):
    N, M, R, C, L = map(int, input().split())  # 세로, 가로, 맨홀 세로, 가로, 소요시간
    maps = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0]*M for _ in range(N)]

    pipe_types = {
        1: {
            'd': [(-1, 0), (1, 0), (0, -1), (0, 1)],  # 상,하,좌,우
            'matched': [(1, 2, 5, 6), (1, 2, 4, 7), (1, 3, 4, 5), (1, 3, 6, 7)]
        },
        2: {
            'd': [(-1, 0), (1, 0)],  # 상,하
            'matched': [(1, 2, 5, 6), (1, 2, 4, 7)]
        },
        3: {
            'd': [(0, -1), (0, 1)],  # 좌,우
            'matched': [(1, 3, 4, 5), (1, 3, 6, 7)]
        },
        4: {
            'd': [(-1, 0), (0, 1)],  # 상,우
            'matched': [(1, 2, 5, 6), (1, 3, 6, 7)]
        },
        5: {
            'd': [(1, 0), (0, 1)],  # 하,우
            'matched': [(1, 2, 4, 7), (1, 3, 6, 7)]
        },
        6: {
            'd': [(1, 0), (0, -1)],  # 하, 좌
            'matched': [(1, 2, 4, 7), (1, 3, 4, 5)]
        },
        7: {
            'd': [(-1, 0), (0, -1)],  # 상,좌
            'matched': [(1, 2, 5, 6), (1, 3, 4, 5)]
        },
    }

    BFS(R, C)

    count = 0
    for i in range(N):
        for j in range(M):
            if visited[i][j] == 1:
                count += 1

    print("#{} {}".format(tc, count))
