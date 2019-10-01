import sys

sys.stdin = open('sample_input.txt', 'r')

T = int(input())

for tc in range(1, T + 1):
    N = int(input())

    rooms = [list(map(int, input().split())) for _ in range(N)]

    peoples = []
    stairs = []
    for i in range(N):
        for j in range(N):
            if rooms[i][j] == 1:
                peoples.append([i, j])

            if rooms[i][j] >= 2:
                stairs.append([i, j, rooms[i][j]])

    minV = 10000
    for i in range(0, 1 << len(peoples)):
        s1_group = []
        s1_step = stairs[0][2]
        s2_group = []
        s2_step = stairs[1][2]
        for j in range(len(peoples)):
            if i & (1 << j):
                # 0번계단 쓰기
                d = abs(stairs[0][0] - peoples[j][0]) + abs(stairs[0][1] - peoples[j][1])
                s1_group.append(d)
            else:
                # 다른 사람들은 1번계단 쓰기
                d = abs(stairs[1][0] - peoples[j][0]) + abs(stairs[1][1] - peoples[j][1])
                s2_group.append(d)

        s1_group.sort()
        s2_group.sort()

        t1 = [0] * 100
        last_t1 = 0
        for t in s1_group:
            cnt = 0
            time = t + 1
            while cnt < s1_step:
                if t1[time] < 3:
                    t1[time] += 1
                    time += 1
                    cnt += 1
                else:
                    time += 1
            last_t1 = time

        t2 = [0] * 100
        last_t2 = 0
        for t in s2_group:
            cnt = 0
            time = t + 1
            while cnt < s2_step:
                if t2[time] < 3:
                    t2[time] += 1
                    time += 1
                    cnt += 1
                else:
                    time += 1
            last_t2 = time

        total_time = max(last_t1, last_t2)
        if total_time < minV:
            minV = total_time

    print("#{} {}".format(tc, minV))
