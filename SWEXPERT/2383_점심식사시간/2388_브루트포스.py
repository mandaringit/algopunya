import sys

sys.stdin = open('sample_input.txt', 'r')


def check_total_time(move_times, stair_value):
    times = [0]*10000
    last_time = 0
    move_times.sort()
    for idx, time in enumerate(move_times):
        down_time = time+1  # 계단 입구에 도착하면 1분 후 아래칸으로 내려 갈 수 있다.
        while True:
            if times[down_time] < 3:
                for t in range(down_time, down_time+stair_value):
                    times[t] += 1

                if idx == len(move_times)-1:
                    last_time = down_time+stair_value
                break
            else:
                down_time += 1

    return last_time


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    rooms = [list(map(int, input().split())) for _ in range(N)]

    people = []
    stairs = []
    minTime = 10000000
    for i in range(N):
        for j in range(N):
            if rooms[i][j] == 1:
                people.append((i, j))
            if rooms[i][j] > 1:
                stairs.append((i, j, rooms[i][j]))

    M = len(people)
    stair1 = stairs[0]
    stair2 = stairs[1]
    for i in range(1 << M):
        use_stair1_times = []
        use_stair2_times = []
        for j in range(M):
            p = people[j]
            if i & (1 << j):
                move_time = abs(stair1[0]-p[0])+abs(stair1[1]-p[1])
                use_stair1_times.append(move_time)
            else:
                move_time = abs(stair2[0]-p[0])+abs(stair2[1]-p[1])
                use_stair2_times.append(move_time)

        s1_time = check_total_time(use_stair1_times, stair1[2])
        s2_time = check_total_time(use_stair2_times, stair2[2])

        final_time = max(s1_time, s2_time)
        if minTime > final_time:
            minTime = final_time

    print("#{} {}".format(tc, minTime))
