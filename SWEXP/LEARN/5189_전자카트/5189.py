import sys

sys.stdin = open('sample_input.txt', 'r')


def permutation(n, k):
    global N
    global manage_areas
    global min_consume

    if n == k:
        case = [0] + manage_areas + [0]
        total_consume = 0
        for i in range(N):
            place1 = case[i]
            place2 = case[i + 1]
            battery_consume = field[place1][place2]
            total_consume += battery_consume

        if total_consume < min_consume:
            min_consume = total_consume
    else:
        for i in range(n, k):
            manage_areas[n], manage_areas[i] = manage_areas[i], manage_areas[n]
            permutation(n + 1, k)
            manage_areas[n], manage_areas[i] = manage_areas[i], manage_areas[n]


T = int(input())

for tc in range(1, T + 1):
    N = int(input())

    field = [list(map(int, input().split())) for _ in range(N)]
    manage_areas = [i for i in range(1, N)]

    min_consume = 100 * N
    permutation(0, N - 1)

    print("#{} {}".format(tc, min_consume))
