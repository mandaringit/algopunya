import sys

sys.stdin = open('input.txt', 'r')

# 네 점을 확정짓는다
# 네 점에 따른 구역 구분을 통해 각 영역을 구한다
# 5번 구역은 전체에서 나머지를 뺀 값이다.
# 값 비교.

def is_range_ok(i, j):
    return 0 <= i < N and 0 <= j < N


def get_area(i1, j1, i2, j2, i3, j3, i4, j4):
    global city, N
    # 1구역
    area1 = 0
    J1 = j1+1
    for i in range(0, i4):  # 0 ~ i4 -1
        if i >= i1:
            J1 -= 1  # j1 1 ~  . . . 1씩 감소
        area1 += sum(city[i][:J1])

    # 2구역
    area2 = 0
    J2 = j1+1
    for i in range(0, i2+1):  # 0 ~ i2
        if i >= i1+1:
            J2 += 1  # j1 +1 ~ 1씩 증가
        area2 += sum(city[i][J2:])

    # 3구역
    area3 = 0
    J3 = j4-1
    for i in range(i4, N):  # i4 ~ 끝까지
        if i <= i3:
            J3 += 1
        area3 += sum(city[i][:J3])

    # 4구역
    area4 = 0
    J4 = j2+1
    for i in range(i2+1, N):
        if i <= i3+1:
            J4 -= 1
        area4 += sum(city[i][J4:])

    area5 = total-(area1+area2+area3+area4)

    areas = [area1, area2, area3, area4, area5]
    return max(areas)-min(areas)


N = int(input())
city = [list(map(int, input().split())) for _ in range(N)]

total = 0
for i in range(N):
    total += sum(city[i])

minDiff = total
# 시작점 설정
for i1 in range(0, N-2):
    for j1 in range(1, N-1):
        for d1 in range(1, N):
            # 두번째 점 설정
            i2 = i1+(1*d1)
            j2 = j1+(1*d1)
            if is_range_ok(i2, j2):
                for d2 in range(1, N):
                    # 세번째 점 설정
                    i3 = i2+(1*d2)
                    j3 = j2+(-1*d2)
                    if is_range_ok(i3, j3):
                        # 네번째 점 확정
                        i4 = i3+(-1*d1)
                        j4 = j3+(-1*d1)
                        if is_range_ok(i4, j4):
                            diff = get_area(i1, j1, i2, j2, i3, j3, i4, j4)

                            if diff < minDiff:
                                minDiff = diff
print(minDiff)
