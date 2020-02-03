import sys

sys.stdin = open('input.txt', 'r')

R, C, M = map(int, input().split())
water = {}
# 상어 정보
for _ in range(M):
    r, c, s, d, z = map(int, input().split())
    water[(r - 1, c - 1)] = [s, d, z]

getSize = 0

# 0 ~ C 까지 돈다.
for j in range(C):
    # 낚시왕이 있는 열의 상어 중 땅과 제일 가까운 (i가 가장 작은)
    # 상어 겟. => 상어 소멸
    for i in range(0, R):
        # 뭔가 있으면
        value = water.get((i, j))
        if value:
            size = value[2]
            # 잡는다
            getSize += size
            # 소멸시킨다.
            del water[(i, j)]
            break
    # 상어들이 이동한다.
    new_water = {}
    for shark in water.keys():
        r, c = shark
        d = [(), (-1, 0), (1, 0), (0, 1), (0, -1)]  # 상1하2우3좌4
        speed, direction, size = water[shark]
        dx, dy = d[direction]
        # 이하 비효율적인부분 ㅋ
        T = 0
        while T != speed:
            T += 1
            nr = r + dx
            nc = c + dy

            if 0 <= nr < R and 0 <= nc < C:
                r, c = nr, nc
            else:
                if direction == 1:
                    direction = 2
                elif direction == 2:
                    direction = 1
                elif direction == 3:
                    direction = 4
                elif direction == 4:
                    direction = 3

                dx, dy = d[direction]
                nr = r + dx
                nc = c + dy
                r, c = nr, nc

        if new_water.get((r, c)):
            if size > new_water.get((r, c))[2]:
                new_water[(r, c)] = (speed, direction, size)
        else:
            new_water[(r, c)] = (speed, direction, size)
    water = new_water
print(getSize)
