# 입력 : N(크기), M: 남길 치킨집, N * N 이차원 배열 (0) 빈칸 (1) 집 (2) 치킨집
# 출력 : 최대 M개의 치킨집을 남길 수 있을때, 최소가 되는 치킨거리
# 접근 : 모든 집에 대해, 치킨집을 M개 이하 선택(조합)했을때 선택된 치킨집들과의 최소거리를 구하고 그에대한 합을 모두 비교.

import sys

sys.stdin = open('input.txt', 'r')

N, M = map(int, input().split())

maps = [list(map(int, input().split())) for _ in range(N)]

houses = []
chickens = []
for i in range(N):
    for j in range(N):
        if maps[i][j] == 1:
            houses.append((i, j))
        if maps[i][j] == 2:
            chickens.append((i, j))


minV = len(houses) * (2 * N)


for i in range(1, 1 << len(chickens)):
    ck_subset = []
    for j in range(len(chickens)):
        if i & (1 << j):
            ck_subset.append(chickens[j])

    # 치킨집을 M개 이하로 선택 가능한 경우일때만 검사
    if len(ck_subset) <= M:
        ck_distances = {}

        for i_, j_ in houses:
            min_d = 2 * N
            for x, y in ck_subset:
                diff = abs(x - i_) + abs(y - j_)
                if diff < min_d:
                    min_d = diff

            ck_distances[(i_, j_)] = min_d

        total = sum(ck_distances.values())
        if total < minV:
            minV = total

print(minV)
