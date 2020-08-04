import sys

sys.stdin = open('sample_input.txt', 'r')

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    maps = [list(map(int, input().split())) for _ in range(N)]

    homes = []
    for i in range(N):
        for j in range(N):
            if maps[i][j] == 1:
                homes.append((i, j))

    maxHome = 0
    for x in range(N):
        for y in range(N):
            distances = {}
            for x2, y2 in homes:
                distance = abs(x2 - x) + abs(y2 - y) + 1

                if distance in distances:
                    distances[distance] += 1
                else:
                    distances[distance] = 1

            home_total = 0
            for K in range(1, 2 * N + 1):
                if K in distances:
                    cost = K * K + (K - 1) * (K - 1)
                    home_total += distances[K]
                    margin = M * home_total - cost
                    if margin >= 0 and home_total > maxHome:
                        maxHome = home_total

    print(f"#{tc} {maxHome}")
