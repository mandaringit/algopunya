import sys

sys.stdin = open('sample_input.txt', 'r')

# 기본적으로, 모든위치에서 방범 서비스를 시작 할 수 있다고 생각해야한다. N*N
# 그리고 각 집들까지의 거리를 구해 거리들을 카운팅한다.
# 최대 가능한 거리는 2*N 이다.
# K = 1 ~ 2*N 까지 카운팅된 집 수를 보면서 비용 비교를해가며 가장 많은 집을 커버 가능한곳을 찾는다.

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())  # map 크기, 지불 가격
    maps = [list(map(int, input().split())) for _ in range(N)]

    # 기본적인 집들의 위치
    homes = []
    for i in range(N):
        for j in range(N):
            if maps[i][j] == 1:
                homes.append((i, j))

    max_home = 0
    for x1 in range(N):
        for y1 in range(N):
            # 기준점에서 각 집들까지의 거리를 구해 카운팅해 배열에 저장.
            distances = [0] * 2 * N
            for x2, y2 in homes:
                d = abs(x2 - x1) + abs(y2 - y1)
                distances[d] += 1

            # 코스트 비교
            for k in range(1, 2 * N + 1):
                cost = k * k + (k - 1) * (k - 1)
                home_count = sum(distances[:k])
                margin = home_count * M - cost
                if margin >= 0 and home_count > max_home:
                    max_home = home_count

    print(f"#{tc} {max_home}")
