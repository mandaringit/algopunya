import sys

sys.stdin = open('input.txt', 'r')


def is_left(i, j, ladder):
    ni = i
    nj = j - 1
    return 0 <= ni < 100 and 0 <= nj < 100 and ladder[ni][nj] == 1


def is_right(i, j, ladder):
    ni = i
    nj = j + 1
    return 0 <= ni < 100 and 0 <= nj < 100 and ladder[ni][nj] == 1


def is_wall(i, j, ladder, d):
    ni = i + d[0]
    nj = j + d[1]

    # 범위 안인데 0이거나,
    if 0 <= ni < 100 and 0 <= nj < 100 and ladder[ni][nj] == 0:
        return True
    # 범위 밖일때
    elif 0 > ni or ni >= 100 or 0 > nj or nj >= 100:
        return True

    return False


def go_reverse_ladder(i, j, ladder):
    d = (-1, 0)

    while i != 0:

        if d == (-1, 0):
            if is_left(i, j, ladder):
                d = (0, -1)
            elif is_right(i, j, ladder):
                d = (0, 1)
        else:
            if is_wall(i, j, ladder, d):
                d = (-1, 0)

        i += d[0]
        j += d[1]

    return j


for tc in range(1, 11):
    tc_num = int(input())

    ladder = [list(map(int, input().split())) for _ in range(100)]

    for j in range(100):
        # 역으로 스타트
        i = 99
        if ladder[i][j] == 2:
            print(f"#{tc} {go_reverse_ladder(i, j, ladder)}")
