import sys

sys.stdin = open('sample_input.txt', 'r')
from queue import PriorityQueue

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    lands = [list(map(int, input().split())) for _ in range(N)]

    # 초기 방문(출발점) 표시
    visited = [[0] * N for _ in range(N)]
    visited[0][0] = 1

    # 초기 거리 표시
    D = [[1001] * N for _ in range(N)]
    D[0][0] = 0

    # 우선순위 큐를 구현하면 좋다
    pri_q = PriorityQueue()

    # 시작점 주변 표시
    for dx, dy in [(0, 1), (1, 0)]:
        if 0 <= dx < N and 0 <= dy < N:
            now_h = lands[0][0]
            next_h = lands[dx][dy]
            fuel = 1
            if now_h < next_h:
                fuel += next_h - now_h
            D[dx][dy] = fuel
            pri_q.put((D[dx][dy], (dx, dy)))

    while visited[N - 1][N - 1] != 1:
        # 아직 방문하지 않은 곳들 중, 연료 사용량이 가장 적은곳을 찾는다.
        mi, mj = pri_q.get()[1]

        visited[mi][mj] = 1  # 방문 표시
        # 연료 사용량이 가장 적은곳에서 인접한 곳들 중,
        d = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        for dx, dy in d:
            ni = mi + dx
            nj = mj + dy
            if 0 <= ni < N and 0 <= nj < N:
                if visited[ni][nj] == 0:  # 아직 방문하지 않은 곳들을 확인
                    now_h = lands[mi][mj]
                    next_h = lands[ni][nj]
                    fuel = 1  # 기본 사용량
                    if now_h < next_h:
                        fuel += next_h - now_h
                    D[ni][nj] = min(D[ni][nj], D[mi][mj] + fuel)
                    pri_q.put((D[ni][nj], (ni, nj)))

        if D[N - 1][N - 1] != 1001:
            break

    print("#{} {}".format(tc, D[N - 1][N - 1]))
