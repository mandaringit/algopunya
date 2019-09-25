import sys
import pprint

sys.stdin = open('test_input.txt', 'r')


# 시작 위치, 지금까지 사용한 방향
def cafe_tour(i, j, s_i, s_j, direction_idx, path, values, total):
    global visited
    global cafes
    global N
    global maxV
    global maxPath

    # 우하, 좌하, 좌상, 우상 순서로 0 1 2 3
    d = [(1, 1), (1, -1), (-1, -1), (-1, 1)]

    now_cafe = cafes[i][j]
    now_values = values
    visited[i][j] = 1
    if len(path) > 3 and [i, j] == [s_i + 1, s_j - 1]:
        if maxV < total:
            maxV = total
            maxPath = len(path)
            # print(path)
            # pprint.pprint(visited, indent=4, width=100)

    else:
        if direction_idx == 0:
            next_direction = [0, 1]

        elif direction_idx == 1:
            next_direction = [1, 2]

        elif direction_idx == 2:
            next_direction = [2, 3]

        elif direction_idx == 3:
            next_direction = [3]

        for d_idx in next_direction:
            dx, dy = d[d_idx]

            ni = i + dx
            nj = j + dy

            # 인덱스 범위 안인가?
            if 0 <= ni < N and 0 <= nj < N:
                if visited[ni][nj] != 1 and cafes[ni][nj] not in values:
                    cafe_tour(ni, nj, s_i, s_j, d_idx, path + [[ni, nj]], values + [cafes[ni][nj]],
                              total + cafes[ni][nj])

    visited[i][j] = 0


T = int(input())

for tc in range(1, T + 1):
    N = int(input())

    cafes = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0] * N for _ in range(N)]
    maxV = 0
    maxPath = 0

    for i in range(N - 1):
        for j in range(1, N - 1):
            # 4방향 제외
            cafe_tour(i, j, i, j, 0, [[i, j]], [cafes[i][j]], cafes[i][j])

    if maxPath == 0:
        maxPath = -1

    print("#{} {}".format(tc, maxPath))
