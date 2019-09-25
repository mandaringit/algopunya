import sys

sys.stdin = open('sample_input.txt', 'r')

import math

INF = math.inf

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    lands = [list(map(int, input().split())) for _ in range(N)]

    # 초기 방문(출발점) 표시
    total_case = set()
    for i in range(N):
        for j in range(N):
            total_case.add((i, j))

    # 초기 거리 표시
    D = [[INF] * N for _ in range(N)]
    D[0][0] = 0

    # 시작점 주변 표시
    for dx, dy in [(0, 1), (1, 0)]:
        now_h = lands[0][0]
        next_h = lands[dx][dy]
        fuel = 1
        if now_h < next_h:
            fuel += next_h - now_h
        D[dx][dy] = fuel

    while total_case:
        # 아직 방문하지 않은 곳들 중, 연료 사용량이 가장 적은곳을 찾는다.
        mi = 0
        mj = 0
        min_usage = INF
        for i, j in total_case:
            fuel_usage = D[i][j]
            if fuel_usage <= min_usage:
                min_usage = fuel_usage
                mi, mj = i, j

        total_case -= {(mi, mj)}
        # 연료 사용량이 가장 적은곳에서 인접한 곳들 중,
        d = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        for dx, dy in d:
            ni = mi + dx
            nj = mj + dy
            if 0 <= ni < N and 0 <= nj < N:
                if len(total_case & {(ni, nj)}) == 1:  # 아직 방문하지 않은 곳들을 확인
                    now_h = lands[mi][mj]
                    next_h = lands[ni][nj]
                    fuel = 1  # 기본 사용량
                    if now_h < next_h:
                        fuel += next_h - now_h
                    D[ni][nj] = min(D[ni][nj], D[mi][mj] + fuel)

    print("#{} {}".format(tc, D[N - 1][N - 1]))
