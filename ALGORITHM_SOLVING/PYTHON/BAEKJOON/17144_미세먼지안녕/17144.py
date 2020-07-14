import sys

sys.stdin = open('input.txt', 'r')

R, C, T = map(int, input().split())
area = [list(map(int, input().split())) for _ in range(R)]

dust = []
cleaner = []

for i in range(R):
    for j in range(C):
        if area[i][j] == -1:
            cleaner.append([i, j])
        else:
            dust.append([i, j])

d = [(0, 1), (0, -1), (1, 0), (-1, 0)]
sec = 0
while sec != T:
    # 시간 증가
    sec += 1

    # 1.미세먼지의 확산 - 현재 dust가 빌때까지 돈다
    diffusion_after_adding = {}
    while dust:
        i, j = dust.pop()
        diffusion_count = 0
        dust_amount = area[i][j]
        diffusion_amount = dust_amount // 5
        if diffusion_amount > 0:
            for dx, dy in d:
                ni = i + dx
                nj = j + dy

                if 0 <= ni < R and 0 <= nj < C:
                    if area[ni][nj] != -1:  # 공기청정기자리가 아닐때.
                        diffusion_count += 1  # 확산횟수 증가

                        # 동시에 발생. -> 나중에 끝나고 합산
                        if diffusion_after_adding.get((ni, nj)):
                            diffusion_after_adding[(ni, nj)] += diffusion_amount
                        else:
                            diffusion_after_adding[(ni, nj)] = diffusion_amount

            # 모두 확산 후 자신을 감소
            area[i][j] = area[i][j] - (diffusion_amount) * diffusion_count

    # 2. 미세먼지 확산 이후 증가 더하기
    for key in diffusion_after_adding.keys():
        i, j = key
        area[i][j] += diffusion_after_adding[key]

    # 3. 공기청정기의 가동
    top_cleaner = cleaner[0]
    bottom_cleaner = cleaner[1]

    ti, tj = top_cleaner
    for i in range(ti - 1, 0, -1):
        area[i][0] = area[i - 1][0]

    for j in range(0, C - 1):
        area[0][j] = area[0][j + 1]

    for i in range(0, ti):
        area[i][C - 1] = area[i + 1][C - 1]

    for j in range(C - 1, 0, -1):
        area[ti][j] = area[ti][j - 1]
    area[ti][tj + 1] = 0

    bi, bj = bottom_cleaner
    for i in range(bi + 1, R - 1):
        area[i][0] = area[i + 1][0]

    for j in range(0, C - 1):
        area[R - 1][j] = area[R - 1][j + 1]

    for i in range(R - 1, bi, -1):
        area[i][C - 1] = area[i - 1][C - 1]

    for j in range(C - 1, 1, -1):
        area[bi][j] = area[bi][j - 1]
    area[bi][bj + 1] = 0

    # 공기청정기 순환 후 dust 교체
    new_dust = []
    for i in range(R):
        for j in range(C):
            if area[i][j] > 0:
                new_dust.append([i, j])
    dust = new_dust

dust_all = 0
for i in range(R):
    for j in range(C):
        if area[i][j] > 0:
            dust_all += area[i][j]
print(dust_all)
