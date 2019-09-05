import sys

sys.stdin = open('input.txt', 'r')


def is_right_index_range(i, j, d):
    global room

    ni = i
    nj = j

    # 0 : -> / 1: V / 2: 대각
    if d == 0:
        nj += 1
    elif d == 1:
        ni += 1
    elif d == 2:
        ni += 1
        nj += 1

    # 갈 수 있는 범위 및 벽이 아닌곳
    if 0 <= ni < N and 0 <= nj < N and room[ni][nj] != 1:
        if d == 2:  # 대각선일 때는 대각선 위치의 좌 , 상 확인
            if room[ni][nj - 1] == 0 and room[ni - 1][nj] == 0:
                return True
            else:
                return False
        return True
    return False


def infinity_pipe(x, y, current_direction):
    global count
    global N

    if (x, y) == (N - 1, N - 1):
        count += 1
    else:
        # 가로상태
        if current_direction == 0:
            for i in [0, 2]:
                if is_right_index_range(x, y, i):  # 가능하면
                    if i == 0:
                        infinity_pipe(x, y + 1, i)
                    elif i == 2:
                        infinity_pipe(x + 1, y + 1, i)

        # 세로 상태일때
        elif current_direction == 1:
            for i in [1, 2]:
                if is_right_index_range(x, y, i):  # 가능하면
                    if i == 0:
                        infinity_pipe(x + 1, y, i)
                    elif i == 2:
                        infinity_pipe(x + 1, y + 1, i)
                else:
                    return

        # 대각선 상태일때
        elif current_direction == 2:
            for i in [0, 1, 2]:
                if is_right_index_range(x, y, i):  # 가능하면
                    if i == 0:
                        infinity_pipe(x, y + 1, i)
                    elif i == 1:
                        infinity_pipe(x + 1, y, i)
                    elif i == 2:
                        infinity_pipe(x + 1, y + 1, i)
                else:
                    return


T = int(input())

for tc in range(1, T + 1):
    N = int(input())

    room = [list(map(int, input().split())) for _ in range(N)]

    count = 0

    infinity_pipe(0, 1, 0)

    print(count)
