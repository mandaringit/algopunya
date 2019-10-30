import sys

sys.stdin = open('sample_input.txt', 'r')


def check_time(arrive_times, stair_length):
    arrive_times.sort()
    stair_state = [0] * 1000

    last_time = 0
    for idx, time in enumerate(arrive_times):
        in_time = time + 1
        while True:
            if stair_state[in_time] < 3:
                for k in range(in_time, in_time + stair_length):
                    stair_state[k] += 1

                if idx == len(arrive_times) - 1:
                    last_time = in_time + stair_length
                break
            else:
                in_time += 1

    return last_time


T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    room = [list(map(int, input().split())) for _ in range(N)]

    peoples = []
    stairs = []

    min_time = 1000000000
    for i in range(N):
        for j in range(N):
            if room[i][j] == 1:
                peoples.append((i, j))

            if room[i][j] > 1:
                stairs.append((i, j, room[i][j]))

    stair1 = stairs[0]
    stair2 = stairs[1]
    for i in range(1 << len(peoples)):
        stair1_group = []
        stair2_group = []
        for j in range(len(peoples)):
            p = peoples[j]
            if i & (1 << j):
                arrive_time = abs(stair1[0] - p[0]) + abs(stair1[1] - p[1])
                stair1_group.append(arrive_time)
            else:
                arrive_time = abs(stair2[0] - p[0]) + abs(stair2[1] - p[1])
                stair2_group.append(arrive_time)

        s1 = check_time(stair1_group, stair1[2])
        s2 = check_time(stair2_group, stair2[2])
        result = max(s1, s2)
        if result < min_time:
            min_time = result

    print(f"#{tc} {min_time}")
