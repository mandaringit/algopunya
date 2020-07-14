import sys

sys.stdin = open('sample_input.txt', 'r')


def get_margin(i, j):
    global homes, N, M, maxHome
    distances = [0]*(2*N)  # 최대 거리는 대각선일때.
    for x, y in homes:
        d = abs(x-i)+abs(y-j)
        distances[d] += 1

    for d in range(2*N):
        k = d+1  # 거리가 0일때가 k = 1일때.
        city_count = sum(distances[:k])
        cost = k*k+(k-1)*(k-1)
        margin = (city_count*M)-cost
        if margin >= 0 and city_count > maxHome:
            maxHome = city_count


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    maps = [list(map(int, input().split())) for _ in range(N)]
    homes = []

    # 집찾기
    for i in range(N):
        for j in range(N):
            if maps[i][j] == 1:
                homes.append((i, j))

    maxHome = 0
    for i in range(N):
        for j in range(N):
            get_margin(i, j)

    print("#{} {}".format(tc, maxHome))
