import sys

sys.stdin = open('input.txt', 'r')


def DFS(N, land, rain_h):
    copy_land = [[0] * N for _ in range(N)]

    land_count = 0

    for i in range(N):
        for j in range(N):

            if land[i][j] > rain_h and copy_land[i][j] == 0:
                land_count += 1
                stack = [[i, j]]
                copy_land[i][j] = land_count

                while stack:
                    m, k = stack.pop()

                    d = [(1, 0), (-1, 0), (0, -1), (0, 1)]

                    for dx, dy in d:
                        ni = m + dx
                        nj = k + dy

                        if 0 <= ni < N and 0 <= nj < N:
                            if land[ni][nj] > rain_h and copy_land[ni][nj] == 0:
                                copy_land[ni][nj] = copy_land[i][j]
                                stack.append([ni, nj])
    return land_count


N = int(input())

land = [list(map(int, input().split())) for _ in range(N)]

min_h = 101
max_h = 0

for i in range(N):
    for j in range(N):
        if land[i][j] > max_h:
            max_h = land[i][j]
        if land[i][j] < min_h:
            min_h = land[i][j]

max_safe_land = 1  # 적어도 하나가 잠기는 아래 시도가 모두 0일 경우, 아무것도 잠기지 않는 상황을 고려

# 최소 시작은 가장 작은 수부터, 최대는 모두 잠기기 이전까지만.
for rain_h in range(min_h, max_h):
    safe_land_count = DFS(N, land, rain_h)
    if safe_land_count > max_safe_land:
        max_safe_land = safe_land_count

print(max_safe_land)
